---
name: analizar-brechas-cumplimiento-open-finance
description: Compara obligaciones Open Finance evidenciadas contra el estado actual de producto/APIs/políticas y prioriza gaps. Úsala cuando exista un marco mapeado y un baseline (diseño, contratos, OpenAPI o recon) para medir cumplimiento.
metadata:
  author: yzylabs
  version: "1.0"
---

# Analizar brechas de cumplimiento Open Finance

## Propósito

Producir un gap analysis accionable: obligación → evidencia actual → severidad → owner → dependencia legal.

## Entradas

- Salida de `mapear-marco-regulatorio-open-finance` (obligatorio).
- Baseline: políticas, OpenAPI, journeys, contratos, informe Noland.
- Alcance incluido / fuera de alcance.
- Fecha de análisis.

## Procedimiento

1. Extrae obligaciones materiales del mapa (solo hechos o hipótesis etiquetadas).
2. Para cada obligación, busca evidencia en el baseline; si no hay, marca `sin evidencia`.
3. Clasifica gap: ausente / parcial / presente-no-trazable / N/A fuera de alcance.
4. Asigna severidad (crítica / alta / media / baja) por riesgo regulatorio, no por preferencia de producto.
5. Sugiere owner (producto, seguridad, legal, privacidad) y si requiere decisión de Sengoku.
6. Prohíbe la fila “compliant” global; solo estados por obligación.

## Salida

```md
## Brechas OF — {jurisdicción} — {fecha}
| Obligación | Evidencia actual | Estado | Severidad | Owner | Dep. legal | Fuente |
## Top risks
## Fuera de alcance
## Recomendación de cierre (secuencia)
```

## Casos límite

- Baseline vacío → todas `sin evidencia`; no inventar controles.
- Pedido de certificado de cumplimiento → rechazar; entregar gaps + escalar Sengoku.
- Conflicto entre OpenAPI y política → gap `presente-no-trazable` + riesgo.

## Validación

- Cada fila enlaza a obligación con fuente.
- Severidades justificadas en una línea.
- Sin claim de compliance global.

## Criterios de terminado

- Tabla de gaps priorizable.
- Dependencias legales explícitas.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Mapa BR + OpenAPI parcial | Gaps priorizados con owners |
| Ambiguo | Obligaciones sin baseline | Bloqueo o solo `sin evidencia` |
| Límite | “¿Estamos compliant?” | Rechazo del sí/no; matriz por obligación |

## Fuentes

- Marco mapeado (skill anterior) + fuentes primarias allí citadas
- OpenID FAPI — https://openid.net/wg/fapi/ — 2026-08-04
