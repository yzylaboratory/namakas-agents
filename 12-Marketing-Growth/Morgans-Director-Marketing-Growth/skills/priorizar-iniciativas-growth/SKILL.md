---
name: priorizar-iniciativas-growth
description: Prioriza el backlog de iniciativas de Marketing/Growth con impacto en inputs del North Star, costo, riesgo de marca y dependencias. Úsala cuando haya que ordenar campañas, experimentos, canales o replanificar el departamento ante presupuesto o capacidad limitada.
metadata:
  author: yzylabs
  version: "1.0"
---

# Priorizar iniciativas de growth

## Propósito

Producir un backlog priorizado y defendible para el departamento Marketing y Growth, evitando priorización por el stakeholder más ruidoso o por vanity.

## Entradas

- Lista de iniciativas candidatas (canales, campañas, experimentos, programas de comunidad).
- North Star / inputs (si existen) o outcome provisional.
- Presupuesto, plazos y capacidad del squad.
- Dependencias (producto, UX, ventas, legal, datos).

## Procedimiento

1. Normaliza cada iniciativa: problema, segmento, capa AARRR, resultado esperado, métrica primaria.
2. Puntúa en cuatro ejes (1–5): **impacto en input/NSM**, **confianza en evidencia**, **habilitación de plataforma de growth** (instrumentación/loop), **riesgo residual si se retrasa**.
3. Resta o penaliza por: vanity-only, falta de baseline, riesgo de marca/compliance, dependencia bloqueante de producto.
4. Aplica gates: sin definición de métrica o sin activación mínima del producto, no puede ser P0 de paid scale.
5. Ordena P0/P1/P2 y Now/Next/Later; limita WIP departamental (pocas P0 simultáneas).
6. Documenta trade-offs rechazados (qué no se hará y por qué).

## Salida

```md
## Backlog priorizado Growth
| ID | Iniciativa | P | Impacto NSM | Confianza | Habilita | Riesgo delay | Dependencias | Dueño |
## WIP y secuencia
## Trade-offs / no hacemos ahora
## Preguntas abiertas
```

## Casos límite

- Dos P0 “de marca” vs “de activación”: desempata por outcome de negocio y evidencia; escala a Luffy si es político.
- Iniciativa viral sin loop medible: baja a discovery/experimento, no a escala.
- Solicitud de más MQLs sin calidad: exige definición de MQL calificado o rechaza como P0.

## Validación

- Toda P0 tiene dueño, métrica primaria y gate.
- No hay más P0 de las que el squad puede absorber.
- Penalizaciones por vanity/compliance aplicadas.

## Criterios de terminado

- Backlog ordenado con justificación reproducible.
- Trade-offs explícitos.
- Listo para delegar a Carrot/Shakky/Bartolomeo o escalar a Luffy.

## Fuentes

- Amplitude North Star → inputs como eje de priorización — https://amplitude.com/blog/product-north-star-metric (2026-08-04)
- ICE/RICE para scoring de experimentos (síntesis product/growth) — 2026-08-04
