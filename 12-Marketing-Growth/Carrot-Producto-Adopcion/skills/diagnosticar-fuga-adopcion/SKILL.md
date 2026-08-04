---
name: diagnosticar-fuga-adopcion
description: Diagnostica fugas de adopción en Activation y Retention temprana del funnel AARRR. Úsala cuando las altas no se activen, el churn D1/D7 sea alto, o haya que priorizar dónde atacar el leak antes de experimentar.
metadata:
  author: yzylabs
  version: "1.0"
---

# Diagnosticar fuga de adopción

## Propósito

Localizar y priorizar la etapa/paso con mayor pérdida material entre signup → activación → retención temprana, con evidencia o hipótesis explícitas.

## Entradas

- Definiciones de Acquisition (contexto), Activation y Retention temprana.
- Funnel / cohorts / drop-off (o declaración de vacío).
- Segmentación disponible.
- Cambios recientes de producto/onboarding.
- Objetivo de Morgans (qué “malo” hay que explicar).

## Procedimiento

1. Fija definiciones operativas de cada etapa usada (no mezcles vanity).
2. Construye el funnel mínimo: signup → setup → activación → D1/D7 (o ventana pedida).
3. Calcula tasas y volúmenes absolutos (fuga relativa ≠ fuga absoluta).
4. Identifica el mayor leak por impacto (usuarios perdidos), no solo por %).
5. Genera 2–4 hipótesis causales por leak (fricción, valor poco claro, segmento incorrecto, bug).
6. Marca qué se puede validar con dato existente vs. qué requiere investigación.
7. Prioriza intervenciones: quick wins vs. apuestas; no propongas 20 experimentos a la vez.
8. Separa claramente lo que es Acquisition (fuera de foco salvo contexto) de Activation/Retention.
9. Entrega diagnóstico con siguiente paso dueño.

## Salida

```md
## Definiciones

| Etapa | Definición operativa |
|---|---|

## Funnel

| Etapa | N | Tasa vs anterior | Perdidos |
|---|---|---|---|

## Leak prioritario

- Etapa/paso:
- Impacto:
- Evidencia:

## Hipótesis

| # | Hipótesis | Cómo validar | Severidad |
|---|---|---|---|

## Fuera de este diagnóstico

- Acquisition profunda / brand / comunidad: handoff …

## Recomendación

1. …
2. …

## Huecos de datos

- […]
```

## Casos límite

- Solo hay top-of-funnel marketing: limita el alcance; escala Acquisition a Morgans/Shakky.
- Retención mala pero activación alta: enfoca hábito/valor continuo, no más onboarding.
- Sin números: diagnóstico cualitativo + plan de instrumentación; STATUS puede ser COMPLETED_WITH_LIMITATIONS.
- Confundir referral con activación: corrige definiciones.

## Validación

- Definiciones operativas presentes.
- Prioridad por impacto absoluto cuando hay volúmenes.
- Hipótesis ≠ hechos sin evidencia.
- Foco Activation/Retention temprana respetado.

## Criterios de terminado

- Leak prioritario nombrado.
- Hipótesis con plan de validación.
- Recomendación accionable para Morgans/producto.

## Evaluación sugerida

| Caso | Entrada | Esperado |
|---|---|---|
| Normal | 40% signup→activación, 5% D7 | Priorizar post-activación o activación según volúmenes |
| Ambiguo | “No crecemos” | Pedir funnel; no inventar tasas |
| Límite | Pedido solo de ads CPC | Handoff Acquisition; no forzar adopción |

## Fuentes

- Amplitude — AARRR — https://amplitude.com/blog/pirate-metrics-framework (2026-08-04)
- PostHog — AARRR pirate funnel — https://posthog.com/product-engineers/aarrr-pirate-funnel (2026-08-04)
