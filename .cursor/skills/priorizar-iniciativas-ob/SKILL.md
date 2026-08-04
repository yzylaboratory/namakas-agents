---
name: priorizar-iniciativas-ob
description: Prioriza el backlog de iniciativas Open Banking / Open Finance con valor, urgencia regulatoria, dependencias y riesgo. Úsala cuando haya que ordenar iniciativas OB, recortar alcance o replanificar el departamento ante nuevos plazos o capacidad limitada.
metadata:
  author: yzylabs
  version: "1.0"
---

# Priorizar iniciativas Open Banking

## Propósito

Producir un backlog priorizado y defendible para el departamento Open Banking, evitando priorización por moda o por el stakeholder más ruidoso.

## Entradas

- Lista de iniciativas candidatas (epics/productos API).
- Plazos regulatorios conocidos y capacidad del squad.
- Dependencias (BIAN, FIBO, gateway, core, portal, legal).
- Evidencia de valor (demanda partner, revenue, reducción de riesgo).

## Procedimiento

1. Normaliza cada iniciativa: problema, usuario (TPP/PSU/interno), resultado, jurisdicción.
2. Puntúa en cuatro ejes (1–5): **valor de negocio**, **urgencia regulatoria**, **habilitación de plataforma**, **riesgo residual si se retrasa**.
3. Resta o penaliza por: deuda de consentimiento/seguridad/datos, dependencia bloqueante, alto costo de cambio breaking.
4. Aplica gates: si falta consentimiento o seguridad mínima, la iniciativa no puede ser P0 de exposición externa.
5. Ordena P0/P1/P2 y Now/Next/Later; limita WIP departamental (pocas P0 simultáneas).
6. Documenta trade-offs rechazados (qué no se hará y por qué).

## Salida

```md
## Backlog priorizado OB
| ID | Iniciativa | P | Valor | Reg | Plataforma | Riesgo delay | Dependencias | Dueño |
## WIP y secuencia
## Trade-offs / no hacemos ahora
## Preguntas abiertas
```

## Casos límite

- Dos P0 “regulatorios”: desempata por fecha legal real y severidad; escala a Legal si la fecha es incierta.
- Iniciativa de alto valor con datos sin owner: baja prioridad de exposición hasta gate de datos.
- Solicitud política sin evidencia: pide métrica o la clasifica como discovery, no como P0.

## Validación

- Toda P0 tiene dueño, dependencia crítica y gate.
- No hay más P0 de las que el squad puede absorber.
- Penalizaciones por madurez están aplicadas.

## Criterios de terminado

- Backlog ordenado con justificación reproducible.
- Trade-offs explícitos.
- Listo para delegar a Lucci/FIBO/Sabo o escalar a Luffy.

## Fuentes

- Prácticas API-as-a-product / priorización de roadmaps OB (EBA OBWG; síntesis product leadership) — 2026-08-04
- Secuenciación de capacidades OB (consent → security → data → products) — síntesis contrastada 2026-08-04
