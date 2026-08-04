---
name: auditar-trazabilidad-cumplimiento-open-finance
description: Audita un brief o HANDOFF_REG Open Finance contra invención, claims de compliance, fuentes faltantes y confusión FAPI/datos. Úsala antes de marcar un análisis como completo o cuando Sengoku pida control de calidad.
metadata:
  author: yzylabs
  version: "1.0"
---

# Auditar trazabilidad de cumplimiento Open Finance

## Propósito

Detectar fallas de trazabilidad regulatoria antes de escalar o cerrar: invención, compliance vacío, fuentes secundarias únicas, mezcla FAPI/datos, dictámenes no autorizados.

## Entradas

- `HANDOFF_REG` o brief candidato.
- Marcos/gaps/consent usados como input.
- Criterios de aceptación de la misión.

## Procedimiento

1. Verifica que cada obligación material tenga fuente primaria o marca de hipótesis.
2. Busca claims “compliant/cumplimos/certificados” sin evidencia → falla.
3. Detecta fechas de vigencia no respaldadas por el regulador → falla.
4. Comprueba separación FAPI vs estándar de datos.
5. Verifica escalamientos Corazon/Cobra/Sengoku cuando el contenido lo exige.
6. Confirma que el estado (`completo`/`parcial`/`borrador`) coincide con huecos.
7. Emite veredicto: `aprobado` | `aprobado_con_limitaciones` | `rechazado` + lista de hallazgos.

## Salida

```md
## Auditoría trazabilidad OF
- Veredicto:
- Hallazgos:
| ID | Severidad | Hallazgo | Remedio |
## Claims prohibidos detectados
## Estado recomendado del HANDOFF_REG
```

## Casos límite

- Brief vacío → rechazado.
- Solo fuentes secundarias → máximo `aprobado_con_limitaciones` si hipótesis explícitas; si no, rechazado.
- Dictamen vinculante sin mandato Sengoku → rechazado.

## Validación

- Checklist de invención y compliance vacío ejecutado.
- Veredicto justificado.

## Criterios de terminado

- Veredicto + hallazgos entregados.
- Remedio claro por hallazgo material.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | HANDOFF con fuentes | Aprobado o limitaciones menores |
| Ambiguo | Mezcla FAPI como “dato” | Hallazgo + rechazo o limitaciones |
| Límite | “Somos compliant PSD2” | Rechazado |

## Fuentes

- `references/contrato-produccion-handoff-reg.md`
- Reglas de Tsuru (`Reglas.md`)
- OpenID FAPI — https://openid.net/wg/fapi/ — 2026-08-04
