# Estructura de `reports/` — bitácora por misión

Brook mantiene esta estructura en la raíz del repo. **No altera** resultados técnicos de especialistas; solo registra.

## Convención

```text
reports/
└── <MISSION_ID>/
    ├── mission.md           # Objetivo, alcance, criterios de cierre
    ├── delegation-log.md    # TASK_* emitidas y a quién
    ├── decision-log.md      # Decisiones materiales / enlaces ADR
    ├── status.md            # Estado agregado de la misión
    ├── final-report.md      # Copia del consolidado de Luffy (registro)
    └── agents/
        └── <AGENT_ID>/
            └── <TASK_ID>.md # Reporte REPORT_* del agente
```

Plantilla vacía: `reports/_template/`.

## Qué registra Brook

- Delegaciones (`TASK_*`).
- Estados (`STATUS` enum).
- Decisiones y bloqueos.
- Validaciones recibidas.
- Reporte final de Luffy a Randy.

## Qué no hace Brook

- Reescribir entregables técnicos.
- Responder al usuario en lugar de Luffy.
- Inventar evidencia.
