---
name: definir-sli-slo-error-budget
description: Define SLIs orientados a usuario, SLOs con ventana/target y error budget con política escrita. Úsala cuando se pida fiabilidad, SLO, error budget, availability target o política de freeze por budget.
metadata:
  author: yzylabs
  version: "1.0"
---

# Definir SLI, SLO y error budget

## Propósito

Convertir la fiabilidad deseada en indicadores medibles, objetivos acordados y un presupuesto de fallo que gobierne trade-offs entre features y estabilidad.

## Entradas

- Servicio / journey de usuario y criticidad.
- Tipo de sistema (request/response, pipeline, batch, storage).
- Tráfico o proxies de volumen (si existen).
- Stakeholders de producto/plataforma.
- Restricciones de ventana (rolling 28d vs calendario).

## Procedimiento

1. Identifica el journey crítico y qué “éxito” significa para el usuario.
2. Propón SLIs como ratio good events / total events (0–100%).
3. Clasifica candidatos (availability, latency threshold, correctness) y elige 1–3 SLIs materiales.
4. Define SLO: target % + ventana + exclusión explícita (mantenimientos, dependencias si aplica).
5. Calcula error budget = 1 − SLO; ejemplifica con volumen estimado (errores permitidos).
6. Redacta política de error budget: acciones al agotar (halt features no-P0/security, foco reliability), owners y excepciones.
7. Distingue SLO interno vs SLA comercial; no inventes lenguaje contractual.
8. Lista instrumentación mínima para medir el SLI y gaps de datos.
9. Entrega catálogo SLI/SLO + política + riesgos + dueños.

## Salida

```md
## Servicio / journey
## SLIs (fórmula good/total)
## SLO (target, ventana, exclusiones)
## Error budget (fórmula + ejemplo numérico)
## Política de error budget
## Instrumentación requerida
## SLA vs SLO (nota)
## Riesgos y pendientes
```

## Casos límite

- Sin tráfico histórico → propone SLO provisional + plan de medición; no finjas precisión.
- Dependencia dura de terceros → documenta SLO compuesto o presupuesto compartido; no ocultes el techo.
- Producto pide 100% → rechaza; explica costo e inviabilidad.

## Validación

- SLI es usuario-céntrico y medible.
- Ventana y target explícitos.
- Política escrita con owners de acción.
- Gap de telemetría listado si existe.

## Criterios de terminado

- Catálogo usable por producto y on-call.
- Política de budget lista para acuerdo Franky/producto.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | API pagos 99.9% rolling 28d | SLI success ratio + budget 0.1% + política freeze |
| Ambiguo | “Queremos estar siempre up” | Preguntas de journey + borrador 1–2 SLIs; rechaza 100% |
| Límite | Batch nightly sin RPS | SLI por jobs exitosos en ventana + SLO distinto a HTTP |

## Fuentes

- Google SRE Workbook — Implementing SLOs — https://sre.google/workbook/implementing-slos/ (consultado 2026-08-04).
- Google SRE Workbook — Error Budget Policy — https://sre.google/workbook/error-budget-policy/ (consultado 2026-08-04).
- OpenTelemetry Observability primer (SLI/SLO) — https://opentelemetry.io/docs/concepts/observability-primer/ (consultado 2026-08-04).
