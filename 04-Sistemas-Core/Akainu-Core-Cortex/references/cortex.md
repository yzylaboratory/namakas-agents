> **Nakamas adaptation (2026-08-04).** Schema hub preserved; hosts sanitized to placeholders; no passwords. Live SQL expert: `akainu-core-cortex` under `iceburg-director-sistemas-core`. ≠ Crocus/Tom/Kaku; ≠ Tripulación `brd-*`.

# Cortex Oracle QA — debit-card schema

Read-only inventory for Banreservas **tarjetas de débito** (Cortex PCI). Captured **2026-07-27** against QA.

Companion machine index: [cortex.index.json](cortex.index.json). Protocol: [protocolo compartido](../../Iceburg-Director-Sistemas-Core/skills/consultar-cores-bancarios-sql/SKILL.md), endpoints: [Iceburg connections](../../Iceburg-Director-Sistemas-Core/references/connections.md).

## Connection

| Field | Value |
|-------|--------|
| Host | `<HOST_PRIVATE_CORTEX>:1521` |
| Service | `cfisqa_pctx19qa.paas.oracle.com` |
| DB / service ctx | `PCTX19QA` / `CFISQA_PCTX19QA.paas.oracle.com` |
| User | `cortexpci_uat` (schema `CORTEXPCI_UAT`) |
| Credential source | IAC secret `…/overlays/qa/secret/ms-debit-card-inquiries.env` or `ms-debit-card-device-query.env` (`quarkus.datasource.username` / `quarkus.datasource.password`) |
| Consumers | `ms-debit-card-inquiries`, `ms-debit-card-device-query`, `ms-debit-cards` |

**Never** write passwords into this file. VPN required for private core hosts.

## Schema footprint

| Owner | Tables | Notes |
|-------|--------|--------|
| `CORTEXPCI_UAT` | **1200** | Primary app schema for MS access |
| `CORTEXPCI_UAT` excl. `SP28_%` | **601** | `SP28_*` = snapshot/backup copies — ignore for agents |
| `CORTEXPCI` | 45 | Parallel/legacy objects |
| `DBBROKER` / `BROKER` | 47 each | EAI broker helpers |

Procedures in `CORTEXPCI_UAT`: **114**.

## Domain model (joins)

```text
CUSTIDTYPE ──< CUSTIDCODE >── CUSTDET ──< CRDDET >── CRDPRODUCT
                                 │          │
                                 │          ├── STATCODE → CRDSTATUS
                                 │          ├── PINSTATUS_ID → PINSTATUS
                                 │          ├── BRANCH_ID → BRANCH
                                 │          ├── ACCDET_ID → ACCDET (primary / "Designada")
                                 │          └── ID ← CRDACC → ACCDET (N:M linked accounts)
                                 │
                                 └── ACCDET (accounts; TYPECODE 10=AHORRO, 20=CORRIENTE)

CRDDET.ID ← CRDLIMIT / CRDPIN / CRDEVENT / CDSTHST / TOKEN
CRDPRODUCT.ID ← CRDPRODLIM
VPANDET → VPAN_STATUS / VPAN_PROFILE / VPAN_BATCH
TERMATM / TERMPOS / ATMDEF / POSDEF  (acquiring terminals — "device" infra)
TOKEN.DEVID / DEVTYPE / DEVNAME      (wallet / digital device — tokenization)
```

**PAN handling (agents):**

- `CRDDET.PAN` — stored card identifier used by EAI SPs as lookup key (often tokenized/internal; treat as **secret**).
- `CRDDET.PAN_DISPLAY` — display form; **always mask** as `BIN******LAST4` in outputs.
- Unique business key: `(PAN, SEQNO)` (`HASH_CRDDET`). PK: `CRDDET.ID`.

## Key tables

### Cards / accounts / customers

