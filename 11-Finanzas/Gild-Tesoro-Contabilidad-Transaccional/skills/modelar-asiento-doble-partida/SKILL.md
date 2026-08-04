---
name: modelar-asiento-doble-partida
description: Modela asientos de doble partida (débito/crédito, cuentas, fechas, moneda) para eventos transaccionales. Úsala cuando haya que reflejar contablemente cobros, pagos, fees, FX o liquidaciones sin reescribir el ledger core.
metadata:
  author: yzylabs
  version: "1.0"
---

# Modelar asiento de doble partida

## Propósito

Convertir un evento de negocio o liquidación en un journal balanceado, trazable y auditable.

## Entradas

- Descripción del evento (pago, cobro, fee, FX, settlement, ajuste).
- Plan de cuentas / mapping autorizado (o gap explícito).
- Moneda(s), importes, fechas valor y de libro.
- IDs de transacción / liquidación / factura.
- Restricciones de centros de costo o productos.

## Procedimiento

1. Nombra el evento y la evidencia fuente (extracto, clearing, billing, core export).
2. Identifica cuentas deudoras y acreedoras según mapping autorizado.
3. Construye líneas: cuenta, D/C, importe, moneda, fecha valor, fecha libro, referencia.
4. Verifica balance: Σ débitos = Σ créditos (por moneda; si hay FX, documenta contrapartida y tipo de cambio).
5. Etiqueta hechos vs inferencias (p. ej. cuenta sugerida sin mapping aprobado).
6. Lista controles: segregación preparador/aprobador para ajustes materiales.
7. Marca fuera de alcance: posting en system of record del core (Kaku).

## Salida

```md
## Evento / periodo
## Fuente de evidencia
## Líneas de asiento (tabla)
## Prueba de balance
## Mapping / gaps
## Controles y aprobaciones
## Riesgos / pendientes
```

## Casos límite

- Sin plan de cuentas → `BLOCKED` o borrador marcado como no ejecutable.
- Multi-moneda sin tipo de cambio → no cierres el asiento; escala.
- Ajuste “para cuadrar” sin causa → rechaza; crea break.

## Validación

- Balance numérico verificado.
- Cada línea tiene cuenta y referencia.
- No inventa cuentas no autorizadas sin etiquetar gap.

## Criterios de terminado

- Un revisor puede reproducir el cuadre sin preguntar el origen del evento.
- Gaps de mapping/core tienen dueño.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Cobro API + fee banco | Asiento D/C balanceado con refs |
| Ambiguo | “Registra este movimiento” sin cuentas | Preguntas + borrador con gaps |
| Límite | FX sin rate | BLOCKED parcial + decisión requerida |

## Fuentes

- Principios de doble partida / reconciliación de caja (material FAR / Intermediate FA) — 2026-08-04.
- Datathere — common ledger structure across formats — https://www.datathere.com/articles/finserv-ledger-iso-camt/ (2026-08-04).
