---
name: definir-reglas-posteo-ledger
description: Define reglas de posteo contable/ledger para transacciones core (partida doble, atomicidad, isolation, hold vs capture). Úsala cuando se diseñe o audite cómo una transacción se convierte en asientos en el libro.
metadata:
  author: yzylabs
  version: "1.0"
---

# Definir reglas de posteo ledger

## Propósito

Especificar cómo una transacción de negocio se materializa en asientos: cuentas, importes, moneda, atomicidad y control de concurrencia — sin ambigüedad que permita desbalance o double-spend.

## Entradas

- Tipo de transacción y cuentas involucradas (o roles de cuenta).
- Moneda(s), redondeo, fees.
- Requisitos ACID / isolation del datastore.
- Auth/hold vs capture si aplica.
- Restricciones regulatorias conocidas (alto nivel).

## Procedimiento

1. Declara el asiento canónico: líneas débito/crédito, suma cero por moneda.
2. Define ownership del ledger y fuente de verdad de saldo.
3. Especifica frontera de transacción DB (qué se commitea junto).
4. Define orden determinista de locks (p. ej. sort de account IDs) si hay `SELECT FOR UPDATE`.
5. Separa hold (reserva) de capture (posteo final) cuando el producto lo requiera.
6. Documenta fees/impuestos como líneas explícitas, no “ajustes mágicos”.
7. Define invariantes post-commit (balance check, hash de asiento).
8. Lista anti-patrones prohibidos (posteo parcial visible, saldo negativo no autorizado, etc.).

## Salida

```md
# Reglas de posteo — [Transacción]

## Asiento canónico
| Cuenta/rol | D/C | Importe | Moneda |
## Frontera ACID
## Concurrencia / locks
## Hold vs capture
## Invariantes
## Anti-patrones
## Pendientes
```

## Casos límite

- Multi-moneda / FX → documentar tasa, redondeo y asiento puente; no improvisar.
- Fee absorbido → línea explícita a cuenta de ingreso.
- Ledger distribuido sin isolation adecuada → BLOCKED o limitación explícita.

## Validación

- Débitos = créditos por moneda en el asiento.
- Frontera ACID clara.
- Concurrencia abordada o marcada como riesgo.

## Criterios de terminado

- Reglas implementables por backend/datos.
- Invariantes testeables.
- Huecos listados.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Book transfer A→B | Asiento D/C atómico |
| Ambiguo | “Debitar cliente” sin contra | Exige cuenta crédito; borrador |
| Límite | Dos posts concurrentes mismo saldo | Lock order + isolation |

## Fuentes

- Diseño de ledgers ACID / double-entry en plataformas de pagos — 2026-08-04
- Separación auth/capture en pipelines de pago — contraste 2026-08-04
