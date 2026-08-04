---
name: trazar-dependencias-integraciones
description: Traza dependencias de paquetes, servicios, datos, colas y APIs, incluyendo fronteras async. Úsala cuando el riesgo esté en acoplamientos, integraciones legacy o flujos entre sistemas.
metadata:
  author: yzylabs
  version: "1.0"
---

# Trazar dependencias e integraciones

## Propósito

Hacer visible con qué habla el sistema, qué posee y dónde puede romperse el acoplamiento.

## Entradas

- Mapa estructural preliminar o perímetro a analizar.
- Manifiestos de dependencias y configs de integración.
- Preguntas sobre legacy, core, colas o APIs.

## Procedimiento

1. Extrae dependencias declaradas (lockfiles, manifests) relevantes al perímetro.
2. Busca clientes HTTP, SDKs, connection strings (sin volcar secretos), topics y colas.
3. Identifica stores de estado: DB, cache, archivos, secret managers.
4. Marca fronteras async: workers, webhooks, schedulers, outbox/inbox.
5. Lista integraciones inbound/outbound con dirección observada.
6. Señala dependencias circulares o capas invertidas si hay evidencia.
7. Prioriza las 3–5 integraciones más críticas para la decisión.
8. Documenta qué no se pudo verificar en runtime.

## Salida

```md
## Dependencias de paquetes (relevantes)
## Integraciones inbound / outbound
## Stores de estado
## Fronteras async
## Acoplamientos riesgosos
## Evidencia
## No verificado en runtime
```

## Casos límite

- Secretos en config: reporta ubicación/tipo, no el valor.
- Solo binarios / vendor: marca opacidad y riesgo.
- Event-driven denso: prioriza topics del flujo pedido.

## Validación

- Direcciones de integración coherentes con el código citado.
- No se inventan APIs “obvias”.
- Secretos no aparecen en claro en el informe.

## Criterios de terminado

- Las integraciones críticas del perímetro están listadas.
- Async boundaries visibles.
- Riesgos de acoplamiento priorizados.

## Casos de evaluación

| Caso | Entrada | Esperado |
|---|---|---|
| Normal | BFF que llama 3 MS | Lista outbound + auth observada |
| Ambiguo | “¿De qué depende?” sin perímetro | Exige módulo/servicio concreto |
| Límite | Legacy con DB compartida | Marca store compartido como acoplamiento crítico |

## Fuentes

- Prácticas de mapeo post-adquisición / dependency discovery (límites, stores, runtime) — síntesis 2025–2026.
- Reglas de seguridad de Noland (no exfiltración de secretos).
