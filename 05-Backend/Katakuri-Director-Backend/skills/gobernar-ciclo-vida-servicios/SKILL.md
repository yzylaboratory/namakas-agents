---
name: gobernar-ciclo-vida-servicios
description: Define y aplica gobierno del ciclo de vida de microservicios internos (ownership, versionado, deprecación, contratos, SLOs, migraciones). Úsala cuando se pida política de servicios, catálogo backend, breaking changes o paved road de despliegue.
metadata:
  author: yzylabs
  version: "1.0"
---

# Gobernar ciclo de vida de servicios

## Propósito

Establecer guardrails de producto técnico y operación para servicios backend, de modo que el departamento sea predecible, operable y seguro.

## Entradas

- Catálogo o lista de servicios candidatos/existentes.
- Contratos existentes (OpenAPI/AsyncAPI/schemas).
- Modelo de consumidores (internos, BFF, partners vía otros depts).
- Restricciones de SLO, compliance y plataforma.

## Procedimiento

1. Clasifica cada servicio: **dominio**, **plataforma**, **adaptador/integración**, **experimental**.
2. Exige mínimo viable de gobierno por servicio compartido:
   - Owner de producto técnico + owner on-call.
   - Spec de API y/o contrato de eventos versionado.
   - Política de versionado y deprecación.
   - SLO/SLI básicos y alertas.
   - Plan de migración/rollback cuando toque datos.
3. Define reglas de cambio: qué es breaking; ventana mínima de aviso; convivencia de versiones.
4. Define paved road de release: ambientes, feature flags, contract tests, canary/blue-green si aplica (detalle de plataforma → Franky).
5. Preferir enforcement en CI (lint de specs, contract tests, checks de migración) sobre revisión manual de cada PR.
6. Produce checklist de go-live y lista de excepciones documentadas (con caducidad).

## Salida

```md
## Política de gobierno de servicios
## Inventario / gaps
| Servicio | Clase | Owner | Spec | SLO | Versión | Gap |
## Reglas de versionado y deprecación
## Paved road de release
## Guardrails automatizables
## Excepciones (con expiry)
## Riesgos
```

## Casos límite

- Servicio “shadow” sin owner: bloquear nuevos consumidores hasta asignar ownership.
- Breaking change urgente por seguridad: fast-track con comunicación y plan de rollback.
- Servicio financiero con PCI/PII: gates adicionales y escalamiento a Fujitora/Legal según alcance.

## Validación

- Todo servicio compartido listado tiene owner y contrato.
- Hay regla explícita de deprecación.
- Excepciones tienen fecha de revisión.

## Criterios de terminado

- Política o checklist aplicable por el squad y por Robin/Franky/QA.
- Gaps priorizados.
- Ninguna recomendación depende de un board manual como único control.

## Fuentes

- Azure Architecture Center — Microservices — https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/microservices (2026-08-04)
- 12-Factor App — config, disposability, logs — https://12factor.net/ (2026-08-04)
- Contract-first / OpenAPI como contrato — práctica contrastada 2026-08-04
