---
name: delimitar-mision-descubrimiento
description: Delimita preguntas de exploración, alcance, profundidad y criterios de “suficiente” antes de mapear un sistema. Úsala cuando la misión de reconocimiento esté ambigua o el riesgo de over-exploration sea alto.
metadata:
  author: yzylabs
  version: "1.0"
---

# Delimitar misión de descubrimiento

## Propósito

Convertir un pedido vago (“explora esto”) en una misión de reconocimiento acotada y verificable.

## Entradas

- Objetivo o decisión a desbloquear.
- Contexto disponible (repos, docs, rumores).
- Restricciones de tiempo, acceso y solo lectura.
- Consumidor previsto del informe.

## Procedimiento

1. Reformula el objetivo en una decisión concreta que el mapa debe habilitar.
2. Lista 3–8 preguntas de descubrimiento priorizadas.
3. Define alcance incluido y fuera de alcance.
4. Elige profundidad: recon rápido, mapa estructural o recon profundo.
5. Identifica entradas mínimas necesarias y bloqueos de acceso.
6. Acuerda criterios de “suficiente para decidir”.
7. Declara qué no se explorará aunque sea interesante.
8. Confirma modo solo lectura y entornos permitidos.

## Salida

```md
## Decisión a desbloquear
## Preguntas de descubrimiento
## Alcance / Fuera de alcance
## Profundidad elegida
## Entradas y bloqueos
## Criterios de suficiente
## Consumidor del handoff
```

## Casos límite

- El usuario pide “mapear todo”: exige priorización por decisión o riesgo.
- No hay acceso al código: delimita investigación documental y marca bloqueos.
- Caso ambiguo: propón dos profundidades (rápida vs profunda) y recomienda una.

## Validación

- Existe una decisión clara a desbloquear.
- Hay preguntas concretas, no genéricas.
- Fuera de alcance explícito.
- Profundidad justificada.

## Criterios de terminado

- La misión cabe en un párrafo.
- Un explorador distinto podría ejecutarla sin adivinar.
- Los criterios de suficiente son observables.

## Casos de evaluación

| Caso | Entrada | Esperado |
|---|---|---|
| Normal | “Antes de migrar pagos, ¿qué hay en el monolito?” | Preguntas sobre módulos de pagos, deps, entry points; profundidad estructural |
| Ambiguo | “Explora el sistema” | Exige decisión + propone alcance mínimo |
| Límite | “Documenta toda la empresa” | Rechaza alcance infinito; pide perímetro y priorización |

## Fuentes

- Rol y Reglas de Noland-Explorador (pasadas y profundidad).
- Cursor Subagents — agentes focused / readonly (consultado 2026-08-04).
