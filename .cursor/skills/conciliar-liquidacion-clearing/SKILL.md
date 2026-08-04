---
name: conciliar-liquidacion-clearing
description: Concilia reportes de liquidación/clearing vs libro (neto, fees, FX, fails, value vs booking date). Úsala cuando haya settlement reports, netting o discrepancias de clearing/pagos mayoristas.
metadata:
  author: yzylabs
  version: "1.0"
---

# Conciliar liquidación y clearing

## Propósito

Cuadrar el resultado de liquidación (gross/net, fees, FX, fails) contra el libro financiero y dejar fails/disputas con dueño.

## Entradas

- Settlement / clearing report del periodo.
- Journals o export de libro para las mismas instrucciones.
- Identificadores de instrucción / batch / netting cycle.
- Reglas de fees y FX contractuales (si existen).
- Calendario value date vs booking date.

## Procedimiento

1. Define el ciclo de liquidación (fecha, moneda, mercado/clearing, producto).
2. Normaliza líneas: instrucción, monto bruto, neto, fee, FX, status (settled/fail/partial).
3. Cruza vs libro por ID de instrucción; luego por monto+fecha con tolerancia explícita.
4. Separa diferencias de value date vs booking date (timing) de breaks reales.
5. Explica fees y FX: esperado vs cobrado; no inventes tarifa (escala Du-Feld/Legal si comercial).
6. Lista fails / unsettled con aging y dueño ops/mercado.
7. Propón asientos de fee/FX solo con evidencia; posting core → Kaku.

## Salida

```md
## Ciclo / alcance
## Gross / net / fees / FX
## Matched vs libro
## Timing (value vs booking)
## Fails / disputes
## Ajustes propuestos
## Dueños y escalamiento
## Riesgos / pendientes
```

## Casos límite

- Netting multilateral sin breakdown → pide detalle; no asumas prorrateo.
- Fail reciclado entre ciclos → trackea instrucción end-to-end.
- FX mid-market vs contractual → documenta fuente del rate.

## Validación

- Neto liquidado explicado vs libro.
- Fails no omitidos.
- Fees/FX con fuente o gap etiquetado.

## Criterios de terminado

- Ciclo de settlement tiene explicación completa de diferencias.
- Handoffs a ops/core/comercial claros.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Report neto + journals | Conciliación con fee line |
| Ambiguo | Solo neto sin breakdown | Inputs faltantes / BLOCKED parcial |
| Límite | Fail + FX disputed | Aging fail + escala comercial |

## Fuentes

- SWIFT / CBPR+ — integridad de datos en pagos cross-border ISO 20022 (2026-08-04).
- Datathere — temporal alignment value vs booking — https://www.datathere.com/articles/finserv-ledger-iso-camt/ (2026-08-04).
- ReconArt — settlement predictability / fee transparency (2026-08-04).
