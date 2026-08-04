---
name: producir-brief-insights-mercado
description: Sintetiza sizing, STP, competencia y valor en un brief ejecutivo con handoffs a Morgans/Carrot/Bartolomeo. Úsala cuando se pida resumen de mercado, insight pack o decisión de go-to-market.
metadata:
  author: yzylabs
  version: "1.0"
---

# Producir brief de insights de mercado

## Propósito

Empaquetar la analítica de mercado en un brief corto y accionable: qué importa, por qué, qué decidir, qué falta — con handoffs claros al director y células hermanas.

## Entradas

- Artefactos previos (TAM/SAM/SOM, STP, mapa competitivo, VPC) o datos crudos.
- Pregunta de decisión (entrar, priorizar segmento, mensaje, pricing light).
- Restricciones de tiempo/audiencia del brief (exec vs squad).

## Procedimiento

1. Relee la pregunta de decisión; descarta ruido que no la responde.
2. Extrae 3–5 insights materiales (cada uno: hecho → implicación).
3. Resume oportunidad (sizing) y foco (targets) en ≤10 líneas.
4. Resume posición competitiva y claim recomendado.
5. Lista decisiones requeridas para Morgans.
6. Define handoffs:
   - Carrot: hipótesis de adopción / señales a medir.
   - Bartolomeo: comunidades/audiencias a evangelizar.
7. Adjunta riesgos, supuestos críticos y fuentes clave.
8. Marca STATUS sugerido (`COMPLETED` vs `COMPLETED_WITH_LIMITATIONS`).

## Salida

```md
## Pregunta de decisión
## Insights (3–5)
## Oportunidad (sizing flash)
## Foco (targets)
## Posicionamiento recomendado
## Decisiones para Morgans
## Handoff → Carrot
## Handoff → Bartolomeo
## Riesgos / supuestos
## Fuentes
## Pendientes
```

## Casos límite

- Analítica incompleta → brief parcial + bloqueos explícitos; no rellenes con narrativa.
- Insights contradictorios → presenta tensión y opción A/B; no promedies.
- Pedido de “campaña completa” → brief de insights + `DELEGATION_REQUIRED` a Morgans/Bartolomeo.

## Validación

- Cada insight tiene implicación de decisión.
- Handoffs tienen dueño y próximo paso.
- No sustituye el artefacto detallado cuando se pidió profundidad.

## Criterios de terminado

- Morgans puede priorizar o pedir corrección sin releer todos los anexos.
- Evidencia mínima (fuentes/supuestos) está en el brief.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Pack sizing+STP+mapa | Brief 1–2 páginas con handoffs |
| Ambiguo | “Resume el mercado” | Pregunta de decisión + brief tentativo |
| Límite | Solo rumores internos | Insights etiquetados low-confidence + gaps |

## Fuentes

- Smart Insights — STP as input to communications plans — https://www.smartinsights.com/digital-marketing-strategy/customer-segmentation-targeting/segmentation-targeting-and-positioning/ (2026-08-04).
- Strategyzer — testing value propositions (fit stages) — https://www.strategyzer.com/value-proposition (2026-08-04).
- CFI / Salesforce — sizing vocabulary for exec briefs — https://corporatefinanceinstitute.com/resources/management/total-addressable-market-tam/ (2026-08-04).
