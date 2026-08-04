---
name: disenar-tablero-senales-doradas
description: Diseña tableros de latency, traffic, errors y saturation (golden signals) alineados a SLI y triage on-call. Úsala cuando se pida dashboard SRE, señales doradas, RED/USE, panel de servicio o vista de incidente.
metadata:
  author: yzylabs
  version: "1.0"
---

# Diseñar tablero de señales doradas

## Propósito

Dar al on-call una vista de servicio que muestre si el sistema está en problema y dónde mirar primero, separando paneles de alerta de paneles de debugging.

## Entradas

- Servicio / dependencias críticas.
- SLIs/SLOs existentes.
- Señales disponibles (métricas/traces).
- Herramienta de dashboards (Grafana, etc.).
- Playbook de triage actual (si existe).

## Procedimiento

1. Fija audiencia: on-call primeros 5–10 minutos del incidente.
2. Coloca las cuatro golden signals: latency, traffic, errors, saturation.
3. Desglosa latency de éxitos vs errores; no mezcles sin etiquetar.
4. Define traffic en unidad del dominio (RPS, sesiones, txs).
5. Define errors (explícitos, implícitos, por política de latencia si aplica).
6. Elige saturation del recurso más constraining (CPU, memoria, IO, cola, pool).
7. Añade fila de SLI/SLO/error budget remaining como contexto de decisión.
8. Separa sección debugging (dependencias, top rutas, exemplars/traces) de alerting.
9. Documenta “cómo usar este tablero” en 5 pasos.
10. Lista paneles nice-to-have fuera del MVP para no saturar.

## Salida

```md
## Audiencia y objetivo
## Layout (filas/paneles)
## Golden signals (definición + query/pseudoconsulta)
## SLO / budget strip
## Debugging (secundario)
## Guía de triage (5 pasos)
## Gaps de datos
```

## Casos límite

- Microservicio sin saturation clara → usa cola/pool/thread saturation proxy.
- Muchos endpoints → agrega por critical user journeys, no por cada path.
- Solo infra metrics → marca gap de user-centric SLI; no finjas golden signals de app.

## Validación

- Las cuatro señales están presentes o justificadas como N/A.
- Hay strip de SLO/budget si el SLO existe.
- Guía de triage es ejecutable sin conocimiento tribal.

## Criterios de terminado

- Spec de tablero implementable.
- Gaps de métricas con dueño.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | API gateway + SLO 99.9% | 4 señales + budget + deps |
| Ambiguo | “Haz un dashboard bonito” | Rechaza vanity; pide journey y propone MVP golden |
| Límite | Storage/KV | Traffic=ops, saturation=disk/IO, errors=failed ops |

## Fuentes

- Google SRE Book — Monitoring Distributed Systems (Four Golden Signals) — https://sre.google/sre-book/monitoring-distributed-systems/ (consultado 2026-08-04).
- Google SRE Workbook — Monitoring — https://sre.google/workbook/monitoring/ (consultado 2026-08-04).
