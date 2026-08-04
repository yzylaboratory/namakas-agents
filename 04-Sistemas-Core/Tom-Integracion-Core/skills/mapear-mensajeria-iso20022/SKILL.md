---
name: mapear-mensajeria-iso20022
description: Mapea mensajes ISO 20022 (pacs/camt) y coexistencia MT/MX hacia el canónico/core con fuentes citadas. Úsala cuando el flujo involucre mensajería de pagos/reporting estándar o migración MT→MX.
metadata:
  author: yzylabs
  version: "1.0"
---

# Mapear mensajería ISO 20022

## Propósito

Producir mapeos verificables entre mensajes ISO 20022 (y MT si aplica) y el modelo canónico/core, citando catálogo y usage guidelines — sin inventar elementos.

## Entradas

- Tipo de mensaje / flujo (p. ej. credit transfer, status, statement).
- Jurisdicción o market practice (CBPR+, HVPS+, doméstico, propietario).
- Schemas o ejemplos existentes.
- Canónico interno (si existe).
- Restricciones de coexistencia MT/MX.

## Procedimiento

1. Identifica el mensaje base en el catálogo ISO 20022 (familia pacs/camt/…).
2. Determina usage guideline aplicable (CBPR+/HVPS+/otra); si falta, márcalo como decisión abierta.
3. Cita fuente oficial + fecha de consulta; no inventes tags.
4. Mapea campos críticos: deudor/acreedor, montos, agentes, remittance, status.
5. Si hay MT: documenta reglas de traducción conocidas y truncation.
6. Lista mensajes de status/exception relacionados (p. ej. pacs.002, camt.*) cuando material.
7. Señala deadlines de mercado solo con fuente (p. ej. releases SWIFT); si no hay certeza, no inventes.
8. Entrega matriz de mapeo + riesgos + gaps de guideline.

## Salida

```md
## Mensajes / familia
## Usage guideline / fuente
## Matriz de mapeo
## Coexistencia MT/MX
## Truncation / riesgos
## Gaps / decisiones
```

## Casos límite

- Solo hay “ISO 20022” genérico sin mensaje → exige tipo de mensaje antes de mapear.
- Traducción in-flow como contingencia → documenta deuda y plan de adopción plena (SWIFT FAQ).
- Conflicto entre guidelines → escala a Iceburg; no elijas en silencio.

## Validación

- Cada elemento mapeado tiene fuente o etiqueta “propietario/core”.
- No hay versiones inventadas.
- Truncation MT/MX explícita si aplica.

## Criterios de terminado

- Un ingeniero puede implementar el codec con la matriz.
- Gaps de MyStandards/acceso a guidelines están listados.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Credit transfer cross-border → core | Mapeo pacs.008 (+ status) con citas |
| Ambiguo | “Pasemos todo a ISO 20022” | Inventario de mensajes candidatos + plan por flujo |
| Límite | Solo MT103 sin MX target claro | Truncation + DECISION_REQUIRED de target message |

## Fuentes

- ISO 20022 — https://www.iso20022.org/ (2026-08-04).
- ISO 20022 Catalogue of messages — https://www.iso20022.org/catalogue-messages (2026-08-04).
- SWIFT ISO 20022 Standards — https://www.swift.com/standards/iso-20022/iso-20022-standards (2026-08-04).
- SWIFT Implementation FAQ — https://www.swift.com/standards/iso-20022/iso-20022-faqs/implementation (2026-08-04).
- SWIFT Standards Releases — https://www.swift.com/standards/standards-releases (2026-08-04).
