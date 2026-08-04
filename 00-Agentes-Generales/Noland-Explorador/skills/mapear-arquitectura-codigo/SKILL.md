---
name: mapear-arquitectura-codigo
description: Construye un mapa estructural de un codebase o sistema (entry points, módulos, capas, stack) a partir de evidencia. Úsala cuando haya que entender qué existe antes de diseñar, migrar o implementar.
metadata:
  author: yzylabs
  version: "1.0"
---

# Mapear arquitectura de código

## Propósito

Producir un mapa verificable de la forma del sistema: componentes, responsabilidades observadas y límites.

## Entradas

- Raíz(es) del repositorio o servicio.
- Preguntas de descubrimiento y profundidad acordadas.
- Stack conocido o pistas (lenguaje, framework).

## Procedimiento

1. Inventaria estructura de carpetas de primer y segundo nivel.
2. Localiza entry points (main, servers, workers, CLIs, front apps).
3. Identifica manifiestos (`package.json`, `*.csproj`, `go.mod`, `pom.xml`, Docker, IaC).
4. Agrupa módulos por responsabilidad observada (no por deseo de diseño).
5. Esboza capas o boundaries (UI, API, domain, data, infra) con evidencia.
6. Anota “god modules”, carpetas gigantes y código muerto sospechoso.
7. Dibuja un diagrama ligero (Mermaid) solo con nodos evidenciados.
8. Lista lo no revisado.

## Salida

```md
## Stack observado
## Entry points
## Mapa de módulos
## Capas / boundaries
## Diagrama (Mermaid opcional)
## Hotspots (god modules, deuda visible)
## No revisado
## Evidencia clave (rutas)
```

## Casos límite

- Monorepo enorme: mapea por workspace/paquete prioritario primero.
- Repo generado / mínimo: declara baja densidad de evidencia.
- Multi-lenguaje: separa superficies por runtime.

## Validación

- Cada nodo del mapa tiene al menos una ruta o manifiesto.
- No se inventan servicios fantasma.
- El diagrama no contradice el inventario.

## Criterios de terminado

- Un lector entiende qué hay y dónde mirar después.
- Entry points y stack están cubiertos para el perímetro acordado.
- Hotspots materiales están señalados.

## Casos de evaluación

| Caso | Entrada | Esperado |
|---|---|---|
| Normal | API Nest + workers | Entry points HTTP y jobs; módulos por dominio |
| Ambiguo | Carpeta `src/` sin README | Mapa por carpetas + entry points detectados; marcar desconocidos |
| Límite | 40 paquetes en monorepo | Mapa de workspaces + zoom solo en el perímetro pedido |

## Fuentes

- Prácticas de discovery estructural (entry points → módulos → capas) — síntesis 2025–2026.
- Preferencia por diagramas verificables (“si no se puede dibujar, sigue excavando”).
