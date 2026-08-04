---
name: evaluar-impacto-cambio-regulatorio
description: Evalúa el impacto de un cambio regulatorio Open Finance (nuevo instrumento, consulta, aplazamiento o litigio) con escenarios A/B y decisiones requeridas. Úsala ante PSD3/FIDA, cambios BCB/CMF/CDR/1033 u otras reformas sin inventar fechas de vigencia.
metadata:
  author: yzylabs
  version: "1.0"
---

# Evaluar impacto de cambio regulatorio

## Propósito

Traducir un cambio normativo publicado o en curso a escenarios de impacto para producto y cumplimiento, con decisiones explícitas para Sengoku.

## Entradas

- Descripción del cambio (instrumento, borrador, sentencia, aplazamiento).
- Jurisdicción y rol.
- Estado actual del programa OB (si hay).
- Fecha de análisis.

## Procedimiento

1. Verifica el texto o comunicado **oficial** del cambio; registra fuente y fecha.
2. Clasifica: nuevo mandato / enmienda / consulta / litigio / aplazamiento.
3. Construye escenarios A/B (y C si hace falta) cuando la vigencia sea incierta.
4. Para cada escenario: impacto en APIs, consentimiento, seguridad (FAPI), participantes, reporting.
5. Lista decisiones requeridas (esperar, dual-run, freeze de scope, counsel).
6. Prohíbe fechas inventadas; si el regulador no publicó fecha, dilo.

## Salida

```md
## Cambio regulatorio
- Instrumento / emisor / fuente / fecha consulta:
## Escenarios
| Escenario | Supuesto | Impacto | Probabilidad cualitativa | Acción sugerida |
## Decisiones requeridas (Sengoku)
## No inventado / desconocido
```

## Casos límite

- Solo rumor de prensa → rechazo o borrador con disclaimer; exigir primaria.
- Aplazamiento (ej. entrada en vigor Chile) → actualizar estado; no mantener fecha vieja.
- Conflicto entre fuentes secundarias → priorizar regulador.

## Validación

- Fuente oficial citada o bloqueo.
- Al menos dos escenarios si vigencia incierta.
- Sin compliance date fabricada.

## Criterios de terminado

- Escenarios accionables para Sengoku/Jinbe.
- Decisiones requeridas listadas.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Aplazamiento CMF con comunicado | Escenarios + nueva ventana |
| Ambiguo | “PSD3 pronto” sin texto | Exigir fuente; borrador máximo |
| Límite | Pedido de fecha firme no publicada | Rechazo; marcar desconocido |

## Fuentes

- Open Banking Tracker — https://www.openbankingtracker.com/open-banking-regulations — 2026-08-04
- CFPB PFDR — https://www.consumerfinance.gov/personal-financial-data-rights/ — 2026-08-04
- Panorama LatAm (secundaria) — Ozone API — 2026-08-04
