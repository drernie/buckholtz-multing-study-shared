# NR-012 — H1c: cluster morphology as confounder for the partial correlation — KILLED

**Date:** 2026-07-01
**Verdict:** KILL (pre-registered criterion, tool-verified)
**Branch:** H1c — the leading standard-physics alternative explanation for NR-010's
partial correlation (morphological/dynamical relaxation state as a confounder)

---

## Claim (falsified)

The partial correlation `r(delta_M, E_proxy | M_WL) = −0.701` (NR-010) is primarily
explained by cluster morphological state (X-ray centroid shift wX): morphologically
relaxed clusters would show both higher apparent thermal energy and smaller mass bias,
creating a spurious anti-correlation that requires no TJB-style mechanism.

## Why falsified

| Test | Result | Evidence |
|------|--------|----------|
| Baseline partial r (N=47, wX-available subsample) | −0.714 | `[VERIFIED-REAL]` Mahdavi+2013 Table 2, wX for 47/50 clusters |
| KEY TEST: partial r(delta_M, E_proxy \| M_WL, wX) | −0.726, p=7.7e-9 | Controlling for morphology as well |
| Drop in \|r\| after adding wX | −0.012 (i.e. \|r\| slightly INCREASED) | Morphology adds zero explanatory overlap |
| r(delta_M, wX \| M_WL) | −0.088, p=0.55 | wX does not predict mass bias at fixed M_WL |
| r(E_proxy, wX \| M_WL) | −0.076, p=0.61 | wX not confounded with thermal proxy at fixed M_WL |
| Pre-registered kill threshold | \|r_residual\|=0.726 > 0.40 required to kill H1c | Criterion set before wX data was obtained |

**Data source correction:** originally planned to use Mann & Ebeling 2012 for morphology
data, but that paper uses a different metric (BCG-to-X-ray-peak separation, not centroid
shift). The correct wX values were already in Mahdavi et al. 2013 Table 2 — same paper as
NR-010/NR-011.

## Kill Analysis

**What this KILLED:**
- Morphological/dynamical-state confounding as an explanation for the partial correlation.
  Standard cluster physics via this channel does NOT explain the pattern away.

**What this did NOT kill (survives):**
- The partial correlation `r≈−0.70 to −0.73` — now confirmed robust against THREE
  independent falsification attempts (raw correlation NR-010, mass-split NR-011,
  morphology-split NR-012), all converging on the same magnitude.
- H1 (broad TJB mechanism) — killing the leading standard-physics alternative narrows,
  but does not close, the space of competing explanations, and does not itself confirm H1.

**Relaxation Map:**

| Variant | Changed assumption | Prediction | Status |
|---------|--------------------|-----------|--------|
| Non-thermal pressure support | Turbulence/bulk motion, not captured by wX | Would need velocity-dispersion or simulation-based non-thermal fraction data | Not tested |
| AGN feedback | Feedback-driven gas displacement | Would need AGN-activity indicators per cluster | Not tested |
| H1b (WHIM/filament) | TJB's actual proposed mechanism, filament-scale not cluster-scale | r(delta_M, WHIM thermal energy) > 0.3 in TNG simulations | NEEDS-DATA (TNG API) |

## Addendum — retracted circular test (methodology lesson)

A same-session attempt at a "cheapest test" for a T_x-threshold pearl (direct T_x as
covariate: `partial r(delta_M, E_proxy | M_WL, T_x) = −0.109`) initially looked like strong
mediation evidence but was found INVALID: T_x is a literal multiplicative component of
`E_proxy = M_gas × T_x` (raw `r(T_x, E_proxy) = 0.895`), making the test near-circular.
Retracted before promotion — see `experiments/20260701-h1c-morphology-mass-bias/decision.md`
addendum and `cross_domain_insights.md` (Silver: "circular covariate trap in partial
correlation"). A redesigned non-circular test (M_gas alone, not multiplied by T_x) remains
open, `pearl_registry` next_check 2026-07-15.

## Forbidden use

Do NOT cite NR-012 as confirmation of H1 — it only rules out morphology as the confounder.
Do NOT cite the retracted T_x-covariate result (r=−0.109) as evidence for or against
anything — it is methodologically invalid, not a null result.

## Correct next direction

H1b (WHIM/filament test) is now the only remaining open, cluster-scale-independent test of
the TJB mechanism, since the two most natural standard-physics alternatives (mass-threshold,
morphology) have both been ruled out on real CCCP data.

## Addendum 2026-07-18 — NR-015 reclassification

The redesigned non-circular test this file's own addendum proposed ("M_gas-only, not
M_gas×T_x, remains open for a future session") was finally executed. **Result: NOT-SURVIVES
the pre-registered criterion** — with the exact pre-registered control (`M_WL` AND `T_X`
together, not `M_WL` alone), `r(delta_M, M_gas | M_WL, T_X)` collapses to −0.08 (p=0.58,
bootstrap 95% CI [-0.39,0.27]). Separately, `r(delta_M, T_X | M_WL) = −0.81` — T_X alone, at
fixed M_WL, is a *stronger* predictor than the E_ICM proxy this whole file is built on.
NR-012's own KILL verdict (morphology/wX does not mediate) is unaffected. But this file's
"the partial correlation is therefore robust against two natural standard-physics
alternative explanations" framing (echoed in `paper/main.tex`) overclaims: neither
alternative tested here controlled for T_X. **Mechanism is NOT established** — an
independent skeptic review found a real competing explanation (dynamical state as a genuine
common physical driver of both T_X and delta_M, not merely a definitional M_hydro-T_X
coupling) that this test does not distinguish from the definitional reading; both remain
live. See `null_results/20260718-nr015-tx-shared-variable-artifact.md` for the full
Skeptic Response Matrix.

---

*KILL — pre-registered criterion met on [VERIFIED-REAL] CCCP data (N=47/50).*
*Full analysis: `experiments/20260701-h1c-morphology-mass-bias/decision.md`.*
*NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION*
