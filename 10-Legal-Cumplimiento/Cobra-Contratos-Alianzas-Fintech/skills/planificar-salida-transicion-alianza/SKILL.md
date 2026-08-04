---
name: planificar-salida-transicion-alianza
description: Diseña cláusulas de terminación, transition assistance, devolución de datos y anti lock-in para alianzas fintech/plataforma. Úsala cuando la dependencia operativa sea alta o el contrato carezca de exit plan usable.
metadata:
  author: yzylabs
  version: "1.0"
---

# Planificar salida y transición de alianza

## Propósito

Asegurar que la alianza pueda terminar sin colapsar el servicio al cliente: transition services, migración de datos, continuidad, escrow cuando aplique y disengagement ordenado.

## Entradas

- Cláusulas de term/termination existentes.
- Mapa de dependencia (API crítica, marca, base de clientes, datos).
- SLAs y obligaciones customer-facing.
- Restricciones regulatorias conocidas de continuidad.

## Procedimiento

1. Clasifica triggers: convenience, cause, regulatory change, insolvency, repeated SLA breach.
2. Define notice periods y wind-down windows realistas.
3. Especifica Transition Assistance: duración, scope (acceso, knowledge transfer, migración), fees.
4. Define Data Return/Migration: formato estándar, integridad, certificación de borrado.
5. Si hay lock-in de plataforma, evalúa escrow de componentes críticos o acceso de continuidad.
6. Cubre disengagement customer-facing (mensajes, redirect, brand) cuando el partner es interfaz al cliente.
7. Alinea survival clauses (confidentiality, liability, data) post-terminación.
8. Lista costos de salida y quién los asume; marca gaps.

## Salida

```md
## Triggers y notice
## Transition Assistance
## Data return / deletion
## Continuidad / escrow (si aplica)
## Disengagement customer-facing
## Survival
## Costos y gaps
## Posición negociadora
```

## Casos límite

- Terminación inmediata sin transición en servicio crítico → red flag; exige wind-down mínimo.
- Partner retiene datos “para compliance” sin límite → exige scope, plazo y auditoría.
- Insolvencia del partner → prioriza escrow / step-in rights vía Sengoku.

## Validación

- Hay transition usable, no solo “reasonable efforts”.
- Formato de datos y plazos están definidos o listados como gap.
- Customer-facing disengagement cubierto si aplica.

## Criterios de terminado

- Sengoku puede aceptar/rechazar el exit plan con evidencia.
- Lock-in residual está cuantificado cualitativamente (alto/medio/bajo) con mitigación.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | BaaS con API crítica | Transition 90 días + data return + survival |
| Ambiguo | “Exit estándar” | Plantilla + preguntas de dependencia |
| Límite | Terminación for convenience 5 días en plataforma customer-facing | Red flag + wind-down mínimo obligatorio |

## Fuentes

- Mayer Brown — Collaboration Agreements… (post-termination planning / anti lock-in) (2025-11-21) (2026-08-04).
- ABA — SaaS Agreements… (termination, transition rights, data return) (2021-11) (2026-08-04).
