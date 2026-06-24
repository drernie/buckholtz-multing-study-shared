# Claim Proofs — Reproducibility Ledger

**Purpose:** every numerical atom has a one-command proof from published constants.
A critic challenges a number → you run the command → the arithmetic is on screen.
No trust in prior labels: the script recomputes from PDG 2024 / CODATA 2018 / Planck 2018.

**Master command (all atoms at once):**
```bash
python scripts/verify_all_claims.py        # prints proof per atom, writes reports/verify_all_claims.json, exit 0
```

**Verdict legend:**
- `CONFIRMED` — computed value matches the claim within stated tolerance.
- `CORRECTED` — claim as previously stated was optimistic; honest value here.
- `BLOCKED` — not computable from the preprint (missing inputs); not a single number.

---

## Ledger

| ID | Claim (corrected) | Computed | Verdict | Evidence | Proof command |
|----|-------------------|----------|---------|----------|---------------|
| **C9** | (4/3)(m_τ/m_e)¹² = α_EM/α_G at **0.17σ** | LHS/RHS = 1.00013516 (0.0135%) | ✅ CONFIRMED | `[VERIFIED-BASH]` | `python scripts/verify_all_claims.py` → [C9] |
| **C9b** | n=12 is the **unique** hit (not range-fitted) | 1 of 120 combinations within 1% → only (4/3, 12, τ/e) | ✅ CONFIRMED | `[VERIFIED-BASH]` | `python scripts/verify_all_claims.py` → [C9b] |
| **C4** | N_opt = 5.366, **5.67σ** from integer 5 (delta-method) | N_opt=5.36613, σ_N=0.06456 | ✅ CONFIRMED | `[VERIFIED-BASH]` | `python scripts/verify_all_claims.py` → [C4] |
| **C6** | 7:9:17 holds to ~0.2% by value, but **W = 3.6σ**, H = 1.1σ, Z = anchor | W²=6.993, Z²=9.000, H²=16.966 (units (m_Z/3)²) | ⚠️ CORRECTED | `[VERIFIED-BASH]` | `python scripts/verify_all_claims.py` → [C6] |
| **C5** | ΔN_eff is **BLOCKED** — not computable from preprint; "0.70" is one assumed scenario | naive SM = 22–81 (130–477σ); 0.70 needs g_*S>210 | 🔴 BLOCKED | `[CONFLICTING]` | `python scripts/m7_c_thermal_history_neff_audit.py` + `mirror_dm_neff_constraint.py` |

---

## Corrections logged (vs the working atom table)

These two atoms were stated more favorably than the arithmetic supports. The ledger
reports the honest value so a critic cannot use it against the strong atoms.

### C6 — "✅ 0.4σ" → per-boson σ varies (anchor bias)
- 7:9:17 are ratios of **squared** masses in units `(m_Z/3)²`, not direct mass ratios.
- Anchoring Z makes Z trivially 0σ; the remaining fit is carried by W and H.
- **W = 3.58σ**, H = 1.14σ (PDG m_W=80.377±0.012, matching paper). The headline "0.4σ" was the best single boson (H).
- **Honest statement:** "7:9:17 holds to ~0.2% in value; the W boson deviates ~3.6σ in PDG mass units."

### C5 — "ΔN_eff=0.70" → BLOCKED (three conflicting scenarios)
- `m7_c_thermal_history_neff_audit.py`: **BLOCKED** — 6 of 7 thermal inputs (T_dark, g_D, T_dark/T_ν) absent from the preprint.
- `mirror_dm_neff_constraint.py`: naive SM thermal history (T_dark=T_SM) → ΔN_eff = **22 / 37 / 81** (130–477σ above Planck).
- "0.70" is only reachable assuming MSSM-scale entropy dilution (g_*S>210); even then > the ~0.29–0.40 allowed.
- **Honest statement:** "ΔN_eff is not computable from the preprint; under naive SM it is catastrophic (130–477σ); '0.70' is one assumption-laden scenario, not a derived value."

---

## Atoms confirmed by dedicated scripts (already in repo)

| Atom | Proof command | Result |
|------|---------------|--------|
| ε(z) non-monotone, peak z=0.40 | `python scripts/run_table_a1_recomputation.py` | CONFIRMED (Table A1 diagnostic) |
| β non-identifiable (Fisher rank 1) | `python scripts/m2_g4_fisher_rank_identifiability.py` | CONFIRMED (commit 91ea667) |
| f×σ8 r=0.851 robustness | `python scripts/fsig8_robustness.py` | MODEL-CONFIRMED w/ σ8-tension caveat |
| Koide is lepton-specific (quarks fail) | `python scripts/idm_masses.py` | CONFIRMED (quarks 13–170σ from 2/3) |
| AIC/BIC ΔAIC=−16.65 (IN-SAMPLE only) | `python scripts/aic_model_comparison.py` | CONFIRMED in-sample; out-of-sample BLOCKED |

---

## Rule for critics (and for us)

> A claim is "provable" only if a command reproduces its number from published constants.
> If the number needs an assumption not in the preprint, the verdict is **BLOCKED**, not a value.
> Anchor-dependent fits (like C6) must report the **worst** residual, not the best boson.

*Constants source: PDG 2024 (masses, α_EM), CODATA 2018 (G, ħ, c, m_e), Planck 2018 base-ΛCDM (ω_b, ω_cdm).*
