---
name: disenar-arquitectura-automatizacion
description: Diseña la arquitectura de automatización (gTAA/TAA), capas, patrones y testabilidad del SUT. Úsala al iniciar un framework de tests, reestructurar suites monolíticas o definir Page Object/fixtures.
metadata:
  author: yzylabs
  version: "1.0"
---

# Diseñar arquitectura de automatización

## Propósito

Definir una TAA mantenible alineada a gTAA: capas claras, patrones de abstracción y requisitos de testabilidad — antes de acumular scripts frágiles.

## Entradas

- Objetivo de las suites (smoke/regresión/gate).
- SUT (web, API, mobile, híbrido) y entornos.
- Stack elegido o existente.
- Restricciones de CI y datos.
- Deuda actual (monolito de tests, acoplamiento UI).

## Procedimiento

1. Mapea capacidades gTAA relevantes: interfaz SUT, adaptación de herramienta, lógica de prueba, generación/reporte, gestión de configuración.
2. Define capas del framework (ej. fixtures → page/actions → specs → reporting).
3. Elige patrones: Page Object, Screenplay, component testing — uno primario, documentado.
4. Especifica convenciones: naming, carpetas, tags (`@smoke`, `@regression`), datos por entorno.
5. Lista requisitos de testabilidad del SUT: `data-testid`, hooks, APIs de setup, observabilidad.
6. Define estrategia de datos: factories sintéticas, aislamiento, cleanup.
7. Documenta límites: qué vive en unit/component vs E2E.
8. Entrega diagrama/texto de capas + ADR breve si hay decisión controvertida.

## Salida

```text
TAA_DESIGN:
- layers:
- patterns:
- folder_layout:
- tags:
- testability_requests:
- data_strategy:
- ci_assumptions:
RISKS:
OPEN_DECISIONS:
```

## Casos límite

- Repo ya tiene 3 estilos mezclados → plan de convergencia gradual; no big-bang sin mandato.
- SUT sin IDs ni API de setup → bloquea E2E masivo; reporta testability a Usopp.
- Solo API → no fuerces Page Object UI; diseña client/fixtures API.

## Validación

- Cada capa tiene responsabilidad única y dependencias hacia adentro.
- No hay secretos en el diseño.
- Tags smoke/regression definidos.
- Testability requests son accionables para desarrollo.

## Criterios de terminado

- Diseño revisable por Usopp/devs.
- Mapeo explícito a gTAA/TAA.
- Path de migración si hay deuda.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | App web + Playwright vacío | TAA con layers + Page Object/fixtures |
| Ambiguo | “Pon un framework” sin SUT | Preguntas + TAA mínima genérica + riesgos |
| Límite | Monolito 2k lines un archivo | Plan de split por dominio + tags |

## Fuentes

- ISTQB CTAL-TAE v2.0 Cap. 3 Test Automation Architecture / gTAA (2024).
- Playwright Best Practices — https://playwright.dev/docs/best-practices (2026-08-04).
