# Core DB connections (sanitized — Nakamas)

**No password literals. No secret values in this repo.**

Resolve credentials at runtime from external IAC/project secrets (outside Nakamas) or ask the operator.
Corporate **VPN required** for all private hosts. On timeout/unreachable: stop and report VPN/red — do not invent results.

Adapted from Banreservas core-databases protocol (2026-07/08); hierarchy remapped to Iceburg cells (**not** Codd / `brd-primsa`).

External project root (operator-local, not stored as authority in Nakamas):

`<BANRESERVAS_TC_PROJECT_ROOT>`

| Core | Engine | Host | Port | Service / DB | User (typical) | Client | Credential source (path pattern only) | Expert |
|------|--------|------|------|--------------|----------------|--------|---------------------------------------|--------|
| **Cadencie** | Oracle QA | `<HOST_PRIVATE_CADENCIE>` | `1521` | `pdbuc36` | `appsdbuc` (confirm) | `sqlplus` | External IAC secret pattern: `…/overlays/qa/secret/ms-credit-cards-inquiries.env` keys `quarkus.datasource.username` / `password` | `kizaru-core-cadencie` |
| **Way4** | Oracle testing | `<HOST_PRIVATE_WAY4>` | `1521` | `<WAY4_SERVICE>` (e.g. way4testing-prim…) | `OWS_A` | `sqlplus` / `oracledb` | External IAC / project docs (`WAY4_USER` / `WAY4_PASSWORD`); ask operator if absent | `kuzan-core-way4` |
| **Cortex** | Oracle debit/PCI | `<HOST_PRIVATE_CORTEX>` | `1521` | `<CORTEX_SERVICE>` | `cortexpci_uat` (confirm) | `sqlplus` | External IAC: `…/secret/ms-debit-card-inquiries.env` (or device-query) | `akainu-core-cortex` |
| **ACard** | SQL Server | `<HOST_PRIVATE_ACARD>` | `<ACARD_PORT>` | `ACard_PROD` | `intranet` | `sqlcmd` / `pymssql` | External project notes / IAC; ask operator if absent | `greenbull-core-acard` |
| **Siebel CRM** | Oracle QA | `<HOST_PRIVATE_SIEBEL>` | `1521` | `<SIEBEL_SERVICE>` (DB `PCRMIP14`) | `broker` (alt `crmcert`) | `sqlplus` / `oracledb` | External IAC: `…/secret/ms-party-information-query.env` | `smoker-core-siebel` |

## Connect snippets (password from env — do not echo)

**Oracle (`sqlplus` EZCONNECT):**

```bash
# After loading USER/PASS into shell vars (never echo $PASS)
sqlplus -L "${USER}/${PASS}@//${HOST}:${PORT}/${SERVICE}"
```

**ACard (`sqlcmd`):**

```bash
sqlcmd -S "${HOST},${PORT}" -U "${USER}" -P "${PASS}" -d ACard_PROD -C
```

## Network

All hosts are private. **VPN required**. Fail closed on network errors.

## Schema hubs

Per-expert durable docs under each cell `references/<core>.md` (+ `.index.json`).
Shared protocol skill: `consultar-cores-bancarios-sql`.
