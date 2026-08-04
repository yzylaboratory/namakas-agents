---
name: seleccionar-enfoque-multiplataforma
description: Decide nativo (Swift/Kotlin), React Native o Flutter con matriz de criterios. Úsala cuando haya que elegir o justificar el stack móvil antes de implementar.
metadata:
  author: yzylabs
  version: "1.0"
---

# Seleccionar enfoque multiplataforma

## Propósito

Elegir el enfoque de cliente móvil con evidencia de producto, equipo, plataforma y seguridad — no por moda ni dogma “una sola codebase”.

## Entradas

- Plataformas objetivo (iOS, Android, ambas).
- Sensibilidad de datos (retail, banca, interno).
- Capacidades de equipo y plazos.
- Requisitos de APIs nativas / hardware (biometría, NFC, background).
- Restricciones de compliance o rendimiento.

## Procedimiento

1. Lista requisitos no negociables (seguridad, offline, hardware, store).
2. Evalúa nativo SwiftUI/UIKit + Compose/Kotlin frente a RN y Flutter.
3. Puntúa: time-to-market, acceso nativo, tamaño del equipo, riesgo del bridge, hiring, tooling CI.
4. Documenta dónde vivirían secretos y crypto en cada opción.
5. Propón recomendación primaria + alternativa con condiciones de cambio.
6. Escala a Sanji si falta decisión de negocio o a Fujitora si el riesgo de seguridad es el eje.

## Salida

```md
## Contexto
## Criterios y pesos
## Matriz (nativo / RN / Flutter)
## Recomendación
## Condiciones de revisión
## Riesgos / pendientes
```

## Casos límite

- Solo iOS o solo Android → favorece nativo salvo reutilización forzada documentada.
- App bancaria con attestation/pinning estricto → no elijas multiplataforma sin plan nativo de controles.
- Equipo web-only sin nativos → documenta deuda de bridge y dueño de módulos nativos.

## Validación

- Criterios explícitos y trazables.
- Secretos/crypto considerados por opción.
- No se inventan capacidades de framework.

## Criterios de terminado

- Sanji (o el padre) puede aprobar/rechazar el stack sin ambigüedad.
- Alternativa y triggers de cambio están escritos.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | App retail iOS+Android, equipo RN | Matriz + RN con módulos nativos listados |
| Ambiguo | “Hazlo multiplataforma” | Preguntas de plataformas/seguridad + 2 opciones |
| Límite | Banca con NFC + attestation | Nativo o híbrido con controles nativos obligatorios |

## Fuentes

- React Native Architecture overview — https://reactnative.dev/docs/architecture-overview (2026-08-04).
- OWASP MASVS Using the MASVS (cross-platform) — https://mas.owasp.org/MASVS/03-Using_the_MASVS/ (2026-08-04).
- Apple Interface fundamentals — https://developer.apple.com/documentation/technologyoverviews/interface-fundamentals (2026-08-04).
- Android Material 3 in Compose — https://developer.android.com/develop/ui/compose/designsystems/material3 (2026-08-04).
