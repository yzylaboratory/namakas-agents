---
name: priorizar-iniciativas-backend
description: Prioriza el backlog del departamento Backend con valor, dependencia, riesgo operativo y dueño. Úsala cuando haya conflictos de prioridad entre servicios, datos, eventos, deuda técnica o deadlines de producto.
metadata:
  author: yzylabs
  version: "1.0"
---

# Priorizar iniciativas Backend

## Propósito

Ordenar el trabajo departamental de forma defendible, evitando que features urgentes oculten riesgo de producción o deuda de plataforma.

## Entradas

- Backlog o lista de iniciativas candidatas.
- Dependencias conocidas (contratos, migraciones, consumidores).
- Capacidad del squad y estado stub/forjado de células.
- Incidentes recientes, error budgets y compromisos externos.

## Procedimiento

1. Normaliza cada ítem: outcome, bounded context, esfuerzo relativo, dueño propuesto.
2. Puntúa (o rankea) por:
   - Valor de negocio / compromiso externo.
   - Riesgo si se atrasa (seguridad, data loss, compliance, partner).
   - Dependencias bloqueantes (qué desbloquea).
   - Blast radius si falla.
3. Aplica gates: no priorizar exposición nueva sin ownership + contrato + SLO mínimo.
4. Produce Now / Next / Later con justificación de 1–2 líneas por ítem Now.
5. Marca explícitamente lo que se **desprioriza** y el costo de oportunidad.
6. Si una célula requerida está stub: el ítem de ejecución queda BLOCKED; la priorización de dirección puede COMPLETED_WITH_LIMITATIONS.

## Salida

```md
## Criterios de priorización
## Now
| Ítem | Dueño | Por qué ahora | Gate |
## Next / Later
## Despriorizado (con costo)
## Bloqueos por stub / dependencias
## Decisiones requeridas de Luffy
```

## Casos límite

- Dos features “P0” del mismo servicio: forzar owner único y secuencia.
- Deuda crítica post-incidente: puede saltar a Now con expiry de excepción.
- Prioridad pedida por otro departamento sin contexto: escalar a Luffy, no aceptar ciego.

## Validación

- Cada Now tiene dueño y gate.
- Hay al menos un ítem explícitamente despriorizado o diferido (si el backlog no es trivial).
- Bloqueos stub están visibles.

## Criterios de terminado

- Backlog ordenado usable en planning.
- Justificaciones auditables.
- Sin ambigüedad de “todo es P0”.

## Fuentes

- Azure Architecture Center — Microservices (autonomía, acoplamiento) — https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/microservices (2026-08-04)
- Atlassian StreamHub lessons — capacity, blast radius, guardrails — consultado 2026-08-04
