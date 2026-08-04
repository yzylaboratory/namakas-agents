---
name: disenar-pruebas-contrato-schema-first
description: Diseña o documenta suites schema-first que validen la implementación contra OpenAPI (p. ej. Schemathesis/Dredd). Úsala cuando el provider deba demostrar conformidad con su spec.
metadata:
  author: yzylabs
  version: "1.0"
---

# Diseñar pruebas de contrato schema-first

## Propósito

Definir cómo se prueba que el servicio cumple el OpenAPI: validación runtime de status, headers y bodies frente al schema, incluyendo exploración property-based cuando sea viable.

## Entradas

- OpenAPI parseable (preferible ya auditado).
- Base URL / entorno (sandbox, mock, local).
- Restricciones de auth (client credentials, API key de test).
- Política de datos (solo sintéticos).

## Procedimiento

1. Confirma que la spec es `apto-para-contrato` o documenta limitaciones aceptadas por Usopp.
2. Selecciona enfoque: middleware/validator en tests existentes, cliente generado, o property-based (Schemathesis u equivalente).
3. Define cobertura mínima: ops críticas del alcance + unhappy paths documentados.
4. Configura auth de test sin secretos en el reporte (referencia a vault/env).
5. Documenta comandos CI sugeridos y criterios de fail.
6. Si no hay runtime, entrega diseño de suite + mocks Prism/equivalente y marca limitaciones.
7. Registra supuestos (timeouts, rate limits, datos de provider state).

## Salida

- Diseño de suite schema-first (alcance, herramientas, comandos).
- Resultados de ejecución si hubo entorno (pass/fail por op).
- Lista de ops no cubiertas y razón.

## Casos límite

- Spec incompleta → no expandas cobertura inventando schemas; vuelve a `auditar-calidad-openapi`.
- Producción como base URL → `BLOCKED` sin mandato explícito.
- 3.0 vs 3.1 → declara compatibilidad de herramienta; no asumas JSON Schema 2020-12 en 3.0.

## Validación

- Cada op en alcance tiene criterio de conformidad explícito.
- Evidencia de run o diseño reproducible.
- Sin secretos en artefactos.

## Criterios de terminado

- Suite diseñada (y ejecutada si había entorno) con evidencia.
- Gaps de cobertura listados.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | OpenAPI + sandbox URL | Diseño + run o plan CI con fail criteria |
| Ambiguo | “Haz contract tests” sin URL | Diseño + BLOCKED/limitaciones por falta de runtime |
| Límite | Spec sin 4xx | Limitaciones + no declara cobertura unhappy path |

## Fuentes

- OpenAPI 3.1 — https://spec.openapis.org/oas/v3.1 (2026-08-04).
- Schemathesis docs — https://schemathesis.readthedocs.io/ (2026-08-04).
- QASkills OpenAPI 3.1 contract testing (secundaria) — https://qaskills.sh/blog/openapi-3-1-contract-testing-guide-2026 (2026-08-04).
