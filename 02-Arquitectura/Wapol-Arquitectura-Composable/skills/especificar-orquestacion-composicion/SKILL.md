---
name: especificar-orquestacion-composicion
description: Especifica la capa de orquestación/composición entre PBCs (BFF, workflow, experience API) sin crear un monolito oculto. Úsala cuando frontends o journeys deban componer múltiples capacidades.
metadata:
  author: yzylabs
  version: "1.0"
---

# Especificar orquestación de composición

## Propósito

Definir dónde y cómo se orquesta la composición entre PBCs — con límites claros — evitando que el orquestador posea todos los datos y reglas de dominio.

## Entradas

- Blueprint de composición / journey.
- PBCs y contratos disponibles.
- Canales de experiencia (web, móvil, partner).
- Preferencia sync vs event-driven.

## Procedimiento

1. Identifica consumidores de la composición (canales) y latencia esperada.
2. Elige patrón: BFF / experience API / workflow orchestrator / coreografía por eventos.
3. Declara responsabilidades del orquestador (agregación, auth context, mapping) y **no-responsabilidades** (fuente de verdad de dominio).
4. Mapea llamadas/eventos a cada PBC; marca timeouts, idempotencia y degradación.
5. Si la composición es predominantemente event-driven → documenta y escala patrones a Enel.
6. Exige que frontends no llamen capacidades backend crudas sin capa de composición cuando el stack es multi-PBC.
7. Señala riesgos de “god orchestrator” y propone splits si acumula reglas de varios dominios.
8. Lista requisitos de contrato hacia Robin (sin escribir el OpenAPI formal aquí salvo borrador de operaciones).

## Salida

```md
## Consumidores / canales
## Patrón de orquestación elegido (+ alternativas descartadas)
## Responsabilidades / No-responsabilidades
## Mapa PBC ↔ operaciones/eventos
## Degradación y resiliencia
## Riesgos de monolito oculto
## Handoffs (Enel / Robin / Frontend / Law)
```

## Casos límite

- Un solo PBC → quizá no hace falta orquestador; no sobre-diseñes.
- Orquestador necesita escribir en muchas DBs → red flag; rediseña.
- Partner API externa → coordina con Sabo vía Law; no mezcles producto externo con BFF interno sin etiquetar.

## Validación

- No-responsabilidades explícitas.
- Mapa completo PBC ↔ interacción.
- Escala a Enel si EDA es central.

## Criterios de terminado

- Frontend/Backend saben qué componer y qué no vive en el orquestador.
- Riesgo de god-orchestrator documentado o mitigado.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | App móvil agrega accounts + cards + offers | BFF/experience API con mapa |
| Ambiguo | “Pon un orquestador central” | Exige límites y no-responsabilidades |
| Límite | Orquestador con reglas de pricing+ledger+KYC | Riesgo monolito + split propuesto |

## Fuentes

- Conscia — orchestration layer in composable stacks — https://www.conscia.ai/post/what-is-a-composable-architecture (2026-08-04).
- MACH Alliance materials — https://machalliance.org/ (2026-08-04).
- Apidog — API-first composition — https://apidog.com/blog/composable-architecture/ (2026-08-04).
