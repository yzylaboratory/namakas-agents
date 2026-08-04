---
name: preparar-paquete-monetizacion-api
description: Consolida el paquete de monetización profunda (pricing + métrica + metering + share + reconciliación) desde handoff Sabo. Úsala para entregar a Denjiro/Legal/ops; no para DX o portal UI.
metadata:
  author: yzylabs
  version: "1.0"
---

# Preparar paquete de monetización de API

## Propósito

Empaquetar una decisión de monetización completa y auditables para aprobación y ejecución, consumiendo el handoff light de Sabo.

## Entradas

- Handoff Sabo (tiers light, fair use, drivers, gaps).
- Salidas de skills de pricing/métrica/metering/share/reconciliación (o ejecutarlas).
- Restricciones Denjiro / Legal conocidas.

## Procedimiento

1. Verifica handoff Sabo: si falta, lista gaps o `DELEGATION_REQUIRED` a Sabo/Luffy.
2. Consolida: clasificación API, modelo de precio, value metric, metering/billing, revenue share (si aplica), reconciliación.
3. Completa RACI: Du-Feld, Denjiro, Sabo, Koala, Gild, Legal, King Riku.
4. Marca estado “listo para cobrar” solo si pasan reglas hard de Reglas.md; si no, lista blockers.
5. Separa decisiones abiertas (precio final, descuentos enterprise, MG) de hechos.
6. Adjunta fuentes/supuestos y riesgos (bill shock, leakage, regulatorio).
7. Define NEXT_HANDOFF (Denjiro aprobación → Legal term sheet → eng metering → Gild).
8. Emite resumen ejecutivo ≤1 página + apéndices.

## Salida

```md
## Executive summary
## Inputs Sabo / gaps
## Pricing + métrica
## Metering / billing
## Revenue share (si aplica)
## Reconciliación / Gild
## RACI
## Listo para cobrar? (sí/no + blockers)
## Decisiones requeridas
## Fuentes
```

## Casos límite

- Solo piden price list sin metering → paquete con BLOCKED + spec metering mínima.
- Conflicto Sabo tiers vs planes profundos → documenta delta; no silencies.
- Multi-producto → un paquete por producto o matriz clara.

## Validación

- Sin placeholders.
- Regla hard de monetización aplicada.
- Dueños explícitos.
- Reportable a `denjiro-director-finanzas`.

## Criterios de terminado

- Paquete usable para aprobación Denjiro.
- Blockers y next handoff claros.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Handoff Sabo completo | Paquete full + listo para cobrar condicionado a Legal |
| Ambiguo | “Monetiza el ecosistema” | Preguntas + DELEGATION_REQUIRED Sabo/Denjiro |
| Límite | Sin value metric ni eventos | BLOCKED con gaps dueñados |

## Fuentes

- Rol.md Du-Feld — fuentes de monetización 2026 (2026-08-04).
- Sabo — `definir-partnership-monetizacion-light` handoff shape (2026-08-04).
