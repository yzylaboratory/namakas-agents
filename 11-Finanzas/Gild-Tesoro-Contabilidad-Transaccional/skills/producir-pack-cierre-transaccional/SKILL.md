---
name: producir-pack-cierre-transaccional
description: Produce el pack de cierre del periodo (reconciliaciones, aging de breaks, ajustes pendientes, evidencia de control). Úsala cuando Denjiro pida cierre mensual/diario o evidencia auditable de contabilidad transaccional.
metadata:
  author: yzylabs
  version: "1.0"
---

# Producir pack de cierre transaccional

## Propósito

Empaquetar el estado de cuadre del periodo para aprobación de Denjiro/auditoría con controles explícitos y sin declarar cierre falso.

## Entradas

- Periodo y alcance (cuentas, productos, monedas).
- Salidas de conciliación bancaria, cash application, clearing y cola de breaks.
- Asientos/ajustes propuestos del periodo.
- Roles preparador/revisor y política de materialidad.
- Dependencias abiertas (Du-Feld, Kaku, King Riku).

## Procedimiento

1. Checklist de cobertura: qué universos se conciliaron y cuáles faltan.
2. Resume matched rates, montos unmatched y aging buckets.
3. Lista ajustes propuestos vs aplicados (solo aplicados con aprobación).
4. Adjunta evidencia de control: quién preparó, quién revisó, timestamps, fuentes.
5. Marca blockers de cierre (breaks materiales, mapping faltante, dispute comercial).
6. Separa COMPLETED vs COMPLETED_WITH_LIMITATIONS vs BLOCKED según materialidad.
7. Define NEXT_HANDOFF (Denjiro aprobación, Du-Feld pricing, Kaku posting, Brook ADR si decisión permanente).

## Salida

```md
## Periodo / alcance
## Checklist de cobertura
## Resumen de cuadres (KPIs)
## Aging de breaks
## Ajustes (propuestos / aplicados)
## Evidencia de control
## Blockers / limitaciones
## STATUS recomendado + NEXT_HANDOFF
```

## Casos límite

- Cierre pedido con 40% unmatched → no COMPLETED; limita o BLOCKED.
- Revisor = preparador en ajuste material → falla control; exige segundo par.
- Datos parciales de una moneda → cierra subalcance etiquetado, no el global.

## Validación

- Cobertura explícita.
- Evidencia preparador/revisor presente para reconciliaciones materiales.
- STATUS coherente con breaks abiertos.

## Criterios de terminado

- Denjiro puede aprobar o rechazar el cierre con un solo paquete.
- Limitaciones no están escondidas en prosa.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Conciliaciones OK + 3 breaks dueños | Pack + COMPLETED_WITH_LIMITATIONS |
| Ambiguo | “Cierra el mes” sin extractos | BLOCKED + inputs |
| Límite | Ajuste material sin revisor | REQUIRES_CORRECTION por control |

## Fuentes

- COSO ICIF — control activities, segregation, evidence (2026-08-04).
- Solvexia — reconciliation audit trail / approvals — https://www.solvexia.com/blog/internal-control-bank-reconciliation (2026-08-04).
- CPA Exams Mastery — proof of cash / period integrity (2026-08-04).
