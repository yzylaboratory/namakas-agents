# Setup Nakamas Agents en otra Mac

Guía reproducible para instalar el runtime Cursor desde este repo (`namakas-agents` = SoT versionada).

## 1. Clonar o actualizar el repo

```bash
# Primera vez
git clone git@github.com:yzylaboratory/namakas-agents.git
cd namakas-agents

# Mac que ya lo tiene
cd /ruta/a/namakas-agents
git pull origin main
```

## 2. Instalar subagentes en `~/.cursor/agents/`

```bash
cd /ruta/a/namakas-agents
chmod +x scripts/install-nakamas.sh
./scripts/install-nakamas.sh          # copia
# ./scripts/install-nakamas.sh --symlink   # opcional
```

El script instala todos los `.md` de `runtime-agents/` en `~/.cursor/agents/` y `ODA/oda.mdc` en `~/.cursor/rules/oda.mdc`.

**No** crees `~/.cursor/agents/oda.md`. Oda no es subagente.

```bash
ls ~/.cursor/agents/*.md | wc -l   # 22
rg -n '^model:' ~/.cursor/agents/*.md | sort
```

## 3. Sync rule Oda

| Superficie | Dónde |
|------------|--------|
| Rule alwaysApply | `~/.cursor/rules/oda.mdc` (script) |
| User Rule | Settings → Rules → **«Oda — runtime raíz Nakamas»** = `ODA/INSTRUCTIONS.md` |
| SoT | `ODA/INSTRUCTIONS.md` |

Chat raíz: selecciona **Grok 4.5 High** (`cursor-grok-4.5-high`) para Oda.

## 4. Tabla definitiva de modelos

| Agente | UI | slug |
|--------|-----|------|
| Oda | Grok 4.5 High | `cursor-grok-4.5-high` (chat) |
| Law | Grok 4.5 High | `cursor-grok-4.5-high` |
| Noland | Composer 2.5 Base | `composer-2.5[]` |
| Robin | Composer 2.5 Base | `composer-2.5[]` |
| Edison | Grok 4.5 High | `cursor-grok-4.5-high` |
| Doflamingo | Composer 2.5 Base | `composer-2.5[]` |
| Beckman | Composer 2.5 Base | `composer-2.5[]` |
| Clover | Composer 2.5 Base | `composer-2.5[]` |
| Luffy | Composer 2.5 Base | `composer-2.5[]` |
| Franky | GPT-5.6 Sol High | `gpt-5.6-sol-high` |
| Usopp | Composer 2.5 Base | `composer-2.5[]` |
| Sanji | GPT-5.3 Codex High | `gpt-5.3-codex-high` |
| Nami | Composer 2.5 Base | `composer-2.5[]` |
| Jinbe | Composer 2.5 Base | `composer-2.5[]` |
| Zoro | GPT-5.6 Sol High | `gpt-5.6-sol-high` |
| Brook | Composer 2.5 Base | `composer-2.5[]` |
| Lucci | Claude Sonnet 5 High | `claude-sonnet-5-thinking-high` |
| Tashigi | Composer 2.5 Base | `composer-2.5[]` |
| Chopper | Claude Opus 5 High | `claude-opus-5-thinking-high` |
| Stussy | Claude Opus 5 High | `claude-opus-5-thinking-high` |
| Fujitora | Composer 2.5 Base | `composer-2.5[]` |
| Sengoku | Composer 2.5 Base | `composer-2.5[]` |
| Kaku | Composer 2.5 Base | `composer-2.5[]` |

`composer-2.5[]` = base (no Fast). Tras una prueba, confirma en el dashboard de Task que Composer no corrió como Fast.

## 5. Capitanes, especialistas y Engineering Loop

```
Usuario → Oda → Capitán → Tripulación
Law → READY_FOR_IMPLEMENTATION → Luffy → READY_FOR_VERIFICATION → Lucci → VERIFIED → DONE
```

Detalle: `ODA/INSTRUCTIONS.md` (routing 0–4 + L0–L4 + loop).

## Checklist

- [ ] `git pull`
- [ ] `./scripts/install-nakamas.sh`
- [ ] User Rule Oda = `ODA/INSTRUCTIONS.md`
- [ ] Chat Oda en Grok 4.5 High
- [ ] 22 agentes; modelos = tabla de arriba
- [ ] Prueba Task: Composer base (no Fast)
