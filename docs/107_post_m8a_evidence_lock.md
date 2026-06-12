# EOD-2: Post-M8A Evidence Lock — Independent Bridge Investigation

**Gate:** EOD-2 Post-Independent-Investigation Lock  
**Date:** 2026-06-12  
**Status:** WAITING_FOR_TJB · INDEPENDENT_INVESTIGATION_COMPLETE

```
SAFETY LABELS (HARD — unchanged from EOD-1):
  NOT_VALIDATION · NOT_REFUTATION · NOT_AUTHOR_MODEL_FALSIFICATION
  INTERNAL_DIAGNOSTIC_ONLY · OUR_RECONSTRUCTION
  NO_EMAIL_BEFORE_2026-06-18 · NO_PUBLIC_CLAIMS · NO_MCMC
```

---

## 1. Previous State (EOD-1 / docs/106)

Email to TJB sent 2026-06-12 (commit 9513289, Q1+Q2+Q3).  
Follow-up not before 2026-06-18.  
Hard blockers: Q1 (bridge), Q2 (k_A(z)), Q3 (β phenomenological), Q_TH1–5, MCMC.

---

## 2. New Results Since EOD-1 (this session)

### M7-C2 — Mirror DM N_eff Constraint `[IF_MIRROR_DM_INTERPRETATION]`

**Commit:** `6c64253`  
**Script:** `scripts/mirror_dm_neff_constraint.py`  
**Tests:** 19 passed

| Parameter | Value | Status |
|---|---|---|
| IDM preprint line 1063–1065 | "one counterpart for each known SM particle per isomer" | AUTHOR_HINTED |
| Mirror DM structural match | IDM 5 isomers = 5 Mirror sectors | IF_MIRROR_DM_INTERPRETATION |
| ΔN_eff at T_dark=T_SM (interp A, minimal) | 22.0 (130σ above Planck) | [VERIFIED-tool] |
| ΔN_eff at T_dark=T_SM (interp C, full mirror) | 81.1 (477σ above Planck) | [VERIFIED-tool] |
| Required T_dark/T_SM for Planck compatibility | < 0.27–0.37 depending on interp | [VERIFIED-tool] |

**M7-C verdict: remains BLOCKED.**  
IDM preprint does not specify T_dark/T_SM → AUTHOR_DERIVATION_NEEDED.  
Mirror DM analysis gives external conditional benchmark only — not a resolution.

**Secondary finding:** Cool mirror sector (x < 0.35) cannot produce 5:1 dark/baryon mass ratio from equal baryon asymmetry → M7-A/B AUTHOR_DERIVATION_NEEDED status confirmed.

---

### M8-A — Bridge Derivation Attempt `[OUR_RECONSTRUCTION]`

**Commit:** `30473a2`  
**Script:** `scripts/bridge_derivation_attempt.py`  
**Tests:** 22 passed

#### ε(z) = (H_MULT/H_FLRW)² − 1 — extracted from Table A1

| z | H_FLRW | H_MULT | ε(z) |
|---|--------|--------|------|
| 0.06 | 68.1 | 70.2 | 0.0626 |
| 0.14 | 69.3 | 73.5 | 0.1249 |
| 0.25 | 71.5 | 78.8 | 0.2146 |
| **0.40** | **75.0** | **83.1** | **0.2277** ← global max |
| 0.65 | 83.0 | 91.4 | 0.2127 |
| 1.00 | 95.7 | 104.2 | 0.1855 ← local min |
| 1.50 | 114.8 | 126.5 | 0.2142 ← local rise |
| 2.10 | 140.3 | 151.8 | 0.1707 |
| 3.20 | 187.6 | 197.3 | 0.1061 |
| **5.00** | **265.2** | **271.5** | **0.0481** ← global min |
| 8.50 | 398.5 | 418.1 | 0.1008 ← uptick (single-point leverage) |

All arithmetic **independently verified** by adversarial re-audit agent.

#### Bridge Candidate Verdicts

| Candidate | Verdict | Evidence |
|---|---|---|
| Constant ε (H²_MULT = H²_FLRW × (1+C)) | **FAILS** | max_residual=0.104 is 2.1× heuristic threshold; robust |
| Power law ε ∝ (1+z)^α | **FAILS** | α varies −2.22 to +9.49 across z-pairs; sign changes confirm non-monotonicity |
| Friedmann + cluster density | **BLOCKED** | requires k_A(z) schedule from TJB (Q2) |

#### M8-A-R1 Adversarial Re-Audit (2026-06-12)

Re-audit independently verified all numerical claims. Corrections applied:

