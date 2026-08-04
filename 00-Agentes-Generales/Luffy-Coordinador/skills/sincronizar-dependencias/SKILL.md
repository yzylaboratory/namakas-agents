---
name: sincronizar-dependencias
description: Use esta skill cuando varios agentes trabajen sobre entregables relacionados y sea necesario controlar precedencias, contratos compartidos, puntos de integración, estados y bloqueos sin duplicar trabajo.
compatibility: Compatible con Claude Code y Cursor mediante el estándar Agent Skills.
---

# Sincronizar dependencias

## Propósito

Mantener alineados los flujos de trabajo y evitar que un agente construya sobre supuestos incompatibles.

## Entradas

- Plan de ejecución.
- Responsables.
- Dependencias.
- Contratos o artefactos compartidos.
- Estado de cada tarea.

## Procedimiento

1. Construye un mapa de dependencias.
2. Identifica la ruta crítica.
3. Define la fuente de verdad para cada contrato o decisión.
4. Marca puntos de integración.
5. Establece qué evidencia habilita comenzar una tarea dependiente.
6. Revisa cambios que puedan afectar a otros agentes.
7. Notifica únicamente cambios materiales.
8. Bloquea integraciones sobre versiones no aprobadas.
9. Consolida estados en una vista única.
10. Recalcula el orden cuando cambie una dependencia.

## Estados permitidos

- Pendiente.
- Lista para iniciar.
- En progreso.
- Bloqueada.
- En validación.
- Requiere corrección.
- Completada.

No utilices “casi terminada” como estado. Es una emoción, no información operativa.

## Formato de salida

```md
## Estado consolidado

| Entregable | Responsable | Estado | Depende de | Bloquea a | Próxima acción |
|---|---|---|---|---|---|

## Ruta crítica

1. [...]
2. [...]

## Contratos compartidos

- Fuente de verdad: [...]
- Versión aprobada: [...]
- Consumidores: [...]

## Bloqueos

- [...]
```

## Criterios de finalización

- Cada dependencia tiene un propietario.
- La fuente de verdad está identificada.
- Ninguna tarea dependiente inicia con entradas no aprobadas.
- Los bloqueos y la ruta crítica son visibles.
