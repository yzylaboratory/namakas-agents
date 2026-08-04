---
name: implementar-suite-automatizada
description: Implementa o actualiza suites de tests automatizados con localizadores resilientes y aserciones del framework. Úsala cuando haya que escribir/arreglar código de prueba UI/E2E/component según el stack del repo.
metadata:
  author: yzylabs
  version: "1.0"
---

# Implementar suite automatizada

## Propósito

Entregar tests ejecutables, legibles y mantenibles que den señal de regresión sin sleeps fijos ni selectores frágiles.

## Entradas

- Casos priorizados (de `seleccionar-candidatos-automatizacion` o Usopp).
- TAA / convenciones del repo.
- Stack (p. ej. Playwright, Cypress, Jest, pytest).
- Entorno y datos sintéticos.
- Criterios de aceptación del flujo.

## Procedimiento

1. Reproduce el flujo manualmente o con evidencia (spec, tratado, grabación).
2. Elige el nivel de prueba acordado; no subas a E2E sin necesidad.
3. Implementa usando abstracciones de la TAA (pages/fixtures), no copy-paste de selectores.
4. Localizadores: prioriza role/text/test-id; evita CSS de layout y XPath largos.
5. Aserciones: usa matchers con auto-wait/retry del framework (`expect(locator).toBeVisible`, etc.).
6. **Prohibido** en código entregable: `waitForTimeout` / sleep de sincronización.
7. Datos: factories sintéticas; limpia estado entre tests; evita orden dependiente.
8. Tags: `@smoke` / `@regression` según diseño.
9. Ejecuta localmente el mismo comando documentado para CI.
10. Adjunta reporte/falla (trace/screenshot) si aplica.

## Salida

- Diff / archivos de test.
- Comando de ejecución.
- Lista de flujos cubiertos y no cubiertos.
- Limitaciones (entorno, mocks, browsers).

## Casos límite

- UI inestable sin test ids → implementa mínimo + `testability_requests`; no inventes selectores mágicos.
- Necesita contrato OpenAPI como verdad → coordina Kalifa; Kuma puede consumir mock/client, no ser dueño del schema.
- Test requiere performance assert (p95) → fuera de alcance; Kaido.

## Validación

- Suite pasa (o falla solo por defecto de producto documentado).
- Sin sleeps fijos de sync.
- Sin secretos/PII en fixtures.
- Tags y naming según TAA.

## Criterios de terminado

- Código en el path del proyecto de tests.
- Comando reproducible.
- Evidencia de ejecución adjunta al reporte.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Login smoke + Playwright | Spec con getByRole/testId + expect web-first |
| Ambiguo | “Haz el E2E del checkout” sin pasos | Lista de supuestos + suite mínima o BLOCKED |
| Límite | Pedido de sleep(5000) “porque flaky” | Rechazo; usa auto-wait / estabilizar-pruebas-flaky |

## Fuentes

- Playwright Writing tests — https://playwright.dev/docs/writing-tests (2026-08-04).
- Playwright Best Practices — https://playwright.dev/docs/best-practices (2026-08-04).
- Playwright Auto-waiting — https://playwright.dev/docs/actionability (2026-08-04).
- ISTQB CTAL-TAE v2.0 Cap. 4 Implementing Test Automation (2024).
