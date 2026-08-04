---
name: seleccionar-candidatos-automatizacion
description: Prioriza qué casos/flujos automatizar según ROI, pirámide de pruebas y estabilidad del SUT. Úsala cuando haya backlog de QA, pedidos de “automatizar todo” o duda sobre UI vs API/component.
metadata:
  author: yzylabs
  version: "1.0"
---

# Seleccionar candidatos a automatización

## Propósito

Construir un backlog de automatización priorizado, evitando suites frágiles o de bajo valor que aumenten mantenimiento sin señal.

## Entradas

- Lista de casos, historias o flujos críticos.
- Frecuencia de ejecución esperada (smoke, nightly, release).
- Estabilidad conocida del SUT / historial de cambios de UI.
- Stack disponible (unit, component, API, UI/E2E).
- Restricciones de tiempo de CI.

## Procedimiento

1. Inventaría candidatos y el riesgo de negocio que cubren.
2. Clasifica el nivel más bajo de la pirámide que dé señal (unit → component → API → UI).
3. Puntúa: criticidad × frecuencia × repetibilidad ÷ (inestabilidad UI + costo de datos).
4. Marca “no automatizar ahora” si el flujo cambia a diario, depende de terceros no mockeables o es exploración única.
5. Separa ownership: si el valor es contrato/schema → Kalifa; carga → Kaido; checklist regulatorio manual → Tashigi.
6. Produce backlog P0–P2 con justificación y nivel de prueba propuesto.
7. Define criterios de salida (qué señal debe dar cada suite).

## Salida

```text
CANDIDATES_AUTOMATION:
- id:
  risk:
  level: unit|component|api|ui-e2e
  priority: P0|P1|P2
  rationale:
  out_of_scope_reason: (si aplica)
  handoff: (kalifa|tashigi|kaido|none)
SMOKE_SET:
REGRESSION_SET:
REJECTED:
```

## Casos límite

- “Automatiza el sistema entero” → entrega P0 smoke + plan por fases; no promete cobertura total.
- Solo hay UI y API inestable → propone testabilidad (IDs, mocks) antes de E2E masivo.
- Candidato es prueba de performance → `DELEGATION_REQUIRED` a Kaido vía Usopp.

## Validación

- Cada P0 tiene riesgo de negocio explícito y nivel de pirámide justificado.
- Rechazos tienen razón (no “después vemos”).
- No hay solape no declarado con Kalifa/Tashigi/Kaido.

## Criterios de terminado

- Backlog priorizado revisable por Usopp.
- Smoke set acotado (típicamente minutos, no horas).
- Fuentes/criterios citados.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | 20 casos de regresión mixtos | P0–P2 con niveles de pirámide |
| Ambiguo | “Automatiza el portal” | Preguntas de riesgo + smoke P0 mínimo; no inventar flujos |
| Límite | Caso de stress 10k RPS | Reject + handoff Kaido |

## Fuentes

- ISTQB CTAL-TAE v2.0 — selección y despliegue de automatización (2024-06 / PDF 2024-11).
- ISTQB CT-TAS v1.0 — factores de estrategia de automatización (anuncio 2024-06).
