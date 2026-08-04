---
name: definir-partnership-monetizacion-light
description: Define patrones de partnership y monetización-light (tiers, cuotas, sandbox→prod, empaquetado). Úsala para alianzas API básicas; escala pricing/billing profundo a Du-Feld.
metadata:
  author: yzylabs
  version: "1.0"
---

# Definir partnership y monetización-light

## Propósito

Establecer el camino de partnership y el empaquetado light de acceso a APIs (tiers, rate limits, certificación) sin diseñar modelos financieros profundos.

## Entradas

- Producto de API y audiencias.
- Restricciones legales/comerciales conocidas.
- Capacidad de metering/gateway.
- Objetivos de ecosistema (adopción vs revenue).

## Procedimiento

1. Define etapas de partnership: apply → sandbox → certify → production → operate.
2. Por etapa, lista evidencia requerida (scopes, tests, contactos, compliance).
3. Propón tiers light (Free/Sandbox, Partner, Premium) con límites de cuota y soporte — sin precios finales.
4. Señala qué debe medir el gateway (calls, errores, latencia) para enforcement.
5. Documenta reglas de fair use y consecuencias de abuso (throttle, suspensión).
6. Identifica decisiones de monetización profunda (price points, revenue share, invoicing) y escala a Du-Feld.
7. Coordina con Koala qué del packaging es visible en portal pre/post login.
8. Entrega RACI light: Sabo (patrones), Du-Feld (pricing), Legal (contratos), Koala (UX portal).

## Salida

```md
## Etapas partnership
## Evidencia por etapa
## Tiers light (sin precios finales)
## Metering / fair use
## Handoff Du-Feld / Legal / Koala
## Riesgos
```

## Casos límite

- Partner estratégico sin self-service → flujo white-glove documentado + métricas iguales.
- Regulación prohíbe cobro en ciertos endpoints → separa APIs reguladas de value-added.
- Se pide “cuánto cobramos” → no inventes precios; produce handoff Du-Feld con drivers de valor.

## Validación

- Etapas y evidencia claras.
- Sin precios inventados.
- Dueños de monetización/legal/portal explícitos.
- Tiers alineados al producto de API.

## Criterios de terminado

- Patrón partnership usable por ops/portal.
- Handoff Du-Feld completo si hay revenue.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Partner fintech AIS | Sandbox→cert→prod + 3 tiers light + metering |
| Ambiguo | “Monetizar APIs” | Drivers de valor + handoff Du-Feld sin price list |
| Límite | API PSD2 gratuita + API enrich de pago | Separación regulatory vs commercial packaging |

## Fuentes

- Zuplo API-as-a-Product 2026 — https://zuplo.com/learning-center/api-as-a-product-guide-2026 (2026-08-04).
- Zuplo Fintech API Gateways 2026 (self-serve keys / tiers) — https://zuplo.com/learning-center/best-api-gateways-for-fintech-workloads-2026 (2026-08-04).
- Halkwinds Open Banking & API Economy Report 2026 — https://www.halkwinds.com/research/open-banking-api-economy-report-2026 (2026-08-04).
- Bamboodt API Management for Banks — https://www.bamboodt.com/building-a-secure-api-management-platform-for-banks-a-blueprint-for-open-banking-and-fintech-collaboration/ (2026-08-04).
