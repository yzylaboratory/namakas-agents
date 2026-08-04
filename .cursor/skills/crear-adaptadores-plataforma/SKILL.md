---
name: crear-adaptadores-plataforma
description: Crea archivos de subagente invocables para Cursor y Claude Code a partir de un agente canónico. Úsala después de generar el agente estándar y antes de la validación final.
metadata:
  author: yzylabs
  version: "1.0"
---

# Crear adaptadores de plataforma

## Procedimiento

1. Determina el slug del agente.
2. Define herramientas y modo de lectura o escritura.
3. Genera el adaptador de Cursor.
4. Genera el adaptador de Claude Code.
5. Valida rutas, frontmatter y permisos.

## Cursor

Crea `.cursor/agents/<slug>.md` con:

- `name` único.
- `description` específica sobre cuándo delegar.
- `model: inherit` salvo razón documentada.
- `readonly: true` cuando el agente solo investiga o audita.
- Cuerpo autocontenido que apunte al agente canónico.

## Claude Code

Crea `.claude/agents/<slug>.md` con:

- `name` y `description`.
- Herramientas mínimas necesarias.
- `model: inherit` salvo razón documentada.
- `permissionMode: default`.
- Skills relevantes precargadas solo si son esenciales en cada ejecución.
- Cuerpo autocontenido.

## Reglas

1. No otorgues escritura a un agente que solo necesita leer.
2. No precargues todas las skills si pueden descubrirse bajo demanda.
3. La descripción debe indicar la intención del usuario y el momento de uso.
4. No dependas de rutas absolutas.
5. Valida el frontmatter.

## Validación

- Frontmatter parseable.
- Descripción específica.
- Permisos mínimos.
- Rutas relativas existentes.
- Agente invocable por nombre.

## Salida

- Adaptador Cursor.
- Adaptador Claude Code.
- Nota de herramientas y permisos.
