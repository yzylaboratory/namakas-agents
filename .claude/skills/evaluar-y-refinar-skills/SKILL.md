---
name: evaluar-y-refinar-skills
description: Crea casos de prueba, compara resultados y refina activación, alcance e instrucciones de skills. Úsala para skills críticas, nuevas o que se activan demasiado o muy poco.
metadata:
  author: yzylabs
  version: "1.0"
---

# Evaluar y refinar skills

## Casos mínimos

Crea al menos:

1. Caso normal que debe activar la skill.
2. Redacción alternativa que también debe activarla.
3. Caso límite o ambiguo.
4. Caso negativo que no debe activarla, cuando sea relevante.

Guarda evaluaciones en:

```text
skills/<skill>/evals/evals.json
```

## Procedimiento

1. Define resultado esperado observable.
2. Ejecuta con la skill en contexto limpio.
3. Ejecuta sin la skill o con versión anterior.
4. Compara precisión, cobertura, errores, tiempo y ruido.
5. Revisa trazas para detectar pasos improductivos.
6. Ajusta descripción, alcance o procedimiento.
7. Repite la evaluación.
8. Conserva cambios que mejoren resultados sin inflar contexto.

## Salida

- Casos de evaluación.
- Comparación con baseline.
- Cambios aplicados.
- Evidencia de mejora o decisión de retirar la skill.

## Validación

Confirma que la skill mejora el resultado, se activa en los casos correctos y no añade ruido desproporcionado.

## Señales de mala skill

- Se activa para demasiadas solicitudes.
- Necesita otras cuatro skills para completar una acción simple.
- Repite conocimiento genérico.
- Contiene muchas opciones sin recomendación.
- Mezcla dominios no relacionados.
- No define evidencia de éxito.
