> **Nakamas adaptation (2026-08-04).** Schema hub preserved; hosts sanitized to placeholders; no passwords. Live SQL expert: `kizaru-core-cadencie` under `iceburg-director-sistemas-core`. ≠ Crocus/Tom/Kaku; ≠ Tripulación `brd-*`.

# Cadencie Oracle QA — schema map (credit cards)

**Core:** Cadencie — tarjetas de crédito Banreservas  
**Environment:** Oracle QA (`PCAD36` / service `PDBUC36`)  
**Explored:** 2026-07-27 (read-only, `oracledb` thin)  
**Primary MS:** `ms-credit-cards-v2`, `ms-credit-cards-inquiries` (+ EAI SOAP helpers in same DB user)  
**Catalog size:** **412** tables + **7** views under owner `CADENCIE` (do not dump all; below is MS-relevant subset)

Related baselines (project):  
`<BANRESERVAS_TC_PROJECT_ROOT>/…

---

## 1. Purpose

Cadencie is the **legacy credit-card core** used by Banreservas inquiry / list / detail / transaction flows: plastics (`CARD`), dual-currency accounts (`ACCT` DOP/USD), product catalog (`PRMCN`), customer/document (`CUSTR`), statements (`STMT`), posted events (`EVENT`), close/status codes (`CLOCD`), Credimás (`MPUR`/`MSTM`), and generic code tables (`CODES`).

Not Way4 (OpenWay) and not Cortex (debit/PCI).

---

## 2. Connection summary (no password)

| Field | Value |
|-------|--------|
| Host | `<HOST_PRIVATE_CADENCIE>` |
| Port | `1521` |
| Service | `pdbuc36` |
| User | `appsdbuc` |
| DB name (session) | `PCAD36` |
| Preferred client | Python `oracledb` thin or `sqlplus` EZCONNECT |
| Credential source | IAC `iac/iac-onpremise-dev-qa/aks-cluster/apps/integraciones/overlays/qa/secret/ms-credit-cards-inquiries.env` keys `quarkus.datasource.username` / `quarkus.datasource.password`. JDBC URL in sibling configmap. Resolve at runtime; **never** write password into skill/schema files. |
| Network | Private IP — **corporate VPN required**. Timeout → stop and report VPN. |

```bash
# After loading ORACLE_USER / ORACLE_PASS (never echo)
python3 -c "import oracledb,os; c=oracledb.connect(user=os.environ['ORACLE_USER'],password=os.environ['ORACLE_PASS'],dsn='<HOST_PRIVATE_CADENCIE>:1521/pdbuc36',tcp_connect_timeout=8); print(c.version); c.close()"
```

See also: [Iceburg connections](../../Iceburg-Director-Sistemas-Core/references/connections.md), [protocolo compartido](../../Iceburg-Director-Sistemas-Core/skills/consultar-cores-bancarios-sql/SKILL.md).

---

## 3. Key schemas / owners

| Owner | Role |
|-------|------|
| **CADENCIE** | Physical tables (~412). Qualify as `CADENCIE.CARD` when needed. |
| **APPSDBUC** | Login user for MS JDBC. Synonyms for core tables + **~127 procedures** (LI_*, GET_*, EAI_*). Prefer unqualified names (`CARD`, `PRMCN`) via synonyms. |
| **ALOYAL** / **APPSQUARKUS** | Other synonym consumers (ignore for credit MS). |

Session probe (2026-07-27): `USER=APPSDBUC`, `DB_NAME=PCAD36`, `SERVICE_NAME=PDBUC36`.

Currencies used everywhere: **`214` = DOP**, **`840` = USD**.

Cadencie **day** fields (`ISSUE_DAY`, `STM_CLOSDY`, `EMV_EFFDAY`, `FEC_PRIMER`, …) are often **days since 1957-01-01** (`TO_DATE('1957-01-01') + day`). Helpers: `eai_fecha_cadencie()`, `FromDefaultDate()`.

---

## 4. Card / account model (join spine)

```
CUSTR (party / document)
   └── CARD  BANK + CUSTR_NBR
         │     PROFIL ──────────────► PRMCN.PRODUCT  (product catalog)
         │     CANCL_CODE ──────────► CLOCD.CLOSE_CD (status catalog)
         │     ACCOUNT + BANK
         ├── ACCT  BANK + ACCOUNT  (or CARD_NBR) + CURR_NUM ∈ {214,840}
         │     ├── STMT  BANK + ACCOUNT + MONTH_NBR (= ACCT.MONTH_NBR - 1 for due date)
         │     ├── MSTM  BANK + ACCOUNT + MONTH_NBR  (Credimás rem capital)
         │     └── MPUR  ACCOUNT + STATUS='A'       (active Credimás purchase)
         └── EVENT  CARD_NBR  (posted txns; ISPEC TRAN/MPTR)
