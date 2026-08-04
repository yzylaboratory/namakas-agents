---
name: modelar-landing-zone-cloud
description: Modela landing zones multi-cuenta (OUs, identidad, logging, red hub, baselines). Úsala cuando se diseñe foundations cloud o account vending antes de workloads.
metadata:
  author: yzylabs
  version: "1.0"
---

# Modelar landing zone cloud

## Propósito

Definir un entorno multi-cuenta/suscripción listo para gobernanza: identidad, logging inmutable, guardrails y red — codificado en IaC.

## Entradas

- Cloud (AWS Control Tower/AFT/LZA, Azure landing zone, GCP foundations, …).
- Requisitos de compliance (CIS, Well-Architected, sectorial).
- Número estimado de cuentas/workloads.
- Restricciones de red y regiones.

## Procedimiento

1. Mapa de cuentas: management, security/audit, log-archive, shared-services, workloads.
2. Define OUs/folders y herencia de políticas.
3. Identidad federada / permission sets (sin usuarios long-lived en management).
4. Logging central (trail org, retención, cifrado, inmutabilidad).
5. Red hub-spoke o patrón equivalente; egress controlado.
6. Baselines por cuenta (Config/Security Hub equivalentes, regiones allow-list).
7. Account vending: AFT/GitOps u homólogo; inputs del request.
8. Lista qué queda fuera (workloads app) y handoffs a Bege/Paulie/Viola/Fujitora.
9. Entrega diagrama lógico + módulos/stacks foundations.

## Salida

```md
## Mapa de cuentas / OUs
## Identidad
## Logging y auditoría
## Red
## Baselines y regiones
## Account vending
## Módulos/stacks foundations
## Fuera de alcance / handoffs
```

## Casos límite

- Una sola cuenta “para todo” → documenta deuda y plan de split.
- Multi-cloud → foundations por cloud + capa de naming/tags común; no unificar providers a la fuerza.
- Herencia de cuentas legacy → plan de enrollment/drift, no big-bang sin evidencia.

## Validación

- Cuentas de seguridad/logging separadas de workloads.
- Guardrails de OU definidos.
- IaC foundations con state propio.
- Compliance citado con fuente (no inventado).

## Criterios de terminado

- Modelo implementable por fases.
- Riesgos de blast radius org-level listados.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | AWS greenfield 20 cuentas | OUs + log-archive + hub TGW + AFT sketch |
| Ambiguo | “Haz landing zone” | Preguntas cloud/compliance + plantilla mínima |
| Límite | Mezclar prod en management account | Rechazo + remediación de separación |

## Fuentes

- AWS Control Tower / landing zone docs — https://docs.aws.amazon.com/controltower/ (2026-08-04).
- AWS Well-Architected — https://docs.aws.amazon.com/wellarchitected/ (2026-08-04).
- CIS Benchmarks — https://www.cisecurity.org/cis-benchmarks (2026-08-04).
