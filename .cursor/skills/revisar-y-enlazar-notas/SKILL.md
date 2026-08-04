---
name: revisar-y-enlazar-notas
description: Revisa capturas recientes del vault, promueve lo durable a notas permanentes y añade enlaces entre diario, decisiones y ADR. Úsala en revisiones periódicas o cuando la memoria esté fragmentada.
metadata:
  author: yzylabs
  version: "1.0"
---

# Revisar y enlazar notas

## Propósito

Evitar que el diario se convierta en vertedero: promover aprendizaje reutilizable y conectar artefactos relacionados.

## Entradas

- Ventana a revisar (p. ej. últimos 7 días).
- Temas o MOC a actualizar (opcional).
- Criterio de promoción (reutilizable / recurrente / decisión vigente).

## Procedimiento

1. Lista diarios y decisiones en la ventana.
2. Marca candidatos a nota permanente (una idea clara, útil fuera del día).
3. Crea o actualiza `memoria/permanente/slug.md` en palabras propias, atómica.
4. Añade enlaces bidireccionales razonables (diario ↔ decisión ↔ ADR ↔ permanente).
5. Detecta ADR `proposed` estancados o decisiones `en duda`; listarlos para Luffy.
6. No reescribas historia: corrige enlaces y notas permanentes, no reescribas hechos del diario sin nota de corrección.

## Salida

```md
## Revisión

- Ventana:
- Promovidas:
- Enlaces añadidos:
- Conflictos / estancados:
```

## Casos límite

- Nada promocionable → reporta “sin promoción” y limpia solo enlaces rotos si los hay.
- Nota permanente duplicada → fusiona por enlace, no copies párrafos enteros.
- Diario con secretos antiguos → redacta al tocar; no propagues el secreto.

## Casos de evaluación

- Normal: 3 diarios con un aprendizaje repetido → 1 permanente + enlaces.
- Ambiguo: captura mezclada hecho/opinión → separar antes de promover.
- Límite: ADR proposed sin dueño → listar escalamiento, no accepted automático.

## Validación

- Enlaces apuntan a rutas existentes.
- Permanentes son atómicas (una idea principal).
- Diario original no quedó truncado.

## Criterios de terminado

- Informe de revisión entregado.
- Promociones y enlaces aplicados o justificados.

## Fuentes

- Prácticas PARA + Zettelkasten ligero (captura diaria → nota permanente enlazada) — contraste secundario, 2026-08-04.
- `references/estructura-memoria.md`
