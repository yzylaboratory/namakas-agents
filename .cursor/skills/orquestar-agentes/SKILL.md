---
name: orquestar-agentes
description: Use esta skill cuando una misión requiera varios agentes o departamentos y sea necesario asignar responsabilidades, preparar delegaciones autocontenidas, decidir trabajo paralelo o secuencial y consolidar los resultados.
compatibility: Compatible con Claude Code y Cursor mediante el estándar Agent Skills.
---

# Orquestar agentes

## Propósito

Asignar el trabajo correcto al agente correcto y mantener una ejecución coherente.

## Entradas

- Misión alineada.
- Entregables.
- Prioridad.
- Mapa de agentes.
- Dependencias.

## Procedimiento

1. Clasifica cada tarea por dominio.
2. Selecciona un único responsable principal del **roster Nakamas** (`.cursor/agents/`).
3. Identifica revisores o agentes consultados.
4. Prepara una delegación autocontenida para cada responsable (`REPORT_TO` obligatorio).
5. Al lanzar Task / Custom Agent:
   - **FORBIDDEN** Task types Cursor genéricos (`shell`, `generalPurpose`, `explore`, `best-of-n-runner`, …) salvo pedido explícito de Randy.
   - Cadena: Luffy → Director → célula (célula directa solo si alcance unipersonal cerrado).
   - git/push/remoto/`gh` → Franky → Paulie.
   - `description` (título UI): preferir `{Especialista} ← {Director}: {acción}`; o `{Personaje}: {acción}` + `REPORT_TO` en el prompt (ver `00-Agentes-Generales/Luffy-Coordinador/Delegacion.md` HARD).
6. Decide qué tareas pueden ejecutarse en paralelo.
7. Evita conflictos sobre archivos, contratos o decisiones compartidas.
8. Define el formato de retorno.
9. Solicita evidencia y riesgos.
10. Consolida resultados y detecta contradicciones.
11. Devuelve correcciones al responsable original antes de reasignar.

## Validación de orquestación (añadida)

- Ningún Task usa `shell` / genéricos Cursor como trabajador Nakamas.
- La cadena Luffy→Director→célula (o célula justificada) es visible en `description` y/o `REPORT_TO`.
- Push/remoto no se enruta a un built-in genérico.

## Matriz RACI simplificada

Para cada tarea define:

- **Responsable:** ejecuta.
- **Aprobador:** acepta el resultado.
- **Consultado:** aporta conocimiento.
- **Informado:** necesita conocer el resultado.

Luffy conserva el rol de aprobador de la misión general, pero no sustituye aprobaciones legales, regulatorias, financieras o de seguridad.

## Contenido mínimo de una delegación

```md
Objetivo:
Contexto:
Alcance:
Fuera de alcance:
Entradas:
Restricciones:
Entregable:
Criterios de aceptación:
Dependencias:
Validación requerida:
```

## Regla de contexto

Asume que un agente delegado inicia sin conocer la conversación completa. Incluye toda la información necesaria para ejecutar la tarea sin adivinar decisiones previas.

## Regla de retorno

Solicita respuestas con:

- Resultado.
- Cambios o artefactos.
- Evidencia.
- Riesgos.
- Decisiones requeridas.
- Dependencias desbloqueadas.

## Validación

- No existen tareas sin responsable.
- No existen dos responsables principales para la misma tarea.
- Las delegaciones son autocontenidas.
- El paralelismo no crea conflictos.
- Cada entrega tiene criterios verificables.
