---
name: preparar-handoff-persistencia-eventos
description: Prepara el handoff de requisitos de persistencia (Pudding) y eventos (Apoo) para un MS financiero, incluyendo outbox. Úsala cuando el diseño de dominio deba transferirse a células de datos o mensajería sin dual-write.
metadata:
  author: yzylabs
  version: "1.0"
---

# Preparar handoff de persistencia y eventos

## Propósito

Empaquetar lo que Pudding y Apoo necesitan para sostener el MS: modelo mínimo, constraints de idempotencia, outbox y contratos de eventos — sin implementar el broker ni el esquema completo en su lugar.

## Entradas

- Bounded context e invariantes.
- Casos de uso mutantes y eventos de dominio previstos.
- Decisiones de saga (si existen).
- Restricciones de stack (SQL/NoSQL, Kafka, etc.) si constan.

## Procedimiento

1. Lista agregados y tablas/colecciones mínimas con claves e invariantes.
2. Especifica constraints únicos para idempotency keys / business keys.
3. Diseña outbox: mismos TX que el aggregate; campos (id, type, payload, created_at, published_at).
4. Define relay esperado (polling / CDC) como requisito; no elijas herramienta de plataforma sin Franky/Apoo.
5. Cataloga eventos de dominio (nombre, payload mínimo, ordering key, sensibilidad).
6. Exige consumidores idempotentes (Apoo): processed-message store / dedup.
7. Separa “requisito X-Drake” vs “decisión Pudding/Apoo pendiente”.
8. Emite paquete de handoff con criterios de aceptación verificables.

## Salida

```md
## Destinatarios
## Modelo mínimo / constraints
## Outbox
## Eventos de dominio
## Requisitos de consumo
## Decisiones pendientes (Pudding/Apoo)
## Criterios de aceptación
```

## Casos límite

- Evento sin outbox propuesto → rechaza el handoff.
- Payload con PII/PAN → exige reducción/tokenización; escala Fujitora si hace falta.
- Pudding/Apoo aún stub → handoff igual; Katakuri escala forja o ejecución.

## Validación

- Outbox atómico con el commit del aggregate.
- Eventos tienen ordering/dedup pensados.
- No hay dual-write implícito.

## Criterios de terminado

- Pudding/Apoo (o Katakuri) pueden ejecutar sin reinterpretar el dominio.
- Gaps de plataforma listados.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Hold created + event | Outbox + evento + constraint idempotency |
| Ambiguo | “Publica a Kafka después del save” | Rechazo dual-write + outbox obligatorio |
| Límite | Evento con PAN en clear | Redacción + escalamiento seguridad |

## Fuentes

- microservices.io — Transactional Outbox — https://microservices.io/patterns/data/transactional-outbox.html (2026-08-04).
- Relacionado: Saga pattern (necesidad de outbox en pasos).