| Table | PK / unique | Role | Approx rows (QA) |
|-------|-------------|------|------------------|
| `CRDDET` | `ID`; UK `(PAN,SEQNO)` | Card master: product, status, expiry, emboss, primary `ACCDET_ID`, `CUSTDET_ID` | 2 581 |
| `ACCDET` | `ID`; UK `(INST_ID,ACCNO,CURRCODE)` | Account master: `ACCNO`, `TYPECODE`, balances, `STATCODE` | 6 736 |
| `CRDACC` | `(CRDDET_ID,ACCDET_ID)` | Card↔account link (`TYPECODE`, `ISOCODE`, `PRIORITY`) | ~594 |
| `CUSTDET` | `ID`; UK `(INST_ID,CUSTCODE)` | Customer profile (PII — do not dump) | ~661 |
| `CUSTIDCODE` | `ID`; UK `(IDTYPE_ID,IDCODE)`; UK `CUSTDET_ID` | Document ↔ customer | ~641 |
| `CUSTIDTYPE` | `ID` | Doc types: `6` Cédula, `4` Pasaporte, `3` RNC | 3 |
| `BRANCH` | `ID` | Branch (`BRNCODE`, `DESCR`) | 407 |

### Catalogs — product / status

| Table | Key | Role |
|-------|-----|------|
| `CRDPRODUCT` | `ID`; UK `CRDPRODUCT` (4-char code) | Debit products |
| `CRDSTATUS` | `STATCODE` | Card status; `CANCELED` flag; auth `ACTIONCODE`/`RSPCODE` |
| `CRDSTATUSTRANS` / `CRDSTATUSTRANSSET` | `(STATCODE_FROM,STATCODE_TO)` via set; product FK `CRDPRODUCT.CRDSTATUSTRANSSET_ID` | **Matriz efectiva que aplica BRE** — un solo set (`DEFAULT`, ID 1) para los 9 productos de débito. Desde `00`: `01,03,04,05,06,07,08,15,35,36,50,70,71`. Desde `36`: solo `06,07,36`. Desde `71`: `00` |
| `BRE_CUST_CRDSTATUSTRANS` / `BRE_CUST_CRDSTATUSTRANSSET` | same shape | Solo 2 filas (`00→36`, `36→00`). **No es la matriz que BRE aplica**: live acepta `00↔71` (ausente aquí) y rechaza `36→00` (presente aquí) |
| `STATCHGPERM` + ACS `cdstchg_xxxx` | ACS status-change permission | QA: granted to USRGRP `cortex` only (not `webservice`) |
| `CDSTHST` | card status history | `OLD_STATCODE`→`NEW_STATCODE`, `WHO_SET`, `WHY_SET` |
| `ACCSTATUS` | `STATCODE` | Account status |
| `ACCTYPE` | `(INST_ID,TYPECODE)` | Account types (`10` AHORRO, `20` CORRIENTE, …) |
| `PINSTATUS` | `ID` | PIN lifecycle on card |
| `CRDPRODLIM` | product FK | Product-level cash/purchase limits |
| `CRDLIMIT` | `CRDDET_ID` | Per-card limit counters |
| `CAT_ISSRISK` | `ID`; `CATVALUE` | Issuer risk / transaction-channel allow matrix (Local · International · Internet). Linked from `CRDDET.CAT_ISSRISK_ID`. Used by SOAP `UpdateTransactionBlocking` (`IssRiskId`). |
| `CAT_ISSRISKCNTRL` | `ID` | Issuer-risk control catalog (empty in QA 2026-07-27) |

### Virtual PAN / tokenization / devices

| Table | Role |
|-------|------|
| `VPANDET` | Virtual PANs (`VPAN`, `PAN_DISPLAY`, status/profile/batch FKs) |
| `VPAN_STATUS` | `GENERATED` / `EXTRACTED` / `IN_USE` |
| `VPAN_PROFILE` | Prefix/format for VPAN generation |
| `TOKEN` | Wallet tokens; device cols `DEVID`, `DEVTYPE`, `DEVNAME`, `DEVIPADDRESS` |
| `BRETKNWEBSERV` | BRE token web-service audit (`STATUS` e.g. `APROBADO`) |
| `TERMATM` / `ATMDEF` | ATM terminal instances / models |
| `TERMPOS` / `POSDEF` | POS terminals / models |

