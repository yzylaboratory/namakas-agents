# TuBanco — schema hub (durable)

> **Nakamas forge 2026-08-05.** Hosts y usuarios **no** se documentan aquí con secretos. Conexión solo vía env `TUBANCO_*` (ver `.env.example` en la raíz del repo). Experto live-SQL: `mont-dor-tubanco-sql` bajo `katakuri-director-backend`. ≠ Pudding (persistencia greenfield); ≠ cores Iceburg.

## Alcance

| Campo | Valor |
|-------|-------|
| Sistema | TuBanco (App Empresas / Banreservas cuando aplique) |
| Motor | Azure SQL Managed Instance (T-SQL) |
| Entornos | `des`, `qa` |
| Puerto típico | `1433` (MI VNet-local / endpoint documentado por Azure) |
| Modo por defecto | **read-only** |

## Credenciales (nombres de env — sin valores)

| Variable | Uso |
|----------|-----|
| `TUBANCO_DES_SERVER` | FQDN instancia DES |
| `TUBANCO_DES_USER` | Usuario DES |
| `TUBANCO_DES_PASSWORD` | Password DES (solo local/keychain) |
| `TUBANCO_QA_SERVER` | FQDN instancia QA |
| `TUBANCO_QA_USER` | Usuario QA |
| `TUBANCO_QA_PASSWORD` | Password QA (solo local/keychain) |
| `TUBANCO_DEFAULT_ENV` | `des` \| `qa` (opcional) |
| `TUBANCO_DES_DATABASE` | DB name DES (opcional; completar con evidencia) |
| `TUBANCO_QA_DATABASE` | DB name QA (opcional; completar con evidencia) |

## Hubs de negocio

DB QA principal (live 2026-08-06): `DevOps_DO_BR_ICB7_AZ_QA`. Otras: snapshots `*_23102025-*` / `*_27102025-*`, `*_MIG`, `*_Logging`, `UY_Infocorp_ICBanking_aspnetdb`, `DBATools`.

| Schema | Objeto | Rol | Evidencia |
|--------|--------|-----|-----------|
| dbo | Users | Login Empresas: UserName, Password, DocumentTypeId, DocumentNumber (cifrado at-rest Base64), UserStatusId | QA live 2026-08-06 |
| dbo | DocumentTypes | Catálogo tipo doc (ej. 3=CÉDULA DE IDENTIDAD, 10=PASAPORTE, 101=RNC) | QA live 2026-08-06 |
| dbo | Sites | Organización/empresa (SiteId, Name, SiteTypeId Company\|Person) | QA live 2026-08-06 |
| dbo | Clients | Identificación org/cliente: DocumentTypeId + DocumentNumber (cifrado); SiteId FK | QA live 2026-08-06 |
| dbo | SiteAditionalData | PrincipalClientId por Site | QA live 2026-08-06 |
| — | Login Empresas | `identificacionOrganizacion.numeroDocumento` ↔ Clients.DocumentNumber (at-rest encrypted); Users.SiteId → Site → Client | QA live 2026-08-06 |
| dbo | ReservedUsers | Username + DocumentTypeId + DocumentNumber | QA live 2026-08-06 |
| BackOffice | Users | Backoffice users (UserName/Password; sin Document*) | QA live 2026-08-06 |
| Migration | Users | Staging migración de usuarios | QA live 2026-08-06 |

## Notas de discovery

- Preferir `sys.tables` / `sys.columns` / `sys.foreign_keys` para detalle.
- Usar `INFORMATION_SCHEMA.TABLES` / `COLUMNS` cuando se necesite vista ISO.
- Ampliar esta sección solo con SQL ejecutado y fecha.
- `dbo.Users.DocumentNumber` / `Clients.DocumentNumber`: ciphertext Base64 (no cédula/RNC en claro). `Password`: en QA la mayoría vacío; subset corto parece plaintext de prueba (no hash membership).

## Seguridad

- Nunca pegar passwords, connection strings con `User Id`+`Password`, ni dumps PII en este hub, vault Obsidian, ni git.
- Si credenciales circularon en chat: rotar tras setup local.
