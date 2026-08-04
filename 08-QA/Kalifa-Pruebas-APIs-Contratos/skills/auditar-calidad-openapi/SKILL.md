---
name: auditar-calidad-openapi
description: Audita calidad y completeness de OpenAPI/AsyncAPI con lint (Spectral u equivalente) y checklist de errores/examples/security. Úsala cuando haya que gobernar la spec antes de generar pruebas de contrato.
metadata:
  author: yzylabs
  version: "1.0"
---

# Auditar calidad OpenAPI / AsyncAPI

## Propósito

Evaluar si el contrato es apto como fuente de verdad para pruebas: parseable, lintable y suficientemente completo (errores, examples, seguridad) antes de schema-first o CDCT.

## Entradas

- Ruta o contenido OpenAPI 3.x / AsyncAPI.
- Ruleset Spectral (o política del repo) si existe.
- Alcance: interno (Robin) vs externo (Sabo), si se conoce.

## Procedimiento

1. Confirma versión del documento (`openapi` / `asyncapi`) y que parsea.
2. Ejecuta o simula lint con ruleset (`spectral:oas` / `spectral:asyncapi` o el del repo); registra severidades.
3. Checklist de completeness mínimo:
   - `info` (title, version)
   - `operationId` estables en ops críticas
   - securitySchemes / security en ops autenticadas
   - respuestas de error documentadas (al menos 401/403/404/4xx/5xx relevantes)
   - examples o `examples` arrays en schemas críticos
4. Marca “happy-path-only” si faltan unhappy paths documentados.
5. Clasifica hallazgos `blocker|major|minor|info` con ubicación (path/op).
6. Propón dueño de remediación (Robin interno / Sabo externo).

## Salida

- Informe de calidad de spec (tabla hallazgos).
- Resultado de lint (comando/salida o equivalente documentado).
- Veredicto: `apto-para-contrato` | `apto-con-limitaciones` | `no-apto`.

## Casos límite

- Spec 2.0/Swagger legacy → limita herramientas; recomienda migración; no inventes 3.1.
- Multi-file `$ref` rotos → blocker de parseo.
- Solo AsyncAPI sin canales/mensajes → no-apto.

## Validación

- Documento parseable o error de parseo explícito.
- Hallazgos con ubicación y severidad.
- Veredicto justificado.

## Criterios de terminado

- Informe entregado a Usopp con evidencia de lint/checklist.
- Gaps de completeness listados con dueño.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | OpenAPI 3.1 con ops y errores | Lint + veredicto apto o limitaciones menores |
| Ambiguo | “Revisa el swagger” sin ruta | Pregunta ruta/versión; no inventa spec |
| Límite | Solo 200 OK documentados | no-apto o limitaciones + lista unhappy paths faltantes |

## Fuentes

- OpenAPI Specification 3.1.x — https://spec.openapis.org/oas/v3.1 (2026-08-04).
- Spectral — https://stoplight.io/open-source/spectral y https://meta.stoplight.io/docs/spectral (2026-08-04).
- AsyncAPI reference — https://www.asyncapi.com/docs/reference (2026-08-04).
