---
name: modelar-evento-dominio
description: Modela un evento de dominio con envelope CloudEvents 1.0 (id, source, type, specversion, data/schema). Úsala cuando debas definir o normalizar el contrato de un evento antes de publicar o consumir.
metadata:
  author: yzylabs
  version: "1.0"
---

# Modelar evento de dominio

## Propósito

Convertir un hecho de negocio en un evento interoperable: envelope estable, tipo versionado, payload mínimo y referencias a schema — sin inventar canales AsyncAPI formales.

## Entradas

- Hecho de negocio / transición de estado.
- Productor esperado (`source`).
- Consumidores conocidos o hipotéticos.
- AsyncAPI / schema existente (si hay).
- Restricciones de PII y tamaño.

## Procedimiento

1. Nombra el `type` como `{dominio}.{entidad}.{accion}.vN` (o alinea al AsyncAPI existente).
2. Fija `specversion: "1.0"` si usas CloudEvents.
3. Define `id` (UUID/ULID único por ocurrencia) y `source` (URI estable del productor).
4. Añade `subject` / `time` / `dataschema` cuando aporten trazabilidad.
5. Diseña `data` compacto: IDs y deltas; enlaza blobs grandes en lugar de embeberlos.
6. Declara breaking vs compatible (nuevo `.vN` si rompe consumidores).
7. Lista consumidores y efectos esperados (matriz corta).

## Salida

```md
## Evento
## Envelope (CloudEvents)
## Payload / schema
## Compatibilidad / versionado
## Productor / consumidores
## Riesgos PII / tamaño
```

## Casos límite

- Solo hay log interno → no lo promociones a evento de integración sin mandato.
- Payload con PII → minimiza o referencia; no copies secretos.
- Conflicto con AsyncAPI de Robin → no inventes; escala gap.

## Validación

- Campos REQUIRED de CloudEvents presentes si aplica (`id`, `source`, `specversion`, `type`).
- `type` versionado y estable.
- Payload sin secretos embebidos.

## Criterios de terminado

- Un implementador puede serializar el evento sin adivinar headers.
- Versionado y consumidores quedan explícitos.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | `PaymentCaptured` con orderId | CloudEvents + type versionado + data mínimo |
| Ambiguo | “Avisar cuando cambie algo” | Preguntas de entidad/acción + 2 candidatos de `type` |
| Límite | Evento con PDF de 20MB | Envelope + link a blob; no embed |

## Fuentes

- CloudEvents Spec 1.0.2 — https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md (2026-08-04).
- CloudEvents Primer — https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/primer.md (2026-08-04).
