---
name: modelar-forecast-gasto-tecnologia
description: Construye un forecast de gasto de infraestructura con supuestos, escenarios y sensibilidad. Úsala cuando se pida proyectar costos cloud/SaaS/plataforma o comparar forecast vs presupuesto — no para revenue de APIs.
metadata:
  author: yzylabs
  version: "1.0"
---

# Modelar forecast de gasto de tecnología

## Propósito

Proyectar el gasto futuro de infraestructura de forma reproducible, con escenarios y drivers explícitos, para decisiones de funding y commits.

## Entradas

- Histórico de consumo/costo (idealmente normalizado, p. ej. FOCUS).
- Presupuesto vigente (si existe).
- Roadmap (nuevos servicios, migraciones, AI/ML, seasonality).
- Commits actuales y fechas de renewal.
- Cambios de precio o de arquitectura conocidos.

## Procedimiento

1. Fija horizonte y cadencia de actualización del forecast.
2. Elige método (run-rate, driver-based, bottom-up por servicio) y documenta por qué.
3. Identifica drivers (compute hours, storage GB, transfer, seats SaaS, etc.).
4. Construye escenarios bajo / base / alto con supuestos por escenario.
5. Incorpora commits solo sobre baseline estable rightsized (o marca riesgo si no lo está).
6. Calcula accuracy previa (MAPE u otra métrica) si hay histórico de forecasts.
7. Destaca puntos de inflexión (go-live, decommission, renewals).
8. Entrega tabla forecast vs presupuesto y lista de sensibilidades top.

## Salida

```md
## Horizonte y método
## Drivers
## Escenarios (bajo/base/alto)
## Forecast vs presupuesto
## Commits / lock-in
## Sensibilidad
## Accuracy histórica (si aplica)
## Riesgos / pendientes
```

## Casos límite

- Series cortas o ruidosas → rangos amplios + plan de mejorar datos.
- Migración big-bang → forecast por fases (antes/durante/después) no un solo run-rate.
- Precio vendor desconocido → marca supuesto y no inventes list price.

## Validación

- Cada escenario tiene supuestos numerados.
- No se presenta un solo número como certeza.
- Commits no se asumen sin baseline.
- Fuentes de datos citadas.

## Criterios de terminado

- Un decisor ve el rango y los 3 drivers que más mueven el gasto.
- Acciones de mejora de forecast tienen dueño.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | 6 meses FOCUS + roadmap Q+1 | Forecast base/alto/bajo + vs budget |
| Ambiguo | “¿Cuánto gastaremos el año que viene?” | Horizonte propuesto + drivers + datos faltantes |
| Límite | Commit SP al 80% sin rightsizing | Forecast con riesgo de overcommit explícito |

## Fuentes

- FinOps Framework — Forecasting capability — https://www.finops.org/framework/capabilities/forecasting/ (consultado 2026-08-04).
- FOCUS™ — https://focus.finops.org/ (FOCUS 1.4 anunciado; consultar spec vigente).
