# NR-014 — H1e: AGN feedback as confounder for the partial correlation — KILLED

**Date:** 2026-07-17 (pre-registered 2026-07-13)
**Verdict:** KILL (pre-registered criterion, tool-verified)
**Branch:** H1e — third natural standard-physics alternative explanation for NR-010's
partial correlation (AGN radio/kinetic-mode feedback as a confounder)

---

## Claim (falsified)

The partial correlation `r(delta_M, E_ICM | M_WL) ≈ −0.71` (NR-010) is primarily
explained by AGN feedback activity (cool-core regulation): clusters with strong central
AGN feedback would show systematically different thermal-energy proxy and/or mass bias,
creating the observed anti-correlation without requiring a TJB-style mechanism.

## Why falsified

| Test | Result | Evidence |
|------|--------|----------|
| Baseline partial r (N=47, K0/wX-available subsample) | −0.7143 | `[VERIFIED-REAL]` Mahdavi+2013 Table 2, K0 for 47/50 clusters |
| KEY TEST: partial r(delta_M, E_ICM \| M_WL, K0) | −0.7181, p=1.33e-08 | Controlling for AGN feedback (central entropy) as well |
| Change in \|r\| after adding K0 | +0.0038 (essentially unchanged) | AGN feedback adds zero explanatory overlap |
| r(K0, delta_M \| M_WL) | 0.0180, p=0.904 | K0 does not predict mass bias at fixed M_WL |
| r(K0, E_ICM \| M_WL) | 0.0795, p=0.595 | K0 not confounded with thermal proxy at fixed M_WL |
| Pre-registered kill threshold | \|r_residual\|=0.7181 > 0.40 required to kill H1e | Criterion set before the test was run |

**A2 cross-check (K0 vs wX, not a duplicate of H1c):** raw r(K0, wX)=0.31, p=0.035 —
correlated but <10% shared variance; consistent with the source paper's own reported
Spearman r=0.52±0.10. Controlling for wX instead of K0 reproduces NR-012's exact number
(r=−0.726), confirming the merged dataset and both covariates behave independently.

## Kill Analysis

**What this KILLED:**
- AGN-feedback/cool-core confounding as an explanation for the partial correlation.
  Standard cluster physics via this channel does NOT explain the pattern away.

**What this did NOT kill (survives):**
- The partial correlation `r≈−0.70 to −0.73` — now confirmed robust against FOUR
  independent falsification attempts (raw NR-010, mass-split NR-011, morphology-split
  NR-012, AGN-feedback-split H1e/NR-014), all converging on the same magnitude.
- H1 (broad TJB mechanism) — killing the third standard-physics alternative narrows
  further, but does not close, the space of competing explanations, and does not
  itself confirm H1.

**Relaxation Map:**

| Variant | Changed assumption | Prediction | Status |
|---------|--------------------|-----------|--------|
| Non-thermal pressure support | Turbulence/bulk motion, not captured by wX or K0 | Would need velocity-dispersion or simulation-based non-thermal fraction data | Not tested |
| Weak-lensing measurement systematics | Shape-pipeline/triaxiality bias in M_WL itself | Would need alternative WL pipeline comparison per cluster | Not tested, not yet formulated as a branch |
| H1b (WHIM/filament) | TJB's actual proposed mechanism, filament-scale not cluster-scale | r(delta_M, WHIM thermal energy) > 0.3 in TNG simulations | NEEDS-DATA (TNG API, blocked 16+ days) |

## Forbidden use

Do NOT cite NR-014 as confirmation of H1 — it only rules out AGN feedback as the
confounder. Do NOT conflate H1e with H1c — they use mechanistically distinct covariates
(K0 vs wX) despite moderate correlation between them (r=0.31, verified non-degenerate).

## Correct next direction

With all four testable standard-physics alternatives on existing CCCP data now killed
(H1a, H1c, H1d, H1e), H1b (WHIM/filament test) remains the only originally-considered
open test of the TJB mechanism, still blocked on TNG API access. A genuinely new
alternative not yet tested is weak-lensing measurement systematics itself.

---

*KILL — pre-registered criterion met on [VERIFIED-REAL] CCCP data (N=47/50).*
*Full analysis: `experiments/20260713-h1e-agn-feedback-confound/decision.md`.*
*NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION*