```

**MS conventions**

| Rule | Expression |
|------|------------|
| Principal vs additional | `DECODE(SUBSTR(CARD_NBR,-3,1),'1',0,1)` → `0` principal, `1` additional |
| Active status | `CANCL_CODE = ' '` (space). MS filters often `DECODE(CANCL_CODE,' ','_',CANCL_CODE)` |
| Pending activation | `PendienteActivacion(code)` / `CANCL_CODE = 'T'` |
| Embossed | `EMBOSS_CRD = '1'` |
| Renewal reason | `ISSUE_REAS = 'X'` (`CODES.CODE_TYPE='RCISS'`) |
| Product join | `CARD.PROFIL = PRMCN.PRODUCT` (not `CARD.PRODUCT` alone for MS list/detail) |
| Quota / garantía | `TRIM(ACCT.ACC_TYPE)` as `QUOTA_TYPE` (`Z`, `EM`, `CG`, …) — **not** `TIP_CUOTA` |
| Detail DOP account | Prefer `CARD`→`ACCT` on `BANK`+`ACCOUNT`+`CURR_NUM=214` (EAI path); list SP often joins `ACCT` on `CARD_NBR` |

Mask PAN as `BIN********LAST4`. Never dump full PAN lists or customer name/email samples into vault/skill outputs.

---

## 5. Important tables / views

### 5.1 `CADENCIE.CARD` — plastic / device

**Purpose:** One row per card (PAN). Status, emboss, expiry, link to customer and account.  
**Est. rows (QA):** ~4.4M · **cols:** 179

| Column | Type | Meaning |
|--------|------|---------|
| `CARD_NBR` | `VARCHAR2(19)` | PAN (mask in outputs) |
| `CUSTR_NBR` | `VARCHAR2(12)` | Customer id / document number (padded) |
| `ACCOUNT` | `NUMBER(11)` | Account number |
| `BANK` | `NUMBER(2)` | Bank (typically `1`) |
| `PROFIL` | `NUMBER(2)` | Product profile → `PRMCN.PRODUCT` |
| `PRODUCT` | `NUMBER(2)` | Product code field (prefer `PROFIL` for MS joins) |
| `CANCL_CODE` | `VARCHAR2(1)` | Card status / close code |
| `CANCL_NEW` | `VARCHAR2(1)` | Pending/new status code |
| `ISSUE_STS` | `NUMBER(1)` | Issue status (QA mostly `9`) |
| `ISSUE_REAS` | `VARCHAR2(1)` | Issue reason (`RCISS` in `CODES`) |
| `ISSUE_DAY` | `NUMBER(5)` | Issue day (1957 epoch) |
| `EMBOSS_NME` | `VARCHAR2(26)` | Embossed name (PII — do not sample) |
| `EMBOSS_CRD` | `VARCHAR2(1)` | Emboss flag (`1` embossed) |
| `EXPIRY_DTE` / `EXPIRY_NEW` | `NUMBER(4)` | Expiry YYMM |
| `SUP_LIMIT` | `NUMBER(10)` | Supplementary limit |
| `VALID_FROM` | `NUMBER(4)` | Valid-from |
| `DESPATCH` | `VARCHAR2(4)` | Delivery method code |
| `EMV_EFFDAY` / `FEC_PRIMER` | `NUMBER(5)` | EMV / member-since days |
| `CURR_NUM` | `NUMBER(3)` | Currency on card row |

**Useful indexes (no formal PK constraints):**  
- Unique `PCARDNUMB` (`CARD_NBR`, `CARDHOLDER`)  
- Unique `PCARDISSU` (`BANK`, `ISSUE_STS`, `EXPIRY_DTE`, `CARD_NBR`, `CARDHOLDER`)  
- Nonunique `CARD_IND_1` (`CUSTR_NBR`), `IND_CARD_ACCOUNT` (`ACCOUNT`)

**Common joins:** `CUSTR` on `BANK`+`CUSTR_NBR`; `ACCT` on `BANK`+`ACCOUNT` or `CARD_NBR`; `PRMCN` on `PROFIL=PRODUCT`; `CLOCD` on `CANCL_CODE=CLOSE_CD`.

---

### 5.2 `CADENCIE.ACCT` — account balances / limits

**Purpose:** Account ledger per currency (DOP/USD). Limits, balances, payments, interest, quota type.  
**Est. rows:** ~4.3M · **cols:** 339

| Column | Type | Meaning |
|--------|------|---------|
| `BANK` | `NUMBER(2)` | Bank |
| `ACCOUNT` | `NUMBER(11)` | Account |
| `CARD_NBR` | `VARCHAR2(19)` | Linked PAN |
| `CURR_NUM` | `NUMBER(3)` | `214` DOP / `840` USD |
| `CRED_LIMIT` | `NUMBER(10)` | Credit limit |
| `CREDLIM_X` | `NUMBER(6)` | Alt USD limit (when `CRED_LIMIT=0`) |
| `ACC_TYPE` | `VARCHAR2(4)` | Quota type → MS `quotaType` |
| `PRODUCT` | `NUMBER(2)` | Product on account |
| `CLASS_CODE` | `VARCHAR2(3)` | Customer class |
| `CYCLE_NBR` | `NUMBER(2)` | Billing cycle |
| `MONTH_NBR` | `NUMBER(3)` | Current statement month code |
| `STM_CLOSDY` | `NUMBER(5)` | Statement close day (1957 epoch) |
| `STM_BALNCE` | `NUMBER(15,2)` | Statement balance |
| `STM_MINDUE` | `NUMBER(15,2)` | Min due |
| `PAYMT_CLRD` / `PAYMT_FREE` / `PAYMT_UNCL` | amounts | Cleared / in-transit / adjustments |
| `AUTHS_AMT` | `NUMBER(15,2)` | Pending authorizations |
| `INT_RATE` | `NUMBER(6,4)` | Interest rate |
| `CAPITAL` / `SOFI_CASHA` | `NUMBER(15,2)` | Used in available-credit EAI formula |
| `CASH_ADVCE` / `CASH_ADFEE` | `NUMBER(15,2)` | Cash advance / fee |
| `APP_SOURCE` | `VARCHAR2(10)` | Application source |
| `BUSINESS` | `NUMBER(6)` | Business flag (Credimás rem capital gate) |
| `MP_BIL_AMT` | `NUMBER(15,2)` | Credimás monthly installment |
| Balance components | various | `DEBIT_ADJ`, `PURCHASES`, `INT_CHGD`, `STM_BALINT`, `BAL_INT`, … for `GetAccountBalance` / interest |

**Useful indexes:** Unique `PACCT` (`BANK`,`ACCOUNT`); `PACCTCARD` (`BANK`,`CARD_NBR`); `ACCT_IND_2` (`CARD_NBR`); `IND_ACCT_ACCOUNT` (`ACCOUNT`).

**Join keys:** Detail SP: `BANK`+`ACCOUNT`+`CURR_NUM`. List SP: `CARD_NBR`+`CURR_NUM`.

QA currency split: DOP `214` ~3.3M rows; USD `840` ~0.99M.

---

### 5.3 `CADENCIE.PRMCN` — product catalog

**Purpose:** Product codes and descriptions for cards.  
**Est. rows:** ~89 · **cols:** 71

| Column | Type | Meaning |
|--------|------|---------|
| `PRODUCT` | `NUMBER(2)` | Product code (join from `CARD.PROFIL`) |
| `PROD_DESC` | `VARCHAR2(20)` | Description |
| `PROFIL` | `NUMBER(2)` | Profile (often equals `PRODUCT` for DOP; USD rows map back) |
| `PRODUCT_TY` | `VARCHAR2(1)` | Type (`0` personal / `1` corporate-ish) |
| `BANK` | `NUMBER(2)` | Bank |
| `CURR_NUM` | `NUMBER(3)` | Catalog currency (`214` or `840`) |
| `ACCT_STYLE` | `VARCHAR2(1)` | Account style |
| `MP_IND` | `VARCHAR2(1)` | Multipay / Credimás indicator |

**Indexes:** Unique `PPRMCNBNK` (`BANK`,`PRODUCT`); `PPRMCNCUR` (`BANK`,`CURR_NUM`,`PRODUCT`).

USD catalog rows (`PRODUCT` 71+) share `PROFIL` with DOP counterparts (e.g. `71` → profil `11`). MS product-code mapping usually keys DOP profils; skip USD-only keys unless needed.

---

### 5.4 `CADENCIE.CUSTR` — customer / document

**Purpose:** Customer master; document id lives in `CUSTR_NBR`, type in `DOCUM_TYPE`.  
**Est. rows:** ~5.1M · **cols:** 125

| Column | Type | Meaning |
|--------|------|---------|
| `BANK` | `NUMBER(2)` | Bank |
| `CUSTR_NBR` | `VARCHAR2(12)` | Id number (cédula / passport / RNC) |
| `DOCUM_TYPE` | `VARCHAR2(2)` | Doc class (`P1`…`E3`) → `TipoDocumento()` |
| `SURNAME` / `FORENAMES` | `VARCHAR2(30)` | Name (PII — column names only) |
| `DATE_BIRTH` | `VARCHAR2(7)` | Birth date string |
| `EMAIL_ADDR` | `VARCHAR2(40)` | Email (PII) |
| `NAME_KEY` | `VARCHAR2(20)` | Name search key |
| `CUSTR_REF` | `VARCHAR2(12)` | Reference |

**Indexes:** Unique `PCUSTR` (`BANK`,`CUSTR_NBR`); `IND_CUSTR_NBR` (`CUSTR_NBR`).

**`TipoDocumento(DOCUM_TYPE)` → numeric id type (APPSDBUC function):**

| Label | Numeric | `DOCUM_TYPE` values |
|-------|---------|---------------------|
| Cédula | `6` | `P1`,`P3`,`P4`,`P5`,`P6`,`T2` |
| Pasaporte | `4` | `P2`,`P7`,`P8` |
| RNC | `3` | `E1`,`E2`,`E3` |
| else | `5` | fallback |

---

### 5.5 `CADENCIE.STMT` — statement cycles

**Purpose:** Historical statement rows; payment due date for detail SP.  
**Est. rows:** ~73M · **cols:** 111

| Column | Type | Meaning |
|--------|------|---------|
| `BANK` / `ACCOUNT` | number | Account key |
| `MONTH_NBR` | `NUMBER(3)` | Cycle month code |
| `MIN_DUE_DT` | `VARCHAR2(7)` | Min due date string (`ddmonyy`) |
| `MIN_DUE` | `NUMBER(15,2)` | Min due amount |
| `OPEN_BAL` / `CLOSE_BAL` | `NUMBER(15,2)` | Open/close balance |
| `CRED_LIMIT` | `NUMBER(10)` | Limit at cycle |
| `CYCLE_NBR` / `PRODUCT` | number | Cycle / product |

**Indexes:** Unique `PSTMTACCT` (`BANK`,`ACCOUNT`,`MONTH_NBR`).

**EAI rule:** prefer `STMT.MONTH_NBR = ACCT.MONTH_NBR - 1`; else latest `STMT` with non-blank `MIN_DUE_DT`.

---

### 5.6 `CADENCIE.EVENT` — posted transactions

**Purpose:** Posted card events / movements (huge). Used by `LI_GET_CARD_TRANSACTIONS` and cashback/refund samplers.  
**Est. rows:** ~565M · **cols:** 175

| Column | Type | Meaning |
|--------|------|---------|
| `BANK` | `NUMBER(2)` | Bank |
| `CARD_NBR` | `VARCHAR2(19)` | PAN |
| `ACCTNBR` | `NUMBER(11)` | Account |
| `ISPEC` | `VARCHAR2(5)` | Spec (`TRAN`, `MPTR`, …) |
| `TRANS_TYPE` | `NUMBER(4)` | Transaction type / MS `TRN_TYPE` |
| `BILL_AMT` | `NUMBER(12,2)` | Billed amount (`>0` DEBIT, `<0` CREDIT) |
| `DES_LINE1` / `DES_LINE2` | varchar | Description lines |
| `INP_DATE` / `INP_TIME` / `TRANNO` | number | Input key parts |
| `AUTH_CODE` | `VARCHAR2(6)` | Auth code |
| `MERCHANT` | `NUMBER(10)` | Merchant id |
| `CURRNCY_CD` | `NUMBER(3)` | Currency |
| `MICRO_REF` | `VARCHAR2(23)` | Micro reference |

**Indexes:** `PEVENTCARD` (`CARD_NBR`,`INP_DATE`,`INP_TIME`,`TRANNO`); `PTRANINP` / `PMPTRINP` / `PMPTRACCT` (account + dates).

**Cashback codes (MS secret):** `TRANS_TYPE IN (8603,8604,8605,8616)`. Refund heuristic: `BILL_AMT < 0` and not cashback and `DES_LINE1` like `REFUND%` / `DEVOLUCION%`.

---

### 5.7 `CADENCIE.CLOCD` — close / status code catalog

**Purpose:** Descriptions for `CARD.CANCL_CODE`.  
**Est. rows:** 32 · **cols:** 28

| Column | Type | Meaning |
|--------|------|---------|
| `BANK` | `NUMBER(2)` | Bank |
| `CLOSE_CD` | `VARCHAR2(1)` | Status code (= `CANCL_CODE`) |
| `CLOSE_DESC` | `VARCHAR2(20)` | Description |
| `AUTH_RESP` | `VARCHAR2(2)` | Auth response mapping |
| `VALID_CLOS` / `BLO_TERMIN` | flags | Close validity / terminal block |

**Index:** Unique `PCLOCDBNK` (`BANK`,`CLOSE_CD`).

---

### 5.8 `CADENCIE.MPUR` / `CADENCIE.MSTM` — Credimás

| Table | Purpose | Key columns | Index |
|-------|---------|-------------|-------|
| **MPUR** | Multipurchase / Credimás plans (~9.6M) | `BANK`,`ACCOUNT`,`STATUS`,`PURCH_DAY`,`MIN_DUE`,`MTH_PPL`,`MTH_INT`,`TOT_INT_CG`,`NBR_MTHS`,`INSTL_CNT` | Unique `PMPURACCT` (`BANK`,`ACCOUNT`,`INP_DAY`,`MP_NUMBER`) |
| **MSTM** | Credimás monthly (~54M) | `BANK`,`ACCOUNT`,`MONTH_NBR`,`REM_PPL` | Unique `PMSTMACCT` (`BANK`,`ACCOUNT`,`MONTH_NBR`) |

Detail SP: latest active `MPUR` (`STATUS='A'`) by `PURCH_DAY`; `MSTM.REM_PPL` when `ACCT.BUSINESS=0`.

---

### 5.9 `CADENCIE.CODES` — generic code table

**Purpose:** Coded lists by `CODE_TYPE` (e.g. issue reasons).  
**PK-like:** Unique `PCODES` (`BANK`,`CODE_TYPE`,`CODE_VALUE`).

| Column | Type | Meaning |
|--------|------|---------|
| `CODE_TYPE` | `VARCHAR2(5)` | List id (`RCISS`, …) |
| `CODE_VALUE` | `VARCHAR2(4)` | Code |
| `SHORT_DEF` / `BRIEF` / `VALUE_DEF` | varchar | Labels |

**`RCISS` (issue reason → `CARD.ISSUE_REAS`):** `A` new, `X` renewal/vencimiento, `L` lost replace, `S` stolen replace, `F` fraud replace, …

---

### 5.10 `CADENCIE.AUTH` — authorizations (supporting)

Pending auth amounts also live on `ACCT.AUTHS_AMT`. `AUTH` holds authorization trail keyed by `CARD_NBR` (`PAUTHCARD`, `PAUTHCODE`). Use when tracing auth lifecycle; list/detail MS usually read `ACCT.AUTHS_AMT` only.

---

## 6. Status / product code fields

| Concern | Where | Notes |
|---------|-------|-------|
| Card status | `CARD.CANCL_CODE` | Space = active; join `CLOCD.CLOSE_CD` |
| Pending new status | `CARD.CANCL_NEW` | |
| Issue status | `CARD.ISSUE_STS` | QA mostly `9` |
| Issue reason | `CARD.ISSUE_REAS` | `CODES` `RCISS` |
| Emboss | `CARD.EMBOSS_CRD` | `1` embossed |
| Product code | `CARD.PROFIL` → `PRMCN.PRODUCT` | Description `PRMCN.PROD_DESC` |
| Product on account | `ACCT.PRODUCT` | Optional resolve filter |
| Quota / garantía | `ACCT.ACC_TYPE` | MS `QUOTA_TYPE` (`CG` garantía) |
| Canonical map (IAC) | `status-mapping.yaml` | ACTIVE=` `, BLOCKED=`6`, PENDING_ACTIVATION=`T`, … |
| Product map (IAC) | `product-code-mapping.yml` | Cross-core codes |

### Status catalog highlights (`CLOCD`, BANK=1)

| Code | Meaning (CLOSE_DESC) | IAC / MS note |
|------|----------------------|---------------|
| ` ` (space) | (active — blank code) | Canonical `ACTIVE` |
| `T` | `T -BLOQ. TEMP.-NUEVA` | `PENDING_ACTIVATION` / `PendienteActivacion` |
| `6` | `A - BLOQ. TEMP. APP` | Canonical `BLOCKED` |
| `R` / `Q` / `P` | cancel / auto-close | Cancelled family |
| `L` / `S` | lost / stolen | |
| `F` | fraud | |
| `H` | cuenta cerrada | |
| `U` | inactiva | |
| `O` | bloq. seguridad | |
| `C` | cobranzas | |
| `Y` | comprometida | |
| `Z` | fallecimiento | |

QA volume tip: space ~1.2M; `T` ~146k; cancelled/lost codes also large.

### Product samples (`PRMCN`, BANK=1, DOP)

| PRODUCT | PROD_DESC |
|---------|-----------|
| 1 | BANRESERVAS CLASICA |
| 11 | VISA CLASICA |
| 12 | VISA GOLD |
| 16 | VISA PLATINUM |
| 21 | MASTERCARD STANDARD |
| 24 | MASTERCARD PLATINUM |
| 32 | MASTERCARD BLACK |
| 35 | VISA INFINITE |

Full live dump: IAC research `…/configmap/_research/2026-07-23_cadencie_product_codes.json`.

### Quota (`ACC_TYPE`) top DOP values (QA)

`OF`, `Z`, `I`, `CN`, `TP`, `PS`, `EM`, `CG`, `IA`, `PR`, … — MS documents `Z` / `EM` / `CG` (garantía).

---

## 7. MS procedures (APPSDBUC) — anchors

| Object | Used by | Role |
|--------|---------|------|
| `GET_CUSTOMER_CARDS_PROC` | `ms-credit-cards-v2` | List / additional cards + `QUOTA_TYPE` |
| `LI_GET_CREDIT_CARD_DETAIL` | `ms-credit-cards-inquiries` | Card detail (pure SQL EAI formulas) |
| `LI_GET_CARD_TRANSACTIONS` | inquiries / v2 tx path | Posted movements |
| `LI_GET_CUSTOMER_CARDS` / `LI_GET_ADDITIONAL_CARDS` / `LI_GET_CARDS_EXPIRING` | inquiries | Related list helpers |
| `TipoDocumento` / `PendienteActivacion` | SQL baselines / EAI | Doc type / pending flag |
| `eai_fecha_cadencie` / `FromDefaultDate` / `GetAccountBalance` / `GetAccountInterest` | detail formulas | Date + balance helpers |
| `EAI_*` family | SOAP / legacy | Broader EAI surface (many VALID procs) |

---

## 8. Example query patterns (masked)

Binds only — never paste real PAN/PII into chat/vault.

### 8.1 Resolve card by document + masked PAN

```sql
-- :id_number, :id_type (Cedula|Pasaporte|RNC), :bin4, :last4, :product_code, :n
SELECT TRIM(c.card_nbr) card_nbr,
       TRIM(cu.custr_nbr) custr_nbr,
       TRIM(cu.docum_type) docum_type,
       TipoDocumento(cu.docum_type) tipo_doc_num,
       TRIM(c.profil) profil,
       TRIM(p.prod_desc) product_desc,
       DECODE(c.cancl_code,' ','<space>',c.cancl_code) cancl_code
