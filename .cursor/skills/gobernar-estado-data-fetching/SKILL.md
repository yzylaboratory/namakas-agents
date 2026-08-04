---
name: gobernar-estado-data-fetching
description: Gobierna estado (servidor, URL, cliente) y patrones de data-fetching/cache en apps web. Úsala cuando haya stores globales, waterfalls o duda sobre dónde vive el estado.
metadata:
  author: yzylabs
  version: "1.0"
---

# Gobernar estado y data-fetching

## Propósito

Asignar cada pieza de estado al lugar correcto y definir fetching/cache/revalidación para evitar stores globales innecesarios y waterfalls.

## Entradas

- Flujos interactivos y formularios.
- Datos de servidor ya modelados (BFF/RSC).
- Necesidades de deep-linking / shareable URL.
- Librerías de estado existentes (si hay).

## Procedimiento

1. Clasifica estado: servidor (fuente de verdad remota), URL (filtros/navegación), cliente efímero (UI local), cliente durable (preferencias).
2. Prefiere URL para estado compartible; servidor para datos de dominio; cliente solo para UI efímera.
3. Define fetching: dónde ocurre, paralelismo, Suspense/streaming, error boundaries.
4. Define cache/revalidate/invalidación y quién dispara mute.
5. Rechaza store global por defecto; justifica si se introduce (cross-route client state real).
6. Documenta anti-patrones (duplicar server state en client sin sync).
7. Alinea con matriz de renderizado y límites BFF.

## Salida

```md
## Clasificación de estado
## Política de fetching
## Cache / invalidación
## Stores (sí/no + alcance)
## Anti-patrones prohibidos
```

## Casos límite

- Wizard multi-step → estado URL o session controlado; no localStorage sensible.
- Optimistic UI → delimitado; rollback y fuente de verdad claros.
- Legacy Redux monolítico → plan de reducción incremental, no big-bang sin mandato.

## Validación

- Cada tipo de estado tiene home explícito.
- No hay duplicación injustificada server↔client.
- Invalidación tiene dueño de evento.

## Criterios de terminado

- Un implementador sabe qué poner en URL vs store vs server.
- Waterfalls conocidos tienen remediación o aceptación documentada.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Lista + filtros + detalle | Filtros en URL; detalle server-fetch |
| Ambiguo | “Ponemos Zustand para todo” | Rechazo parcial + mapa de estado mínimo |
| Límite | Form con PII en draft | No localStorage; sesión server/BFF |

## Fuentes

- Next.js Data Fetching — https://nextjs.org/docs/app/building-your-application/data-fetching (2026-08-04).
- React — Managing State — https://react.dev/learn/managing-state (2026-08-04).
- web.dev — INP (interactivity budgets) — https://web.dev/articles/inp (2026-08-04).
