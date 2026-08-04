---
name: resolver-bloqueos
description: Use esta skill cuando una tarea o agente no pueda avanzar por falta de información, permisos, herramientas, dependencias, decisiones, acceso, capacidad o conflictos de alcance.
compatibility: Compatible con Claude Code y Cursor mediante el estándar Agent Skills.
---

# Resolver bloqueos

## Propósito

Eliminar impedimentos con el menor impacto posible sobre alcance, calidad y calendario.

## Clasificación

Clasifica el bloqueo como:

- Información.
- Decisión.
- Dependencia.
- Acceso o permiso.
- Herramienta o entorno.
- Error técnico.
- Capacidad.
- Conflicto de alcance.
- Riesgo regulatorio, legal o de seguridad.

## Procedimiento

1. Describe el bloqueo con evidencia.
2. Identifica la causa raíz, no solo el síntoma.
3. Determina qué tareas están afectadas.
4. Busca una resolución local y reversible.
5. Consulta al especialista adecuado.
6. Reordena tareas independientes si pueden avanzar sin riesgo.
7. Escala únicamente la decisión mínima necesaria.
8. Registra la resolución y sus consecuencias.
9. Confirma que la tarea puede continuar.
10. Actualiza dependencias y prioridad.

## Estrategias permitidas

- Obtener información faltante.
- Corregir el entorno.
- Aprobar o actualizar un contrato.
- Crear un stub o simulador claramente identificado.
- Dividir el trabajo.
- Reordenar tareas.
- Sustituir una dependencia por una alternativa aprobada.
- Reducir alcance sin comprometer el objetivo.

## Estrategias prohibidas

- Inventar datos.
- Ignorar una validación.
- Ocultar el bloqueo.
- Marcar una tarea como completada.
- Saltarse controles regulatorios o de seguridad.
- Crear una solución temporal sin registrarla.

## Formato de salida

```md
## Bloqueo

Descripción:
Evidencia:
Causa:
Impacto:

## Resolución recomendada

Acción:
Responsable:
Riesgo:
Tiempo o dependencia:
Plan alternativo:

## Estado posterior

[Desbloqueada | Sigue bloqueada]
```

## Criterios de finalización

- La causa está identificada.
- Existe una acción y responsable.
- El impacto es visible.
- La solución no oculta deuda ni riesgo.
- El estado posterior fue confirmado.
