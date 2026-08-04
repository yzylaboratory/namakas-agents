---
name: integrar-playground-try-it
description: Especifica la consola interactiva try-it-now del portal alineada a OpenAPI y sandbox. Úsala cuando se pida playground, “probar API”, console embebida o try-it en la referencia.
metadata:
  author: yzylabs
  version: "1.0"
---

# Integrar playground / try-it-now

## Propósito

Definir una experiencia interactiva en el portal que permita ejecutar llamadas de sandbox desde la referencia, con ejemplos prefijados y unhappy paths visibles.

## Entradas

- OpenAPI publicado y base URL de sandbox.
- Credenciales de prueba / mecanismo de inyección.
- Restricciones CORS/gateway.
- Catálogo de unhappy paths relevantes (Sabo/sandbox).
- Política de datos sintéticos.

## Procedimiento

1. Ubica try-it en la referencia por operación (no solo página aislada).
2. Prefija request examples; inyecta key de prueba del usuario autenticado cuando exista.
3. Muestra response real del sandbox (status, headers, body) y errores machine-readable.
4. Incluye cURL/HTTP export; no fuerces SDK para el primer try.
5. Etiqueta entorno (sandbox) y bloquea apuntar a producción por defecto.
6. Lista unhappy paths mínimos a demostrar (401, 403, 429, error de negocio).
7. Define límites de abuso (rate limit del playground) y escala seguridad si hace falta.

## Salida

```md
## Ubicación UX del playground
## Requisitos técnicos (CORS, auth inject)
## Happy + unhappy paths
## Export snippets
## Riesgos de abuso
## Gaps + owners
```

## Casos límite

- Sandbox no espeja prod → documenta divergencias visibles en UI.
- Sin CORS → proxy de portal documentado; no fingir try-it roto.
- Operaciones destructivas → confirmación + solo sandbox + scopes mínimos.

## Validación

- Try-it usa la misma operación/spec que la referencia.
- No hay PII ni tokens de prod en ejemplos.
- Producción no es el target por defecto.

## Criterios de terminado

- Spec de playground implementable.
- Unhappy paths listados con owner de datos/sandbox.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | OpenAPI + sandbox URL | Try-it por operación + inject key |
| Ambiguo | “Pon un Swagger UI” | Requisitos + anti-prod + unhappy paths |
| Límite | Endpoint de pago real | Bloqueo prod + confirmación + scopes |

## Fuentes

- APIScout Developer Portal 2026 — https://apiscout.dev/guides/building-developer-portal-api-2026 (2026-08-04).
- Mintlify playground / time-to-first-call — https://www.mintlify.com/library/api-developer-portals-for-enterprise (2026-08-04).
- Skene onboarding (HTTP before SDK) — https://www.skene.ai/resources/blog/developer-onboarding-guide (2026-08-04).
