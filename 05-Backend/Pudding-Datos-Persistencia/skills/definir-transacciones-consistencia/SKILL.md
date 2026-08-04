---
name: definir-transacciones-consistencia
description: Define límites transaccionales ACID, isolation y consistencia (fuerte vs eventual). Úsala cuando un caso de uso atraviese múltiples escrituras, riesgos de carrera o handoff a eventos.
metadata:
  author: yzylabs
  version: "1.0"
---

# Definir transacciones y consistencia

## Propósito

Asegurar que las escrituras respeten ACID donde corresponde y explicitar cuándo la consistencia es eventual vía mensajería.

## Entradas

- Caso de uso / invariantes de negocio.
- Operaciones de escritura involucradas.
- Motor (p. ej. PostgreSQL) y isolation default.
- Necesidad de outbox/eventos (Apoo).
- Tolerancia a anomalías de lectura.

## Procedimiento

1. Lista invariantes que deben cumplirse al commit (consistencia).
2. Agrupa operaciones en la unidad atómica mínima (no más amplia de lo necesario).
3. Elige isolation (Read Committed default vs Repeatable Read / Serializable) con justificación.
4. Define manejo de conflicto (retry, abort, savepoint).
5. Si hay side-effects externos (email, bus): no los metas dentro de la TX ciega; diseña outbox → Apoo.
6. Documenta visibilidad concurrente (qué ven otras TX antes/después del commit).
7. Señala riesgos de dirty / non-repeatable / phantom reads si el nivel es bajo.
8. Entrega política transaccional del caso de uso.

## Salida

```md
## Caso de uso
## Invariantes
## Frontera transaccional
## Isolation level
## Conflictos / retries
## Side-effects / outbox
## Anomalías aceptadas o mitigadas
## Riesgos
```

## Casos límite

- Lectura larga de reporte dentro de TX de escritura → separa read model / snapshot.
- “Necesitamos eventual consistency” sin dueño de eventos → `DELEGATION_REQUIRED` a Apoo vía Katakuri.
- Dinero/ledger → isolation estricta + evidencia; no bajes el nivel por latencia sin aprobación.

## Validación

- Frontera TX explícita.
- Isolation justificada vs default del motor.
- Side-effects fuera de TX o con outbox.
- Fuentes ACID/motor citadas.

## Criterios de terminado

- Un implementador sabe qué va en `BEGIN…COMMIT` y qué no.
- Handoff a Apoo documentado si hay eventos.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Transferencia entre dos filas | Una TX, invariante de suma, isolation documentada |
| Ambiguo | “Hazlo consistente” | Preguntas de invariantes + borrador de frontera |
| Límite | Cobro + publicar evento Kafka | TX local + outbox; no publish-before-commit |

## Fuentes

- PostgreSQL 18 Transactions — https://www.postgresql.org/docs/18/tutorial-transactions.html (2026-08-04).
- PostgreSQL Glossary (ACID) — https://www.postgresql.org/docs/current/glossary.html (2026-08-04).
