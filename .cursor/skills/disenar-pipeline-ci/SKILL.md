---
name: disenar-pipeline-ci
description: Diseña o actualiza un pipeline de integración continua (pipeline-as-code) con triggers, etapas fail-fast, jobs y artefactos. Úsala cuando se pida crear/mejorar CI (lint, test, build) en GitHub Actions, GitLab CI u otra plataforma — no para GitOps ni IaC de cloud.
metadata:
  author: yzylabs
  version: "1.0"
---

# Diseñar pipeline CI

## Propósito

Definir un pipeline de integración continua versionado, reproducible y fail-fast que valide cambios cerca del commit.

## Entradas

- Plataforma CI (GitHub Actions, GitLab CI, Azure Pipelines, Jenkins, etc.).
- Repositorio y estrategia de branching.
- Stack de build/test (lenguaje, managers, contenedores).
- Triggers deseados (PR, push, tag, schedule).
- Restricciones de runners y tiempos.

## Procedimiento

1. Confirma plataforma y ubicación canónica del pipeline (p. ej. `.github/workflows/`, `.gitlab-ci.yml`).
2. Declara triggers y path filters; evita pipelines globales innecesarios.
3. Ordena etapas: lint/format → unit → build → integration (ajusta al stack).
4. Define jobs con dependencias explícitas (`needs` / `dependencies`) y fail-fast.
5. Publica artefactos de build para reutilizar en CD (build once).
6. Parametriza versiones de toolchains; evita “latest” sin pin.
7. Documenta variables requeridas y runners (hosted vs self-hosted).
8. Entrega YAML + resumen de etapas + riesgos.

## Salida

- Archivo(s) de pipeline CI.
- Tabla etapas → jobs → artefactos.
- Lista de variables/secretos necesarios (nombres, no valores).
- Pendientes y riesgos.

## Casos límite

- Monorepo → path filters / pipelines por paquete; no un único job monolítico sin justificación.
- Solo CD solicitado → no fuerces CI vacío; declara gap de CI.
- Runner self-hosted único → documenta cola y single-point-of-failure.

## Validación

- Pipeline-as-code en repo.
- Orden fail-fast coherente.
- Artefactos definidos si habrá CD.
- Sin secretos en claro en el YAML.

## Criterios de terminado

- Un revisor puede entender qué corre en cada trigger.
- El diseño es implementable en la plataforma indicada.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | App Node en GitHub, PRs a main | Workflow lint+test+build con artefactos |
| Ambiguo | “Pon CI” sin stack | Preguntas mínimas + esqueleto por plataforma candidata |
| Límite | Monorepo 8 paquetes | Path filters / matrix por paquete; no pipeline único ciego |

## Fuentes

- GitHub Docs — Workflow syntax — https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions (2026-08-04).
- GitLab Docs — CI/CD YAML — https://docs.gitlab.com/ee/ci/yaml/ (2026-08-04).
- DORA metrics — https://dora.dev/ (2026-08-04).
