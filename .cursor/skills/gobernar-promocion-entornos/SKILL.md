---
name: gobernar-promocion-entornos
description: Diseña promoción GitOps entre entornos (PR/MR, gates, rollback vía Git, progressive delivery). Úsala cuando se pida el camino dev→staging→prod o políticas de release declarativas.
metadata:
  author: yzylabs
  version: "1.0"
---

# Gobernar promoción entre entornos

## Propósito

Definir cómo un cambio de desired state avanza entre entornos con auditoría, aprobación y rollback por Git — separando el artefacto de CI (Paulie) de la declaración desplegada (Capone).

## Entradas

- Entornos y su criticidad.
- Artefacto inmutable producido por CI (digest/chart version).
- Requisitos de aprobación (CODEOWNERS, change advisory).
- Progressive delivery (canary/blue-green) si aplica.
- Restricciones regulatorias o ventanas de cambio.

## Procedimiento

1. Dibuja el camino de promoción y qué archivo/overlay cambia en cada paso.
2. Fija que CI publica el artefacto; GitOps solo actualiza la referencia en el overlay destino.
3. Define gates: tests, sync healthy en env previo, aprobaciones humanas.
4. Especifica mecanismo: PR entre branches/dirs, image updater controlado, o promotion bot con evidencia.
5. Documenta rollback: revert commit / PR; prohíbe kubectl como proceso normal.
6. Si hay canary: integra Argo Rollouts o Flagger como extensión del desired state.
7. Define SLAs de promoción (tiempo máximo en staging, freeze windows).
8. Lista métricas de release para Viola (éxito sync, rollback rate).

## Salida

```md
## Camino de promoción
## Artefacto CI vs declaración GitOps
## Gates y aprobaciones
## Mecanismo (PR/dirs/bot)
## Rollback
## Progressive delivery (si aplica)
## Freeze / ventanas
## Métricas / handoff Viola
```

## Casos límite

- Hotfix prod → procedimiento de emergencia con post-facto PR; no normalizar bypass.
- Mismos manifests en todos los envs → overlays mínimos obligatorios (al menos config/URL).
- Promotion bot sin audit trail → rechazar; exige commit atribuible.

## Validación

- Cada promoción deja historial en el state store.
- Rollback no depende de “recordar el YAML anterior” fuera de Git.
- Frontera Paulie (build) vs Capone (declare) está escrita.
- Prod no auto-promueve sin gate documentado.

## Criterios de terminado

- Un release manager sabe qué PR abrir y qué verificar antes de merge a prod.
- Viola puede enganchar señales de sync/rollback.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | digest sha256… listo en staging | PR a prod overlay + checklist gates |
| Ambiguo | “Promueve a prod” | Preguntar evidencia staging healthy + owners |
| Límite | Pedido de kubectl set image en prod | Rechazo; promoción por Git o emergencia escalada |

## Fuentes

- OpenGitOps Principles v1.0.0 — https://opengitops.dev/ (2026-08-04).
- CNCF GitOps in 2025 (PR/MR + reconciliation; Rollouts/Flagger) — https://www.cncf.io/blog/2025/06/09/gitops-in-2025-from-old-school-updates-to-the-modern-way/ (2025-06-09).
