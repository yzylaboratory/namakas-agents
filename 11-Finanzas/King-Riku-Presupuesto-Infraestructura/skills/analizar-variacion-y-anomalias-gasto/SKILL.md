---
name: analizar-variacion-y-anomalias-gasto
description: Analiza variances presupuesto/forecast vs actual y define detección/respuesta a anomalías de gasto de infraestructura. Úsala cuando haya overspend, underspend o picos inexplicados — no para reconciliar asientos contables.
metadata:
  author: yzylabs
  version: "1.0"
---

# Analizar variación y anomalías de gasto

## Propósito

Explicar desviaciones materiales del plan y establecer guardrails para detectar y responder a anomalías de consumo/costo a tiempo.

## Entradas

- Actual vs presupuesto y/o forecast del periodo.
- Serie temporal de costo/uso.
- Cambios conocidos (releases, migraciones, incidentes, commits).
- Umbrales vigentes (si existen).
- Owners por scope.

## Procedimiento

1. Cuantifica variance absoluta y % por dimensión (servicio, equipo, entorno).
2. Clasifica drivers: uso, tarifa/precio, mix, one-off/crédito, error de allocation.
3. Separa “esperado por roadmap” de “anomalía”.
4. Define o aplica umbrales (desviación vs baseline/forecast) y severidad.
5. Diseña playbook: alert → triage owner → contención → postmortem de costo.
6. Propón acciones (freeze no-prod, ticket a plataforma, ajuste de forecast).
7. Documenta falsos positivos conocidos (billing delays, credits, tax).
8. Escala overspend estructural a Denjiro con opciones cuantificadas.

## Salida

```md
## Variance resumen
## Drivers por dimensión
## Anomalías vs esperados
## Umbrales y severidad
## Playbook de respuesta
## Acciones y dueños
## Impacto en forecast/presupuesto
## Riesgos
```

## Casos límite

- Billing delayed/incomplete → marca datos provisionales; no cierres “ahorro”.
- Pico por incident scale-out → documenta como one-off + costo de resiliencia.
- Underspend grande → investiga freze de entrega o forecast inflado; no celebres sin contexto.

## Validación

- Cada variance material tiene driver y owner.
- Playbook tiene pasos y responsables.
- No se confunde con conciliación contable (Gild Tesoro).
- Hechos vs hipótesis etiquetados.

## Criterios de terminado

- Denjiro/ingeniería saben qué pasó, por qué y qué hacer en 24–72h.
- Ajustes a forecast/presupuesto quedan explícitos.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | +35% compute vs forecast | Drivers + owner + acciones |
| Ambiguo | “El cloud está caro” | Desglose por dimensión + top 3 drivers |
| Límite | Alerta diaria por credits/tax noise | Retune umbrales + exclusiones documentadas |

## Fuentes

- FinOps Framework — Anomaly Management — https://www.finops.org/framework/capabilities/anomaly-management/ (consultado 2026-08-04).
- FinOps Framework — Budgeting / Reporting & Analytics — https://www.finops.org/framework/capabilities/ (2026).
