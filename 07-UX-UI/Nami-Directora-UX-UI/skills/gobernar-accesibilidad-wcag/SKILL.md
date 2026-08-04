---
name: gobernar-accesibilidad-wcag
description: Gobierna accesibilidad a nivel director con WCAG 2.2 (objetivo AA), método de evaluación y gates by design. Úsala cuando se pida plan a11y, conformidad objetivo, revisión de accesibilidad de producto o política departamental.
metadata:
  author: yzylabs
  version: "1.0"
---

# Gobernar accesibilidad WCAG

## Propósito

Definir y aplicar gobierno de accesibilidad de producto/proceso alineado a WCAG 2.2, sin emitir certificación legal.

## Entradas

- Producto/flujos en alcance y plataformas (web, móvil, docs).
- Objetivo de conformidad (default: WCAG 2.2 AA) o mandato distinto.
- Estado del design system y componentes.
- Resultados previos de auditorías o linters.
- Jurisdicción si hay presión regulatoria (solo para escalamiento).

## Procedimiento

1. Fija estándar: **WCAG 2.2** + nivel (**AA** salvo excepción documentada) + alcance.
2. Mapea principios POUR (perceivable, operable, understandable, robust) a gates de producto.
3. Exige a11y by design en intake de patrones/componentes (Miss Goldenweek) y en UI (Perona).
4. Define método de evaluación mixto:
   - automático (baseline, no suficiente solo)
   - manual (teclado, SR smoke, contraste, foco)
   - usuarios con discapacidad cuando el riesgo lo justifique (vía Chopper / especialistas)
5. Clasifica gaps por severidad y criterio WCAG (ID de success criterion cuando sea posible).
6. Separa: deuda de sistema vs deuda de pantalla vs contenido.
7. Si hay EAA / EN 301 549 / política legal: escala a Legal con el mapa de gaps; no firmes conformidad.
8. Produce plan Now/Next con dueños y criterio de “hecho”.

## Salida

```md
## Gobierno de accesibilidad
- Estándar / nivel / alcance:
- Método de evaluación:
## Gaps
| SC (si conocido) | Problema | Severidad | Capa (sistema/UI/contenido) | Dueño |
## Plan Now/Next
## Lo que NO se afirma (no certificación)
## Escalamiento legal (si aplica)
```

## Casos límite

- Solo linter verde: insuficiente; documentar límites del método.
- WCAG 3 draft: no usar como requisito de conformidad; mencionar solo como horizonte.
- App nativa: aplicar orientación WCAG2ICT; no fingir cobertura web idéntica.

## Validación

- Versión y nivel WCAG explícitos.
- Método de evaluación declarado.
- Sin afirmación de “100% conforme” sin evidencia proporcional.
- Legal escalado cuando hay mandato regulatorio.

## Criterios de terminado

- Política/plan accionable para el squad y Frontend.
- Gaps priorizados con dueños.
- Límites legales explícitos.

## Fuentes

- W3C WAI — WCAG 2 Overview — https://www.w3.org/WAI/standards-guidelines/wcag/ (2026-08-04)
- W3C — Web Content Accessibility Guidelines (WCAG) 2.2 — https://www.w3.org/TR/WCAG22/ (2026-08-04)
- W3C — How to Meet WCAG 2 (Quick Reference) — https://www.w3.org/WAI/WCAG22/quickref/ (2026-08-04)
- ISO/IEC 40500:2025 — WCAG 2.2 como estándar ISO (nota WAI) — consultado 2026-08-04
- EN 301 549 / EAA — referencia de escalamiento legal (no dictamen) — consultado 2026-08-04
