---
name: elaborar-plan-cuenta-b2b
description: Elabora o actualiza un plan de cuenta estratégica B2B vivo (paisaje, value map, señales, relaciones, acciones con dueños). Úsala cuando se pida account plan SAM, no un pitch genérico ni un playbook de enablement.
metadata:
  author: yzylabs
  version: "1.0"
---

# Elaborar plan de cuenta B2B

## Propósito

Convertir una cuenta Tier 1/2 en un sistema operable: alineado a prioridades del cliente, con señales, cobertura relacional y acciones con dueño — no un documento anual archivado.

## Entradas

- Cuenta nombrada + tier aprobado o provisional.
- Contexto comercial (contrato, pipeline, competencia).
- Prioridades del cliente (fuentes publicadas si existen).
- Mapa de stakeholders previo (si existe).
- Restricciones de pricing/legal/producto.

## Procedimiento

1. Completa **Account landscape** (org, prioridades, competencia, contrato) citando fuentes.
2. Construye **Value map**: prioridad del cliente ↔ oferta nuestra ↔ evidencia de valor.
3. Inicializa **Signal dashboard** con triggers materiales y protocolo de refresh.
4. Integra o solicita **Relationship map** (multi-thread obligatorio en Tier 1).
5. Define **Action plan** trimestral: acción → señal/objetivo → owner → due → dependencia.
6. Define cadencia (mensual táctico / trimestral estratégico) y criterio de freshness (~60 días).
7. Usa `references/plantilla-plan-cuenta.md` como esqueleto.
8. Lista escalamientos (Legal, Enablement, Producto) sin improvisar autoridad.

## Salida

```md
## Cuenta / Tier / Freshness
## Landscape
## Value map
## Signals
## Relationships (resumen + gaps)
## Action plan
## Cadencia
## Riesgos / DELEGATION_REQUIRED
```

## Casos límite

- Sin prioridades del cliente → co-discovery planificado; no inventes strategy deck.
- Plan existente stale → refresh diferencial (qué cambió), no reescritura ciega.
- Solo se pide “deck bonito” → entrega plan operable + rechaza estética sin dueños.

## Validación

- Cinco componentes presentes o gap explícito.
- Acciones con owner + due.
- Multi-thread evaluado en Tier 1.
- Sin precios/cláusulas inventadas.

## Criterios de terminado

- El equipo puede ejecutar la próxima acción sin reinterpretar el plan.
- Freshness y próxima revisión están fechadas.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Cuenta Tier 1 con contrato y 3 stakeholders | Plan 5 componentes + acciones Q |
| Ambiguo | “Haz un account plan” sin cuenta | Pregunta bloqueante + plantilla mínima |
| Límite | Plan de hace 9 meses sin updates | Marcado stale + refresh + riesgos |

## Fuentes

- SAMA — Strategic Account Business Value Plan / SAM Process — https://strategicaccounts.org/sama-fundamentals/ (2026-08-04).
- Salesmotion — five-component framework — https://salesmotion.io/blog/strategic-account-planning-top-companies (2026-08-04).
- Fullcast — Strategic Account Plan Template — https://www.fullcast.com/content/strategic-account-plan-template/ (2026-08-04).
- `references/plantilla-plan-cuenta.md`
