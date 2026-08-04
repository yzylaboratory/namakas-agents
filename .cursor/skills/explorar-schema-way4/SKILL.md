---
name: explorar-schema-way4
description: "Amplía el hub durable de Way4 ante gaps. Úsala solo si references/way4.md no documenta el objeto necesario."
metadata:
  author: yzylabs
  version: "1.0"
---

# explorar-schema-way4

## Propósito

Cerrar gaps UNKNOWN del hub `way4` con evidencia live mínima, sin re-dump completo del catálogo.

## Entradas

- Gap concreto (tabla/columna/vista/SP).
- Hub actual `references/way4.md`.

## Procedimiento

1. Confirma que el objeto **no** está en el hub/index.
2. Meta-query acotada (ALL_TAB_COLUMNS / USER_TABLES) solo al objeto faltante.
3. Documenta columnas/joins relevantes + fecha de exploración.
4. Marca UNKNOWN lo no verificado.
5. Actualiza hub/index con evidencia; no copies secretos.

## Salida

```md
## Gap
## Evidencia SQL
## Patch al hub
## UNKNOWN restantes
```

## Validación

- No re-inventario masivo de catálogo documentado.
- Sin PII/secretos en el patch.

## Criterios de terminado

- Gap cerrado o UNKNOWN explícito con dueño.
