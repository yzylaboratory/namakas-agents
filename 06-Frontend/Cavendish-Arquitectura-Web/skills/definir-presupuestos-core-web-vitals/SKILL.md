---
name: definir-presupuestos-core-web-vitals
description: Define presupuestos LCP/INP/CLS y plan de medición lab+field para rutas web críticas. Úsala cuando se fijen SLOs de rendimiento percibido o se evalúe impacto arquitectónico en CWV.
metadata:
  author: yzylabs
  version: "1.0"
---

# Definir presupuestos Core Web Vitals

## Propósito

Traducir arquitectura web en presupuestos medibles de experiencia (LCP, INP, CLS) con umbrales oficiales y plan de medición.

## Entradas

- Rutas críticas user-facing.
- Matriz de renderizado (si existe).
- Telemetría actual (CrUX, RUM, Lighthouse) si hay.
- Restricciones de third-parties (tags, embeds).

## Procedimiento

1. Selecciona rutas del journey crítico (entrada, conversión, post-login clave).
2. Aplica umbrales “good” @ p75: LCP ≤ 2.5s, INP ≤ 200ms, CLS ≤ 0.1 (web.dev).
3. Relaciona riesgos arquitectónicos: LCP (SSR/SSG, images, fonts), INP (JS client, handlers largos), CLS (reservas de espacio, fonts).
4. Define medición lab (Lighthouse/DevTools) y field (CrUX/RUM); no sustituyas una por la otra.
5. Fija presupuestos de JS third-party y dueños.
6. Define gates: qué regresión bloquea merge vs backlog.
7. Lista remediaciones priorizadas (arquitectura primero, micro-opts después).

## Salida

```md
## Rutas críticas
## Presupuestos LCP/INP/CLS
## Lab vs field
## Riesgos por arquitectura
## Gates y dueños
## Remediación priorizada
```

## Casos límite

- Sin telemetría field → presupuestos + plan de instrumentación; no inventes “ya estamos bien”.
- Solo marketing pages → enfoca LCP/CLS; INP sigue documentado.
- Heavy dashboard auth → INP prioritario; SEO/LCP de marketing no aplica igual.

## Validación

- Umbrales citados a web.dev (no inventados).
- Cada ruta crítica tiene presupuesto y dueño de regresión.
- Third-parties tienen presupuesto o veto.

## Criterios de terminado

- El equipo puede medir y fallar un PR/release por CWV con criterio explícito.
- Gaps de RUM/CrUX tienen dueño (Sanji / Observabilidad).

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Landing + checkout | Presupuestos p75 + riesgos LCP/CLS |
| Ambiguo | “Hazlo rápido” | Preguntas de rutas + borrador de budgets |
| Límite | Tag manager sin dueño | Cap de third-party + escalamiento |

## Fuentes

- web.dev Web Vitals — https://web.dev/articles/vitals (2026-08-04).
- web.dev Defining CWV thresholds — https://web.dev/articles/defining-core-web-vitals-thresholds (2026-08-04).
- web.dev LCP — https://web.dev/articles/lcp (2026-08-04).
- web.dev INP — https://web.dev/articles/inp (2026-08-04).
- web.dev CLS — https://web.dev/articles/cls (2026-08-04).
