---
name: evaluar-riesgo-cambio-legacy
description: Evalúa fragilidad, acoplamiento, blast radius y seams insertables antes de tocar un legado. Úsala cuando se proponga un cambio, migración o extracción y haya que cuantificar riesgo.
metadata:
  author: yzylabs
  version: "1.0"
---

# Evaluar riesgo de cambio legacy

## Propósito

Decidir si un cambio es seguro en etapas, qué seams faltan y qué contención se requiere antes de intervenir.

## Entradas

- Ficha de caracterización (o misión que la produzca primero).
- Cambio propuesto (feature, extracción, cutover, deprecación).
- Restricciones de downtime y blast radius aceptable.
- Cobertura de tests / jobs de caracterización conocidos.

## Procedimiento

1. Describe el cambio en una frase y el outcome de negocio.
2. Identifica módulos, datos e interfaces en la ruta del cambio.
3. Estima acoplamiento: dependientes upstream/downstream con evidencia.
4. Busca seams existentes (interfaces, proxies, feature flags, colas).
5. Evalúa tests de caracterización: ¿hay red de seguridad o es vuelo a ciegas?
6. Clasifica riesgo: bajo / medio / alto / crítico con justificación.
7. Recomienda contención: proxy, dual-run, feature flag, freeze de zona, más recon.
8. Si el riesgo es alto sin seams, bloquea big-bang y propone inserción de seams primero.

## Salida

```md
## Cambio propuesto
## Superficie afectada
## Acoplamiento / blast radius
## Seams existentes vs faltantes
## Cobertura de caracterización
## Clasificación de riesgo
## Contenciones recomendadas
## Bloqueos / no-hacer
## Evidencia
```

## Casos límite

- Sin tests: riesgo mínimo “alto”; exige caracterización o dual-run antes de cutover.
- Cambio solo de config: evalúa igual blast radius de misconfig.
- Datos compartidos multi-dominio: marca riesgo crítico de corrupción cruzada.

## Validación

- Clasificación de riesgo tiene premisas explícitas.
- No se aprueba extracción sin seam o contención cuando el riesgo es alto.
- Dependientes citados con evidencia o marcados desconocidos.

## Criterios de terminado

- Iceburg/Tom pueden decidir go/no-go con el informe.
- Seams faltantes listados como trabajo previo si aplica.
- “No-hacer” explícito (p. ej. big-bang).

## Casos de evaluación

| Caso | Entrada | Esperado |
|---|---|---|
| Normal | Extraer módulo de reportes con API clara | Riesgo medio + seam HTTP existente |
| Ambiguo | “Refactorizar el core” sin perímetro | Bloqueo; exige delimitar cambio |
| Límite | Tabla compartida por 12 apps | Riesgo crítico; ACL/CDC antes de cortar |

## Fuentes

- Azure Strangler Fig — consideraciones de dependencias cruzadas y rollback (consultado 2026-08-04).
- Fowler — necesidad de seams para partir el legado (consultado 2026-08-04).
