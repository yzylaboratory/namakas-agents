---
name: aplicar-privacy-by-design
description: Aplica privacy by design/by default a productos, APIs, consentimientos y telemetría. Úsala al diseñar o revisar features Open Banking, sandboxes, logs o formularios que traten datos personales.
metadata:
  author: yzylabs
  version: "1.0"
---

# Aplicar privacy by design

## Propósito

Traducir principios de protección de datos (minimización, finalidad, default restrictivo, transparencia) en requisitos verificables para producto e ingeniería — sin implementar el código ni el portal.

## Entradas

- Descripción de feature/API/flujo.
- Datos recolectados, derivados o inferidos.
- Base legal / consentimiento previsto.
- Audiencia (cliente, TPP, empleado, partner).
- Artefactos existentes (OpenAPI, tratados, políticas).

## Procedimiento

1. Declara finalidad(es) y datos mínimos necesarios por paso del flujo.
2. Marca datos que sobran; propone no recolectar o tokenizar/seudonimizar.
3. Define defaults restrictivos (opt-in, scopes mínimos, retención corta).
4. Revisa transparencia: avisos, lenguajes de consentimiento, capas de información.
5. Exige datos sintéticos/enmascarados en sandbox, docs y demos (handoff Sabo/Koala).
6. Señala telemetría/analytics con PII; exige propósito y retención.
7. Lista requisitos de privacidad numerados para Robin/Sabo/Backend/Fujitora.
8. Define criterios de aceptación de privacidad (testables) antes de “GA”.

## Salida

```md
## Finalidades y minimización
## Defaults restrictivos
## Transparencia / consentimiento
## Requisitos por equipo
## Prohibiciones (PII en demo/logs)
## Criterios de aceptación de privacidad
## Riesgos / DPIA trigger
## Fuentes
```

## Casos límite

- Feature “recomendaciones” sin base legal clara → bloqueo hasta base/DPIA.
- Partner pide dump de producción para “integración” → rechazo; sandbox sintético.
- OpenAPI documenta campos PII sin sensibilidad marcada → requisito de clasificación.

## Validación

- Cada requisito tiene dueño y es verificable.
- No hay PII real en ejemplos públicos.
- Finalidad y minimización explícitas.
- Triggers de DPIA señalados si aplica.

## Criterios de terminado

- Producto/ingeniería puede implementar sin reinterpretar la ley.
- Gaps legales/contratos escalados a Sengoku/Cobra.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Consent AIS Open Banking | Requisitos minimización + scopes + aviso |
| Ambiguo | “Añadir tracking en el portal” | Preguntas de finalidad + defaults off |
| Límite | Demo partner con datos reales | Rechazo + plan datos sintéticos |

## Fuentes

- GDPR Art. 25 (data protection by design and by default) — https://eur-lex.europa.eu/eli/reg/2016/679/oj (consultado 2026-08-04).
- ISO/IEC 27701:2025 — PIMS guidance — https://www.iso.org/standard/27701 (2025-10).
- Ley 172-13 — principios de calidad, finalidad, seguridad, consentimiento (PDF oficial, 2013-12-13).
