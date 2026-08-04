---
name: disenar-arquitectura-gitops
description: Diseña la topología GitOps (repos, paths, entornos, ownership y fronteras). Úsala cuando se pida arquitectura de state store, multi-cluster o layout de promoción antes de configurar Argo/Flux.
metadata:
  author: yzylabs
  version: "1.0"
---

# Diseñar arquitectura GitOps

## Propósito

Definir cómo se organiza el desired state: dónde vive, quién lo cambia, cómo se aíslan entornos y cómo se cumple OpenGitOps sin convertir el cluster en fuente de verdad.

## Entradas

- Apps / plataformas a gestionar.
- Número de clusters y entornos (dev/staging/prod).
- Restricciones de ownership y compliance.
- Stack tentativo (Argo CD, Flux, Helm, Kustomize).
- Inventario de repos existentes (si hay).

## Procedimiento

1. Lista sistemas y entornos; marca qué es desired state vs dato runtime.
2. Elige topología: mono-repo, multi-repo por equipo, o repo de apps + repo de plataforma.
3. Define paths/overlays por entorno y reglas de merge (quién aprueba `prod`).
4. Declara fronteras: namespace, cluster, app, secret store.
5. Separa responsabilidades: CI produce artefactos (Paulie); GitOps declara referencias; IaC cloud (Haredas) fuera del path de app config salvo acuerdo.
6. Documenta bootstrap del agente GitOps (instalación mínima) sin secretos en claro.
7. Verifica cobertura de los 4 principios OpenGitOps v1.0.0.
8. Lista riesgos (blast radius, permisos de merge, acoplamiento de repos).

## Salida

```md
## Objetivo y sistemas
## Topología de state store
## Paths / overlays por entorno
## Ownership y gates de merge
## Fronteras cluster/namespace/app
## Bootstrap agente GitOps
## Conformidad OpenGitOps (4 principios)
## Riesgos / handoffs
```

## Casos límite

- Un solo cluster “prod-only” → igual exige versionado + reconciliación; no omitas staging lógico si hay riesgo.
- Multi-tenant con equipos hostiles → multi-repo o CODEOWNERS estrictos; no compartas path `prod` abierto.
- Legacy con kubectl diario → arquitectura de migración por oleadas, no big-bang sin inventario.

## Validación

- State store versionado/inmutable identificado.
- Entornos con frontera de promoción explícita.
- Secretos no viven en claro en el diseño.
- Handoffs Paulie/Haredas/Viola nombrados cuando aplica.

## Criterios de terminado

- Un equipo puede implementar el layout sin adivinar ownership.
- Queda claro qué NO es GitOps en el diseño (CI, IaC cloud).

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | 3 envs, 2 equipos, Argo CD | Mono o multi-repo con paths y CODEOWNERS |
| Ambiguo | “Queremos GitOps” | Preguntas + 2 topologías candidatas con trade-offs |
| Límite | 10 equipos, un repo compartido sin owners | Rechazo del layout; propuesta multi-repo o owners |

## Fuentes

- OpenGitOps Principles v1.0.0 — https://opengitops.dev/ (2026-08-04).
- OpenGitOps PRINCIPLES.md — https://github.com/open-gitops/documents/blob/main/PRINCIPLES.md (2026-08-04).
- CNCF GitOps in 2025 — https://www.cncf.io/blog/2025/06/09/gitops-in-2025-from-old-school-updates-to-the-modern-way/ (2025-06-09).
