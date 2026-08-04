---
name: planificar-estudio-usuarios
description: Diseña el plan de estudio UX (participantes, tareas, ética, logística, métricas y pilot). Úsala cuando el método ya está elegido y hace falta un protocolo ejecutable y compartible.
metadata:
  author: yzylabs
  version: "1.0"
---

# Planificar estudio de usuarios

## Propósito

Convertir el método elegido en un plan de estudio verificable, ético y listo para ejecutar o handoff.

## Entradas

- Preguntas de investigación y método seleccionado.
- Perfiles de usuario objetivo.
- Artefacto a evaluar (concepto, prototipo, producción).
- Restricciones legales/compliance y canales de reclutamiento.

## Procedimiento

1. Define objetivos del estudio en una frase.
2. Especifica perfiles de participantes y criterios de inclusión/exclusión.
3. Fija tamaño de muestra según tipo:
   - Cualitativo usability: ~5 por grupo homogéneo (ajustar 3–4/grupo si hay varios grupos).
   - Cuantitativo / benchmarking: N sustancialmente mayor; no uses N=5 para “estadística”.
4. Escribe tareas o temas de entrevista alineados a objetivos (escenarios realistas, no instrucciones de UI).
5. Decide formato: moderado/no moderado, remoto/presencial, scripted vs natural.
6. Define métricas solo si el diseño del estudio las soporta (éxito, tiempo, errores, satisfacción).
7. Redacta requisitos de consentimiento informado (propósito, datos, retención, retiro, observadores).
8. Planifica pilot (1 sesión) y checklist logística.
9. Documenta el test plan compartible con el equipo.

## Salida

```md
## Test plan
- Producto / artefacto
- Objetivos
- Formato y logística
- Perfiles y N
- Tareas / guion (resumen)
- Métricas / cuestionarios
- Ética y consentimiento
- Pilot
- Roles (moderador, notetaker, observadores)
```

## Casos límite

- Vulnerable populations / temas sensibles: escala a Nami; no improvises.
- Stakeholders quieren observar en vivo: define protocolo de observadores y consentimiento.
- Sin tiempo de pilot: marca riesgo alto de protocolo defectuoso.

## Validación

- Tareas mapean 1:1 a objetivos.
- N justificado por tipo de estudio.
- Consentimiento cubre grabación/PII si aplica.
- Plan cabe en una página operativa + anexos.

## Criterios de terminado

- Otro moderador podría ejecutar el estudio con el plan.
- Ética no es un checkbox vacío.

## Casos de evaluación

| Caso | Entrada | Esperado |
|---|---|---|
| Normal | Usability test de flujo de transferencia | Plan con 5 usuarios, 4–6 tareas, consentimiento |
| Ambiguo | “Organiza interviews” | Exige perfiles + temas + N + ética |
| Límite | “40 métricas con 5 usuarios” | Separa cuali; rechaza cuanti inválido |

## Fuentes

- NN/g — Checklist for Planning Usability Studies (consultado 2026-08-04).
- NN/g — How Many Test Users in a Usability Study? (consultado 2026-08-04).
- NN/g — Obtaining Consent for User Research (consultado 2026-08-04).
- GOV.UK — Getting informed consent for user research (consultado 2026-08-04).
