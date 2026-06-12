# docs/113 — Post-HD-MAVP-1 Selection Artifact Lock

**Date:** 2026-06-13  
**Gate:** HD-MAVP-1 completion freeze-point  
**Supersedes (this topic):** M8-C PARTIAL interpretation  
**Status:** WAITING_FOR_TJB — all authorized gates complete

```
SAFETY LABELS (HARD):
  NOT_VALIDATION · NOT_REFUTATION · NOT_AUTHOR_MODEL_FALSIFICATION
  INTERNAL_DIAGNOSTIC_ONLY · OUR_RECONSTRUCTION
  NO_EMAIL_BEFORE_2026-06-18 · NO_PUBLIC_CLAIMS · NO_MCMC
  NOT_THEORY_FALSE · NOT_AI_HALLUCINATION_CLAIM · NOT_FABRICATION_CLAIM
  HD_MAVP_1 · SELECTION_BIAS_AUDIT · NOT_CLAIM_PS_FACT
```

---

## 1. Why This Lock Exists

HD-MAVP-1 (commit `80c44a0`) produced a finding that **materially changes the interpretation
of M8-C** (Claim C14, survey dN/dz → r=0.723). This document freezes that finding before
any further work is attempted.

**Core finding:** The SZ survey selection function alone — with zero cluster physics — produces
`r(ε, f_sel) = 0.666`, which is 92% of the M8-C best signal and explains ~85% of its variance.

This does not kill M8-C. It creates a **two-way ambiguity** that Q2 can resolve.

---

## 2. Key Numbers (VERIFIED-tool, commit 80c44a0)

| Metric | Value | Source |
|--------|-------|--------|
| M8-C best signal (intrinsic dN/dz, M_min=5e14) | r = **0.723** | M8-C, commit d1638d4 |
| f_sel alone — zero physics SZ instrument model | r = **0.666** | HD-MAVP-1, 80c44a0 |
| Correlation ratio (f_sel / M8-C) | **92%** | 0.666 / 0.723 |
| Variance ratio (f_sel / M8-C) | **85%** | 0.666² / 0.723² = 0.444 / 0.523 |
| Candidate B (intrinsic dN/dz, M_min=1e14) | r = **0.773** | HD-MAVP-1, 80c44a0 |
| Candidate B (intrinsic dN/dz, M_min=5e14) | r = **0.699** | HD-MAVP-1, 80c44a0 |
| Candidate B (intrinsic dN/dz, M_min=2e15) | r = **0.560** | HD-MAVP-1, 80c44a0 |
| Candidate A (PS density, no volume, M_min=5e14) | r = **−0.100** | HD-MAVP-1, 80c44a0 |
| Candidate D (ΛCDM dark energy fraction f_DE) | r = **0.167** | HD-MAVP-1, 80c44a0 |
| z_eq (Λ-matter equality) | **0.296** | (Ω_Λ/Ω_m)^(1/3) − 1 |

---

## 3. Verdict Map — Four Candidates

| Candidate | Physical meaning | r range | Verdict |
|-----------|-----------------|---------|---------|
| A: PS density n(>M,z) | Intrinsic formation, no geometry | −0.25 to +0.08 | **KILLED** |
| B: Intrinsic dN/dz | PS × comoving volume element | 0.560–0.773 | **PARTIAL** (M_min-sensitive) |
| C: SZ-selection-weighted | B × parametric f_sel | 0.607–0.683 | **PARTIAL** |
| **f_sel alone** | **Zero physics, instrument only** | **0.666** | **SURVIVES_AS_ARTIFACT** |
| D: ΛCDM f_DE | Dark energy fraction (monotone) | 0.167 | **KILLED** |

**Overall verdict: PARTIAL-KILL**
- Intrinsic cluster formation history: **KILLED**
- Observed-count / selection / schedule artifact: **SURVIVES**

---

## 4. Revised Interpretation of M8-C

**Before HD-MAVP-1:**
> M8-C r=0.723 was classified PARTIAL — survey dN/dz overlaps ε peak qualitatively.
> Secondary ε structure (z=1.0–1.5 uptick, z=8.5 uptick) unexplained. [docs/112]

**After HD-MAVP-1 (this lock):**
> The ε(z) peak at z≈0.40 **does not confirm a physical epoch of cluster formation**.
> It is consistent with three alternative explanations:
>
> 1. **Observed count / selection artifact** — SZ surveys detect clusters preferentially
>    at z≈0.40 by instrument physics (beam dilution + flux limits). The correlation
>    r=0.666 from f_sel alone demonstrates this artifact is sufficient to explain ~85%
>    of M8-C variance.
>
> 2. **Intrinsic dN/dz at correct M_min** — Volume-weighted PS counts peak near z=0.40
>    for M_min≈5e14 M_sun. r=0.699 at this scale without any selection function applied.
>    This would represent a physical signal — but M_min is undetermined without Q2.
>
> 3. **Bridge functional-form artifact** — Any function peaking at z=0.40 can be fitted
>    from 11 data points; the peak itself does not constrain the underlying physics.
>
> **Q2 (author cluster schedule) is now the decisive discriminator.**
> Without k_A(z)/D_eff(z), these three cannot be separated.

