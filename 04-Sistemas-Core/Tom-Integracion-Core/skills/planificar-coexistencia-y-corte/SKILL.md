---
name: planificar-coexistencia-y-corte
description: Planifica coexistencia de formatos/sistemas (MT/MX, dual-write, shadow) y corte hacia el core con reconciliación. Úsala en migraciones o reemplazos de integración sin big-bang ciego.
metadata:
  author: yzylabs
  version: "1.0"
---

# Planificar coexistencia y corte

## Propósito

Diseñar un camino seguro de coexistencia y cutover para integraciones core, con criterios medibles de paridad y no-duplicación.

## Entradas

- Estado as-is / to-be de formatos y sistemas.
- Volúmenes y ventanas de mantenimiento.
- Capacidad de dual-write / shadow del core.
- Requisitos de reconciliación y auditoría.
- Fechas de mercado solo si hay fuente (no inventar).

## Procedimiento

1. Inventaría flujos en alcance y dependencia entre ellos.
2. Elige patrón por flujo: dual-write, shadow compare, strangler, cutover seco.
3. Define criterios de éxito (paridad de campos, tasa de mismatch, lag, duplicados=0).
4. Diseña reconciliación automatizable (claves de negocio, reportes, umbrales).
5. Plan de rollback y freeze de cambios durante ventana.
6. Documenta truncation y comportamientos divergentes durante coexistencia.
7. Asigna dueños (Tom diseño, Kaku posting, Crocus legado, ops ejecución).
8. Produce timeline por fases con go/no-go checks.

## Salida

```md
## Alcance de flujos
## Patrón por flujo
## Criterios go/no-go
## Reconciliación
## Rollback
## Riesgos de coexistencia
## Timeline / dueños
```

## Casos límite

- Negocio exige big-bang sin reconciliación → REJECT / COMPLETED_WITH_LIMITATIONS con riesgo explícito a Iceburg.
- Dual-write dobla posting → exige deduplicación; escala a Kaku.
- Fecha regulatoria incierta → no inventes deadline; lista fuente faltante.

## Validación

- Cada flujo tiene patrón y criterio medible.
- Rollback documentado.
- Ownership de posting vs integración claro.

## Criterios de terminado

- Iceburg puede aprobar o rechazar el corte con evidencia.
- No queda “migración lista” sin reconciliación.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | MT statements → camt.053 | Fases shadow → dual → cutover + reconciliación |
| Ambiguo | “Migremos el core el sábado” | Preguntas de flujos + plan mínimo anti-big-bang |
| Límite | Sin ambiente de shadow | BLOCKED + alternativas (replay histórico, muestreo) |

## Fuentes

- BlazeTrends dual-write / middleware — https://blazetrends.com/how-core-banking-apis-connect-with-external-financial-systems/ (2026-08-04).
- SWIFT ISO 20022 coexistence / implementation — https://www.swift.com/standards/iso-20022/iso-20022-standards (2026-08-04).
- SWIFT Implementation FAQ — https://www.swift.com/standards/iso-20022/iso-20022-faqs/implementation (2026-08-04).
- 6B Core Banking Integration — https://6b.finance/insight/core-banking-system-integration-using-iso-20022-rest-apis-and-legacy-message-queues/ (2026-08-04).
