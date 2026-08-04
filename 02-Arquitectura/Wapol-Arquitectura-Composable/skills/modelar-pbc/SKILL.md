---
name: modelar-pbc
description: Modela Packaged Business Capabilities (PBCs) con límites, datos, APIs, eventos y dueños. Úsala cuando haya que decomponer un dominio o producto en capacidades de negocio ensamblables.
metadata:
  author: yzylabs
  version: "1.0"
---

# Modelar Packaged Business Capabilities (PBC)

## Propósito

Definir PBCs como bloques de capacidad de negocio autónomos — reconocibles por negocio, con schema/servicios/APIs/eventos acotados — listos para composición.

## Entradas

- Objetivo de negocio / journeys.
- Dominios o sistemas candidatos.
- Contratos, eventos y ownership conocidos.
- Restricciones de autonomía de datos.

## Procedimiento

1. Nombra capacidades en lenguaje de negocio (p. ej. “Pricing”, no “pricing-svc-v3”).
2. Para cada PBC candidata, documenta: propósito, actores, incluido/excluido.
3. Declara encapsulación de datos (qué posee; qué no se comparte por DB).
4. Lista APIs de borde y canales de eventos (o gaps).
5. Evalúa autonomía: dependencias críticas externas → gap o rediseño.
6. Diferencia explícitamente: PBC vs microservicio granular vs módulo monolítico.
7. Asigna dueño de producto/técnico; sin dueño = no listo.
8. Produce catálogo priorizado (must-have vs later).

## Salida

```md
## Catálogo PBC
### PBC: <nombre>
- Capacidad de negocio:
- Incluido / Excluido:
- Datos encapsulados:
- APIs:
- Eventos:
- Dependencias:
- Autonomía: alta|media|baja + justificación
- Dueño:
- Madurez: propuesta|parcial|listo
## Mapa de relaciones entre PBCs
## Gaps de autonomía
## Riesgos / pendientes
```

## Casos límite

- Capacidad solo técnica (“API Gateway”) → no es PBC de negocio; reclasifica.
- Varios dominios en un “PBC” → split o marca monolito empaquetado.
- Datos maestros compartidos sin anti-corruption → autonomía baja + remedio.

## Validación

- Cada PBC es reconocible por un usuario de negocio.
- Datos/APIs/eventos/dueño presentes o gap explícito.
- No se inventan contratos formales (eso es Robin).

## Criterios de terminado

- Catálogo usable para composición y buy/build.
- Gaps de autonomía tienen dueño propuesto.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Checkout + inventario + pagos | 3+ PBCs con límites |
| Ambiguo | “Haz microservicios del monolito” | Pregunta por capacidades de negocio |
| Límite | Un solo DB compartido | PBCs con autonomía baja + plan de encapsulación |

## Fuentes

- Magnolia — PBCs — https://www.magnolia-cms.com/blog/packaged-business-capabilities.html (2026-08-04).
- Elastic Path — PBCs vs microservices — https://www.elasticpath.com/blog/what-is-the-difference-between-pbcs-and-microservices (2026-08-04).
- Trisotech — Composability and PBCs — https://www.trisotech.com/composability-and-packaged-business-capabilities/ (2026-08-04).
- GlobalLogic Composable Enterprise PBC PDF — https://www.globallogic.com/wp-content/uploads/2023/04/Composable-Enterprise-PBC.pdf (2026-08-04).
