# Vegapunk — Forjador de Agentes

Paquete para Cursor y Claude Code que investiga, diseña, genera y valida agentes especializados inspirados en personajes de One Piece.

## Qué crea

Por cada agente objetivo genera exactamente esta estructura canónica:

```text
Personaje-Rol/
├── Personalidad.md
├── Rol.md
├── Reglas.md
├── Delegacion.md
└── skills/
    ├── skill-uno/
    │   └── SKILL.md
    └── skill-dos/
        └── SKILL.md
```

Además crea adaptadores invocables en:

```text
.cursor/agents/<slug>.md
.claude/agents/<slug>.md
```

## Instalación

Extrae el contenido de este ZIP en la raíz del repositorio.

La estructura `.cursor/` queda lista para Cursor. La estructura `.claude/` queda lista para Claude Code.

## Uso rápido en Cursor

```text
Usa el subagente vegapunk-forjador-agentes para crear el agente Brook-Cronista.
Investiga en internet las mejores prácticas y skills para registro de agentes,
bitácoras de decisiones y Second Brain. Genera la estructura estándar completa,
crea el adaptador de Cursor y valida el resultado antes de terminar.
```

## Uso por lote

```text
Usa el subagente vegapunk-forjador-agentes y la skill crear-agentes-en-lote.
Lee catalogo/agentes-one-piece.yaml, procesa únicamente los agentes con
status: pending y crea cada agente completo. Investiga cada dominio en fuentes
oficiales, evita skills duplicadas, ejecuta scripts/validate_agents.py y actualiza
el status del catálogo solo cuando el agente pase la validación.
```

## Nota sobre Vegapunk

Vegapunk Stella queda reservado como Forjador de Agentes. Para la célula FIBO se propone Vegapunk Pythagoras, evitando dos agentes con la misma identidad.
