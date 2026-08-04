---
name: aplicar-controles-masvs-movil
description: Mapea controles OWASP MASVS al diseño del cliente (storage, network, crypto, auth, code, resilience). Úsala antes de declarar una app lista para producción o auditoría.
metadata:
  author: yzylabs
  version: "1.0"
---

# Aplicar controles MASVS móvil

## Propósito

Traducir OWASP MASVS a un mapa accionable para el stack elegido, con gaps y dueños — sin fingir compliance.

## Entradas

- Stack (nativo / RN / Flutter).
- Clasificación de datos y amenazas.
- Controles ya implementados (si existen).
- Nivel de verificación objetivo (orientativo vs auditado).

## Procedimiento

1. Selecciona categorías MASVS materiales al producto (STORAGE, NETWORK, CRYPTO, AUTH, CODE, RESILIENCE, PRIVACY según versión vigente).
2. Por control: estado (presente / parcial / ausente), dónde vive (nativo vs JS), evidencia.
3. En multiplataforma: exige Keychain/Keystore, pinning y crypto anclados en nativo.
4. Prohíbe secretos y lógica de confianza solo en el bundle interpretado.
5. Lista pruebas MASTG-equivalentes o handoff a Fujitora/QA.
6. Produce backlog priorizado de gaps con severidad.

## Salida

```md
## Alcance MASVS
## Mapa control → implementación
## Gaps y severidad
## Plan de remediación
## Dueños (Reiju / Fujitora / QA)
## Evidencia / pruebas
```

## Casos límite

- Solo “obfuscation” como resiliencia → insuficiente; documenta límites.
- RN sin módulos nativos de storage → bloqueo para datos sensibles.
- App interna de bajo riesgo → reduce alcance pero no inventes “N/A” sin justificación.

## Validación

- Cada control material tiene estado y dueño.
- No se inventan IDs de control; se cita categoría/fuente MASVS.
- Secretos en bundle = gap crítico explícito.

## Criterios de terminado

- Fujitora/QA puede verificar sin reinterpretar el diseño.
- No se declara “MASVS compliant” sin evidencia de verificación.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | App retail RN | Mapa STORAGE/NETWORK + gaps de pinning |
| Ambiguo | “Hazla segura” | Inventario de datos + mapa MASVS mínimo |
| Límite | Token JWT en AsyncStorage plaintext | Gap crítico + remedio Keychain |

## Fuentes

- OWASP Mobile Application Security — https://owasp.org/www-project-mobile-app-security/ (2026-08-04).
- OWASP MASVS — Using the MASVS — https://mas.owasp.org/MASVS/03-Using_the_MASVS/ (2026-08-04).
- OWASP — Securing React Native Mobile Apps with OWASP MAS — https://owasp.org/blog/2024/10/02/Securing-React-Native-Mobile-Apps-with-OWASP-MAS.html (2024-10-02).
