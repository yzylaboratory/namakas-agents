---
name: evaluar-arquitectura-solucion
description: Evalúa una arquitectura de solución frente a stakeholders, concerns, vistas y NFR, produciendo veredicto aceptar/condicionar/rechazar. Úsala cuando se pida design review, revisión de RFC/C4, fitness de arquitectura o análisis de trade-offs de una solución concreta.
metadata:
  author: yzylabs
  version: "1.0"
---

# Evaluar arquitectura de solución

## Propósito

Revisar un diseño concreto con rigor suficiente para decidir avance, usando vocabulario de descripción de arquitectura (stakeholders/concerns/views) y trade-offs explícitos — sin exigir un deliverable 42010 ceremonial completo.

## Entradas

- Propuesta de diseño (diagramas, RFC, narrativa, ADRs relacionados).
- Sistema de interés y alcance.
- NFR y restricciones conocidas.
- Principios/estándares del departamento.

## Procedimiento

1. Identifica sistema de interés y stakeholders relevantes.
2. Lista concerns materiales (propósito, interoperabilidad, seguridad, operabilidad, costo, evolución).
3. Selecciona vistas mínimas necesarias (p. ej. contexto, contenedores, runtime/eventos, despliegue) según concerns — no inventes vistas vacías.
4. Analiza trade-offs: acoplamiento, consistencia, latencia, resiliencia, team topology, lock-in.
5. Busca riesgos: SPOF, bounded contexts difusos, trust boundaries omitidos, deuda no nombrada.
6. Emite veredicto:
   - **Aceptar** — alineado a principios y NFR con evidencia.
   - **Condicionar** — avance con condiciones verificables.
   - **Rechazar** — rediseño requerido; indica por qué.
7. Indica qué debe ir a Enel / Fujitora / Wapol / Robin / Franky.

## Salida

```md
## Sistema de interés
## Stakeholders y concerns
## Vistas usadas
## Trade-offs
## Riesgos
## Veredicto
## Condiciones (si aplica)
## Handoffs
```

## Casos límite

- Solo diagrama sin NFR: condicionar o rechazar por evidencia insuficiente.
- Over-architecture para problema local: rechazar complejidad; proponer corte mínimo.
- Conflicto con estándar OB/API: escalar a Jinbe/Robin; no redefinir contratos aquí.

## Validación

- Concerns cubiertos o marcados como fuera de alcance.
- Veredicto con criterios observables.
- No se fingió conformidad ISO 42010 completa si solo hay review ligero.
- Handoffs a especialistas correctos.

## Criterios de terminado

- Veredicto usable por Luffy/implementación.
- Riesgos y condiciones explícitos.
- Próximo paso claro.

## Fuentes

- ISO/IEC/IEEE 42010:2022 — Architecture description — https://standards.ieee.org/ieee/42010/6846/ (2026-08-04)
- ISO/IEC/IEEE 42010 conceptual model — http://www.iso-architecture.org/42010/ (2026-08-04)
- The Open Group — TOGAF architecture compliance / review practices (síntesis) — 2026-08-04
