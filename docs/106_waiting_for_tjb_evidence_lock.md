# EOD-1: Waiting-State Evidence Lock

**Gate:** EOD-1 Consolidated Evidence Lock  
**Date:** 2026-06-12  
**Status:** WAITING_FOR_TJB · EMAIL_SENT · EVIDENCE_LOCKED

```
SAFETY LABELS (HARD):
  NOT_VALIDATION · NOT_REFUTATION · NOT_AUTHOR_MODEL_FALSIFICATION
  INTERNAL_DIAGNOSTIC_ONLY · OUR_RECONSTRUCTION
  NO_EMAIL_BEFORE_2026-06-18 · NO_PUBLIC_CLAIMS · NO_MCMC
```

---

## 1. Email Status

| Parameter | Value |
|---|---|
| Document sent | `docs/104_author_q1_q3_send_ready_candidate.md` |
| Approved by user | 2026-06-12 |
| Commit | `9513289` |
| Recipient | Dr. Thomas J. Buckholtz |
| Subject | *Reproducibility follow-up: three clarification questions on Table A1* |
| Content | Q1 (bridge), Q2 (cluster schedule), Q3 (β provenance) — 664 words |
| Follow-up not before | **2026-06-18** |
| Second email rule | BLOCKED until 2026-06-18; then polite follow-up only if no reply |

---

## 2. Hard Blockers — Active

| ID | Blocker | Unlock condition |
|---|---|---|
| **Q1** | Bridge formula F_oP → H_MULT(z) absent from preprint | TJB answer to Q1 |
| **Q2** | D_C:AB(z) cluster variable schedule unknown | TJB answer to Q2 |
| **Q3** | β_d, β_q not derived from first principles (TJB confirmed: phenomenological) | TJB answer to Q3 |
| **Q_TH1** | Were five dark isomers thermally populated in early universe? | Follow-up email after Q1–Q3 |
| **Q_TH2** | T_dark/T_visible for each dark sector? | Follow-up email |
| **Q_TH3** | Decoupling temperature from SM bath? | Follow-up email |
| **Q_TH4** | Which dark particles relativistic at BBN / recombination? | Follow-up email |
| **Q_TH5** | IDM ΔN_eff prediction vs Planck 2018 bound? | Follow-up email |
| **MCMC** | 0/5 blockers resolved; all five depend on Q1+Q2 | Q1 + Q2 both answered |

**Priority:** Q1 > Q2 > Q3 >> Q_TH1–5. Thermal questions are secondary; do not send before bridge is resolved.

---

## 3. Verified Evidence Registry

All results below are `[VERIFIED-tool]` under `OUR_RECONSTRUCTION`.  
Evidence scope: our CSV cluster parameters + preprint formulas. NOT author-confirmed.

### M2-G4 — β Non-Identifiability `[PASS]`

| Finding | Value | Status |
|---|---|---|
| Fisher rank of [β_d, β_q] | rank 1 (not 2) | `[VERIFIED-tool]` |
| β pair identifiability | NON-IDENTIFIABLE | `[VERIFIED-tool]` |
| Practical implication | H(z) fit constrained by β_d × β_q product, not individual values | — |
| Commit | `91ea667` | — |

### M7-A — Eq.31 Mass-Ratio `[PARTIAL]`

| Finding | Value | Status |
|---|---|---|
| IDM integer count | 5.0 dark isomers : 1 ordinary | `AUTHOR_HINT` |
| Planck ρ_DM/ρ_OM | 5.364 ± 0.065 | `EXTERNAL_VERIFIED` |
| Gap | −6.8%, pull −5.6σ from Planck central | `[VERIFIED-tool]` |
| Mechanism | Not derived — post-hoc integer counting | `AUTHOR_DERIVATION_NEEDED` |
| Commit | `3b128dd` | — |

### M7-B — 5:1 Dark Isomer Ratio `[PARTIAL]`

| Finding | Value | Status |
|---|---|---|
| Sec 4.5 "pluses" | 4 qualitative options, not derived mass fractions | `NOT_AUTHOR_CONFIRMED` |
| Neutron-mass correction | +0.08% max — cannot close 7% gap | `[VERIFIED-tool]` |
| Thermal history | Absent from preprint | `NOT_FOUND` |
| Commit | `e624bd3` | — |

### M7-C — N_eff / BBN Blocker `[BLOCKED]`

| Ingredient | Status |
|---|---|
| I1: relativistic dark species at BBN | NOT_FOUND |
| I2: T_dark / T_visible | NOT_FOUND |
| I3: decoupling temperature | NOT_FOUND |
| I4: entropy-transfer history | NOT_FOUND |
| I5: dark particle existence | AUTHOR_HINTED (preprint line 1063–1065) |
| I6: coupling/thermalization | NOT_FOUND |
| I7: explicit ΔN_eff | NOT_FOUND |
| ΔN_eff computable from IDM | **NO — BLOCKED** |
| Planck 2018 bound applicable | NO — no IDM input to compare against |
| Commit | `9ebd05c` | — |

### SC-6 / F5 — Local Group Anomaly `[FALSIFIED-LOCAL]`

**Absolute forces at D = 0.785 Mpc (MW–M31) `[VERIFIED-tool 2026-06-12]`:**

