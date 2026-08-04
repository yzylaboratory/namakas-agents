---
name: evaluar-madurez-backend
description: Evalúa madurez y readiness de la plataforma backend (ownership, contratos, datos, eventos, observabilidad, operación) y propone gates. Úsala antes de escalar el catálogo de servicios, adoptar EDA amplia o afirmar que el departamento está listo para alta carga.
metadata:
  author: yzylabs
  version: "1.0"
---

# Evaluar madurez Backend

## Propósito

Diagnosticar si la ambición de escala/modernización es realista dado el estado de capacidades, y definir gates antes de exponer más servicios, schemas o topics.

## Entradas

- Ambición declarada (mantener, modernizar, EDA-first, multi-región).
- Evidencia operativa: incidentes, SLOs, lag, fallos de migración, on-call.
- Catálogo de servicios / ownership / contratos.
- Hallazgos de discovery si existen.

## Procedimiento

1. Puntúa madurez (1–5) en dimensiones:
   - **Ownership y bounded contexts**
   - **Contratos API/eventos** (versionado, compatibilidad)
   - **Datos** (database-per-service, migraciones, calidad)
   - **Eventos** (idempotencia, DLQ, schema registry/contrato)
   - **Observabilidad y SLOs**
   - **Operación** (rollback, capacity, runbooks, blast radius)
   - **Organización** (RACI, paved road, presupuesto de plataforma)
2. Identifica el cuello de botella más bajo (la dimensión más débil limita el resto).
3. Define gates go/no-go para la siguiente ola de servicios o topics.
4. Propón plan de cierre de gaps en 30/60/90 días alineado al squad.
5. Señala riesgos de “exportar problemas internos” vía más APIs/eventos.

## Salida

```md
## Ambición vs readiness
## Scorecard
| Dimensión | Score 1-5 | Evidencia | Gap crítico |
## Cuello de botella
## Gates go/no-go
## Plan 30/60/90
## Riesgos si se escala ahora
```

## Casos límite

- Scores altos en código de servicio pero bajos en datos/eventos: no aprobar EDA amplia.
- Deadline de producto con madurez baja: MVP controlado + deuda explícita con expiry.
- Falta de evidencia: marca dimensión como “desconocida”, no como madura.
- Células stub: limita scores de ejecución; no inventes madurez de implementación.

## Validación

- Cada score tiene evidencia o está marcado desconocido.
- Gates son binarios y verificables.
- El plan tiene dueños (Katakuri/X-Drake/Pudding/Apoo/otros).

## Criterios de terminado

- Scorecard completo.
- Recomendación clara: escalar / pausar / solo plataforma mínima.
- Gates acordables con Luffy y el squad.

## Fuentes

- Azure Architecture Center — Microservices — https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/microservices (2026-08-04)
- Confluent — EDA intro — https://www.confluent.io/learn/event-driven-architecture/ (2026-08-04)
- Atlassian StreamHub — capacity guardrails and recovery — consultado 2026-08-04
- 12-Factor App — https://12factor.net/ (2026-08-04)
