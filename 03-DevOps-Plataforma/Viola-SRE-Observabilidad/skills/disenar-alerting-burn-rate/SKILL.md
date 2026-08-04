---
name: disenar-alerting-burn-rate
description: Diseña alertas multi-ventana y multi-burn-rate ancladas al error budget (page vs ticket). Úsala cuando se pida alerting SRE, burn rate, alertas de SLO, PagerDuty/Alertmanager o reducir ruido de pages.
metadata:
  author: yzylabs
  version: "1.0"
---

# Diseñar alerting burn-rate

## Propósito

Convertir SLOs en alertas de eventos significativos: detectar quemado rápido y lento del error budget con buena precisión y tiempo de detección, sin pages por blips.

## Entradas

- SLO (target, ventana) y definición del SLI.
- Stack de alerting (Prometheus/Alertmanager, cloud monitoring, etc.).
- Capacidad on-call y canales (page vs ticket).
- Runbooks existentes o gap.

## Procedimiento

1. Confirma SLI como ratio y error budget rate = 1 − SLO.
2. Diseña tiers multi-ventana / multi-burn-rate (Workbook): típico para 99.9% — page 14.4× (1h∧5m), page/warn 6× (6h∧30m), ticket 1× (3d∧6h); ajusta si el SLO difiere.
3. Exige condición AND de ventana larga + corta para cada tier.
4. Asigna severidad: page solo a quemados que amenazan budget materialmente; ticket a drift lento.
5. Define `for` / duración mínima para reducir flapping; no bajes umbrales antes de tunear `for`.
6. Adjunta runbook: señales a mirar, mitigaciones seguras, escalamiento.
7. Especifica labels (service, slo, severity, burn_tier) y routing.
8. Documenta cómo validar (simulación de burn, recording rules).
9. Lista anti-patrones rechazados (alertar si error_rate > SLO crudo sin burn).

## Salida

```md
## SLO de referencia
## Tabla tiers (severity · ventanas · burn · % budget · severidad)
## Expresiones / pseudocódigo
## Routing y labels
## Runbook mínimo por alerta page
## Validación propuesta
## Anti-patrones evitados
```

## Casos límite

- Tráfico muy bajo → ventanas cortas ruidosas; alarga ventanas o usa ticket-first.
- Múltiples SLIs → una familia de alertas por SLI; evita “mega-alerta”.
- Solo hay umbral legacy → plan de migración; no declares burn-rate si no hay ratio SLI.

## Validación

- Cada page tiene AND multi-ventana y runbook.
- Ticket tier cubre slow burn.
- Severidades mapean a canales reales.

## Criterios de terminado

- Spec implementable en el stack del equipo.
- Riesgos de ruido y gaps de datos listados.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | SLO 99.9% HTTP | 3 tiers Workbook + runbooks page |
| Ambiguo | “Alerta si hay errores” | Rechaza umbral crudo; pide SLI/SLO o propone draft |
| Límite | 10 RPS servicio | Ventanas adaptadas + advertencia de estadística |

## Fuentes

- Google SRE Workbook — Alerting on SLOs — https://sre.google/workbook/alerting-on-slos/ (consultado 2026-08-04).
- Google SRE Workbook — Implementing SLOs — https://sre.google/workbook/implementing-slos/ (consultado 2026-08-04).
