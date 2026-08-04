---
name: seleccionar-metodo-ux
description: Selecciona métodos de UX research según actitud vs comportamiento, cuali vs cuanti, contexto de uso y fase del producto. Úsala cuando haya que justificar qué método usar (entrevista, usability test, survey, card sort, etc.).
metadata:
  author: yzylabs
  version: "1.0"
---

# Seleccionar método UX

## Propósito

Elegir el método mínimo adecuado a la pregunta, con justificación explícita y alternativas descartadas.

## Entradas

- Preguntas de investigación y fase (salida de `delimitar-pregunta-investigacion`).
- Acceso a usuarios, prototipo/producto, instrumentación analytics.
- Tiempo y presupuesto relativos.
- Restricciones (remoto, moderado, regulado).

## Procedimiento

1. Ubica cada pregunta en el marco NN/g de 3 dimensiones:
   - Actitudinal (dicen) vs comportamental (hacen).
   - Cualitativo (por qué / cómo arreglar) vs cuantitativo (cuántos / cuánto).
   - Contexto de uso: natural, scripted, limitado, sin producto.
2. Mapea a fase: Strategize (generativo) / Design (formativo) / Launch & Assess (sumativo).
3. Propón 1 método primario y opcionalmente 1 complementar (mixed-methods solo si aporta facetas distintas).
4. Descarta métodos populares pero inadecuados (p. ej. focus group para usabilidad fina).
5. Declara qué NO responderá el método elegido.
6. Si hay analytics: úsalos para priorizar preguntas, no como sustituto del “por qué”.
7. Documenta trade-offs de validez y costo.

## Salida

```md
## Pregunta(s)
## Posición en marco 3D
## Método primario (+ opcional secundario)
## Por qué este método
## Métodos descartados y por qué
## Qué no responderá este estudio
## Necesidades (prototipo, reclutamiento, tools)
```

## Casos límite

- Stakeholder pide survey para “entender por qué”: rechaza o combina con cualitativo.
- Sin acceso a usuarios reales: propone guerrilla / internal only con `COMPLETED_WITH_LIMITATIONS` o `BLOCKED`.
- Quieren A/B sin tráfico ni instrumentación: marca bloqueo técnico.

## Validación

- Método alineado a tipo de pregunta.
- Descarte justificado.
- Límites del método explícitos.

## Criterios de terminado

- Nami/Perona pueden entender por qué ese método y no otro.
- No hay “kitchen sink” de métodos sin razón.

## Casos de evaluación

| Caso | Entrada | Esperado |
|---|---|---|
| Normal | “¿Los usuarios encuentran el botón de pago?” | Usability testing comportamental cualitativo |
| Ambiguo | “Haz research del checkout” | Exige pregunta; propone método condicional |
| Límite | “Survey de 5 personas para métricas de conversión” | Rechaza cuanti con N=5; propone cuali o N mayor |

## Fuentes

- NN/g — When to Use Which UX Research Methods (consultado 2026-08-04).
- NN/g — Mixed-Methods Research (consultado 2026-08-04).
- Referencia interna: `07-UX-UI/Chopper-Investigacion-Usuario/references/framework-metodos-ux.md`.
