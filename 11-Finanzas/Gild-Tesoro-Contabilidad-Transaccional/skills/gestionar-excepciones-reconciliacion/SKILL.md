---
name: gestionar-excepciones-reconciliacion
description: Clasifica, prioriza y hace aging de breaks de conciliación (monto, referencia, timing, duplicado, missing, FX). Úsala cuando haya cola de excepciones, force-match propuesto o disputa de cuadre.
metadata:
  author: yzylabs
  version: "1.0"
---

# Gestionar excepciones de reconciliación

## Propósito

Convertir unmatched en una cola accionable con clasificación, severidad, aging, dueño y evidencia — sin cerrar por vanidad de match rate.

## Entradas

- Lista de unmatched / breaks.
- Conciliación o cash application de origen.
- Políticas de SLA y severidad.
- Histórico de breaks recurrentes (si existe).
- Roles (preparador, revisor, ops, legal).

## Procedimiento

1. Normaliza cada break: IDs, montos, fechas, fuentes A/B, diferencia.
2. Clasifica: timing | monto | referencia | moneda/FX | duplicado | missing | data-quality | sospecha-fraude.
3. Asigna severidad (materialidad, aging, riesgo de fraude/reporting).
4. Propón dueño y siguiente acción (enrich data, ajuste, disputa, reprocess).
5. Rechaza force-match; conviértelo en ajuste propuesto con aprobación.
6. Detecta patrones (mismo partner, misma cuenta, mismo preparador) y escala.
7. Actualiza aging buckets (0–3d, 4–7d, 8–30d, +30d) y bloquea “cierre” si material +30d sin dueño.

## Salida

```md
## Resumen de cola (conteos / montos)
## Breaks (tabla: clase, severidad, aging, dueño, acción)
## Force-match rechazados / ajustes propuestos
## Patrones / riesgos
## Escalamiento a Denjiro / Legal
## Pendientes
```

## Casos límite

- Break por truncación ISO 20022 → data-quality; remediar fuente, no matchear a ciegas.
- Break neteado “informalmente” entre periodos → no permitas; documenta y escala.
- Sospecha de lapping / unapplied crónico → escalamiento inmediato.

## Validación

- Cada break tiene clase + dueño + aging.
- No hay cierre de break sin evidencia o aprobación.
- Materialidad alineada a política o marcada como asumida.

## Criterios de terminado

- Cola usable por ops/Denjiro el mismo día.
- Riesgos de fraude/control señalados explícitamente.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | 12 unmatched mixtos | Cola clasificada con dueños |
| Ambiguo | “Ciérralos todos” | Rechazo force-match + plan |
| Límite | Mismo short-pay 40 días | Severidad alta + escala Legal/Denjiro |

## Fuentes

- ReconArt — granular reason codes / exceptions — https://www.reconart.com/blog/iso-20022-adoption-transform-reconciliation-enhance-payments-unlock-efficiencies/ (2026-08-04).
- Solvexia — internal control bank reconciliation / exception evidence — https://www.solvexia.com/blog/internal-control-bank-reconciliation (2026-08-04).
- COSO ICIF — detective controls / segregation (2026-08-04).
