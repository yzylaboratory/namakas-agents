---
name: consumir-mapeo-bian
description: Consume y propaga un mapeo BIAN recibido (HANDOFF_BIAN / equivalente) hacia el tratado y los contratos, sin inventar Service Domains. Úsala antes de documentar un MS/orch bancario nuevo o cuando debas alinear semántica BIAN.
metadata:
  author: yzylabs
  version: "1.0"
---

# Consumir mapeo BIAN

## Propósito

Integrar el mapeo de Service Domains y operaciones BIAN producido por el especialista en los artefactos de Robin, manteniendo trazabilidad y bloqueando invención.

## Entradas

- `HANDOFF_BIAN`, `HANDOFF_HOSTOS` (legado de naming) u equivalente Nakamas.
- Versión BIAN citada por el especialista (p. ej. V14 / release 14.x).
- Objetivo del MS/orch a documentar.
- Tratado o contratos en borrador (opcional).

## Procedimiento

1. Localiza el handoff BIAN en las entradas de la tarea.
2. Si no existe y el MS/orch es bancario/nuevo → **no inventes**; produce bloqueo con datos faltantes y escala (Lucci vía Luffy).
3. Extrae: Service Domains, service operations, control records / behavior qualifiers si vienen, y versión BIAN.
4. Verifica que el handoff cite fuente (portal BIAN, guía, repo oficial). Si no cita, marca riesgo de procedencia.
5. Mapa de trazabilidad: capacidad del MS → Service Domain(s) → operación/evento.
6. Propaga nombres y semántica al tratado (`sección BIAN`) y, si aplica, a extensiones o descripciones OpenAPI/AsyncAPI.
7. Registra explícitamente qué parte del MS **no** está cubierta por el mapeo.
8. Prohíbe rellenar huecos con Service Domains “parecidos”.

## Salida

```md
## Consumo BIAN

- Versión BIAN: [...]
- Fuente del handoff: [...]
- Service Domains consumidos: [...]
- Operaciones / eventos trazados: [...]
- Cobertura del MS: [completa | parcial]
- Huecos (sin inventar): [...]
- Acción: [continuar documentación | BLOQUEO]
```

## Casos límite

- Handoff parcialmente aplicable → documenta subset y bloquea el resto.
- Conflicto entre dos handoffs → no elijas; escala a Luffy/Lucci.
- Pedido de “elegir el Service Domain obvio” → rechaza; pide especialista BIAN.

## Validación

- Ningún Service Domain aparece sin origen en el handoff.
- Versión BIAN registrada.
- Huecos listados o cobertura completa justificada.

## Criterios de terminado

- Trazabilidad BIAN escrita en el tratado/contratos, o bloqueo formal emitido.
- Cero invención de dominio.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | HANDOFF_BIAN completo V14 | Trazabilidad en tratado + continuar |
| Ambiguo | MS bancario sin handoff | BLOQUEO con checklist de faltantes |
| Límite | Handoff con 1 SD pero MS con 3 capacidades | Cobertura parcial + huecos; sin inventar 2 SD |

## Fuentes

- https://bian.org/ (2026-08-04).
- BIAN Semantic API Practitioner’s Guide v8.1 (2024-12).
- https://github.com/bian-official/public (2026-08-04).

## Referencia interna

Ver `references/contrato-handoff-bian.md`.
