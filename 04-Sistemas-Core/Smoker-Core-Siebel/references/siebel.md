> **Nakamas adaptation (2026-08-04).** Schema hub preserved; hosts sanitized to placeholders; no passwords. Live SQL expert: `smoker-core-siebel` under `iceburg-director-sistemas-core`. ≠ Crocus/Tom/Kaku; ≠ Tripulación `brd-*`.

# Siebel CRM (Oracle QA) — schema map (clientes / party)

**Core:** Siebel CRM — clientes / party Banreservas  
**Environment:** Oracle QA (`PCRMIP14` / service `uatip22`)  
**Explored:** 2026-07-27 (read-only, `oracledb` thin)  
**Primary consumers:** `ms-party-information-query`, `ms-inquiry-parameters`, `ms-customer-event-history-integration`, `nexo-cuenta-automation`, lab `OracleCrm` (`CLIENTESACTIVOS`)  
**Catalog size:** **SIEBEL** ~5521 tables / 41 views; **BROKER** 103 tables / 91 views (prefer BROKER for agent SQL)

SOAP/EAI endpoints (`srvlazcrmwq1…/siebel/app/eai*`) are **not** this JDBC DB; they are the application tier. This doc is the **Oracle CRM DB**.

---

## 1. Purpose

CRM/party source of truth for **physical (PF) and legal (PJ) clients**: identity documents, CIF, contact channels, addresses, status/condition, employee/PEP flags, and **product-system linkage** (Cadencie / SGN / SFB via assets). Cross-core join to cards cores is almost always **document number (`IDENTIFICACION` / `SOC_SECURITY_NUM`)** and/or **`CIF`**, plus optional Way4 client id on extensions.

Not Cadencie, Way4 issuing, Cortex debit, or ACard.

---

## 2. Connection summary (no password)

| Field | Value |
|-------|--------|
| Host | `<HOST_PRIVATE_SIEBEL>` |
| Port | `1521` |
| Service | `uatip22.sndb.vcndev.oraclevcn.com` |
| DB name (session) | `PCRMIP14` |
| Preferred user | `broker` (owns `BROKER.*` views; used by party-query) |
| Alternate user | `crmcert` (inquiry-parameters / nexo / card-nexus CRM keys) |
| JDBC | `jdbc:oracle:thin:@//<HOST_PRIVATE_SIEBEL>:1521/uatip22.sndb.vcndev.oraclevcn.com` |
| Preferred client | Python `oracledb` thin or `sqlplus` EZCONNECT |
| Credential source (broker) | `iac/iac-onpremise-dev-qa/aks-cluster/apps/integraciones/overlays/qa/secret/ms-party-information-query.env` — keys `quarkus.datasource.username` / `quarkus.datasource.password` (+ JDBC URL in same file). Same under `des/secret/`. |
| Credential source (crmcert) | `…/qa/secret/ms-inquiry-parameters.env` or `…/qa/secret/nexo-cuenta-automation.env` (`ORACLE_CRM_*` / `quarkus.datasource.*`). |
| Lab mirror | `pruebas_automatizadas/test-innovations-labs/.env` — `CRM_DB_URL` / `CRM_DB_USER` / `CRM_DB_PASSWORD` (comment: `CLIENTESACTIVOS`). **Do not copy passwords into skill files.** |
| Network | Private IP — **corporate VPN required**. Timeout → stop and report VPN. |

```bash
# After loading CRM_USER / CRM_PASS from secret (never echo)
python3 -c "import oracledb,os; c=oracledb.connect(user=os.environ['CRM_USER'],password=os.environ['CRM_PASS'],dsn='<HOST_PRIVATE_SIEBEL>:1521/uatip22.sndb.vcndev.oraclevcn.com',tcp_connect_timeout=8); print(c.version); c.close()"
```

See also: [Iceburg connections](../../Iceburg-Director-Sistemas-Core/references/connections.md), [protocolo compartido](../../Iceburg-Director-Sistemas-Core/skills/consultar-cores-bancarios-sql/SKILL.md).

---

## 3. Key schemas / owners

