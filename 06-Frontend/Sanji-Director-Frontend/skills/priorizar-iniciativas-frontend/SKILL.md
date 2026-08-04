---
name: priorizar-iniciativas-frontend
description: Prioriza el backlog Frontend con valor de usuario, dependencias multi-canal, riesgo de deuda a11y/perf y capacidad del squad. Úsala cuando haya que ordenar iniciativas web/móvil/portal o replanificar el departamento Frontend.
metadata:
  author: yzylabs
  version: "1.0"
---

# Priorizar iniciativas Frontend

## Propósito

Producir un backlog ordenado y defendible para el departamento Frontend, con gates explícitos.

## Entradas

- Lista de iniciativas o epics.
- Capacidad estimada de Cavendish / Reiju / Koala.
- Dependencias (Nami, Backend, Robin, Sabo, QA).
- Métricas o auditorías recientes (CWV, a11y, crashes, adopción DS).

## Procedimiento

1. Normaliza cada ítem: problema de usuario, canal(es), hipótesis de valor, esfuerzo relativo.
2. Puntúa (o clasifica) por: valor, urgencia (incl. cumplimiento a11y), riesgo de no hacer, dependencia bloqueante.
3. Aplica gates antes de “Now”:
   - ¿Hay dueño de canal?
   - ¿DoD de calidad aplicable definido?
   - ¿Dependencia de API/design resuelta o acotada?
4. Ordena Now / Next / Later; marca Quick wins de plataforma que desbloqueen varios features.
5. Identifica WIP máximo por canal para evitar thrash multi-front.
6. Documenta trade-offs rechazados (qué no se hará ahora y por qué).

## Salida

```md
## Backlog priorizado Frontend
| ID | Iniciativa | Canal | Valor | Riesgo | Dependencias | Now/Next/Later | Dueño |
## Gates aplicados
## Capacidad y WIP
## Trade-offs / diferidos
## Decisiones requeridas (Luffy / otros)
```

## Casos límite

- Tres canales piden “lo mismo” a la vez: prioriza journey crítico + paridad documentada, no triple implementación ciega.
- Deuda a11y vs feature comercial: explicitar riesgo legal/reputacional; no esconder el trade-off.
- Célula stub: prioriza igual pero marca ejecución BLOCKED hasta forja o `DELEGATION_REQUIRED`.

## Validación

- Cada Now tiene dueño y dependencia explícita.
- No hay dos Now críticos sin capacidad.
- Riesgos de calidad no quedan implícitos.

## Criterios de terminado

- Backlog usable en planificación sin reinterpretar criterios.
- Trade-offs visibles para Luffy.

## Fuentes

- web.dev Core Web Vitals thresholds — https://web.dev/articles/vitals (2026-08-04)
- W3C WCAG 2.2 como referencia de riesgo/cumplimiento de experiencia — https://www.w3.org/TR/WCAG22/ (2026-08-04)
