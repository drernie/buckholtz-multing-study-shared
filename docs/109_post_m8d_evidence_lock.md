# docs/109 — Post-M8D Evidence Lock (EOD-4)

**Date:** 2026-06-13  
**Gate:** EOD-4 — freeze-point after M8-D MAVS  
**Replaces:** docs/107 (EOD-2, previous freeze-point)  
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
**Tests:** 690 passed / 12 skipped / 0 failed [VERIFIED-tool 2026-06-13]  
**Ruff:** clean [VERIFIED-tool 2026-06-13]  
**Branch:** feature/appendix-a1-doc-updates

---

## 2. New Commits Since EOD-2

| Commit | Description | Verdict |
|---|---|---|
| `9100b0a` | M8-D: MAVS virial+PS schedule | FAIL |
| `4f628af` | docs: null_results registry + mechanism insights | PASS |

---

## 3. M8-D Result: Minimal Assumption Virial Schedule (MAVS)

**Scope:** OUR_RECONSTRUCTION · CONDITIONAL_RECONSTRUCTION · NOT_AUTHOR_CONFIRMED  
**Labels:** M8_D_MAVS · AUTHOR_SCHEDULE_NEEDED · <HYPOTHESIS>

### Construction

Four MAVS components derived from first principles (no FLRW H(z) fitting, no power-law fit to Table A1):

| Component | Formula | Physical source |
|---|---|---|
| k_A(z) | G·M / r_vir(z)² | Virial theorem: 2K+U=0 → σ_v²=G·M/r_vir |
| r_vir(z) | [(3M)/(4π·200·ρ_crit(z))]^(1/3) | Overdensity criterion Δ_vir=200 |
| r_A(z) | n(>M_min, z)^(−1/3) | Press-Schechter mean comoving separation |
| r_P(z) | r_A(z) / (1+z) | Comoving → physical conversion |
| D_C:AB(z) | r_A(z) | Minimal assumption |

Tested at M_min = 1×10¹⁴, 5×10¹⁴, 2×10¹⁵ M_sun. ΛCDM: Ω_m=0.315, H_0=70, σ_8=0.811.

### Results

| M_min | k_A Pearson r | r_A Pearson r | r_P Pearson r | monotone_k_A |
|---|---|---|---|---|
| 1×10¹⁴ M_sun | −0.4621 | −0.2573 | −0.2573 | True |
| 5×10¹⁴ M_sun | −0.4621 | −0.5552 | −0.6004 | True |
| 2×10¹⁵ M_sun | −0.4621 | −0.5406 | −0.4469 | True |

**Best positive Pearson r across all components and all M_min: −0.2573** (all anti-correlated with ε).

**Verdict: FAIL**

### Why FAIL

k_A = G·M/r_vir² = const · M^(1/3) · ρ_crit(z)^(2/3) **∝ H(z)^(4/3)**.  
H(z) is monotone increasing with z → k_A is **monotone increasing by theorem**.  
A monotone function cannot reproduce a peak at z=0.40 followed by secondary structure at z=1.0–1.5.  
This is not a numerical limitation — it is a consequence of the virial theorem + overdensity criterion.

r_A = n^(−1/3) is monotone increasing for M_min below the PS knee.  
r_P is dominated by the PS divergence at high z.  
No MAVS component has a non-monotone profile.

**ε(z) structure that any valid bridge must reproduce:**
```
z:    0.06   0.14   0.25   0.40*  0.65   1.00   1.50   2.10   3.20   5.00   8.50
ε:   .063   .125   .215   .228   .213   .186   .214   .171   .106   .048   .101
             ↑      ↑    PEAK↓    ↓   LOCAL_MIN  RISE    ↓     ↓  GLOBAL_MIN UPTICK
```

No single monotone MAVS component can produce this pattern.

### Test coverage

29/29 tests passing for M8-D. Key safety tests:
- `test_k_A_monotone_increasing` — confirms virial theorem scaling holds
- `test_no_mavs_component_peaks_at_z040` — confirms FAIL is categorical, not marginal
- `test_verdict_fail_confirmed` — asserts overall_verdict == "FAIL"
- `test_safety_labels_present` — all 8 required labels in JSON report
- `test_no_h_fitting_flag` — no FLRW H(z) fitting used