| Owner | Role | Footprint (approx) |
|-------|------|--------------------|
| **BROKER** | Integration / EAI layer — **preferred for agents**. Client views `VW_CLI_*`, `VI_DETALLE_CLIENTES`, table `CLIENTESACTIVOS`. | 103 tables, 91 views, 129 procedures |
| **SIEBEL** | Native Siebel base (`S_*`) + Banreservas extensions (`CX_*`, `X_*` columns). | ~5521 tables, 41 views |
| **SIEBELREV** | Revision/history sibling schema. | ~5100 tables |
| **APPSBROKER** | Synonyms only (3). | — |

Login as `broker` → session user `BROKER`. Qualify Siebel objects as `SIEBEL.*`.

Stats (ALL_TABLES.NUM_ROWS, analyzed ~2026-01…07):

| Object | ~Rows |
|--------|-------|
| `BROKER.CLIENTESACTIVOS` | 5.39M |
| `BROKER.UNIVERSOIDENT` | 5.65M |
| `SIEBEL.S_CONTACT` | 3.97M |
| `SIEBEL.S_CONTACT_X` | 3.97M |
| `SIEBEL.S_PARTY` | 4.08M |
| `SIEBEL.S_ADDR_PER` | 8.03M |
| `SIEBEL.S_ORG_EXT` | 53K |
| `SIEBEL.CX_DOCUMENTOS` | 14K (doc **catalog**/requirements — not customer ID numbers) |
| `SIEBEL.CX_ID_PF` | **0** (empty on this QA; do not rely on it) |

---

## 4. Client model (join spine)

Prefer **BROKER views** (already PF∪PJ). Under the hood for PF detail:

```
SIEBEL.S_CONTACT c                    -- party person (ROW_ID)
  ├── S_CONTACT_FNX d                 -- IDEN_TYPE_CD, birth place, … (d.ROW_ID = c.ROW_ID or PAR_ROW_ID)
  ├── S_CONTACT_X e                   -- Banreservas attrs (e.PAR_ROW_ID = c.ROW_ID); X_CLIENTID_W4 → Way4
  ├── S_CON_ADDR / S_ADDR_PER         -- primary address (c.PR_PER_ADDR_ID)
  ├── S_PARTY                         -- party root (ROW_ID = contact/org)
  ├── S_ASSET_CON → S_ASSET → S_PROD_INT   -- products → SISTEMA (CADENCIE/SGN/SFB)
  └── (PJ) S_ORG_EXT                  -- legal entity; OU_NUM / TAX_IDEN_NUM / X_CIF / X_IDEN_TYPE_CD
```

**Document ↔ cores**

| Field | Where | Use |
|-------|--------|-----|
| `IDENTIFICACION` | BROKER views; = `S_CONTACT.SOC_SECURITY_NUM` (PF) or org number (PJ) | **Primary cross-core key** to Cadencie `custr_nbr`, Way4 `REG_NUMBER`, ACard `Numero_Identificacion` |
| `CIF` | `VI_DETALLE` / `VW_CLI_IDENTIFICACION` / `S_CONTACT.X_CIF` / `S_ORG_EXT.X_CIF` | Internal CRM customer number |
| `ROW_ID_CLIENTE` / `ROW_ID` | BROKER; = `S_CONTACT.ROW_ID` or org `ROW_ID` | Siebel party key |
| `TIPO_IDENTIFICACION` | From `S_CONTACT_FNX.IDEN_TYPE_CD` (PF) or `S_ORG_EXT.X_IDEN_TYPE_CD` (PJ) | Doc type label |
| `TIPO_PERSONA` | `PF` / `PJ` | Person vs company |
| `X_CLIENTID_W4` | `S_CONTACT_X` | Optional Way4 client id |
| `SISTEMA` | `VW_CLI_SISTEMAS_RELACIONADOS` | Derived: `CADENCIE` / `SGN` / `SFB` from asset number length + product type |

**Mask docs** in all outputs: e.g. `01*******45` (keep first 2 + last 2). Never dump full cédula/RNC lists into vault/skill notes.

---

## 5. Important BROKER objects (agent-first)

### 5.1 `BROKER.CLIENTESACTIVOS` (table)

Active-client probe used by lab automation.

| Column | Type | Meaning |
|--------|------|---------|
| `IDENTIFICACION` | VARCHAR2(100) | Document number |
| `NOMBRECOMPLETO` | VARCHAR2(200) | Display name |