FROM custr cu
JOIN card c ON c.bank = cu.bank AND c.custr_nbr = cu.custr_nbr
JOIN acct a ON a.bank = c.bank AND a.account = c.account AND a.curr_num = 214
LEFT JOIN prmcn p ON p.product = c.profil
WHERE cu.bank = 1
  AND TRIM(cu.custr_nbr) = :id_number
  AND (:id_type IS NULL OR TipoDocumento(cu.docum_type) =
       CASE UPPER(TRIM(:id_type)) WHEN 'CEDULA' THEN 6 WHEN 'PASAPORTE' THEN 4 WHEN 'RNC' THEN 3 END)
  AND SUBSTR(TRIM(c.card_nbr),1,4) = :bin4
  AND SUBSTR(TRIM(c.card_nbr),-4) = :last4
  AND (:product_code IS NULL
       OR LTRIM(TRIM(c.profil),'0') = LTRIM(TRIM(:product_code),'0'))
FETCH FIRST :n ROWS ONLY;
```

### 8.2 Customer cards (list spine = `GET_CUSTOMER_CARDS_PROC`)

```sql
SELECT C.CARD_NBR,
       C.CUSTR_NBR,
       DECODE(SUBSTR(C.CARD_NBR,-3,1),'1',0,1) is_additional,
       P.PRODUCT, P.PROD_DESC,
       NVL(A_DOP.CRED_LIMIT,0) limit_dop,
       NVL(A_USD.CRED_LIMIT,0) limit_usd,
       DECODE(C.CANCL_CODE,' ','<space>',C.CANCL_CODE) status,
       TRIM(A_DOP.ACC_TYPE) quota_type
