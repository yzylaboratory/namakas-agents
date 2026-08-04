---
name: definir-metrica-valor-api
description: Define la value metric y dimensiones de medición para cobro de APIs (txn, tokens, registros, compute). Úsala al elegir qué contar; no para fijar el price list completo.
metadata:
  author: yzylabs
  version: "1.0"
---

# Definir métrica de valor de API

## Propósito

Elegir la unidad de cobro que el partner entiende, controla y correlaciona con valor — base del metering.

## Entradas

- Caso de uso y percepción de valor del cliente.
- Modelo de pricing candidato (o borrador).
- Capacidad de telemetría/gateway.
- Cost drivers técnicos (compute, storage, third-party calls).

## Procedimiento

1. Lista candidatos de métrica (calls, txns exitosas, registros, tokens, compute-minutos, seats+usage).
2. Evalúa cada candidata: alineación a valor, predictibilidad, fraudabilidad, costo de instrumentar.
3. Elige métrica primaria; documenta secundarias solo si el híbrido multi-meter está justificado.
4. Define reglas: qué evento cuenta, exclusiones (health checks, 401, retries idempotentes), ventana de agregación.
5. Define atribución: tenant, aplicación, partner, agent-id si hay consumo máquina.
6. Exige UX de consumo: dashboard + alertas 75/90/100% (o umbrales acordados).
7. Señala si hace falta multi-meter (rompe Stripe simple → plataformas tipo Metronome/Orb/Lago).
8. Entrega contrato de métrica usable por metering y por portal.

## Salida

```md
## Métrica primaria
## Dimensiones / atribución
## Reglas de conteo y exclusiones
## Alertas y visibilidad
## Multi-meter (sí/no) y implicación de plataforma
## Riesgos de gaming
```

## Casos límite

- Cobrar calls brutos infla factura por polling → preferir txns de negocio.
- AI/token pricing aterroriza buyers → considera créditos con mapeo transparente.
- Free tier abused por key sharing → métrica + enforcement + identidad.

## Validación

- Partner puede estimar gasto con la métrica elegida.
- Exclusiones de retry/health documentadas.
- Alineada al modelo de pricing.
- Gaming risks listados.

## Criterios de terminado

- Contrato de métrica implementable por metering.
- Alertas definidas.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Payments status API | Métrica = consultas de estado exitosas por cuenta |
| Ambiguo | “Cobra por uso” | 2–3 candidatas + recomendación + trade-offs |
| Límite | LLM wrapper API | Créditos o tokens con cache-hit discount documentado |

## Fuentes

- Moesif API Pricing 2026 — https://www.moesif.com/blog/api-monetization/api-pricing/ (2026-08-04).
- ScaleDrone How to Price Your API — https://www.scaledrone.com/blog/how-to-price-your-api/ (2026-08-04).
- Dodo Payments API Monetization — https://dodopayments.com/blogs/api-monetization (2026-08-04).
