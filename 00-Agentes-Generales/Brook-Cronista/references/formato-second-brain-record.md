# Formato SECOND_BRAIN_RECORD

Bloque que los trabajadores y el coordinador pueden devolver al final de un turno para que Brook lo consolide. No requiere Olvia ni `brd-second-brain`.

```md
## SECOND_BRAIN_RECORD

- **Quién pidió:** [usuario / Luffy / misión]
- **Qué se hizo:** [resumen factual 2–6 líneas]
- **Agentes / roles:** [lista]
- **Archivos tocados:** [rutas]
- **Decisiones:** [veredictos o "ninguna"]
- **Aprendizajes:** [opcionales]
- **Abiertos:** [bloqueos o siguientes pasos]
- **No registrar:** [ruido explícitamente excluido]
```

## Reglas de consolidación

1. Un bloque → normalmente una sección en `memoria/diario/YYYY-MM-DD.md`.
2. Si hay decisión material → también `memoria/decisiones/` o ADR.
3. Redactar secretos como `[REDACTED]`.
4. Si el bloque está incompleto, completar solo con hechos presentes en el mismo mensaje; marcar faltantes en Abiertos.
