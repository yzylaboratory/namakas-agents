---
name: validar-entrega
description: Use esta skill antes de declarar completada una misión, fase o entregable para comprobar criterios de aceptación, coherencia entre resultados, pruebas ejecutadas, riesgos pendientes y preparación para uso o revisión.
compatibility: Compatible con Claude Code y Cursor mediante el estándar Agent Skills.
---

# Validar entrega

## Propósito

Evitar cierres falsos y asegurar que el resultado final cumple la misión.

## Entradas

- Objetivo.
- Alcance.
- Criterios de aceptación.
- Entregables.
- Evidencias.
- Resultados de pruebas.
- Riesgos y errores conocidos.

## Procedimiento

1. Verifica cada criterio de aceptación.
2. Revisa que todos los entregables existan.
3. Comprueba consistencia entre contratos, implementación, documentación y pruebas.
4. Confirma que las validaciones declaradas realmente fueron ejecutadas.
5. Revisa cambios fuera de alcance.
6. Identifica errores, deuda, riesgos y limitaciones.
7. Devuelve correcciones al responsable correspondiente.
8. Repite la validación después de las correcciones.
9. Clasifica la entrega.
10. Prepara el cierre y solicita al Cronista registrar decisiones relevantes.

## Clasificación

- **Aprobada:** cumple todos los criterios y puede utilizarse.
- **Aprobada con limitaciones:** cumple el objetivo, pero tiene limitaciones explícitas que no impiden su uso acordado.
- **Requiere corrección:** existen fallos solucionables antes de aprobar.
- **Bloqueada:** falta una dependencia o decisión material.
- **Rechazada:** no cumple el objetivo o se aparta del alcance.

## Lista de control

- [ ] Objetivo cubierto.
- [ ] Alcance respetado.
- [ ] Criterios verificados.
- [ ] Evidencia disponible.
- [ ] Pruebas ejecutadas.
- [ ] Contratos consistentes.
- [ ] Riesgos documentados.
- [ ] Errores conocidos visibles.
- [ ] Documentación actualizada.
- [ ] Siguiente responsable informado.

## Formato de salida

```md
## Veredicto

[Clasificación]

## Criterios de aceptación

| Criterio | Estado | Evidencia |
|---|---|---|

## Validaciones

- [...]

## Limitaciones y riesgos

- [...]

## Correcciones requeridas

- [...]

## Resultado final

[Resumen utilizable]
```

## Regla de cierre

No utilices “terminado” cuando:

- Falten pruebas disponibles.
- Existan criterios sin comprobar.
- Los resultados de agentes se contradigan.
- Un error material esté oculto.
- La entrega no pueda ser utilizada por su destinatario.
