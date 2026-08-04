---
name: guiar-sesion-y-captura-evidencia
description: Facilita o estructura sesiones de entrevista/usability testing y captura evidencia sin sesgar al participante. Úsala durante o al preparar la ejecución de sesiones con usuarios.
metadata:
  author: yzylabs
  version: "1.0"
---

# Guiar sesión y captura de evidencia

## Propósito

Obtener evidencia confiable: comportamiento y relato, con mínima interferencia y máxima trazabilidad.

## Entradas

- Test plan / discussion guide.
- Consentimiento documentado (o checklist de obtención).
- Prototipo o sistema bajo prueba.
- Rol: moderador, co-piloto o analista de grabaciones autorizadas.

## Procedimiento

1. Reconfirma consentimiento y derecho a retirarse al inicio.
2. Enmarca la sesión: no se evalúa a la persona; se evalúa el diseño.
3. Usa think-aloud en usability testing; evita enseñar la UI.
4. Haz preguntas abiertas y neutrales; prohíbe leading (“¿Fácil, verdad?”).
5. Prioriza observación de comportamiento sobre opiniones abstractas.
6. Captura por tarea: éxito/fallo, fricciones, errores, tiempo aproximado, citas anonimizadas.
7. Nota contexto (dispositivo, entorno, interrupciones) que afecte validez.
8. Cierra con debrief corto; no “vendas” la solución del equipo.
9. Anonimiza notas antes de compartir; separa raw notes de insights.

## Salida

```md
## Registro de sesión (anonimizado)
- ID sesión / fecha / perfil (sin PII)
- Consentimiento: sí/no + alcance
- Tareas y resultados
- Observaciones (comportamiento)
- Citas (anonimizadas)
- Incidentes / sesgos de moderación
- Materiales retenidos (según consentimiento)
```

## Casos límite

- Participante en distress: prioriza bienestar; detén si hace falta.
- Stakeholder interrumpe o corrige al usuario: interrumpe la dinámica y documenta contaminación.
- Solo hay grabación sin consentimiento de compartir: no uses clips; trabaja con notas agregadas si está permitido.

## Validación

- Notas separan observado vs dicho.
- No hay PII innecesaria.
- Tareas del plan fueron cubiertas o desviaciones documentadas.

## Criterios de terminado

- Cada sesión produce un registro usable para síntesis.
- No se filtraron datos personales a canales abiertos.

## Casos de evaluación

| Caso | Entrada | Esperado |
|---|---|---|
| Normal | Sesión moderada de 45 min | Registro por tarea + citas anonimizadas |
| Ambiguo | “Toma notas de la call” | Exige estructura observación/dicho + consentimiento |
| Límite | Stakeholder guía al usuario | Documenta sesgo; marca validez reducida |

## Fuentes

- NN/g — prácticas de usability testing / think-aloud (artículos de métodos y planning, consultado 2026-08-04).
- NN/g — Obtaining Consent for User Research (consultado 2026-08-04).
- Reglas de Chopper — ética y evidencia.
