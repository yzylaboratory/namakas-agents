# nakamas-agents

Definiciones de agentes (personalidad, rol, reglas, skills) para la tripulación nakamas.

## Disponibilidad actual

**Solo Luffy-Coordinador está operativo en Cursor.**

- Docs + skills: [`00-Agentes-Generales/Luffy-Coordinador/`](00-Agentes-Generales/Luffy-Coordinador/)
- Custom Agent: [`.cursor/agents/luffy-coordinador.md`](.cursor/agents/luffy-coordinador.md)
- Regla de proyecto: [`.cursor/rules/nakamas-luffy-only.mdc`](.cursor/rules/nakamas-luffy-only.mdc)
- Skill: [`.cursor/skills/luffy-coordinador/SKILL.md`](.cursor/skills/luffy-coordinador/SKILL.md)

Los demás asientos (directores, células, agentes generales) están documentados o esbozados en carpetas `00`–`12`, pero **aún no tienen demos / Custom Agents**. Hasta entonces:

1. Todo el trabajo en este repo lo hace **Luffy en el mismo chat**.
2. **No** se enruta a agentes viejos de Tripulación (`brd-todologo`, `brd-second-brain`, `brd-luperon`, …).
3. **No** se inventa delegación Task a asientos nakamas sin demo.

Ver también la nota en [`Delegacion.md`](00-Agentes-Generales/Luffy-Coordinador/Delegacion.md).

## Fuera de este repo

Workspaces Banreservas / Tripulación siguen usando las reglas globales `mandatory-delegation` y `yzy-dispatch` (Task → especialistas / Usopp / Olvia).