| Force | Value (N) | Ratio ε = F/F_m |
|---|---|---|
| **F_m** (monopole gravity) | **6.75×10²⁹** | 1.000 |
| **F_d** (dipole, β_d=4.5) | **2.03×10²³** | **ε_d = 3.01×10⁻⁷** |
| **F_q** (quadrupole, β_q=18.0) | **2.72×10¹⁶** | ε_q = 4.03×10⁻¹⁴ |

**Structural findings:**

```
β_d needed for ε_d = 1 (dipole dominance):  1.495×10⁷
Current β_d = 4.5  →  need ×3,320,000 more

Cross-check:
  β_d = 4.5      → ε_d(LG) = 3×10⁻⁷ | ε_d(cluster, z=0) = 1.1×10⁻³
  β_d = 14.95M   → ε_d(LG) = 1.0     | ε_d(cluster) ≈ 3500 → destroys Table A1

No single β_d satisfies both conditions simultaneously.
```

**Input parameters (OUR_RECONSTRUCTION):**
m_MW = 1.0×10¹² M☉ · m_M31 = 1.5×10¹² M☉ · σ_v = 150 km/s · D = 0.785 Mpc  
k_A convention: k_A/c² = ½·m·(σ_v/c)²

**Status:** `[FALSIFIED-LOCAL — OUR_RECONSTRUCTION]`  
**Scope qualifier:** Author k_A(z) schedule for galaxy-scale UNKNOWN. Q15 for TJB remains open.  
**v_radial observed:** −109 km/s (approach) — consistent with gravity dominating at β_d=4.5.

---

## 4. Overall Diagnostic Summary

| Module | Verdict | Blocker |
|---|---|---|
| K0 reproducibility setup | PASS | — |
| M2-G4 identifiability | PASS | — |
| M7-A Eq31 mass-ratio | PARTIAL | AUTHOR_DERIVATION_NEEDED |
| M7-B 5:1 ratio | PARTIAL | AUTHOR_DERIVATION_NEEDED |
| M7-C N_eff thermal | BLOCKED | 6/7 ingredients NOT_FOUND |
| SC-2 bridge gap | FALSIFIED-LOCAL | Q1+Q2 unlock |
| SC-4 dipole dominance | FALSIFIED-LOCAL | Q2 unlock |
| SC-6/F5 LG anomaly | FALSIFIED-LOCAL | independent of bridge |
| MCMC estimation | BLOCKED | 0/5 blockers resolved |
| AB-2 author email | **SENT** | — |

---

## 5. Overclaim Guard

| Forbidden statement | Why forbidden |
|---|---|
| "MULTING is false / wrong / broken" | We tested OUR_RECONSTRUCTION, not author's |
| "IDM predicts X" (for anything unspecified) | Author has not confirmed bridge, schedule, or thermal history |
| "ΔN_eff constraint rules out IDM" | No IDM ΔN_eff exists to compare |
| "5:1 ratio is a coincidence" | Mechanism absent ≠ mechanism wrong |
| "SC-6 proves dipole never dominates" | Only proved at β_d=4.5 and our LG params |
| "email was rejected / accepted" | No response received yet |

**Correct language:**  
> "Under our reconstruction, [finding]. Author clarification (Q1/Q2/Q3) is needed before this can be interpreted as a statement about IDM."

---

## 6. Next Allowed Actions

| Action | Allowed from | Notes |
|---|---|---|
| Wait for TJB response | Now | Passive |
| Polite follow-up email if no reply | **2026-06-18** | One follow-up only; same Q1–Q3 scope |
| M7-D (optional low-priority gate) | Now | Only if explicitly chosen; independent of TJB |
| Update docs/100 with TJB answers | After TJB reply | Do not extrapolate before reply |
| F1/F2 (Table A1 reproduction) | After Q1+Q2 answered | Requires bridge + schedule |
| F3 BIC vs ΛCDM | After F1 | Requires F1 |
| Add Q_TH1–5 to follow-up | After Q1–Q3 answered satisfactorily | Secondary priority |

---

## 7. Forbidden Actions

```
NO second email before 2026-06-18
NO public claims about IDM validity
NO MCMC (0/5 blockers resolved)
NO "theory false" wording
NO new physics tests started without explicit user choice
NO modifications to docs/104 email content retroactively
NO LLM API calls / web search unless local sources exhausted
```

---

## 8. Gate Chain — Complete Record

| Gate | Status | Commit | Date |
|---|---|---|---|
| EC-1 Error Correction | PASS | a9eca5d | 2026-06-12 |
| VS-1 Vault Sync | PARTIAL | 85c7c1f | 2026-06-12 |
| AB-1 Author Brief Draft | PARTIAL | 8277cf0 | 2026-06-12 |
| AB-2 Send-Readiness | PASS → SENT | 9513289 | 2026-06-12 |
| M7-C Thermal History | BLOCKED | 9ebd05c | 2026-06-12 |
| EOD-1 Evidence Lock | **PASS** | this file | 2026-06-12 |

---

*NOT_VALIDATION · NOT_REFUTATION · INTERNAL_DIAGNOSTIC_ONLY*  
*EOD-1 gate closed 2026-06-12 · Next session starts here*
