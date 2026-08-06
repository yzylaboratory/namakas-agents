# TuBanco connections (placeholders)

> No passwords. Valores reales solo en `.env` / `.env.local` gitignored.

| Env | Server env var | User env var | Password env var | Database env var (opt) | Expert |
|-----|----------------|--------------|------------------|------------------------|--------|
| DES | `TUBANCO_DES_SERVER` | `TUBANCO_DES_USER` | `TUBANCO_DES_PASSWORD` | `TUBANCO_DES_DATABASE` | `mont-dor-tubanco-sql` |
| QA | `TUBANCO_QA_SERVER` | `TUBANCO_QA_USER` | `TUBANCO_QA_PASSWORD` | `TUBANCO_QA_DATABASE` | `mont-dor-tubanco-sql` |

Clientes sugeridos: `sqlcmd`, `mssql-cli`, o driver TDS compatible (pymssql / Microsoft ODBC) con cifrado en tránsito.

Default: `TUBANCO_DEFAULT_ENV=des` o `qa`.
