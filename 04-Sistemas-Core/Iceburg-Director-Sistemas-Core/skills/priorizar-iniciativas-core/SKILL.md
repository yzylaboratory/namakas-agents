---
name: priorizar-iniciativas-core
description: Prioriza el backlog de Sistemas Core con valor, dependencia técnica y riesgo de cutover. Úsala cuando haya que ordenar iniciativas de modernización, integración o integridad transaccional del core.
metadata:
  author: yzylabs
  version: "1.0"
---

# Priorizar iniciativas Core

## Propósito

Ordenar el backlog departamental con criterios explícitos y gates, evitando priorizar por moda tecnológica o presión sin evidencia.

## Entradas

- Backlog candidato (épicas/iniciativas).
- Capacidad del squad y ventanas de cambio.
- Métricas actuales (breaks, latencia, incidentes).
- Dependencias externas (rails, Arquitectura, Backend, OB).

## Procedimiento

1. Normaliza cada ítem: objetivo, capa de core, valor, dependencia, riesgo cutover, esfuerzo relativo.
2. Aplica scoring simple y transparente (no caja negra): Valor × Urgencia / (Riesgo × Esfuerzo), ajustado por dependencias bloqueantes.
3. Separa Must-now (integridad/incidente/mandato) de Should/Could.
4. Verifica gates previos: no priorices cutover si faltan reconciliación, idempotencia u ownership.
5. Asigna dueño (Crocus/Tom/Kaku/Iceburg) y criterio de salida.
6. Publica Now / Next / Later y lo que queda explícitamente fuera.

## Salida

```md
## Backlog priorizado Sistemas Core
| Rank | Iniciativa | Valor | Deps | Riesgo | Dueño | Gate | Now/Next/Later |
## Fuera de alcance este ciclo
## Capacidad y supuestos
## Riesgos de priorización
```

## Casos límite

- Dos cutovers sobre el mismo ledger path: serializar; un solo owner.
- Presión de negocio vs riesgo de descuadre: documentar trade-off y escalar a Luffy.
- Célula stub: prioriza igual pero marca ejecución como `DELEGATION_REQUIRED`.

## Validación

- Cada ítem Now tiene dueño, gate y dependencia explícita.
- No hay dos Must-now mutuamente excluyentes sin secuencia.
- Riesgos de integridad están visibles en el top del backlog.

## Criterios de terminado

- Backlog accionable para el squad y para Luffy.
- Justificación reproducible del orden.
- Escalaciones claras donde el riesgo exceda el mandato.

## Fuentes

- `references/mapa-gobierno-sistemas-core.md` — gates de cutover (2026-08-04)
- Prácticas de priorización operativa bancaria / coexistencia (síntesis contrastada, 2026-08-04)
