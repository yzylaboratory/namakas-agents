---
name: auditar-accesibilidad-interfaz
description: Audita pantallas o componentes UI contra WCAG 2.2 y produce hallazgos con severidad y remediación. Úsala cuando se pida revisión a11y de interfaz, contraste, foco, teclado o targets — no como dictamen legal de cumplimiento.
metadata:
  author: yzylabs
  version: "1.0"
---

# Auditar accesibilidad de interfaz

## Propósito

Evaluar una interfaz concreta frente a criterios WCAG 2.2 (nivel acordado, por defecto AA) y entregar un informe accionable.

## Entradas

- Pantallas, specs, capturas o código UI.
- Nivel objetivo (A / AA / AAA); default AA si no se indica.
- Plataforma y tecnologías (HTML, React Native, etc.) si se conocen.
- Restricciones (marca que fuerza bajo contraste, etc.).

## Procedimiento

1. Confirma alcance (pantallas) y nivel WCAG.
2. Revisa perceivable: texto alternativo, contraste (1.4.3/1.4.11), no solo-color.
3. Revisa operable: teclado, foco visible (2.4.7), foco no oscurecido (2.4.11), target size (2.5.8), gestos.
4. Revisa understandable: labels, errores, lenguaje, consistencia.
5. Revisa robust: name/role/value, estados programáticamente expuestos.
6. Clasifica hallazgos (blocker / major / minor) con criterio WCAG citado.
7. Propón remediación concreta; marca lo no verificable sin runtime.

## Salida

```md
# Auditoría a11y — [Alcance]
Nivel: WCAG 2.2 AA (u otro)

| ID | Criterio | Severidad | Hallazgo | Remediación | Evidencia |
|---|---|---|---|---|---|

## Resumen
- Blockers: N
- Majors: N
- Minors: N

## No verificado / fuera de alcance
- …
```

## Casos límite

- Solo mockup estático: limita a contraste/layout; marca teclado/SR como no verificado.
- AAA pedido sin mandato: aclara costo; audita AA + seleccionados AAA.
- Conflicto marca vs contraste: documenta riesgo; no “apruebes” por estética.
- No es dictamen legal ni certificación formal.

## Validación

- Cada hallazgo cita criterio WCAG 2.2.
- Severidades coherentes.
- Remediaciones accionables.

## Criterios de terminado

- Informe entregado con resumen.
- Alcance y limitaciones explícitos.
- Sin declaración de “100% conforme” sin evidencia runtime.

## Evaluación sugerida

| Caso | Entrada | Esperado |
|---|---|---|
| Normal | Form con placeholder como label | Hallazgo 1.3.1/3.3.2 + remediación |
| Ambiguo | “¿Es accesible?” sin pantallas | Pedir alcance; no inventar |
| Límite | Modal que tapa el foco | 2.4.11 + remediación |

## Fuentes

- W3C WCAG 2.2 (REC 2023-10-05; consultado 2026-08-04) — https://www.w3.org/TR/WCAG22/
- W3C WAI — WCAG 2 Overview (2026-08-04) — https://www.w3.org/WAI/standards-guidelines/wcag/
- W3C WAI — What's New in WCAG 2.2 (2026-08-04) — https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/
