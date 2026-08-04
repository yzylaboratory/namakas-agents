> **Nakamas adaptation (2026-08-04).** Schema hub preserved; hosts sanitized to placeholders; no passwords. Live SQL expert: `kuzan-core-way4` under `iceburg-director-sistemas-core`. ≠ Crocus/Tom/Kaku; ≠ Tripulación `brd-*`.

# Way4 Oracle testing — schema map (credit cards)

**Core:** Way4 (OpenWay) — tarjetas de crédito Banreservas  
**Environment:** Oracle testing (`PQAOWPRIM`)  
**Explored:** 2026-07-27 (read-only, `oracledb` thin)  
**Primary MS:** `ms-credit-card-facility-query` (+ Way4 payment-method / production-status mappers)  
**Catalog size:** **950** tables + **627** views under owner `OWS` (do not dump all; below is MS-relevant subset)

Related baselines (project):  
`<BANRESERVAS_TC_PROJECT_ROOT>/…

---

## 1. Purpose

Way4 is the **credit-card issuing core** used by facility / payment-method inquiry flows: contracts (account + card), plastics (`CARD_INFO`), products (`APPL_PRODUCT` / soft product ids), contract status (`CONTR_STATUS`), client identification, custom statuses (e.g. `GARANTIA`), balances/dues, and documents (`DOC`).

Not the debit/PCI core (that is Cortex) and not Cadencie.

---

## 2. Connection summary (no password)

| Field | Value |
|-------|--------|
| Host | `<HOST_PRIVATE_WAY4>` |
| Port | `1521` |
| Service | `way4testing-prim.sndb.vcndev.oraclevcn.com` |
| User | `OWS_A` |
| DB name (session) | `PQAOWPRIM` |
| Preferred client | Python `oracledb` thin or `sqlplus` EZCONNECT |
| Credential source | IAC `…/overlays/{qa,des}/secret/card-nexus.env` keys `WAY4_USER` / `WAY4_PASSWORD` (also under `iac-dev-qa/.../card-nexus.env`). Resolve at runtime; **never** write password into skill/schema files. |
| Network | Private IP — **corporate VPN required**. Timeout → stop and report VPN. |

```bash
# After loading WAY4_USER / WAY4_PASS (never echo)
python3 -c "import oracledb,os; c=oracledb.connect(user=os.environ['WAY4_USER'],password=os.environ['WAY4_PASS'],dsn='<HOST_PRIVATE_WAY4>:1521/<WAY4_SERVICE>',tcp_connect_timeout=8); print(c.version); c.close()"
```

See also: [Iceburg connections](../../Iceburg-Director-Sistemas-Core/references/connections.md), [protocolo compartido](../../Iceburg-Director-Sistemas-Core/skills/consultar-cores-bancarios-sql/SKILL.md).

---

## 3. Key schemas / owners

| Owner | Role |
|-------|------|
| **OWS** | Application schema — contracts, cards, clients, products, docs, CS status (~950 tables, ~627 views). All facility SQL uses `OWS.*`. |
| **OWS_A** | Login user (session schema defaults to `OWS_A`; qualify objects as `OWS.`). |

FI row: `OWS.F_I` id `970` / Banreservas / country `DOM` / local currency `214` (DOP). USD accounts use `CURR=840`.

Amendment convention on most master tables: **`AMND_STATE = 'A'`** = current/active version.

---

## 4. Contract / card model (join spine)

```
CLIENT (party)
   └── ACNT_CONTRACT card   CON_CAT='C'   CLIENT__ID → CLIENT.ID
         │                    ACNT_CONTRACT__OID → parent account
         │                    PRODUCT = soft product (APPL_PRODUCT.INTERNAL_CODE)
         │                    CONTR_STATUS → CONTR_STATUS.ID
         │                    PRODUCTION_STATUS (plastic lifecycle letter)
         ├── CARD_INFO        ACNT_CONTRACT__OID → card.ID  (plastic / PAN)
         └── ACNT_CONTRACT parent  CON_CAT='A'   (cardAccountId in MS)
               └── ACNT_BALANCE    ACNT_CONTRACT__OID → account/card ID
