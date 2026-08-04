---
name: medir-rendimiento-entrega-dora
description: Define y evalúa métricas de entrega DORA (deployment frequency, lead time, change failure rate, time to restore) y señales de plataforma/DevEx asociadas. Úsala cuando se pida baseline DORA, scorecard de entrega, o evidencia de impacto de la plataforma en throughput y estabilidad.
metadata:
  author: yzylabs
  version: "1.0"
---

# Medir rendimiento de entrega (DORA)

## Propósito

Establecer definiciones operativas, fuentes de datos y lectura equilibrada de velocidad vs estabilidad — sin vanity metrics ni umbrales inventados.

## Entradas

- Alcance (equipo, dominio, plataforma vs apps).
- Fuentes disponibles (CI/CD, deploys, incidentes, repos).
- Periodo de medición y supuestos de “producción”.
- Cambios recientes de plataforma que se quieran atribuir.

## Procedimiento

1. Fija el perímetro y la definición de “deployment a producción” y “failure/incidente”.
2. Declara las four keys con fórmula y fuente:
   - Deployment frequency.
   - Lead time for changes.
   - Change failure rate.
   - Time to restore service / failed deployment recovery time.
3. Separa scorecard de **plataforma** (adopción, task success, clear feedback) vs **equipos de aplicación**.
4. Recoge baseline (aunque sea parcial) y marca gaps de instrumentación.
5. Interpreta balance velocidad/estabilidad; evita optimizar una key a costa de otra sin decisión explícita.
6. Si cites bandas elite/high/medium/low, indica año/reporte o márcalo como ilustrativo no normativo.
7. Propón 2–5 acciones de plataforma que muevan las keys con dueño (célula).

## Salida

```md
## Perímetro y definiciones
## Scorecard DORA
| Métrica | Valor | Fuente | Confianza | Gap |
## Señales DevEx / adopción
## Lectura (velocidad vs estabilidad)
## Acciones propuestas
## Riesgos de medición
```

## Casos límite

- Sin datos de incidentes: no inventes change failure rate; reporta gap y proxy temporal documentado.
- Multi-repo / multi-pipeline: define reglas de agregación antes de comparar equipos.
- Mejora de coding AI sin mejora de deploy: señala bottleneck downstream (tesis DORA 2025).

## Validación

- Cada métrica tiene definición + fuente o gap explícito.
- No se declara “elite” sin evidencia y contexto de umbral.
- Acciones mapean a dueños del squad.

## Criterios de terminado

- Scorecard usable para Luffy y el departamento.
- Gaps de instrumentación priorizables.
- Interpretación equilibrada documentada.

## Fuentes

- DORA — platform engineering & measurement — https://dora.dev/capabilities/platform-engineering/ (consultado 2026-08-04)
- DORA four keys / Four Keys project — https://github.com/dora-team/fourkeys (METRICS.md; consultado 2026-08-04)
- DORA research hub — https://dora.dev/ (consultado 2026-08-04)