---

## 4. Interpretation

**MAVS is OUR_RECONSTRUCTION, not the author's schedule.**

This result does NOT mean:
- MULTING is false or refuted
- The author's bridge is wrong
- The virial theorem is inapplicable to MULTING
- H_MULT(z) values in Table A1 are incorrect

This result DOES mean:
- Standard virial self-similar scaling **cannot** be the sole ingredient in a bridge that reproduces ε(z)
- Any viable bridge must contain a **non-monotone component** — either in k_A, D_eff, or the normalization
- The author's specific k_A(z)/D_eff(z)/cluster-selection schedule is **essential** and cannot be reconstructed from first principles alone

**Strengthens Q2 blocker:** Before M8-D, Q2 was "we don't know k_A(z)". After M8-D, Q2 is sharpened: "any k_A(z) consistent with virial self-similar scaling is ruled out as the sole non-monotone ingredient — author's specific schedule is uniquely needed."

---

## 5. Updated Q2 Blocker

**Q2 (original):** k_A(z) / D_eff(z) cluster schedule unknown.

**Q2 (post-M8-D):** The schedule must satisfy:
1. NOT reducible to standard virial k_A ∝ H(z)^(4/3) alone
2. Must produce a non-monotone ε(z) with primary peak near z≈0.40
3. Must account for secondary structure at z=1.0–1.5 and uptick at z=8.5
4. Options: non-virial k_A formula, OR non-PS D_eff, OR cluster-selection that peaks mid-z, OR a ratio of two monotone components with different scalings

**Status:** MISSING — only TJB can resolve Q2.

---

## 6. Mechanism Insights Captured (commit 4f628af)

Four mechanistic constraints from negative results are now documented in `null_results/` + `docs/mechanism_insights.md`:

| # | Insight | Confidence |
|---|---------|------------|
| 1 | ε(z) has 3+ characteristic scales — no single-parameter bridge possible | `[STRONG]` |
| 2 | Cluster density n(>M,z) anti-correlated; formation rate dN/dz best signal (r=0.723) | `[SIGNAL]` |
| 3 | k_A from virial ∝ H(z)^(4/3) — monotone by theorem, not data-dependent | `[THEOREM]` |
| 4 | Non-monotone ε constrains bridge to specific topological class | `[STRONG]` |

---

## 7. Full Blocker Status

| Blocker | Status |
|---|---|
| Q1: Bridge method F_oP → H_MULT(z) | MISSING |
| Q2: k_A(z) / D_eff(z) cluster schedule | MISSING (sharpened by M8-D) |
| Q3: β parameter provenance | OPEN (TJB partial: "fitted, may or may not be fundamental") |
| Independent data (Pantheon+ / BAO) | MISSING |
| Complexity penalty (AIC/BIC) | MISSING |

**0/5 blockers resolved. MCMC remains BLOCKED.**

---

## 8. Forbidden Actions (Hard)

| Action | Reason |
|---|---|
| Public claim about MULTING validity | 0/5 blockers resolved |
| MCMC | 0/5 blockers resolved |
| "Theory false / refuted / falsified" | We tested OUR reconstruction, not author's intended bridge |
| "AI hallucinated Table A1" | Risk is established; hallucination claim is overclaim |
| Second email before 2026-06-18 | Author contact protocol |
| New physics additions | Not authorized without TJB Q1+Q2 answers |

---

## 9. Evidence Block

