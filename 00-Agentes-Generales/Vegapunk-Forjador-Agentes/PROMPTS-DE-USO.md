# Prompts de uso

## Crear un agente individual

```text
Usa el subagente vegapunk-forjador-agentes para crear [PERSONAJE-ROL].

Responsabilidad: [DESCRIPCIÓN DEL ROL].
Departamento: [DEPARTAMENTO].

Investiga en internet las prácticas, estándares, herramientas y responsabilidades
actuales del dominio. Prioriza fuentes oficiales y primarias. Diseña skills
específicas, moderadamente acotadas y activables por intención. Genera:
Personalidad.md, Rol.md, Reglas.md, Delegacion.md y skills/*/SKILL.md.

También crea el adaptador en .cursor/agents/ y .claude/agents/. Ejecuta la
validación y corrige cualquier error antes de presentar el resultado.
```

## Crear todos los agentes pendientes

```text
Usa el subagente vegapunk-forjador-agentes para procesar
catalogo/agentes-one-piece.yaml.

Crea todos los agentes con status: pending en el orden del catálogo. Para cada uno:
1. Investiga el dominio y las mejores skills actuales.
2. Verifica las fuentes y registra las referencias dentro de Rol.md y cada SKILL.md.
3. Genera la estructura estándar.
4. Genera adaptadores para Cursor y Claude Code.
5. Ejecuta scripts/validate_agents.py.
6. Corrige errores.
7. Cambia el status a completed solo después de aprobar la validación.

No sobrescribas agentes completed salvo que se solicite una actualización.
```

## Actualizar un agente existente

```text
Usa el subagente vegapunk-forjador-agentes para auditar y actualizar
[AGENTE]. Compara sus skills con documentación oficial actual, elimina
solapamientos, mejora descripciones de activación y ejecuta las evaluaciones.
Conserva cambios útiles y registra qué cambió y por qué.
```
