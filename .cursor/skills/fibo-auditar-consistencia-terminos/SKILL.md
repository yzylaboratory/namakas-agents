---
name: fibo-auditar-consistencia-terminos
description: Audita consistencia de términos entre APIs, schemas y glosarios frente al vocabulario FIBO alineado; detecta drift, homónimos y recomendaciones accionables. Úsala cuando debas revisar coherencia semántica en contratos o modelos de datos.
metadata:
  author: yzylabs
  version: "1.0"
---

# Auditar consistencia de términos

## Propósito

Encontrar inconsistencias semánticas materiales y proponer correcciones alineadas al glosario FIBO del alcance.

## Entradas

- OpenAPI/AsyncAPI, schemas, diccionarios o extracts de código.
- Glosario canónico / HANDOFF_FIBO (si existe).
- Alcance de auditoría (servicios, bounded context).

## Procedimiento

1. Inventaría términos en superficies (nombres de campos, schemas, descripciones).
2. Contrasta con glosario canónico alineado a FIBO.
3. Clasifica hallazgos: conflicto | homónimo | sin definición | drift entre servicios | ok.
4. Prioriza por impacto (interop, riesgo regulatorio, ambigüedad de party/account/money).
5. Propón acción: renombrar | alias documentado | `description`/`x-semantic-ref` | escalar definición.
6. No reescribas el tratado completo (eso es Robin); entrega hallazgos semánticos.
7. Si falta glosario base, produce uno mínimo o bloquea con faltantes.

## Salida

```md
## Auditoría semántica

- Alcance: [...]
- Resumen: N hallazgos (críticos / medios / bajos)

| Término | Dónde | Problema | FIBO/canónico | Acción |
|---|---|---|---|---|

- Recomendaciones prioritarias: [...]
- Pendientes: [...]
```

## Casos límite

- Mismo meaning, distinto spelling en v1/v2 → recomienda alias + plan de deprecación.
- Término marketing en description → no lo trates como concepto canónico.
- Sin acceso a FIBO Viewer en el entorno → usa evidencia ya citada en handoff; no inventes.

## Validación

- Cada hallazgo material tiene ubicación y acción.
- No se inventan equivalencias FIBO nuevas sin evidencia (escala a alineación).

## Criterios de terminado

- Informe accionable para owners de API/datos.
- Críticos listados primero.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Dos OpenAPI con `customerId` vs `partyId` | Hallazgo de homonimia/roles |
| Ambiguo | Descriptions vacías | Hallazgos “sin definición” |
| Límite | Pedido de “fix OpenAPI ya” | Hallazgos + handoff a Robin; no dueño del contrato |

## Fuentes

- https://spec.edmcouncil.org/fibo (2026-08-04)
- Práctica de data meaning / semantic consistency (síntesis EDM Council FIBO overview, 2026-08-04)
- `references/contrato-handoff-fibo.md`
