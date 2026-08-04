---
name: crear-agentes-en-lote
description: Crea múltiples agentes desde un catálogo, procesando únicamente elementos pendientes, controlando duplicados, dependencias, consistencia y validación por agente. Úsala cuando el usuario solicite generar una tripulación o departamento completo.
metadata:
  author: yzylabs
  version: "1.0"
---

# Crear agentes en lote

## Entradas

- `catalogo/agentes-one-piece.yaml`.
- Agentes existentes.
- Convenciones y plantillas.

## Procedimiento

1. Lee el catálogo completo.
2. Excluye agentes con `status: completed`, salvo actualización explícita.
3. Valida personajes únicos y nombres de carpeta.
4. Ordena por:
   - Agentes generales.
   - Directores.
   - Células dependientes.
5. Procesa un agente a la vez para las escrituras.
6. Puede paralelizar investigación de dominios independientes.
7. Por cada agente ejecuta el flujo completo:
   - Analizar.
   - Investigar.
   - Seleccionar personaje.
   - Diseñar.
   - Generar.
   - Crear adaptadores.
   - Validar.
   - Evaluar skills críticas.
8. Cambia el estado a `completed` solo después de aprobar.
9. Registra errores con `status: blocked` y motivo.
10. Ejecuta validación global al terminar.

## Control de consistencia

- Ningún personaje duplicado.
- Ninguna skill con el mismo propósito en agentes hermanos sin justificación.
- Directores delegan a células existentes.
- Células escalan al director correcto.
- Nombres y departamentos coinciden con el catálogo.

## Validación

- Ejecuta el validador por agente.
- Ejecuta una validación global de personajes, nombres, delegaciones y skills duplicadas.
- Confirma que solo los agentes aprobados cambian a `completed`.

## Salida

```md
Agentes creados:
Agentes actualizados:
Agentes bloqueados:
Validación global:
Decisiones de reasignación:
```
