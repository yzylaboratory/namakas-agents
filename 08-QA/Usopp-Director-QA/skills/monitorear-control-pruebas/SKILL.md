---
name: monitorear-control-pruebas
description: Monitorea y controla el progreso de pruebas con métricas, desviaciones y acciones correctivas. Úsala cuando haya que reportar estado QA, replanificar esfuerzo o controlar un ciclo de pruebas en curso.
metadata:
  author: yzylabs
  version: "1.0"
---

# Monitorear y controlar pruebas

## Propósito

Mantener el plan de pruebas bajo control: detectar desviaciones temprano, actuar y reportar hechos a Luffy y stakeholders.

## Entradas

- Plan / estrategia y backlog RBT.
- Datos de ejecución (pass/fail, bloqueados, no ejecutados).
- Defectos abiertos por severidad.
- Capacidad real vs estimada.
- Estado de ambientes y pipelines.

## Procedimiento

1. Selecciona métricas mínimas alineadas a objetivos (progreso, calidad producto, efectividad, bloqueos).
2. Establece cadencia de monitoreo (diario/por sprint) y umbrales de alerta.
3. Compara plan vs real: cobertura de riesgos P0, ejecución, defectos, automatización flaky.
4. Clasifica desviaciones: ambiente, alcance, calidad del build, capacidad, datos.
5. Define acciones de control: re-priorizar, cortar alcance de bajo riesgo, escalar ambiente, pedir hotfix.
6. Actualiza forecast de readiness (tendencia, no deseo).
7. Emite informe corto con decisiones pedidas.

## Salida

```md
## Periodo / release
## Métricas
| Métrica | Plan | Real | Tendencia |
## Desviaciones
## Acciones de control
## Riesgos P0 aún abiertos
## Forecast de gate
## Decisiones requeridas
```

## Casos límite

- Métricas incompletas: reporta “desconocido” + plan de instrumentación; no inventes %.
- Suites verdes con riesgos P0 sin ejecutar: progreso engañoso → alerta.
- Hiperfoco en pass rate: equilibra con riesgo residual y defectos sevirity.

## Validación

- Cada métrica tiene fuente de datos.
- Toda desviación material tiene acción o escalamiento.
- El informe distingue hecho vs inferencia.

## Criterios de terminado

- Snapshot usable por Luffy sin reinterpretar.
- Acciones de control con dueño y plazo.
- Forecast de gate explícito.

## Fuentes

- ISTQB CTAL-TM v3.0 — Test Metrics; Monitoring, Control, and Completion; Test Reporting — https://istqb.org/certifications/certified-tester-advanced-level-test-management-ctal-tm-v3-0/ (2026-08-04)
- ISTQB Glossary — test monitoring, test control (2026-08-04)
