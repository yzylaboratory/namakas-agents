---
name: explorar-schema-siebel
description: "Amplía el hub durable de Siebel ante gaps. Úsala solo si references/siebel.md no documenta el objeto necesario."
metadata:
  author: yzylabs
  version: "1.0"
---

# explorar-schema-siebel

## Propósito

Cerrar gaps UNKNOWN del hub `siebel` con evidencia live mínima, sin re-dump completo del catálogo.

## Entradas

- Gap concreto (tabla/columna/vista/SP).
- Hub actual `references/siebel.md`.

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
