---
name: generar-agente-estandar
description: Genera los archivos canónicos Personalidad.md, Rol.md, Reglas.md, Delegacion.md y las carpetas skills/*/SKILL.md a partir de una arquitectura aprobada. Úsala para materializar un agente individual.
metadata:
  author: yzylabs
  version: "1.0"
---

# Generar agente estándar

## Procedimiento

1. Consulta `organization/organigrama.yaml` y define supervisor, tipo, departamento y `direct_reports`.
2. Crea primero una carpeta temporal.
3. Usa las plantillas de `templates/` (incluyen Posición organizacional y `REPORT_TO`).
4. Sustituye todos los marcadores; no dejes placeholders invisibles.
5. Escribe los cuatro archivos canónicos con jerarquía completa.
6. Crea una carpeta por skill.
7. Asegura que `name` coincida con la carpeta.
8. Incluye fuentes consultadas en Rol.md y, cuando corresponda, en cada skill.
9. Genera adapters con bloque de cadena de mando y contratos.
10. Ejecuta `python scripts/validate_agents.py` y `python scripts/validate_organization.py`.
11. Actualiza `organization/organigrama.yaml` solo tras aprobar.
12. Mueve al destino solo cuando ambos validadores aprueben.

## Estructura obligatoria

```text
Personaje-Rol/
├── Personalidad.md
├── Rol.md
├── Reglas.md
├── Delegacion.md
└── skills/
    └── nombre-skill/
        └── SKILL.md
```

## Salida

- Carpeta canónica completa.
- Skills con frontmatter válido.
- Fuentes registradas.
- Resultado del validador.

## Validación

- Ejecutar `python 00-Agentes-Generales/Vegapunk-Forjador-Agentes/scripts/validate_agents.py <path>`.
- Ejecutar `python scripts/validate_organization.py`.
- Confirmar supervisor, `REPORT_TO`, nivel jerárquico y `puede_responder_usuario` correctos.
- Confirmar que no quedan placeholders.
- Verificar que el destino no pierde contenido útil.

## Prohibiciones

- No generar skills vacías.
- No dejar texto genérico como “seguir mejores prácticas”.
- No afirmar que se investigó sin registrar fuentes.
- No sobrescribir sin comparación previa.
- No finalizar sin entrada en `organization/organigrama.yaml`.
- No otorgar `puede_responder_usuario: true` a nadie excepto Luffy.
