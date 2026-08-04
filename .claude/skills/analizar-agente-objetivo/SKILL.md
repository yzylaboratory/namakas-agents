---
name: analizar-agente-objetivo
description: Analiza una solicitud para crear o actualizar un agente, identifica misión, departamento, responsabilidades, límites, relaciones y entregables. Úsala antes de investigar o generar cualquier agente individual.
metadata:
  author: yzylabs
  version: "1.0"
---

# Analizar agente objetivo

## Entradas

- Nombre o responsabilidad solicitada.
- Departamento y célula.
- Personaje asignado, si existe.
- Catálogo y agentes ya creados.

## Procedimiento

1. Resume la responsabilidad principal en una oración.
2. Identifica usuarios internos y entregables.
3. Separa responsabilidades permanentes de procedimientos repetibles.
4. Define límites de autoridad y riesgos.
5. Detecta solapamientos con agentes existentes.
6. Identifica agentes a los que delegará y de los que recibirá trabajo.
7. Formula preguntas de investigación concretas.
8. Produce una ficha de diseño.

## Salida

```md
Nombre:
Personaje:
Misión:
Departamento:
Responsabilidades:
Fuera de alcance:
Entradas:
Salidas:
Delegaciones:
Riesgos:
Preguntas de investigación:
```

## Validación

- La misión es única.
- No duplica otro agente.
- Los procedimientos candidatos pueden convertirse en skills.
- Los límites son explícitos.
