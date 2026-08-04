---
name: evaluar-madurez-ux
description: Evalúa la madurez UX organizacional (modelo NN/g de 6 etapas) y propone el siguiente paso realista. Úsala cuando se pida diagnóstico de madurez UX, DesignOps maturity o plan para profesionalizar la práctica de experiencia.
metadata:
  author: yzylabs
  version: "1.0"
---

# Evaluar madurez UX

## Propósito

Diagnosticar la madurez UX de la organización o producto en los factores estrategia, cultura, proceso y outcomes, y proponer un ascenso de etapa creíble.

## Entradas

- Evidencia de práctica actual (rituales, research en roadmap, design system, métricas).
- Entrevistas/inputs de stakeholders (Producto, Eng, UX) si disponibles.
- Alcance (equipo, producto, empresa).
- Restricciones de capacidad.

## Procedimiento

1. Recuerda el modelo NN/g de **6 etapas**: Absent → Limited → Emergent → Structured → Integrated → User-driven.
2. Evalúa cuatro factores: **strategy**, **culture**, **process**, **outcomes**.
3. Asigna etapa actual con evidencia (no deseo).
4. Identifica 3–5 gaps que impiden el siguiente nivel.
5. Propón un plan de 90 días con dueños (Nami + células + Luffy/otros).
6. Define señales de progreso observables (no vanity metrics).
7. Separa “teatro UX” (artefactos sin decisión) de práctica real.

## Salida

```md
## Evaluación de madurez UX
- Alcance:
- Etapa actual (1–6) y nombre:
- Evidencia por factor (strategy/culture/process/outcomes):
## Gaps hacia la siguiente etapa
## Plan 90 días
| Acción | Dueño | Señal de progreso |
## Riesgos / anti-patrones
## Recomendación a Luffy
```

## Casos límite

- Startup temprana: no forzar Integrated; apunta a Emergent/Structured con research en journeys críticos.
- Design system sin adopción: no cuenta como Integrated solo por existir librería.
- AI generando UI: madurez exige gobernanza de sistema + juicio humano (taste/research), no volumen de pantallas.

## Validación

- Etapa justificada con evidencia.
- Plan acotado y con dueños.
- No se infla la etapa por aspiración.

## Criterios de terminado

- Diagnóstico defendible ante Luffy.
- Siguiente paso único y realista.
- Métricas/señales definidas.

## Fuentes

- Nielsen Norman Group — The 6 Levels of UX Maturity — https://www.nngroup.com/articles/ux-maturity-model/ (2026-08-04)
- Nielsen Norman Group — State of UX in 2026 — https://www.nngroup.com/articles/state-of-ux-2026/ (2026-08-04)
- ISO 9241-220 — Processes for enabling HCD in organizations (referencia de industria para enablement) — consultado 2026-08-04
