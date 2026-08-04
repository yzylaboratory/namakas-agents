---
name: auditar-deriva-y-sync
description: Audita drift entre estado real y desired state, políticas de self-heal y conformidad OpenGitOps. Úsala cuando haya que investigar divergencias, sync fallido o cumplimiento GitOps.
metadata:
  author: yzylabs
  version: "1.0"
---

# Auditar deriva y sync

## Propósito

Detectar, clasificar y remediar (vía Git) las divergencias entre el estado real del cluster y el desired state, y evaluar si el flujo cumple los cuatro principios OpenGitOps.

## Entradas

- Sync status del agente (Argo/Flux) y apps afectadas.
- Diffs conocidos (kubectl, cambios manuales, operadores).
- Política vigente (self-heal, ignoreDifferences).
- Ventana temporal del incidente o auditoría.
- Acceso de solo lectura a status (preferido).

## Procedimiento

1. Obtén estado de sync/health por app y última revisión reconciliada.
2. Clasifica drift: manual edit, operador externo, out-of-band pipeline, fallo de sync, ignoreDifferences.
3. Evalúa conformidad OpenGitOps (declarativo, inmutable, pull, reconcile).
4. Decide remediación: self-heal, commit que formaliza el cambio, o rollback Git.
5. Señala cambios que deben permanecer fuera de Git (efímeros) vs los que deben entrar.
6. Propón alertas/señales para Viola sin diseñar toda la plataforma SRE.
7. Documenta blameless timeline: qué divergió, cuándo, impacto.
8. Emite veredicto: conforme / conforme con limitaciones / no GitOps.

## Salida

```md
## Alcance auditado
## Sync/health observado
## Drift clasificado
## Conformidad OpenGitOps (checklist)
## Remediación vía Git
## Señales / handoff Viola
## Veredicto y riesgos
## Evidencia
```

## Casos límite

- Self-heal apagado y drift “aceptado” → documenta deuda; no finjas conformidad.
- Operador que muta campos continuamente → ignoreDifferences acotado + dueño del operador.
- Sin acceso al cluster → auditoría por status exportado; marca limitaciones.

## Validación

- Cada hallazgo tiene evidencia (sync revision, diff, commit).
- Remediación preferente es Git, no runbook de kubectl edit.
- Veredicto no afirma OpenGitOps v1.0.0 si falta un principio.

## Criterios de terminado

- Franky recibe veredicto accionable con dueños.
- Drift material tiene plan de cierre o aceptación explícita.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | App Degraded, replicas editadas a mano | Drift manual + self-heal o commit |
| Ambiguo | “Prod se siente distinto” | Plan de recolección de sync status + preguntas |
| Límite | Solo CI push, sin agente | Veredicto no GitOps + gap list |

## Fuentes

- OpenGitOps Principles v1.0.0 — https://opengitops.dev/ (2026-08-04).
- OpenGitOps PRINCIPLES.md — https://github.com/open-gitops/documents/blob/main/PRINCIPLES.md (2026-08-04).
- Argo CD docs (sync / diff) — https://argo-cd.readthedocs.io/ (2026-08-04).
- Flux docs (reconciliation) — https://fluxcd.io/flux/ (2026-08-04).
