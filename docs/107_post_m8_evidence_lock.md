# docs/107 — Post-M8 Evidence Lock (EOD-2)

**Date:** 2026-06-12  
**Gate:** EOD-2 — freeze-point after M7-C2, M8-A, M8-A-R1, M8-C  
**Replaces:** docs/106 (previous evidence lock, pre-M8 gates)  
**Status:** WAITING_FOR_TJB

```
SAFETY LABELS (HARD):
  NOT_VALIDATION · NOT_REFUTATION · NOT_AUTHOR_MODEL_FALSIFICATION
  INTERNAL_DIAGNOSTIC_ONLY · OUR_RECONSTRUCTION
  NO_EMAIL_BEFORE_2026-06-18 · NO_PUBLIC_CLAIMS · NO_MCMC
  NOT_THEORY_FALSE · NOT_AI_HALLUCINATION_CLAIM
```

---

## 1. Current State

**Project status:** WAITING_FOR_TJB  
**Email sent:** 2026-06-12, commit 9513289 — Q1 (bridge method), Q2 (k_A(z) schedule), Q3 (β provenance)  
**Follow-up:** not before 2026-06-18  
**MCMC:** BLOCKED (0/5 blockers resolved)  
**Tests:** 661 passed / 12 skipped / 0 failed [VERIFIED-tool 2026-06-12]  
**Branch:** feature/appendix-a1-doc-updates

---

## 2. New Commits Since docs/106

| Commit | Description | Verdict |
|---|---|---|
| `6c64253` | M7-C2: Mirror DM conditional N_eff benchmark | IF_MIRROR · BLOCKED |
| `30473a2` | M8-A: Bridge derivation attempt — ε(z) non-monotonic | CONFIRMED (post-reaudit) |
| `add7cba` | M8-A-R1: Adversarial re-audit — 4 corrections applied | PASS |
| `d1638d4` | M8-C: Closure Schedule — Press-Schechter cluster bridge | PARTIAL |
| `9513289` | AB-2: Author email Q1–Q3 sent to TJB | SENT |
| `c79cb3a` | docs/108: EOD-3 three-layer claim status matrix | PASS |

---

## 3. Confirmed Results

### 3a. Mirror DM Conditional Benchmark (M7-C2, commit 6c64253)

**Scope:** OUR_RECONSTRUCTION · CONDITIONAL_BENCHMARK · IF_MIRROR_DM_INTERPRETATION

- IF IDM ≈ mirror-sector dark matter (5 isomers, each with SM counterpart):
  - At equal temperature (T_dark/T_SM = 1): ΔN_eff ≈ 22–81 depending on relativistic species count
  - Planck 2018 bound: ΔN_eff < 0.28 (2σ)
  - This is 130–477σ excess — excluded if mirror sectors are in thermal equilibrium with SM
- Required constraint: T_dark/T_SM < ~0.27–0.37 for Planck compatibility
- **What this does NOT mean:** IDM is ruled out. The conditional applies only if IDM = fully thermalized mirror sectors. Author has not confirmed this interpretation.
- **M7-C status unchanged:** BLOCKED — IDM does not specify T_dark/T_SM, decoupling epoch, or thermal history. Author derivation needed.

### 3b. ε(z) Non-Monotonic Structure (M8-A + M8-A-R1, commits 30473a2, add7cba)

**Scope:** TABLE_LEVEL_DIAGNOSTIC · OUR_RECONSTRUCTION  
**Labels:** [TRANSCRIBED from Table A1, arithmetic verified]

ε(z) = (H_MULT/H_FLRW)² − 1:

| z | ε(z) | Sign of Δε |
|---|---|---|
| 0.06 | 0.0626 | — |
| 0.14 | 0.1249 | ↑ |
| 0.25 | 0.2146 | ↑ |
| **0.40** | **0.2277** | **↑ GLOBAL PEAK** |
| 0.65 | 0.2127 | ↓ |
| 1.00 | 0.1855 | ↓ LOCAL MIN |
| 1.50 | 0.2142 | ↑ SECONDARY STRUCTURE |
| 2.10 | 0.1707 | ↓ |
| 3.20 | 0.1061 | ↓ |
| **5.00** | **0.0481** | **↓ GLOBAL MIN** |
| 8.50 | 0.1008 | ↑ SINGLE-POINT (leverage) |

**Structure:** RISE → PEAK(z=0.40) → FALL → LOCAL_MIN(z=1.00) → SECONDARY_RISE(z=1.50) → FALL → GLOBAL_MIN(z=5.00) → UPTICK(z=8.50, single-point leverage)

**Confirmed failures (arithmetic verified, M8-A-R1 PASS):**
- Constant-ε bridge: max residual 0.104 (2.1× heuristic threshold 0.05) — **FAILS**
- Power-law bridge: α spans [−2.22, +9.49] with 3 sign changes — **FAILS**

**What this does NOT mean:** H_MULT values are outputs of an AI service reconstructed from the preprint, not independently measured observational data. "TRANSCRIBED" = data copied correctly from Table A1, arithmetic verified. NOT "physically proven" or "author-confirmed computation."

