---
name: catalogar-eventos-de-dominio
description: Construye el catálogo de eventos de dominio (nombre, payload mínimo, productor, consumidores, clave e idempotencia). Úsala cuando haya que inventariar o normalizar eventos antes de AsyncAPI o implementación.
metadata:
  author: yzylabs
  version: "1.0"
---

# Catalogar eventos de dominio

## Propósito

Producir un catálogo estable de eventos de dominio que sirva de fuente para envelopes, schemas y contratos AsyncAPI.

## Entradas

- Topología EDA o lista de flujos.
- Lenguaje ubicuo / glosario del dominio.
- Handoffs BIAN/FIBO si los eventos son bancarios/financieros.
- Specs o topics existentes.

## Procedimiento

1. Extrae candidatos a evento desde casos de uso (hechos del pasado: `OrderPlaced`, no `CreateOrder` como evento de dominio salvo que sea comando).
2. Distingue **comando**, **evento de dominio** y **mensaje técnico**.
3. Asigna nombre estable y `type` tentativo (alineable a CloudEvents `type`).
4. Define payload mínimo (campos obligatorios) sin PII real en ejemplos.
5. Registra productor dueño, consumidores, canal, clave de partición/orden y estrategia de idempotencia.
6. Añade correlation/causation ids cuando haya cadenas de proceso.
7. Marca TBD y bloqueos; no inventes consumidores.
8. Si hay conflicto de nombres entre equipos, registra alias y propone canónico.

## Salida

```md
## Catálogo de eventos
| Evento | type | Productor | Consumidores | Canal | Clave | Idempotencia | Schema |
## Comandos vs eventos vs técnicos
## Alias y deprecaciones
## Huecos / TBD
```

## Casos límite

- “Emitiremos algo” sin payload → bloqueo; schema mínimo o aplazado explícito.
- Evento bancario sin HANDOFF_BIAN/FIBO → escala; no inventes semántica de dominio.
- Mismo hecho con dos nombres → normaliza o documenta alias; no dejes drift.

## Validación

- Cada evento de dominio tiene productor o TBD explícito.
- No hay secretos/PII reales en ejemplos.
- Comandos no están etiquetados como eventos de dominio sin justificación.

## Criterios de terminado

- Catálogo navegable y listo para envelope/schema/AsyncAPI.
- Huecos listados.
- Naming estable acordado o marcado como decisión requerida.

## Fuentes

- CloudEvents Spec v1.0.2 (`type`, `id`, `source`) — https://github.com/cloudevents/spec/blob/ce@v1.0.2-branch/cloudevents/spec.md (2026-08-04).
- AsyncAPI — channels/messages como contrato de catálogo — https://www.asyncapi.com/docs/reference/specification/latest (2026-08-04).
