# Contrato de producción — HANDOFF_REG

Plantilla que Tsuru usa al cerrar un análisis regulatorio Open Finance para Sengoku.

```md
## HANDOFF_REG

### Metadatos
- Fecha:
- Agente: tsuru-regulacion-open-finance
- REPORT_TO: sengoku-director-legal-cumplimiento
- Jurisdicción(es):
- Rol de la entidad:
- Objetivo / decisión a desbloquear:
- Fecha de análisis:
- Estado: completo | parcial | borrador

### Fuentes primarias
| Instrumento | Emisor | Versión/fecha | URL o referencia | Notas |

### Fuentes secundarias (si aplica)
| Fuente | Rol | Limitación |

### Marco aplicable
| Marco | Artefacto técnico asociado | Estado (vigente/transición/litigado/aplazado) | Evidencia |

### Obligaciones materiales
| Obligación | Impacto (API/consent/security/ops) | Tipo (hecho/hipótesis) | Escala a | Fuente |

### Brechas (si hay baseline)
| Gap | Severidad | Evidencia actual | Owner sugerido | Dependencia legal? |

### Consentimiento / compartición
- Requisitos OF:
- Escalado a Corazon:
- Fuera de alcance privacidad:

### Cambio regulatorio (si aplica)
| Cambio | Escenario A | Escenario B | Decisión requerida |

### Fuera de alcance / no cubierto
-

### Riesgos
-

### Decisiones requeridas (Sengoku / counsel)
-

### Consumo por Jinbe (opcional)
- Resumen producto (no es dictamen):
```

## Estados

- `completo` — cobertura del alcance sin huecos materiales de fuente.
- `parcial` — usable; huecos explícitos.
- `borrador` — exploración; evidencia insuficiente para decisiones.

## Reglas

1. Cero obligación material sin fuente o marca de hipótesis.
2. No afirmar compliance en el handoff.
3. FAPI ≠ estándar de datos: documentar ambos si aplican, por separado.
