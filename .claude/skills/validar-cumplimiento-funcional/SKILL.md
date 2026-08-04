---
name: validar-cumplimiento-funcional
description: Ejecuta o revisa la validación funcional de controles y requisitos regulatorios citados, emitiendo veredicto con evidencia. Úsala cuando haya que demostrar cumplimiento funcional (no dictamen legal) antes de release o auditoría.
metadata:
  author: yzylabs
  version: "1.0"
---

# Validar cumplimiento funcional

## Propósito

Determinar si el SUT cumple los comportamientos y controles funcionales exigidos por requisitos/mandatos **citados**, con evidencia reproducible y clasificación de hallazgos.

## Entradas

- Matriz de trazabilidad (idealmente previa).
- Casos de prueba funcionales prioritarios.
- Acceso a evidencias de ejecución, logs sintéticos, capturas o resultados de entorno de prueba.
- Alcance y criterios de salida del ciclo.

## Procedimiento

1. Confirma que cada control bajo validación tiene cita y caso asociado.
2. Ejecuta o revisa evidencia caso por caso (según mandato de la tarea).
3. Clasifica cada ítem: PASS / FAIL / BLOCKED / NOT_EXECUTED.
4. Para FAIL: tipo = defecto funcional | control ausente | control parcial | evidencia insuficiente.
5. Vincula defectos a requisito y control.
6. Agrega cobertura de controles críticos vs no críticos.
7. Emite veredicto: CUMPLE / CUMPLE CON DEUDAS / NO CUMPLE / NO DETERMINABLE.
8. Lista residual risk y handoffs (Legal / Kuma / Kalifa).

## Salida

```md
## Validación de cumplimiento funcional — [Alcance]

### Veredicto
### Resumen de ejecución
| Caso | Control | Resultado | Evidencia |
### Hallazgos
| ID | Tipo | Severidad | Requisito | Control | Descripción |
### Cobertura de controles críticos
### Riesgo residual
### Handoffs
```

## Casos límite

- Sin entorno: produce checklist de ejecución y marca NOT_EXECUTED; veredicto NO DETERMINABLE si críticos no corridos.
- “El negocio dice que cumple” sin evidencia → no aceptes; exige artefacto.
- Conflicto requisito vs mandato citado → NO DETERMINABLE + escalamiento legal; no elijas tú la norma.

## Validación

- Ningún PASS de control crítico sin evidencia referenciada.
- Veredicto coherente con FAILs en controles críticos.
- Sin afirmaciones legales fuera de hechos observados.

## Criterios de terminado

- Veredicto emitido.
- Hallazgos tipados y trazados.
- Residual risk explícito.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Suite crítica PASS con evidencias | CUMPLE o deudas menores |
| Ambiguo | Evidencias parciales en 1 control crítico | NO DETERMINABLE o CUMPLE CON DEUDAS |
| Límite | Mandato citado contradictorio con AC | Escalamiento legal + NO DETERMINABLE |

## Fuentes

- ISTQB CT-FT Syllabus v1.0 § Compliance Testing — objectives, control/substantive testing, auditability (2026-05-27; consultado 2026-08-04).
- ISTQB CT-FT BO2 — practices supporting compliance with auditability and documentation (consultado 2026-08-04).
