---
name: fibo-alinear-concepto-ob
description: Alinea un concepto de Open Banking/Open Finance al vocabulario FIBO con categoría exacto/cercano/parcial/sin cobertura y evidencia citada. Úsala cuando debas mapear términos de APIs, glosarios o productos OB a FIBO.
metadata:
  author: yzylabs
  version: "1.0"
---

# Alinear concepto Open Banking a FIBO

## Propósito

Producir una alineación trazable entre un término local OB y FIBO, sin fingir cobertura inexistente.

## Entradas

- Concepto local (nombre, definición operativa, superficie API/schema/glosario).
- Candidatos FIBO (de `fibo-navegar-dominios`) o permiso para navegar primero.
- Restricciones de naming del ecosistema (opcional).

## Procedimiento

1. Captura el concepto local con definición y ejemplo.
2. Si no hay candidatos FIBO, ejecuta navegación de dominios primero.
3. Completa `references/plantilla-alineacion-concepto.md`.
4. Elige categoría: exacto | cercano | parcial | sin cobertura.
5. Define término canónico, alias y “no usar” (homónimos).
6. Si sin cobertura: documenta hueco; no inventes clase FIBO; apunta a extensión/puente.
7. Registra impacto esperado en APIs/datos.

## Salida

Ficha de alineación completa (plantilla) más resumen:

```md
## Alineación

- Local: [...]
- FIBO: [dominio / concepto]
- Categoría: [...]
- Canónico: [...]
- Evidencia: [...]
- Hueco/extensión: [...]
```

## Casos límite

- Varios sistemas usan el mismo label con significados distintos → produce filas por sistema.
- Conflicto con término BIAN homónimo → documenta distinción; no fusiones estándares.
- Pedido de “forzar FIBO” sin clase → rechaza; propone extensión local.

## Validación

- Categoría presente.
- Evidencia primaria citada.
- Sin IRIs inventados.

## Criterios de terminado

- Ficha usable por Robin/implementadores.
- Huecos explícitos si aplica.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | “payment account balance” con candidatos FBC/FND | Alineación cercana/exacta documentada |
| Ambiguo | “customer” | Desambiguación Party/Legal Person/role |
| Límite | “consentId PSD2” | sin cobertura + extensión propuesta |

## Fuentes

- https://spec.edmcouncil.org/fibo (2026-08-04)
- https://edmcouncil.org/frameworks/industry-models/fibo/ (2026-08-04)
- https://doi.org/10.3390/app13031447 (secundaria OB/OBO, 2026-08-04)
- `references/plantilla-alineacion-concepto.md`
