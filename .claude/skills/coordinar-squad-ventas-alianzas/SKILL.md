---
name: coordinar-squad-ventas-alianzas
description: Coordina el squad Buggy→Crocodile (cuentas B2B), Mr. 3 (enablement) y Bon Clay (partner success) con RACI, secuencia y contratos de delegación. Úsala cuando una iniciativa comercial requiera alinear a varios especialistas del departamento o resolver choques hunting/enablement/success.
metadata:
  author: yzylabs
  version: "1.0"
---

# Coordinar squad ventas y alianzas

## Propósito

Orquestar el trabajo departamental sin que Buggy absorba hunting, playbooks u onboarding, y sin que los especialistas avancen en direcciones contradictorias.

## Entradas

- Iniciativa u objetivo departamental (cuenta, partner, play, launch).
- Estado de artefactos (pipeline, playbooks, onboarding checklist, contratos draft).
- Restricciones de plazo y dependencias externas (Legal, Finanzas, Marketing, OB).

## Procedimiento

1. Define el resultado único de la iniciativa (una frase).
2. Parte el trabajo:
   - Crocodile: cuentas / deals estratégicos B2B.
   - Mr. 3: enablement (plays, content, certification, kits co-sell).
   - Bon Clay: onboarding y éxito del partner.
3. Elabora RACI por entregable.
4. Decide secuencia vs paralelo:
   - Paralelo temprano: Crocodile avanza cuentas mientras Mr. 3 arma el play — solo si el mensaje/ICP está congelado.
   - Gate: operating model/economía del partner antes de scale de Bon Clay.
5. Emite contratos de delegación autocontenidos (objetivo, alcance, entradas, criterios, validación).
6. Al sincronizar: detecta contradicciones (promesa de deal ≠ capacidad de delivery ≠ readiness del partner) y resuelve o escala.
7. Entrega consolidado departamental a Luffy o al siguiente eslabón.

## Salida

```md
## Objetivo de la iniciativa
## RACI del squad
| Entregable | R | A | C | I |
## Plan (secuencia / paralelo)
## Delegaciones emitidas
## Contradicciones y resoluciones
## Pendientes / bloqueos
## Listo para
```

## Casos límite

- Especialista aún stub (sin demo Cursor): planifica roster y ejecuta solo la capa de dirección; emite `DELEGATION_REQUIRED` a Luffy; no inventes Task `brd-*`.
- Choque Crocodile vs Bon Clay (“cerrar logo vs partner no onboarded”): Buggy decide gate o MVP de activation documentado.
- Marketing quiere co-branding sin pipeline: exige joint motion o rechaza como vanity.

## Validación

- Cada especialista tiene un entregable distinto.
- Hay al menos un accountable (Buggy) por iniciativa.
- No hay dos dueños escribiendo el mismo artefacto crítico sin regla de merge / deal registration.

## Criterios de terminado

- Plan y RACI claros.
- Delegaciones listas para pegar en Tasks cuando existan agentes vivos.
- Contradicciones materiales resueltas o escaladas.

## Fuentes

- Forecastable — operating cadence for partnerships — https://forecastable.com/b2b-partnerships/ (2026-08-04)
- Catálogo Nakamas Ventas y Alianzas — `catalogo/agentes-one-piece.yaml` (Crocodile, Mr. 3, Bon Clay)