### History / activity

| Table | Role |
|-------|------|
| `CDSTHST` | Card status history (`OLD_STATCODE`→`NEW_STATCODE`, `DATE_SET`, `CRDDET_ID`) |
| `CRDEVENT` / `CRDEV_STHSTLK` | Card events / status-history links |
| `TLOG` | Transaction log (`ACNUM1`, `PAN`, dates) — large; filter tightly |

### PCI / mapping helpers

| Table | Notes |
|-------|--------|
| `PANENC` | Encrypted/mapped PAN↔ACCNO helper (treat contents as secret) |
| `BIN` / `BIN_RANGE` | BIN inventory / VPAN ranges (BIN table is huge — avoid full scans) |

## Catalog snapshots (QA 2026-07-27)

### `CAT_ISSRISK` (transaction channel blocking)

`CATVALUE` encodes Locales | Internacionales | Internet as `Si`/`No`. SOAP flags:

- `AllowLocalTransactions` → ATM local
- `AllowInternationalTransactions` → ATM internacional
- `AllowInternetTransactions` → Internet TXN

| ID | CATVALUE | DESCR |
|----|----------|-------|
| 1 | `DEFAULT/NONE` | No Issuer Risk Category Defined |
| 2 | `DEFAULT` | Default Issuer Risk |
| 3 | `NoNoNo` | Locales-No Internacionales-No Internet-No |
| 4 | `NoNoSi` | Locales-No Internacionales-No Internet-Si |
| 5 | `NoSiNo` | Locales-No Internacionales-Si Internet-No |
| 6 | `NoSiSi` | Locales-No Internacionales-Si Internet-Si |
| 7 | `SiNoNo` | Locales-Si Internacionales-No Internet-No |
| 8 | `SiNoSi` | Locales-Si Internacionales-No Internet-Si |
| 9 | `SiSiNo` | Locales-Si Internacionales-Si Internet-No |

Gap: no `SiSiSi` row in QA. Card distribution 2026-07-27: **2580** → id=1, **1** → id=2, **0** → ids 3–9.

BRE: `https://<HOST_PRIVATE_CORTEX>:19084/CRDBASE-WS-BRE/updateTransactionBlocking` (WSDL `.wsdl`). Capacidad BIAN separada: core adapter `ms-debit-card-transaction-blocking` + orch canónico `orch-debit-card-transaction-blocking` (**no** `ms-debit-cards`).

### `CRDPRODUCT`

| ID | Code | Description | `PRODNUM` |
|----|------|-------------|-----------|
| 1 | `MINT` | 536069 INTERNACIONAL. MDS | 6 |
| 3 | `MLCL` | 536058 LOCAL MDS | 2 |
| 4501 | `MDGO` | 529733 GOLD MDS | 9 |
| 6501 | `MDBC` | 529760 NEGOCIOS MDB | 20 |
| 8501 | `MDBP` | 517375 PLATINUM MDBP | 10 |
| 10501 | `TSUP` | TARJETA SUPERVISOR ATM | 0 |
| 16501 | `MDB8` | 50339678 BRE DEBIT MDB8 | 11 |
| 18501 | `BN-8` | 52976033 BIN 8 | 20 |
| 20501 | `MDST` | 223528 LOCAL MDST | 2 |
| 22501 | `MDS2` | 223667 LOCAL MDS2 | 2 |

Currency heuristic in `EAI_DATOSCLIENTE_CORTEX`: BIN `536069` → moneda `2`, else `1`. Account currency decode in account SPs: `214`→`1`, `840`→`2`, `978`→`3`.

### `CRDSTATUS` (selected)

