---
name: definir-marco-cumplimiento
description: Define el alcance y marco del sistema de cumplimiento (CMS): obligaciones, roles, controles y evidencia alineados a buenas prácticas tipo ISO 37301. Úsala cuando se pida política de compliance, alcance departamental, RACI legal o diseño inicial del CMS.
metadata:
  author: yzylabs
  version: "1.0"
---

# Definir marco de cumplimiento

## Propósito

Convertir el mandato del departamento en un marco operable: qué está en alcance, quién responde, qué controles y qué evidencia se exige — sin fingir certificación ISO.

## Entradas

- Productos, jurisdicciones y actores en juego.
- Apetito de riesgo de negocio (si existe).
- Inventario inicial de obligaciones o gaps conocidos.
- Estado del squad (Corazon / Tsuru / Cobra: vivo o stub).

## Procedimiento

1. Delimita alcance del CMS: entidades, productos, jurisdicciones, exclusiones.
2. Identifica categorías de obligaciones (regulatorias, contractuales, internas, estándares voluntarios).
3. Define roles: Accountable (Sengoku), Responsible por dominio (células), Consulted/Informed (Jinbe, Robin, Law, Fujitora, Luffy).
4. Establece ciclo mínimo: identificar obligaciones → evaluar riesgos → controles → monitoreo → mejora.
5. Define artefactos mínimos: registro de obligaciones, matriz de riesgos, log de gates, memos.
6. Señala gaps (células stub, falta de counsel, falta de inventario) como bloqueos explícitos.
7. Entrega marco con métricas iniciales (p. ej. % obligaciones con dueño, gates cerrados a tiempo).

## Salida

```md
## Alcance del CMS
## Categorías de obligaciones
## RACI
## Ciclo de cumplimiento (pasos)
## Artefactos mínimos
## Gaps / bloqueos
## Métricas iniciales
## Fuera de alcance
```

## Casos límite

- Pedido de “certificarnos ISO 37301”: entregar gap analysis y plan; no afirmar certificación.
- Solo una jurisdicción conocida: acotar alcance; marcar expansión como Next.
- Células stub: el marco puede existir; la ejecución profunda queda `BLOCKED` hasta forja.

## Validación

- Hay alcance y exclusiones explícitos.
- Cada categoría de obligación tiene dueño potencial.
- No se afirma certificación ni cumplimiento absoluto.

## Criterios de terminado

- Marco usable por Luffy y por el squad.
- Gaps listados con impacto.
- Fuentes del enfoque CMS citadas.

## Fuentes

- ISO 37301:2021 Compliance management systems (consultado 2026-08-04) — https://www.iso.org/standard/75080.html
- ISO/TC 309 FAQs ISO 37301 (May 2022) — consultado 2026-08-04