```

| `CON_CAT` | Meaning | Active count (approx) |
|-----------|---------|------------------------|
| `A` | Account / issuing contract | ~44 460 |
| `C` | Card contract | ~39 380 |
| `M` | Device / other | ~33 |

**MS convention:** `cardAccountId` = parent account `ACNT_CONTRACT.ID` where `CON_CAT='A'`. Device/PAN from `CARD_INFO.CARD_NUMBER` (fallback `card.CONTRACT_NUMBER`). Mask as `BIN********LAST4` in outputs.

---

## 5. Important tables (MS-relevant)

### 5.1 `OWS.ACNT_CONTRACT` — contracts (account + card)

| Column | Type | Meaning |
|--------|------|---------|
| `ID` | NUMBER PK | Contract id |
| `AMND_STATE` | VARCHAR2 | `'A'` = current |
| `CON_CAT` | VARCHAR2 | `A` account / `C` card / `M` device |
| `CONTRACT_NUMBER` | VARCHAR2 | Contract / often PAN-like on cards |
| `CLIENT__ID` | NUMBER | → `CLIENT.ID` |
| `ACNT_CONTRACT__OID` | NUMBER | Parent contract (card → account) |
| `PRODUCT` | VARCHAR2 | **Soft product id** = `APPL_PRODUCT.INTERNAL_CODE` |
| `PARENT_PRODUCT` / `MAIN_PRODUCT` | VARCHAR2/NUMBER | Product hierarchy helpers |
| `CONTR_STATUS` | NUMBER | → `CONTR_STATUS.ID` |
| `PRODUCTION_STATUS` | VARCHAR2 | Plastic lifecycle: `R`/`L`/`S`/`C`/null |
| `CURR` | VARCHAR2 | ISO numeric currency (`214` DOP, `840` USD) |
| `AUTH_LIMIT_AMOUNT` / `AMOUNT_AVAILABLE` / balances | NUMBER | Limits & balances on contract |
| `DATE_OPEN` / `DATE_EXPIRE` / `CARD_EXPIRE` | DATE/VARCHAR2 | Lifecycle dates |
| `STATUS_CATEGORY` | VARCHAR2 | Status category flag |
| `EXT_DATA` / `ADD_INFO_*` | VARCHAR2 | Extensible blobs |

Join keys: `ID`, `CLIENT__ID`, `ACNT_CONTRACT__OID`, `PRODUCT`, `CONTR_STATUS`.

### 5.2 `OWS.CARD_INFO` — plastic / device

| Column | Type | Meaning |
|--------|------|---------|
| `ID` | NUMBER PK | Plastic row |
| `ACNT_CONTRACT__OID` | NUMBER | → card contract `ACNT_CONTRACT.ID` |
| `CARD_NUMBER` | VARCHAR2 | Device/PAN (**redact in outputs**) |
| `STATUS` | VARCHAR2 | `A` Active, `L` Locked, `I` InProduction, `C` Closed |
| `SEQV_NUMBER` | VARCHAR2 | Sequence; `>1` ≈ reissue |
| `PREV_CARD` / `PARENT_CARD` | NUMBER | Prior plastic; **`PARENT_CARD` unused (all NULL) on this DB** |
| `CARD_EXPIRE` / `PROD_DATE` / `DATE_FROM` | VARCHAR2/DATE | Expiry / production |
| `PRODUCTION_TYPE` / `PRODUCTION_EVENT` | VARCHAR2 | Production metadata |

**Production letter ↔ plastic (observed):**

| `ACNT_CONTRACT.PRODUCTION_STATUS` | `CARD_INFO.STATUS` | API-ish meaning |
|-----------------------------------|--------------------|-----------------|
| `R` | `A` | Ready / embossed active |
| `L` | `L` | Locked (embossed, pending activation) |
| `S` | `I` | In plant / InProduction |
| `C` | `A`/`C` | Closed / cancelled variants |

~13 045 card contracts have plastic `STATUS IN ('A','L')`; many cards have no plastic yet (`PRODUCTION_STATUS` null).

### 5.3 `OWS.CLIENT` — party / identification

| Column | Type | Meaning |
|--------|------|---------|
| `ID` | NUMBER PK | Client id |
| `AMND_STATE` | VARCHAR2 | `'A'` current |
| `CLIENT_NUMBER` | VARCHAR2 | Way4 client number |
| `REG_NUMBER` | VARCHAR2 | Document id (cédula/passport/RNC) — **PII** |
| `REG_NUMBER_TYPE` | VARCHAR2 | Dirty enum: `ID_CARD`, `CEDULA`, `NATIONAL_PASSPORT`, `RNC`, typos, nulls |
| `SHORT_NAME` / `FIRST_NAM` / `LAST_NAM` | VARCHAR2 | Names — **PII, do not dump** |
| `PHONE*` / `E_MAIL` | VARCHAR2 | Contact — **PII** |
| `DATE_OPEN` / `F_I` | DATE/NUMBER | Open date / FI |

Facility resolve: match `TRIM(REG_NUMBER)` (+ normalized type) and masked device BIN4/LAST4.

### 5.4 `OWS.APPL_PRODUCT` — products (+ soft product)

| Column | Type | Meaning |
|--------|------|---------|
| `ID` | NUMBER PK | Product row |
| `AMND_STATE` | VARCHAR2 | `'A'` active catalog row |
| `CODE` | VARCHAR2 | Business / MS product code (`11B`, `21`, `20`, …) |
| `INTERNAL_CODE` | VARCHAR2 | **Soft product** stored on `ACNT_CONTRACT.PRODUCT` |
| `NAME` | VARCHAR2 | Display name |
| `CON_CAT` | VARCHAR2 | Product applies to `A`/`C`/`M` |
| `PARENT_CODE` | VARCHAR2 | Parent soft product (`INTERNAL_CODE` of parent) |
| `PRODUCT_GROUP` | VARCHAR2 | `ISSCRED`, `ISSCRED_MC`, `ISSCRED_CORP`, acquirer groups |
| `PRODUCT_STATUS` / `IS_ACTIVE` | VARCHAR2 | Catalog flags |
| `MAX/MIN/DEFAULT_CREDIT_LIMIT` | NUMBER | Product limit defaults |
| `CUSTOM_DATA` | VARCHAR2 | Product custom blob |

**Soft product rule:**  
`card.PRODUCT = APPL_PRODUCT.INTERNAL_CODE` → business code via `APPL_PRODUCT.CODE`.

**Caveat:** ~22 k active card contracts point at soft ids whose **active** (`AMND_STATE='A'`) product row is missing (legacy/`I` rows still hold the `INTERNAL_CODE`). Prefer:

```sql
LEFT JOIN OWS.APPL_PRODUCT ap
  ON ap.INTERNAL_CODE = card.PRODUCT
 AND ap.AMND_STATE = 'A'