| Code | Descr | Canceled |
|------|-------|----------|
| `00` | NORMAL | 0 |
| `01` | EXCESO_PIN_PERMITIDO | 0 |
| `02` | EMITIDA | 0 |
| `03` | TARJETA_EXPIRADA | 1 |
| `04` | PERDIDA | 1 |
| `05` | ROBADA | 1 |
| `06` | CANCELADA_POR_CLIENT | 1 |
| `07` | CANCELADA_POR_BANCO | 1 |
| `08` | SOSPECHA_FRAUDE | 1 |
| `15` | DETERIORADA | 1 |
| `20` | REEMPLAZADA | 0 |
| `35` | RETENIDA_EN_ATM | 0 |
| `36` | Bloqueo_preventivo (**etiqueta engañosa** — es bloqueo *permanente*, ver abajo) | 0 |
| `70`/`71` | PREVENTIVO / Call_Prevencion (`71` = bloqueo *preventivo* de negocio) | 0 |

QA distribution (top): `02` EMITIDA ≫ `07` cancel banco ≫ `00` NORMAL.

#### `36` vs `71` — semántica de negocio (verificado live 2026-07-28)

El `DESCR` de `CRDSTATUS` **no** refleja la semántica Banreservas. La verdad está en la
reversibilidad de `CRDSTATUSTRANS` (set `DEFAULT`, el único set real, usado por los 9 productos
de débito) y confirmada con `updateCardStatus` en BRE QA:

| Código | `CRDSTATUS.DESCR` | Salidas permitidas desde el estado | Semántica de negocio |
|--------|-------------------|------------------------------------|----------------------|
| `36` | `Bloqueo_preventivo` | `06` cancelada cliente, `07` cancelada banco, `36` — **sin retorno a `00`** | **Bloqueo permanente** (terminal, solo desemboca en cancelación) |
| `71` | `Call_Prevencion` | `00` | **Bloqueo preventivo** (reversible) |
| `70` | `PREVENTIVO` | histórico Sentinel / prevención de fraude | Bloqueo por riesgo (motor Sentinel) |

Evidencia live BRE QA `<HOST_PRIVATE_CORTEX>:19084` (`updateCardStatus`, usuario `api`):

| Transición | `RtnCde` |
|------------|----------|
| `00` → `71` | `000` (éxito; `CRDDET.STATCODE=71`, `CDSTHST` registra `WHO_SET=webservice`) |
| `71` → `00` | `000` (round-trip completo) |
| `36` → `00` | `119` Status change not allowed |
| `36` → `71` | `119` Status change not allowed |

Uso operativo en `CDSTHST`: el canal (`WHO_SET=AppUser`) escribe `WHY_SET='Bloqueo preventivo'`
contra `NEW_STATCODE=71` (22 ocurrencias 2025-09 → 2026-04). Los registros de `36` con ese motivo
son 2 y el resto son `API TEST` o motivos definitivos (`REEMPLAZO`, `TARJETA BLOQUEADA`).

**La matriz que BRE realmente aplica es `CRDSTATUSTRANS`, no `BRE_CUST_CRDSTATUSTRANS`:**
`BRE_CUST_CRDSTATUSTRANS` solo lista `00↔36`, pero live acepta `00↔71` (ausente en esa tabla) y
rechaza `36→00` (presente en ella). El `119` que se atribuyó a "`71` no habilitado" era en realidad
estado/vigencia del plástico de prueba: una tarjeta expirada o ya sentada en `36` (terminal).

### `ACCTYPE` / `CUSTIDTYPE` / `PINSTATUS`

- Accounts: `10` AHORRO, `20` CORRIENTE (`CURRCODE` often `214`).
- Docs: `CUSTIDTYPE.ID` `6`=Cédula, `4`=Pasaporte, `3`=RNC. SP `EAI_DATOSCLIENTE_CORTEX` maps `IDTYPE_ID` `1`→`6`, else→`4` for API `TipoDocumento`.
- PIN: `0` normal, `10` wait_processing, `20` deliv_pending, `40` activa_wait, …

## EAI / SP surface used by debit MS

