> **Nakamas adaptation (2026-08-04).** Schema hub preserved; hosts sanitized to placeholders; no passwords. Live SQL expert: `greenbull-core-acard` under `iceburg-director-sistemas-core`. ≠ Crocus/Tom/Kaku; ≠ Tripulación `brd-*`.

# ACard (SQL Server) — schema map (TC delivery / emboss trail)

**Core:** ACard — delivery / emboss trail Banreservas  
**Environment:** SQL Server intranet (`ACard_PROD`)  
**Captured:** 2026-07-27 from verified baselines (2026-07-21) — **not** a full live inventory  
**Primary consumers:** `ms-credit-cards-inquiries` (join Cadencie∩ACard), `microservices/acard/*` (ACARD HTTP API; not direct SQL)  
**Catalog size:** **Unknown** — no full table count captured yet

Not Cadencie, Way4, Cortex, or Siebel JDBC.

---

## 1. Purpose

Source of **plastic request → emboss → delivery status** for credit cards. Join to Cadencie is typically by masked/full PAN (`Tarjeta` / `PAN`) and/or identification. Product catalog surface is `Tipo_Producto` (referenced via `Solicitud_Gestion.IDTipo_Producto`). Canonical product/status codes live in IAC mappings, not invented here.

---

## 2. Connection summary (no password)

| Field | Value |
|-------|--------|
| Host | `<HOST_PRIVATE_ACARD>` |
| Port | `59374` |
| Database | `ACard_PROD` (also `Acard`, `ProcesosTC` if needed — not SoT for trail docs) |
| User | `intranet` |
| Preferred client | `sqlcmd` or Python `pymssql` / `pyodbc` |
| Credential source | Known project notes / IAC if present; otherwise **ask the user**. Never print the password. |
| Network | Private IP — **corporate VPN required**. Timeout → stop and report VPN. |

```bash
# After loading ACARD_USER / ACARD_PASS (never echo)
sqlcmd -S "<HOST_PRIVATE_ACARD>,59374" -U "${ACARD_USER}" -P "${ACARD_PASS}" -d ACard_PROD -C
```

See also: [Iceburg connections](../../Iceburg-Director-Sistemas-Core/references/connections.md), [protocolo compartido](../../Iceburg-Director-Sistemas-Core/skills/consultar-cores-bancarios-sql/SKILL.md).

---

## 3. Evidence sources (absolute)

| Artifact | Path |
|----------|------|
| Status trail baseline | `<BANRESERVAS_TC_PROJECT_ROOT>/…
| Cadencie ∩ ACard cards | `<BANRESERVAS_TC_PROJECT_ROOT>/…
| Sampler script | `<BANRESERVAS_TC_PROJECT_ROOT>/…
| IAC status map (`by-core.ACARD`) | `<BANRESERVAS_TC_PROJECT_ROOT>/…
| IAC product map (`by-core.ACARD`) | `<BANRESERVAS_TC_PROJECT_ROOT>/…

---

## 4. Domain model (join spine)

```
dbo.Solicitud_Gestion sg
  ├── dbo.Solicitud_Estado_Entrega e   -- e.IDSolicitud_Gestion = sg.IDSolicitud_Gestion
  ├── dbo.Plastico_Embozado p          -- emboss row (join key NOT fully documented — see unknowns)
  └── dbo.Tipo_Producto tp             -- conceptual: tp via sg.IDTipo_Producto (columns UNKNOWN)
```

Related names only (no column evidence): `Solicitud_Gestion_Log`, `Notificacion_Estado`, `Mensajero_Entrega`.  
Vault-only view name (unverified in baselines): `vw_NV_Estado_Entrega`.

---

## 5. Key tables

### `dbo.Solicitud_Gestion` — verified columns

| Column | Notes |
|--------|--------|
| `IDSolicitud_Gestion` | PK / trail key |
| `Tarjeta` | PAN — **mask** `BIN********LAST4` |
| `Numero_Identificacion` | Doc — mask in outputs |
| `Tipo_Identificacion` | |
| `IDTipo_Producto` | FK conceptual → `Tipo_Producto` |
| `Tipo_Solicitud` | |
| `Cuenta` | |
| `nvEstado_Embozado` | Emboss status narrative |
| `nvEstado_Entrega` | Delivery status narrative |
| `Fecha_Solicitud` | |
| `Fecha_Embozado` | |
| `Fecha_Entrega` | |
| `Sucursal_Origen` | |
| `Sucursal_Entrega` | |
| `Nombre_Cliente` | PII — redact in vault |
| `Estado_Registro` | Sample filter `= 'C'` in baselines |

### `dbo.Solicitud_Estado_Entrega` — verified schema block

| Column | Type (from baseline) |
|--------|----------------------|
| `IDSolicitud_Gestion` | int |
| `EstatusId` | int — status code |
| `Descripcion` | varchar |
| `Fecha` | datetime |

Sample `EstatusId` values seen in baseline (not exhaustive): `0`, `98`, `111`, `1072`, `113`, `114`, `108`, `109`. Map to canonical via IAC `status-mapping.yaml` `by-core.ACARD`.

### `dbo.Plastico_Embozado` — partial (one sample row)

| Column | Notes |
|--------|--------|
| `IDPlastico_Embozado` | |
| `PAN` | **mask** |
| `Fecha_Embozado` | |
| `nvEstatus_Embozado` | |
| `Fecha_Activacion` | |

Full DDL: **UNKNOWN**.

### `dbo.Tipo_Producto` — table name only

Usage: product catalog referenced by `Solicitud_Gestion.IDTipo_Producto`. **No verified columns** in workspace. Do not invent. Prefer IAC `product-code-mapping.yml` `by-core.ACARD` for codes until live DESCRIBE.

### Name-only (columns UNKNOWN)

- `dbo.Solicitud_Gestion_Log`
- `dbo.Notificacion_Estado`
- `dbo.Mensajero_Entrega`

---

## 6. Unknowns (explicit)

| Item | Status |
|------|--------|
| Full DB table/procedure counts | Not inventoried |
| `Tipo_Producto` columns | Unknown |
| Full `Plastico_Embozado` DDL | Partial only |
| Join key `Solicitud_Gestion` ↔ `Plastico_Embozado` | Not documented in baselines |
| `vw_NV_Estado_Entrega` | Vault mention only — unverified in SQL baselines |
| Research dump `…/_research/2026-07-23_acard_product_codes.json` | Referenced in vault; folder may be absent |

When a column/object is missing here: query `INFORMATION_SCHEMA.COLUMNS` / `sys.tables` once, then update this doc.

---

## 7. Safety / output

- Read-only by default.
- Never print passwords; never dump PAN/PII into Obsidian.
- Return: core+env, SQL used, counts, masked samples, artifact paths.
