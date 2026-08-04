---
name: validar-agente-generado
description: Revisa estructura, frontmatter, coherencia, fuentes, permisos, solapamientos y criterios de terminado de un agente generado. Úsala siempre antes de marcar un agente como completado.
metadata:
  author: yzylabs
  version: "1.0"
---

# Validar agente generado

## Procedimiento

1. Ejecuta la validación automática.
2. Realiza la revisión semántica.
3. Ejecuta la revisión adversarial.
4. Corrige y repite hasta obtener un veredicto aceptable.

## Validación automática

Ejecuta:

```bash
python 00-Agentes-Generales/Vegapunk-Forjador-Agentes/scripts/validate_agents.py <agent-path>
python scripts/validate_organization.py
```

## Validación semántica

Comprueba:

- Misión única y clara.
- Personalidad profesional, no teatral.
- Responsabilidades y límites completos.
- Reglas permanentes separadas de procedimientos.
- Delegaciones consistentes con `REPORT_TO` y organigrama.
- Posición organizacional completa; solo Luffy responde al usuario.
- Entrada en `organization/organigrama.yaml`.
- Skills coherentes, moderadas y no duplicadas.
- Descripciones de activación específicas.
- Fuentes suficientes y actuales.
- Herramientas y permisos mínimos.
- Adaptadores invocables.

## Revisión adversarial

Pregunta:

1. ¿Qué haría mal este agente por ambigüedad?
2. ¿Qué skill se activaría cuando no debería?
3. ¿Qué responsabilidad no tiene dueño?
4. ¿Qué permisos son excesivos?
5. ¿Qué información podría estar obsoleta?
6. ¿Qué otro agente se solapa con este?

## Salida

Entrega errores, advertencias, evidencia revisada, correcciones y veredicto final.

## Veredicto

- Aprobado.
- Aprobado con observaciones.
- Requiere corrección.
- Rechazado.

No uses “aprobado con observaciones” para ocultar fallos estructurales o riesgos materiales.
