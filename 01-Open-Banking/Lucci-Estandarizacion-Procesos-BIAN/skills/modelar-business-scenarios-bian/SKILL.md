---
name: modelar-business-scenarios-bian
description: Modela o adapta Business Scenarios y wireframes BIAN como ilustraciones de interacción entre Service Domains. Úsala cuando debas mostrar el flujo entre dominios sin tratar el escenario como estándar prescritivo.
metadata:
  author: yzylabs
  version: "1.0"
---

# Modelar Business Scenarios BIAN

## Propósito

Usar escenarios y wireframes BIAN (o adaptaciones locales) para explicar interacciones entre Service Domains ya mapeados, sin alterar su rol canónico.

## Entradas

- Service Domains ya validados (salida de `mapear-service-domains`).
- Requisito de negocio o proceso end-to-end.
- Referencia a escenario/wireframe BIAN si existe.
- Versión BIAN de trabajo.

## Procedimiento

1. Confirma que los Service Domains participantes tienen evidencia (si no, vuelve a mapear).
2. Localiza escenario/wireframe BIAN de partida cuando exista (release notes / portal).
3. Declara disclaimer: **ilustrativo, no prescritivo**.
4. Secuencia intercambios entre SDs (quién inicia, qué operación/evento, qué CR se toca a alto nivel).
5. Adapta el flujo a la organización **sin** cambiar el propósito canónico de ningún SD.
6. Marca pasos locales no cubiertos por BIAN como extensión org. o hueco.
7. No uses el escenario para “crear” Service Domains nuevos.

## Salida

```md
## Business Scenario (adaptado)
- Versión BIAN:
- Origen (BIAN ref / local):
- Disclaimer: ilustrativo, no prescritivo

### Pasos
| # | Service Domain | Interacción / operación | Notas |
|---|---|---|---|

### Extensiones locales / huecos
- ...
```

## Casos límite

- Escenario BIAN incluye SD fuera de alcance → omite o marca fuera de alcance; no expandas misión.
- Conflicto escenario vs rol canónico del SD → prevalece el catálogo del SD; ajusta el escenario.
- Sin escenario oficial → construye ilustración local solo con SDs ya evidenciados.

## Validación

- Todos los SD del escenario están en el mapeo evidenciado.
- Disclaimer presente.
- Ningún SD inventado vía escenario.

## Criterios de terminado

- Flujo comprensible para Robin/Law/negocio.
- Separación claro estándar vs ilustración.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Escenario hipoteca BIAN + SDs mapeados | Pasos adaptados + disclaimer |
| Ambiguo | Pedido “el escenario define el dominio” | Rechazo; catálogo manda |
| Límite | Wireframe con SD fuera de alcance | Omitido/marcado; sin ampliar alcance |

## Fuentes

- BIAN Semantic API Practitioner’s Guide v8.1 (Business Scenarios / wireframes no prescritivos) — https://bian.org/wp-content/uploads/2024/12/BIAN-Semantic-API-Pactitioner-Guide-V8.1-FINAL.pdf — 2024-12; consultado 2026-08-04.
- BIAN v14.0 Release Notes § Business Scenarios / Wireframes — 2026-02.
- https://bian.org/deliverables/service-landscape/
