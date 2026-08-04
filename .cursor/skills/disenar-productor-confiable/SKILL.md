---
name: disenar-productor-confiable
description: Diseña un productor de eventos fiable (transactional outbox/relay, ids, headers, anti dual-write). Úsala cuando un servicio deba publicar eventos junto a cambios de estado sin perder mensajes.
metadata:
  author: yzylabs
  version: "1.0"
---

# Diseñar productor confiable

## Propósito

Garantizar que el estado de dominio y la intención de publicar un evento se confirmen juntos, y que un relay publique al broker con reintentos seguros.

## Entradas

- Servicio/productor y store de dominio.
- Eventos a emitir (modelo previo o borrador).
- Broker destino.
- Restricciones de latencia y orden.
- Dueño de persistencia (Pudding) si el outbox toca schema.

## Procedimiento

1. Detecta dual-write (DB + broker en dos pasos) y márcalo como riesgo.
2. Propón transactional outbox: misma transacción escribe estado + fila/documento outbox.
3. Define relay (worker/change feed) que lee outbox y publica al broker.
4. Usa `id` del evento como clave de deduplicación en el broker si está disponible.
5. Define estados outbox (`pending` / `published` / `failed`) y política de reintento.
6. Documenta headers (CloudEvents mode structured/binary, trace context).
7. Si el schema outbox es nuevo → handoff a Pudding; no inventes migraciones sin evidencia.

## Salida

```md
## Productor
## Riesgo dual-write
## Diseño outbox + relay
## Ids / dedupe
## Reintentos y fallos
## Handoff Pudding / X-Drake
## Riesgos
```

## Casos límite

- Store sin transacciones multi-documento → documenta límites (p. ej. misma partición Cosmos) o patrón alternativo.
- Publicación síncrona exigida por SLA → mide trade-off; no ocultes pérdida potencial.
- Relay publica dos veces → consumidores deben tolerarlo (at-least-once).

## Validación

- No queda dual-write sin mitigación documentada.
- Outbox y relay tienen dueños y estados.
- `id` de evento definido para dedupe.

## Criterios de terminado

- Un crash entre commit y publish no pierde el evento de forma silenciosa.
- Reintentos del relay están especificados.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | OrderService + Kafka | Outbox + relay + ids |
| Ambiguo | “Publica al bus después del save” | Dual-write marcado + outbox propuesto |
| Límite | Cosmos sin misma partición | Límites ACID + alternativa documentada |

## Fuentes

- Microsoft Learn — Transactional Outbox — https://learn.microsoft.com/en-us/azure/architecture/databases/guide/transactional-outbox-cosmos (2026-08-04).
- CloudEvents Spec 1.0.2 — https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md (2026-08-04).
