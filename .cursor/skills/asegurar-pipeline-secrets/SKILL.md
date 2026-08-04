---
name: asegurar-pipeline-secrets
description: Endurece secretos, permisos y supply-chain del pipeline (OIDC, least privilege, pin SHA, anti script-injection). Úsala cuando se audite o configure seguridad de CI/CD; no para IAM cloud de producto (Haredas) ni AppSec de aplicación completa.
metadata:
  author: yzylabs
  version: "1.0"
---

# Asegurar pipeline y secretos

## Propósito

Reducir el riesgo de exfiltración, privilege escalation y supply-chain attacks en workflows CI/CD.

## Entradas

- Workflows/pipelines actuales.
- Secretos y environments existentes (nombres).
- Proveedores cloud/SCM a autenticar.
- Requisitos de compliance (si hay).

## Procedimiento

1. Inventaría secretos: lifetime, alcance (repo/org/env), rotación.
2. Preferir OIDC/federación cloud; plan de migración desde keys estáticas.
3. Aplica least privilege a `GITHUB_TOKEN` / job tokens por job.
4. Protege environments de prod (reviewers, wait timer si aplica).
5. Pin acciones/orbs/imagenes a SHA/digest; evita tags móviles (`@v1`, `:latest`) en caminos críticos.
6. Revisa interpolación de `github.event` / inputs en shells (script injection).
7. Verifica masking, y que no se impriman secretos en logs/artefactos.
8. Entrega checklist de hallazgos (sev) + diffs de endurecimiento + plan de rotación si hubo exposición.

## Salida

- Diffs de permisos/OIDC/pinning.
- Matriz secreto → alcance → dueño → rotación.
- Hallazgos con severidad y remediación.
- Evidencia de validación (dry-run / review de logs de prueba sin secretos reales).

## Casos límite

- Action de terceros sin mantenimiento → reemplazo o fork pinneado; no “porque el marketplace”.
- Self-hosted runner compartido → aislar; documentar riesgo residual.
- Secreto ya en logs → rotar + borrar logs + reporte a Franky inmediato.

## Validación

- Ningún secreto en plaintext en repo.
- Permisos write justificados.
- Acciones críticas pineadas.
- OIDC o justificación de secreto estático restante.

## Criterios de terminado

- Hallazgos materiales remediados o aceptados explícitamente por Franky/Seguridad.
- Plan de rotación si aplica.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Workflow con `permissions: write-all` | Diff least privilege + justificación |
| Ambiguo | “Seguriza el CI” | Inventario + top 5 riesgos priorizados |
| Límite | AWS keys en secrets de repo | Migración OIDC + plan deprecación keys |

## Fuentes

- GitHub Docs — Security hardening for GitHub Actions — https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions (2026-08-04).
- GitHub Docs — Using secrets in GitHub Actions — https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions (2026-08-04).
- GitLab Docs — CI/CD secure files / job token — https://docs.gitlab.com/ee/ci/jobs/ci_job_token.html (2026-08-04).
- NIST SP 800-204C — https://csrc.nist.gov/publications/detail/sp/800-204c/final (2026-08-04).
