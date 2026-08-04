---
name: orquestar-saga-compensaciones-financieras
description: Diseña sagas con compensaciones idempotentes para flujos financieros multi-paso. Úsala cuando un caso de uso atraviese más de dos side-effects (débito, riesgo, crédito, capture) y 2PC no sea viable.
metadata:
  author: yzylabs
  version: "1.0"
---

# Orquestar saga y compensaciones financieras

## Propósito

Coordinar consistencia eventual entre pasos financieros con acciones compensatorias explícitas, estados observables y reconciliación — sin 2PC entre DB y sistemas externos.

## Entradas

- Flujo multi-paso (secuencia de comandos/side-effects).
- Invariantes de dinero del bounded context.
- Capacidades de compensación de cada paso (refund, release hold, reverse).
- Restricciones de orquestador (Temporal/Dapr/custom) si existen.

## Procedimiento

1. Confirma que el flujo tiene >2 side-effects o cruza límites de servicio; si es local ACID, no fuerces saga.
2. Elige orquestación (preferida para pagos) vs coreografía; documenta la decisión.
3. Por cada paso forward: precondiciones, timeout, resultado (`success`/`fail`/`ambiguous`).
4. Por cada paso: compensación idempotente y estado de negocio aceptable tras compensar.
5. Define máquina de estados del saga (incl. stuck / compensating / failed / manual).
6. Prohíbe retry ciego de pasos no idempotentes; aplica query-back o marca ambiguous.
7. Diseña reconciliación (scanner de stuck) y kill-switch hacia intervención manual.
8. Entrega diagrama/tabla + requisitos de observabilidad (trace id, saga id).

## Salida

```md
## Decisión orquestación vs coreografía
## Pasos forward / compensación
## Estados del saga
## Ambiguous / reconciliación
## Observabilidad
## Riesgos
```

## Casos límite

- Compensación imposible (p. ej. cash out irreversible) → estado terminal + proceso de negocio, no fingir undo.
- Paso legacy sin idempotencia → adapter con dedup o bloqueo.
- Saga de un solo servicio con TX local → simplifica; no introduzcas orquestador cosmético.

## Validación

- Cada forward material tiene compensación o justificación de irreversibilidad.
- Estados stuck tienen dueño de reconciliación.
- Pasos son idempotentes o tienen estrategia anti-doble-efecto.

## Criterios de terminado

- Un operador puede leer el estado del saga y saber qué falta.
- No se depende de 2PC DB↔broker/PSP.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | debit → fraud → credit | Saga orquestada + compensaciones |
| Ambiguo | Timeout en credit tras debit | Compensación/refund path + reconciliación |
| Límite | Paso irreversible mid-flow | Estado manual + política de negocio |

## Fuentes

- microservices.io — Saga pattern — https://microservices.io/patterns/data/saga.html (2026-08-04).
- Contraste: Practical Saga Orchestration / banking MS guides (secundario, 2026-08-04).