FROM CADENCIE.CARD C
JOIN PRMCN P ON P.PRODUCT = C.PROFIL
LEFT JOIN ACCT A_DOP ON A_DOP.CARD_NBR = C.CARD_NBR AND A_DOP.CURR_NUM = 214
LEFT JOIN ACCT A_USD ON A_USD.CARD_NBR = C.CARD_NBR AND A_USD.CURR_NUM = 840
WHERE EXISTS (
  SELECT 1 FROM CADENCIE.CARD CP
  WHERE CP.ACCOUNT = C.ACCOUNT
    AND CP.CUSTR_NBR = :id_number
    AND DECODE(SUBSTR(CP.CARD_NBR,-3,1),'1',0,1) = 0
);
```

### 8.3 Detail join (DOP account via BANK/ACCOUNT)

```sql
SELECT C.CARD_NBR, C.CANCL_CODE, P.PRODUCT, P.PROD_DESC,
       A_DOP.CRED_LIMIT, A_DOP.STM_BALNCE, A_DOP.AUTHS_AMT,
       TRIM(A_DOP.ACC_TYPE) quota_type, A_DOP.MONTH_NBR
FROM CADENCIE.CARD C
JOIN PRMCN P ON P.PRODUCT = C.PROFIL
JOIN CARD W ON W.BANK = NVL(C.BANK,1) AND TRIM(W.CARD_NBR) = TRIM(C.CARD_NBR)
JOIN ACCT A_DOP ON A_DOP.BANK = W.BANK AND A_DOP.ACCOUNT = W.ACCOUNT AND A_DOP.CURR_NUM = 214
WHERE C.CARD_NBR = TRIM(:card_nbr);
```

### 8.4 Payment due date from STMT

```sql
SELECT S.MONTH_NBR, S.MIN_DUE_DT, S.MIN_DUE, S.CLOSE_BAL
FROM STMT S
WHERE S.BANK = :bank AND S.ACCOUNT = :account
  AND S.MONTH_NBR = :acct_month_nbr - 1;
