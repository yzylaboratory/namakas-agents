---
name: mapear-obligaciones-regulatorias
description: Construye o actualiza un registro de obligaciones regulatorias por jurisdicción, producto y actor, con fuente y estado. Úsala cuando se pida mapa de compliance, inventory de normas aplicables a OB/fintech/privacidad o revisión de alcance normativo.
metadata:
  author: yzylabs
  version: "1.0"
---

# Mapear obligaciones regulatorias

## Propósito

Hacer visible qué obliga a quién, bajo qué instrumento y con qué certeza — base para priorización y gates.

## Entradas

- Jurisdicción(es) y producto(s).
- Rol del actor (ASPSP, TPP, controlador, encargado, parte contractual).
- Fuentes candidatas o hallazgos previos (Jinbe alto nivel, discovery, counsel).
- Referencia interna `references/mapa-obligaciones-base.md` si existe.

## Procedimiento

1. Fija alcance: jurisdicción × producto × actor.
2. Lista instrumentos candidatos (ley, reglamento, resolución, estándar de esquema, contrato).
3. Para cada obligación potencial: enunciado, artículo/sección si se conoce, fuente URL/doc, vigencia/fecha.
4. Clasifica: mandatoria / contractual / voluntaria (estándar de industria).
5. Marca estado: confirmada / provisional / en transición / no aplica (con razón).
6. Asigna dueño de seguimiento (Corazon / Tsuru / Cobra / Sengoku).
7. Separa “requisito de producto” (Jinbe) de “obligación legal” (este registro).
8. Documenta incertidumbre y preguntas abiertas; no inventes texto legal.

## Salida

```md
## Alcance del mapa
## Registro
| ID | Obligación | Jurisdicción | Actor | Tipo | Fuente | Estado | Dueño | Notas |
## No aplica (con razón)
## Incertidumbres / en transición
## Preguntas para counsel / célula
```

## Casos límite

- Norma en litigio (p. ej. regímenes de datos financieros en disputa): estado “en transición”; no asumas vigencia.
- Multi-jurisdicción: una fila por jurisdicción; no mezcles GDPR con LGPD/OF BR en la misma celda.
- Solo hay alineación de alto nivel de Jinbe: conviértela en candidatos y marca “requiere Tsuru/Corazon”.

## Validación

- Cada fila confirmada tiene fuente.
- Tipo (mandatoria/contractual/voluntaria) asignado.
- Ninguna afirmación “obligatorio” sin evidencia.

## Criterios de terminado

- Registro usable para priorizar y para gates.
- Incertidumbres explícitas.

## Fuentes

- Open Finance Brasil — actos normativos BCB — https://openfinancebrasil.org.br/atos-normativos/ (2026-08-04)
- Berlin Group openFinance / NextGenPSD2 — https://www.berlin-group.org/open-finance (2026-08-04)
- GDPR (UE) 2016/679 — EUR-Lex (2026-08-04)
- CFPB Personal Financial Data Rights / §1033 — https://www.consumerfinance.gov/personal-financial-data-rights/ (2026-08-04)
- ISO 37301:2021 — identificación de compliance obligations (2026-08-04)
