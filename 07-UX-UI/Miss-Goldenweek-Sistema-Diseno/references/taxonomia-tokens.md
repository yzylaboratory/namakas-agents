# Taxonomía de tokens (referencia rápida)

Fuente primaria: Design Tokens Format Module **2025.10** (DTCG, Final Community Group Report 2025-10-28).  
https://www.designtokens.org/tr/2025.10/

## Capas recomendadas

| Capa | Pregunta que responde | Ejemplo |
|---|---|---|
| Primitivo / reference | ¿Qué valor raw existe? | `color.blue.600` |
| Semántico / system | ¿Para qué rol de UI? | `color.text.primary` → `{color.blue.600}` |
| Componente | ¿Override de un componente? | `button.primary.bg` → `{color.action.primary}` |

## Reglas operativas

1. Los componentes del sistema consumen semánticos (o tokens de componente que aliasan semánticos).
2. Los temas reasignan semánticos; no duplican el árbol.
3. Preferir tipos DTCG (`$type`) y referencias `{path.to.token}`.
4. Contrastar pares semánticos por modo contra WCAG 2.2 AA como mínimo.

## Contraste (recordatorio)

- Texto normal AA: ≥ 4.5:1 (WCAG 2.2 SC 1.4.3).
- Texto grande AA: ≥ 3:1.
- UI no-texto AA: ≥ 3:1 (SC 1.4.11).

## Fronteras de rol

- Tokens/temas/API DS → Miss Goldenweek.
- Pantallas/flujos → Perona.
- Research → Chopper.
- Código de librería → Frontend (vía Nami/Luffy).
