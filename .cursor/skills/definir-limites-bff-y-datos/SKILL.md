---
name: definir-limites-bff-y-datos
description: Define límites BFF/servidor/cliente para datos y secretos en apps web. Úsala cuando se decida dónde vive el fetching, agregación o sesión frente a APIs backend.
metadata:
  author: yzylabs
  version: "1.0"
---

# Definir límites BFF y datos

## Propósito

Clarificar qué datos y orquestación ocurren en BFF/servidor frente al cliente, protegiendo secretos y evitando acoplar la UI a contratos internos de MS.

## Entradas

- Flujos de pantalla y datos requeridos.
- APIs existentes / tratados Robin / specs OpenAPI.
- Modelo de auth (cookies, tokens, OIDC).
- Restricciones de CORS, gateway y PII.

## Procedimiento

1. Inventaría datos por vista: fuente, sensibilidad, frescura.
2. Clasifica cada dato: server-only, BFF-aggregatable, client-safe.
3. Decide BFF cuando haya agregación multi-MS, ocultación de contratos internos o sesión server-side.
4. Prohíbe secretos y tokens de larga vida en el bundle; documenta cookies HttpOnly si aplica.
5. Define contratos de UI (shape estable) vs contratos MS (Robin/Backend).
6. Señala waterfalls evitables (fetch en servidor paralelo vs client waterfall).
7. Lista gaps de Backend/seguridad con dueño.

## Salida

```md
## Inventario de datos por vista
## Frontera server / BFF / client
## Secretos y sesión
## Contratos UI vs MS
## Riesgos / dueños
```

## Casos límite

- Solo hay API pública ya productizada (Sabo) → consumo documentado; no inventes BFF sin necesidad.
- PII en listados → server/BFF + minimización; no caches en localStorage.
- Realtime (WS) → isla client delimitada; shell sigue en servidor si aplica.

## Validación

- Ningún secreto en client bundle según diseño.
- Cada vista crítica tiene frontera explícita.
- Acoplamiento a MS internos está mediado o justificado.

## Criterios de terminado

- Implementación sabe dónde fetchear sin filtrar tokens.
- Handoffs a Robin/Backend/Fujitora están listados si faltan contratos.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Dashboard con 3 MS | BFF agrega; client recibe DTO UI |
| Ambiguo | “Llama al API desde React” | Preguntas de secretos + frontera propuesta |
| Límite | Refresh token en localStorage | Rechazo; diseño cookie/BFF |

## Fuentes

- Next.js Data Fetching / caching patterns — https://nextjs.org/docs/app/building-your-application/data-fetching (2026-08-04).
- OWASP — XSS / sensitive data in client — https://owasp.org/www-community/attacks/xss/ (referencia seguridad client, 2026-08-04).
- React Server Components — https://react.dev/reference/rsc/server-components (2026-08-04).
