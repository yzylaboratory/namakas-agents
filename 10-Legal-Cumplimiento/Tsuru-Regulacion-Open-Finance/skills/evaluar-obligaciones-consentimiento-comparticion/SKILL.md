---
name: evaluar-obligaciones-consentimiento-comparticion
description: Evalúa obligaciones regulatorias de consentimiento y compartición de datos en Open Finance, separando requisitos OF de privacidad profunda. Úsala cuando el alcance incluya consent, authorization, data sharing o screen scraping vs APIs.
metadata:
  author: yzylabs
  version: "1.0"
---

# Evaluar obligaciones de consentimiento y compartición

## Propósito

Documentar qué exige el marco OF sobre consentimiento/autorización y compartición de datos, y qué debe escalarse a Corazon (privacidad) sin mezclar dominios.

## Entradas

- Marco mapeado (jurisdicción + rol).
- Journeys de consentimiento / revocación / reautorización.
- Políticas de privacidad o DPIA existentes (si hay).
- Fecha de análisis.

## Procedimiento

1. Extrae requisitos OF de consentimiento (granularidad, duración, revocación, purpose limitation del marco).
2. Identifica reglas de compartición con TPPs / ADRs / agregadores y límites de uso.
3. Separa: **obligación OF** vs **privacidad general** (LGPD/GDPR/etc.) → esta última escala a Corazon.
4. Nota postura del marco sobre screen scraping vs API obligatoria, si aplica.
5. Lista controles esperados (logs de consentimiento, dashboards, re-consent) como impacto, no como diseño UX final.
6. Marca lo que requiere counsel (bases legales ambiguas, menores, datos sensibles).

## Salida

```md
## Consentimiento / compartición OF
| Requisito | Tipo (OF/privacidad) | Impacto | Escala a | Fuente |
## Flujos afectados
## Escalado a Corazon
## Pendiente counsel
```

## Casos límite

- Solo hay política de cookies → insuficiente; no inferir cumplimiento OF.
- Conflicto OF vs privacidad → documentar tensión; escalar Sengoku + Corazon.
- Multi-país → no unificar consent models.

## Validación

- Cada requisito OF tiene fuente.
- Hay al menos una fila de escalamiento a Corazon cuando haya PII/DPIA.
- No se diseña UI final (eso es producto/UX).

## Criterios de terminado

- Separación OF vs privacidad clara.
- Escalaciones listadas.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | PSD2 AIS consent | Requisitos OF + nota SCA/RTS |
| Ambiguo | “consentimiento genérico” | Exigir jurisdicción y journey |
| Límite | Pedido de redactar DPIA | DELEGATION_REQUIRED → Corazon |

## Fuentes

- Berlin Group / PSD2 access — https://www.berlin-group.org/psd2-access-to-bank-accounts — 2026-08-04
- Open Banking Tracker — https://www.openbankingtracker.com/open-banking-regulations — 2026-08-04
- CFPB PFDR — https://www.consumerfinance.gov/personal-financial-data-rights/ — 2026-08-04
