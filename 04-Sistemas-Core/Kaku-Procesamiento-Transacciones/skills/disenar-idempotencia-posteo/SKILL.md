---
name: disenar-idempotencia-posteo
description: Diseña claves de idempotencia, ventanas de deduplicación y semántica de replay para aceptación y posteo de transacciones. Úsala cuando existan reintentos, colas at-least-once o riesgo de doble cargo/asiento.
metadata:
  author: yzylabs
  version: "1.0"
---

# Diseñar idempotencia de posteo

## Propósito

Garantizar que procesar la misma instrucción lógica N veces produzca el mismo resultado de negocio que procesarla una vez (exactly-once efectivo a nivel de asiento).

## Entradas

- Productor (API, cola, file, gateway).
- Semántica de entrega (at-least-once / at-most-once).
- Ventana de negocio requerida para deduplicación.
- Distinción aceptación vs posteo ledger.
- Identificadores de negocio disponibles.

## Procedimiento

1. Define la unidad lógica: qué constituye “la misma” transacción.
2. Elige clave de idempotencia (cliente+operación+id lógico; o hash canónico de instrucción).
3. Separa capas: (A) dedupe de mensaje/API, (B) dedupe de posteo ledger.
4. Define store: TTL corto para locks pendientes + persistencia larga para replay de respuesta.
5. Especifica respuestas: first success → cache; duplicate → same response; conflict (same key, different body) → error explícito.
6. Relaciona con `MsgId` determinista en envíos interbank (no regenerar en retry).
7. Documenta fallos: crash mid-post, timeout tras commit, poison messages.
8. Entrega spec de idempotencia + pruebas de aceptación.

## Salida

```md
# Idempotencia — [Flujo]

## Unidad lógica
## Clave(s)
## Capas (API / posteo)
## Store y TTL
## Semántica de replay / conflicto
## Relación MsgId / EndToEnd
## Fallos cubiertos
## Pruebas de aceptación
```

## Casos límite

- Misma clave, payload distinto → conflicto, no silently overwrite.
- Posteo commit + timeout al cliente → replay debe devolver éxito original, no segundo asiento.
- Ventana de dedupe menor que ventana de retry del cliente → BLOCKED.

## Validación

- Clave no es solo request-id de red efímero sin anclar a negocio (salvo justificado).
- Replay no crea segundo asiento.
- Conflicto definido.

## Criterios de terminado

- Spec implementable.
- Casos de retry cubiertos.
- Riesgos residuales listados.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | API REST con retries | Clave + store + replay |
| Ambiguo | “Que no se duplique” sin productor | Preguntas + borrador mínimo |
| Límite | Commit OK, response lost | Replay idempotente del resultado |

## Fuentes

- Prácticas industry de idempotency keys en payment APIs — 2026-08-04
- Determinismo de `MsgId` en pipelines ISO 20022 — contraste técnico 2026-08-04
