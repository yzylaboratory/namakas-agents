---
name: consultar-tubanco-sql
description: "Ejecuta SQL live contra TuBanco DES/QA (read-only por defecto) con redacción de PII y evidencia. Úsala cuando el schema ya está claro y hay que contar, muestrear o validar datos para migration-tool / App Empresas."
metadata:
  author: yzylabs
  version: "1.0"
---

# consultar-tubanco-sql

## Propósito

Ciclo connect → query acotada → redact → report sobre TuBanco.

## Entradas

- Objetivo de negocio de la consulta.
- Entorno DES|QA.
- Hub `references/tubanco.md` (u objetos ya inventariados).
- Confirmación explícita del usuario si el SQL no es read-only.

## Procedimiento

1. Confirma ownership TuBanco.
2. Lee hub; si falta el objeto, ejecuta primero `explorar-schema-tubanco` (gap real).
3. Resuelve credenciales desde `TUBANCO_*`; nunca echo password.
4. Clasifica el SQL:
   - Read-only (`SELECT`/`WITH`…`SELECT`) → proceder.
   - Destructivo/DDL → **STOP** hasta confirmación explícita del usuario.
5. Escribe SQL mínimo con `TOP`/`OFFSET-FETCH` razonable para samples.
6. Ejecuta; enmascara PII en la salida.
7. Empaqueta entorno + SQL + counts + samples masked.
8. Reporta a Katakuri con EVIDENCE.

## Salida

```md
## Entorno
## SQL
## Counts / samples (masked)
## Gaps UNKNOWN
## Connectivity
```

## Validación

- Sin secretos ni PII completos.
- Sin resultados inventados.
- Confirmación explícita presente si hubo DML/DDL.

## Criterios de terminado

- Evidencia SQL usable **o** `BLOCKED` (VPN/firewall/env).
- `REPORT_TO: katakuri-director-backend`.

## Fuentes

| Fuente | Fecha | Uso |
|--------|-------|-----|
| Microsoft Learn — Azure SQL MI connectivity | 2026-08-05 | Conexión |
| references/tubanco.md | forja 2026-08-05 | Hubs |
