---
name: definir-flujo-interaccion
description: Define flujos pantalla-a-pantalla, microinteracciones y criterios de aceptación UI. Úsala cuando haya que mapear journeys de interfaz, feedback y unhappy paths — no para research etnográfico ni historias de usuario largas de producto.
metadata:
  author: yzylabs
  version: "1.0"
---

# Definir flujo de interacción

## Propósito

Documentar cómo el usuario atraviesa pantallas y qué feedback recibe en cada paso, incluyendo recuperación ante errores.

## Entradas

- Objetivo del flujo y actor.
- Pantallas o layouts involucrados.
- Reglas de negocio conocidas (permisos, validaciones).
- Restricciones de plataforma (gestos, teclado, back).
- Research o supuestos explícitos.

## Procedimiento

1. Nombra el flujo y el resultado de éxito.
2. Lista pasos felices (happy path) con pantalla + acción + feedback.
3. Añade ramas: empty, error, denegado, timeout, offline, cancelación.
4. Define navegación (push, modal, tabs, deep link) y comportamiento de atrás.
5. Especifica microinteracciones críticas (debounce, optimistic UI, undo).
6. Escribe criterios de aceptación UI verificables (Given/When/Then o checklist).
7. Marca dependencias de backend/copy/DS; escala si bloquean.

## Salida

```md
# Flujo — [Nombre]

## Éxito
[resultado observable]

## Happy path
1. [Pantalla] — acción → feedback

## Ramas
| Condición | Pantalla/estado | Feedback | Recuperación |

## Criterios de aceptación UI
- [ ] …

## Dependencias / riesgos
- …
```

## Casos límite

- Flujo sin pantallas definidas: produce esqueleto + pide layouts.
- Confirmaciones excesivas: una confirmación solo para acciones destructivas.
- Optimistic UI: documenta rollback visible si falla.
- Accesibilidad: todo feedback también disponible sin solo-color / solo-toast efímero.

## Validación

- Happy path y al menos empty + error cubiertos o N/A justificado.
- Criterios de aceptación son observables.
- No inventa reglas de negocio.

## Criterios de terminado

- Mapa de flujo entregado.
- Ramas críticas documentadas.
- Criterios UI listos para QA.

## Evaluación sugerida

| Caso | Entrada | Esperado |
|---|---|---|
| Normal | Checkout 3 pasos | Happy + error pago + atrás |
| Ambiguo | “Hazlo fluido” | Preguntas; microinteracciones mínimas |
| Límite | Permiso denegado mid-flow | Estado explícito + ruta de recuperación |

## Fuentes

- W3C WCAG 2.2 — operable / understandable (2026-08-04) — https://www.w3.org/TR/WCAG22/
- Apple HIG — App architecture / navigation patterns (2026-08-04) — https://developer.apple.com/design/human-interface-guidelines/
