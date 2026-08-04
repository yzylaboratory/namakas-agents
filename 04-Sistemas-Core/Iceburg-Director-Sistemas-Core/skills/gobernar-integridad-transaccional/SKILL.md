---
name: gobernar-integridad-transaccional
description: Gobierna integridad transaccional del core (idempotencia, reconciliación, dual-run, auditoría). Úsala cuando se evalúe cutover, descuadres, reintentos o readiness de flujos de posting/pagos sobre el system of record.
metadata:
  author: yzylabs
  version: "1.0"
---

# Gobernar integridad transaccional

## Propósito

Asegurar que cambios en el core no rompan saldos, trazabilidad ni semántica de reintentos; definir gates de integridad antes de producción.

## Entradas

- Flujo(s) transaccionales afectados.
- Volúmenes y SLAs.
- Mecanismos actuales de idempotencia/reconciliación.
- Resultados de dual-run o pruebas, si existen.

## Procedimiento

1. Identifica unidades de trabajo: intent → authorization → posting → settlement/report.
2. Exige clave de idempotencia y semántica at-least-once vs exactly-once *efectiva* en el ledger.
3. Define reconciliación: fuentes A/B, umbral de breaks, owner, tiempo de resolución.
4. Para migraciones: dual-run con criterios de parity y plan de divergencia.
5. Exige auditoría inmutable / trace id end-to-end en flujos de alto valor.
6. Emite go/no-go de integridad con evidencia; si falta, `BLOCKED` o no-go explícito.

## Salida

```md
## Evaluación de integridad
- Flujos:
- Idempotencia:
- Reconciliación / breaks:
- Dual-run:
- Auditoría / trazas:
## Go / No-go
## Condiciones abiertas
## Riesgos residuales
```

## Casos límite

- Reintentos que crean doble posting: no-go hasta corregir clave/semántica.
- Breaks “aceptables” sin owner ni TTL: rechazar.
- Solo métricas de latencia sin reconciliación: insuficiente para cutover de ledger.

## Validación

- Hay criterio numérico o cualitativo verificable de integridad.
- Owner de breaks nombrado.
- Rollback o contención documentados.

## Criterios de terminado

- Decisión go/no-go justificada con evidencia.
- Pendientes accionables con dueño.
- Escalación a Kaku/Law/ops cuando corresponda.

## Fuentes

- `references/mapa-gobierno-sistemas-core.md` — gates (2026-08-04)
- Prácticas de pagos: idempotencia, dual-run, quarantine (síntesis contrastada, 2026-08-04)
- Swift — valor de datos estructurados ISO 20022 para STP/compliance (contexto, 2026-08-04)
