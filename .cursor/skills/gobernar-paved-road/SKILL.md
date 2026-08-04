---
name: gobernar-paved-road
description: Gobierna golden paths / paved roads (ownership, versionado, deprecación, escape hatches y guardrails). Úsala cuando se defina o audite el camino soportado de desarrollo→producción, templates de plataforma o políticas de cambio breaking para consumidores internos.
metadata:
  author: yzylabs
  version: "1.0"
---

# Gobernar paved road / golden paths

## Propósito

Definir y mantener el camino soportado que reduce carga cognitiva, con límites claros y escapes controlados — sin convertir la plataforma en golden cage ni en anarquía de tools.

## Entradas

- Journeys candidatos (nuevo servicio, deploy, hotfix, entorno efímero, etc.).
- Templates/capacidades existentes y sus dueños.
- Política de seguridad baseline y consumidores actuales.
- Historial de workarounds / shadow IT conocidos.

## Procedimiento

1. Inventaria paths: nombre, journey cubierto, owner, versión, estado (supported / experimental / deprecated).
2. Para cada path soportado define:
   - Entrada/salida del journey.
   - Guardrails automáticos (lint, policy-as-code, required checks).
   - Observabilidad y rollback mínimos.
   - Escape hatch: cuándo se permite salir, quién aprueba, caducidad.
3. Define política de cambio: SemVer o esquema equivalente, ventana de deprecación, canal de comunicación.
4. Identifica anti-patrones activos (ticket-ops, ivory tower, one-size-fits-all) y acciones correctivas.
5. Propón scorecard de adopción y task success por path.
6. Escala a Fujitora si el path implica controles de seguridad estructurales nuevos.

## Salida

```md
## Catálogo de golden paths
| Path | Journey | Owner | Versión | Estado | Escape hatch |
## Política de cambio / deprecación
## Guardrails
## Scorecard de adopción
## Workarounds a eliminar
## Riesgos y escalamientos
```

## Casos límite

- Equipo con requisito legítimo fuera del path: escape hatch con dueño y fecha; no “no” absoluto sin alternativa.
- Path sin owner: no puede ser `supported`; baja a experimental o se asigna owner.
- Deprecación sin consumidores migrados: bloquea removal; plan de migración obligatorio.

## Validación

- Todo path `supported` tiene owner y versión.
- Hay política de deprecación escrita.
- Escape hatches no son el camino por defecto.

## Criterios de terminado

- Catálogo usable por equipos consumidores y por el squad.
- Cambios breaking tienen plan de comunicación.
- Gaps de guardrails explícitos.

## Fuentes

- DORA Platform engineering — golden paths, shift down, extensibility, pitfalls — https://dora.dev/capabilities/platform-engineering/ (consultado 2026-08-04)
- CNCF Platforms White Paper — platform as curated capabilities for internal customers (consultado 2026-08-04)
