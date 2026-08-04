---
name: cubrir-estados-vacios-error
description: Diseña y especifica estados vacíos, carga, error y éxito de una interfaz. Úsala cuando falten empty/error/loading states o cuando se revise una pantalla “feliz” sin unhappy paths.
metadata:
  author: yzylabs
  version: "1.0"
---

# Cubrir estados vacíos y error

## Propósito

Asegurar que cada superficie de UI tenga estados no-felices útiles: qué ve el usuario, qué puede hacer y cómo se recupera.

## Entradas

- Pantalla o componente objetivo.
- Fuentes de datos / condiciones de fallo conocidas.
- Tono de marca y microcopy existente.
- Patrones del DS para empty/error/skeleton.

## Procedimiento

1. Lista superficies que muestran datos o acciones (listas, detalles, forms, modales).
2. Para cada una define: loading, empty, error, success (si aplica), partial.
3. Empty: explica por qué está vacío + CTA primario (si hay acción).
4. Error: causa en lenguaje de usuario + recuperación (reintentar, soporte, atrás).
5. Loading: skeleton vs spinner; evita layout shift brusco.
6. Verifica que el estado no dependa solo del color; texto legible.
7. Entrega tabla + microcopy corto; escala prosa larga a Vivi si hace falta.

## Salida

```md
# Estados — [Pantalla/Componente]

| Superficie | Loading | Empty | Error | Success | Notas |
|---|---|---|---|---|---|

## Microcopy
| Estado | Título | Cuerpo | CTA |

## Riesgos
- …
```

## Casos límite

- Empty vs error de permisos: no digas “no hay datos” si es 403.
- Empty de onboarding: CTA de creación, no mensaje de fallo.
- Errores técnicos crudos: traducir; correlacionar id solo si ayuda a soporte.
- Multi-error en form: resumen + enlace a campos.

## Validación

- Toda superficie de datos del alcance tiene empty + error o N/A.
- CTAs de recuperación son accionables.
- Sin PII en ejemplos.

## Criterios de terminado

- Tabla de estados completa.
- Microcopy mínimo definido o marcado pendiente.
- Riesgos listados.

## Evaluación sugerida

| Caso | Entrada | Esperado |
|---|---|---|
| Normal | Inbox vacío | Empty + CTA “Nuevo” |
| Ambiguo | “Ponle un empty chulo” | Empty útil + tono; no ornamentar |
| Límite | API 500 intermitente | Error + reintentar + no perder input |

## Fuentes

- W3C WCAG 2.2 — 3.3 Input Assistance (2026-08-04) — https://www.w3.org/TR/WCAG22/
- Apple HIG — Feedback / empty states patterns (2026-08-04) — https://developer.apple.com/design/human-interface-guidelines/
