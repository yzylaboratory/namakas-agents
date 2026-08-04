---
name: modelar-desired-state
description: Modela el desired state declarativo (manifiestos, Kustomize, Helm, OCI) versionado e inmutable. Úsala cuando haya que estructurar overlays, values y referencias a artefactos para GitOps.
metadata:
  author: yzylabs
  version: "1.0"
---

# Modelar desired state

## Propósito

Expresar el estado deseado de forma declarativa y auditable en el state store, con referencias inmutables a artefactos y overlays por entorno — sin scripts imperativos ni secretos en claro.

## Entradas

- Workloads y config a desplegar.
- Artefactos publicados por CI (imagen, chart, OCI digest).
- Convención de entornos y overlays.
- Restricciones de naming, labels y policy (PSS, network).
- Estrategia de secretos (External Secrets / sealed / CSI).

## Procedimiento

1. Inventaría recursos Kubernetes (o equivalentes) que forman el desired state.
2. Elige empaquetado: YAML plano, Kustomize bases/overlays, Helm chart+values, o OCI.
3. Fija referencias de imagen por digest en prod; evita `latest`.
4. Separa base común de overlays por entorno (replicas, URLs, resources).
5. Externaliza secretos: solo referencias; documenta el proveedor.
6. Añade labels/annotations de ownership y app para sync/observabilidad.
7. Valida que un `diff` de Git explique cualquier cambio de prod.
8. Entrega árbol de directorios + ejemplo mínimo de overlay.

## Salida

```md
## Inventario de recursos
## Empaquetado elegido
## Árbol de directorios
## Referencias de artefactos (digests/tags)
## Overlays por entorno
## Estrategia de secretos
## Validaciones (kubeconform/kustomize build/helm template)
## Riesgos
```

## Casos límite

- Chart de terceros sin values tipados → overlay controlado + pin de versión chart.
- Config que cambia cada minuto (feature flags runtime) → no fuerces todo a Git; delimita qué es desired state.
- Secretos legacy en ConfigMaps → bloquea; escala patrón de secretos.

## Validación

- Desired state es declarativo y versionable.
- Prod no depende de tags flotantes sin justificación documentada.
- Ningún secreto en claro en el ejemplo.
- Build local del overlay/chart es reproducible.

## Criterios de terminado

- Un agente GitOps puede reconciliar el árbol sin pasos manuales extra.
- Paulie sabe qué artefacto debe publicar para que el overlay lo consuma.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | API Deployment + Service, 3 envs | Base + overlays con digests |
| Ambiguo | “Pon esto en Git” (carpeta mixta) | Separación desired vs basura; árbol propuesto |
| Límite | Password en YAML | Rechazo + patrón External Secrets |

## Fuentes

- OpenGitOps Principles v1.0.0 (Declarative, Versioned and Immutable) — https://opengitops.dev/ (2026-08-04).
- Flux docs (sources & HelmRelease) — https://fluxcd.io/flux/ (2026-08-04).
- Argo CD docs (declarative setup) — https://argo-cd.readthedocs.io/ (2026-08-04).