```

…and accept null `CODE` for orphans; or inspect inactive rows only when researching history.

Active catalog: **167** product rows (`AMND_STATE='A'`); **134** with `CON_CAT='C'`. Numeric-style codes (~`^[0-9]+B?$`): **61** distinct.

### 5.5 `OWS.CONTR_STATUS` — contract status catalog

| Column | Type | Meaning |
|--------|------|---------|
| `ID` | NUMBER PK | Referenced by `ACNT_CONTRACT.CONTR_STATUS` |
| `CODE` | VARCHAR2(8) | Short code (`00`, `54`, `14`, `41`, …) — **not unique alone** |
| `NAME` | VARCHAR2 | Label |
| `EXTERNAL_CODE` | VARCHAR2 | External / ISO-ish code (`L`, `S`, `F`, `M2`, …) |
| `CON_CAT` | VARCHAR2 | Separate rows for `A` vs `C` (same `CODE` can differ by category) |
| `IS_VALID` | VARCHAR2 | `V` valid / `D` decline-ish / `I` inactive-closed family (observed) |
| `AMND_STATE` | VARCHAR2 | `'A'` current |

High-volume statuses (active contracts): `54` “to close”, `00` OK — both account and card variants.

Always join `cs.ID = ac.CONTR_STATUS` (and filter `cs.CON_CAT` if needed). Do **not** join only on `CODE`.

### 5.6 Custom status (guarantee, soft block)

| Table | Role |
|-------|------|
| `CS_STATUS_TYPE` | Type catalog (`CODE='GARANTIA'` id `10110`; `SOFT_BLOCK` id `1640`) |
| `CS_STATUS_VALUE` | Values (`GARANTIA`: `PERS`/`CERT`/`EXT`/`SIN`) |
| `CS_STATUS_LOG` | Active assignments (`IS_ACTIVE='Y'`); guarantee is **client-scoped** (`CLIENT__OID` set, `ACNT_CONTRACT__OID` null here) |

Helper package: **`OWS.DECR.GET_CS_VALUE(contract_id, client_id, 'GARANTIA')`** (and many `EFF_STATUS_*` / `SET_CS_*` APIs — read-only use `GET_*` / `EFF_*`).

MS `hasGuarantee`: custom_data / CS value present and ≠ `SIN`.

### 5.7 `OWS.ACNT_BALANCE` — balances / dues

Key columns: `ACNT_CONTRACT__OID`, `BALANCE_TYPE_CODE`, `CURR`, `AVAILABLE`, `BALANCE`, `BLOCKED`, `CREDIT_LIMIT`.  
Useful codes for facility: `CRDT_LINE`, `TOTAL_BALANCE`, `DUE`, `TOTAL_DUE`, `PAST_DUE`, `BLOCKED`, `STMT_BALANCE`, …

### 5.8 `OWS.DOC` + `OWS.TRANS_TYPE` — transactions / refunds

| Join | Notes |
|------|-------|
| `DOC.TRANS_TYPE` → `TRANS_TYPE.ID` | |
| **Way4 REST native refund** | Spec `2026-06-26` Payment Methods TX: **`transaction_type.transaction_group = REFUND`** (`TransactionGroupName`). Filter `transaction_groups=REFUND`. Not stored as a simple DOC column on this DB (`OWS.TRANS_GROUP` empty). |
| `TRANS_TYPE.TRANS_TYPE_IDT` | **`0616`** = `K1`/`Credit` (ISO credit); **`CASHB`** = promo name. These are **not** native REST refund. Former MS invent-map IDT→REFUND **retired** (2026-07-27). Orch `cashback=true` only when MS category REFUND ← Way4 **group**. Exclude `0512` POS Retail with CashBack |
| `DOC.TARGET_CONTRACT` / `SOURCE_CONTRACT` | → `ACNT_CONTRACT` |
| `DOC.POSTING_STATUS` / `RETURN_CODE` | Prefer posted `P` + `RETURN_CODE=0` for samples |

### 5.9 Other useful objects

| Object | Purpose |
|--------|---------|
| `OWS.F_I` | Financial institution (Banreservas) |
| `OWS.ACNT_CONTRACT` balances columns | Quick limits without `ACNT_BALANCE` |
| `OWS.DECR` package | CS / status helpers (`GET_CS_VALUE`, …) |

---

## 6. Status / product fields — where they live

| Concern | Location |
|---------|----------|
| Business product code (`11B`, `21`, …) | `APPL_PRODUCT.CODE` via soft id |
| Soft product id | `ACNT_CONTRACT.PRODUCT` = `APPL_PRODUCT.INTERNAL_CODE` |
| Product group | `APPL_PRODUCT.PRODUCT_GROUP` |
| Contract OK / block / cancel | `ACNT_CONTRACT.CONTR_STATUS` → `CONTR_STATUS` |
| Plastic lifecycle | `ACNT_CONTRACT.PRODUCTION_STATUS` + `CARD_INFO.STATUS` |
| Guarantee | `CS_STATUS_*` type `GARANTIA` on client (or `DECR.GET_CS_VALUE`) |
| Party id for resolve | `CLIENT.REG_NUMBER` + `REG_NUMBER_TYPE` |
| Currency | `ACNT_CONTRACT.CURR` (`214`/`840`) |

---

## 7. Reusable query patterns (no PII/PAN dumps)

Bind `:n` with `FETCH FIRST :n ROWS ONLY`. Mask devices in app layer.

### Q1 — Active card + account + product + status

```sql
SELECT parent.ID AS ACCOUNT_CONTRACT_ID,
       card.ID AS CARD_CONTRACT_ID,
       ap.CODE AS PRODUCT_CODE,
       card.PRODUCT AS SOFT_PRODUCT,
       cs.CODE AS CONTR_STATUS_CODE,
       cs.NAME AS CONTR_STATUS_NAME,
       card.PRODUCTION_STATUS,
       card.CURR
