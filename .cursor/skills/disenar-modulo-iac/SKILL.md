---
name: disenar-modulo-iac
description: Diseña módulos Terraform/OpenTofu con estructura estándar, inputs/outputs descritos y composición plana. Úsala cuando se pida crear o refactorizar un módulo reutilizable de infraestructura.
metadata:
  author: yzylabs
  version: "1.0"
---

# Diseñar módulo IaC

## Propósito

Producir un módulo reutilizable que eleve el nivel de abstracción (concepto de arquitectura), no un wrapper fino de un solo recurso.

## Entradas

- Concepto a encapsular (p. ej. VPC hub, bucket logging, EKS baseline).
- Cloud/provider y constraints de versión.
- Consumidores previstos y entornos.
- Requisitos de seguridad / tagging / naming.

## Procedimiento

1. Nombra el módulo por el concepto de arquitectura, no por el resource type.
2. Aplica estructura estándar: `main.tf` / `variables.tf` / `outputs.tf` + `README.md`.
3. Declara variables con `description`, tipos y defaults seguros; marca sensibles.
4. Declara outputs necesarios para composición; evita filtrar secretos.
5. Prefiere composición plana; nested modules solo bajo `modules/` con justificación.
6. Añade `examples/` mínimos si el módulo será publicado o reutilizado ampliamente.
7. Fija `required_version` y `required_providers` con constraints.
8. Lista checks: `fmt`, `validate`, tflint; tests `tofu test` cuando aporte valor.
9. Documenta no-objetivos (qué no crea el módulo) y supuestos.

## Salida

```md
## Nombre y propósito
## Estructura de archivos
## Variables / outputs
## Providers y versions
## Ejemplos
## No-objetivos
## Checks requeridos
```

## Casos límite

- Wrapper de un solo `aws_instance` → rechaza; usa el resource directo.
- Módulo “dios” multi-dominio → parte en stacks/módulos por blast radius.
- Breaking change de interface → versiona major y guía de migración.

## Validación

- Estructura estándar presente.
- Variables/outputs con description.
- Constraints de versión explícitos.
- No secretos en defaults ni outputs.

## Criterios de terminado

- Módulo implementable/consumible por otro root module.
- README con uso y no-objetivos.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Módulo VPC hub-spoke | Estructura estándar + vars/outputs + example |
| Ambiguo | “Hazme un módulo de AWS” | Preguntas de concepto + borrador de boundary |
| Límite | Pedido de wrapper `aws_s3_bucket` | Rechazo justificado + alternativa |

## Fuentes

- OpenTofu Creating Modules — https://opentofu.org/docs/language/modules/develop/ (2026-08-04).
- Terraform Standard Module Structure — https://developer.hashicorp.com/terraform/language/modules/develop/structure (2026-08-04).
