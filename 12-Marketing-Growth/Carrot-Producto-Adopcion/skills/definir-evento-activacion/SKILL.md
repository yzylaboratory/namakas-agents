---
name: definir-evento-activacion
description: Define el evento de activación (aha) medible y predictivo de retención. Úsala cuando haya que decidir qué cuenta como usuario activado, separar tour/checklist de valor real, o fijar la métrica primaria de onboarding.
metadata:
  author: yzylabs
  version: "1.0"
---

# Definir evento de activación

## Propósito

Formular un evento de activación observable que represente el primer valor del producto (aha moment) y que pueda instrumentarse y correlacionarse con retención — sin confundirlo con completar un tour.

## Entradas

- Producto y job-to-be-done del segmento.
- Evidencia de usuarios retenidos (cohorts, entrevistas) o hipótesis explícita.
- Capacidades reales del producto.
- Ventana temporal de interés (D1, D7, etc.).
- Restricciones de privacidad / analytics.

## Procedimiento

1. Describe el valor central en una frase (qué “hace click” para el usuario).
2. Propón 1–3 candidatos de evento comportamental (no vanity).
3. Para cada candidato: observabilidad, instrumentación, falsos positivos, relación esperada con retención.
4. Elige el evento primario y eventos secundarios (leading indicators).
5. Define la definición operativa: actor, acción, umbral, ventana, exclusiones.
6. Documenta cómo se validaría la correlación (método mínimo; no inventes resultados).
7. Lista huecos de datos y dueño de instrumentación.
8. Entrega el paquete listo para Morgans / analytics / producto.

## Salida

```md
## Evento de activación (primario)

- Nombre:
- Definición operativa:
- Ventana:
- Segmento:

## Por qué predice retención (hipótesis)

[…]

## Eventos secundarios / leading

| Evento | Rol |
|---|---|

## No es activación

- [tour, checklist vacío, pageview, …]

## Instrumentación

- Eventos / propiedades mínimas:
- Dueño:
- Riesgos de PII:

## Validación de correlación (plan)

[…]

## Supuestos y preguntas abiertas

- […]
```

## Casos límite

- Solo hay “completó signup”: reformula hacia primer valor o marca BLOCKED por falta de producto usable.
- Múltiples segmentos con ahás distintos: define por segmento; no fuerces uno solo.
- Producto B2B multi-seat: distingue activación de usuario vs. de cuenta.
- Sin analytics: entrega definición + plan de medición; no inventes tasas.

## Validación

- El evento es pass/fail observable.
- No equivale solo a UI tour.
- Hipótesis de retención explícita.
- Exclusiones y ventana claras.

## Criterios de terminado

- Evento primario definido operativamente.
- Lista de “no es activación”.
- Plan de instrumentación o hueco etiquetado.
- Listo para handoff a Morgans/analytics.

## Evaluación sugerida

| Caso | Entrada | Esperado |
|---|---|---|
| Normal | SaaS con acción core clara | Evento comportamental + ventana |
| Ambiguo | “Que usen el producto” | Descomponer candidatos; pedir foco |
| Límite | Pedido de tracking de PII sensible | Marcar riesgo; no normalizar |

## Fuentes

- Appcues — Product-led onboarding (activation ≠ tour) — https://www.appcues.com/blog/product-led-onboarding (2026-08-04)
- PLG Handbook — Aha moment — https://plghandbook.com/aha-moment/ (2026-08-04)
- PostHog — AARRR activation — https://posthog.com/product-engineers/aarrr-pirate-funnel (2026-08-04)
