---
name: sintetizar-informe-reconocimiento
description: Consolida el reconocimiento en un informe HANDOFF_EXPLORADOR con hechos, riesgos, vacíos y siguiente paso. Úsala al cerrar una exploración o cuando otro agente deba continuar sin redescubrir el terreno.
metadata:
  author: yzylabs
  version: "1.0"
---

# Sintetizar informe de reconocimiento

## Propósito

Entregar un handoff autocontenido, accionable y honesto sobre lo mapeado.

## Entradas

- Resultados de delimitación, mapa, docs y dependencias.
- Preguntas originales y criterios de suficiente.
- Consumidor del handoff.

## Procedimiento

1. Relee las preguntas de descubrimiento acordadas.
2. Resume en ≤10 líneas qué se sabe con confianza.
3. Organiza el mapa y las integraciones sin repetir ruido.
4. Clasifica hallazgos: observado / inferido / desconocido.
5. Prioriza riesgos por impacto en la decisión pendiente.
6. Adjunta evidencia clave (pocas citas de alta señal).
7. Lista fuentes con fecha/versión.
8. Recomienda un único siguiente paso y el agente/rol consumidor.
9. Confirma que fuera de alcance se respetó.
10. No cueles diseño de solución ni implementación “de regalo”.

## Salida

```md
## HANDOFF_EXPLORADOR

### Resumen
### Preguntas respondidas / pendientes
### Mapa
### Dependencias e integraciones
### Hallazgos
### Riesgos y vacíos
### Evidencia clave
### Fuentes
### Recomendación de siguiente paso
### Fuera de alcance respetado
```

## Casos límite

- Exploración parcial por tiempo: declara cobertura % cualitativa y vacíos.
- Contradicción docs vs código: sección de conflictos obligatoria.
- Nada encontrado: informe de vacío con hipótesis de búsqueda fallida.

## Validación

- Toda afirmación material tiene tipo (observado/inferido/desconocido).
- Hay recomendación principal de siguiente paso.
- No hay cambios de código atribuidos a esta misión (salvo artefacto pedido).

## Criterios de terminado

- El consumidor puede actuar sin releer todo el chat.
- Riesgos críticos no están enterrados al final sin destaque.
- Preguntas sin respuesta están explícitas.

## Casos de evaluación

| Caso | Entrada | Esperado |
|---|---|---|
| Normal | Mapa + deps listos | HANDOFF completo con siguiente paso a Law/Luffy |
| Ambiguo | Notas dispersas sin preguntas | Reconstruye preguntas o marca misión mal delimitada |
| Límite | Solo 1 carpeta revisada de 20 | Cobertura explícita + vacíos + no afirmar mapa total |

## Fuentes

- Contrato `HANDOFF_EXPLORADOR` en `Delegacion.md` de Noland.
- Cursor Subagents — retorno de resultados al padre (consultado 2026-08-04).
