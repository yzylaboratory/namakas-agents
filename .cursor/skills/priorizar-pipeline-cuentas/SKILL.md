---
name: priorizar-pipeline-cuentas
description: Prioriza pipeline, cuentas enterprise y partners con valor, fit de ICP, riesgo y capacidad. Úsala cuando haya que ordenar backlog comercial, elegir cuentas foco o recortar forecast inflado.
metadata:
  author: yzylabs
  version: "1.0"
---

# Priorizar pipeline y cuentas

## Propósito

Convertir un backlog ruidoso de oportunidades/cuentas/partners en una lista priorizada con dueños, gates y justificación defendible.

## Entradas

- Lista de oportunidades, cuentas o partners candidatos.
- Objetivo de revenue y capacidad del squad.
- Señales de ICP fit, stage, amount, close date, partner touch.
- Bloqueos conocidos (legal, producto, pricing).

## Procedimiento

1. Normaliza el inventario (cuenta/oportunidad/partner, stage, $ , dueño, motion).
2. Puntúa cada ítem:
   - Valor (impacto en revenue / strategic fit).
   - Probabilidad (calidad MEDDPICC / historial).
   - Urgencia (plazo, ventana competitiva).
   - Esfuerzo / dependencia (legal, producto, enablement).
   - Riesgo (conflicto de canal, overpromise, concentración).
3. Clasifica Now / Next / Later / Kill (o nurture).
4. Asigna dueño: Crocodile (enterprise), Bon Clay (partner health/activation), Mr. 3 (si el bloqueo es enablement), Buggy (prioridad departamental).
5. Define el gate de salida de cada Now (evidencia mínima para avanzar stage).
6. Produce forecast view: commit / best case / pipeline — sin inflar commit sin Economic Buyer + Paper Process.

## Salida

```md
## Objetivo de priorización
## Método de scoring
## Backlog priorizado
| Ítem | Motion | Score | Now/Next/Later/Kill | Dueño | Gate | Riesgo |
## Forecast view
| Bucket | $ | Confianza | Huecos MEDDPICC |
## Decisiones y kills
## Escalaciones
```

## Casos límite

- Sandbagging vs sandcastle: si falta Champion/EB, no está en commit.
- Partner sin time-to-first-deal path: Later o Kill hasta enablement/onboarding.
- Empate de score: prioriza ICP fit y capacidad de delivery sobre logo size.

## Validación

- Cada Now tiene dueño y gate.
- Commit no incluye deals sin evidencia material de calificación.
- No hay dos dueños writing la misma oportunidad sin deal registration.

## Criterios de terminado

- Lista priorizada actionable en el horizonte pedido.
- Forecast buckets explícitos.
- Kills/nurture documentados.

## Fuentes

- MEDDPICC® qualification — https://meddpicc.net/understanding-the-meddpicc-sales-framework/ (2026-08-04)
- The Point Company — co-sell pipeline reviews / time-to-first-deal — https://thepointco.com/channel-partner-pipeline-generation-how-to-build-a-co-sell-motion-that-generates-revenue/ (2026-08-04)