| Issue | Original | Correction | Severity |
|---|---|---|---|
| Docstring label | "VERIFIED from Table A1" | "[TRANSCRIBED from Table A1, arithmetic verified]" | MEDIUM |
| Claim 1 incompleteness | "peaks at 0.40, min at 5.0" | Added: secondary structure at z=1.0–1.5, uptick at z=8.5 is single-point leverage | LOW |
| Claim 4 (Press-Schechter) | "consistent with cluster peak" — implied causal | Marked `<HYPOTHESIS>` — numerical coincidence, no DAG, descriptive only | MEDIUM |
| Threshold 0.05 | Unmarked | Marked as heuristic; max_residual=0.104 is 2.1× threshold → verdict robust | LOW |

**Re-audit verdict: PARTIAL → PASS (after corrections applied)**

---

## 3. Sharpened Understanding of Q2 Blocker

Before EOD-1, Q2 = "what is the cluster schedule?"  
**After M8-A, Q2 is sharpened:**

```
Q2-REFINED:
  What k_A(z) and D_eff(z) schedule generates NON-MONOTONIC ε(z)
  with a primary peak near z≈0.40 (NOT a simple power law)?

  Any bridge formula candidate must:
  (a) Reproduce peak ε≈0.228 at z≈0.40
  (b) Reproduce global minimum ε≈0.048 at z≈5.0
  (c) NOT be representable as ε ∝ (1+z)^α for any single α
  (d) Include cluster-formation-epoch physics (when clusters form ↔ ε rises)
```

This sharpens — but does NOT replace — the Q2 question to TJB.

---

## 4. Evidence Registry (Updated)

### From EOD-1 (unchanged)

| Module | Verdict | Commit |
|---|---|---|
| M2-G4 β non-identifiability | PASS | 91ea667 |
| M7-A Eq31 mass-ratio | PARTIAL | 3b128dd |
| M7-B 5:1 dark isomer ratio | PARTIAL | e624bd3 |
| M7-C N_eff thermal history | BLOCKED | 9ebd05c |
| SC-6/F5 LG anomaly | FALSIFIED-LOCAL | 2026-06-12 |
| AB-2 author email | SENT | 9513289 |
| EOD-1 evidence lock | PASS | 397575c |

### New (this session)

| Module | Verdict | Commit |
|---|---|---|
| M7-C2 Mirror DM N_eff | IF_MIRROR_DM · BLOCKED | 6c64253 |
| M8-A bridge derivation attempt | ε(z) TRANSCRIBED · 3 candidates fail/blocked | 30473a2 |
| M8-A-R1 adversarial re-audit | PARTIAL→PASS (4 corrections applied) | this commit |

---

## 5. Next Allowed Actions (Priority Order)

| Priority | Action | Condition | Notes |
|---|---|---|---|
| 1 | Wait for TJB response | Now | Passive |
| 2 | M8-C — Closure schedule / cluster formation | Now | Does cluster mass function explain ε(z) shape? |
| 3 | M8-B — Φ-normalization bridge reconstruction | After M8-C | Forensic; lower priority than physical test |
| 4 | Polite follow-up if no TJB reply | ≥ 2026-06-18 | Same Q1–Q3 scope only |
| 5 | Add Q_TH1–5 to follow-up | After Q1–Q3 answered | Secondary priority |
| — | F1/F2 Table A1 reproduction | After Q1+Q2 answered | Bridge + schedule required |
| — | MCMC | After 5/5 blockers resolved | 0/5 currently |

---

## 6. Forbidden Actions (HARD)

```
NO second email before 2026-06-18
NO public claims about IDM validity
NO MCMC (0/5 blockers resolved)
NO "theory false/refuted/falsified" wording
NO "AI hallucinated / AI fabricated" wording (overclaim)
NO push unless explicitly approved
NO LLM API calls / web search
```

**Correct language:**  
> "Under our reconstruction from Table A1 data, [finding].  
> Author clarification (Q1/Q2/Q3) is needed before interpreting as a statement about IDM."

---

## 7. Gate Chain — Complete Record

| Gate | Status | Commit | Date |
|---|---|---|---|
| EC-1 Error Correction | PASS | a9eca5d | 2026-06-12 |
| VS-1 Vault Sync | PARTIAL | 85c7c1f | 2026-06-12 |
| AB-2 Author Email | PASS → SENT | 9513289 | 2026-06-12 |
| M7-C Thermal History | BLOCKED | 9ebd05c | 2026-06-12 |
| EOD-1 Evidence Lock | PASS | 397575c | 2026-06-12 |
| M7-C2 Mirror DM N_eff | IF_MIRROR · BLOCKED | 6c64253 | 2026-06-12 |
| M8-A Bridge Derivation | PARTIAL→CORRECTED | 30473a2 | 2026-06-12 |
| M8-A-R1 Adversarial Re-Audit | PASS (after 4 fixes) | this commit | 2026-06-12 |
| **EOD-2 Evidence Lock** | **PASS** | this file | 2026-06-12 |

---

*NOT_VALIDATION · NOT_REFUTATION · INTERNAL_DIAGNOSTIC_ONLY*  
*EOD-2 gate closed 2026-06-12 · Next session starts here*
