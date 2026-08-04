---
name: gobernar-versionado-deprecacion-api
description: Gobierna versionado, deprecación y migración de APIs públicas/partner (majors, convivencia, notices). Úsala cuando haya breaking changes, soporte multi-versión o alineación a estándares Open Banking.
metadata:
  author: yzylabs
  version: "1.0"
---

# Gobernar versionado y deprecación de API

## Propósito

Proteger a consumidores externos ante el cambio: reglas de versionado, ventanas de soporte, comunicación y guías de migración alineadas a prácticas de ecosistema.

## Entradas

- Contrato/OpenAPI actual y propuesto.
- Lista de breaking vs non-breaking changes.
- Compromisos con partners / estándar regional.
- Capacidad de gateway para multi-versión.

## Procedimiento

1. Clasifica cambios: additive compatible vs breaking (campos removidos, semántica alterada, auth).
2. Elige estrategia de versionado pública (p. ej. URL `/v1` `/v2` + OpenAPI por major).
3. Define política de convivencia: cuántos majors, tiempo mínimo de soporte post-deprecación.
4. Redacta notice de cambio: qué, cuándo, impacto, acción requerida, ambiente (sandbox/prod).
5. Exige changelog y guía de migración con mapeo campo/operación.
6. Alinea con patrones regionales cuando aplique (p. ej. OBL notification via developer portal; majors FDX/Berlin Group).
7. Verifica que docs del major antiguo no desaparezcan en un 404 inmediato.
8. Entrega calendario de deprecación y owners de comunicación.

## Salida

```md
## Clasificación de cambios
## Estrategia de versionado
## Política de convivencia / soporte
## Notice de cambio
## Changelog + migración
## Calendario
## Owners
```

## Casos límite

- Breaking sin major → rechaza publicación; exige major o compat shim temporal documentado.
- Estándar externo impone timeline → no inventes fechas; cita el estándar/OBL notice rules.
- Partners sin canal de aviso → bloquea deprecación hasta definir notificación.

## Validación

- Breaking changes tienen major o excepción firmada (no improvisada).
- Notice incluye fechas e impacto.
- OpenAPI por major separado cuando se usen majors.
- Portal/docs del major previo planificados.

## Criterios de terminado

- Política usable por gateway, portal y soporte.
- Riesgos de ruptura de partners cuantificados.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Remover campo published en AIS | Major v2 + guía migración + ventana soporte |
| Ambiguo | “Actualizar la API” | Clasificación change-by-change + preguntas |
| Límite | Estándar OBL nuevo obligatorio | Calendario alineado a notice-of-change + portal |

## Fuentes

- UK OBL — Implementation of a new Standard — https://standards.openbanking.org.uk/operational-guidelines/change-and-communication-management/implementation-of-a-new-obl-standard/latest/ (2026-08-04).
- UK OBL — Notification of a Change — https://standards.openbanking.org.uk/operational-guidelines/change-and-communication-management/notification-of-a-change/v3-1-9/ (2026-08-04).
- UK Open Banking API Specs v4.0.1 — https://standards.openbanking.org.uk/api-specifications/latest/ (2026-08-04).
- Zuplo Versioning — https://zuplo.com/docs/articles/versioning-on-zuplo (2026-08-04).
- APIScout portal versioning guidance — https://apiscout.dev/guides/building-developer-portal-api-2026 (2026-08-04).
- Berlin Group NextGenPSD2 downloads — https://www.berlin-group.org/nextgenpsd2-downloads (2026-08-04).
- FDX API overview — https://ozoneapi.com/the-open-finance-tracker/library/fdx-api-financial-data-exchange/ (2026-08-04).
