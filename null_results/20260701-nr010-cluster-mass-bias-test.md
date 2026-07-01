# NR-010 — H1a: cluster ICM thermal energy vs WL-HE mass gap — KILLED

**Date:** 2026-07-01
**Verdict:** KILL (pre-registered criterion, tool-verified)
**Branch:** H1a — first sub-hypothesis of H1 (TJB IGM thermal energy = second gravitational source)

---

## Claim (falsified)

Cluster intracluster medium (ICM) thermal energy (`M_gas × T_x`) predicts the
lensing-to-hydrostatic mass gap (`delta_M = M_WL − M_HE`) in X-ray luminous clusters —
the most direct, cluster-scale test of the TJB thermal-energy-as-gravity mechanism.

## Why falsified

| Test | Result | Evidence |
|------|--------|----------|
| r(delta_M, M_gas×T_x) | 0.021, p=0.883 | `[VERIFIED-REAL]` CCCP N=50 (Mahdavi+2013) |
| Pre-registered kill threshold | r=0.021 < 0.20 required for survival; p=0.88 >> 0.30 | Criterion set before data seen |
| Direction check | Slightly negative, not positive as H1a requires | Hot clusters (T_x>8 keV) show LESS bias (delta_frac=−0.005) than cool (delta_frac=0.359) — opposite to prediction |
| Mass-scaling confound | r(M_WL, E_proxy)=0.713 — strong | Controlling for M_WL: partial r=−0.701, p<0.0001 — reverses sign, does not rescue H1a |
| Power check | N=50 gives ~91% power to detect r=0.4 at p<0.05 | Genuine null, not underpowered |

**Root cause:** H1a tests cluster-interior ICM, which is a narrower quantity than TJB's
actual mechanism (cosmic-web IGM/WHIM in filaments and nodes). Cluster ICM sits inside the
virial radius and is dominated by relaxation state, not the filament-scale thermal
reservoir the mechanism proposes.

## Kill Analysis

**What this KILLED:**
- The claim that cluster-interior ICM thermal energy (as measured, `M_gas×T_x`) predicts
  the WL-HE mass gap in the direction and strength H1a required.

**What this did NOT kill (survives):**
- H1 (broad TJB mechanism) — cosmic-web IGM/WHIM at filament/node scale is untested here.
- The striking partial correlation `r(delta_M, E_proxy | M_WL) = −0.701` — an unexplained,
  robust empirical pattern (later confirmed to survive both mass-split (NR-011) and
  morphology-split (NR-012) falsification attempts).

**Relaxation Map (surviving option space):**

| Variant | Changed assumption | Prediction | Status |
|---------|--------------------|-----------|--------|
| H1b | Use WHIM gas (T~10⁵–10⁷ K) in cosmic-web filaments, not cluster ICM | r(delta_M, WHIM thermal pressure) > 0.3 | NEEDS-DATA (TNG API) |
| H1c | Cluster morphological/dynamical state mediates the partial correlation | residual r drops below 0.20 after controlling for centroid shift | KILLED — see NR-012 |
| H1d | Effect is mass-threshold dependent (stronger in massive clusters) | |r_high| >> |r_low| | KILLED — see NR-011 |
| H1e (pearl candidate) | Effect is T_x-threshold dependent, not mass-threshold | needs N≥20 cool-cluster (T_x<5 keV) sample | pearl_registry, next_check 2026-07-15 |

## Forbidden use

Do NOT cite NR-010 as evidence against the broad TJB mechanism (H1) — it only rules out
the cluster-interior ICM formulation. Do NOT claim the partial correlation `r=−0.701`
validates H1 — it is an unexplained pattern, not a confirmed mechanism (see NR-011, NR-012
for what has been ruled out as an alternative explanation).

## Correct next direction

H1b (WHIM/filament thermal energy via IllustrisTNG simulation data) is the only remaining
open, TJB-specific test — blocked on user's TNG API registration (submitted 2026-07-01).

---

*KILL — pre-registered criterion met on [VERIFIED-REAL] CCCP data (Mahdavi et al. 2013, N=50).*
*Full analysis: `experiments/20260701-cluster-mass-bias-test/decision.md`.*
*NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION*
