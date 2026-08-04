---
name: disenar-compensacion-y-reversa
description: Diseña caminos de compensación, return y reversa correlacionados al original (sin borrar historia). Úsala cuando haya fallos parciales, returns interbank, ajustes o sagas que deban deshacer efectos de posteo.
metadata:
  author: yzylabs
  version: "1.0"
---

# Diseñar compensación y reversa

## Propósito

Definir cómo se deshacen o mitigan efectos financieros de forma auditable, correlacionada y segura ante reintentos.

## Entradas

- Ciclo de vida y estados del original.
- Tipos de fallo (reject, timeout, partial settle, customer return).
- Mensajería de return/status si aplica (p. ej. `pacs.004`, status `pacs.002`).
- Política de negocio (full reverse, partial, adjust).

## Procedimiento

1. Clasifica escenarios: never posted, posted then rejected, settled then returned, partial.
2. Para cada escenario, elige estrategia: no-op, reverse asiento, return message, adjust.
3. Exige correlación al original (`EndToEndIdentification` / IDs locales).
4. Define asiento compensatorio (líneas invertidas o explícitas) — **no delete**.
5. Aplica idempotencia también a la reversa (clave propia o derivada).
6. Ordena compensaciones en sagas multi-paso (compensating transaction pattern).
7. Documenta efectos en reporting/`camt` y en colas de excepción.
8. Entrega matriz escenario → acción + pruebas.

## Salida

```md
# Compensación/Reversa — [Flujo]

## Escenarios
| Escenario | Estrategia | Asiento | Correlación | Idempotencia |
## Sagas / orden
## Efectos en reporting
## Pruebas
## Pendientes
```

## Casos límite

- Reverse de reverse → política explícita (forbid vs adjust).
- Partial amount return → líneas parciales + remanente.
- Original aún en hold → release hold ≠ settlement reverse.

## Validación

- Ningún escenario material usa delete de historia.
- Correlación obligatoria.
- Idempotencia de reversa definida.

## Criterios de terminado

- Matriz completa para escenarios in-scope.
- Implementable y testeable.
- Fuera de alcance listado.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Settled + customer return | Asiento compensatorio + correlación |
| Ambiguo | “Si falla, deshacer” | Matriz por fase del ciclo |
| Límite | Saga 3 pasos, falla el 3º | Compensaciones 2→1 ordenadas |

## Fuentes

- ISO 20022 returns/status (`pacs.004`, `pacs.002`) — catálogo / guías SWIFT — 2026-08-04
- Compensating transactions / saga pattern — contraste diseño 2026-08-04
