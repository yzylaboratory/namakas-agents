---
name: auditar-reemplazabilidad
description: Audita acoplamiento y reemplazabilidad de PBCs/componentes (¿se puede hacer swap sin reescritura masiva?). Úsala cuando se cuestione vendor lock-in, acoplamiento o si una arquitectura es realmente composable.
metadata:
  author: yzylabs
  version: "1.0"
---

# Auditar reemplazabilidad

## Propósito

Determinar si un componente o PBC puede sustituirse con costo acotado, listando acoplamientos que bloquean el swap.

## Entradas

- Componente/PBC objetivo de reemplazo (hipotético o real).
- Dependientes conocidos (consumidores de API/eventos/UI/datos).
- Contratos, schemas compartidos, librerías internas.
- Blueprint de composición actual.

## Procedimiento

1. Define el escenario de swap (qué se reemplaza, por qué, horizonte).
2. Inventaría acoplamientos: DB compartida, tipos internos, UI embebida, SDK propietario, eventos sin contrato.
3. Clasifica cada acoplamiento: `bloqueante` | `costoso` | `aceptable`.
4. Estima blast radius (equipos, contratos, datos a migrar).
5. Propón remedios (anti-corruption, versionado de contrato, dual-run, strangler).
6. Emite veredicto: `swappable` | `swappable-with-cost` | `not-swappable` + evidencia.
7. Si “composable” dependía del swap, degrada el claim hasta remediar.

## Salida

```md
## Escenario de swap
## Inventario de acoplamientos
| Acoplamiento | Tipo | Severidad | Evidencia | Remedio |
## Blast radius
## Veredicto de reemplazabilidad
## Plan de remediación (ordenado)
## Impacto en claim “composable”
```

## Casos límite

- Solo hay abstracción verbal sin contrato → not-swappable.
- Eventos sin schema/version → costoso o bloqueante; escala Enel/Robin según caso.
- Datos históricos atrapados en vendor → documenta migración; no minimices.

## Validación

- Veredicto respaldado por acoplamientos listados.
- Remedios concretos, no “desacoplar más”.
- No aprueba excepciones de seguridad (Fujitora).

## Criterios de terminado

- Law entiende el costo real del swap.
- Gaps bloqueantes tienen dueño.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | CMS headless con API estable | swappable-with-cost |
| Ambiguo | “Podemos cambiar de vendor fácil” | Exige inventario de acoplamientos |
| Límite | DB compartida + tipos internos | not-swappable + remedios |

## Fuentes

- Elastic Path — PBCs vs microservices / modularity — https://www.elasticpath.com/blog/what-is-the-difference-between-pbcs-and-microservices (2026-08-04).
- MACH Architecture — loose coupling / replaceability — https://macharchitecture.com/ (2026-08-04).
- Apidog — composable components via APIs — https://apidog.com/blog/composable-architecture/ (2026-08-04).
