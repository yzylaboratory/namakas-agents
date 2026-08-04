---
name: especificar-contratos-integracion
description: Especifica contratos sync/async de integración (REST, colas, headers, SLAs, idempotencia, DLQ). Úsala cuando haya que formalizar cómo se invoca o se publica hacia/desde el core.
metadata:
  author: yzylabs
  version: "1.0"
---

# Especificar contratos de integración

## Propósito

Dejar explícito el contrato operativo entre productores, capa de integración y core: payload, correlación, fallos y garantías de entrega.

## Entradas

- Flujo y topología aprobada (o borrador).
- Canónico / schemas.
- Preferencias REST vs cola.
- SLAs de negocio (latencia, ventana).
- Límites del core (timeouts, rate).

## Procedimiento

1. Elige estilo por operación: request/response vs fire-and-forget vs request + callback.
2. Define endpoint/topic/queue naming y ownership.
3. Especifica headers: correlation id, idempotency key, content-type, schema version.
4. Define payload (referencia al canónico) y ejemplos sintéticos (sin PII real).
5. Declara semántica de entrega y deduplicación en destino.
6. Política de reintentos (backoff, max, qué errores son retryable).
7. DLQ / poison message: criterio de enrutado y runbook mínimo.
8. Matriz de errores (técnicos vs de negocio) y timeouts.
9. SLAs observables y métricas mínimas (éxito, lag, DLQ depth).

## Salida

```md
## Operaciones / estilo
## Endpoints o topics
## Headers / correlación / idempotencia
## Payload (ref canónico)
## Reintentos / DLQ
## Errores / timeouts
## SLAs / métricas
## Ejemplos sintéticos
```

## Casos límite

- Core sin soporte de idempotency → exige capa de deduplicación + reconciliación; no ignores el gap.
- Fan-out a varios consumidores → documenta orden y ownership de side-effects.
- Mezcla batch + online → contratos separados; no unifiques a la fuerza.

## Validación

- Toda operación con efecto financiero tiene idempotency key.
- DLQ y reintentos definidos.
- Ejemplos sin secretos ni PII real.

## Criterios de terminado

- Un consumidor puede integrar sin preguntas abiertas sobre headers o fallos.
- Gaps de capacidad del core tienen dueño (Kaku/Iceburg).

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Alta de transferencia async a cola core | Contrato con idempotency + DLQ + SLA |
| Ambiguo | “Expongamos una API al core” | Preguntas sync/async + 2 opciones de contrato |
| Límite | Core timeout 2s con proceso 30s | Async + callback/status; rechazo de sync forzado |

## Fuentes

- 6B Core Banking Integration (REST + queues + security) — https://6b.finance/insight/core-banking-system-integration-using-iso-20022-rest-apis-and-legacy-message-queues/ (2026-08-04).
- BlazeTrends Core Banking APIs — https://blazetrends.com/how-core-banking-apis-connect-with-external-financial-systems/ (2026-08-04).
- IoT Digital Twin PLM Architecture 2026 — https://iotdigitaltwinplm.com/iso-20022-migration-payments-architecture-2026/ (2026-08-04).
