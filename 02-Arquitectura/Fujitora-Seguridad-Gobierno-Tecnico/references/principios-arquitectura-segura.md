# Principios de arquitectura segura (referencia operativa)

Síntesis accionable para revisiones. Fuentes primarias citadas en Rol.md (consultado 2026-08-04).

## Principios base (ISO/IEC 27001:2022 A.8.27 / ingeniería segura)

1. **Menor privilegio** — identidades y componentes solo con permisos necesarios.
2. **Defensa en profundidad** — controles en capas; un fallo no abre todo.
3. **Fallar seguro** — ante error, denegar / degradar de forma controlada.
4. **Defaults seguros** — configuración inicial restrictiva.
5. **Segregación / aislamiento** — separar dominios de riesgo (red, proceso, datos, tenants).
6. **Decisiones documentadas** — ASVS 5.0 enfatiza Documented Security Decisions.

## Confianza cero (NIST SP 800-207)

- No hay confianza implícita por ubicación de red ni ownership del activo.
- Autenticación y autorización son funciones discretas antes de acceder al recurso.
- Políticas dinámicas; enforcement en puntos explícitos (PEP).
- Recursos (no solo el perímetro) son el foco de protección.

## Outcomes útiles (NIST CSF 2.0)

- **Govern (GV)** — roles, política, oversight, supply chain cyber.
- **Identify** — activos, riesgos, dependencias.
- **Protect** — controles preventivos sobre activos críticos.

## Uso

Aplicar solo los principios relevantes al alcance. No exigir Zero Trust completo a un cambio cosmético. Registrar qué principios se evaluaron y cuáles quedaron fuera con justificación.
