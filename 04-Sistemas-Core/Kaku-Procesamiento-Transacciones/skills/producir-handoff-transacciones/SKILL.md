---
name: producir-handoff-transacciones
description: Empaqueta HANDOFF_TX con ciclo de vida, idempotencia, posteo, compensación, integridad y pendientes para Tom/Robin/implementadores. Úsala al cerrar un diseño de procesamiento de transacciones o al transferir trabajo a integración/especificación.
metadata:
  author: yzylabs
  version: "1.0"
---

# Producir HANDOFF_TX

## Propósito

Entregar un paquete único y consumible que permita a peers continuar sin reinterpretar la semántica transaccional.

## Entradas

- Salidas de skills de ciclo de vida, idempotencia, posteo, compensación y/o auditoría.
- Destinatario (Tom, Robin, backend, Iceburg).
- Estado pretendido: `completo` | `parcial` | `borrador`.

## Procedimiento

1. Reúne artefactos y rutas de archivos.
2. Completa el contrato en `references/contrato-handoff-transacciones.md`.
3. Fija estado honesto según auditoría (no “completo” con bloqueantes).
4. Lista dependencias: Tom (adapters), Crocus (legacy), Lucci (BIAN), Robin (API).
5. Incluye riesgos, decisiones abiertas y next handoff.
6. Adjunta evidencia de validaciones ejecutadas.
7. Prepara bloque de reporte `REPORT_TO: iceburg-director-sistemas-core`.

## Salida

Documento `HANDOFF_TX` según contrato de references, más resumen ejecutivo para Iceburg.

## Casos límite

- Destinatario Robin sin límites de API → handoff marca que falta tratado; no inventes OpenAPI.
- Falta auditoría → máximo `parcial`.
- Conflicto con ADR → `DECISIONS_REQUIRED` explícito.

## Validación

- Campos mínimos del contrato presentes.
- Estado coherente con bloqueantes.
- Sin PII real.
- `REPORT_TO` correcto.

## Criterios de terminado

- `HANDOFF_TX` escrito en ruta acordada.
- Peer puede actuar o listar preguntas concretas.
- Reporte listo para Iceburg.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Specs + auditoría PASS | HANDOFF completo |
| Ambiguo | Solo ciclo de vida | parcial + pendientes |
| Límite | FAIL en auditoría | borrador/parcial; no completo |

## Fuentes

- `references/contrato-handoff-transacciones.md`
- Contratos Nakamas de reporte — 2026-08-04
