---
name: definir-north-star-y-metricas
description: Define o valida North Star Metric, input metrics y guardrails con definiciones operativas y anti-gaming. Úsala cuando se pida sistema de métricas de growth, NSM, árbol de inputs o alinear al departamento a un outcome de valor.
metadata:
  author: yzylabs
  version: "1.0"
---

# Definir North Star y métricas

## Propósito

Establecer un sistema de métricas operable (NSM + inputs + guardrails) que alinee Marketing/Growth con valor al cliente y predicción de crecimiento sostenible.

## Entradas

- Visión de producto / job-to-be-done y modelo de negocio.
- Datos o hipótesis de comportamiento (eventos disponibles).
- “Juego” predominante si se conoce (attention / transaction / productivity — Amplitude).
- Stakeholders y equipos que deben poseer inputs.

## Procedimiento

1. Nombra el momento de valor del cliente (qué “trabajo” completa el producto).
2. Lista 3–5 candidatos de NSM cerca de ese momento (acción × entidad × cadencia).
3. Aplica filtros: refleja valor, es leading vs revenue, influenciable, simple, resistente a gaming.
4. Elige un NSM provisional + fecha de revisit; valida correlación con retención/revenue si hay datos (si no, marca hipótesis).
5. Descompón en 3–5 **inputs** (breadth, depth, frequency, efficiency) con dueño (Carrot/Shakky/Bartolomeo/otros).
6. Define **guardrails** (churn, calidad, margen, confianza/compliance, error rate de tracking).
7. Escribe definiciones operativas versionadas (evento, filtros, ventana, entidad).

## Salida

```md
## North Star
- Métrica:
- Definición operativa:
- Por qué refleja valor:
- Revisit:
## Inputs
| Input | Definición | Dueño | Cómo mueve el NSM |
## Guardrails
| Guardrail | Umbral | Acción si se rompe |
## Anti-patterns rechazados
## Supuestos / datos faltantes
```

## Casos límite

- Solo vanity disponible: declara gap de instrumentación; no eleves vanity a NSM.
- Multi-producto: un NSM por producto o NSM de plataforma explícito; no mezclar.
- Conflicto ventas vs PLG: documenta dual metrics con primary/secondary; escala a Luffy.

## Validación

- NSM no es revenue crudo sin justificación.
- Cada input tiene dueño y definición.
- Hay al menos un guardrail de calidad/confianza.
- Segmentación/cohortes mencionadas cuando el promedio engaña.

## Criterios de terminado

- Sistema usable en weekly review y priorización.
- Definiciones suficientemente precisas para Shakky/analítica.
- Listo para enlazar backlog a inputs.

## Fuentes

- Amplitude North Star Playbook — https://amplitude.com/books/north-star/amplitudes-north-star-metric-and-inputs (2026-08-04)
- Amplitude — Product North Star Metric (Attention/Transaction/Productivity games) — https://amplitude.com/blog/product-north-star-metric (2026-08-04)
