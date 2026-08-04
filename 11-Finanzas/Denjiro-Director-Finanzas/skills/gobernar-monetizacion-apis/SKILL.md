---
name: gobernar-monetizacion-apis
description: Define políticas de monetización de APIs (pricing, metering, packaging, margen vs unit cost) a nivel dirección. Úsala cuando se pida gobierno de revenue de APIs, modelos de cobro partner/interno o gates antes de habilitar billing en producción.
metadata:
  author: yzylabs
  version: "1.0"
---

# Gobernar monetización de APIs

## Propósito

Establecer reglas de producto financiero para APIs sin que Denjiro escriba rate cards detalladas: Du Feld ejecuta; Denjiro fija gates, margen mínimo y coherencia con costo e integridad ledger.

## Entradas

- Productos/APIs candidatos a monetizar y segmento (partner, interno, premium OB).
- Unit costs disponibles (King Riku) o gaps.
- Capacidad de metering y estado del ledger (Gild Tesoro).
- Restricciones legales/comerciales conocidas.

## Procedimiento

1. Clasifica el modelo: free/tiered, usage-based, subscription, hybrid, showback-only.
2. Exige definición de unidad de metering (call, mensaje, MB, journey) alineada a telemetría real.
3. Cruza con unit cost: calcula o marca TBD el puente de margen; bloquea P0 de cobro externo si el costo es desconocido y el riesgo es alto.
4. Define packaging y deprecación de planes (breaking changes de precio = comunicación + ventana).
5. Separa monetización externa de chargeback interno; no mezclar KPIs.
6. Lista gates pre-producción: metering estable, pricing versionado, reconciliación ledger, owner de disputes.
7. Emite contrato a Du Feld; escala a Sengoku (contratos) y Jinbe/Sabo (producto/DX) vía Luffy cuando aplique.

## Salida

```md
## Política de monetización API
- Productos en alcance:
- Modelo(s) de pricing:
- Unidad de metering:
- Puente margen vs unit cost:
- Packaging / deprecación:
## Gates pre-producción
## Fuera de alcance / no monetizar aún
## Delegación a Du Feld
## Escalaciones Legal / OB / Plataforma
```

## Casos límite

- Partner estratégico “gratis”: documenta costo absorbido y revisión de caducidad; no ocultar subsidy.
- Open Banking mandatorio vs premium: distingue cumplimiento (posible free/regulated) de value-added cobrable.
- Sin Gild Tesoro forjado: permite diseño de pricing; bloquea go-live de cobro con `DELEGATION_REQUIRED`.

## Validación

- Cada producto P0 tiene metering y owner de revenue.
- Margen o subsidy está explícito.
- Gates de ledger listados antes de producción.

## Criterios de terminado

- Política accionable para Du Feld y revisable por Luffy.
- Trade-offs de precio vs adopción documentados.
- Escalaciones legales identificadas.

## Fuentes

- FinOps — Invoicing & Chargeback / Unit Economics capabilities — https://www.finops.org/framework/capabilities/ (consultado 2026-08-04)
- Prácticas API-as-a-product monetization (metering/packaging; síntesis secundaria contrastada) — 2026-08-04