```sql
SELECT 1 AS FOUND
FROM BROKER.CLIENTESACTIVOS
WHERE IDENTIFICACION = :doc
FETCH FIRST 1 ROW ONLY;
```

### 5.2 `BROKER.VI_DETALLE_CLIENTES` (view)

Rich client profile (PF∪PJ). Key columns:

| Column | Meaning |
|--------|---------|
| `ROW_ID_CLIENTE` | Siebel `ROW_ID` |
| `IDENTIFICACION` | Doc number |
| `CIF` | CRM CIF |
| `TIPO_IDENTIFICACION` / `TIPO_IDENTIFICACION_NUM` | Type label + numeric decode |
| `PRIMER_NOMBRE` … `SEGUNDO_APELLIDO`, `SEXO`, `FECHA_NACIMIENTO` | Demographics |
| `TIPO_CLIENTE`, `TIPO_PERSONA`, `ESTADO_CLIENTE`, `CONDICION_CLIENTE`, `SUBESTADO_CLIENTE` | Segment / lifecycle |
| `ES_EMPLEADO_GRUPO`, `CODIGO_EMPLEADO`, `SEGMENTO_CLIENTE` | Employee / segment |
| `CODIGO_PAIS_ORIGEN`, `ES_EXTRANJERO`, `ESTA_EN_LISTA_NEGRA` | Risk / residency flags |

Join: `ROW_ID_CLIENTE = SIEBEL.S_CONTACT.ROW_ID` (PF path).

### 5.3 Identity & channel views

Most `VW_CLI_*` are `PF UNION ALL PJ` wrappers.

| View | Role | Join key |
|------|------|----------|
| `VW_CLI_IDENTIFICACION` | Doc + type + CIF | `IDENTIFICACION` |
| `VW_CLI_DATOS_GENERALES` | Full general data (`ROW_ID`, status, occupation, …) | `IDENTIFICACION` / `ROW_ID` |
| `VW_CLI_CORREOS` | Emails (`DIRECCION`, `ESPRINCIPAL`) | `IDENTIFICACION` |
| `VW_CLI_TELEFONOS` | Phones (`NUMERO`, `TIPO`, `ESPRINCIPAL`) | `IDENTIFICACION` |
| `VW_CLI_DIRECCIONES` | Addresses (calle/ciudad/sector/…) | `IDENTIFICACION` |
| `VW_CLI_SISTEMAS_RELACIONADOS` | Product cores (`SISTEMA`, `TIPOSPRODUCTOS`) | `IDENTIFICACION` |
| `EAI_VW_CLI_*` | EAI-oriented twins of the above | same |

`TIPO_PERSONA` distinct: **PF** ~3.97M, **PJ** ~53K.

Observed `TIPO_IDENTIFICACION` labels (catalog, not PII): Cédula, Pasaporte, Menor de edad, RNC, Otros, …

### 5.4 `BROKER.T001_TIPOS_DOCUMENTOS_IDENTIDAD_SB`

| CODIGO | DESCRIPCION |
|--------|-------------|
| 1 | Cédula de identidad y electoral o NUI |
| 2 | Cédula para extranjeros |
| 3 | Identificación local del país extranjero |
| 4 | Pasaporte |
| 5 | Registro nacional del contribuyente |
| 6 | Número de identificación fiscal extranjero |

---

## 6. Important SIEBEL tables

### 6.1 `SIEBEL.S_CONTACT` — person

| Column | Meaning |
|--------|---------|
| `ROW_ID` | PK; = BROKER `ROW_ID_CLIENTE` |
| `PAR_ROW_ID` | Party link |
| `SOC_SECURITY_NUM` | **Primary document number (PF)** |
| `X_CIF` | CIF |
| `FST_NAME` / `MID_NAME` / `LAST_NAME` / `MAIDEN_NAME` | Names |
| `SEX_MF`, `BIRTH_DT`, `MARITAL_STAT_CD` | Demographics |
| `EMAIL_ADDR`, `CELL_PH_NUM`, `HOME_PH_NUM`, `WORK_PH_NUM` | Contacts (prefer BROKER phone/email views) |
| `CUST_STAT_CD` | Estado cliente (e.g. ACTIVO, CANCELADO, CREADO) |
| `CUST_VALUE_CD` | Condición cliente |
| `STATUS_CD`, `INTEGRATION_ID`, `PERSON_UID` | Status / integration |
| `PR_PER_ADDR_ID`, `PR_POSTN_ID` | Primary address / position |
| `X_RNC`, `X_SEG_ID` | RNC / segment FK |

