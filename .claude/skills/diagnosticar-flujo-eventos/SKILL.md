---
name: diagnosticar-flujo-eventos
description: Diagnostica pipelines de eventos (lag, duplicados, desorden, poison, outbox atrasado). Úsala cuando haya fallos de integración asíncrona o síntomas de mensajería degradada.
metadata:
  author: yzylabs
  version: "1.0"
---

# Diagnosticar flujo de eventos

## Propósito

Localizar la causa de fallos en pub/sub con evidencia (offsets, métricas, logs, estados outbox) y proponer corrección sin adivinar.

## Entradas

- Síntoma (lag, duplicados, mensajes faltantes, DLQ creciente).
- Productor(es), consumidor(es), canal.
- Ventana temporal y correlation/trace ids.
- Acceso a métricas/logs/offsets (o dumps aportados).

## Procedimiento

1. Reproduce el síntoma en una línea de tiempo: produce → broker → consume → side effect.
2. Verifica outbox: ¿hay `pending`/`failed` atrasados?
3. Mide lag del consumer group / profundidad de cola.
4. Busca duplicados por `event.id` y side effects repetidos.
5. Inspecciona DLQ: tasa, errores, poison top-N.
6. Comprueba desorden vs invariantes de negocio (¿se asumió orden global?).
7. Contrasta con AsyncAPI/contrato (schema drift).
8. Entrega hipótesis rankeadas con evidencia y siguiente acción (fix code, replay, scale, handoff).

## Salida

```md
## Síntoma
## Línea de tiempo
## Evidencia (métricas/logs/offsets)
## Hipótesis rankeadas
## Acciones recomendadas
## Riesgos / blast radius
## Handoffs
```

## Casos límite

- Sin acceso a broker → pide dumps mínimos; no inventes offsets.
- “Falta el evento” pero outbox vacío → falla antes de outbox (transacción de dominio).
- Storm de reintentos → prioriza cortar poison antes de scale horizontal.

## Validación

- Cada hipótesis cita evidencia.
- No se declara root cause sin dato.
- Acciones distinguen mitigación inmediata vs fix estructural.

## Criterios de terminado

- Katakuri puede decidir replay/fix/scale con el reporte.
- Se evita “reinicia el pod” como única respuesta sin evidencia.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Lag creciente en group billing | Lag + slow handler o under-partitioned |
| Ambiguo | “A veces duplica cobros” | Dedupe ausente + plan de ledger |
| Límite | Sin métricas del broker | Lista de evidencias faltantes + BLOCKED parcial |

## Fuentes

- CloudEvents Primer — https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/primer.md (2026-08-04).
- Microsoft Learn — Transactional Outbox — https://learn.microsoft.com/en-us/azure/architecture/databases/guide/transactional-outbox-cosmos (2026-08-04).
