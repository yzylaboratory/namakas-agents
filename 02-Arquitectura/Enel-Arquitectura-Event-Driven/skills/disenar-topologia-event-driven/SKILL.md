---
name: disenar-topologia-event-driven
description: Diseña la topología event-driven (productores, canales, consumidores, fan-out/fan-in y límites de contexto). Úsala cuando Law o Luffy pidan arquitectura EDA, mapa de mensajería o desacoplar servicios vía eventos.
metadata:
  author: yzylabs
  version: "1.0"
---

# Diseñar topología event-driven

## Propósito

Convertir un problema de integración o desacoplamiento en una topología EDA explícita, con límites, canales y roles pub/sub verificables.

## Entradas

- Objetivo de negocio y bounded contexts.
- Inventario de servicios/APIs existentes.
- Restricciones de latencia, orden y disponibilidad.
- Broker/plataforma ya decidida (si existe).
- Decisiones previas de Law.

## Procedimiento

1. Acota el outcome: desacoplar escritura, proyectar lecturas, integrar dominios, audit trail u otro.
2. Lista productores y consumidores candidatos; marca dueños TBD si faltan.
3. Propón canales/topics con naming estable; separa canal de dominio vs técnico.
4. Dibuja fan-out/fan-in y puntos de acoplamiento temporal.
5. Elige estilo (pub/sub vs request/reply async vs streaming) con trade-off en una frase.
6. Declara orden, partición/clave y backpressure a nivel de diseño (sin inventar capacidad de cluster).
7. Lista no-objetivos (p. ej. “no event sourcing en esta iteración”).
8. Entrega la topología lista para catálogo de eventos y handoff.

## Salida

```md
## Topología EDA
- Outcome:
- Bounded contexts:
## Nodos
| Rol | Servicio | Dueño | Notas |
## Canales
| Canal/address | Propósito | Retención (si conocida) |
## Flujos
| De → Canal → A | Garantía deseada | Riesgo |
## Trade-offs y no-objetivos
## Pendientes de broker/infra
```

## Casos límite

- Solo HTTP síncrono sin necesidad de eventos → recomienda no-EDA y justifica.
- Multi-país / multi-tenant → canales o atributos de tenant explícitos; no mezclar.
- Un solo “bus global” propuesto sin dueños → rechaza o exige ownership por evento.

## Validación

- Cada canal tiene al menos un productor o consumidor documentado (o TBD explícito).
- Hay outcome y no-objetivos.
- No se inventó broker concreto si no estaba dado (queda como pendiente).

## Criterios de terminado

- Topología usable por Law/Robin/Backend sin reinterpretar roles.
- Acoplamientos y riesgos listados.
- Lista de pendientes de infra.

## Fuentes

- AsyncAPI Initiative — AsyncAPI / CloudEvents / OpenTelemetry — https://www.asyncapi.com/blog/async_standards_compare (2026-08-04).
- AsyncAPI Specification — https://www.asyncapi.com/docs/reference/specification/latest (2026-08-04).
