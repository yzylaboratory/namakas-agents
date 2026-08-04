---
name: alinear-consistencia-distribuida
description: Alinea patrones de consistencia entre microservicios, persistencia y eventos (database-per-service, outbox, idempotencia, sagas, eventual vs fuerte). Úsala cuando haya dual-writes, acoplamiento por DB compartida, sagas incompletas o dudas sync vs async.
metadata:
  author: yzylabs
  version: "1.0"
---

# Alinear consistencia distribuida

## Propósito

Hacer explícitos los trade-offs de consistencia en el departamento Backend y elegir patrones verificables, evitando dual-writes silenciosos y schemas compartidos entre bounded contexts.

## Entradas

- Flujos de negocio afectados (comando → persistencia → evento → consumidores).
- Mapa de stores y topics involucrados.
- Requisitos de lectura fuerte vs eventual (p. ej. saldo antes de débito).
- Restricciones de latencia, orden y compliance/auditoría.

## Procedimiento

1. Dibuja el flujo actual: writers, stores, brokers, consumers, lecturas críticas.
2. Clasifica cada frontera:
   - **Fuerte** (misma transacción / lectura del write model).
   - **Eventual** (proyecciones, integración entre servicios).
3. Detecta anti-patrones:
   - DB/schema compartido entre servicios.
   - Dual-write (DB + publish) sin outbox/transactional messaging.
   - Consumers no idempotentes / sin DLQ.
   - Saga implícita sin compensación ni timeout.
4. Propón patrón objetivo por frontera: API sync, outbox, inbox/idempotency key, saga/orquestación-coreografía, CQRS read model.
5. Define contratos de evento (schema, versión, compatibilidad) y ownership.
6. Lista gaps y plan Now/Next; escala a Law si el rediseño cruza dominios.

## Salida

```md
## Flujos analizados
## Matriz de consistencia
| Frontera | Hoy | Objetivo | Patrón | Owner |
## Anti-patrones detectados
## Contratos de evento / schema
## Plan de remediación
## Riesgos y lecturas críticas
## Escalaciones
```

## Casos límite

- Lectura crítica financiera: no forzar eventual; documentar read-from-write o locking explícito.
- Replay masivo: exigir retención, idempotencia y control de blast radius (lecciones operativas de streaming).
- Migración de monolito: transición por strangler + ownership de datos por contexto, no “share DB forever”.

## Validación

- Cada frontera tiene tipo de consistencia declarado.
- No queda dual-write sin patrón mitigador o excepción con expiry.
- Owners de store y de topic están nombrados.

## Criterios de terminado

- Matriz usable por X-Drake / Pudding / Apoo (cuando existan) y por Law.
- Anti-patrones priorizados.
- Decisiones de trade-off explícitas.

## Fuentes

- Microsoft — Data considerations for microservices — https://learn.microsoft.com/en-us/azure/architecture/microservices/design/data-considerations (2026-08-04)
- Microsoft — Data sovereignty per microservice — https://learn.microsoft.com/en-us/dotnet/architecture/microservices/architect-microservice-container-applications/data-sovereignty-per-microservice (2026-08-04)
- Confluent — Event-Driven Architecture — https://www.confluent.io/learn/event-driven-architecture/ (2026-08-04)
- Atlassian StreamHub — operational resilience at event scale — consultado 2026-08-04
