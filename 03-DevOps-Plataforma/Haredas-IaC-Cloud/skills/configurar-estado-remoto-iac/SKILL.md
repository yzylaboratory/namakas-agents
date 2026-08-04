---
name: configurar-estado-remoto-iac
description: Define backends remotos, locking, cifrado y keys de state por stack/entorno. Úsala cuando se configure o migre el state de Terraform/OpenTofu fuera del disco local.
metadata:
  author: yzylabs
  version: "1.0"
---

# Configurar estado remoto IaC

## Propósito

Establecer una fuente de verdad compartida del state con locking y acceso least-privilege, evitando corrupción por applies concurrentes.

## Entradas

- Tooling (OpenTofu/Terraform) y versión.
- Cloud del backend (S3, GCS, Azure Blob, Consul, TACOS, …).
- Inventario de stacks y entornos.
- Requisitos de cifrado, retención y auditoría.

## Procedimiento

1. Declara backend en el bloque settings; valores resolubles en `init` (sin interpolaciones de state).
2. Exige locking nativo o complemento (p. ej. DynamoDB con S3, locks GCS).
3. Diseña convención de keys: `<org>/<stack>/<env>/terraform.tfstate` (o equivalente).
4. Separa keys prod vs non-prod; documenta prohibición de cruce.
5. Define IAM/roles de acceso al backend (plan vs apply vs break-glass).
6. Activa cifrado en reposo y política de no versionar state en git.
7. Si migras: backup → `init -migrate-state` → verificar → retirar state local.
8. Entrega checklist de rotación de credenciales de backend.

## Salida

```md
## Backend elegido
## Locking
## Convención de keys
## Acceso / IAM
## Cifrado y backup
## Procedimiento de migración
## Prohibiciones
```

## Casos límite

- Solo local state en equipo → bloquea promoción a shared/prod.
- State monolítico gigante → propone split de stacks (ver blast radius).
- Credenciales en HCL → rechaza; usa env/OIDC/CI roles.

## Validación

- Locking documentado y viable.
- Keys por entorno separadas.
- Sin state ni secrets en VCS.
- Procedimiento de migrate con backup.

## Criterios de terminado

- Spec de backend implementable por plataforma/CI.
- Riesgos de corrupción/concurrencia listados.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | 3 stacks AWS (net/iam/app) × 3 envs | Backend S3+lock + keys separadas |
| Ambiguo | “Pon remote state” | Preguntas cloud/locking + plantilla mínima |
| Límite | Migrar prod con apply en curso | STOP + ventana + backup obligatorio |

## Fuentes

- OpenTofu Remote State — https://opentofu.org/docs/language/state/remote/ (2026-08-04).
- OpenTofu Backend Configuration — https://opentofu.org/docs/language/settings/backends/configuration/ (2026-08-04).
- Terramate Terraform/OpenTofu Best Practices — https://terramate.io/rethinking-iac/terraform-and-opentofu-best-practices/ (2026-08-04).
