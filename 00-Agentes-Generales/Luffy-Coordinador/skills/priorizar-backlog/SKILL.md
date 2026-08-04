---
name: priorizar-backlog
description: Use esta skill cuando existan múltiples tareas, solicitudes o flujos compitiendo por atención y sea necesario ordenarlos por valor, riesgo, urgencia, dependencias, costo y capacidad del equipo.
compatibility: Compatible con Claude Code y Cursor mediante el estándar Agent Skills.
---

# Priorizar backlog

## Propósito

Crear un orden de ejecución defendible y alineado con el objetivo principal.

## Entradas

- Objetivo.
- Lista de tareas o entregables.
- Dependencias.
- Riesgos.
- Restricciones de capacidad o fecha.

## Criterios

Evalúa cada elemento según:

1. Seguridad y cumplimiento.
2. Capacidad de desbloquear otras tareas.
3. Reducción de riesgo o incertidumbre.
4. Valor para el usuario o negocio.
5. Urgencia real.
6. Costo y esfuerzo.
7. Reversibilidad.
8. Dependencias externas.

## Procedimiento

1. Elimina tareas fuera de alcance.
2. Identifica obligaciones regulatorias o de seguridad.
3. Marca bloqueadores y dependencias críticas.
4. Prioriza pruebas de supuestos de alto riesgo.
5. Ordena el trabajo que genera valor temprano.
6. Ajusta el orden según capacidad disponible.
7. Explica las tres decisiones de prioridad más importantes.
8. Define qué no se hará todavía.

## Regla de desempate

Cuando dos tareas tengan prioridad similar:

1. Ejecuta primero la que desbloquee más trabajo.
2. Luego la que reduzca mayor riesgo.
3. Luego la que sea más reversible.
4. Finalmente, la de menor costo.

## Formato de salida

```md
## Prioridad actual

| Orden | Tarea | Motivo | Dependencias | Riesgo de retraso |
|---:|---|---|---|---|

## Ahora

- [...]

## Después

- [...]

## No todavía

- [...]

## Decisiones de prioridad

1. [...]
```

## Criterios de finalización

- Cada tarea tiene una posición defendible.
- Los bloqueadores aparecen antes que sus dependientes.
- El orden protege seguridad y cumplimiento.
- Existe una lista explícita de trabajo pospuesto.
