# Contrato de producción — HANDOFF_SEGURIDAD

Consumidores típicos: `law-director-arquitectura`, `robin-tratadista`, implementación Backend/DevOps vía cadena de mando.

## Bloque obligatorio

```md
## HANDOFF_SEGURIDAD

| Campo | Valor |
|---|---|
| Fecha | YYYY-MM-DD |
| Productor | fujitora-seguridad-gobierno-tecnico |
| Objetivo | |
| Alcance incluido | |
| Fuera de alcance | |
| Frameworks de referencia | NIST CSF 2.0 / ASVS 5.0 / NIST SP 800-207 / ISO 27001 A.8.27 (según aplique) |
| Estado | completo \| parcial \| borrador |

### Supuestos de amenaza
- ...

### Trust boundaries e identidades
- ...

### Amenazas priorizadas
| ID | Amenaza | Activo | Severidad | Evidencia |
|---|---|---|---|---|

### Controles recomendados
| ID | Control | Tipo (P/D/C) | Traza a | Evidencia de verificación |
|---|---|---|---|---|

### Riesgos residuales y excepciones
| ID | Residual / excepción | Owner sugerido | Caducidad sugerida |
|---|---|---|---|

### Requisitos para contratos (Robin)
- AuthN/AuthZ: ...
- Datos sensibles: ...
- Errores / logging seguro: ...

### Fuera de cobertura / pendientes
- ...

### Fuentes
- ...
```

## Estados

- `completo` — alcance cubierto sin huecos materiales; residuales documentados.
- `parcial` — usable para decidir, con huecos explícitos.
- `borrador` — exploración inicial o evidencia insuficiente.

## Reglas

- Cero controles sin traza a amenaza/requisito.
- Cero secretos/PII reales.
- No afirmar certificación o cumplimiento legal.