FROM OWS.ACNT_CONTRACT card
JOIN OWS.ACNT_CONTRACT parent
  ON parent.ID = card.ACNT_CONTRACT__OID
 AND parent.AMND_STATE = 'A' AND parent.CON_CAT = 'A'
LEFT JOIN OWS.APPL_PRODUCT ap
  ON ap.INTERNAL_CODE = card.PRODUCT AND ap.AMND_STATE = 'A'
LEFT JOIN OWS.CONTR_STATUS cs
  ON cs.ID = card.CONTR_STATUS AND cs.AMND_STATE = 'A'
WHERE card.AMND_STATE = 'A' AND card.CON_CAT = 'C'
FETCH FIRST :n ROWS ONLY
```

### Q2 — Product catalog (card soft products)

```sql
SELECT CODE, NAME, INTERNAL_CODE, PRODUCT_GROUP, PARENT_CODE, CON_CAT
FROM OWS.APPL_PRODUCT
WHERE AMND_STATE = 'A' AND CON_CAT = 'C'
ORDER BY CODE
```

### Q3 — Contract status catalog

```sql
SELECT ID, CODE, NAME, EXTERNAL_CODE, CON_CAT, IS_VALID
FROM OWS.CONTR_STATUS
WHERE AMND_STATE = 'A'
ORDER BY CON_CAT, CODE
```

### Q4 — Embossed plastics (Ready / Locked)

```sql
SELECT parent.ID AS ACCOUNT_CONTRACT_ID,
       card.ID AS CARD_CONTRACT_ID,
       card.PRODUCTION_STATUS,
       ci.STATUS AS PLASTIC_STATUS,
       ci.SEQV_NUMBER
