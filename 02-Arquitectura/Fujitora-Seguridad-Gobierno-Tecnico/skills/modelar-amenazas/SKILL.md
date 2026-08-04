---
name: modelar-amenazas
description: Construye un modelo de amenazas priorizado (actores, activos, entradas, STRIDE/OWASP) para un alcance dado. Úsala cuando haya que identificar y priorizar amenazas antes de elegir controles o emitir handoff de seguridad.
metadata:
  author: yzylabs
  version: "1.0"
---

# Modelar amenazas

## Propósito

Producir un modelo de amenazas accionable y priorizado, sin ritual vacío ni inventario infinito fuera de alcance.

## Entradas

- Alcance y objetivo del sistema/cambio.
- Diagrama de flujo de datos o equivalente.
- Activos y datos sensibles conocidos.
- Supuestos de amenaza (interno, externo, insider, supply chain) si existen.

## Procedimiento

1. Define alcance y “fuera de modelo”.
2. Lista activos (datos, identidades, claves, servicios, pipelines).
3. Identifica actores y puntos de entrada.
4. Traza flujos de datos entre trust boundaries.
5. Aplica STRIDE (o categorías OWASP Threat Modeling) por elemento relevante del diagrama.
6. Prioriza: impacto × explotabilidad en contexto (no CVSS inventado sin base).
7. Descarta amenazas fuera de alcance con justificación explícita.
8. Entrega IDs estables (`T-01`…) consumibles por `definir-controles-tecnicos`.

## Salida

Tabla de amenazas priorizadas + diagramas/listas de trust boundaries + supuestos + fuera de modelo.

## Casos límite

- Sin diagrama → produce DFD mínimo propuesto y marca borrador.
- Pedido de “todas las amenazas posibles” → limita al alcance; documenta exclusión.
- Amenaza depende de bug de implementación no visible → marca como hipótesis, no hecho.

## Validación

- Cada amenaza tiene activo y severidad relativa.
- Hay al menos un supuesto de amenaza explícito.
- IDs únicos y estables.

## Criterios de terminado

- Modelo priorizado usable para mapear controles.
- Fuera de modelo listado.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | DFD de API + DB | Amenazas STRIDE priorizadas con IDs |
| Ambiguo | Alcance “toda la plataforma” | Exige acotar; borrador o BLOCKED |
| Límite | Solo amenaza reputacional de negocio | Escala a Law/Luffy; no fuerces STRIDE vacío |

## Fuentes

- OWASP Threat Modeling Project — https://owasp.org/www-project-threat-modeling/ — consultado 2026-08-04
- NIST CSF 2.0 Identify/Govern outcomes — https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final — consultado 2026-08-04
