---
name: especificar-navegacion-deep-links
description: Especifica grafo de navegación tipado, deep links/App Links/Universal Links y restauración de estado. Úsala cuando se diseñen flujos, rutas o linking móvil.
metadata:
  author: yzylabs
  version: "1.0"
---

# Especificar navegación y deep links

## Propósito

Definir navegación verificable y entry points externos seguros, adaptados a escenas y tamaños de ventana — no pantallas sueltas.

## Entradas

- Flujos de usuario / journeys.
- Plataformas y stack.
- Esquema de URLs / dominios asociados.
- Requisitos de auth (rutas públicas vs protegidas).
- Restricciones de adaptabilidad (iPad, foldable, multitasking).

## Procedimiento

1. Inventaría pantallas y transiciones; dibuja grafo (tabs, stacks, modales).
2. Tipifica rutas (enums/typed routes); evita strings mágicos.
3. Define deep links: esquema, path, parámetros, validación y fallback.
4. Declara rutas que requieren sesión y comportamiento si el token expiró.
5. Especifica restauración de estado / cold start desde link.
6. Audita supuestos de orientación e “idioma de UI”; usa size classes / window size.
7. Lista pruebas: link válido, inválido, auth-gated, app terminada vs background.

## Salida

```md
## Grafo de navegación
## Rutas tipadas
## Deep links / App Links / Universal Links
## Auth gates
## Adaptabilidad
## Casos de prueba
## Riesgos
```

## Casos límite

- Link a recurso borrado → pantalla de error con salida clara.
- Multi-ventana / iPhone Mirroring → no fijar layout a orientación.
- Parámetros sensibles en query → prohibir tokens en URL; usar one-time codes.

## Validación

- Cada deep link tiene dueño de dominio/asociación.
- Rutas auth-gated definidas.
- Pruebas de cold start incluidas.

## Criterios de terminado

- QA puede probar linking sin leer el código fuente.
- Gaps de associated domains / assetlinks tienen dueño.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Onboarding + home + detalle | Grafo + universal links documentados |
| Ambiguo | “Pon deep links” | Preguntas de dominio/auth + borrador de esquema |
| Límite | Token en query string | Rechazo + flujo seguro alternativo |

## Fuentes

- Apple WWDC26 Modernize your UIKit app (scenes/size classes) — https://developer.apple.com/videos/play/wwdc2026/278/ (2026-08-04).
- Apple Interface fundamentals — https://developer.apple.com/documentation/technologyoverviews/interface-fundamentals (2026-08-04).
- Android App Links / navigation (docs oficiales Android Developers) — https://developer.android.com/ (2026-08-04).