Primary consumer path in `ms-debit-card-inquiries`: JDBC call `{ call EAI_DATOSCLIENTE_CORTEX(?, ?, ?) }` (`CortexCardSpService`). SOAP remains for Enc/Dec PAN and GetCardDetails.

| Object | In | Out | Joins / purpose |
|--------|----|-----|-----------------|
| `EAI_DATOSCLIENTE_CORTEX` | `p_tarjeta` (= `CRDDET.PAN`) | `p_resultado`, ref cursor | `CRDDET`⋈`CUSTDET`⋈`CUSTIDCODE`; product via `EAI_GETDESCRPRODUCTO` |
| `EAI_DETALLETARJETACORTEX` | PAN | result + 2 cursors | Card detail + linked accounts (`Designada`/`Relacionada`) |
| `EAI_TARJETASDEBITOCUENTA` / `_V2` | `ACCNO` | result + cursor | Cards by account via `CRDACC`⋈`ACCDET`; limits via `EAI_LIMITETARJETA` |
| `EAI_TARJETACORTEXPORID` | id | cursor | Cards by customer id |
| `SP_CARD_PRODUCT` | document `IDCODE` | cursor | Cards + product + BRE token count |
| `SP_CARD_UPDATE_ACCOUNT` | `PAN_DISPLAY`, account, type | cursor | **DML** — rewrite `CRDACC` / `CRDDET.ACCDET_ID` (not for read-only agents) |
| `EAI_GETDESCRPRODUCTO` | product id | varchar | Looks up `CRDPRODUCT.DESCR` by **`PRODNUM`** (note: caller often passes `CRDPRODUCT_ID` — verify before trusting descr) |
| `EAI_LIMITETARJETA` | product id, card/acc id, `'ATM'`/`'POS'` | number | Limit helper used by account listing SPs |

Result codes seen: `'000'` OK, `'904'`/`'384'` not found, `'001'`/`'404'` error.

## Query patterns (read-only)

Mask `PAN` / `PAN_DISPLAY` / names / `IDCODE` in any shared output.

### 1. Card by tokenized/internal PAN (same key as EAI SP)

```sql
SELECT c.ID,
       SUBSTR(c.PAN_DISPLAY,1,6)||'******'||SUBSTR(c.PAN_DISPLAY,-4) AS pan_mask,
       c.STATCODE, s.DESCR AS status_descr,
       c.CRDPRODUCT_ID, p.CRDPRODUCT, p.DESCR AS product_descr,
       c.EXPDATE, c.BRANCH_ID, c.CUSTDET_ID, c.ACCDET_ID, c.CRDACTSTAT
FROM CRDDET c
JOIN CRDSTATUS s ON s.STATCODE = c.STATCODE
JOIN CRDPRODUCT p ON p.ID = c.CRDPRODUCT_ID
WHERE c.PAN = :pan AND ROWNUM < 2;
```

### 2. Cards by document (`CUSTIDCODE`)

```sql
SELECT c.ID,
       SUBSTR(c.PAN_DISPLAY,1,6)||'******'||SUBSTR(c.PAN_DISPLAY,-4) AS pan_mask,
       s.DESCR AS status_descr, p.CRDPRODUCT, p.DESCR AS product_descr, c.EXPDATE
FROM CUSTIDCODE i
JOIN CRDDET c ON c.CUSTDET_ID = i.CUSTDET_ID
JOIN CRDSTATUS s ON s.STATCODE = c.STATCODE
JOIN CRDPRODUCT p ON p.ID = c.CRDPRODUCT_ID
WHERE i.IDCODE = :idcode;
```

### 3. Cards linked to an account

