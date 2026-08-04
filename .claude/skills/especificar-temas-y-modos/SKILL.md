---
name: especificar-temas-y-modos
description: Especifica temas y modos (light/dark/brand/density) reasignando tokens semánticos y validando contraste WCAG 2.2. Úsala cuando se pida dark mode, multi-marca o modos de densidad del design system.
metadata:
  author: yzylabs
  version: "1.0"
---

# Especificar temas y modos

## Propósito

Permitir variaciones de apariencia sin duplicar el árbol de tokens ni romper accesibilidad.

## Entradas

- Set semántico base aprobado.
- Modos solicitados (light, dark, high-contrast, brand A/B, comfortable/compact).
- Nivel WCAG objetivo (AA por defecto).
- Pares críticos de UI (texto/fondo, borde/fondo, focus, error/success).

## Procedimiento

1. Lista modos y su disparador (OS, usuario, marca, densidad).
2. Identifica qué semánticos cambian por modo; primitivos permanecen salvo brand pack.
3. Define tablas de remapeo semántico → primitivo por modo.
4. Calcula o registra contraste de pares críticos (1.4.3 texto; 1.4.11 no-texto ≥3:1).
5. Documenta anti-patrones (invertir hex a ciegas, same hue low contrast).
6. Especifica fallback si un modo no cubre un semántico.
7. Entrega matriz de modos + excepciones firmadas si algún par no alcanza AA.

## Salida

```md
## Modos
## Remapeo semántico por modo
## Matriz de contraste (pares críticos)
## Fallbacks
## Excepciones / riesgos
```

## Casos límite

- Solo piden “dark mode” sin semánticos → primero `definir-fundamentos-tokens`.
- Brand pack incompleto → marca modo `draft`; no apruebes GA.
- AAA pedido sin presupuesto → documenta costo de pares y escala a Nami.

## Validación

- Estructura de tokens idéntica entre modos (solo valores/aliases cambian).
- Pares críticos con ratio documentado.
- WCAG 2.2 citado; no inventar umbrales.

## Criterios de terminado

- Un tema se puede activar sin fork de componentes.
- Ningún par crítico AA queda sin medir o sin excepción explícita.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Light + dark sobre semánticos | Remapeo + matriz contraste |
| Ambiguo | “Que se vea bien de noche” | Preguntas de pares críticos + borrador dark |
| Límite | Dark falla 4.5:1 en body | Hallazgo + propuestas de primitivo; no aprobar |

## Fuentes

- WCAG 2.2 — https://www.w3.org/TR/WCAG22/ (1.4.3, 1.4.11; 2023-10-05; consultado 2026-08-04).
- DTCG 2025.10 theming / multi-brand capabilities — https://www.designtokens.org/tr/2025.10/ (consultado 2026-08-04).
- Material 3 light/dark color schemes — Android Material3 docs (consultado 2026-08-04).
