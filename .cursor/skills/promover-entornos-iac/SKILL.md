---
name: promover-entornos-iac
description: Diseña promoción dev→stage→prod con módulos versionados y states separados. Úsala cuando se pida liberar infrastructure changes entre entornos sin copiar state ni drift silencioso.
metadata:
  author: yzylabs
  version: "1.0"
---

# Promover entornos IaC

## Propósito

Mover el mismo diseño de infraestructura entre entornos mediante artefactos versionados, no mediante clonación de state ni applies manuales divergentes.

## Entradas

- Stacks/módulos involucrados.
- Entornos y backends/keys.
- Diferencias legítimas por env (sizing, multi-AZ, retención).
- Requisitos de aprobación/ventana en prod.

## Procedimiento

1. Inventaría divergencias actuales (código, vars, drift).
2. Fija el artefacto promovible: tag de módulo / commit SHA / versioned package.
3. Mantén roots por entorno con vars distintas; misma fuente de módulo.
4. Verifica state keys distintos; aborta si prod comparte backend path.
5. Define secuencia: plan non-prod → apply → validar → plan prod → aprobación → apply.
6. Lista checks obligatorios pre-prod (guardrails, tests, peer review).
7. Documenta rollback: revert de tag + plan; destroy solo con autoridad explícita.
8. Handoff a Paulie para automatizar la secuencia en CI; Haredas no inventa el YAML del pipeline.

## Salida

```md
## Artefacto promovible
## Matriz env → backend/key → vars
## Secuencia de promoción
## Checks pre-prod
## Rollback
## Handoff CI (Paulie)
```

## Casos límite

- Hotfix solo en prod → deuda; exige backport a módulo y plan de convergencia.
- Workspaces únicos para todo → aceptable en escala pequeña; documenta límite y plan de split.
- Cambios de provider major → promoción congelada hasta guía de migración.

## Validación

- Ningún share de state prod/non-prod.
- Artefacto versionado identificable.
- Rollback path escrito.
- Dueño de apply prod explícito.

## Criterios de terminado

- Runbook de promoción usable por plataforma.
- Riesgos de drift entre envs listados.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Módulo red v1.2.0 a stage→prod | Secuencia + keys + aprobación |
| Ambiguo | “Pásalo a prod” | Preguntas artefacto/state + plan mínimo |
| Límite | State prod = state stage | STOP + redesign de backends |

## Fuentes

- OpenTofu Remote State — https://opentofu.org/docs/language/state/remote/ (2026-08-04).
- Terramate Best Practices (environments) — https://terramate.io/rethinking-iac/terraform-and-opentofu-best-practices/ (2026-08-04).
- Gruntwork state topologies — https://www.gruntwork.io/blog/how-to-manage-large-opentofu-terraform-state-files (2026-08-04).
