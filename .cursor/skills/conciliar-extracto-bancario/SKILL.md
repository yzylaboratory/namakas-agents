---
name: conciliar-extracto-bancario
description: Concilia libro interno vs extracto bancario (camt.052/053/054 u homologados), separando timing, matched y breaks. Úsala cuando se pida bank reconciliation, proof of cash o cuadre de saldos de efectivo.
metadata:
  author: yzylabs
  version: "1.0"
---

# Conciliar extracto bancario

## Propósito

Explicar diferencias entre saldo de libros y saldo de extracto con ítems reconciliatorios y cola de excepciones auditable.

## Entradas

- Periodo y cuenta(s) bancaria(s).
- Extracto (camt.053 EOD, camt.052 intradía, camt.054, MT940/950 u export propietario).
- Mayor / journal de caja del mismo periodo.
- Políticas de tolerancia y cutoff.
- Responsables (preparador / revisor).

## Procedimiento

1. Fija saldos iniciales y finales (banco vs libro) y moneda.
2. Normaliza movimientos a estructura común: fecha valor, booking, monto, D/C, referencia, contraparte, fuente.
3. Ejecuta matching por referencia estructurada primero; luego monto+fecha con tolerancia explícita.
4. Clasifica ítems solo en banco (fees, intereses, cheques cobrados) vs solo en libro (outstanding, deposits in transit).
5. Separa timing differences de errores, duplicados y sospecha de fraude.
6. Produce proof-of-cash ligero si el riesgo o el cierre lo exige (flujos del periodo, no solo saldo final).
7. Lista breaks abiertos con aging y dueño; no declares 100% matched ocultando unmatched.

## Salida

```md
## Alcance / periodo / cuenta
## Saldos banco vs libro
## Matched
## Reconciling items (timing)
## Breaks (clasificación + aging)
## Ajustes propuestos
## Evidencia de control (preparador/revisor)
## Riesgos / pendientes
```

## Casos límite

- Formatos mixtos (camt + MT + PDF) → documenta capa de normalización; no forces un solo parser narrativo.
- Truncación de referencias ISO 20022 → break de data integrity; no inventes remesa.
- Cutoff ambiguo → declara regla de cutoff usada.

## Validación

- Suma de matched + reconciling + breaks explica la diferencia de saldos.
- Timing ≠ error sin evidencia.
- Estándar/formato de extracto citado.

## Criterios de terminado

- Denjiro/auditoría puede ver qué cuadra, qué es timing y qué está abierto.
- Force-match ausente sin justificación.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | camt.053 + mayor caja | Conciliación con timing y 2 breaks fee |
| Ambiguo | “Cuadra el banco” sin extracto | BLOCKED / inputs faltantes |
| Límite | Referencias truncadas post-MT | Breaks de integridad + no auto-match |

## Fuentes

- SWIFT ISO 20022 FI focus — https://www.swift.com/standards/iso-20022/iso-20022-financial-institutions-focus-payments-instructions (2026-08-04).
- Zanders — ISO 20022 receivables reconciliation — https://zandersgroup.com/en/insights/blog/iso-20022-xml-an-opportunity-to-accelerate-and-elevate-receivables-reconciliation (2026-08-04).
- CPA Exams Mastery — bank reconciliations & proof of cash (2026-08-04).
- COSO ICIF — reconciliations as control activities (2026-08-04).