**What this does NOT mean:**
```
✗ M8-C r=0.723 is spurious or wrong
✗ The ε peak at z=0.40 is explained by selection artifacts
✗ Cluster formation is unrelated to ε
✗ MULTING theory is false or refuted
✗ The selection bias explanation is confirmed
✗ Any M_min value is the "correct" one
```

---

## 5. New INSIGHTs (from HD-MAVP-1)

| ID | Insight | Confidence | Gate |
|----|---------|------------|------|
| INSIGHT-5a | r(ε, f_sel_alone)=0.666 — instrument artifact (no physics) explains 85% of M8-C variance | `[VERIFIED-tool]` | HD-MAVP-1 NR-005 |
| INSIGHT-5b | Candidate B r is M_min-sensitive (0.560–0.773) — not a fixed physics prediction | `[VERIFIED-tool]` | HD-MAVP-1 |
| INSIGHT-5c | ΛCDM z_eq=0.296 is proximate (Δz=0.104) but f_DE is monotone — cannot explain ε peak | `[THEOREM]` | HD-MAVP-1 |

---

## 6. Updated Gate Chain (complete)

| Gate | Verdict | Commit | Key finding |
|------|---------|--------|-------------|
| M2-G4 β identifiability | PASS | `91ea667` | β non-identifiable; sensitivity ~1e-7 |
| M8-A Bridge Derivation | CONFIRMED | `30473a2` | No explicit bridge in public materials |
| M8-A-R1 Adversarial Re-Audit | PASS | `add7cba` | 11 ε values verified; peak z=0.40 |
| M8-C Closure Schedule / dN/dz | PARTIAL | `d1638d4` | r=0.723; secondary structure unexplained |
| M8-D MAVS Virial+PS | FAIL | `9100b0a` | k_A monotone by theorem; r negative |
| ASRE required-schedule | PARTIAL | `507ead9` | required_bridge extracted; 3 degenerate families |
| BETA-0 β provenance | PASS | `37f2d04` | β spread 5.8×/95×; DO_NOT_USE |
| MASTER LOCK | PASS | `c133de3` | All prior gates consolidated |
| **HD-MAVP-1 cluster audit** | **PARTIAL-KILL** | **`80c44a0`** | **f_sel alone r=0.666; intrinsic KILLED; selection SURVIVES** |
| **POST-HD-MAVP LOCK (this)** | **PASS** | — | Freeze-point after HD-MAVP-1 |

---

## 7. Updated Evidence Block (complete as of 2026-06-13)

```
EVIDENCE BLOCK — POST-HD-MAVP-1 (2026-06-13)

CONFIRMED [VERIFIED-tool or VERIFIED]:
  [1]  No explicit bridge F_oP → H_MULT(z) in public materials (BLOCKER Q1)
  [2]  ε(z) non-monotone; peak 0.2277 at z=0.40; min 0.0481 at z=5.00 [M8-A-R1]
  [3]  Constant-ε and power-law bridges FAIL [NR-001/002]
  [4]  PS comoving density monotone; cannot peak at z=0.40 [NR-003, M8-C, HD-MAVP-1]
  [5]  dN/dz survey rate: r=0.723, peak z=0.40–0.65 [M8-C PARTIAL]
  [6]  MAVS k_A(z) ∝ H^(4/3) — monotone by theorem — FAIL [M8-D, INSIGHT-3]
  [7]  All MAVS components anti-correlated with ε; best r = −0.2573 [M8-D]
  [8]  required_bridge = ε×H² uniquely extracted; two targets [ASRE]
  [9]  3 degenerate (k_A, D_eff) families; virial excluded [ASRE]
  [10] β_d spread 5.8×, β_q spread 95× across 3 AI services [BETA-0]
  [11] M2-G4: β non-identifiable under OUR_RECONSTRUCTION (Fisher rank 1)
  [12] TJB Q3 partial: β are "phenomenological computation… remains to be determined"
  [13] Q2 sharpened: valid schedule must be non-virial AND non-monotone [M8-D]
  ─── NEW (HD-MAVP-1) ─────────────────────────────────────────────
  [14] r(ε, f_sel_alone) = 0.666 — SZ selection function (zero physics) produces
       85% of M8-C variance; selection artifact hypothesis SURVIVES [NR-005]
  [15] Intrinsic PS density n(>M,z) KILLED — r=−0.10 to +0.08 (all M_min) [NR-005]
  [16] Candidate B (dN/dz, M_min=1e14) r=0.773 — M_min-sensitive; not robust [HD-MAVP-1]
  [17] ΛCDM f_DE monotone (r=0.167); z_eq=0.296 proximate but wrong shape [HD-MAVP-1]

HYPOTHESIS [not confirmed]:
  [H1] ε(z) shape connected to cluster formation rate (ambiguous: selection vs intrinsic)
  [H2] Φ-normalization carries the non-monotone structure (M8-B forensic pending)
  [H3] Selection artifact alone explains M8-C r=0.723 (NOT confirmed — Q2 needed)

OPEN [requires TJB]:
  [O1] Actual bridge formula (Q1)
  [O2] k_A(z) / D_eff(z) — non-virial, non-monotone schedule (Q2) ← NOW MORE CRITICAL
  [O3] β canonical values + derivation method (Q3)

REJECTED [do not repeat]:
  — "MULTING refuted" / "theory false" / "AI hallucinated"
  — "β fabricated" / "β are constants of nature"
  — "virial theorem disproves MULTING"
  — "ε peak at z=0.40 is a confirmed selection artifact"
  — "M8-C r=0.723 is spurious"
```

