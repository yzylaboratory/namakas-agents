---
name: configurar-agente-reconciliacion
description: Configura Applications/ApplicationSets (Argo) o GitRepository/Kustomization/HelmRelease (Flux) con políticas de sync. Úsala cuando haya que cablear el agente pull-based al desired state.
metadata:
  author: yzylabs
  version: "1.0"
---

# Configurar agente de reconciliación

## Propósito

Definir cómo el agente GitOps hace pull del state store y reconcilia continuamente el cluster: recursos de fuente, destino, sync policy, prune y self-heal — conforme a OpenGitOps principios 3 y 4.

## Entradas

- Stack elegido (Argo CD o Flux).
- URL/path del desired state y credenciales de lectura (sin pegar secretos).
- Destino (cluster, namespace, project/tenant).
- Política deseada (auto-sync, manual, ventanas).
- Restricciones RBAC y network.

## Procedimiento

1. Declara la fuente (Git repo/path, Helm chart, OCI) con pin de revisión cuando aplique.
2. Declara el destino (cluster/namespace) y isolation (Argo Project / Flux namespace).
3. Configura sync policy: automated vs manual; prune; selfHeal.
4. Define retry/backoff y ignoreDifferences solo con justificación.
5. Para multi-app: ApplicationSet (Argo) o kustomizations anidadas (Flux).
6. Documenta health checks y qué significa “Synced/Healthy”.
7. Lista permisos mínimos del ServiceAccount del agente.
8. Entrega manifests/CRDs de ejemplo + checklist de bootstrap.

## Salida

```md
## Fuente(s)
## Destino(s)
## Recursos del agente (CRDs/CRs)
## Sync policy (auto/prune/self-heal)
## Multi-app / generators
## RBAC mínimo
## Health / señales para Viola
## Checklist de verificación
```

## Casos límite

- Repo privado sin access desde el cluster → documenta deploy key / workload identity; no dejes PAT en Git.
- Auto-sync + prune en prod sin gates → exige promoción previa o sync manual en prod.
- ignoreDifferences abusivo → trata como drift aceptado; lista riesgo.

## Validación

- Pull automático desde el cluster (o agente) está descrito.
- Reconciliación continua no depende de un humano corriendo apply.
- Secretos de repo no están en el entregable en claro.
- Política de prune/self-heal es explícita por entorno.

## Criterios de terminado

- Un operador puede aplicar los CRs y ver el primer sync.
- Queda claro cómo se observa el estado de sync (señales a Viola).

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Argo + repo apps/dev | Application con auto-sync en dev |
| Ambiguo | “Conecta Flux” sin path | Preguntas + plantilla GitRepository+Kustomization |
| Límite | Prod con prune automático sin owners | Sync manual o gates; no auto-prune ciego |

## Fuentes

- OpenGitOps Principles v1.0.0 (Pulled Automatically, Continuously Reconciled) — https://opengitops.dev/ (2026-08-04).
- Argo CD docs — https://argo-cd.readthedocs.io/ (2026-08-04).
- Flux docs — https://fluxcd.io/flux/ (2026-08-04).
