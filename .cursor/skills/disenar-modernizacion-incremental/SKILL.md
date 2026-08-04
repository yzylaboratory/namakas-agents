---
name: disenar-modernizacion-incremental
description: Diseña una estrategia strangler/façade por etapas para reemplazar un legado sin big-bang. Úsala cuando haya que modernizar o migrar un sistema heredado de forma incremental y reversible.
metadata:
  author: yzylabs
  version: "1.0"
---

# Diseñar modernización incremental

## Propósito

Definir cómo la higuera estranguladora crece alrededor del host: façade, orden de extracción, arquitectura transitoria y criterios de avance.

## Entradas

- Caracterización del legado.
- Evaluación de riesgo / seams.
- Outcomes de modernización alineados (negocio + técnico).
- Restricciones de coexistencia y ventanas.

## Procedimiento

1. Confirma outcomes medibles (no “reescribir en X”).
2. Verifica que las requests/flujos críticos se puedan interceptar; si no, documenta bloqueo del patrón.
3. Diseña la façade/proxy: qué enruta, dónde vive, NFR (SPOF, latencia, observabilidad).
4. Parte el legado en frentes (capacidades / bounded contexts), no en capas técnicas solas.
5. Ordena etapas: bajo blast radius + aprendizaje temprano primero.
6. Para cada etapa: entregable, ruta legacy vs nueva, rollback, métricas de éxito.
7. Declara arquitectura transitoria que se retirará (y cuándo).
8. Si semánticas divergen, enlaza `definir-capa-anticorruption`.
9. Si big-bang parece tentador, exige justificación escrita o recházalo.

## Salida

```md
## Outcomes
## Por qué incremental (o excepción documentada)
## Façade / routing
## Frentes y orden de extracción
## Etapas (alcance, éxito, rollback)
## Arquitectura transitoria
## Dependencias con ACL / datos
## Riesgos residuales
## Diagrama (Mermaid opcional)
```

## Casos límite

- No se pueden interceptar requests: patrón no apto; propone alternativa o bloqueo.
- Sistema pequeño: documenta excepción big-bang con evidencia de bajo riesgo.
- Mainframe sin seams: plan de inserción de seams antes de extracción.

## Validación

- Cada etapa es entregable y reversible hasta su cutover.
- Façade no es SPOF silencioso: hay plan de escala/observabilidad.
- Orden de frentes justificado por riesgo/valor.

## Criterios de terminado

- Plan usable por Iceburg/Tom/Law sin redescubrir el host.
- Big-bang ausente o excepcionado con evidencia.
- Criterios de avance por etapa explícitos.

## Casos de evaluación

| Caso | Entrada | Esperado |
|---|---|---|
| Normal | Monolito con API gateway viable | Façade + 3–5 etapas por capacidad |
| Ambiguo | “Pasar a microservicios” sin outcomes | Exige outcomes; plan esqueleto + bloqueos |
| Límite | Legacy sin proxy posible | BLOCKED del strangler + alternativas |

## Fuentes

- Martin Fowler — Strangler Fig Application (consultado 2026-08-04).
- Microsoft Learn — Strangler Fig Pattern (2026-05-29; consultado 2026-08-04).
- AWS Prescriptive Guidance — Strangler fig (consultado 2026-08-04).
- `references/patrones-modernizacion-legacy.md`
