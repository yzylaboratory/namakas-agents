# Referencias — patrones de modernización legacy

Material de apoyo para skills de Crocus. Preferir siempre las fuentes primarias citadas abajo; este archivo es índice, no autoridad.

## Strangler Fig

- **Idea:** reemplazar el host de forma gradual; façade/proxy enruta al legado o al nuevo hasta que el host pueda retirarse.
- **Actividades (Fowler / Patterns of Legacy Displacement):** alinear outcomes → partir el problema → entregar partes → cambiar la organización para sostener el ritmo.
- **Cuándo no:** no se pueden interceptar requests; sistema pequeño y sustituible de golpe; retiro urgente sin coexistencia posible.
- Fuentes:
  - https://martinfowler.com/bliki/StranglerFigApplication.html
  - https://learn.microsoft.com/en-us/azure/architecture/patterns/strangler-fig
  - https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/strangler-fig.html

## Anti-Corruption Layer (ACL)

- **Idea:** fachada/adaptador que traduce modelos y protocolos entre legado y moderno para que el dominio nuevo no herede semánticas corruptas.
- **No es:** lugar para reglas de negocio u orquestación larga.
- **Considerar:** latencia, ownership de la capa, escalado, validación en frontera de confianza, si la ACL es temporal o permanente.
- Fuente:
  - https://learn.microsoft.com/en-us/azure/architecture/patterns/anti-corruption-layer

## Coexistencia y datos

- Dual-run / shadow traffic cuando el riesgo lo exige.
- ETL inicial + CDC para sincronizar dominios durante extracción de datos (patrón documentado en Azure Strangler Fig sobre DBs monolíticas).
- Rollback explícito hasta eliminar objetos del host; después el costo de rollback sube.

## Relación con otros agentes Nakamas

| Agente | Frontera |
|---|---|
| Noland | Mapa/recon general; Crocus consume y especializa en legacy care |
| Tom | Implementa integración core según plan de Crocus/Iceburg |
| Kaku | Motor/flujos transaccionales; Crocus no los diseña |
| Law | Arquitectura objetivo; Crocus aporta constraints del host |
| Robin | Contratos formales; Crocus no inventa OpenAPI |

Consulta: 2026-08-04.
