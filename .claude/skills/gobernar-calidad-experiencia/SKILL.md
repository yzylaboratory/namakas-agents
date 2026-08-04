---
name: gobernar-calidad-experiencia
description: Define y aplica gates de calidad UX (heurísticas, estados, consistencia, handoff). Úsala cuando se pida critique de diseño, checklist de calidad, DesignOps liviano o aprobación de handoff a ingeniería.
metadata:
  author: yzylabs
  version: "1.0"
---

# Gobernar calidad de experiencia

## Propósito

Establecer y ejecutar barras de calidad de experiencia antes de handoff, usando criterios observables (no gusto personal).

## Entradas

- Flujos/pantallas/prototipo a evaluar.
- Principios de producto y design system aplicable.
- Nivel de riesgo del journey (crítico vs cosmético).
- Restricciones de plataforma y contenido.

## Procedimiento

1. Fija el alcance de review (flujo completo vs pantalla).
2. Evalúa contra heurísticas de usabilidad (NN/g 10) y principios locales.
3. Verifica estados obligatorios: vacío, carga, error, éxito, permisos, offline si aplica.
4. Revisa consistencia con sistema (componentes, spacing, tipografía, iconografía) a nivel director; detalle → Miss Goldenweek/Perona.
5. Revisa claridad de copy de UI y jerarquía visual (escalar microcopy largo a Vivi).
6. Define severidad de hallazgos (bloqueante / mayor / menor) y dueño de fix.
7. Emite veredicto: **aprobado** / **aprobado con limitaciones** / **rechazado** para handoff.
8. Adjunta checklist DesignOps mínima (assets, specs, comportamiento, a11y notes).

## Salida

```md
## Review de calidad UX
- Alcance:
- Veredicto:
## Hallazgos
| ID | Heurística/principio | Severidad | Evidencia | Dueño |
## Estados cubiertos / faltantes
## Consistencia de sistema
## Checklist de handoff
## Riesgos residuales
```

## Casos límite

- Solo mock estático: limita veredicto; exige prototipo o especificación de interacción para journeys críticos.
- Conflicto con “pixel perfect” sin usabilidad: rechaza handoff bloqueante.
- Design system incompleto: documenta excepciones temporales con fecha de intake.

## Validación

- Hallazgos son accionables y severizados.
- Veredicto explícito.
- No se declara COMPLETED de craft ajeno.

## Criterios de terminado

- Gate de calidad usable por Frontend/QA.
- Dueños de fix asignados.
- Riesgos residuales visibles para Luffy.

## Fuentes

- Nielsen Norman Group — 10 Usability Heuristics for User Interface Design — https://www.nngroup.com/articles/ten-usability-heuristics/ (consultado 2026-08-04)
- ISO 9241-110 — Dialogue principles (referencia) — consultado 2026-08-04
- Nielsen Norman Group — State of UX in 2026 (juicio crítico vs UI commodity) — https://www.nngroup.com/articles/state-of-ux-2026/ (2026-08-04)
