---
name: mapear-camino-valor-ttv
description: Mapea el camino más corto al primer valor y audita time-to-value (TTV) y fricción por paso. Úsala cuando usuarios tarden en activarse, el onboarding sea largo, o haya que eliminar/automatizar/diferir pasos.
metadata:
  author: yzylabs
  version: "1.0"
---

# Mapear camino al valor y TTV

## Propósito

Construir el mapa signup (o primer uso) → evento de activación, estimar o medir TTV, y clasificar cada paso como eliminar, automatizar o diferir.

## Entradas

- Evento de activación (o borrador).
- Flujo actual (screens, pasos, requisitos).
- Datos de drop-off por paso si existen.
- Restricciones (compliance, KYC, verificación) que no se pueden eliminar.
- Segmento / intent.

## Procedimiento

1. Fija el punto de partida (landing post-signup, empty state, etc.) y el evento de activación.
2. Lista todos los pasos actuales en orden.
3. Cronometra o estima duración y tasa de abandono por paso (dato o supuesto).
4. Clasifica cada paso: **Eliminar** / **Automatizar** / **Diferir post-valor** / **Mantener (crítico)**.
5. Propón el camino mínimo viable al valor.
6. Calcula TTV actual vs. TTV propuesto (rango si hay incertidumbre).
7. Señala trade-offs (filtrar tire-kickers vs. velocidad; aprendizaje necesario).
8. Entrega backlog de fricción priorizado por impacto×esfuerzo.

## Salida

```md
## Camino actual

| # | Paso | Tipo | TTV/drop | Clasificación |
|---|---|---|---|---|

## Camino mínimo al valor

1. …
2. …

## TTV

- Actual:
- Propuesto:
- Supuestos:

## Fricción prioritaria

| Ítem | Impacto | Esfuerzo | Dueño sugerido |
|---|---|---|---|

## Trade-offs

- […]

## Preguntas abiertas

- […]
```

## Casos límite

- Verificación legal obligatoria: no “eliminar”; diferir solo si la regulación lo permite; documentar.
- Valor requiere setup largo (datos, equipo): no fuerces regla de 5 minutos; ajusta modelo de valor.
- Sin telemetría: mapa cualitativo + plan de medición de drop-off.
- Confundir marketing landing con in-product: delimita el alcance al journey de producto.

## Validación

- Cada paso tiene clasificación.
- El camino propuesto termina en el evento de activación.
- Restricciones no eliminables están marcadas.
- TTV con supuestos visibles.

## Criterios de terminado

- Mapa actual y mínimo documentados.
- Backlog de fricción priorizado.
- TTV actual/propuesto con incertidumbre explícita.

## Evaluación sugerida

| Caso | Entrada | Esperado |
|---|---|---|
| Normal | Onboarding de 12 pasos | Clasificación + camino corto |
| Ambiguo | “Está lento” | Pedir flujo; no inventar pantallas |
| Límite | KYC obligatorio mid-funnel | Mantener/diferir legal; no borrar |

## Fuentes

- PLG Handbook — Time to value — https://plghandbook.com/time-to-value/ (2026-08-04)
- Appcues — shortest path to value — https://www.appcues.com/blog/product-led-onboarding (2026-08-04)
