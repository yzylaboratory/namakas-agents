---
name: seleccionar-stack-gitops
description: Elige o justifica Argo CD vs Flux (u otro agente pull-based) con criterios OpenGitOps. Úsala cuando haya que decidir herramienta de reconciliación, no para implementar el pipeline CI.
metadata:
  author: yzylabs
  version: "1.0"
---

# Seleccionar stack GitOps

## Propósito

Recomendar el agente de reconciliación (típicamente Argo CD o Flux, ambos CNCF graduated) alineado a requisitos de UI, modularidad, fuentes (Git/Helm/OCI) y progressive delivery — sin inventar capacidades.

## Entradas

- Requisitos de UX (UI web vs CLI-first).
- Fuentes de config (Git, Helm, OCI, S3).
- Necesidad de ApplicationSets / multi-cluster / multi-tenant.
- Progressive delivery (Rollouts vs Flagger).
- Skills del equipo y restricciones de plataforma.

## Procedimiento

1. Confirma que el problema es reconciliación GitOps (no CI build).
2. Lista criterios ponderados: UI, modularidad, OCI/Helm, multi-source, PD, operación.
3. Contrasta Argo CD (all-in-one + UI) vs Flux (toolkit modular + CLI).
4. Descarta push-only desde CI como “GitOps completo” si falta reconciliación continua.
5. Documenta progressive delivery: Argo Rollouts vs Flagger como extensión.
6. Señala dependencias (RBAC del agente, ingress UI, network policies).
7. Emite recomendación principal + alternativa y criterios de revisión.
8. Cita fuentes CNCF/OpenGitOps con fecha.

## Salida

```md
## Contexto y no-objetivos
## Criterios ponderados
## Comparativa Argo CD vs Flux
## Recomendación principal
## Alternativa
## Progressive delivery
## Riesgos / prerequisites
## Fuentes
```

## Casos límite

- Equipo solo conoce Helm + CI push → explicar gap OpenGitOps; no fingir conformidad.
- Requisito estricto de OCI-only → priorizar capacidades documentadas de Flux/Argo; verificar docs vigentes.
- Mandato ejecutivo de una herramienta → documentar conformidad y gaps, no sabotear.

## Validación

- Ambos lados de la comparación tienen criterios observables.
- No se inventan features; se citan docs/CNCF.
- Pull + reconcile quedan como requisito no negociable para “GitOps conforme”.

## Criterios de terminado

- Franky/equipo puede decidir con la matriz sin investigación adicional.
- Queda explícito qué queda fuera (CI Paulie, IaC Haredas).

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | UI fuerte + apps Helm | Argo CD como principal con justificación |
| Ambiguo | “Lo más GitOps” | Matriz + pregunta de UI/OCI/multi-cluster |
| Límite | Solo push desde Jenkins al API | COMPLETED_WITH_LIMITATIONS: no es GitOps completo |

## Fuentes

- CNCF GitOps in 2025 (Argo vs Flux) — https://www.cncf.io/blog/2025/06/09/gitops-in-2025-from-old-school-updates-to-the-modern-way/ (2025-06-09).
- CNCF What is Flux CD? — https://www.cncf.io/blog/2023/09/15/what-is-flux-cd/ (2023-09-15).
- OpenGitOps Principles v1.0.0 — https://opengitops.dev/ (2026-08-04).
- Argo CD docs — https://argo-cd.readthedocs.io/ (2026-08-04).
- Flux docs — https://fluxcd.io/flux/ (2026-08-04).
