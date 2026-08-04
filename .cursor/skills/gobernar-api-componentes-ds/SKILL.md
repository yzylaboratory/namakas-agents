---
name: gobernar-api-componentes-ds
description: Define el API del design system para componentes reutilizables (variantes, estados, props/slots y tokens consumidos). Úsala cuando se pida especificar o gobernar componentes del sistema, no pantallas de producto.
metadata:
  author: yzylabs
  version: "1.0"
---

# Gobernar API de componentes del design system

## Propósito

Tratar cada componente del sistema como un contrato estable consumible por diseño e implementación.

## Entradas

- Nombre del componente y problema que resuelve.
- Tokens semánticos / temas disponibles.
- Requisitos de accesibilidad (teclado, focus, ARIA mínima a nivel de spec).
- Inventario existente o referencias (Spectrum schemas, Material components).

## Procedimiento

1. Decide inclusión: ¿es sistema (reutilizable ≥2 contextos) o one-off de producto? (one-off → Perona).
2. Define anatomía (partes) y slots/props públicos.
3. Enumera variantes y estados (default, hover, focus, disabled, error, loading…).
4. Mapea cada parte/estado a tokens semánticos (no hex).
5. Declara do/don't de composición y contenido.
6. Especifica criterios a11y de componente (focus visible, contraste no-texto, no color-only).
7. Define versionado del contrato (additive vs breaking).
8. Prepara handoff a Frontend (spec, no implementación obligatoria).

## Salida

```md
## Componente
## Inclusión (sistema vs one-off)
## Anatomía / props / slots
## Variantes y estados
## Tokens por parte/estado
## A11y checklist
## Do / Don't
## Handoff implementación
```

## Casos límite

- Pedido de pantalla completa como “componente” → rechaza; divide o escala a Perona.
- Variantes explosivas → consolida en props ortogonales.
- Sin tokens semánticos → bloquea API; ejecuta fundamentos primero.

## Validación

- Ningún estado crítico sin token o regla explícita.
- Breaking props marcados.
- Frontera clara vs UI de producto.

## Criterios de terminado

- Diseño e ingeniería pueden implementar el mismo componente sin reinterpretar.
- One-offs no contaminan el inventario del sistema.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Button primary/secondary | API + estados + tokens |
| Ambiguo | “Componente de dashboard” | Preguntas; posible rechazo one-off |
| Límite | 12 variantes visuales sin props | Rediseño a 3 variantes × props |

## Fuentes

- Adobe Spectrum component schemas / design-data — https://github.com/adobe/spectrum-design-data (consultado 2026-08-04).
- Material 3 component theming customization patterns — Android Material3 docs (consultado 2026-08-04).
- WCAG 2.2 focus/contrast related SCs — https://www.w3.org/TR/WCAG22/ (consultado 2026-08-04).
