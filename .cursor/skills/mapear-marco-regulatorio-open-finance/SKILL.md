---
name: mapear-marco-regulatorio-open-finance
description: Mapea el marco regulatorio Open Banking/Open Finance de una jurisdicción con fuentes primarias, estado de vigencia y artefactos técnicos asociados. Úsala cuando haya que identificar qué norma aplica y qué estándar técnico acompaña antes de un brief o gap analysis.
metadata:
  author: yzylabs
  version: "1.0"
---

# Mapear marco regulatorio Open Finance

## Propósito

Construir el mapa normativo primario por jurisdicción (instrumento, emisor, estado, artefactos técnicos) que alimenta el resto del análisis de Tsuru.

## Entradas

- Jurisdicción(es) y rol de la entidad.
- Productos/journeys en alcance (AIS, PIS, data sharing, open insurance, etc.).
- Fecha de análisis.
- Mapa alto nivel de Jinbe (opcional).

## Procedimiento

1. Identifica el marco primario (ej. PSD2/PSD3+FIDA UE; UK OB; Open Finance BCB; CDR AU; CFPB 1033 US; Ley Fintech/CMF Chile; SFC Colombia).
2. Localiza la fuente primaria del regulador o del legislador; registra URL/referencia y fecha de consulta.
3. Relaciona artefactos técnicos: API standards del ecosistema, perfiles FAPI, directorios/acreditación, consentimiento.
4. Clasifica estado: vigente / transición / litigado / aplazado — sin inventar fechas.
5. Lista instrumentos secundarios (RTS, NCG, manuales de API) con jerarquía clara.
6. Marca gaps de acceso a texto oficial (paywall, idioma, no publicado).

## Salida

```md
## Marco regulatorio — {jurisdicción}
- Rol entidad / fecha análisis:
| Instrumento | Emisor | Estado | Artefacto técnico | Fuente | Notas |
## Relación con mapa Jinbe (si aplica)
## Huecos de fuente
```

## Casos límite

- Multi-jurisdicción: una tabla por país; no fusionar obligaciones “parecidas”.
- Norma en consulta pública: estado `transición`; no tratar draft como vigente.
- Solo trackers secundarios disponibles: estado `borrador` + exigencia de primaria.

## Validación

- Al menos una fuente primaria por marco, o hipótesis explícita.
- FAPI separado del estándar de datos.
- Fecha de análisis presente.

## Criterios de terminado

- Mapa usable para obligaciones y gaps.
- Huecos de fuente listados.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Brasil Open Finance, ASPSP | Tabla con BCB + manuales + FAPI-BR nota |
| Ambiguo | “LatAm” sin país | Bloqueo; exigir jurisdicción |
| Límite | US 1033 litigado | Estado litigado + escenarios; sin compliance date inventada |

## Fuentes

- https://www.openbankingtracker.com/open-banking-regulations — 2026-08-04
- https://openid.net/wg/fapi/ — 2026-08-04
- https://www.berlin-group.org/psd2-access-to-bank-accounts — 2026-08-04
- https://www.consumerfinance.gov/personal-financial-data-rights/ — 2026-08-04
