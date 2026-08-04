---
name: coordinar-squad-backend
description: Coordina el squad Katakuri→X-Drake (microservicios), Pudding (datos/persistencia) y Apoo (eventos) con RACI, secuencia y contratos de delegación. Úsala cuando una iniciativa backend requiera alinear varios especialistas o resolver choques servicio/datos/eventos.
metadata:
  author: yzylabs
  version: "1.0"
---

# Coordinar squad Backend

## Propósito

Orquestar el trabajo departamental sin que Katakuri absorba implementación de MS, schemas o consumers, y sin que las células avancen en direcciones contradictorias.

## Entradas

- Iniciativa u objetivo departamental.
- Estado de artefactos (servicios, schemas, topics, specs).
- Restricciones de plazo y dependencias externas (Law, Robin, Franky, Jinbe, Core).
- Estado forja/stub de X-Drake, Pudding y Apoo.

## Procedimiento

1. Define el resultado único de la iniciativa (una frase).
2. Parte el trabajo:
   - X-Drake: microservicios / límites de dominio financiero.
   - Pudding: persistencia / migraciones / ownership de store.
   - Apoo: productores/consumidores / contratos de eventos / DLQ.
3. Elabora RACI (Responsible/Accountable/Consulted/Informed) por entregable.
4. Decide secuencia vs paralelo:
   - Paralelo temprano: exploración X-Drake + Pudding.
   - Gate de congelación de contrato API/evento antes de scale de Apoo.
5. Emite contratos de delegación autocontenidos (objetivo, alcance, entradas, criterios, validación).
6. Si célula stub: emite `DELEGATION_REQUIRED` (forja) o plan con `STATUS: BLOCKED` para la parte ejecutable.
7. Al sincronizar: detecta contradicciones (campo DB ≠ evento ≠ API) y resuelve o escala a Law/Robin.
8. Entrega consolidado departamental a Luffy o al siguiente eslabón.

## Salida

```md
## Objetivo de la iniciativa
## RACI del squad
| Entregable | R | A | C | I |
## Plan (secuencia / paralelo)
## Delegaciones emitidas
## Estado stub / DELEGATION_REQUIRED
## Contradicciones y resoluciones
## Pendientes / bloqueos
## Listo para
```

## Casos límite

- Solo Katakuri forjado: entrega dirección + contratos; no inventes output de células.
- Choque “hay que publicar evento ya” vs schema inestable: gate o MVP acotado documentado.
- Robin necesita contratos: exige handoff mínimo de límites de servicio/datos o marca draft inestable.

## Validación

- Cada especialista tiene un entregable distinto.
- Hay al menos un accountable (Katakuri) por iniciativa.
- No hay dos dueños escribiendo el mismo artefacto crítico sin regla de merge.

## Criterios de terminado

- Plan y RACI claros.
- Delegaciones listas para Tasks cuando existan agentes forjados.
- Contradicciones materiales resueltas o escaladas.

## Fuentes

- Microsoft — Designing microservice-oriented applications — https://learn.microsoft.com/en-us/dotnet/architecture/microservices/multi-container-microservice-net-applications/microservice-application-design (2026-08-04)
- Catálogo Nakamas Backend (X-Drake, Pudding, Apoo) — `catalogo/agentes-one-piece.yaml`
