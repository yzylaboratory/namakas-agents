---
name: medir-salud-advocacy
description: Define y reporta métricas de salud comunitaria y advocacy basadas en comportamiento, no vanity. Úsala cuando haya que demostrar impacto de comunidad, auditar un dashboard o elegir KPI para rituales/embajadores.
metadata:
  author: yzylabs
  version: "1.0"
---

# Medir salud y advocacy

## Propósito

Elegir un set mínimo de señales conductuales que predicen retención/advocacy y reportarlas con honestidad metodológica — evitando member count y page views como único éxito.

## Entradas

- Objetivos de Morgans (retención, activación asistida por comunidad, contribución).
- Datos disponibles (analytics, community tools, CRM) o gaps.
- Definición de “éxito de producto” alineada con Carrot cuando aplique.
- Ventana y segmentos.

## Procedimiento

1. Lista métricas vanity actuales y márcalas como insuficientes solas.
2. Propón 3–5 señales conductuales, por ejemplo:
   - Tiempo a primera acción significativa (si hay datos; si no, handoff Carrot).
   - % retorno a comunidad/producto en 7 días.
   - Calidad de contribución (respuestas útiles, PRs, guías de miembros).
   - Progresión de engagement (lurker → pregunta → ayuda a otros → advocacy).
   - Referidos o activaciones atribuibles con método explícito.
3. Para cada métrica: definición, fuente, fórmula, owner, cadencia de reporte.
4. Define umbrales de “salud” solo con baseline o como hipótesis.
5. Conecta narrativa a outcome de negocio sin exagerar causalidad.
6. Documenta lo que **no** se puede afirmar aún.
7. Entrega tablero mínimo + preguntas de instrumentación.

## Salida

```md
# Tablero salud/advocacy — [producto]

## Vanity a no usar como éxito único
- …

## KPI conductuales
| Métrica | Definición | Fuente | Fórmula | Owner | Cadencia |
|---|---|---|---|---|---|

## Lectura actual
- … (datos o “sin baseline”)

## Vínculo a outcome
- Hipótesis: …
- Evidencia: …
- No causalidad no demostrada: …

## Gaps de instrumentación
- …

## Riesgos de gaming
- …
```

## Casos límite

- Sin instrumentación: tablero como especificación; STATUS puede ser `COMPLETED_WITH_LIMITATIONS`.
- Presión ejecutiva por vanity: reporta vanity en anexo, lidera con conductuales.
- Atribución multi-touch imposible: usa cohortes/proxies y declara límites.
- Comunidad financiera: no uses engagement engañoso (bots, giveaways de leads sensibles).

## Validación

- ≥3 métricas conductuales definidas o gaps explícitos.
- Cada métrica tiene fuente/fórmula/owner.
- Causalidad no exagerada.
- Gaming risks listados.

## Criterios de terminado

- Tablero mínimo entregado.
- Método reproducible.
- Claro qué decidirá Morgans con estos números.

## Fuentes

- Stateshift CLG — behavioral signals (TTFV, 7-day return, feature progression) vs vanity (Nov 2025); consultado 2026-08-04.
- Stateshift / industry DevRel — proving impact with data as top challenge; consultado 2026-08-04.
