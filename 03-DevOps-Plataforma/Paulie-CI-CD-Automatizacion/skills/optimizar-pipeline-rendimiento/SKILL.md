---
name: optimizar-pipeline-rendimiento
description: Reduce duración y costo del pipeline (caché, paralelismo, path filters, fail-fast) midiendo antes/después. Úsala cuando el CI/CD sea lento o caro; no sacrifiques gates de seguridad por velocidad sin acuerdo explícito.
metadata:
  author: yzylabs
  version: "1.0"
---

# Optimizar rendimiento del pipeline

## Propósito

Acortar lead time de feedback de CI/CD sin degradar confiabilidad ni seguridad acordadas.

## Entradas

- Pipelines actuales y métricas (p50/p95 duración, cola, tasa de fallo).
- Cuellos de botella conocidos (tests, build, pulls de imagen).
- Límites de runners/minutos.
- Gates que no pueden relajarse.

## Procedimiento

1. Mide baseline: duración por job, tasa de cache hit, minutos facturables.
2. Identifica el critical path (jobs en serie que dominan el wall-clock).
3. Aplica path filters / conditional jobs para cambios irrelevantes.
4. Introduce caché de dependencias con keys estables y restore keys seguras.
5. Paraleliza suites independientes; serializa solo donde haya dependencia real.
6. Reordena fail-fast: barato primero.
7. Evalúa sharding de tests solo con evidencia de ganancia.
8. Compara after vs baseline; no declare victoria sin números.
9. Si la optimización toca un gate de seguridad, exige aprobación de Franky/Seguridad.

## Salida

```md
## Baseline
## Cambios aplicados
## Métricas after
## Trade-offs
## Riesgos
```

## Casos límite

- Cache que oculta roturas de lockfile → invalidación por hash de lock.
- Paralelismo que satura runners → documenta cola y costo.
- “Quita el SAST para ir más rápido” → rechaza o escala; no lo hagas solo.

## Validación

- Baseline y after con misma definición de éxito.
- Gates bloqueantes intactos o cambio aprobado.
- Cache keys documentadas.

## Criterios de terminado

- Reducción medible o explicación de por qué no hubo ganancia.
- Sin regresión de seguridad/calidad sin aceptación explícita.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | CI 25 min, npm install 12 min | Cache + baseline/after |
| Ambiguo | “Hazlo más rápido” | Medición primero + top 3 hipótesis |
| Límite | Pedido de quitar SAST | Rechazo/escala; alternativa (parallel SAST) |

## Fuentes

- GitHub Docs — Caching dependencies — https://docs.github.com/en/actions/using-workflows/caching-dependencies-to-speed-up-workflows (2026-08-04).
- GitLab Docs — Caching in GitLab CI/CD — https://docs.gitlab.com/ee/ci/caching/ (2026-08-04).
- DORA — Lead time for changes — https://dora.dev/ (2026-08-04).
