---
name: disenar-modelo-pricing-api
description: Diseña el modelo de pricing de una API (freemium, usage, suscripción, híbrido base+overage, créditos, enterprise). Úsala cuando haya que decidir cómo cobrar; no para tiers light sin precios (Sabo).
metadata:
  author: yzylabs
  version: "1.0"
---

# Diseñar modelo de pricing de API

## Propósito

Seleccionar y documentar un modelo de precio alineado a valor, costo y segmento (PLG vs enterprise), con supuestos explícitos.

## Entradas

- Producto de API y audiencias (handoff Sabo si existe).
- Objetivo financiero (margen, adopción, ARR mínimo).
- Costos unitarios o proxies.
- Restricciones regulatorias (qué no se cobra).
- Comparables de mercado (si hay).

## Procedimiento

1. Clasifica la API: regulatoria/obligatoria vs value-added comercial.
2. Lista drivers de valor y de costo; marca qué es hecho vs inferencia.
3. Evalúa candidatos: freemium (adquisición), usage-only, subscription tiers, híbrido base+overage, créditos, enterprise custom.
4. Recomienda un modelo primario (preferir híbrido cuando haga falta predictibilidad + upside).
5. Define planes: cuota incluida, overage, mínimos, descuentos anuales, path enterprise.
6. Analiza riesgos: bill shock, pricing cliffs, freemium dilution, churn por sorpresa.
7. Documenta supuestos y qué debe aprobar Denjiro antes de publicar price list.
8. Si solo piden packaging sin montos → no inventes precios; deriva a Sabo o produce drivers + open decisions.

## Salida

```md
## Clasificación API (regulatoria vs comercial)
## Drivers de valor / costo
## Modelo recomendado (+ alternativas)
## Planes (cuotas, overages, enterprise)
## Supuestos y aprobaciones Denjiro
## Riesgos
## Fuentes
```

## Casos límite

- API PSD2/obligatoria “gratis” + enrich de pago → dos empaquetados; solo el value-added lleva precio.
- Solo existe freemium sin metering → exige instrumentar antes de fijar paid conversion.
- Enterprise pide custom sin margen modelado → BLOCKED hasta costos/proxies.

## Validación

- Modelo alineado a value metric (o enlaza skill de métrica).
- Sin tarifas huérfanas de supuestos.
- Frontera Sabo/Du-Feld clara.
- Riesgos de bill shock tratados.

## Criterios de terminado

- Recomendación decidible por Denjiro.
- Planes documentados o decisiones abiertas explícitas.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | API enrich B2B con costo por txn | Híbrido base+overage + path enterprise |
| Ambiguo | “Ponle precio a la API” | Drivers + opciones + DECISIONS_REQUIRED |
| Límite | Endpoint regulatorio + add-on comercial | Separación packaging; precio solo add-on |

## Fuentes

- APIScout API Monetization 2026 — https://apiscout.dev/guides/api-monetization-models-guide-2026 (2026-08-04).
- Moesif API Pricing 2026 — https://www.moesif.com/blog/api-monetization/api-pricing/ (2026-08-04).
- ScaleDrone How to Price Your API — https://www.scaledrone.com/blog/how-to-price-your-api/ (2026-08-04).