### 6.2 `SIEBEL.S_CONTACT_FNX` — identity extension

| Column | Meaning |
|--------|---------|
| `ROW_ID` / `PAR_ROW_ID` | Aligns to contact |
| `IDEN_TYPE_CD` | Doc type label used by BROKER views |
| `IDEN_NUM` / `IDEN_EXP_DT` | Alternate id / expiry |
| `BIRTH_PLACE` | Birth place |

### 6.3 `SIEBEL.S_CONTACT_X` — Banreservas extension

| Column | Meaning |
|--------|---------|
| `PAR_ROW_ID` | → `S_CONTACT.ROW_ID` |
| `X_CLIENTID_W4` | Way4 client id (when populated) |
| `X_COD_EMPLEADO` / `X_EMP_GRUPO` | Employee group |
| `X_ESTADO_DEL_CLIENTE` / `X_ESTADO_IDENTIFICACION` | Extra status |
| `X_TIPO_DISCAPACIDAD`, PEP / FATCA attrs | Compliance |
| Many `ATTRIB_*` / `X_ATTRIB_*` | Mapped in `VI_DETALLE_CLIENTES` (tipo persona, actividad económica, listas, …) |

### 6.4 `SIEBEL.S_ORG_EXT` — account / PJ

| Column | Meaning |
|--------|---------|
| `ROW_ID` | Org PK |
| `NAME`, `OU_NUM` | Name / org number |
| `TAX_IDEN_NUM` | Tax id |
| `X_CIF`, `X_IDEN_TYPE_CD` | CIF / id type (often `RNC`) |
| `STATUS_CD`, `MAIN_EMAIL_ADDR`, `MAIN_PH_NUM` | Status / contacts |
| `PR_CON_ID` | Primary contact |

### 6.5 Party / address / products

| Object | Role |
|--------|------|
| `S_PARTY` | Party root (`PARTY_TYPE_CD`, `PARTY_UID`, `NAME`) |
| `S_ADDR_PER` + `S_CON_ADDR` | Addresses linked to contacts |
| `S_ASSET` + `S_ASSET_CON` + `S_PROD_INT` | Owned products; drives `VW_CLI_SISTEMAS_RELACIONADOS` |
| `CX_DOCUMENTOS` | Document **requirement** catalog (OnBase metadata) — not cédula store |
| `CX_ID_PF` | Intended PF id store — **empty on this QA**; use `SOC_SECURITY_NUM` + `S_CONTACT_FNX` |

**SISTEMA derivation** (`VW_CLI_SISTEMAS_RELACIONADOS_PF`):

- `LENGTH(ASSET_NUM)=10` → `SGN`
- `LENGTH>10` and product ≠ `Tarjetas de crédito` → `SFB`
- `LENGTH>10` and product = `Tarjetas de crédito` → `CADENCIE`

Observed product types include: Cuentas de ahorro/corrientes, Certificados, Préstamos, Tarjetas de crédito.

---

## 7. Query patterns (5–10)

Mask `IDENTIFICACION` in result sets. Bind `:doc` / `:cif` / `:row_id`.

**1. Active client by document**

```sql
SELECT 1 AS FOUND
FROM BROKER.CLIENTESACTIVOS
WHERE IDENTIFICACION = :doc
FETCH FIRST 1 ROW ONLY;
```

**2. Profile header**

```sql
SELECT ROW_ID_CLIENTE, CIF, TIPO_IDENTIFICACION, TIPO_PERSONA,
       ESTADO_CLIENTE, CONDICION_CLIENTE, SEGMENTO_CLIENTE
FROM BROKER.VI_DETALLE_CLIENTES
WHERE IDENTIFICACION = :doc
FETCH FIRST 1 ROW ONLY;
```

