---
name: definir-estrategia-renderizado
description: Define la estrategia de renderizado por ruta (SSR, SSG, ISR, CSR, RSC/híbrido) con justificación. Úsala cuando se diseñe o cambie cómo se genera HTML/datos de una app web.
metadata:
  author: yzylabs
  version: "1.0"
---

# Definir estrategia de renderizado

## Propósito

Elegir, por ruta o flujo, el modo de renderizado que equilibre SEO, frescura de datos, personalización, TTFB y costo de compute — sin un interruptor global improvisado.

## Entradas

- Inventario de rutas / flujos críticos.
- Requisitos SEO, auth y personalización.
- Frecuencia de cambio de datos y tolerancia a staleness.
- Stack (p. ej. App Router / RSC) y restricciones de hosting/cache.

## Procedimiento

1. Lista rutas críticas y su audiencia (público SEO vs autenticado).
2. Para cada ruta, responde: ¿debe rankear? ¿datos idénticos para todos? ¿cambian entre deploys? ¿toleran revalidate? ¿requieren request-time data?
3. Asigna modo: SSG / ISR / SSR / CSR / RSC+streaming / híbrido (shell estático + islas).
4. Documenta triggers dinámicos (cookies, headers, searchParams, no-store) si aplica al framework.
5. Marca dónde `"use client"` (o equivalente) es obligatorio vs opcional.
6. Define cache/revalidate explícito cuando la frescura lo permita.
7. Lista riesgos (TTFB alto, drift de cache, JS excesivo) y métricas a observar.

## Salida

```md
## Matriz ruta → modo
| Ruta | Modo | SEO | Auth | Frescura | Justificación |
## Límites client/server
## Cache / revalidate
## Riesgos y métricas
```

## Casos límite

- Dashboard auth sin SEO → CSR o SSR personalizado; no fuerces SSG.
- Catálogo grande con updates frecuentes → ISR/revalidate antes que SSR puro.
- Marketing + widget personalizado → shell estático + isla client/stream.

## Validación

- Toda ruta crítica tiene modo + justificación.
- No hay “todo CSR” ni “todo SSR” sin evidencia.
- Fuentes de framework citadas cuando la decisión depende de ellas.

## Criterios de terminado

- Un implementador puede aplicar la matriz sin reinterpretar el intent.
- Gaps de hosting/cache tienen dueño (Sanji / DevOps).

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Landing + blog + dashboard auth | SSG/ISR públicos; CSR/SSR dashboard |
| Ambiguo | “Hazlo Next.js” | Preguntas SEO/auth + borrador de matriz |
| Límite | 10k productos con updates horarios | ISR/revalidate; no SSG full rebuild |

## Fuentes

- Next.js Rendering (App Router) — https://nextjs.org/docs/app/building-your-application/rendering (2026-08-04).
- React Server Components — https://react.dev/reference/rsc/server-components (2026-08-04).
- next.js Discussion #86106 hybrid scaling — https://github.com/vercel/next.js/discussions/86106 (2026-08-04).