### 3c. M8-C Press-Schechter Closure Schedule (commit d1638d4)

**Scope:** OUR_RECONSTRUCTION · EXTERNAL_STANDARD_PHYSICS  
**Hypothesis label:** HYPOTHESIS — not confirmed

ΛCDM parameters: Ω_m=0.315, Ω_Λ=0.685, H_0=70 km/s/Mpc, σ_8=0.811, δ_c=1.686, γ=0.27  
M_8 = 2.678×10¹⁴ M_sun [VERIFIED-tool, 10% tolerance test passes]

Results by model and M_min:

| M_min | Model A (PS comoving) peak_z | Model A r | Model B (dN/dz) peak_z | Model B r |
|---|---|---|---|---|
| 1×10¹⁴ M_sun | 0.06 (monotone) | −0.048 | **0.65** | **0.723** |
| 5×10¹⁴ M_sun | 0.06 (monotone) | −0.264 | **0.40** | 0.541 |
| 2×10¹⁵ M_sun | 0.06 (monotone) | −0.413 | 0.25 | 0.183 |

**Overall verdict: PARTIAL**  
Best Pearson r = 0.723 (Model B, M_min=1e14)

**What PARTIAL means:**
- Model B (survey count rate dN/dz) peaks at z=0.65 for M_min=1e14 and at z=0.40 for M_min=5e14 — qualitative overlap with ε primary peak range
- Model A (PS comoving density) is always monotonically decreasing — categorically cannot explain ε peak at z=0.40
- Secondary structure at z=1.0–1.5 is NOT reproduced by any PS model tested
- Uptick at z=8.50 is NOT reproduced

**What PARTIAL does NOT mean:**
- Does NOT confirm that MULTING physics is connected to cluster formation
- Does NOT identify the author's actual bridge or cluster schedule
- Does NOT constitute validation of MULTING
- The PS connection remains HYPOTHESIS status only

---

## 4. Main Blocker

**Q2: k_A(z) / D_eff(z) / cluster schedule** — the unknown function mapping cluster forces to H_MULT(z).

This blocker was **sharpened** by M8-C: any proposed bridge must reproduce the non-monotonic ε(z) shape with primary peak near z≈0.40 and secondary structure at z=1.0–1.5 — not any single power law, and not a monotonically decreasing function.

Blockers still open (0/5 resolved):

| Blocker | Status |
|---|---|
| Q1: Bridge method F_oP → H_MULT(z) | MISSING |
| Q2: k_A(z) / D_eff(z) / cluster schedule | MISSING |
| Q3: β parameter provenance (physical or fitted) | OPEN (TJB partial: "fitted, may or may not be fundamental") |
| Independent data (Pantheon+ / BAO integration) | MISSING |
| Complexity penalty (AIC/BIC for bridge) | MISSING |

---

## 5. Overclaim Guard

The following language is FORBIDDEN in any internal or external communication:

| Forbidden claim | Reason |
|---|---|
| "MULTING is false / refuted / falsified" | We tested OUR reconstruction, not author's intended bridge |
| "AI hallucinated Table A1" | Risk of AI-mediated bridge is established; hallucination is overclaim |
| "SC-2 gap proves the theory is wrong" | Gap ×4365 = our reconstruction fails, not author theory fails |
| "Press-Schechter confirms the bridge" | r=0.723 is PARTIAL at best; secondary structure unexplained |
| "ε(z) is physically derived" | It is TRANSCRIBED from AI-service Table A1 output, not observational |
| "We have the bridge" | No author-confirmed bridge exists |
| "Mirror DM audit refutes IDM" | Conditional benchmark only; author IDM ≠ confirmed mirror sectors |

**Canonical language (safe):**
> "We found reproducibility blockers and failures under our reconstruction of the MULTING bridge from publicly available materials. The author's intended bridge method is not confirmed from the preprint alone."

---

## 6. Next Allowed Gates

| Gate | Priority | Prerequisites |
|---|---|---|
| TJB follow-up email | HIGH | Wait until 2026-06-18; same Q1–Q3 scope only |
| M8-C-R1 lightweight re-audit | MEDIUM | Context-blind falsification of M8-C claims (like M8-A-R1) |
| M8-B Φ-normalization forensic | LOW | Forensic analysis of AI-mediated Phi(z) bridge (no new physics) |

**Blocked until Q1+Q2 resolved:**
- MCMC
- Full BBN/CMB/Bullet Cluster audit
- Any public claims about MULTING validity

---

## 7. Forbidden Actions (Hard)

- NO public claim about MULTING validity or invalidity
- NO MCMC (0/5 blockers resolved)
- NO "theory false" language
- NO "AI hallucinated Table A1" language
- NO second email before 2026-06-18
- NO new physics additions without author confirmation

---

## 8. Evidence Block Summary

