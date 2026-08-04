---
name: gobernar-gates-legales
description: Define y aplica gates de revisión legal (privacidad, Open Finance, contratos) con decisión go / no-go / go-with-conditions. Úsala antes de publicar APIs, firmar alianzas, activar consentimientos o declarar readiness de cumplimiento.
metadata:
  author: yzylabs
  version: "1.0"
---

# Gobernar gates legales

## Propósito

Impedir que producto o alianzas avancen sin revisión proporcional al riesgo, sin convertir cada cambio en un comité infinito.

## Entradas

- Cambio propuesto (API, journey, partner, cláusula, dataset).
- Mapa de obligaciones y riesgos priorizados (si existen).
- Evidencia disponible (DPIA draft, specs, términos, FAPI/consentimiento).
- Plazo de negocio.

## Procedimiento

1. Clasifica el trigger: nuevo procesamiento de datos, nuevo participante OF, breaking change público, nueva alianza, cambio de base legal, exportación, etc.
2. Selecciona gates aplicables:
   - Privacidad → Corazon
   - Regulación OF → Tsuru
   - Contratos → Cobra
3. Define evidencia mínima por gate (lista corta verificable).
4. Evalúa: go / no-go / go-with-conditions.
5. Condiciones: dueño, fecha, criterio de cierre, residual risk.
6. Si evidencia falta y célula es stub: no-go o go-with-conditions solo si el riesgo es bajo y Luffy/negocio acepta residual — documentado.
7. Registra decisión en log de gates (quién, cuándo, alcance).
8. Comunica al solicitante (Jinbe/Robin/Sabo/Luffy) el siguiente paso concreto.

## Salida

```md
## Cambio evaluado
## Gates aplicables
## Evidencia revisada
## Decisión: go | no-go | go-with-conditions
## Condiciones (si aplica)
## Residual risk y aceptante
## Próximo dueño
```

## Casos límite

- “Es solo un campo más en el API”: reevaluar minimización y base legal; no asumir under-gate.
- Presión de plazo sin evidencia: no-go o condiciones duras; no firmes compliant.
- Excepción recurrente: escala a marco CMS / apetito de riesgo (Luffy).

## Validación

- Decisión explícita con alcance y fecha.
- Condiciones verificables (no “revisar luego” vacío).
- Gates no aplicables justificados.

## Criterios de terminado

- Decisión comunicable al solicitante.
- Log listo para auditoría interna / Brook.

## Fuentes

- Accountability y medidas apropiadas — GDPR Arts. 24–25; EDPB Guidelines 4/2019 (DPbDD) — 2026-08-04
- CMS performance evaluation / controls — ISO 37301:2021 — 2026-08-04
- Práctica de API governance + legal review en OB — contrastada con gates de Jinbe (alto nivel) vs legal profundo — 2026-08-04
