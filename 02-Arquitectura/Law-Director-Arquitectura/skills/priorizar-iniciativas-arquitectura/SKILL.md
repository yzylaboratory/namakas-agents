---
name: priorizar-iniciativas-arquitectura
description: Prioriza iniciativas de arquitectura, modernización y deuda técnica con valor, riesgo, dependencia y dueños (Now/Next/Later). Úsala cuando se pida backlog de arquitectura, ranking de deuda, roadmap de modernización o replanificación del departamento.
metadata:
  author: yzylabs
  version: "1.0"
---

# Priorizar iniciativas de arquitectura

## Propósito

Ordenar el backlog departamental de arquitectura con criterios explícitos para que Luffy y el squad ejecuten sin reinterpretar prioridades.

## Entradas

- Backlog candidato (deuda, modernización, estándares, habilitadores).
- Riesgos conocidos (incidentes, SPOF, compliance de diseño).
- Dependencias externas (producto, OB, plataforma).
- Capacidad del squad y horizonte temporal.

## Procedimiento

1. Normaliza cada ítem: problema, impacto, esfuerzo relativo, riesgo de no hacer, dependencias, dueño tentativo.
2. Clasifica: **riesgo inmediato**, **habilitador estratégico**, **deuda estructural**, **higiene/estándar**.
3. Aplica scoring simple y transparente (no caja negra):
   - Valor / riesgo reducido.
   - Urgencia (incidente, bloqueo de producto, vencimiento de excepción).
   - Esfuerzo y dependencia.
4. Produce Now / Next / Later con WIP limit razonable para el squad.
5. Marca qué requiere Enel / Fujitora / Wapol y qué queda en Law.
6. Declara qué se dice “no ahora” y por qué (evita prioridad infinita).
7. Replanifica si cambian incidentes, capacidad o mandatos de Luffy.

## Salida

```md
## Criterios de priorización
## Backlog priorizado
| Ítem | Clase | Valor/Riesgo | Esfuerzo | Dueño | Now/Next/Later |
## WIP y capacidad
## No-ahora (explícito)
## Dependencias y bloqueos
## Recomendación a Luffy
```

## Casos límite

- Todo es P0: fuerza ranking relativo; pide a Luffy corte de capacidad.
- Deuda invisible sin evidencia: exige síntoma (incidente, lead time, acoplamiento medible) antes de priorizar alto.
- Iniciativa multi-departamento: prioriza la parte Arquitectura y escala el resto a Luffy.

## Validación

- Cada ítem Now tiene dueño y resultado esperable.
- Criterios son reproducibles.
- Hay lista explícita de no-ahora.
- No se priorizó por moda tecnológica sin valor/riesgo.

## Criterios de terminado

- Backlog usable para planificar el squad.
- Trade-offs de prioridad documentados.
- Escalaciones a Luffy claras cuando falte capacidad o autoridad.

## Fuentes

- The Open Group — TOGAF EA capability / roadmap practices (síntesis 10th Edition) — https://publications.opengroup.org/c220 (2026-08-04)
- Prácticas de priorización de deuda técnica y modernización en EA governance (secundaria contrastada) — 2026-08-04
