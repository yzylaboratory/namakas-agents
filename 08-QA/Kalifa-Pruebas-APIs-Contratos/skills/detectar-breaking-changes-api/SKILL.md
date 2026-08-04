---
name: detectar-breaking-changes-api
description: Detecta y clasifica breaking changes entre dos versiones de OpenAPI/AsyncAPI (oasdiff/openapi-diff u equivalente). Úsala cuando haya baseline y se deba gatear merges o releases por compatibilidad.
metadata:
  author: yzylabs
  version: "1.0"
---

# Detectar breaking changes de API

## Propósito

Comparar el contrato candidato contra un baseline y clasificar cambios como safe, dangerous o breaking con evidencia accionable para Usopp y owners de remediación.

## Entradas

- Spec candidata (PR/branch).
- Baseline (main, tag, versión publicada, portal).
- Política de versionado (major URL, header, etc.) si existe.
- Alcance: interno vs externo público.

## Procedimiento

1. Fija baseline explícito (commit/tag/ruta); sin baseline → no inventes; `BLOCKED`.
2. Ejecuta diff de contratos (oasdiff, openapi-diff u herramienta del repo).
3. Clasifica cada cambio:
   - **breaking**: remove field/op, type narrow, new required, status removals, auth más estricta incompatible
   - **dangerous**: semantic change ambiguous, default changes
   - **safe**: additive opcionales, docs
4. Cruza con política de versionado: ¿hay major/migración/notice?
5. Para APIs externas, señala necesidad de changelog/deprecación (Sabo).
6. Recomienda gate: fail CI en breaking sin label/aprobación explícita.

## Salida

- Informe de diff clasificado.
- Lista breaking con path/op y impacto.
- Recomendación de versión/migración o rechazo de merge.

## Casos límite

- Renames disfrazados de remove+add → tratar como breaking salvo compat layer documentada.
- Solo AsyncAPI → usa diff AsyncAPI-aware; no fuerces herramienta OpenAPI.
- Baseline y candidata en major distinto ya acordado → documenta expected breaking.

## Validación

- Baseline y candidata identificados.
- Cada breaking tiene evidencia de diff.
- Gate recomendado explícito.

## Criterios de terminado

- Informe clasificado entregado.
- Decisiones requeridas (aprobar breaking / bump major) listadas para Usopp.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | main vs PR OpenAPI | Diff clasificado + gate |
| Ambiguo | “¿Rompe?” sin baseline | BLOCKED pidiendo baseline |
| Límite | Campo required nuevo en response consumer | breaking + dueño consumer/provider |

## Fuentes

- OpenAPI 3.1 — https://spec.openapis.org/oas/v3.1 (2026-08-04).
- Total Shift Left — Contract testing / breaking changes (secundaria) — https://totalshiftleft.ai/learn/testing/contract-testing (2026-08-04).
- oasdiff (comunidad) — https://github.com/tufin/oasdiff (2026-08-04).