FROM OWS.ACNT_CONTRACT card
JOIN OWS.ACNT_CONTRACT parent
  ON parent.ID = card.ACNT_CONTRACT__OID
 AND parent.AMND_STATE = 'A' AND parent.CON_CAT = 'A'
JOIN OWS.CARD_INFO ci
  ON ci.ACNT_CONTRACT__OID = card.ID
 AND ci.STATUS IN ('A', 'L')
WHERE card.AMND_STATE = 'A' AND card.CON_CAT = 'C'
  AND card.PRODUCTION_STATUS IN ('R', 'L')
FETCH FIRST :n ROWS ONLY
-- Do not SELECT CARD_NUMBER in agent transcripts; mask if needed.
```

### Q5 — Clients with guarantee (`GARANTIA` ≠ `SIN`)

```sql
SELECT cli.ID AS CLIENT_ID,
       v.CODE AS GARANTIA,
       parent.ID AS ACCOUNT_CONTRACT_ID,
       card.ID AS CARD_CONTRACT_ID
FROM OWS.CS_STATUS_LOG l
JOIN OWS.CS_STATUS_VALUE v ON v.ID = l.STATUS_VALUE
JOIN OWS.CLIENT cli ON cli.ID = l.CLIENT__OID AND cli.AMND_STATE = 'A'
JOIN OWS.ACNT_CONTRACT card
  ON card.CLIENT__ID = cli.ID AND card.AMND_STATE = 'A' AND card.CON_CAT = 'C'
