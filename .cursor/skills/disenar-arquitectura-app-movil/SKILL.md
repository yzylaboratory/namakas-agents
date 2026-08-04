---
name: disenar-arquitectura-app-movil
description: Diseña la arquitectura del cliente móvil (capas, módulos, estado, DI, límites nativos). Úsala cuando se pida blueprint, ADR o estructura de app iOS/Android.
metadata:
  author: yzylabs
  version: "1.0"
---

# Diseñar arquitectura de app móvil

## Propósito

Definir una arquitectura de cliente mantenible: UI, estado, dominio, datos y frontera nativa — alineada al stack elegido y a UDF.

## Entradas

- Stack aprobado (nativo / RN / Flutter).
- Mapa de features y sensibilidad de datos.
- Dependencias de API y design system.
- Requisitos de testabilidad y modularización.

## Procedimiento

1. Declara capas y reglas de dependencia (UI → estado → dominio → datos).
2. Define módulos por feature o bounded context de cliente.
3. Elige patrón de estado (ViewModel/@Observable, UDF Compose, Redux-like RN, etc.) con justificación.
4. Especifica DI e inyección de servicios (no singletons globales opacos).
5. Marca frontera nativa: Keychain, biometría, pinning, sensors.
6. Define estrategia de testing (unit ViewModels, UI smoke, contrato API).
7. Produce ADR corto + diagrama textual de módulos.

## Salida

```md
## Contexto / stack
## Capas y reglas
## Módulos
## Estado y DI
## Frontera nativa
## Testing
## ADR
## Riesgos
```

## Casos límite

- Legacy monolito móvil → plan de strangler por módulos, no big-bang.
- Lógica de negocio duplicada en backend → no copies reglas; consume API.
- Multiplataforma → lista módulos que deben ser nativos desde el día 1.

## Validación

- Dependencias entre capas no ciclan.
- Secretos no viven en capa UI/JS.
- ADR tiene decisión y consecuencias.

## Criterios de terminado

- Un desarrollador puede crear el primer feature module sin reinventar capas.
- Gaps de API/UX/seguridad tienen dueño.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | App Compose + banking lite | Capas UDF + Keystore + módulos feature |
| Ambiguo | “Arquitectura limpia” | Preguntas de stack + ADR con 2 opciones |
| Límite | RN con crypto en JS | Rechazo + rediseño con módulo nativo |

## Fuentes

- Apple Interface fundamentals / SwiftUI — https://developer.apple.com/documentation/technologyoverviews/interface-fundamentals (2026-08-04).
- Android Compose Material 3 / UDF practices — https://developer.android.com/develop/ui/compose/designsystems/material3 (2026-08-04).
- OWASP blog RN + MAS — https://owasp.org/blog/2024/10/02/Securing-React-Native-Mobile-Apps-with-OWASP-MAS.html (2024-10-02).
