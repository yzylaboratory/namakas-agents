---
name: planificar-release-tiendas
description: Prepara checklist y plan de release para App Store y Google Play (versionado, firmas, privacy, tracks, go/no-go). Úsala cuando se acerque beta o producción móvil.
metadata:
  author: yzylabs
  version: "1.0"
---

# Planificar release a tiendas

## Propósito

Convertir una build móvil en un paquete listo para revisión de tiendas y rollout controlado, con criterios go/no-go explícitos.

## Entradas

- Plataformas y números de versión/build.
- Cambios desde el último release.
- Privacy/permissions nuevos.
- Estado de CI, firmas y tracks (internal/beta/prod).
- Dependencias de backend/feature flags.

## Procedimiento

1. Fija esquema de versionado (semver marketing + build number monotónico).
2. Verifica firmas (iOS certificates/profiles, Android App Signing / upload key).
3. Inventaría permisos, privacy nutrition labels / Data safety y justifications.
4. Prepara store listing: capturas, texto, review notes, account de prueba.
5. Define tracks: internal → closed → open → prod; % rollout si aplica.
6. Lista smoke checks post-install (deep links, auth, pagos si hay).
7. Escribe go/no-go: crash-free, blockers abiertos, dependencia de API.
8. Coordina changelog cliente ↔ breaking changes de backend.

## Salida

```md
## Versión / build
## Firmas y CI
## Privacy / permisos
## Store listing
## Tracks y rollout
## Smoke checks
## Go / No-go
## Riesgos / dueños
```

## Casos límite

- Permission nuevo sin copy de justificación → no-go.
- Backend breaking sin app mínima compatible → bloqueo coordinado.
- Solo una plataforma lista → release parcial documentado, no “completo”.

## Validación

- Checklist actionable por release owner.
- Privacy/permisos alineados al código.
- Criterios go/no-go medibles.

## Criterios de terminado

- Un release manager puede subir sin improvisar datos de privacy.
- Gaps de cuenta de review / feature flags tienen dueño.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | 1.2.0 con biometría nueva | Checklist + Data safety/privacy updates |
| Ambiguo | “Súbelo a prod” | Preguntas de versión/tracks + go/no-go draft |
| Límite | Crash rate alto en beta | No-go + condiciones de remediación |

## Fuentes

- Apple App Store Review Guidelines (oficial) — https://developer.apple.com/app-store/review/guidelines/ (2026-08-04).
- Google Play policy center (oficial) — https://play.google.com/about/developer-content-policy/ (2026-08-04).
- Apple / Google consolas de distribución (App Store Connect / Play Console) docs vigentes (2026-08-04).
