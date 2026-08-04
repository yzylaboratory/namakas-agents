---
name: disenar-arquitectura-modulos-web
description: Diseña la arquitectura de módulos/features del frontend web (límites, ownership, shared vs domain). Úsala cuando se estructure o reorganice una app web; no para apps nativas ni portal DX.
metadata:
  author: yzylabs
  version: "1.0"
---

# Diseñar arquitectura de módulos web

## Propósito

Definir una estructura de módulos mantenible: features, shared, design-system boundaries y ownership — evitando acoplamiento accidental y over-engineering.

## Entradas

- Dominios de producto / bounded contexts de UI.
- Equipos o owners actuales (si existen).
- Design system / librería de UI existente.
- Restricciones de monorepo/paquetes.
- Presión real de escala (multi-equipo, multi-deploy).

## Procedimiento

1. Identifica dominios de UI (no copies ciegamente carpetas legacy).
2. Propón capas: `app` (rutas), `features/*`, `shared` (utils/ui primitives), `design-system` (tokens/componentes base).
3. Declara reglas de dependencia (features no importan features hermanos; shared no conoce features).
4. Asigna ownership por feature.
5. Evalúa micro-frontends / federation **solo** si hay evidencia de equipos/deploy independientes; si no, rechaza con motivo.
6. Define puntos de extensión (slots, composition) frente a herencia de páginas monolíticas.
7. Lista migraciones incrementales si hay codebase existente.

## Salida

```md
## Mapa de módulos
## Reglas de dependencia
## Ownership
## Shared vs design-system
## Micro-frontends (sí/no + evidencia)
## Plan de migración (si aplica)
```

## Casos límite

- Un solo equipo pequeño → arquitectura modular simple; no federation.
- Design system inmaduro → boundary explícito + handoff a Miss Goldenweek/Perona.
- Features cruzadas por analytics → extrae shared intentional, no importa circular.

## Validación

- Reglas de dependencia son verificables (lint/path o convención documentada).
- Ownership no queda vacío.
- Micro-frontends justificados o explícitamente descartados.

## Criterios de terminado

- Un dev sabe dónde poner una feature nueva sin preguntar “en utils”.
- Deudas de acoplamiento tienen dueño y prioridad.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | App banking web 4 dominios | features + shared + reglas de import |
| Ambiguo | “Ordena el repo” | Preguntas de dominio + mapa candidato |
| Límite | Pedido de module federation sin multi-equipo | Rechazo documentado + alternativa modular |

## Fuentes

- Next.js App Router project structure — https://nextjs.org/docs/app/getting-started/project-structure (2026-08-04).
- React docs — thinking in components / composition — https://react.dev/learn/thinking-in-react (2026-08-04).
