---
name: integrar-automatizacion-ci
description: Integra o ajusta jobs de automatización en CI (smoke/regresión, artefactos, gates, comandos reproducibles). Úsala cuando las suites deban correr en pipeline, fallar el gate o publicar reportes.
metadata:
  author: yzylabs
  version: "1.0"
---

# Integrar automatización en CI

## Propósito

Hacer que las suites den señal confiable en el pipeline: triggers correctos, duración acotada, artefactos de fallo y umbrales de gate — sin rediseñar la plataforma CI/CD.

## Entradas

- Comando local de ejecución de suites.
- Distinción smoke vs regression.
- Runner disponible (OS, browsers, containers).
- Secretos/vars de entorno de test.
- Política de gate (block PR, nightly only).
- Owner de CI (Paulie / DevOps) si hay cambios de infraestructura.

## Procedimiento

1. Inventaría jobs existentes de test; no dupliques.
2. Define matriz mínima: smoke en PR; regression en nightly/main según costo.
3. Escribe/ajusta job: install → test → upload artifacts (JUnit/HTML/trace).
4. Asegura que el comando CI ≡ comando documentado local (mismas flags/tags).
5. Configura fail-fast o sharding solo si el framework y runners lo soportan.
6. Gates: qué job bloquea merge; qué es informativo.
7. Secretos vía store CI; nunca hardcode.
8. Si faltan runners/browsers/containers → `DELEGATION_REQUIRED` a plataforma CI (vía Usopp/Luffy).
9. Documenta troubleshooting: cómo bajar artifacts y reproducir.
10. Valida con un run real o dry-run de pipeline según permisos.

## Salida

```text
CI_TEST_INTEGRATION:
- jobs:
- triggers:
- commands:
- artifacts:
- gate_policy:
- secrets_required:
- local_repro:
LIMITATIONS:
```

## Casos límite

- Suite > presupuesto de tiempo de PR → mueve regression a nightly; deja smoke P0 en PR.
- Flaky conocidos en gate → no habilites gate hasta estabilizar o cuarentenar.
- Pedido de rediseñar Jenkins/GitHub runners → fuera de alcance; escala Paulie/DevOps.

## Validación

- Smoke acotado en tiempo razonable para el repo.
- Artefactos presentes en fallo.
- Sin secretos en YAML/logs de ejemplo.
- Gate policy explícita y aceptada por Usopp.

## Criterios de terminado

- Job definido o PR de CI listo.
- Evidencia de al menos un run (o bloqueo documentado de permisos).
- Guía de reproducción local.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Playwright + GitHub Actions | Job smoke PR + artifacts |
| Ambiguo | “Pon tests en CI” sin comando | Extrae comando del package/Makefile primero |
| Límite | Requiere farm de 50 browsers nuevos | DELEGATION_REQUIRED plataforma CI |

## Fuentes

- ISTQB CTAL-TAE v2.0 Cap. 5 Implementation and Deployment Strategies / CI pipelines (2024).
- Playwright CI docs (referencia del stack del repo; citar URL concreta al aplicar) — consultar docs oficiales del framework usado (2026-08-04).
