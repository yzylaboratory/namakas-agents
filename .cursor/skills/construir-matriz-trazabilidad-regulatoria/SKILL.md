---
name: construir-matriz-trazabilidad-regulatoria
description: Construye o audita la matriz de trazabilidad bidireccional mandato/control → requisito → caso → resultado/defecto para auditabilidad. Úsala cuando se exija evidencia de cobertura regulatoria o reconstrucción para auditoría.
metadata:
  author: yzylabs
  version: "1.0"
---

# Construir matriz de trazabilidad regulatoria

## Propósito

Establecer linaje verificable entre mandatos/controles citados, requisitos, casos de prueba y resultados, habilitando auditabilidad (forward y backward traceability).

## Entradas

- Lista de mandatos/controles con citas (fuente, versión/fecha).
- Requisitos o historias mapeadas.
- Casos de prueba existentes (si hay).
- Resultados de ejecución / defectos (si el ciclo ya corrió).

## Procedimiento

1. Inventaría controles/mandatos **solo** si están citados; no inventes filas regulatorias.
2. Mapea cada control → requisito(s) funcionales que lo implementan.
3. Mapea cada requisito → caso(s) de prueba.
4. Si hay ejecución: mapea caso → resultado/defecto/evidencia.
5. Calcula cobertura: control sin requisito, requisito sin caso, caso sin resultado (según fase).
6. Clasifica huecos: bloqueante / mayor / menor.
7. Emite matriz + veredicto de auditabilidad: AUDITABLE / AUDITABLE CON DEUDAS / NO AUDITABLE.

## Salida

```md
## Matriz de trazabilidad — [Alcance]

### Veredicto de auditabilidad
### Matriz
| Control/Mandato | Fuente | Requisito | Caso | Resultado | Evidencia |
### Huecos
| ID | Severidad | Tipo | Descripción |
### Forward gaps / Backward gaps
```

## Casos límite

- Controles sin texto fuente → no inventes el control; pide cita a Legal/producto.
- Casos sin requisito (“exploratorios”) → segrega sección; no los uses para afirmar cumplimiento.
- Solo requisitos de producto sin mandato → matriz funcional válida; no etiquetes “regulatoria completa”.

## Validación

- Toda fila de cumplimiento tiene cita de fuente.
- Veredicto alineado a huecos bloqueantes.
- Bidireccionalidad comprobable (de defecto a control y de control a caso).

## Criterios de terminado

- Matriz entregada.
- Veredicto emitido.
- Huecos priorizados.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Controles citados + AC + casos | AUDITABLE o deudas menores |
| Ambiguo | “Cumplir GDPR” sin artículos | NO AUDITABLE / bloqueante por falta de cita |
| Límite | Defecto sin enlace a caso | Backward gap mayor |

## Fuentes

- ISTQB CT-FT Syllabus v1.0 § Compliance Testing — auditability, bidirectional traceability (2026-05-27; consultado 2026-08-04).
- ISTQB Glossary — traceability / compliance testing (consultado 2026-08-04).
