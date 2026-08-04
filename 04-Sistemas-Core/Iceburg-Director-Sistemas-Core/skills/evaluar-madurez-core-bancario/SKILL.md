---
name: evaluar-madurez-core-bancario
description: Evalúa la madurez del core bancario (integridad, integración, coexistencia, operación, rollback) y produce gates de readiness. Úsala cuando se pida assessment de modernización, readiness de cutover o diagnóstico departamental de Sistemas Core.
metadata:
  author: yzylabs
  version: "1.0"
---

# Evaluar madurez Core bancario

## Propósito

Diagnosticar madurez del departamento/sistema de core con dimensiones observables y recomendaciones priorizadas.

## Entradas

- Alcance (producto, país, ledger, conjunto de interfaces).
- Evidencias: métricas, incidentes, mapas, contratos.
- Restricciones de tiempo y riesgo.

## Procedimiento

1. Evalúa dimensiones (0–5 o Red/Amber/Green):
   - Integridad / reconciliación
   - Idempotencia / reintentos
   - Integración / modelo canónico
   - Coexistencia / strangler
   - Observabilidad / operación
   - Rollback / cutover discipline
   - Ownership / catálogo de interfaces
2. Recoge evidencia por dimensión; marca “desconocido” si falta dato (no inventes scores altos).
3. Identifica blockers vs deuda aceptable.
4. Propón 3–7 acciones Now con dueño (Crocus/Tom/Kaku/otros).
5. Emite readiness para el objetivo pedido (p. ej. cutover X): Ready / Ready with limitations / Not ready.

## Salida

```md
## Madurez Sistemas Core
| Dimensión | Nivel | Evidencia | Gap |
## Readiness del objetivo
## Acciones Now
| Acción | Dueño | Gate |
## Riesgos
## Datos faltantes
```

## Casos límite

- Sin métricas de breaks: dimensión Integridad = desconocido/rojo; no declare Ready.
- Core externalizado (vendor): evalúa controles contractuales y de integración, no asumas control total del ledger.
- Multi-país: madurez por perímetro; evita promedio engañoso.

## Validación

- Cada score tiene evidencia o “desconocido”.
- Readiness coherente con gaps rojos.
- Acciones Now son finitas y asignables.

## Criterios de terminado

- Assessment usable para priorización de Iceburg/Luffy.
- Readiness explícita para el objetivo.
- Lista de datos faltantes para re-evaluación.

## Fuentes

- `references/mapa-gobierno-sistemas-core.md` — 2026-08-04
- Swift ISO 20022 — contexto de modernización de pagos — https://www.swift.com/standards/iso-20022 (2026-08-04)
- Prácticas de readiness operacional en modernización core (síntesis contrastada, 2026-08-04)
