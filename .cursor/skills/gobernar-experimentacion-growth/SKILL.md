---
name: gobernar-experimentacion-growth
description: Gobierna el ciclo de experimentación de growth (hipótesis, métrica primaria, guardrails, decisión ship/iterate/kill y registro de aprendizajes). Úsala cuando se pida A/B test, experimento de canal/onboarding, o política de experimentación del departamento.
metadata:
  author: yzylabs
  version: "1.0"
---

# Gobernar experimentación de growth

## Propósito

Asegurar que los experimentos de marketing/growth produzcan decisiones confiables, no “tests” eternos ni ship por anécdota.

## Entradas

- Hipótesis o iniciativa a probar.
- Métrica primaria alineada a un input/NSM y guardrails.
- Tráfico/volumen estimado y restricciones de marca/compliance.
- Capacidad de implementación (producto, creatividades, tracking).

## Procedimiento

1. Escribe hipótesis en formato: **si** [cambio] **para** [segmento] **entonces** [métrica] **porque** [mecanismo].
2. Fija métrica primaria (una), secundarias y guardrails (calidad, churn, quejas, margen).
3. Define diseño: A/B, staged rollout, geo-split, o pre/post solo si no hay alternativa — declara sesgos.
4. Estima duración/muestra mínima; si el volumen no alcanza potencia, reduce scope o usa decisión bayesiana/secuencial explícita — no finjas significancia.
5. Criterios de decisión a priori: ship / iterate / kill / scale.
6. Ejecuta checklist pre-launch: tracking, consentimiento, brand, overlap con otros tests.
7. Cierra con resultado, aprendizaje y siguiente apuesta; archiva en registro departamental (Brook si es decisión material).

## Salida

```md
## Experimento
- ID / nombre:
- Hipótesis:
- Segmento:
## Diseño
- Tipo:
- Métrica primaria:
- Guardrails:
- Duración / muestra:
## Decisión a priori
## Resultado
- Decisión: ship | iterate | kill | scale
- Evidencia:
- Aprendizaje:
## Siguiente paso
```

## Casos límite

- Stakeholder quiere ship sin datos: exige criterio a priori o marca como lanzamiento de riesgo aceptado (no “experimento”).
- Múltiples tests en el mismo funnel: serializa o asigna traffic split con owner único.
- Regulación/claims: bloquea hasta Legal.

## Validación

- Hay una sola métrica primaria.
- Guardrails definidos.
- Criterios de decisión escritos antes del resultado.
- Aprendizaje documentado al cierre.

## Criterios de terminado

- Experimento gobernado de punta a punta o bloqueado con razón.
- Decisión trazable y reutilizable.
- Sin contaminación no documentada con otros tests.

## Fuentes

- Experimentación en producto/growth (hipótesis, guardrails, decision quality) — síntesis contrastada 2026-08-04
- North Star inputs como ancla de métrica primaria — Amplitude, 2026-08-04
- ICE para priorizar cola de experimentos (Impact/Confidence/Ease) — práctica común, secundaria 2026-08-04
