---
name: alinear-objetivo
description: Use esta skill cuando una solicitud sea amplia, ambigua o mezcle varios resultados y sea necesario convertirla en un objetivo principal, alcance, restricciones y criterios de éxito antes de planificar o delegar.
compatibility: Compatible con Claude Code y Cursor mediante el estándar Agent Skills.
---

# Alinear objetivo

## Propósito

Transformar una solicitud en una misión clara, medible y compartida por toda la tripulación.

## Entradas

- Solicitud del usuario.
- Contexto disponible.
- Restricciones conocidas.
- Artefactos o decisiones previas.

## Procedimiento

1. Resume la necesidad real en una oración.
2. Define un único objetivo principal.
3. Identifica el usuario, sistema o negocio beneficiado.
4. Separa:
   - Hechos confirmados.
   - Restricciones.
   - Supuestos.
   - Riesgos.
   - Dudas materiales.
5. Define qué está incluido y qué queda fuera.
6. Especifica resultados observables.
7. Establece criterios de éxito verificables.
8. Comprueba que el objetivo no describa una solución prematura.
9. Presenta una versión consolidada lista para planificación.

## Regla de aclaración

No interrumpas por detalles menores. Utiliza supuestos explícitos y reversibles.

Solicita una decisión únicamente cuando:

- Cambia materialmente el resultado.
- Tiene impacto legal, regulatorio, financiero o de seguridad.
- Es irreversible.
- No existe evidencia suficiente para recomendar una opción segura.

## Formato de salida

```md
## Misión

[Objetivo principal]

## Resultado esperado

[Resultado observable]

## Alcance incluido

- [...]

## Fuera de alcance

- [...]

## Restricciones

- [...]

## Supuestos

- [...]

## Criterios de éxito

- [...]

## Riesgos iniciales

- [...]
```

## Criterios de finalización

- Existe un único objetivo.
- El alcance es comprensible.
- Los supuestos son visibles.
- Los criterios pueden verificarse.
- La misión está lista para descomponerse.
