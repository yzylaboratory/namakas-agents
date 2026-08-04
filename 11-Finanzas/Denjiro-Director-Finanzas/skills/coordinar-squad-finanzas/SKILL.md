---
name: coordinar-squad-finanzas
description: Coordina el squad Denjiro→King Riku (presupuesto), Du Feld (monetización APIs) y Gild Tesoro (contabilidad transaccional) con RACI, secuencia y contratos de delegación. Úsala cuando una iniciativa financiera requiera alinear varias células o resolver choques entre ahorro, pricing e integridad del ledger.
metadata:
  author: yzylabs
  version: "1.0"
---

# Coordinar squad Finanzas

## Propósito

Orquestar el trabajo departamental sin que Denjiro absorba FinOps operativo, pricing ni ledger, y sin que las células avancen en direcciones contradictorias.

## Entradas

- Iniciativa u objetivo departamental.
- Estado de artefactos (budgets, cost reports, pricing models, ledger/reconciliación).
- Restricciones de plazo y dependencias externas (Jinbe/Sabo, Franky, Law, Sengoku).

## Procedimiento

1. Define el resultado único de la iniciativa (una frase).
2. Parte el trabajo:
   - King Riku: presupuesto / allocation / forecasting / anomalías de infra.
   - Du Feld: monetización / pricing / metering / packaging.
   - Gild Tesoro: contabilidad transaccional / reconciliación / cierre.
3. Elabora RACI por entregable (Denjiro Accountable de la iniciativa).
4. Decide secuencia vs paralelo:
   - Paralelo temprano: baseline de costo (King Riku) + hipótesis de packaging (Du Feld).
   - Gate de ledger (Gild Tesoro) antes de cobro en producción.
5. Emite contratos de delegación autocontenidos.
6. Si la célula es stub: documenta plan y emite `DELEGATION_REQUIRED`; no inventes ejecución.
7. Al sincronizar: detecta contradicciones (unit cost ≠ pricing ≠ asiento) y resuelve o escala.
8. Entrega consolidado departamental a Luffy.

## Salida

```md
## Objetivo de la iniciativa
## RACI del squad
| Entregable | R | A | C | I |
## Plan (secuencia / paralelo)
## Delegaciones emitidas
## Stubs / DELEGATION_REQUIRED
## Contradicciones y resoluciones
## Pendientes / bloqueos
## Listo para
```

## Casos límite

- Especialista sin demo Cursor (stub): planifica roster; no inventes Task `brd-*`.
- Choque Du Feld vs King Riku (“precio agresivo vs costo real”): Denjiro exige puente de margen o bloquea go-live.
- Urgencia comercial sin Gild Tesoro: MVP showback interno con deuda de ledger explícita; no fingir cobro producción.

## Validación

- Cada célula tiene un entregable distinto.
- Hay al menos un Accountable (Denjiro) por iniciativa.
- No hay dos dueños escribiendo el mismo artefacto crítico sin regla de merge.

## Criterios de terminado

- Plan y RACI claros.
- Delegaciones listas para Tasks cuando existan agentes forjados.
- Contradicciones materiales resueltas o escaladas.

## Fuentes

- FinOps Framework — Personas / collaboration principles — https://www.finops.org/framework/principles/ (consultado 2026-08-04)
- Organigrama Nakamas — `organization/organigrama.yaml` (squad Finanzas)
