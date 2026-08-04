---
name: proponer-experimento-adopcion
description: Propone experimentos de adopción con métrica primaria, segmento, duración y criterios de decisión. Úsala cuando ya hay hipótesis de fuga/activación y haga falta un test priorizado (A/B, checklist, empty state, copy de onboarding).
metadata:
  author: yzylabs
  version: "1.0"
---

# Proponer experimento de adopción

## Propósito

Convertir una hipótesis de adopción en un experimento ejecutable, medible y decidible — sin diluir el éxito en vanity metrics.

## Entradas

- Hipótesis causal (de diagnóstico o stakeholder).
- Evento de activación / métrica de retención relevante.
- Baseline actual (o supuesto).
- Restricciones de tráfico, compliance y release.
- Capacidad de instrumentación y de shipping.

## Procedimiento

1. Reescribe la hipótesis en formato: si hacemos X en segmento Y, entonces Z (métrica) sube/baja porque…
2. Elige **una** métrica primaria alineada a activación o retención temprana.
3. Define métricas de guardrail (p. ej. no empeorar D7, no subir tickets).
4. Especifica variante(s), control y asignación.
5. Fija duración, tamaño mínimo o criterio de parada (sin fingir power analysis inventada: declara supuestos).
6. Lista cambios de producto/copy/UX y dueños.
7. Define criterios de decisión: ship / iterate / revert.
8. Anticipa riesgos (novelty effect, confusión de segmentos, sesgo de selección).
9. Prioriza si hay varios candidatos (ICE o impacto×confianza×esfuerzo).
10. Entrega el diseño listo para Morgans / producto / analytics.

## Salida

```md
## Hipótesis

Si … entonces … porque …

## Diseño

- Segmento:
- Control:
- Variante(s):
- Primaria:
- Guardrails:
- Ventana:

## Criterios de decisión

- Ship si:
- Iterate si:
- Revert si:

## Implementación

| Cambio | Dueño |
|---|---|

## Riesgos

- […]

## Prioridad (si hay cola)

| Exp | Impacto | Confianza | Esfuerzo |
|---|---|---|---|
```

## Casos límite

- Sin baseline: declara medición previa obligatoria o experimento solo exploratorio.
- Métrica primaria vanity: rechaza y propone métrica de comportamiento.
- Multi-cambio en una variante: advierte confusión de atribución; sugiere factorizar.
- Tráfico insuficiente: propone qualitative test / sequential; no inventes significancia.

## Validación

- Una métrica primaria clara.
- Criterios de decisión binarios/ternarios explícitos.
- Hipótesis falseable.
- Guardrails presentes cuando el riesgo lo amerita.

## Criterios de terminado

- Al menos un experimento especificable end-to-end.
- Dueños de implementación listados.
- Listo para aprobación de Morgans.

## Evaluación sugerida

| Caso | Entrada | Esperado |
|---|---|---|
| Normal | “Checklist confunde” | A/B checklist 3 vs 5 + activation rate |
| Ambiguo | “Probemos cosas” | Pedir hipótesis; no inventar 10 tests |
| Límite | Optimizar clicks de tooltip | Rechazar vanity; reanclar a activación |

## Fuentes

- Amplitude / PostHog — AARRR focus on stage with leak — https://amplitude.com/blog/pirate-metrics-framework (2026-08-04); https://posthog.com/product-engineers/aarrr-pirate-funnel (2026-08-04)
- Appcues — iterate onboarding with behavioral metrics — https://www.appcues.com/blog/product-led-onboarding (2026-08-04)
