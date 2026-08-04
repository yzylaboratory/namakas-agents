---
name: disenar-onboarding-producto
description: Diseña o audita onboarding product-led orientado al aha (setup mínimo, checklist 3–5, bumpers). Úsala cuando haga falta un flujo de primera experiencia, empty state guiado o rediseño de onboarding sin tour de features.
metadata:
  author: yzylabs
  version: "1.0"
---

# Diseñar onboarding de producto

## Propósito

Especificar un onboarding product-led cuyo único objetivo sea llevar al usuario al evento de activación con fricción mínima y guía accionable.

## Entradas

- Evento de activación definido.
- Camino mínimo al valor (o borrador TTV).
- Segmentos / intents conocidos.
- Restricciones de UI/marca y compliance.
- Estado del empty state actual (si existe).

## Procedimiento

1. Confirma el evento de activación y el segmento primario.
2. Define setup mínimo (solo lo necesario para el aha).
3. Diseña checklist in-product de 3–5 ítems event-driven (no genéricos).
4. Especifica bumpers: tooltips/hotspots solo en la “pista” hacia el valor; evita modal walls.
5. Define empty state con datos demo o plantilla si acelera comprensión (sin inventar datos reales de clientes).
6. Si hay intents distintos, define rutas (no un único tour infinito).
7. Especifica mensajes de progreso/celebración al completar activación.
8. Lista copy necesario para handoff a Vivi; no sustituyas docs largas.
9. Define métricas de éxito del onboarding (activation rate, step completion, TTV).
10. Entrega especificación lista para producto/UX.

## Salida

```md
## Objetivo de onboarding

- Segmento:
- Evento de activación:
- TTV objetivo:

## Setup mínimo

- […]

## Checklist (3–5)

| # | Ítem | Evento que lo completa |
|---|---|---|

## Bumpers / empty state

[…]

## Rutas por intent (si aplica)

| Intent | Camino |
|---|---|

## Métricas

- […]

## Handoffs

- Vivi (copy): …
- UX: …
- Analytics: …

## Fuera de alcance

- […]
```

## Casos límite

- Pedido de “tour completo de features”: rechaza como anti-patrón; redirige a activación.
- Checklist >5 ítems: recorta o divide por fase post-activación.
- Sin evento de activación: ejecuta primero `definir-evento-activacion` o marca dependencia.
- Dark patterns: prohibidos; marca riesgo y no especifiques engaño.

## Validación

- Cada ítem del checklist mapea al camino al valor.
- No hay tour como métrica de éxito.
- Setup mínimo justificado.
- Métricas de activación/TTV presentes.

## Criterios de terminado

- Especificación de onboarding usable por producto/UX.
- Checklist 3–5 con eventos.
- Handoffs y fuera de alcance claros.

## Evaluación sugerida

| Caso | Entrada | Esperado |
|---|---|---|
| Normal | Activación = crear primer objeto | Checklist corto + empty state |
| Ambiguo | “Mejorar onboarding” | Pedir evento/segmento; no inventar UI |
| Límite | Forzar 15 tooltips | Reducir a pista; documentar rechazo |

## Fuentes

- Appcues — Product-led onboarding — https://www.appcues.com/blog/product-led-onboarding (2026-08-04)
- PLG Handbook — Aha / bowling alley / checklists — https://plghandbook.com/aha-moment/ (2026-08-04)