---

## 8. Active Gates and Hold Status

```
ACTIVE GATES: NONE

HOLD (requires explicit approval):
  HD-MAVP-2:  HOLD — would require author bridge/schedule; another reconstruction layer
  M8-B:       LOW PRIORITY — Φ-normalization forensic; requires explicit approval
  BETA-1:     HOLD — controlled AI β replication; requires explicit approval

NEXT AUTHORIZED ACTIONS:
  IF TJB replies to Q1+Q2:
    → Unlock ASRE individual k_A / D_eff split
    → Unlock M8-B if relevant
    → Unlock MCMC design
    → Resolve intrinsic-vs-selection ambiguity (Candidate B vs f_sel)

  IF TJB replies to Q3:
    → Update β status; potentially unlock modeling

  IF no reply by ~2026-07-12:
    → Consider archiving as AUTHOR_DECLINED_DETAIL

  Earliest follow-up email: 2026-06-18 (same Q1–Q3 scope only)
```

---

## 9. The Most Accurate Statement Now

```
The ε(z) peak at z≈0.40 does not confirm a physical epoch of cluster formation.

It is consistent with:
  (1) Observed-count / selection artifact: SZ instrument model (zero physics)
      reproduces r=0.666, explaining ~85% of M8-C variance.
  (2) Intrinsic volume-weighted dN/dz at correct M_min (r=0.560–0.773 depending on M_min).
  (3) Bridge functional-form artifact: any peaked function fits 11 points.

These cannot be distinguished without the author's cluster schedule (Q2).
Q2 is therefore the single most decisive piece of missing information.

Do NOT claim the peak is a selection artifact.
Do NOT claim the peak is physical cluster formation.
Correct: "The peak is ambiguous; Q2 is decisive."
```

---

## 10. Verdict

```
POST-HD-MAVP-1 LOCK VERDICT: PASS

Rationale:
  - HD-MAVP-1 findings correctly consolidated
  - r numbers match verified report (commit 80c44a0, 41/41 tests)
  - M8-C interpretation updated (not killed, made more specific)
  - Two-way ambiguity documented; Q2 as decisive discriminator
  - No overclaiming (selection not confirmed, M8-C not killed)
  - No new physics, no new models, no new AI calls
  - Safety language enforced throughout

Modeling readiness:   BLOCKED (0/5 MCMC blockers resolved)
Public claim readiness: NO
HD-MAVP-2:            HOLD (no further gates authorized)
```

---

## 11. Files Changed

| File | Change |
|------|--------|
| `docs/113_post_hd_mavp_selection_artifact_lock.md` | NEW — this document |

*No scripts, tests, or reports created — this is a consolidation lock only.*

---

## 12. Next State

```
NEXT_STATE: WAITING_FOR_TJB (unchanged)

  Phase:              FROZEN — all authorized gates complete
  Active gates:       NONE
  Email sent:         2026-06-12 (Q1, Q2, Q3)
  Earliest follow-up: 2026-06-18
  HD-MAVP-2:          HOLD
  M8-B:               LOW PRIORITY (requires explicit approval)
  BETA-1:             HOLD (requires explicit approval)

SESSION START PROTOCOL (next session):
  1. Read docs/112 (MASTER LOCK) — prior gates, MCMC blockers, β status
  2. Read docs/113 (this file) — HD-MAVP-1 findings, selection artifact lock
  3. Check email for TJB reply — if received, unlock path from Section 8 above
  4. Do NOT start new gates without explicit approval

STOP — awaiting TJB
```

---

*NOT_VALIDATION · NOT_REFUTATION · INTERNAL_DIAGNOSTIC_ONLY*  
*NOT_THEORY_FALSE · NOT_AI_HALLUCINATION_CLAIM · NOT_FABRICATION_CLAIM*  
*HD_MAVP_1 · SELECTION_BIAS_AUDIT · NOT_CLAIM_PS_FACT*  
*Post-HD-MAVP lock closed 2026-06-13 · docs/113_post_hd_mavp_selection_artifact_lock.md*
