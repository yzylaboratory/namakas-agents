---
name: documentar-design-system
description: Documenta el design system para consumidores (fundamentos, uso de componentes, do/don't, changelog orientado a adopción). Úsala cuando se pida docs del DS, guidelines o preparar handoff a Perona/Frontend.
metadata:
  author: yzylabs
  version: "1.0"
---

# Documentar design system

## Propósito

Convertir tokens y APIs de componentes en guías accionables que reduzcan reinterpretación y tickets de “¿cómo se usa?”.

## Entradas

- Artefactos de tokens/temas/componentes aprobados.
- Audiencia (diseño, ingeniería, QA).
- Canal (MD en repo, Storybook, portal interno).
- Cambios recientes a comunicar.

## Procedimiento

1. Define audiencia y preguntas que debe responder la doc.
2. Estructura: fundamentos → temas → componentes → patrones → changelog.
3. Para cada componente: cuándo usarlo, anatomía, variantes, a11y, do/don't.
4. Enlaza tokens semánticos (nombres), no solo capturas.
5. Añade ejemplos mínimos de composición correcta e incorrecta.
6. Publica changelog orientado a impacto en consumidores.
7. Lista gaps de doc y dueños.

## Salida

```md
## Índice / audiencia
## Fundamentos (resumen + links a tokens)
## Temas / modos
## Componentes (fichas)
## Patrones
## Changelog
## Gaps
```

## Casos límite

- Solo hay mockups → documenta como `draft`; marca lo no tokenizado.
- Pedido de README de producto → escala/handoff a Vivi; tú docs del DS.
- Storybook vacío → docs MD primero; no inventes stories implementadas.

## Validación

- Cada ficha de componente apunta a tokens/estados reales.
- Do/don't no contradicen el API gobernado.
- Changelog menciona breaking si aplica.

## Criterios de terminado

- Un nuevo consumidor adopta un componente sin sesión 1:1.
- Gaps restantes están listados.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Button + tokens v1 | Ficha completa + do/don't |
| Ambiguo | “Documenta el DS” | Índice priorizado + MVP docs |
| Límite | Componente sin API estable | Doc draft + bloqueo de GA |

## Fuentes

- DTCG 2025.10 como contrato de intercambio de tokens — https://www.designtokens.org/tr/2025.10/ (consultado 2026-08-04).
- Spectrum / Material docs patterns (component options + guidelines) — spectrum-design-data / Material3 docs (consultado 2026-08-04).
