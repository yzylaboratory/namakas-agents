---
name: validar-coherencia-contrato-implementacion
description: Detecta drift entre OpenAPI/AsyncAPI, implementación runtime y (si aplica) producto externo o Pacts. Úsala cuando haya sospecha de desalineación spec↔código↔portal.
metadata:
  author: yzylabs
  version: "1.0"
---

# Validar coherencia contrato ↔ implementación

## Propósito

Producir una matriz de drift que explique dónde diverge la verdad: spec canónica, runtime, consumidores y exposición externa — sin reescribir el contrato.

## Entradas

- OpenAPI/AsyncAPI canónico (Robin o repo).
- Evidencia runtime (logs de contract suite, respuestas capturadas, gateway).
- OpenAPI externo / portal (Sabo) si aplica.
- Pacts si existen.
- Resultados previos de lint/schema-first/CDC.

## Procedimiento

1. Inventaría fuentes de verdad declaradas por la misión.
2. Compara spec canónica vs respuestas/observables runtime (status, required fields, enums).
3. Compara spec interna vs externa (campos/ops filtrados vs leak de internos).
4. Compara Pacts vs OpenAPI (campos usados no documentados o documentados no usados).
5. Clasifica cada drift: `spec-stale` | `impl-stale` | `portal-stale` | `consumer-stale` | `unknown`.
6. Asigna dueño propuesto (Robin, backend/Katakuri, Sabo, consumer, Usopp).
7. Prioriza por severidad e impacto de release.

## Salida

- Matriz de drift (fuente A vs B, evidencia, severidad, dueño).
- Recomendación de remediación ordenada.
- Flags de riesgo (seguridad, breaking silencioso).

## Casos límite

- Solo una fuente disponible → COMPLETED_WITH_LIMITATIONS; no inventes la otra.
- Mock que siempre cumple spec → no equivalga a prod; declara limitación de entorno.
- BIAN/FIBO terms → no audites semántica de dominio; escala a Lucci/FIBO si el hallazgo es de glosario.

## Validación

- Cada fila de drift tiene evidencia.
- Dueños propuestos sin asumir autoridad de merge.
- Separación clara de tipos de stale.

## Criterios de terminado

- Matriz entregada a Usopp.
- Sin remediación inventada del contrato por Kalifa.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Spec + fallos Schemathesis | Matriz impl-stale/spec-stale con ops |
| Ambiguo | “Hay drift” sin artefactos | Pregunta fuentes; BLOCKED si faltan |
| Límite | Portal muestra campo ausente en gateway | portal-stale o gateway-stale + Sabo/ops |

## Fuentes

- OpenAPI 3.1 — https://spec.openapis.org/oas/v3.1 (2026-08-04).
- Spectral anti-drift practices — https://stoplight.io/open-source/spectral (2026-08-04).
- Pact + OpenAPI complementarity (secundaria) — https://qaskills.sh/blog/api-contract-testing-microservices (2026-08-04).
