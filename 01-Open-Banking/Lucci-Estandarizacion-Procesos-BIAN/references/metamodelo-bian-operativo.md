# Resumen operativo del metamodelo BIAN (para Lucci)

Síntesis accionable a partir de fuentes oficiales. No sustituye el catálogo ni las specs YAML.

Consultado: 2026-08-04.

## Bloques

| Artefacto | Qué es | Uso en mapeo |
|---|---|---|
| Service Landscape | Organización de Service Domains | Buscar y validar nombres/versión |
| Service Domain | Unidad funcional MECE (asset type + functional pattern) | Partición canónica de capacidad |
| Functional Pattern | ~19 patrones de comercialización (operate, manage, analyze, …) | Explica el “cómo” del dominio |
| Control Record (CR) | Artefacto operativo de una ocurrencia del SD a lo largo del ciclo de vida | Núcleo de información intercambiada |
| Behavior Qualifier (BQ) | Partición más estrecha del CR | Sub-recursos / operaciones más específicas |
| Service Operations + Action Terms | Interfaz del SD (Initiate, Update, Retrieve, …) | Puente a Semantic APIs |
| Business Scenarios | Ejemplos de interacción entre SDs | Ilustración **no prescritiva** |
| Wireframes | Diagramas de partida para escenarios org. | Igual: adaptar sin cambiar rol del SD |
| Semantic APIs | OAS3 / AsyncAPI por Service Domain | Evidencia de operaciones y paths |

## Action terms frecuentes (Semantic API)

Según guía de practitioners y patrones públicos del repo oficial (HTTP típico):

| Action term | Rol típico |
|---|---|
| Initiate | Crear instancia de CR |
| Update | Modificar atributos |
| Retrieve | Consultar estado |
| Control | Controlar flujo operativo |
| Execute | Disparar acción automatizada |
| Request | Intervención manual |
| Exchange | Aceptar / verificar / validar |
| Register | Alta en directorio |
| Notify | Notificaciones / suscripción (según spec) |
| Evaluate | Análisis / evaluación (según guía) |

Confirma siempre contra el YAML del Service Domain en la release de trabajo.

## V14.0 — notas de forja

- Racionalización de definiciones de Service Domain; menos operaciones innecesarias; más enlaces ISO 20022.
- Cambios relevantes en Payments; altas en Insurance; métricas ~322 Service Domains en release notes V14.
- CR/BOM en UML; Service Domains/Capabilities en ArchiMate 3.2.
- Semantic APIs release14.0.0 en `bian-official/public` (BOM-extended y ISO20022-ext-ddd; OAS3 y AsyncAPI 3.x).

## Fuentes

- https://bian.org/deliverables/service-landscape/
- https://bian.org/wp-content/uploads/2026/02/BIAN-v14.0-Release-Notes-v1.0_-Final-Version.pdf
- https://bian.org/wp-content/uploads/2024/12/BIAN-Semantic-API-Pactitioner-Guide-V8.1-FINAL.pdf
- https://github.com/bian-official/public
