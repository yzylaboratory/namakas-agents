---
name: fibo-navegar-dominios
description: Navega dominios y módulos FIBO (FND, BE, FBC, SEC, LOAN, etc.), localiza clases/propiedades vía Viewer o GitHub y registra IRIs con evidencia. Úsala cuando debas encontrar el concepto FIBO correcto antes de alinear o modelar.
metadata:
  author: yzylabs
  version: "1.0"
---

# Navegar dominios FIBO

## Propósito

Orientar la búsqueda en la ontología FIBO modular y devolver candidatos verificables con dominio, definición y fuente.

## Entradas

- Pregunta o concepto de negocio (p. ej. “cuenta de depósito”, “obligación contractual”, “entidad legal”).
- Contexto Open Banking / producto (opcional).
- Preferencia de ancla: release GitHub actual vs spec OMG formal (opcional).

## Procedimiento

1. Reformula el concepto en lenguaje de negocio, no de UI.
2. Selecciona dominios candidatos usando `references/mapa-dominios-fibo.md` (FND primero si es transversal).
3. Consulta FIBO Viewer (`https://spec.edmcouncil.org/fibo/ontology`) y/o paths en `https://github.com/edmcouncil/fibo`.
4. Lista 1–5 candidatos con: dominio, nombre, path/IRI, definición resumida.
5. Descarta candidatos por rol vs entidad, homonimia o deprecación (revisa release notes si hay duda).
6. Registra fecha de consulta y, si es material, release/tag.
7. No inventes clases ausentes en las fuentes.

## Salida

```md
## Navegación FIBO

- Concepto buscado: [...]
- Dominios explorados: [...]
- Candidatos:
  | Dominio | Concepto | Evidencia (URL/path) | Notas |
- Recomendación principal: [...]
- Descartados: [...]
- Fecha/fuente: [...]
```

## Casos límite

- Concepto solo de API/consentimiento PSD2 → puede no existir en FIBO; declara sin candidato y deriva a extensión.
- Clase deprecada por migración a OMG Commons → marca deprecación y busca reemplazo.
- Demasiados candidatos → prioriza FND/FBC/BE según el tipo de cosa (acuerdo, producto, entidad).

## Validación

- Cada candidato tiene URL o path de fuente primaria.
- Ningún IRI inventado.
- Dominios explorados justificados.

## Criterios de terminado

- Lista de candidatos usable para alineación.
- Recomendación principal o “sin cobertura” explícita.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | “legal entity” | Candidatos en BE/FND con evidencia |
| Ambiguo | “account” | Varios candidatos + desambiguación pedida |
| Límite | “AIS consent” | Sin cobertura FIBO clara + nota de extensión |

## Fuentes

- https://spec.edmcouncil.org/fibo (2026-08-04)
- https://github.com/edmcouncil/fibo (2026-08-04)
- https://spec.edmcouncil.org/fibo/release-notes (2026-08-04)
- `references/mapa-dominios-fibo.md`
