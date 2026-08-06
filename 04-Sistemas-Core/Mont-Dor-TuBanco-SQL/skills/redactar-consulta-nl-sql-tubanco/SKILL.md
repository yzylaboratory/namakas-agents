---
name: redactar-consulta-nl-sql-tubanco
description: "Traduce pregunta en lenguaje natural a T-SQL para TuBanco con el patrón listar→schema→chequear→ejecutar (estilo LangChain). Úsala cuando Randy pida NL→SQL sobre TuBanco sin inventar fallbacks."
metadata:
  author: yzylabs
  version: "1.0"
---

# redactar-consulta-nl-sql-tubanco

## Propósito

Aplicar un flujo NL→SQL disciplinado (inspirado en LangChain `SQLDatabaseToolkit` y prompts tipo `langchain-ai/sql-query-system-prompt`) sobre TuBanco, con read-only por defecto.

## Entradas

- Pregunta en lenguaje natural.
- Dialect implícito: T-SQL (Azure SQL MI).
- Entorno DES|QA.
- Hub / tablas candidatas si ya se conocen.

## Procedimiento

1. Reformula la pregunta y lista tablas relevantes (equivalente a `sql_db_list_tables` / listado desde hub).
2. Inspecciona schema solo de esas tablas (hub o `explorar-schema-tubanco` / meta-query acotada — equivalente a `sql_db_schema`).
3. Redacta T-SQL candidato; incluye límites de filas cuando sea exploración.
4. Autochequeo (equivalente a `sql_db_query_checker`): joins, tipos, identificadores citados, `NOT IN`+NULL, agregaciones, dialect T-SQL.
5. Si la query no es read-only → pedir confirmación explícita; no ejecutar.
6. Ejecutar vía `consultar-tubanco-sql` (equivalente a `sql_db_query` / execute).
7. Si el motor falla por columna/tabla desconocida → volver al paso 2; no inventar datos.
8. Entregar respuesta + SQL + evidencia; sin secretos.

## Salida

```md
## Pregunta
## Tablas consideradas
## SQL propuesto / ejecutado
## Resultado (masked)
## Notas de chequeo
```

## Validación

- Se inspeccionó schema antes de ejecutar (salvo SQL ya validado por el usuario).
- Sin fallbacks inventados.
- Read-only respetado salvo confirmación explícita.

## Criterios de terminado

- Respuesta grounded en ejecución **o** `BLOCKED` / SQL propuesto pendiente de confirmación.
- `REPORT_TO: katakuri-director-backend`.

## Fuentes

| Fuente | Fecha | Uso |
|--------|-------|-----|
| LangChain Docs — SQLDatabase toolkit | 2026-08-05 | Ciclo list/schema/check/query |
| Hub prompt pattern `langchain-ai/sql-query-system-prompt` (referencia comunitaria) | 2026-08-05 | Disciplina de system prompt SQL |
| Microsoft Learn — T-SQL catalog / MI | 2026-08-05 | Dialect + discovery |
