---
name: auditar-higiene-alertas
description: Audita ruido, falsos positivos, pages por turno y alertas sin dueño/runbook; propone retuning o deprecación. Úsala cuando el on-call esté saturado, haya alert fatigue, o se pida scorecard de calidad de alertas.
metadata:
  author: yzylabs
  version: "1.0"
---

# Auditar higiene de alertas

## Propósito

Medir y mejorar la calidad del alerting para que el on-call responda a eventos significativos, no a ruido — alineado a carga sostenible y a defensa del SLO.

## Entradas

- Inventario de alertas (nombre, severidad, servicio).
- Histórico de fires / acks / resolves (si existe).
- Páginas por turno / semana.
- SLO y política de budget (si existen).
- Runbooks asociados.

## Procedimiento

1. Inventaría alertas page vs ticket vs info.
2. Clasifica cada alerta page: ¿defiende SLO/budget? ¿tiene runbook? ¿tiene dueño?
3. Cuantifica ruido: % resolved without action, flapping, duplicados.
4. Compara volumen de pages con señal SRE (~≤2 eventos materiales / turno 12h como heurística de diseño).
5. Marca anti-patrones: umbral crudo sin burn, alertas de disco en app tier sin user impact, pages por warning logs.
6. Propón acciones: retune (ventanas/`for`), degradar severidad, merge, deprecate, añadir runbook.
7. Prioriza por (ruido × severidad × falta de dueño).
8. Entrega scorecard + backlog de higiene con owners.
9. Define métricas de seguimiento (FP rate, MTTA, pages/turno).

## Salida

```md
## Alcance auditado
## Scorecard (totales · page · con runbook · sin dueño · sospechosas)
## Hallazgos top N
## Recomendaciones (retune / degrade / deprecate)
## Backlog priorizado
## KPIs de seguimiento
## Riesgos (ciegos al bajar severidad)
```

## Casos límite

- Sin histórico → auditoría estática por diseño + plan de telemetría de alertas.
- Alertas de seguridad/compliance → no deprecar sin Fujitora/seguridad.
- Servicio sin SLO → recomienda definir SLI/SLO antes de “optimizar” pages.

## Validación

- Cada recomendación cita evidencia (diseño o dato).
- No se eliminan pages de budget defense sin reemplazo.
- Owners asignados o escalados a Franky.

## Criterios de terminado

- Scorecard actionable.
- Backlog priorizado con dueños.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | 40 pages/semana, 70% auto-resolve | Top noise + plan degrade/retune |
| Ambiguo | “Las alertas molestan” | Inventario mínimo + preguntas de severidad/histórico |
| Límite | Unica page es burn-rate SLO | Conservar; auditar ticket tier y dashboards |

## Fuentes

- Google SRE Book — Service Best Practices (on-call load) — https://sre.google/sre-book/service-best-practices/ (consultado 2026-08-04).
- Google SRE Workbook — Alerting on SLOs — https://sre.google/workbook/alerting-on-slos/ (consultado 2026-08-04).
- Google SRE Workbook — Monitoring (alerting vs debugging metrics) — https://sre.google/workbook/monitoring/ (consultado 2026-08-04).
