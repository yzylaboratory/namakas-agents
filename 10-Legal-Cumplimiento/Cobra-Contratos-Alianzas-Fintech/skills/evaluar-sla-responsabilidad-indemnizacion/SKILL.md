---
name: evaluar-sla-responsabilidad-indemnizacion
description: Diseña o audita SLA medibles, caps de liability, exclusiones e indemnizaciones en alianzas fintech. Úsala cuando haya que equilibrar riesgo operativo/regulatorio o cuando el partner proponga créditos simbólicos sin remedio real.
metadata:
  author: yzylabs
  version: "1.0"
---

# Evaluar SLA, responsabilidad e indemnización

## Propósito

Definir o revisar el paquete de performance y risk allocation: métricas SLA, medición, remedios, limitation of liability, exclusiones e indemnidades alineadas a una alianza fintech/plataforma.

## Entradas

- Borrador de SLA / liability / indemnification.
- Criticidad del servicio (customer-facing vs back-office).
- Dependencias bidireccionales (plataforma colaborativa vs vendor SaaS puro).
- Incidentes temidos (downtime, data breach, fraude, errores de pago).

## Procedimiento

1. Lista métricas SLA observables (disponibilidad, latencia, time-to-restore, soporte).
2. Define método de medición, ventana, exclusiones (force majeure, misuse) y reporting.
3. Asocia remedios (service credits, right to terminate, RCA obligatorio).
4. Revisa limitation of liability: cap, agregación, carve-outs (IP infringement, confidentiality, data/security breach, gross negligence, fraud).
5. Diseña indemnidades por lado (regulatory fines atribuibles, third-party claims, IP).
6. En colaboraciones bidireccionales, considera mutual SLAs / mutual dependencies (no solo vendor→cliente).
7. Marca créditos-only sin terminate right ante breach reiterado como riesgo material.
8. Produce ask / fallback / walk-away para cada punto controvertido.

## Salida

```md
## SLA propuesto
## Medición y exclusiones
## Remedios
## Liability map (cap + carve-outs)
## Indemnidades
## Asimetrías detectadas
## Posiciones de negociación
## Riesgos residuales
```

## Casos límite

- Partner ofrece solo “commercially reasonable efforts” → no aceptes como SLA; exige métricas o marca gap crítico.
- Cap igual a fees de 3 meses ante data breach → red flag; propone carve-out.
- Mutual platform → documenta obligaciones del banco/cliente que afectan el SLA del partner.

## Validación

- Cada métrica tiene método de medición.
- Carve-outs de seguridad/datos/negligencia grave están explícitos o listados como gap.
- No se confunde credit con indemnificación.

## Criterios de terminado

- Sengoku puede decidir si el risk allocation es aceptable.
- Walk-away conditions están escritas.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | 99.9% uptime + credits | SLA completo + remedios + gaps |
| Ambiguo | “Liability standard” sin números | Opciones de cap + preguntas |
| Límite | Exclusión total de damages por breach | Red flag + walk-away |

## Fuentes

- ABA — SaaS Agreements: Key Contractual Provisions (SLA, liability, indemnification) (2021-11) (2026-08-04).
- Mayer Brown — Collaboration Agreements… (mutual SLAs / customer experience metrics) (2025-11-21) (2026-08-04).