```sql
SELECT SUBSTR(c.PAN_DISPLAY,1,6)||'******'||SUBSTR(c.PAN_DISPLAY,-4) AS pan_mask,
       c.STATCODE, s.DESCR,
       CASE WHEN c.ACCDET_ID = a.ID THEN 'Designada' ELSE 'Relacionada' END AS tipo_relacion,
       a.ACCNO, a.TYPECODE, a.CURRCODE
FROM ACCDET a
JOIN CRDACC r ON r.ACCDET_ID = a.ID
JOIN CRDDET c ON c.ID = r.CRDDET_ID
JOIN CRDSTATUS s ON s.STATCODE = c.STATCODE
WHERE a.ACCNO = :accno;
```

### 4. Primary account for a card

```sql
SELECT a.ID, a.ACCNO, a.TYPECODE, a.CURRCODE, a.STATCODE, ast.DESCR
FROM CRDDET c
JOIN ACCDET a ON a.ID = c.ACCDET_ID
JOIN ACCSTATUS ast ON ast.STATCODE = a.STATCODE
WHERE c.ID = :crddet_id;
```

### 5. Product / status catalogs

```sql
SELECT ID, CRDPRODUCT, DESCR, DEF_TYPEACC, PRODNUM, VALIDITY FROM CRDPRODUCT ORDER BY CRDPRODUCT;
SELECT STATCODE, DESCR, ACTIONCODE, RSPCODE, CANCELED FROM CRDSTATUS ORDER BY STATCODE;
SELECT TYPECODE, CLASSID, CURRCODE, DESCR FROM ACCTYPE ORDER BY TYPECODE;
```

### 6. Status history for a card

```sql
SELECT OLD_STATCODE, NEW_STATCODE, DATE_SET, WHY_SET, WHO_SET
FROM CDSTHST
WHERE CRDDET_ID = :crddet_id
ORDER BY DATE_SET DESC, TIME_SET DESC
FETCH FIRST 50 ROWS ONLY;
```

### 7. Per-card / product limits

```sql
SELECT * FROM CRDLIMIT WHERE CRDDET_ID = :crddet_id;
SELECT l.* FROM CRDPRODLIM l WHERE l.CRDPRODUCT_ID = :crdproduct_id;
```

### 8. Wallet / digital device tokens for a card

```sql
SELECT ID, SCHEMEID, PANSUFFIX, TKNSTATUS, PROVISIONINGSTATUS,
       DEVTYPE, DEVNAME, /* do not select DEVID/IP unless needed */
       TKNEXPIRYDATE, WHENCREATED
FROM TOKEN
WHERE CRDDET_ID = :crddet_id;
```

### 9. ATM / POS terminal (device-query style)

```sql
SELECT ID, TERMCODE, STATUSID, BRANCH_ID, CURRCODE, LOCATION
FROM TERMATM WHERE TERMCODE = :termcode AND ROWNUM < 5;
SELECT ID, TERMCODE, STATUSID, MERCHANT_ID, LOCATION
FROM TERMPOS WHERE TERMCODE = :termcode AND ROWNUM < 5;
```

### 10. Call SP from Python / JDBC (no PAN logging)

```sql
-- JDBC: { call EAI_DATOSCLIENTE_CORTEX(?, ?, ?) }
-- 1 IN VARCHAR2 pan, 2 OUT VARCHAR2 result, 3 IN/OUT REF CURSOR
-- Cursor cols: Tarjeta, Documento, TipoDocumento, Estado, Moneda, FechaExpiracion, TipoProducto, …
```

## Agent rules

1. Prefer `CORTEXPCI_UAT` objects; skip `SP28_%` backups.
2. Prefer EAI SPs above for parity with MS; raw joins for exploration/diagnostics.
3. Never `SELECT *` from `CRDDET`/`CUSTDET`/`PANENC`/`BIN` into chat/vault — project and mask.
4. Do not run `SP_CARD_UPDATE_ACCOUNT` (or any DML SP) unless the user explicitly requests write access.
5. `BIN` has millions of rows — never full-table scan.

## Source anchors

- Skill consumer: `<BANRESERVAS_TC_PROJECT_ROOT>/…
- IAC JDBC QA: `…/overlays/qa/configmap/ms-debit-card-inquiries.env` (URL only); secrets under `…/secret/`