JOIN OWS.ACNT_CONTRACT parent
  ON parent.ID = card.ACNT_CONTRACT__OID AND parent.AMND_STATE = 'A' AND parent.CON_CAT = 'A'
WHERE l.STATUS_TYPE = (
        SELECT ID FROM OWS.CS_STATUS_TYPE
        WHERE CODE = 'GARANTIA' AND AMND_STATE = 'A' AND ROWNUM = 1
      )
  AND l.IS_ACTIVE = 'Y'
  AND v.CODE <> 'SIN'
FETCH FIRST :n ROWS ONLY
```

### Q6 — Resolve by document + masked device (+ optional product)

```sql
SELECT parent.ID AS ACCOUNT_CONTRACT_ID,
       card.ID AS CARD_CONTRACT_ID,
       ap.CODE AS PRODUCT_CODE,
       card.PRODUCTION_STATUS,
       ci.STATUS AS PLASTIC_STATUS
FROM OWS.CLIENT cli
JOIN OWS.ACNT_CONTRACT card
  ON card.CLIENT__ID = cli.ID AND card.AMND_STATE = 'A' AND card.CON_CAT = 'C'
JOIN OWS.ACNT_CONTRACT parent
  ON parent.ID = card.ACNT_CONTRACT__OID AND parent.AMND_STATE = 'A' AND parent.CON_CAT = 'A'
LEFT JOIN OWS.CARD_INFO ci ON ci.ACNT_CONTRACT__OID = card.ID
LEFT JOIN OWS.APPL_PRODUCT ap
  ON ap.AMND_STATE = 'A' AND ap.INTERNAL_CODE = card.PRODUCT
WHERE cli.AMND_STATE = 'A'
  AND TRIM(cli.REG_NUMBER) = :id_number
  AND SUBSTR(NVL(ci.CARD_NUMBER, card.CONTRACT_NUMBER), 1, 4) = :bin4
  AND SUBSTR(NVL(ci.CARD_NUMBER, card.CONTRACT_NUMBER), -4) = :last4
  AND (:product_code IS NULL OR UPPER(TRIM(ap.CODE)) = UPPER(TRIM(:product_code)))
FETCH FIRST :n ROWS ONLY
```

### Q7 — Principal + additional under same account

```sql
SELECT parent.ID AS ACCOUNT_CONTRACT_ID,
       COUNT(DISTINCT card.CLIENT__ID) AS CLIENT_COUNT,
       COUNT(*) AS CARD_COUNT
FROM OWS.ACNT_CONTRACT parent
JOIN OWS.ACNT_CONTRACT card
  ON card.ACNT_CONTRACT__OID = parent.ID
 AND card.AMND_STATE = 'A' AND card.CON_CAT = 'C'
WHERE parent.AMND_STATE = 'A' AND parent.CON_CAT = 'A'
GROUP BY parent.ID
HAVING COUNT(DISTINCT card.CLIENT__ID) >= 2
FETCH FIRST :n ROWS ONLY
```

### Q8 — Credit line / due balances for an account

```sql
SELECT b.BALANCE_TYPE_CODE, b.CURR, b.AVAILABLE, b.BALANCE, b.CREDIT_LIMIT, b.BLOCKED
FROM OWS.ACNT_BALANCE b
WHERE b.ACNT_CONTRACT__OID = :account_contract_id
  AND b.BALANCE_TYPE_CODE IN ('CRDT_LINE', 'TOTAL_BALANCE', 'DUE', 'TOTAL_DUE', 'PAST_DUE', 'BLOCKED')
