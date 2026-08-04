---
name: evaluar-readiness-liberacion
description: Evalúa readiness de liberación (go / no-go / go-with-risks) consolidando evidencia del squad QA. Úsala antes de recomendar producción, un release candidate o firmar un quality gate final.
metadata:
  author: yzylabs
  version: "1.0"
---

# Evaluar readiness de liberación

## Propósito

Emitir una recomendación de liberación basada en evidencia de pruebas y riesgo residual, consolidando el departamento QA.

## Entradas

- Gates / exit criteria acordados.
- Informes de Tashigi / Kalifa / Kuma / Kaido (o estado stub + gaps).
- Defectos abiertos y waivers.
- Resultados NFR (perf, seguridad básica de prueba si aplica).
- Cambios de último minuto en el build.

## Procedimiento

1. Verifica entry del gate final (build identificado, notas de release, ambiente).
2. Cruza exit criteria vs evidencia real por tipo de prueba crítico.
3. Inventaría defectos abiertos por severidad y mapea a riesgos P0/P1.
4. Evalúa riesgo residual: probabilidad/impacto restantes y mitigaciones (monitoreo, feature flag, rollback).
5. Emite recomendación: **go** / **no-go** / **go-with-risks**.
6. Si go-with-risks: lista condiciones, aceptador de negocio (vía Luffy), triggers de abort.
7. Adjunta EVIDENCE y limita afirmaciones (“probado en X, no en Y”).

## Salida

```md
## Build / release
## Recomendación: go | no-go | go-with-risks
## Exit criteria
| Criterio | Estado | Evidencia |
## Defectos abiertos materiales
## Riesgo residual
## Condiciones / waivers
## No cubierto / limitaciones
## REPORT listo para Luffy
```

## Casos límite

- Células stub sin ejecución: `no-go` o `BLOCKED` con gap explícito; no finjas readiness.
- Perf no corrido por falta de ambiente: no-go para SLOs críticos o go-with-risks solo si negocio acepta.
- Hotfix de última hora: reabre subset de regresiones; no reutilices evidencia vieja ciegamente.

## Validación

- Recomendación alineada a evidencia, no a la fecha.
- Limitaciones explícitas.
- Identidad: firma como `usopp-director-qa`, no como todólogo.

## Criterios de terminado

- Recomendación clara con EVIDENCE.
- Riesgos residuales y decisiones de aceptación listadas.
- Consolidado departamental listo para `REPORT_TO: luffy-coordinador`.

## Fuentes

- ISTQB CTAL-TM v3.0 — Assess and report test progress; test completion; defect info for decisions — https://istqb.org/certifications/certified-tester-advanced-level-test-management-ctal-tm-v3-0/ (2026-08-04)
- Quality gates / release readiness — síntesis contrastada con CTAL-TM, 2026-08-04
