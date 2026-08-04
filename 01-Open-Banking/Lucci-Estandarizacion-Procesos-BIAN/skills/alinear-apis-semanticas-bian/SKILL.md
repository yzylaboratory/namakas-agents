---
name: alinear-apis-semanticas-bian
description: Alinea APIs existentes o previstas con Semantic APIs BIAN (action terms, paths CR/BQ, OAS3/AsyncAPI oficiales). Úsala cuando debas mapear endpoints o eventos a operaciones de Service Domain con evidencia del repo oficial.
metadata:
  author: yzylabs
  version: "1.0"
---

# Alinear APIs semánticas BIAN

## Propósito

Relacionar superficies API (HTTP/eventos) del MS/orch con especificaciones Semantic API BIAN de la misma release, sin inventar operaciones.

## Entradas

- Service Domains (+ CR/BQ si existen).
- Inventario de APIs/eventos del producto o recon.
- Versión/release BIAN (p. ej. release14.0.0).
- Rutas a YAML oficiales o URL del árbol `bian-official/public`.

## Procedimiento

1. Localiza specs del Service Domain en `bian-official/public` para la release (OAS3 y/o AsyncAPI).
2. Extrae action terms y paths (patrón típico `/ServiceDomain/Initiate`, `/{id}/Retrieve`, BQ anidados).
3. Mapea cada endpoint/evento del producto a operación BIAN **si** hay correspondencia semántica evidenciada.
4. Registra gaps: producto sin match BIAN; BIAN sin implementación local.
5. Anota alineación ISO 20022 / DDD solo si la variante de spec lo documenta (p. ej. `apis-iso20022_ext-ddd`).
6. No renombres operaciones BIAN para “sonar mejor” en el producto dentro del mapeo.
7. Prepara trazabilidad para el handoff (SD → op → API local).

## Salida

```md
## Alineación Semantic API
- Release BIAN:
- Variante spec: [BOM-extended | ISO20022-ext-ddd | otra]
- Fuente repo:

| API/evento local | Service Domain | Action term / path BIAN | Evidencia YAML | Gap |
|---|---|---|---|---|

### Gaps
- ...
```

## Casos límite

- API local agrega varios SDs → descomponer; no forzar un solo SD.
- Solo Async en producto / solo OAS en BIAN (o viceversa) → mapear patrón de mensaje; marcar asimetría.
- Sin YAML para un SD en la release → no inventes paths; hueco.

## Validación

- Cada fila con match cita path/archivo YAML o URL.
- Gaps listados.
- Action terms coherentes con la spec, no con costumbre.

## Criterios de terminado

- Matriz API↔BIAN lista para handoff o para Robin (consumo semántico).
- Cero operaciones inventadas.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | OAS local + YAML SD release14 | Trazabilidad path↔action term |
| Ambiguo | Endpoint “/pay” genérico | Descomposición o gap; sin forzar SD |
| Límite | Pedido inventar `/Initiate` sin YAML | Rechazo + hueco |

## Fuentes

- https://github.com/bian-official/public (release14.0.0 semantic-apis / apis-iso20022_ext-ddd) — consultado 2026-08-04.
- BIAN Semantic API Practitioner’s Guide v8.1 — 2024-12.
- BIAN news Service Landscape 14.0 (interop APIs/messaging) — https://bian.org/news-room/bian-unveils-new-service-landscape-14-0-to-accelerate-ai-ready-banking-architecture/ — 2026-03-13.