```

### Q9 — Cards with Credit/promo IDT docs (`0616`, `CASHB`) — not native REST REFUND

```sql
-- ISO Credit / promo IDT fixtures. Native REST refund = transaction_group=REFUND (API only).
SELECT DISTINCT parent.ID AS ACCOUNT_CONTRACT_ID, card.ID AS CARD_CONTRACT_ID,
       t.TRANS_TYPE_IDT
FROM OWS.DOC d
JOIN OWS.TRANS_TYPE t
  ON t.ID = d.TRANS_TYPE
 AND t.AMND_STATE = 'A'
 AND t.TRANS_TYPE_IDT IN ('0616', 'CASHB')
JOIN OWS.ACNT_CONTRACT tgt ON tgt.ID = d.TARGET_CONTRACT AND tgt.AMND_STATE = 'A'
JOIN OWS.ACNT_CONTRACT card ON (
       (tgt.CON_CAT = 'C' AND card.ID = tgt.ID)
    OR (tgt.CON_CAT = 'A' AND card.ACNT_CONTRACT__OID = tgt.ID AND card.CON_CAT = 'C')
     )
 AND card.AMND_STATE = 'A'
JOIN OWS.ACNT_CONTRACT parent
  ON parent.ID = NVL(CASE WHEN tgt.CON_CAT = 'A' THEN tgt.ID END, card.ACNT_CONTRACT__OID)
 AND parent.CON_CAT = 'A' AND parent.AMND_STATE = 'A'
WHERE d.AMND_STATE = 'A'
  AND d.POSTING_STATUS = 'P'
  AND NVL(d.RETURN_CODE, 0) = 0
FETCH FIRST :n ROWS ONLY
```

### Q10 — In-production / renewal plastics

```sql
-- In plant only
SELECT card.ID, card.PRODUCTION_STATUS, ci.STATUS
FROM OWS.ACNT_CONTRACT card
JOIN OWS.CARD_INFO ci ON ci.ACNT_CONTRACT__OID = card.ID AND ci.STATUS = 'I'
WHERE card.AMND_STATE = 'A' AND card.CON_CAT = 'C' AND card.PRODUCTION_STATUS = 'S'
FETCH FIRST :n ROWS ONLY;

-- hasRenewal: same card contract has both Active and InProduction plastics
SELECT card.ID
FROM OWS.ACNT_CONTRACT card
JOIN OWS.CARD_INFO a ON a.ACNT_CONTRACT__OID = card.ID AND a.STATUS = 'A'
JOIN OWS.CARD_INFO i ON i.ACNT_CONTRACT__OID = card.ID AND i.STATUS = 'I'
WHERE card.AMND_STATE = 'A' AND card.CON_CAT = 'C'
FETCH FIRST :n ROWS ONLY
```

---

## 8. Agent guardrails

- Read-only by default (`SELECT` / dictionary views).
- Never print or persist passwords; never commit secrets.
- Never dump full PAN lists, names, docs, phones, emails into vault/skill files — mask devices.
- On connect timeout to `<HOST_PRIVATE_WAY4>`: report VPN and stop.
- Prefer `OWS.` qualification; filter `AMND_STATE='A'` on versioned masters.
- Soft product join may miss legacy codes — treat null `APPL_PRODUCT.CODE` as expected for orphan soft ids.
- Full sampling SQL library: facility-query baselines under `db/patches/baselines/2026-07-21_way4_*`.

---

## 9. Snapshot counts (2026-07-27)

| Metric | Count |
|--------|------:|
| `OWS` tables | **950** |
| `OWS` views | 627 |
| Active contracts (`AMND_STATE='A'`) | 83 873 |
| Accounts `CON_CAT='A'` | 44 460 |
| Cards `CON_CAT='C'` | 39 380 |
| Active clients | 11 222 |
| `CARD_INFO` rows | 14 431 |
| Active `APPL_PRODUCT` | 167 |
| Active `CONTR_STATUS` | 40 |