```
EVIDENCE BLOCK — EOD-4 (2026-06-13)

CONFIRMED [VERIFIED-tool or TRANSCRIBED]:
  [1] No explicit bridge F_oP → H_MULT(z) found in public materials (BLOCKER Q1)
  [2] ε(z) non-monotonic (11 values verified, M8-A-R1 PASS)
      Peak: ε=0.2277 at z=0.40 | Min: ε=0.0481 at z=5.00
  [3] Constant-ε bridge FAILS (max residual 0.104 >> 0.05)
  [4] Power-law bridge FAILS (α sign changes at z=0.40, 1.00, 5.00)
  [5] PS comoving density (Model A) monotone — cannot peak at z=0.40 (M8-C)
  [6] dN/dz (Model B) peaks at z=0.40–0.65, best Pearson r=0.723 (M8-C PARTIAL)
  [7] MAVS k_A(z) ∝ H(z)^(4/3) — monotone by theorem — FAIL (M8-D)
  [8] All MAVS components anti-correlated with ε; best r = −0.2573 (M8-D)
  [9] null_results/ registry: 4 REJECT entries with mechanistic insights
  [10] β = phenomenological fitting coefficients (TJB confirmed partial, Q3)
  [11] Author email Q1–Q3 sent 2026-06-12; reply expected not before 2026-06-18

HYPOTHESIS [not confirmed]:
  [H1] ε(z) shape connected to cluster formation rate (dN/dz signal r=0.723)
  [H2] Bridge non-monotone component is in Φ-normalization (M8-B forensic pending)

OPEN [requires TJB]:
  [O1] Author's actual bridge formula (Q1)
  [O2] k_A(z) / D_eff(z) — non-virial, non-monotone schedule (Q2 sharpened)
  [O3] Physical vs fitted status of β (Q3)

REJECTED CLAIMS [do not repeat]:
  - "MULTING refuted" / "theory false"
  - "AI hallucinated" (overclaim)
  - "SC-2 gap refutes author theory"
  - "PS bridge confirmed" / "MAVS confirms Q2"
  - "Virial theorem disproves MULTING"
```

---

## 10. Verdict

```
EOD-4 VERDICT: PASS

Rationale:
  - M8-D completed with honest FAIL verdict (not inflated)
  - 29/29 tests pass; ruff clean; JSON report produced
  - Mechanistic insights from negative results captured in null_results/ and
    docs/mechanism_insights.md (commit 4f628af)
  - Q2 blocker sharpened (not just "unknown" — now "must be non-virial and non-monotone")
  - All safety labels present; no overclaims in committed files
  - No forbidden actions taken

Evidence quality: sufficient for a freeze-point.
MCMC readiness: 0/5 blockers — remains BLOCKED.
Public claim readiness: NO — awaiting TJB response.
```

---

## 11. Files Changed (since EOD-2 / docs/107)

| File | Change | Commit |
|---|---|---|
| scripts/m8d_mavs_schedule.py | NEW — virial+PS schedule, 280 lines | 9100b0a |
| tests/test_m8d_mavs_schedule.py | NEW — 29 tests | 9100b0a |
| reports/m8d_mavs_schedule.json | NEW — gate report, verdict=FAIL | 9100b0a |
| null_results/INDEX.md | NEW — 4 REJECT entries | 4f628af |
| null_results/20260612-bridge-candidates-fail.md | NEW — NR-001/002 | 4f628af |
| null_results/20260612-ps-comoving-model-a-fail.md | NEW — NR-003 | 4f628af |
| null_results/20260613-mavs-virial-ps-insufficient.md | NEW — NR-004 | 4f628af |
| docs/mechanism_insights.md | NEW — INSIGHT-1 through INSIGHT-4 | 4f628af |

---

## 12. Next State

```
NEXT_STATE: WAITING_FOR_TJB

  Active gates:          NONE (all completed or blocked)
  Next trigger:          TJB reply to Q1–Q3 email (2026-06-12)
  Earliest follow-up:    2026-06-18 (one polite nudge, same Q scope)

  Next allowed gates (priority order):
    1. ASRE — Author-Schedule Reverse Engineering
       (only when TJB answers Q1+Q2; not before)
    2. M8-B — Φ-normalization forensic audit
       (low priority; forensic only, no new physics)
    3. TJB follow-up email
       (not before 2026-06-18; same Q1–Q3 scope only)

  Hard blockers remain: Q1 bridge + Q2 k_A(z) → MCMC still 0/5

  Session freeze: this file is the authoritative state snapshot.
  Next session starts with: docs/109 + docs/mechanism_insights.md + activeContext.md
```

---

*NOT_VALIDATION · NOT_REFUTATION · INTERNAL_DIAGNOSTIC_ONLY*  
*EOD-4 gate closed 2026-06-13 · docs/109_post_m8d_evidence_lock.md*
