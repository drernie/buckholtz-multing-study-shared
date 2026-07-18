# NR-011 — H1d: mass-threshold effect on ICM/mass-bias partial correlation — KILLED

**Date:** 2026-07-01
**Verdict:** KILL (pre-registered criterion, tool-verified)
**Branch:** H1d — sub-hypothesis of H1, testing whether the partial correlation found in
NR-010 is mass-scale dependent

---

## Claim (falsified)

The partial correlation `r(delta_M, E_proxy | M_WL) = −0.701` (from NR-010) is
significantly larger in magnitude in high-mass clusters (M_WL ≥ median) than in low-mass
clusters — i.e. the TJB mechanism acts preferentially at cluster scale, consistent with a
mass-threshold for gravitational significance.

## Why falsified

| Test | Result | Evidence |
|------|--------|----------|
| partial r, HIGH-mass (N=25, M_WL≥6×10¹⁴) | −0.732 | `[VERIFIED-REAL]` CCCP N=50 split at median |
| partial r, LOW-mass (N=25, M_WL<6×10¹⁴) | −0.731 | same |
| Fisher z-test (\|r_high\| vs \|r_low\|) | z=0.005, p=0.498 | No significant difference |
| Pre-registered kill threshold | \|r_diff\|=0.001 << 0.20 required to survive | Criterion set before data seen |

**Root cause:** the partial correlation is essentially identical across the full mass
range tested — there is no mass-dependent regime change in the CCCP sample.

## Kill Analysis

**What this KILLED:**
- Mass-threshold framing of H1: the idea that the partial correlation's strength depends
  on cluster mass scale, within the CCCP sample's mass range.

**What this did NOT kill (survives):**
- The partial correlation itself — confirmed IDENTICAL in both subsamples, which is
  itself a robustness finding (see NR-010, NR-012).
- Pearl P001 (T_x-threshold, not mass-threshold): sensitivity split by T_x showed HOT
  (T_x≥5 keV, N=41): r=−0.681 vs COOL (T_x<5 keV, N=9): r=−0.066 — but N=9 is severely
  underpowered, this is NOT informative evidence either way (see pearl_registry entry).

**Relaxation Map:**

| Variant | Changed assumption | Prediction | Status |
|---------|--------------------|-----------|--------|
| H1d-Tx (Pearl P001) | Temperature threshold instead of mass threshold | \|r_hot\| >> \|r_cool\| on N≥20 cool-cluster sample | pearl_registry [CANDIDATE], underpowered attempt at direct T_x-as-covariate test was found CIRCULAR and retracted (see NR-012 addendum) |
| Higher mass regime | Threshold above CCCP's mass range (>10¹⁵ M_sun) | Untestable on CCCP (only N=7 clusters above this) | Would need SPT/ACT data |

## Forbidden use

Do NOT cite NR-011 as evidence that H1 (broad) is dead — it only rules out a
mass-dependent regime change within the CCCP mass range (roughly 10¹⁴–2×10¹⁵ M_sun).

## Correct next direction

H1b (WHIM/filament test, TNG-based) remains the cleanest untested TJB-specific prediction.
The redesigned non-circular T_x-mediation test (M_gas alone, not M_gas×T_x, as the proxy)
is a cheap next check reusing existing CCCP data — see pearl_registry, next_check 2026-07-15.

## Addendum 2026-07-18 — NR-015 reclassification

The redesigned test flagged above as the "correct next direction" was finally executed.
**Result: NOT-SURVIVES the pre-registered criterion** — `r(delta_M, M_gas | M_WL, T_X)`
collapses to −0.08 (p=0.58, bootstrap 95% CI [-0.39,0.27]) once T_X is properly controlled,
while T_X alone at fixed M_WL has r=−0.81, the single strongest predictor found in the H1
program. **Mechanism is NOT established** (definitional M_hydro-T_X coupling vs. a genuine
common physical driver like dynamical state remain both live — see NR-015's Skeptic Response
Matrix). NR-011's own KILL verdict (no mass-threshold effect) is unaffected — it correctly
rules out mass-threshold specifically. But NR-011 never controlled for T_X, so it cannot be
cited (alone or combined with NR-012/NR-014) as evidence the correlation is unexplained by
standard physics. See `null_results/20260718-nr015-tx-shared-variable-artifact.md` for the
full analysis.

---

*KILL — pre-registered Fisher z-test criterion met on [VERIFIED-REAL] CCCP data.*
*Full analysis: `experiments/20260701-h1d-mass-threshold/decision.md`.*
*NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION*
