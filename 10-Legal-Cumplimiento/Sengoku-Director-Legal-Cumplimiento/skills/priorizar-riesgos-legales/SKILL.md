---
name: priorizar-riesgos-legales
description: Prioriza riesgos legales y de cumplimiento con impacto, probabilidad, plazo y residual risk. Úsala cuando haya backlog legal, incidentes, cambios normativos o conflicto de prioridad entre privacidad, Open Finance y contratos.
metadata:
  author: yzylabs
  version: "1.0"
---

# Priorizar riesgos legales

## Propósito

Ordenar el trabajo del departamento con criterios verificables para que Corazon, Tsuru y Cobra (o Luffy) sepan qué atacar primero.

## Entradas

- Lista de temas / hallazgos / obligaciones.
- Jurisdicción y producto afectados.
- Plazos regulatorios o contractuales conocidos.
- Capacidad del squad y dependencias externas.

## Procedimiento

1. Normaliza cada ítem: descripción, jurisdicción, actor, fuente (si hay).
2. Puntúa impacto (legal, reputacional, operativo) y probabilidad; anota detectabilidad.
3. Marca deadline duro (norma, contrato, auditoría) vs blando.
4. Clasifica Now / Next / Later con dueño (célula o Sengoku).
5. Define residual risk aceptable solo con decisión explícita (quién acepta).
6. Señala dependencias (Jinbe, Robin, Law, counsel) que bloquean mitigación.
7. Revisa si un ítem “Next” se vuelve “Now” por cambio normativo.

## Salida

```md
## Resumen ejecutivo
## Matriz Now / Next / Later
| ID | Riesgo | Impacto | Prob. | Plazo | Dueño | Residual | Dependencias |
## Decisiones de apetito requeridas
## Bloqueos
```

## Casos límite

- Datos insuficientes: clasifica como “triage pendiente” con preguntas concretas; no inventes severidad.
- Dos Now con dueño distinto: define secuencia o pide decisión a Luffy si compiten por el mismo journey.
- Stub de célula dueña: prioriza igual; marca ejecución `BLOCKED` + forja requerida.

## Validación

- Cada Now tiene dueño y criterio de salida.
- No hay “prioridad alta” sin justificación.
- Residual risk tiene aceptante o queda abierto.

## Criterios de terminado

- Backlog priorizado accionable.
- Escalados a Luffy explícitos si hace falta apetito de negocio.

## Fuentes

- Enfoque risk-based CMS — ISO 37301:2021 (obligations + compliance risk) — consultado 2026-08-04
- Principio de accountability / riesgos a derechos — GDPR Art. 24–25 / EDPB Guidelines 4/2019 — consultado 2026-08-04
