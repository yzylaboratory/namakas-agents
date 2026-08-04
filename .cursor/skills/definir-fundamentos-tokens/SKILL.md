---
name: definir-fundamentos-tokens
description: Define la taxonomía y el set de design tokens (primitivo → semántico → componente) en formato alineado a DTCG 2025.10. Úsala cuando se pida crear o reestructurar fundamentos del design system, no pantallas sueltas.
metadata:
  author: yzylabs
  version: "1.0"
---

# Definir fundamentos y tokens

## Propósito

Establecer la fuente de verdad de decisiones de diseño como tokens intercambiables, con capas claras y sin hex sueltos en el core del sistema.

## Entradas

- Marca / producto / plataformas objetivo.
- Brand guidelines o tokens legacy (si existen).
- Dominios a cubrir (color, type, space, radius, elevation, motion…).
- Restricciones de naming y tooling (Style Dictionary, Tokens Studio, etc.).

## Procedimiento

1. Inventaría tokens existentes y clasifícalos (primitivo / semántico / componente / huérfano).
2. Define naming convention y grupos DTCG (`$type`, aliases `{token.path}`).
3. Modela primitivos (escalas raw) sin semántica de UI.
4. Modela semánticos (roles: `color.text.primary`, `space.inset.md`) aliasando primitivos.
5. Define tokens de componente solo cuando el componente necesite override controlado.
6. Declara qué queda fuera (ilustraciones one-off, marketing no sistemático).
7. Produce artefacto JSON/YAML compatible con Design Tokens Format Module 2025.10 o tabla equivalente si el repo aún no tiene pipeline.
8. Lista gaps y riesgos (contraste, multi-marca, densidad).

## Salida

```md
## Alcance de fundamentos
## Naming / grupos
## Primitivos
## Semánticos
## Componente (si aplica)
## Artefacto tokens (ruta o bloque)
## Fuera de alcance
## Riesgos / pendientes
```

## Casos límite

- Solo hay hex en Figma → no copies planos; propone capas semánticas primero.
- Multi-marca → mismos nombres semánticos; primitivos/brand por tema.
- Pedido de “todos los colores Material” → acota a roles usados; no infles el set.

## Validación

- Tres capas distinguibles.
- Semánticos no duplican literales sin alias.
- Tipos DTCG coherentes (`color`, `dimension`, `typography`, etc.) cuando hay artefacto.
- Fuente DTCG 2025.10 citada.

## Criterios de terminado

- Un consumidor sabe qué token usar sin preguntar “qué hex es el primary”.
- No quedan primitivos expuestos como API pública del sistema sin justificación.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Nueva app con brand book | Taxonomía 3 capas + set semántico inicial |
| Ambiguo | “Ponemos tokens” | Preguntas de plataformas + borrador mínimo color/type/space |
| Límite | 400 hex flat en legacy | Plan de migración por capas; no dump 1:1 |

## Fuentes

- DTCG Design Tokens Format Module 2025.10 — https://www.designtokens.org/tr/2025.10/ (2025-10-28; consultado 2026-08-04).
- Material 3 token roles (reference/system/component) — Android Material3 theming docs (consultado 2026-08-04).
