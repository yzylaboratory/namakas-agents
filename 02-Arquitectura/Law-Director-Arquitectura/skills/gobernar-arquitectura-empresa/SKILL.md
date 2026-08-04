---
name: gobernar-arquitectura-empresa
description: Opera el gobierno de arquitectura (principios, estándares, revisiones tipo ARB, compliance y excepciones). Úsala cuando se pida Architecture Board, gates de diseño, dispensas, compliance arquitectónico o modelo operativo de gobierno.
metadata:
  author: yzylabs
  version: "1.0"
---

# Gobernar arquitectura de empresa

## Propósito

Establecer y operar un modelo de gobierno que preserve la integridad de la arquitectura: quién decide, con qué criterios, cómo se revisa y cómo se gestionan excepciones.

## Entradas

- Principios y estándares vigentes (o borrador).
- Propuesta de cambio / RFC / diseño bajo revisión.
- Excepciones abiertas y ADRs previos.
- Nivel de riesgo e impacto (sistemas, datos, trust boundaries).

## Procedimiento

1. Clasifica el cambio: rutinario (guardrail), material (revisión), excepcional (dispensa).
2. Define o aplica el paquete mínimo de evidencia:
   - Concerns afectados.
   - Opciones y trade-offs.
   - NFR relevantes.
   - Impacto en estándares / paved road.
3. Ejecuta revisión estilo Architecture Board / ARB:
   - Cumple principios → aceptar.
   - Cumple con condiciones → condicionar (lista verificable).
   - Viola sin mitigación → rechazar o exigir rediseño.
4. Si hay excepción: documenta dueño, justificación, compensación, fecha de vencimiento y plan de retorno.
5. Actualiza el registro de decisiones / backlog de conformidad.
6. Prefiere automatizar criterios (lint de boundaries, checklists) cuando sea viable; no inventes burocracia.

## Salida

```md
## Clasificación del cambio
## Evidencia revisada
## Veredicto
- Aceptar | Condicionar | Rechazar | Dispensa
## Condiciones / compensación
## Excepción (si aplica)
| Dueño | Vence | Plan de retorno |
## Seguimiento
```

## Casos límite

- Urgencia de producción: dispensa temporal con vencimiento corto; no “aprobación eterna”.
- Estándar inexistente: fija principio mínimo temporal y agenda formalización; no fingas catálogo maduro.
- Revisión ceremonial sin concerns: devuelve REQUIRES_CORRECTION pidiendo paquete mínimo.

## Validación

- Veredicto explícito con criterios.
- Excepciones tienen dueño y vencimiento.
- No se confundió gobierno con implementación detallada.
- Fuentes de marco citadas cuando se invoca TOGAF/ARB.

## Criterios de terminado

- Decisión de gobierno accionable.
- Registro listo para Brook/ADR si es material.
- Próximo gate o seguimiento claro.

## Fuentes

- The Open Group — Architecture Board / Architecture Governance (TOGAF) — https://www.opengroup.org/architecture/ (2026-08-04)
- The Open Group — TOGAF® Standard, 10th Edition — EA Capability and Governance — https://publications.opengroup.org/c220 (2026-08-04)
