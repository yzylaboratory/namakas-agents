# Estructura de memoria — Brook Cronista

Convención por defecto bajo el agente canónico:

```text
00-Agentes-Generales/Brook-Cronista/memoria/
├── diario/
│   └── YYYY-MM-DD.md
├── decisiones/
│   └── YYYY-MM-DD-slug-corto.md
├── adr/
│   └── NNNN-titulo-kebab.md
└── permanente/
    └── slug-corto.md
```

## diario/

Una nota por día calendario. Si el archivo existe, se **añade una sección** (no se sobrescribe el día entero).

Secciones recomendadas:

- `## Misión / turno`
- `## Hechos`
- `## Decisiones`
- `## Archivos tocados`
- `## Abiertos`
- `## Enlaces`

## decisiones/

Veredictos puntuales del equipo que no requieren ADR completo (prioridad, alcance, naming, proceso).

## adr/

Decisiones arquitectónicamente significativas (estructura, NFR, dependencias, interfaces, técnicas de construcción). Ver `plantilla-adr-nygard.md`.

Numeración: siguiente entero disponible (`0001`, `0002`, …).

## permanente/

Notas atómicas reutilizables (aprendizajes, convenciones, mapas de contenido). Una idea principal por nota; enlazar a diarios/ADR relacionados.

## Principios

1. Captura primero en diario; promueve a decisión/ADR/permanente cuando aporte recuperación futura.
2. Preferir enlaces relativos Markdown a copiar el mismo texto en tres sitios.
3. Nunca guardar secretos en claro.
