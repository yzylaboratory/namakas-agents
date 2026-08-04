---
name: evaluar-madurez-devops-plataforma
description: Evalúa la madurez de DevOps/plataforma (CI/CD, GitOps, IaC, observabilidad, self-service, cultura de producto interno) con gates y roadmap de mejora. Úsala cuando se pida assessment de madurez, readiness de paved road o diagnóstico antes de escalar self-service.
metadata:
  author: yzylabs
  version: "1.0"
---

# Evaluar madurez DevOps / plataforma

## Propósito

Diagnosticar el estado actual del departamento y de los consumidores del paved road, con niveles explícitos, evidencia y plan de cierre de gaps — sin checklist genérico vacío.

## Entradas

- Alcance (org, dominio, producto).
- Evidencia operativa (pipelines, repos IaC, GitOps, dashboards, postmortems).
- Adopción actual de templates/paths.
- Restricciones de seguridad y compliance de alto nivel.

## Procedimiento

1. Define dimensiones de evaluación (mínimo):
   - CI/CD y quality gates (Paulie).
   - GitOps / deploy declarativo (Capone Bege).
   - IaC / cloud reproducibility (Haredas).
   - Observabilidad / SRE practices (Viola).
   - Self-service / product mindset / feedback (Franky).
   - Seguridad baseline embebida en paths (coordinación Fujitora).
2. Para cada dimensión asigna nivel (p. ej. 0 ausente → 4 optimizado) con **evidencia** o “sin evidencia”.
3. Identifica blockers para el siguiente nivel (no más de 3 por dimensión).
4. Cruza con métricas DORA/DevEx disponibles (o gaps).
5. Propón plan Now/Next de cierre alineado a capacidad del squad.
6. Marca riesgos de J-curve (dip temporal al madurar plataforma) si aplica.

## Salida

```md
## Alcance
## Scorecard de madurez
| Dimensión | Nivel | Evidencia | Blocker principal | Dueño |
## Gaps críticos
## Plan de mejora Now/Next
## Dependencias externas
## Riesgos
```

## Casos límite

- “Tenemos Kubernetes” ≠ madurez de plataforma: exige journeys y self-service, no solo runtime.
- Alta automatización con cero observabilidad: nivel de CI/CD no puede ser alto si change failure es ciego.
- Células stub: evalúa con evidencia de sistemas reales; no asumas capacidad celular forjada.

## Validación

- Cada nivel cite evidencia o declare ausencia.
- Blockers son accionables y con dueño.
- Plan no salta gates de seguridad/observabilidad.

## Criterios de terminado

- Assessment usable para priorización.
- Diferencia clara entre runtime tools y plataforma como producto.
- Próximos pasos delegables al squad.

## Fuentes

- DORA Platform engineering — MVP platform, J-curve, measurement — https://dora.dev/capabilities/platform-engineering/ (consultado 2026-08-04)
- CNCF Platforms White Paper — capabilities curated for internal customers (consultado 2026-08-04)
- DORA four keys como outcomes de madurez de entrega — https://dora.dev/ (consultado 2026-08-04)