```
EVIDENCE BLOCK — EOD-2 (2026-06-12)

CONFIRMED [VERIFIED-tool or TRANSCRIBED]:
  [1] No explicit bridge F_oP → H_MULT(z) found in public materials (BLOCKER Q1)
  [2] ε(z) = (H_MULT/H_FLRW)² − 1 is non-monotonic (11 values verified, M8-A-R1 PASS)
      Peak: ε=0.2277 at z=0.40 | Min: ε=0.0481 at z=5.00
      Secondary structure: local min at z=1.00, rise at z=1.50
  [3] Constant-ε bridge FAILS (max residual 0.104 >> 0.05)
  [4] Power-law bridge FAILS (α sign changes at z=0.40, 1.00, 5.00)
  [5] M8-C: Model A (PS comoving) cannot explain ε peak — monotone by construction
  [6] M8-C: Model B (dN/dz) peaks at z=0.40–0.65 for appropriate M_min (PARTIAL)
  [7] Mirror DM: IF IDM≈mirror sectors at equal temp → ΔN_eff=22–81 >> Planck bound
  [8] β_d, β_q = phenomenological fitting coefficients (TJB confirmed partial)
  [9] Author email Q1–Q3 sent 2026-06-12, reply expected not before 2026-06-18

HYPOTHESIS [not confirmed]:
  [H1] ε(z) shape is partly explained by cluster formation history (PS dN/dz)
       Best evidence: peak location overlap, r=0.723. Insufficient for confirmation.
  [H2] IDM requires cold dark sector IF mirror interpretation is correct (T<0.37 T_SM)

OPEN [requires TJB]:
  [O1] Author's actual bridge formula (Q1)
  [O2] k_A(z) / D_eff(z) cluster schedule (Q2)
  [O3] Physical vs fitted status of β (Q3)

REJECTED CLAIMS [do not repeat]:
  - "MULTING refuted" / "theory false"
  - "AI hallucinated" (overclaim)
  - "SC-2 gap refutes author theory"
  - "PS bridge confirmed"
```

---

## 9. Verdict

```
EOD-2 VERDICT: PASS

Rationale:
  - All committed gates completed with honest verdicts (PARTIAL, BLOCKED, PASS)
  - No overclaims found in committed files
  - ε(z) arithmetic independently verified (M8-A-R1 PASS, 4 corrections applied)
  - M8-C PARTIAL correctly recorded (not inflated to PASS)
  - Safety labels present in all reports
  - Author email sent within authorized scope (Q1–Q3 only)
  - Claim status matrix (docs/108) correctly separates CONFIRMED/OPEN/REJECTED

Evidence quality: sufficient for a freeze-point.
MCMC readiness: 0/5 blockers — remains BLOCKED.
Public claim readiness: NO — awaiting TJB response.
```

---

## 10. Files Changed (since docs/106)

| File | Change | Commit |
|---|---|---|
| scripts/m7c2_mirror_dm_neff.py | NEW — mirror DM N_eff benchmark | 6c64253 |
| tests/test_m7c2_mirror_dm_neff.py | NEW — 19 tests | 6c64253 |
| reports/m7c2_mirror_dm_neff.json | NEW — gate report | 6c64253 |
| scripts/bridge_derivation_attempt.py | NEW — ε(z) analysis + bridge candidates | 30473a2 |
| tests/test_bridge_derivation_attempt.py | NEW — 22 tests | 30473a2 |
| reports/bridge_derivation_attempt.json | NEW | 30473a2 |
| reports/m8_a_r1_bridge_derivation_reaudit.md | NEW — adversarial re-audit | add7cba |
| scripts/bridge_derivation_attempt.py | MODIFIED — 4 corrections applied | add7cba |
| tests/test_bridge_derivation_attempt.py | MODIFIED — updated for corrections | add7cba |
| docs/107_post_m8a_evidence_lock.md | RENAMED/REPLACED by this file | — |
| scripts/m8c_closure_schedule.py | NEW — PS cluster bridge test | d1638d4 |
| tests/test_m8c_closure_schedule.py | NEW — 32 tests | d1638d4 |
| reports/m8c_closure_schedule.json | NEW — gate report | d1638d4 |
| .claude/memory/activeContext.md | UPDATED | d1638d4 |
| docs/108_claim_status_matrix.md | NEW — EOD-3 three-layer matrix | c79cb3a |

---

## 11. Next State

```
NEXT_STATE: WAITING_FOR_TJB

  Active gates:          NONE (all completed or blocked)
  Next trigger:          TJB reply to Q1–Q3 email (2026-06-12)
  Earliest follow-up:    2026-06-18 (one polite nudge, same Q scope)
  Optional work:         M8-C-R1 adversarial re-audit
                         M8-B Φ-normalization forensic (low priority)
  Hard blockers remain:  Q1 bridge + Q2 k_A(z) → MCMC still 0/5

  Session freeze: this file is the authoritative state snapshot.
  Next session starts with: docs/107 + docs/108 + activeContext.md
```

---

*NOT_VALIDATION · NOT_REFUTATION · INTERNAL_DIAGNOSTIC_ONLY*  
*EOD-2 gate closed 2026-06-12 · Committed as docs/107_post_m8_evidence_lock.md*
