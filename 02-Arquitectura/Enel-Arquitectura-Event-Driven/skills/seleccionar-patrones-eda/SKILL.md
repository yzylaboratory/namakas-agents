---
name: seleccionar-patrones-eda
description: Selecciona patrones EDA (outbox, inbox, saga/choreography, CQRS, event sourcing) con trade-offs y garantías de entrega/idempotencia. Úsala cuando haya que decidir consistencia, orquestación asíncrona o proyección de lecturas.
metadata:
  author: yzylabs
  version: "1.0"
---

# Seleccionar patrones EDA

## Propósito

Elegir el patrón mínimo suficiente para el problema de consistencia/integración, con garantías de entrega e idempotencia explícitas.

## Entradas

- Topología y catálogo de eventos.
- Requisitos de consistencia (strong vs eventual).
- Restricciones transaccionales de los stores.
- Tolerancia a duplicados y a reordenamiento.

## Procedimiento

1. Clasifica el problema: integración desacoplada, workflow multi-paso, proyección de lectura, audit/event store.
2. Parte de **pub/sub + idempotencia** como baseline; escala complejidad solo si falla.
3. Evalúa **transactional outbox** (y consumers idempotentes / inbox) cuando haya dual-write DB + broker.
4. Evalúa **choreography vs orchestration/saga** para workflows; documenta compensaciones si existen.
5. Evalúa **CQRS** cuando el modelo de lectura diverja materialmente del de escritura.
6. Evalúa **event sourcing** solo con requisitos claros de rebuild/audit; no lo uses por moda.
7. Declara garantía: at-most-once / at-least-once / exactly-once *semántico* (idempotencia + dedupe).
8. Define DLQ, reintentos, poison messages y señal operativa (p. ej. consumer lag).
9. Registra alternativa descartada y por qué.

## Salida

```md
## Decisión de patrón
- Patrón elegido:
- Alternativas descartadas:
## Garantías
- Entrega:
- Idempotencia:
- Orden:
## Mecanismos
| Mecanismo | Dónde | Notas |
## Operación
- DLQ / reintentos / lag:
## Riesgos
```

## Casos límite

- Exactly-once de broker ≠ exactly-once de negocio → exige idempotency key de dominio.
- Saga sin compensación definida → marca BLOCKED o limita el alcance del workflow.
- Outbox sin CDC/relay → documenta componente relay como dependencia.

## Validación

- Hay trade-off escrito (no solo nombre del patrón).
- Garantías e idempotencia explícitas.
- DLQ/reintentos mencionados o TBD con dueño.

## Criterios de terminado

- Decisión implementable por Backend/DevOps.
- Complejidad justificada.
- Riesgos listados.

## Fuentes

- Debezium — Outbox Event Router + CloudEvents — https://debezium.io/documentation/reference/stable/integrations/cloudevents.html (2026-08-04).
- AsyncAPI / CloudEvents roles en DevOps EDA — https://www.asyncapi.com/blog/async_standards_compare (2026-08-04).
- Patrones de entrega, lag y EOS (síntesis Kafka/CloudEvents 2026, contrastada) — 2026-08-04.
