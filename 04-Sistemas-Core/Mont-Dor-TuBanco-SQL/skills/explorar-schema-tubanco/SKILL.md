---
name: explorar-schema-tubanco
description: "Inventaria schema de TuBanco (Azure SQL MI DES/QA) con catalog views e INFORMATION_SCHEMA y actualiza el hub durable. Úsala cuando necesites listar bases, schemas, tablas, columnas o FKs antes de consultar datos."
metadata:
  author: yzylabs
  version: "1.0"
---

# explorar-schema-tubanco

## Propósito

Discovery schema-first de TuBanco sin dumps masivos; ampliar `references/tubanco.md` con evidencia.

## Entradas

- Entorno: `des` | `qa` (o `TUBANCO_DEFAULT_ENV`).
- Alcance opcional (schema/tabla/prefijo).
- Hub vigente `references/tubanco.md`.

## Procedimiento

1. Confirma ownership TuBanco (`mont-dor-tubanco-sql`).
2. Resuelve env vars `TUBANCO_<ENV>_SERVER|USER|PASSWORD` sin imprimir secretos.
3. Conecta (timeout corto). Fallo → `BLOCKED`.
4. Si el hub ya documenta el objeto pedido, reutilízalo; no re-inventaries de cero.
5. Discovery mínimo:
   - `sys.databases` / DB actual
   - `sys.schemas`, `sys.tables`, `sys.columns`
   - FKs vía `sys.foreign_keys` / `sys.foreign_key_columns` si hace falta
   - `INFORMATION_SCHEMA.*` cuando se necesite vista ISO
6. Actualiza `references/tubanco.md` con hallazgos; marca UNKNOWN lo no verificado.
7. Reporta a Katakuri con EVIDENCE (SQL de meta + resumen; sin passwords).

## Salida

```md
## Entorno
## Objetos inventariados
## SQL de discovery
## Gaps UNKNOWN
## Hub actualizado (path)
```

## Validación

- Sin secretos en outputs.
- Sin `SELECT *` de tablas de negocio en esta skill (solo catálogo/meta).
- Hub no contradice evidencia live.

## Criterios de terminado

- Inventario usable **o** `BLOCKED` documentado.
- `REPORT_TO: katakuri-director-backend`.

## Fuentes

| Fuente | Fecha | Uso |
|--------|-------|-----|
| Microsoft Learn — catalog views / INFORMATION_SCHEMA | 2026-08-05 | Meta-queries |
| references/tubanco.md | forja 2026-08-05 | Hub |
