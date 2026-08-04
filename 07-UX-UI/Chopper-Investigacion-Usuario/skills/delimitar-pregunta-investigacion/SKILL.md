---
name: delimitar-pregunta-investigacion
description: Convierte un pedido vago de “investigar usuarios” en decisión a desbloquear, preguntas de investigación priorizadas y criterios de evidencia suficiente. Úsala cuando el brief de UX research esté ambiguo o mezcle discovery con validación.
metadata:
  author: yzylabs
  version: "1.0"
---

# Delimitar pregunta de investigación

## Propósito

Evitar estudios sin decisión: acotar qué se necesita aprender y cuándo hay evidencia “suficiente”.

## Entradas

- Pedido de stakeholders o brief de Nami.
- Producto / flujo / hipótesis (si existen).
- Restricciones de tiempo, acceso a usuarios y compliance.
- Consumidor previsto del handoff.

## Procedimiento

1. Reformula el pedido en una **decisión** concreta (priorizar, rediseñar, lanzar, matar concepto, etc.).
2. Clasifica la fase: generativa, formativa o sumativa (ISO 9241-210 / ciclo HCD).
3. Escribe 3–7 preguntas de investigación falsables y priorizadas.
4. Lista supuestos del equipo que deben verificarse o descartarse.
5. Define alcance incluido y fuera de alcance (qué no se investigará).
6. Acuerda criterios observables de “suficiente evidencia”.
7. Señala riesgos de sesgo (stakeholders como proxy de usuarios, confirmation bias).
8. Declara qué tipo de evidencia NO contará (opinión interna sin contraste).

## Salida

```md
## Decisión a desbloquear
## Fase (generativa | formativa | sumativa)
## Preguntas de investigación
## Supuestos a verificar
## Alcance / Fuera de alcance
## Criterios de evidencia suficiente
## Consumidor del handoff
## Riesgos de sesgo
```

## Casos límite

- “Valida que nuestra solución es correcta”: reformula a preguntas abiertas a falsación; marca riesgo de theatre.
- Solo hay stakeholders, no usuarios: delimita estudio con proxy y marca limitación explícita.
- Mezclan “entender mercado” + “pulir botón”: separa dos misiones o prioriza una.

## Validación

- Existe una decisión clara.
- Preguntas no son genéricas (“¿les gusta?”).
- Fuera de alcance explícito.
- Criterios de suficiente son observables.

## Criterios de terminado

- Un investigador distinto podría ejecutar el brief sin adivinar.
- Fase y tipo de pregunta están alineados.

## Casos de evaluación

| Caso | Entrada | Esperado |
|---|---|---|
| Normal | “Antes de rediseñar onboarding, ¿dónde abandonan?” | Preguntas sobre fricción/tareas; fase formativa o discovery según madurez |
| Ambiguo | “Investiga a los usuarios” | Exige decisión + propone 2–3 preguntas mínimas |
| Límite | “Demuestra que el nuevo diseño es mejor” | Reformula a evaluación falsable; advierte confirmation bias |

## Fuentes

- NN/g — UX Research Cheat Sheet (fases Discover/Explore/Test/Listen) (consultado 2026-08-04).
- ISO 9241-210:2019 — actividades HCD (contexto de uso → requisitos → evaluación) (consultado 2026-08-04).
