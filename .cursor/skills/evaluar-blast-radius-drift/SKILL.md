---
name: evaluar-blast-radius-drift
description: Evalúa blast radius y drift entre state y realidad antes de cambios IaC materiales. Úsala cuando un apply pueda afectar shared services, prod o múltiples cuentas, o cuando se sospeche divergencia.
metadata:
  author: yzylabs
  version: "1.0"
---

# Evaluar blast radius y drift

## Propósito

Cuantificar qué puede romperse y qué ya divergió, para decidir si el cambio es seguro, debe particionarse o debe abortarse.

## Entradas

- Stack(s) objetivo y dependencias (remote state / data sources).
- Último `plan` o capacidad de generarlo.
- Inventario de consumidores (apps, redes, identidades).
- Severidad del entorno (sandbox vs prod).

## Procedimiento

1. Delimita el state unit: recursos gestionados por el root/stack.
2. Identifica dependencias upstream/downstream (TGW, IAM, DNS, KMS).
3. Estima blast radius: cuentas, regiones, #recursos, downtime potencial.
4. Detecta drift: `plan` no vacío sin cambios de código; refresh; lectura cloud si está autorizada.
5. Clasifica hallazgos: safe-align / needs-import / needs-partition / stop-and-escalate.
6. Propón mitigaciones: split de state, feature flags, blue/green infra, ventana.
7. Define evidencia mínima para autorizar apply (revisores, checks, backup).
8. Escala a Viola si hay impacto de disponibilidad; Fujitora si hay superficie de seguridad.

## Salida

```md
## Unidad de state
## Dependencias
## Blast radius
## Drift detectado
## Clasificación y mitigaciones
## Go / no-go apply
## Escalaciones
```

## Casos límite

- State gigante (>miles de recursos) → prioriza split antes de cambios amplios.
- Drift por cambio manual en consola → no “arreglar” con apply masivo sin inventario.
- Destroy de recurso compartido → no-go hasta mapa de consumidores.

## Validación

- Blast radius expresado en unidades observables (cuentas/recursos/servicios).
- Drift con evidencia (plan/refresh), no opinión.
- Go/no-go explícito.

## Criterios de terminado

- Informe accionable para Franky/Paulie/aprobadores.
- Riesgos residuales listados.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Cambio SG en VPC shared | Radius + consumidores + go condicionado |
| Ambiguo | “¿Es seguro aplicar?” | Preguntas stack/plan + checklist mínima |
| Límite | Destroy KMS key org-wide | NO-GO + escalamiento inmediato |

## Fuentes

- OpenTofu state / plan semantics — https://opentofu.org/docs/language/state/ (2026-08-04).
- Gruntwork large state topologies — https://www.gruntwork.io/blog/how-to-manage-large-opentofu-terraform-state-files (2026-08-04).
