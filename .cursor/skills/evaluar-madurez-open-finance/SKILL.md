---
name: evaluar-madurez-open-finance
description: Evalúa madurez y readiness Open Banking→Open Finance (consentimiento, seguridad, datos, operación API, organización) y propone gates. Úsala antes de escalar el catálogo de APIs, entrar a nuevos productos de datos o afirmar que la institución está lista para Open Finance.
metadata:
  author: yzylabs
  version: "1.0"
---

# Evaluar madurez Open Finance

## Propósito

Diagnosticar si la ambición Open Finance es realista dado el estado de capacidades, y definir gates antes de externalizar más datos o journeys.

## Entradas

- Ambición declarada (compliance only vs plataforma vs marketplace).
- Evidencia operativa: consentimientos, incidentes, SLAs, calidad de datos, onboarding TPP.
- Organigrama / RACI actual del programa API.
- Hallazgos de discovery si existen.

## Procedimiento

1. Puntúa madurez (1–5) en dimensiones:
   - **Consentimiento y conduct** (revocación, granularidad, auditoría).
   - **Identidad y seguridad** (OAuth/FAPI, SCA, gestión de secretos/certs).
   - **Datos** (ownership, definiciones, lineage, calidad).
   - **Plataforma API** (gateway, versionado, observabilidad, resiliencia).
   - **Producto y go-to-market** (portal, partner success, monetización).
   - **Organización** (mandato ejecutivo, CoE/C4E, KPIs, presupuesto).
2. Identifica el cuello de botella más bajo (la dimensión más débil limita el resto).
3. Define gates go/no-go para la siguiente ola de productos.
4. Propón un plan de cierre de gaps en 30/60/90 días alineado al squad.
5. Señala riesgos de “exportar problemas internos” vía APIs.

## Salida

```md
## Ambición vs readiness
## Scorecard
| Dimensión | Score 1-5 | Evidencia | Gap crítico |
## Cuello de botella
## Gates go/no-go
## Plan 30/60/90
## Riesgos si se escala ahora
```

## Casos límite

- Scores altos en API gateway pero bajos en datos: no aprobar Open Finance de nuevos dominios.
- Cumplimiento mandatorio urgente con madurez baja: plan de mínimo viable controlado + deuda explícita.
- Falta de evidencia: marca dimensión como “desconocida”, no como madura.

## Validación

- Cada score tiene evidencia o está marcado desconocido.
- Gates son binarios y verificables.
- El plan tiene dueños (Jinbe/Lucci/FIBO/Sabo/otros).

## Criterios de terminado

- Scorecard completo.
- Recomendación clara: escalar / pausar / solo compliance mínimo.
- Gates acordables con Luffy y el squad.

## Fuentes

- EBA OBWG — Gearing the bank operating model towards digital and open banking readiness (consultado 2026-08-04)
- Secuenciación OB para readiness Open Finance — síntesis contrastada 2026-08-04
- C4E / API mindset en banca — síntesis Tyk/EBA 2026-08-04
