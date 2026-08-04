---
name: auditar-integridad-transaccional
description: Audita integridad de diseños o flujos transaccionales (doble posteo, desbalance, breaks de reconciliación, correlación rota). Úsala antes de marcar un diseño completo o al investigar inconsistencias ledger vs mensajes.
metadata:
  author: yzylabs
  version: "1.0"
---

# Auditar integridad transaccional

## Propósito

Detectar fallas de integridad en el diseño o en evidencias de flujo: duplicados, desbalances, huecos de correlación y breaks de reconciliación — con veredicto accionable.

## Entradas

- Artefactos de ciclo de vida, idempotencia, posteo y compensación.
- Muestras sintéticas de mensajes/eventos (sin PII real).
- Reglas de reconciliación esperadas (intraday/EOD).
- Criterios de aceptación de la misión.

## Procedimiento

1. Inventaría invariantes declarados (D=C, exactly-once efectivo, correlación).
2. Busca caminos de doble posteo (retry, dual writer, race).
3. Verifica que toda reversa correlacione y no borre historia.
4. Revisa reconciliación: expected vs booked; clasificación de breaks.
5. Comprueba que status/reporting pueda reconstruir el ciclo vía IDs.
6. Etiqueta hallazgos: crítico / alto / medio; bloqueantes vs deuda.
7. Emite veredicto: `PASS` | `PASS_WITH_LIMITATIONS` | `FAIL`.
8. Lista correcciones requeridas antes de `HANDOFF_TX` completo.

## Salida

```md
# Auditoría integridad — [Flujo]

## Invariantes revisados
## Hallazgos
| ID | Severidad | Evidencia | Impacto | Remedio |
## Veredicto
## Bloqueantes para completo
```

## Casos límite

- Diseño parcial consciente → `PASS_WITH_LIMITATIONS` si huecos explícitos y no críticos ocultos.
- Solo narrativa sin tablas de estado → `FAIL` por falta de evidencia.
- Break sin dueño de excepción → hallazgo alto.

## Validación

- Cada hallazgo cita evidencia (sección/ruta).
- Veredicto coherente con severidades.
- Sin PII real en el informe.

## Criterios de terminado

- Informe con veredicto.
- Bloqueantes listados o confirmados ausentes.
- Listo para decidir estado del handoff.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Spec completa con idempotencia | PASS o limitaciones menores |
| Ambiguo | Solo diagramas sueltos | FAIL o bloqueantes claros |
| Límite | Idempotencia API sí, ledger no | Hallazgo crítico doble posteo |

## Fuentes

- Prácticas de reconciliación streaming/EOD vs ledger — 2026-08-04
- Invariantes ACID / idempotencia en pagos — 2026-08-04
