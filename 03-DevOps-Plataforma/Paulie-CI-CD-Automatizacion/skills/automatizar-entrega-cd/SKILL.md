---
name: automatizar-entrega-cd
description: Diseña etapas de continuous delivery/deployment (promoción de artefactos, entornos, approvals, rollback). Úsala cuando se pida automatizar despliegue o release entre entornos; no para sync GitOps de Bege ni para diseñar IaC de Haredas.
metadata:
  author: yzylabs
  version: "1.0"
---

# Automatizar entrega CD

## Propósito

Promover el mismo artefacto validado a través de entornos con gates explícitos, trazabilidad y procedimiento de rollback.

## Entradas

- Artefacto de CI (imagen, paquete, bundle) y su identificador inmutable.
- Entornos destino y dueños.
- Continuous delivery (approval a prod) vs continuous deployment (auto).
- Restricciones de compliance / change management.
- Si el deploy real es GitOps, nota de handoff a Bege.

## Procedimiento

1. Fija el artefacto canónico (digest/tag inmutable); prohíbe rebuild por entorno.
2. Modela etapas: deploy-dev → smoke → deploy-staging → approve → deploy-prod (ajusta).
3. Declara environments protegidos y reviewers cuando haga falta.
4. Elige estrategia de release (rolling, blue/green, canary) solo a nivel de pipeline; detalle de mesh/GitOps → Bege si aplica.
5. Documenta rollback: qué comando/artefacto previo, quién autoriza, RTO objetivo.
6. Separa “desplegar” de “activar feature” (flags) si el equipo lo usa.
7. Si el destino es cluster GitOps, entrega pipeline hasta publish/update de manifiesto y `DELEGATION_REQUIRED` a Bege para sync.
8. Entrega YAML CD + matriz entornos + rollback + riesgos.

## Salida

- Pipeline/stages de CD.
- Matriz entorno → gate → artefacto.
- Procedimiento de rollback.
- Handoff GitOps/IaC si aplica.

## Casos límite

- Pedido de continuous deployment sin tests/monitoreo → recomienda delivery + lista de gaps; no apruebes CD auto.
- Hotfix → pipeline acotado con mismos gates de seguridad mínimos.
- Solo “deploy script” legacy → propone encapsularlo como job versionado; no UI-only.

## Validación

- Build once / promote many respetado.
- Delivery vs deployment etiquetado.
- Prod tiene protección o justificación escrita.
- Rollback documentado.

## Criterios de terminado

- Un operador sabe cómo promover y revertir con evidencia.
- Frontera con Bege/Haredas explícita.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Imagen OCI + 3 entornos | Stages promote + approval prod + rollback |
| Ambiguo | “Auto-deploy a prod” | Delivery con gaps o CD solo si hay evidencia de madurez |
| Límite | Deploy vía Argo CD | Pipeline publica manifiesto; handoff a Bege |

## Fuentes

- DORA — Deployment frequency / lead time — https://dora.dev/ (2026-08-04).
- GitHub Docs — Deployments and environments — https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment (2026-08-04).
- GitLab Docs — Environments and deployments — https://docs.gitlab.com/ee/ci/environments/ (2026-08-04).
