# Protocolo de reportes — Nakamas Agents

Fuente de verdad jerárquica: `organization/organigrama.yaml`.  
Contratos: `organization/contratos/task-contract.md` y `report-contract.md`.

## Cadena

```text
Randy
  └── luffy-coordinador
        ├── agentes-generales
        └── directores
              └── células
                    └── especialistas (opcional)
```

Todo resultado **sube** por la misma cadena. Solo Luffy entrega el consolidado final a Randy.

Visibilidad en Cursor: el árbol de Tasks debe reflejar esa cadena (p. ej. Luffy → Franky → Paulie), **nunca** Luffy → `shell` genérico. El título UI (`description`) preferido con cadena es `{Especialista} ← {Director}: {acción}`.

## Flujo por misión

1. Luffy crea `MISSION_ID` y el plan de misión.
2. Luffy emite `TASK_*` a directores / agentes generales (`REPORT_TO: luffy-coordinador`; título UI con personaje).
3. Directores emiten `TASK_*` a células (`REPORT_TO: <director>`; título preferido `{Célula} ← {Director}: …`).
4. Células ejecutan (o `DELEGATION_REQUIRED` / `BLOCKED` si stub).
5. Células reportan al director con `REPORT_*` + evidencia (`REPORT_TO` = padre).
6. Director consolida un único reporte departamental a Luffy.
7. Brook registra bitácora bajo `reports/<MISSION_ID>/` sin alterar resultados técnicos.
8. Luffy valida, corrige, consolida y responde a Randy.

## Matriz DevOps (git / remoto)

- git push / remoto / `gh` → Franky → Paulie (Paulie ejecuta; reporta a Franky).
- **FORBIDDEN** usar Task `shell` u otros genéricos Cursor como trabajadores de esa misión.

## Bitácora Brook (`reports/`)

```text
reports/
└── <MISSION_ID>/
    ├── mission.md
    ├── delegation-log.md
    ├── decision-log.md
    ├── status.md
    ├── final-report.md
    └── agents/
        └── <AGENT_ID>/
            └── <TASK_ID>.md
```

Plantilla: `reports/_template/`.

## DELEGATION_REQUIRED

Si un agente no puede lanzar otro subagente:

```text
DELEGATION_REQUIRED:
- agente solicitado:
- objetivo:
- contexto:
- entregable:
- criterios de aceptación:
```

El padre realiza la delegación y devuelve el resultado al hijo para validación.

## Prohibiciones

- Célula no se salta a su director.
- Director no responde a Randy / usuario.
- Padre no declara done sin reportes hijos validados.
- Nadie responde “completado” sin evidencia.
- Luffy no cierra mientras haya delegaciones pendientes, bloqueadas o sin validar.
- No ocultar la cadena: `REPORT_TO` obligatorio; título UI debe nombrar al especialista (y preferiblemente al director).
- No usar Task types Cursor genéricos (`shell`, etc.) como sustituto de células Nakamas.
