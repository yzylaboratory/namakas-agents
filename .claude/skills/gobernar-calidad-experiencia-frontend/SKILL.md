---
name: gobernar-calidad-experiencia-frontend
description: Define y aplica gobierno de calidad de experiencia (WCAG, Core Web Vitals / perf móvil, design system, DoD, CI gates). Úsala cuando se pidan estándares frontend, políticas de a11y/performance, budgets o Definition of Done de UI.
metadata:
  author: yzylabs
  version: "1.0"
---

# Gobernar calidad de experiencia Frontend

## Propósito

Convertir accesibilidad, rendimiento y consistencia en políticas operativas con dueños, umbrales y guardrails — no en auditorías de último minuto.

## Entradas

- Superficies / canales en alcance.
- Nivel de conformidad a11y objetivo (p. ej. WCAG 2.2 AA).
- Telemetría existente (RUM, Lighthouse, crashes) o ausencia de ella.
- Estado del design system (tokens, versionado, adopción).

## Procedimiento

1. Fija el **objetivo de conformidad** a11y (versión WCAG + nivel) y el alcance (páginas/apps).
2. Fija **umbrales de performance** por canal:
   - Web: LCP ≤ 2.5s, INP ≤ 200ms, CLS ≤ 0.1 (p75), citando Web Vitals.
   - Móvil: métricas nativas acordadas (startup, frames, crash-free); no copies CWV ciegamente.
3. Define DoD frontend mínimo: semántica/teclado, contraste, estados de error, budgets, sin regresiones de DS.
4. Diseña guardrails: lint/a11y en CI, budgets de bundle, checks de tokens; lista excepciones con expiry.
5. Asigna ownership por superficie y plan de remediación de deuda (Now/Next).
6. Exige evidencia de campo (RUM) para releases críticos; lab no sustituye campo.
7. Escala Legal si hay obligación regulatoria de accesibilidad; Sanji aporta marco técnico, no dictamen.

## Salida

```md
## Política de calidad Frontend
- WCAG objetivo / alcance:
- Umbrales perf (web / móvil):
## DoD Frontend
## Guardrails CI / RUM
## Ownership por superficie
## Deuda y plan de remediación
## Excepciones documentadas
## Escalaciones
```

## Casos límite

- Sin RUM: política con plan de instrumentación; no fingir cumplimiento de campo.
- Design system inexistente: gobierno mínimo (tokens + componentes críticos) antes de policías de adopción.
- WCAG 3 draft: no lo uses como requisito normativo; preferir WCAG 2.2 estable.

## Validación

- Umbrales citados con fuente.
- DoD es verificable en PR/release.
- Hay dueño por superficie crítica.

## Criterios de terminado

- Política aplicable por el squad sin reinterpretar “calidad”.
- Gates y excepciones explícitos.

## Fuentes

- W3C WCAG 2.2 — https://www.w3.org/TR/WCAG22/ (2026-08-04)
- W3C WAI WCAG overview — https://www.w3.org/WAI/standards-guidelines/wcag/ (2026-08-04)
- Google web.dev Web Vitals — https://web.dev/articles/vitals (actualizado 2024-10-31; consultado 2026-08-04)
- Smashing Magazine — a11y as operational capability — 2026-06
