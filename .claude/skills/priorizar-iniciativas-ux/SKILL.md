---
name: priorizar-iniciativas-ux
description: Prioriza el backlog UX/UI con impacto en usuario, riesgo, dependencia y dueño. Úsala cuando haya que ordenar iniciativas de experiencia, decidir qué rediseñar primero o recortar alcance UX.
metadata:
  author: yzylabs
  version: "1.0"
---

# Priorizar iniciativas UX

## Propósito

Producir un backlog priorizado de iniciativas UX/UI con justificación explícita y gates de salida.

## Entradas

- Lista de iniciativas / journeys / deudas UX candidatas.
- Evidencia disponible (research, métricas, tickets, auditorías a11y).
- Capacidad del squad y dependencias externas (Frontend, APIs, Legal).
- Restricciones de plazo y riesgo.

## Procedimiento

1. Normaliza cada ítem: problema de usuario, evidencia, alcance, esfuerzo relativo, riesgo.
2. Puntúa (o rankea) por: impacto en usuario, severidad de fricción/a11y, urgencia de negocio, dependencia bloqueante.
3. Aplica gates: no priorizar rediseño cosmético sobre defectos de usabilidad/a11y severos sin justificación.
4. Asigna dueño tentativo (Chopper / Perona / Miss Goldenweek / Nami / externo).
5. Construye Now (capacidad real) / Next / Later / Won't.
6. Documenta trade-offs y qué se sacrifica.
7. Define criterio de salida por ítem Now (evidencia mínima aceptable).

## Salida

```md
## Backlog UX priorizado
| Prioridad | Iniciativa | Impacto | Riesgo | Dueño | Gate de salida | Evidencia |
## Now / Next / Later / Won't
## Trade-offs
## Dependencias externas
## Decisiones requeridas
```

## Casos límite

- Empate de impacto: prioriza riesgo a11y/legal y journeys de mayor volumen.
- Presión de “ship visual”: documenta riesgo y escala a Luffy si se ignora evidencia.
- Sin datos: prioriza discovery acotado antes de build amplio.

## Validación

- Cada ítem Now tiene dueño y gate.
- La justificación cita evidencia o declara su ausencia.
- No hay solapamiento ambiguo entre células.

## Criterios de terminado

- Backlog accionable para una iteración.
- Trade-offs explícitos.
- Listo para coordinar squad o escalar.

## Fuentes

- Nielsen Norman Group — UX maturity / prioritization under resource constraints (síntesis State of UX 2026) — https://www.nngroup.com/articles/state-of-ux-2026/ (2026-08-04)
- ISO 9241-11 — Usability (effectiveness, efficiency, satisfaction) como criterio de impacto — consultado 2026-08-04
