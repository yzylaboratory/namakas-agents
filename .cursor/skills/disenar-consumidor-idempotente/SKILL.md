---
name: disenar-consumidor-idempotente
description: Diseña un consumidor de eventos idempotente (dedupe, ack, reintentos, poison→DLQ). Úsala cuando debas implementar o revisar handlers que procesan mensajes at-least-once.
metadata:
  author: yzylabs
  version: "1.0"
---

# Diseñar consumidor idempotente

## Propósito

Hacer que el mismo evento pueda entregarse más de una vez sin efectos laterales duplicados, con ruta clara para mensajes poison.

## Entradas

- Evento(s) a consumir y AsyncAPI/canal.
- Side effects del handler (DB writes, llamadas HTTP, emails).
- Broker y semántica de ack/reentrega.
- Requisitos de orden (si existen).

## Procedimiento

1. Declara semántica: at-least-once (default) u otra con evidencia del broker.
2. Elige clave de idempotencia (`event.id` o negocio compuesto) y store de dedupe.
3. Haz el handler naturalmente idempotente cuando sea posible (upsert por clave de negocio).
4. Define ack: solo tras side effect durable exitoso (o outbox de efectos).
5. Especifica reintentos (backoff, max attempts) y criterios de poison.
6. Enruta poison a DLQ con metadata (error, attempts, offset/id).
7. Si hace falta orden por entidad, documenta sesión/partition key y límites.

## Salida

```md
## Consumidor
## Semántica de entrega
## Idempotencia (clave + store)
## Ack / reintentos
## Poison → DLQ
## Orden (si aplica)
## Riesgos
```

## Casos límite

- Side effect no idempotente (cobro) → usa clave de negocio + ledger de procesados.
- Reordenamiento → no asumas orden global; documenta invariantes.
- DLQ sin replay runbook → incompleto; añade procedimiento de reproceso.

## Validación

- Clave de idempotencia explícita.
- Ack no ocurre antes del commit durable.
- DLQ y max retries definidos.

## Criterios de terminado

- Duplicar el mismo `id` no duplica el efecto de negocio.
- Poison no bloquea indefinidamente el partition/grupo.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | `InvoicePaid` → marcar pagado | Upsert + dedupe por event.id |
| Ambiguo | “Escucha el topic y actualiza” | Preguntas de side effects + borrador idempotente |
| Límite | Cobro a pasarela no idempotente | Ledger + idempotency-key hacia pasarela |

## Fuentes

- CloudEvents Primer (consumers / duplicates) — https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/primer.md (2026-08-04).
- Microsoft Learn — Transactional Outbox (idempotent consumers) — https://learn.microsoft.com/en-us/azure/architecture/databases/guide/transactional-outbox-cosmos (2026-08-04).
