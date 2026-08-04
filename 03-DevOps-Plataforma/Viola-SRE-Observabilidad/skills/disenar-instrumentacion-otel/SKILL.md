---
name: disenar-instrumentacion-otel
description: Diseña instrumentación OpenTelemetry (traces, metrics, logs, Collector/OTLP, correlación). Úsala cuando se pida OTel, tracing distribuido, OTLP, Collector, semantic conventions o unificar telemetría vendor-neutral.
metadata:
  author: yzylabs
  version: "1.0"
---

# Diseñar instrumentación OpenTelemetry

## Propósito

Especificar cómo el servicio emite y correlaciona señales de observabilidad de forma vendor-neutral para diagnosticar unknown unknowns sin instrumentar “a ciegas”.

## Entradas

- Lenguajes/frameworks del servicio.
- Backends actuales (APM, Prometheus, logs).
- SLIs que deben medirse.
- Restricciones de sampling, PII y red.
- Modelo de despliegue (K8s, VM, serverless).

## Procedimiento

1. Declara objetivo de observabilidad: preguntas que debe poder responder el on-call.
2. Mapea señales: traces (spans de journey), metrics (SLI/golden), logs (eventos con contexto).
3. Elige estrategia: auto-instrumentación vs manual en puntos de negocio críticos.
4. Especifica Resource attributes (service.name, version, env) y context propagation.
5. Define export vía OTLP hacia Collector; pipelines de process/export por señal.
6. Lista atributos/semantic conventions mínimas (HTTP/RPC/DB según stack).
7. Define sampling (head/tail) alineado a costo y a necesidad de post-incidente.
8. Señala riesgos de PII en spans/logs y redaction requerida.
9. Entrega plan por fase (MVP correlación → cobertura SLI → rich debugging).
10. Lista dueños de implementación (app vs plataforma) y criterios de aceptación.

## Salida

```md
## Preguntas a responder
## Señales y cobertura
## SDK / auto vs manual
## Resource + propagation
## Collector / OTLP pipelines
## Atributos mínimos
## Sampling y costo
## Privacidad / redaction
## Fases y dueños
## Criterios de aceptación
```

## Casos límite

- Solo logs hoy → plan de correlación progresiva; no prometas traces completos día 1.
- Backend propietario sin OTLP → documenta bridge/Collector exporter; evita lock-in en el diseño.
- Alto cardinality (user_id en métricas) → rechaza labels de alta cardinalidad; usa atributos de span.

## Validación

- Cada SLI material tiene fuente de métrica o derivación documentada.
- Trace context llega a logs o está planificado.
- Collector es el punto de control de export.

## Criterios de terminado

- Spec implementable por app + plataforma.
- Riesgos PII/cardinality/costo listados.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | NestJS + K8s + Prometheus | Plan OTel SDK + Collector + exemplars/traces |
| Ambiguo | “Pon tracing” | Preguntas de journey/SLI + MVP spans HTTP/DB |
| Límite | Batch job sin HTTP | Spans de job/step + metrics de éxito/duración |

## Fuentes

- OpenTelemetry Observability primer — https://opentelemetry.io/docs/concepts/observability-primer/ (consultado 2026-08-04).
- OpenTelemetry Signals — https://opentelemetry.io/docs/concepts/signals/ (consultado 2026-08-04).
- OpenTelemetry Collector — https://opentelemetry.io/docs/collector/ (consultado 2026-08-04).
- OpenTelemetry Docs hub — https://opentelemetry.io/docs/ (consultado 2026-08-04).
