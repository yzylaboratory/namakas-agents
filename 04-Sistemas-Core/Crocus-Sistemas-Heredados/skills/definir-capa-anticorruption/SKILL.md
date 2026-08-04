---
name: definir-capa-anticorruption
description: Diseña una Anti-Corruption Layer entre legado y sistema moderno para traducir modelos/protocolos sin contaminar el dominio nuevo. Úsala cuando haya que integrar o migrar con semánticas distintas.
metadata:
  author: yzylabs
  version: "1.0"
---

# Definir capa anti-corruption

## Propósito

Proteger el diseño moderno aislando traducciones hacia/desde el legado en una frontera explícita.

## Entradas

- Modelos/semánticas del legado (observados).
- Modelo objetivo del sistema nuevo (o borrador de Law/Robin).
- Flujos que deben cruzar la frontera (sync/async).
- Restricciones de latencia, consistencia y trust level.

## Procedimiento

1. Lista conceptos que no mapean 1:1 entre legado y moderno.
2. Define dirección(es) de traducción (nuevo→legado, legado→nuevo, bidireccional).
3. Delimita responsabilidad de la ACL: solo adaptación; sin reglas de negocio largas ni orquestación.
4. Elige forma: librería in-process, servicio dedicado, funciones + API gateway (según contexto; no prescritas).
5. Especifica contratos en el borde moderno (DTOs/eventos canónicos) vs adapters legacy.
6. Planifica validación/sanitización en la frontera de confianza.
7. Define observabilidad: correlation IDs, métricas de fallo de traducción, latencia.
8. Decide si la ACL es temporal (migración) o permanente (cliente legacy residual).
9. Entrega handoff a Tom/Robin/Law para implementación/contratos.

## Salida

```md
## Frontera A ↔ B
## Conceptos y traducciones
## Responsabilidades in/out de la ACL
## Forma de despliegue (propuesta)
## Contratos en el borde moderno
## Validación y seguridad en frontera
## Observabilidad
## Temporal vs permanente
## NFR y riesgos
```

## Casos límite

- Semánticas casi idénticas: ACL mínima o innecesaria; no inventes capa por moda.
- ACL que acumula business rules: refactoriza; escala a Law.
- Multi-legado: considera ACL por bounded context, no un “dios traductor”.

## Validación

- Ninguna regla de orquestación de negocio vive en la ACL.
- Traducciones cubren los flujos pedidos o marcan gaps.
- Trust boundary y validación explícitas.

## Criterios de terminado

- Un implementador puede construir la ACL sin adivinar mapeos.
- Dominio nuevo queda protegido de DTOs legacy.
- Ownership y destino (retirar o conservar) documentados.

## Casos de evaluación

| Caso | Entrada | Esperado |
|---|---|---|
| Normal | Orders legacy ↔ Order moderno | Mapeo de campos + servicio ACL |
| Ambiguo | “Pon una ACL” sin modelos | Exige modelos; esqueleto + bloqueos |
| Límite | Tres hosts con semánticas distintas | ACL por contexto; no monolito traductor |

## Fuentes

- Microsoft Learn — Anti-Corruption Layer Pattern (2026-05-28; consultado 2026-08-04).
- Azure Strangler Fig — uso de ACL para llamadas cruzadas (consultado 2026-08-04).
- Origen conceptual: Eric Evans, Domain-Driven Design (patrón ACL).