**3. Resolve CIF → document type**

```sql
SELECT IDENTIFICACION, TIPO_IDENTIFICACION, TIPO_PERSONA, CIF
FROM BROKER.VW_CLI_IDENTIFICACION
WHERE CIF = :cif;
```

**4. Channels (email / phone / address)**

```sql
SELECT DIRECCION, ESPRINCIPAL FROM BROKER.VW_CLI_CORREOS WHERE IDENTIFICACION = :doc;
SELECT NUMERO, TIPO, ESPRINCIPAL FROM BROKER.VW_CLI_TELEFONOS WHERE IDENTIFICACION = :doc;
SELECT CALLE, CIUDAD, PROVINCIA, SECTOR, TIPODIRECCION, ESPRINCIPAL
FROM BROKER.VW_CLI_DIRECCIONES WHERE IDENTIFICACION = :doc;
```

**5. Which product cores does the client have?**

```sql
SELECT SISTEMA, TIPOSPRODUCTOS
FROM BROKER.VW_CLI_SISTEMAS_RELACIONADOS
WHERE IDENTIFICACION = :doc;
```

**6. Siebel contact + Way4 id**

```sql
SELECT c.ROW_ID, c.X_CIF, c.CUST_STAT_CD, x.X_CLIENTID_W4
FROM SIEBEL.S_CONTACT c
LEFT JOIN SIEBEL.S_CONTACT_X x ON x.PAR_ROW_ID = c.ROW_ID
WHERE c.SOC_SECURITY_NUM = :doc;
```

**7. PJ by RNC / tax id**

```sql
SELECT ROW_ID, NAME, X_CIF, X_IDEN_TYPE_CD, STATUS_CD
FROM SIEBEL.S_ORG_EXT
WHERE TAX_IDEN_NUM = :rnc OR OU_NUM = :rnc OR X_CIF = :cif;
```

**8. Doc-type catalog**

```sql
SELECT CODIGO, DESCRIPCION
FROM BROKER.T001_TIPOS_DOCUMENTOS_IDENTIDAD_SB
ORDER BY CODIGO;
```

**9. Bridge BROKER → native contact**

```sql
SELECT d.ROW_ID_CLIENTE, d.CIF, d.ESTADO_CLIENTE, c.CUST_STAT_CD
FROM BROKER.VI_DETALLE_CLIENTES d
JOIN SIEBEL.S_CONTACT c ON c.ROW_ID = d.ROW_ID_CLIENTE
WHERE d.IDENTIFICACION = :doc;
```

**10. Cadencie-linked clients (via related systems)**

```sql
SELECT IDENTIFICACION, TIPOSPRODUCTOS
FROM BROKER.VW_CLI_SISTEMAS_RELACIONADOS
WHERE SISTEMA = 'CADENCIE'
FETCH FIRST 50 ROWS ONLY;
-- Then join card cores by IDENTIFICACION (masked in outputs).
```

---

## 8. Cross-core linking cheat sheet

| Target core | Join from Siebel/BROKER |
|-------------|-------------------------|
| **Cadencie** | `IDENTIFICACION` ↔ `CARD`/`CUSTR` customer doc (`custr_nbr`); confirm via `SISTEMA='CADENCIE'` |
| **Way4** | Doc ↔ `OWS.CLIENT.REG_NUMBER`; optional `S_CONTACT_X.X_CLIENTID_W4` ↔ Way4 client id |
| **Cortex** | Doc ↔ customer id tables (`CUSTDET` / id codes) — validate live |
| **ACard** | Doc ↔ `Solicitud_Gestion.Numero_Identificacion` |

---

## 9. Safety / agent notes

- Default **read-only** `SELECT` / dictionary only.
- Prefer **`BROKER.VW_CLI_*` / `VI_DETALLE_CLIENTES` / `CLIENTESACTIVOS`** over raw `SIEBEL.S_*` unless you need extension columns.
- **Never** persist passwords, full docs, emails, or phones in vault/skill artifacts.
- Full-table `COUNT(*)` / unfiltered `GROUP BY` on multi-million views can hang — use binds + `FETCH FIRST` / `ROWNUM` samples.
- SOAP CRM URLs in IAC are separate from this JDBC connection.
