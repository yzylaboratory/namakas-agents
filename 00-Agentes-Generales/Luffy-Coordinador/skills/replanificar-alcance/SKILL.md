---
name: replanificar-alcance
description: Use esta skill cuando cambien requisitos, riesgos, capacidad, dependencias o evidencia y sea necesario adaptar el plan sin perder el objetivo principal ni introducir cambios silenciosos.
compatibility: Compatible con Claude Code y Cursor mediante el estándar Agent Skills.
---

# Replanificar alcance

## Propósito

Adaptar la ejecución ante nueva información conservando foco, trazabilidad y control.

## Entradas

- Objetivo vigente.
- Plan actual.
- Cambio detectado.
- Impacto sobre tareas, fechas, riesgos y contratos.
- Trabajo ya completado.

## Procedimiento

1. Describe qué cambió y por qué.
2. Confirma si el objetivo principal sigue siendo válido.
3. Evalúa impacto sobre:
   - Alcance.
   - Prioridad.
   - Dependencias.
   - Arquitectura.
   - Seguridad y cumplimiento.
   - Costo.
   - Entregables completados.
4. Conserva el trabajo útil.
5. Elimina o pospone trabajo que perdió valor.
6. Redefine tareas y responsables afectados.
7. Actualiza criterios de aceptación.
8. Compara el plan anterior y el nuevo.
9. Registra la decisión.
10. Comunica el cambio a los agentes afectados.

## Regla de protección

No cambies el objetivo para justificar un plan fallido. Primero determina si:

- El objetivo cambió realmente.
- El plan era incorrecto.
- Apareció una restricción nueva.
- Un supuesto resultó falso.

## Formato de salida

```md
## Cambio

Qué cambió:
Motivo:
Evidencia:

## Impacto

- Objetivo:
- Alcance:
- Dependencias:
- Riesgos:
- Costos:
- Entregables:

## Plan actualizado

1. [...]
2. [...]

## Trabajo retirado o pospuesto

- [...]

## Decisión registrada

- [...]
```

## Criterios de finalización

- El objetivo vigente está explícito.
- Los cambios tienen motivo y evidencia.
- El plan actualizado no conserva tareas obsoletas.
- Los agentes afectados fueron identificados.
- No existen ampliaciones silenciosas.
