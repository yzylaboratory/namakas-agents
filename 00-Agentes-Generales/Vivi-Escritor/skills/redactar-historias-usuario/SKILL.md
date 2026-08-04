---
name: redactar-historias-usuario
description: Redacta historias de usuario y criterios de aceptación verificables a partir de necesidad de negocio o producto. Úsala cuando falten requisitos funcionales claros, acceptance criteria o historias listas para implementación o QA.
metadata:
  author: yzylabs
  version: "1.0"
---

# Redactar historias de usuario

## Propósito

Convertir una necesidad en historias de usuario y criterios de aceptación observables (pass/fail), sin imponer diseño técnico prematuro.

## Entradas

- Necesidad o problema del usuario.
- Actor(es) o roles.
- Restricciones de negocio conocidas.
- Fuera de alcance conocido.
- Evidencia de producto actual (si es mejora).
- Formato preferido (Markdown, ticket, lista).

## Procedimiento

1. Identifica el actor y el valor (por qué importa).
2. Escribe la historia en forma:
   - *Como* [actor], *quiero* [capacidad], *para* [beneficio].
3. Descompón historias demasiado grandes en entregables independientes cuando el valor lo permita.
4. Redacta criterios de aceptación con lenguaje dado/cuando/entonces o checklist pass/fail.
5. Incluye fuera de alcance y supuestos.
6. Evita esconder decisiones de UI/arquitectura dentro de la historia salvo que el usuario las haya fijado.
7. Marca dependencias (datos, permisos, otros sistemas).
8. Entrega un paquete listo para priorización o handoff a implementación/QA.

## Salida

```md
## Historia

Como [actor], quiero [capacidad], para [beneficio].

## Valor / contexto

[…]

## Criterios de aceptación

- [ ] Dado … cuando … entonces …
- [ ] …

## Fuera de alcance

- […]

## Supuestos

- […]

## Dependencias

- […]

## Preguntas abiertas

- […]
```

## Casos límite

- Pedido solo técnico (“agregar índice SQL”): reformula el valor de usuario o clasifica como tarea técnica, no fuerces una historia falsa.
- Criterios no medibles (“sea rápido/bonito”): sustituye por umbrales o comportamientos observables, o marca como no aceptable aún.
- Conflicto entre stakeholders: documenta las dos lecturas y pide decisión; no elijas en silencio.
- Alcance regulado: añade criterios de evidencia/cumplimiento solo con fuente; si no, pregunta abierta.

## Validación

- Cada criterio es verificable sin reinterpretar.
- La historia describe capacidad, no un diseño completo no pedido.
- Fuera de alcance visible.
- No hay features inventadas.

## Criterios de terminado

- Al menos una historia usable con criterios pass/fail.
- Supuestos y preguntas abiertas listados.
- Listo para handoff a Luffy/implementación/QA según el pedido.

## Evaluación sugerida

| Caso | Entrada | Esperado |
|---|---|---|
| Normal | “El cliente quiere exportar movimientos a CSV” | Historia + criterios de formato/campos/errores |
| Ambiguo | “Mejorar el dashboard” | Descomponer o pedir foco; no inventar widgets |
| Límite | Requisito ilegal/inseguro implícito | No normalizarlo; marcar riesgo y escalar |

## Fuentes

- Práctica de criterios verificables alineada a documentación clara (Google style: precisión y audiencia) — https://developers.google.com/style (2026-08-04)
- Separación de “qué necesita el usuario” vs. referencia técnica (Diátaxis / handoff a Robin) — https://diataxis.fr/ (2026-08-04)
