---
name: fibo-proponer-extension-controlada
description: Propone extensiones semánticas locales o puentes a otros estándares cuando FIBO no cubre un concepto (p. ej. consentimiento Open Banking), sin presentarlas como FIBO core. Úsala solo tras confirmar ausencia de cobertura.
metadata:
  author: yzylabs
  version: "1.0"
---

# Proponer extensión controlada

## Propósito

Cubrir huecos semánticos de Open Banking/Open Finance de forma gobernada, compatible con adopción FIBO incremental.

## Entradas

- Concepto local sin cobertura (evidencia de navegación/alineación).
- Justificación de negocio/regulación.
- Estándares puente candidatos (opcional; p. ej. literatura OBO/PSD2).
- Namespace o convención de naming del repo.

## Procedimiento

1. Confirma “sin cobertura” con evidencia (búsqueda en dominios relevantes).
2. Busca si OMG Commons u otros módulos FIBO recientes ya cubren el caso (release notes).
3. Elige estrategia:
   - Extensión local (namespace propio)
   - Puente a estándar externo documentado
   - Diferir (si el concepto no es material)
4. Define: nombre, definición, relaciones a clases FIBO existentes, constraints.
5. Marca explícitamente: **no es FIBO core**.
6. Lista riesgos de drift y dueño de mantenimiento.
7. No publiqués IRI bajo namespaces `https://spec.edmcouncil.org/fibo/...` inventados.

## Salida

```md
## Extensión controlada

- Concepto: [...]
- Evidencia de hueco FIBO: [...]
- Estrategia: [local | puente | diferir]
- Namespace: [...]
- Definición: [...]
- Relaciones a FIBO: [...]
- Estándar puente: [...]
- Riesgos / gobierno: [...]
```

## Casos límite

- El hueco es realmente un mal nombrado de una clase FIBO existente → vuelve a alineación.
- Regulación exige término legal específico → documenta término legal + mapping; no lo “FIBO-izas”.
- Pedido de fork masivo de FIBO → rechaza; escala a Luffy/Law.

## Validación

- Evidencia de no cobertura presente.
- Namespace no colisiona con FIBO oficial.
- Relación con clases FIBO existentes declarada o “ninguna” justificada.

## Criterios de terminado

- Extensión lista para incluir en HANDOFF_FIBO.
- Etiquetada como no-core.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Consentimiento AIS sin clase FIBO | Extensión local + relaciones a Party/Agreement si aplican |
| Ambiguo | Hueco dudoso | Re-navegación antes de extender |
| Límite | “Crea FIBO branch interna completa” | Rechazo / recorte a subset |

## Fuentes

- https://spec.edmcouncil.org/fibo/release-notes (2026-08-04)
- https://www.omg.org/spec/EDMC-FIBO/FND (extensibility / model conformance notions, 2026-08-04)
- https://doi.org/10.3390/app13031447 (OBO como evidencia secundaria de huecos PSD2, 2026-08-04)
- https://github.com/edmcouncil/fibo (MIT license note, 2026-08-04)
