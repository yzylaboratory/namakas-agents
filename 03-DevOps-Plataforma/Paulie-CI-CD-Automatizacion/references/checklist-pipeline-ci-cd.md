# Checklist CI/CD — Paulie

Referencia operativa rápida. Fuentes: GitHub Actions security hardening, GitLab CI YAML, DORA (consultado 2026-08-04).

## Diseño CI

- [ ] Pipeline-as-code en el repositorio
- [ ] Triggers y path filters explícitos
- [ ] Orden fail-fast (barato → caro)
- [ ] Toolchain pineado (versión/digest)
- [ ] Artefactos publicados para CD

## CD

- [ ] Build once / promote many
- [ ] Delivery vs deployment etiquetado
- [ ] Environments protegidos en prod (o justificación)
- [ ] Rollback documentado y probado al menos una vez
- [ ] Handoff GitOps/IaC si el deploy no es solo job

## Quality gates

- [ ] Umbrales bloqueantes documentados
- [ ] Reportes como artefactos o enlaces
- [ ] Política flaky con dueño
- [ ] Excepciones con fecha de caducidad

## Seguridad

- [ ] Sin secretos en plaintext
- [ ] Least privilege en tokens
- [ ] OIDC preferido a keys estáticas
- [ ] Acciones críticas pineadas a SHA
- [ ] Sin interpolación peligrosa de inputs en shell

## Rendimiento

- [ ] Baseline medido antes de optimizar
- [ ] Cache keys por lockfile/hash
- [ ] Paralelismo con critical path claro
- [ ] No se removieron gates de seguridad sin aprobación

## Fronteras

| Tema | Dueño |
|---|---|
| Pipelines CI/CD | Paulie |
| GitOps sync | Capone Bege |
| IaC / cloud | Haredas |
| SRE / observabilidad runtime | Viola |
| Estrategia QA producto | Usopp-QA Nakamas |
| Prioridad departamento | Franky |
