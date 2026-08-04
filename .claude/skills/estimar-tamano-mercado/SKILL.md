---
name: estimar-tamano-mercado
description: Estima TAM, SAM y SOM con método top-down y/o bottom-up, supuestos y sensibilidad. Úsala cuando se pida tamaño de mercado, oportunidad de revenue o validar si un segmento justifica inversión.
metadata:
  author: yzylabs
  version: "1.0"
---

# Estimar tamaño de mercado (TAM/SAM/SOM)

## Propósito

Cuantificar la oportunidad de mercado de forma auditable: Total Addressable Market (TAM), Serviceable Available/Addressable Market (SAM) y Serviceable Obtainable Market (SOM), con supuestos y rangos — no un único número “mágico”.

## Entradas

- Producto/oferta y unidad de medida (revenue anual, cuentas, usuarios activos).
- Geografía y horizonte temporal.
- Precio/ACV o proxies de monetización.
- Fuentes externas o datos internos disponibles.
- Restricciones de canal, regulación o capacidad.

## Procedimiento

1. Define el mercado en una frase (qué se compra, quién compra, dónde, unidad).
2. Elige método primario: bottom-up (preferido si hay ACV y conteo de buyers) y/o top-down (filtros desde industria).
3. Calcula TAM: demanda total si 100% share en el mercado definido.
4. Deriva SAM: porción alcanzable por geografía, canal, producto y compliance.
5. Estima SOM: share realista en horizonte (competencia, capacidad, go-to-market).
6. Lista supuestos numerados; marca cada uno como dato / proxy / juicio.
7. Corre sensibilidad (bajo/base/alto) en 1–2 drivers clave (precio, # buyers, share).
8. Documenta gaps: qué dato faltaría para subir confianza.

## Salida

```md
## Mercado definido
## Unidad / horizonte / geografía
## Método (top-down / bottom-up / ambos)
## TAM / SAM / SOM (base + rango)
## Supuestos
## Sensibilidad
## Fuentes
## Confianza y gaps
## Implicación para decisión
```

## Casos límite

- Sin precio ni ACV → estima en unidades y declara que revenue requiere pricing.
- Solo top-down de un vendor → cruza con bottom-up mínimo o marca `COMPLETED_WITH_LIMITATIONS`.
- Mercado nuevo sin categoría → usa value theory / analogías y etiqueta incertidumbre alta.

## Validación

- TAM ≥ SAM ≥ SOM en la misma unidad y horizonte.
- Cada cifra tiene fuente o supuesto explícito.
- No se presenta SOM como “garantía de captura”.

## Criterios de terminado

- Un decisor entiende el tamaño, los filtros y qué cambiaría el número.
- Gaps y confianza están explícitos.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | API B2B con ACV y # empresas en 2 países | TAM/SAM/SOM bottom-up + sensibilidad |
| Ambiguo | “¿Cuánto vale el mercado de Open Banking?” | Preguntas de definición + borrador con límites |
| Límite | Cero datos de precio | Sizing en unidades + bloqueo parcial de revenue |

## Fuentes

- Corporate Finance Institute — TAM — https://corporatefinanceinstitute.com/resources/management/total-addressable-market-tam/ (2026-08-04).
- Salesforce — TAM, SAM, SOM — https://www.salesforce.com/blog/small-business/tam-sam-som/ (2026-08-04).
- Infomineo — TAM SAM SOM methods — https://infomineo.com/services/business-research/market-intelligence/tam-sam-som-definitions-formulas-and-how-to-calculate-each/ (2026-08-04).
