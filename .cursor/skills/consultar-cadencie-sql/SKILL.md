---
name: consultar-cadencie-sql
description: "Consulta live SQL de Cadencie (TC crédito Oracle). Úsala cuando inventaríes productos/status o muestrees CARD/ACCT/PRMCN bajo Iceburg."
metadata:
  author: yzylabs
  version: "1.0"
---

# consultar-cadencie-sql

## Propósito

Ejecutar el ciclo schema-first → connect → query → redact → report para **cadencie**.

## Entradas

- Objetivo de negocio de la consulta.
- Filtros (producto, status, id enmascarable).
- Hub `references/cadencie.md` (+ index).
- Protocolo `consultar-cores-bancarios-sql`.

## Procedimiento

1. Confirma ownership: este pedido es cadencie (no otro core).
2. READ `consultar-cores-bancarios-sql` y `references/cadencie.md`.
3. Identifica hubs: `CUSTR` ↔ `CARD` ↔ `ACCT` ↔ `PRMCN`; status `CLOCD`/`CANCL_CODE`.
4. Resuelve credenciales externas; nunca echo password.
5. Connect con timeout corto; VPN required. Fallo → BLOCKED.
6. Escribe SQL mínimo; usa ALL_TAB_COLUMNS / USER_TABLES solo si el hub no tiene el objeto.
7. Ejecuta read-only; enmascara PAN/PII.
8. Empaqueta salida + SQL + counts + samples masked.
9. Reporta a Iceburg con EVIDENCE.

## Salida

```md
## Core + entorno
## Hubs usados
## SQL
## Counts / samples (masked)
## Gaps UNKNOWN
## Connectivity
```

## Validación

- Schema leído antes de meta-queries.
- Sin secretos ni PII/PAN completos.
- Sin resultados inventados.
- Ownership correcto vs pares.

## Criterios de terminado

- Evidencia SQL usable **o** BLOCKED documentado (VPN/credenciales).
- `REPORT_TO: iceburg-director-sistemas-core`.

## Fuentes

| Fuente | Fecha | Uso |
|--------|-------|-----|
| references/cadencie.md | forja 2026-08-04 | Hubs |
| consultar-cores-bancarios-sql | 2026-08-04 | Protocolo |
