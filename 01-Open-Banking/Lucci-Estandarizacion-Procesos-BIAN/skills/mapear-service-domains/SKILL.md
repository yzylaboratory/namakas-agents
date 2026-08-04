---
name: mapear-service-domains
description: Mapea capacidades, procesos o límites de MS/orch a Service Domains BIAN con evidencia del catálogo/release/Semantic API. Úsala cuando debas estandarizar un proceso bancario o elegir Service Domains sin inventarlos.
metadata:
  author: yzylabs
  version: "1.0"
---

# Mapear Service Domains

## Propósito

Traducir capacidades de negocio a Service Domains BIAN verificables (MECE), citando versión y fuente.

## Entradas

- Descripción del proceso / MS / orch / capacidades.
- Alcance incluido y fuera de alcance.
- Versión BIAN (default V14.0).
- Evidencia auxiliar (recon, APIs, owners) si existe.

## Procedimiento

1. Lista capacidades atómicas del alcance (verbos + objetos de negocio).
2. Fija versión BIAN y fuentes primarias a consultar.
3. Para cada capacidad, busca candidatos en Service Landscape / Semantic API / release notes de esa versión.
4. Valida que el candidato cubre el asset type y el functional pattern esperados; descarta “parecidos” sin evidencia.
5. Detecta solapes: si dos SDs cubren lo mismo, documenta conflicto y elige con evidencia o marca ambiguo.
6. Registra capacidades sin match como **fuera de mapeo** (no inventes).
7. Produce matriz capacidad → Service Domain → evidencia.

## Salida

```md
## Mapeo Service Domains
- Versión BIAN:
- Fuentes:

| Capacidad | Service Domain | Evidencia (URL/path/release) | Confianza |
|---|---|---|---|

### Fuera de mapeo
- ...

### Conflictos / ambigüedades
- ...
```

## Casos límite

- Capacidad transversal (p. ej. auditoría) → varios SDs candidatos: no fusiones; documenta partición o escala.
- Rename entre versiones → usa nombre de la versión de trabajo + alias previo.
- Solo nombre informal de negocio → busca evidencia; si no hay, hueco.

## Validación

- Ningún Service Domain sin evidencia.
- Versión BIAN explícita.
- Fuera de mapeo listado cuando aplique.

## Criterios de terminado

- Matriz usable por skills de CR/API/handoff.
- Cero invención.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Capacidad “gestión de cuenta corriente” + acceso a catálogo V14 | SD(s) citados con evidencia |
| Ambiguo | Descripción vaga “motor de pagos” | Descomposición + varios candidatos o huecos; sin inventar |
| Límite | Capacidad sin match en release | Fuera de mapeo; no inventar SD |

## Fuentes

- https://bian.org/deliverables/service-landscape/ (V14.0, 2026-02) — consultado 2026-08-04.
- BIAN v14.0 Release Notes — https://bian.org/wp-content/uploads/2026/02/BIAN-v14.0-Release-Notes-v1.0_-Final-Version.pdf
- https://github.com/bian-official/public — release14.0.0
- `references/metamodelo-bian-operativo.md`
