---
name: auditar-resiliencia-integracion-core
description: Audita resiliencia y operabilidad de integraciones al core (reintentos, DLQ, circuit breakers, correlación, replay). Úsala para revisar diseños o integraciones existentes antes de producción o post-incidente.
metadata:
  author: yzylabs
  version: "1.0"
---

# Auditar resiliencia de integración core

## Propósito

Detectar huecos que provoquen duplicados, pérdida de mensajes, tormentas de reintentos o imposibilidad de operar incidentes en la capa de integración.

## Entradas

- Diseño o implementación de integración.
- Contratos (si existen).
- Métricas/logs/runbooks actuales (si hay).
- Clasificación de criticidad del flujo.

## Procedimiento

1. Inventaría caminos felices y de error por operación.
2. Verifica idempotencia y deduplicación en efectos financieros.
3. Revisa política de reintentos (jitter, límites, errores no retryable).
4. Verifica DLQ/poison: existencia, alertas, ownership de drenado.
5. Evalúa circuit breaker / bulkhead / backpressure hacia el core.
6. Comprueba correlación end-to-end y capacidad de replay seguro.
7. Revisa secretos/permisos de identidades de integración (least privilege).
8. Emite hallazgos severidad + remediación + dueño; no “apruebes” excepciones de seguridad.

## Salida

```md
## Alcance auditado
## Hallazgos (sev / evidencia)
## Idempotencia / duplicados
## Reintentos / DLQ
## Aislamiento / backpressure
## Correlación / replay
## Remediaciones priorizadas
## Riesgos residuales
```

## Casos límite

- No hay telemetría → hallazgos de observabilidad como blocker para prod.
- Replay sin idempotencia → severidad crítica si hay posting.
- Multi-tenant queues → exige segregación; escala seguridad.

## Validación

- Cada hallazgo tiene evidencia o “no observado / supuesto” etiquetado.
- Efectos financieros sin idempotencia = crítico.
- Remediaciones con dueño.

## Criterios de terminado

- Iceburg/ops tienen lista priorizada accionable.
- No se declara “resiliente” sin DLQ+idempotencia en flujos críticos.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | API sync + cola async documentadas | Hallazgos menores + checklist OK/NOK |
| Ambiguo | “¿Está estable la integración?” | Preguntas de flujos críticos + auditoría acotada |
| Límite | Reintentos infinitos sin DLQ | Hallazgo crítico + plan de contención |

## Fuentes

- 6B Core Banking Integration (security + queues) — https://6b.finance/insight/core-banking-system-integration-using-iso-20022-rest-apis-and-legacy-message-queues/ (2026-08-04).
- IoT Digital Twin PLM — orchestration/idempotency — https://iotdigitaltwinplm.com/iso-20022-migration-payments-architecture-2026/ (2026-08-04).
- BlazeTrends Core Banking APIs — https://blazetrends.com/how-core-banking-apis-connect-with-external-financial-systems/ (2026-08-04).