-- fallback: ORDER BY MONTH_NBR DESC where LENGTH(TRIM(MIN_DUE_DT)) > 0 FETCH FIRST 1
```

### 8.5 Status description

```sql
SELECT C.CLOSE_CD, C.CLOSE_DESC
FROM CLOCD C
WHERE C.BANK = 1 AND C.CLOSE_CD = :cancl_code;
```

### 8.6 Pending activation + emboss filter

```sql
SELECT SUBSTR(TRIM(CARD_NBR),1,4)||'********'||SUBSTR(TRIM(CARD_NBR),-4) masked,
       TRIM(CUSTR_NBR) custr_nbr, CANCL_CODE, EMBOSS_CRD, ISSUE_REAS
FROM CARD
WHERE BANK = 1 AND TRIM(CANCL_CODE) = 'T' AND EMBOSS_CRD = '1'
FETCH FIRST :n ROWS ONLY;
```

### 8.7 Product inventory

```sql
SELECT PRODUCT, TRIM(PROD_DESC) prod_desc, PRODUCT_TY, PROFIL, CURR_NUM
FROM PRMCN WHERE BANK = 1 ORDER BY PRODUCT;
```

### 8.8 Cashback sample cards (no PAN dump — mask in SELECT)

```sql
SELECT SUBSTR(TRIM(E.CARD_NBR),1,4)||'********'||SUBSTR(TRIM(E.CARD_NBR),-4) masked,
       E.TRANS_TYPE, E.BILL_AMT, E.DES_LINE1
FROM EVENT E
WHERE E.ISPEC IN ('TRAN','MPTR')
  AND E.TRANS_TYPE IN (8603,8604,8605,8616)
FETCH FIRST :n ROWS ONLY;
```

### 8.9 Credimás active plan

```sql
SELECT M.ACCOUNT, M.STATUS, M.MIN_DUE, M.MTH_PPL, M.NBR_MTHS, M.INSTL_CNT
FROM MPUR M
WHERE M.ACCOUNT = :account AND M.STATUS = 'A'
ORDER BY M.PURCH_DAY DESC FETCH FIRST 1 ROW ONLY;
```

### 8.10 Issue reason label

```sql
SELECT CODE_VALUE, SHORT_DEF
FROM CODES
WHERE BANK = 1 AND TRIM(CODE_TYPE) = 'RCISS' AND TRIM(CODE_VALUE) = :issue_reas;
```

---

## 9. Safety / agent notes

- Read-only by default (`SELECT` / dictionary views).
- VPN required for `<HOST_PRIVATE_CADENCIE>`.
- Redact PAN and customer PII in all agent outputs.
- Prefer MS join patterns above over inventing alternate keys.
- Full DB has **412** Cadencie tables — stay on this MS-relevant set unless a ticket names another object.
)
