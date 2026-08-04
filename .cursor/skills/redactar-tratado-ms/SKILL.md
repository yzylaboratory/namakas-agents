---
name: redactar-tratado-ms
description: Redacta el tratado técnico de un microservicio u orquestación (propósito, límites, flujos, dependencias, decisiones y no-objetivos). Úsala cuando se pida documentar arquitectura de MS/orch o producir el tratado base antes de contratos o handoffs.
metadata:
  author: yzylabs
  version: "1.0"
---

# Redactar tratado de microservicio / orquestación

## Propósito

Producir un tratado técnico accionable que acote el servicio y sirva de fuente narrativa alineada a contratos y mapeos de dominio.

## Entradas

- Nombre y objetivo del MS u orquestación.
- Alcance incluido y excluido.
- Requisitos o historias disponibles.
- Decisiones de arquitectura (ADRs) si existen.
- Mapeo BIAN / `HANDOFF_BIAN` cuando el dominio lo exija.
- Dependencias conocidas (APIs, eventos, sistemas core).

## Procedimiento

1. Confirma el tipo de artefacto: MS singular vs orquestación (saga/proceso).
2. Inventaría entradas; lista huecos materiales.
3. Si es bancario/nuevo y falta mapeo BIAN, aplica `consumir-mapeo-bian` o escala — no inventes Service Domains.
4. Redacta el tratado con la estructura de `references/plantilla-tratado-ms.md`.
5. Separa: contexto, límites, capacidades, datos, APIs, eventos, SLAs/NFR relevantes, riesgos.
6. Etiqueta cada afirmación como hecho, supuesto o pendiente.
7. Cruza con contratos existentes; anota drift.
8. Entrega el tratado y la lista de pendientes.

## Salida

```md
# Tratado — [Nombre MS/Orch]

## 1. Resumen
## 2. Contexto y motivadores
## 3. Límites del servicio (in/out)
## 4. Capacidades y flujos
## 5. Datos y ownership
## 6. Interfaces síncronas
## 7. Eventos / orquestación
## 8. Trazabilidad BIAN (si aplica)
## 9. NFR y restricciones
## 10. Decisiones, supuestos, riesgos, pendientes
```

## Casos límite

- Solo hay un nombre de servicio sin requisitos → tratado mínimo + bloqueo de pendientes; no inventes dominio.
- Orquestación que cruza varios MS → documenta el proceso y referencias a tratados hijos; no fusiones bounded contexts.
- Conflicto entre ADR y código legacy → documenta ambos, marca decisión abierta, escala a Law/Luffy.

## Validación

- Límites in/out explícitos.
- Sin Service Domains inventados.
- Hechos vs supuestos etiquetados.
- Referencias a entradas reales (rutas, IDs de handoff).

## Criterios de terminado

- Tratado usable por un implementador.
- Pendientes listados.
- Coherencia básica con contratos/mapeo disponibles.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Objetivo + límites + HANDOFF_BIAN | Tratado completo con trazabilidad BIAN |
| Ambiguo | Solo nombre del MS | Tratado esqueleto + bloqueos; sin invención de dominio |
| Límite | Orquestación multi-MS sin dueño de datos | Documenta ownership gaps y escala |

## Fuentes

- BIAN Semantic API Practitioner’s Guide v8.1 (2024-12) — Service Domain como building block.
- Práctica contract-first / design-first OpenAPI 3.1 (2026-08-04).
