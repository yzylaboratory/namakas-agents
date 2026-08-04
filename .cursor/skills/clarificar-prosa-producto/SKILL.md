---
name: clarificar-prosa-producto
description: Reescribe textos de producto confusos, redundantes o engañosos en prosa clara para humanos. Úsala cuando exista un draft, README, copy o requisitos ya escritos que deban ganar claridad sin cambiar hechos.
metadata:
  author: yzylabs
  version: "1.0"
---

# Clarificar prosa de producto

## Propósito

Mejorar legibilidad, precisión y tono de textos existentes sin inventar nuevas capacidades ni diluir riesgos.

## Entradas

- Texto fuente (archivo o fragmento).
- Audiencia objetivo.
- Restricciones de tono/marca si existen.
- Hechos que no deben cambiar.
- Idioma de salida (mantener el del fuente salvo pedido).

## Procedimiento

1. Identifica la intención del texto (orientar, instruir, persuadir con hechos, exigir).
2. Extrae afirmaciones fácticas y sepáralas de relleno.
3. Reescribe con:
   - Voz activa.
   - Oraciones cortas.
   - Términos consistentes.
   - Jerarquía (títulos, listas) cuando ayude a escanear.
4. Sustituye ambigüedades (“fácilmente”, “robusto”, “etc.”) por concreto o elimínalas.
5. Conserva advertencias y limitaciones; no las suavices.
6. Entrega diff conceptual: qué cambió y por qué (breve).
7. Lista cualquier hecho que no pudiste verificar.

## Salida

```md
## Texto revisado

[…]

## Cambios materiales

- […]

## Hechos no verificados / supuestos

- […]

## Riesgos de tono o exactitud restantes

- […]
```

Si la tarea pide edición in-place, aplica el texto en el archivo y resume los cambios.

## Casos límite

- Texto legal/compliance: clarifica forma solo con cuidado; no reinterpretar obligaciones.
- Marketing vs. producto: separa claims; elimina o marca lo no demostrable.
- Traducción implícita: no cambies idioma salvo pedido.
- Texto ya claro: di que no requiere reescritura; no “mejorar” por completar.

## Validación

- No se añadieron features nuevas.
- Riesgos materiales siguen visibles.
- El texto es más escaneable y concreto.
- Terminología consistente dentro del fragmento.

## Criterios de terminado

- Versión revisada entregada.
- Cambios materiales explicados en breve.
- Huecos de evidencia listados.

## Evaluación sugerida

| Caso | Entrada | Esperado |
|---|---|---|
| Normal | Párrafo con jerga y pasiva | Prosa activa y concreta |
| Ambiguo | Copy con claim “el más seguro del mercado” | Eliminar/marcar claim sin evidencia |
| Límite | Texto de política de privacidad | Claridad superficial + escalamiento; no reescribir obligaciones |

## Fuentes

- Google developer documentation style guide (voz, claridad, consistencia) — https://developers.google.com/style (2026-08-04)
- Preferir bueno mantenible sobre “perfecto” ornamental — Google docguide best practices (2026-08-04)
