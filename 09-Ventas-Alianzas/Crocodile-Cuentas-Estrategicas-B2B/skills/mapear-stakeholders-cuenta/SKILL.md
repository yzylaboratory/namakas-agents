---
name: mapear-stakeholders-cuenta
description: Mapea el comité de compra y poder en una cuenta B2B (roles, disposición, cobertura, gaps) y exige multi-threading. Úsala cuando haya que entender quién decide, quién bloquea o dónde hay single-thread risk.
metadata:
  author: yzylabs
  version: "1.0"
---

# Mapear stakeholders de cuenta

## Propósito

Hacer visible la política de la cuenta: roles, influencia, disposición y cobertura interna — para protegerse del riesgo de un solo champion y alinear al equipo multifuncional.

## Entradas

- Cuenta y contexto org (org chart si existe).
- Contactos conocidos (CRM, emails, reuniones).
- Equipo interno asignado a la cuenta.
- Objetivo (ganar, expandir, renovar, recuperar).

## Procedimiento

1. Lista personas relevantes (no inventes nombres; marca `unknown` donde falte).
2. Clasifica roles: decision-maker, economic buyer, influencer, champion, blocker, coach.
3. Evalúa disposición (aliado / neutral / detractor) y fuerza de relación (alta/media/baja/ninguna).
4. Asigna cobertura interna (quién de nosotros tiene relación) y gaps.
5. Detecta single-thread risk y propone multi-thread targets.
6. Identifica necesidad de executive sponsor interno y stakeholders del cliente a elevar.
7. Entrega mapa + plan de engagement (sin scripts manipulativos).

## Salida

```md
## Objetivo de mapeo
## Mapa
| Persona | Rol | Disposición | Cobertura interna | Fuerza | Notas |
## Single-thread risks
## Multi-thread plan
## Executive sponsor (sí/no + candidato)
## Datos faltantes
```

## Casos límite

- Solo hay un contacto conocido → mapa parcial + riesgo crítico + acciones de descubrimiento.
- Org chart secreto → trabaja con roles funcionales y gaps, no inventes organigrama.
- Conflicto ético (pedir “bypass” a compliance) → escala a Buggy/Legal; no diseñes engaño.

## Validación

- Roles etiquetados con definición clara.
- Gaps de cobertura explícitos.
- Multi-thread plan con dueños si hay riesgo.
- Sin personas inventadas presentadas como hecho.

## Criterios de terminado

- El plan de cuenta puede referenciar el mapa.
- Single-thread risks tienen mitigación o escalamiento.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | 6 contactos con roles mixtos | Mapa completo + gaps menores |
| Ambiguo | “Habla con el cliente” | Pregunta de contactos + mapa mínimo de roles faltantes |
| Límite | Un solo champion silencioso | Riesgo crítico + multi-thread + trigger de señal |

## Fuentes

- Fullcast — stakeholder mapping in account plans — https://www.fullcast.com/content/strategic-account-plan-template/ (2026-08-04).
- Salesmotion — Relationship Map component — https://salesmotion.io/blog/strategic-account-planning-top-companies (2026-08-04).
- SAMA — Multifunctional Account Team Leadership — https://strategicaccounts.org/sama-fundamentals/ (2026-08-04).
