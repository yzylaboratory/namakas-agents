---
name: descomponer-trabajo
description: Use esta skill cuando una iniciativa sea demasiado grande para ejecutarse directamente y deba dividirse en entregables pequeños, verificables, ordenados por dependencias y asignables a agentes especializados.
compatibility: Compatible con Claude Code y Cursor mediante el estándar Agent Skills.
---

# Descomponer trabajo

## Propósito

Convertir una misión alineada en unidades de trabajo coherentes y verificables.

## Entradas

- Objetivo principal.
- Alcance.
- Restricciones.
- Criterios de éxito.
- Arquitectura o procesos existentes, si aplican.

## Procedimiento

1. Identifica los entregables finales.
2. Trabaja hacia atrás desde cada entregable.
3. Separa decisiones, investigación, diseño, implementación, validación y documentación.
4. Divide tareas grandes hasta que cada una:
   - Tenga un resultado concreto.
   - Pueda asignarse a un responsable.
   - Pueda validarse independientemente.
   - Tenga dependencias explícitas.
5. Detecta hitos que reduzcan incertidumbre.
6. Marca tareas paralelizables.
7. Evita crear tareas puramente ceremoniales.
8. Comprueba que la suma de tareas cubra el objetivo sin ampliar el alcance.

## Granularidad recomendada

Una tarea está bien delimitada cuando puede describirse con:

- Un verbo.
- Un objeto.
- Un entregable.
- Un responsable.
- Un criterio de aceptación.

Ejemplo correcto: “Definir el contrato OpenAPI de consulta de cuentas y validarlo contra las reglas de consentimiento”.

Ejemplo deficiente: “Trabajar en Open Banking”.

## Formato de salida

```md
## Entregables

### E1 — [Nombre]

Resultado: [...]
Responsable sugerido: [...]
Dependencias: [...]
Criterios de aceptación: [...]

#### Tareas

1. [Tarea]
2. [Tarea]
```

## Validación

Comprueba:

- Cobertura completa del objetivo.
- Ausencia de tareas duplicadas.
- Dependencias sin ciclos.
- Responsables claros.
- Tareas suficientemente pequeñas.
- Exclusión de trabajo no solicitado.
