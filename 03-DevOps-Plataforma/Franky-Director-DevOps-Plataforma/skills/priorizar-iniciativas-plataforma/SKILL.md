---
name: priorizar-iniciativas-plataforma
description: Prioriza el backlog del departamento DevOps/Plataforma con valor DevEx, riesgo operativo, dependencias y dueños. Úsala cuando haya que ordenar iniciativas de paved road, elegir Now/Next/Later o replanificar tras incidentes o cuellos de botella de entrega.
metadata:
  author: yzylabs
  version: "1.0"
---

# Priorizar iniciativas de plataforma

## Propósito

Convertir un backlog desordenado de herramientas, tickets e ideas en una cola priorizada con justificación explícita y gates de madurez.

## Entradas

- Backlog candidato (epics, toil, requests de equipos).
- Capacidad del squad Capone / Viola / Haredas / Paulie.
- Riesgos abiertos (seguridad, confiabilidad, deuda de path).
- Métricas o señales disponibles (DORA, adopción, incidentes).

## Procedimiento

1. Normaliza cada ítem: problema del journey, outcome, esfuerzo relativo, riesgo de no hacer.
2. Puntúa con criterios explícitos (ajusta pesos solo si los documentas):
   - Impacto DevEx / lead time.
   - Reducción de riesgo operativo o change failure.
   - Desbloqueo de otros equipos.
   - Costo de delay / toil acumulado.
3. Aplica gates: no priorices self-service amplio si faltan rollback, secretos o telemetría mínima.
4. Ordena Now (capacidad real) / Next / Later / Won’t.
5. Asigna dueño celular o Franky (dirección) y criterio de salida verificable.
6. Declara trade-offs rechazados (qué no se hará este ciclo).

## Salida

```md
## Criterios y pesos
## Backlog priorizado
| Ítem | Now/Next/Later | Valor | Riesgo | Dependencias | Dueño | Gate de salida |
## Rechazados / diferidos
## Capacidad asumida
## Riesgos de la priorización
```

## Casos límite

- Incidente P1 en curso: pausa roadmap cosmético; prioriza restore + acción correctiva con Viola.
- Request ejecutivo de “tool X”: traduce a journey/outcome o marca como Won’t con razón.
- Células stub: prioriza igual; marca ejecución como `DELEGATION_REQUIRED` / forja pendiente.

## Validación

- Todo ítem Now tiene dueño y gate.
- No hay dos Now que peleen el mismo recurso crítico sin regla de merge.
- Gates de seguridad/observabilidad no se saltan por urgencia de feature de plataforma.

## Criterios de terminado

- Cola accionable para el ciclo.
- Trade-offs explícitos.
- Lista lista para contratos de delegación.

## Fuentes

- DORA Platform engineering — product mindset, MVP platform, pitfalls ticket-ops/big-bang — https://dora.dev/capabilities/platform-engineering/ (consultado 2026-08-04)
- DORA four keys como señales de outcome — https://dora.dev/ (consultado 2026-08-04)
