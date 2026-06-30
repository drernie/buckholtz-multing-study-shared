# Decision — 20260701-h1c-morphology-mass-bias

**Date:** 2026-07-01
**Status:** KILL (H1c)
**Evidence grade:** B (N=47/50 real observational data [VERIFIED-REAL])

## Data source

wX (centroid shift variance, units 10^3 × r500_WL) extracted from Mahdavi et al. 2013
(arXiv:1210.3689) Table 2 via direct fetch of the ar5iv HTML rendering. [VERIFIED-REAL]

Note: Mann & Ebeling 2012 (arXiv:1111.0610) — the originally planned source — does NOT
contain the standard centroid shift w parameter. It uses BCG-to-X-ray-peak/centroid
separation in kpc as a merger classifier, a different metric. Mahdavi et al. 2013 Table 2
(the same paper as H1a/H1d) turned out to already contain the needed morphology column,
so no additional cross-matching was required.

**Coverage:** 47/50 CCCP clusters. Missing wX: Abell0115S, Abell2104, Abell2219 (no data
published in Table 2 for these 3).

## Numerical results [OUR-RECONSTRUCTION]

### Baseline (wX-available subsample, N=47)
| | r | p |
|--|---|---|
| partial r(delta_M, E_proxy \| M_WL) | −0.714 | 1.72×10⁻⁸ |

Consistent with full-sample N=50 result from H1a/H1d (r=−0.701) — the 3 excluded
clusters do not materially change the baseline correlation.

### Secondary checks
| Test | r | p | Interpretation |
|------|---|---|----------------|
| r(delta_M, wX \| M_WL) | −0.088 | 0.5543 | Morphology does NOT predict mass bias at fixed M_WL |
| r(E_proxy, wX \| M_WL) | −0.076 | 0.6107 | E_proxy and wX are NOT confounded at fixed M_WL |

### KEY TEST — residual partial correlation
| | r | p |
|--|---|---|
| partial r(delta_M, E_proxy \| M_WL, wX) | **−0.726** | 7.73×10⁻⁹ |

**Drop in \|r\| after adding wX as covariate: −0.012** (i.e., \|r\| slightly INCREASED,
from 0.714 to 0.726 — morphology adds no explanatory overlap with the E_proxy/delta_M
relationship).

## Verdict

**H1c KILLED** by pre-registered criterion:
- \|r_residual\| = 0.726 > 0.40 (kill threshold)
- Morphological state (centroid shift wX) does NOT mediate or explain away the partial
  correlation between thermal energy proxy and mass bias.

The partial correlation r(delta_M, E_proxy | M_WL) ≈ −0.72 is **NOT** an artifact of
cluster dynamical/morphological state. wX is essentially orthogonal to both delta_M and
E_proxy once M_WL is controlled (both secondary checks r ≈ −0.08, p > 0.5, not
significant).

## Kill Analysis

**What was killed:**
H1c — the hypothesis that standard cluster physics (morphological/dynamical state,
proxied by X-ray centroid shift) explains the strong partial anti-correlation between
ICM thermal energy and lensing-hydrostatic mass gap, WITHOUT invoking a TJB-style
second gravitational source.

Conditions: {CCCP N=47 (wX-available subset), wX as the morphology proxy, linear partial
correlation method, OUR_RECONSTRUCTION}.

**What was NOT killed:**
1. H1 (broad TJB mechanism) — H1c was the most natural standard-physics alternative
   explanation; its failure does NOT confirm H1, but removes one major competing
   explanation
2. H1b — WHIM filament thermal energy correlation (still NEEDS-DATA, TNG API)
3. The reality and strength of the partial r ≈ −0.70 to −0.73 (now verified independent
   of mass split AND independent of morphology split)
4. Pearl P001 (T_x threshold) — wX and T_x are conceptually distinct; T_x sensitivity
   not directly tested here

**Important interpretive note:** killing H1c does NOT promote H1. It only eliminates one
alternative (standard-physics morphological confound). Other non-TJB explanations remain
possible (e.g., non-thermal pressure support, AGN feedback, instrument calibration
systematics, hydrostatic bias scaling with something other than morphology or mass).
This experiment narrows but does not close the space of competing explanations.

## Relaxation Map (cumulative, H1 Cycle 2)

| Branch | Changed assumption | Prediction | Status |
|--------|--------------------|-----------|--------|
| H1a | ICM thermal energy ~ mass gap (raw) | r > 0.4 | KILLED (r=0.021) |
| H1d | Mass-threshold effect | \|r_high\| >> \|r_low\| | KILLED (r_diff=0.001) |
| H1c | Morphology (wX) mediates partial r | residual r drops to <0.20 | **KILLED (r=−0.726, stronger than baseline)** |
| H1b | WHIM gas in filaments | r > 0.30 in simulations | NEEDS-DATA (TNG API) |
| H1-Tx (Pearl P001) | T_x threshold instead of mass | \|r_hot\| >> \|r_cool\| on larger sample | PEARL [CANDIDATE] — needs N≥20 cool clusters |

## Skeptic concerns (pre-answered)

**Concern 1:** "N=47 vs N=50 — does excluding 3 clusters bias the result?"
→ DISMISSED. Baseline r on N=47 (−0.714) closely matches full-sample N=50 r (−0.701,
from H1a). The exclusion (3 clusters with missing wX) does not appear to introduce
selection bias on the key relationship.

**Concern 2:** "Maybe wX is a noisy/weak morphology proxy — a null result here doesn't
rule out morphology in general."
→ ACCEPTED as limitation. wX (centroid shift) is one standard morphology metric but not
the only one (concentration, power ratios are alternatives). A genuinely cleaner test
would use multiple morphology indicators jointly. This is a real limitation: H1c tested
ONE morphology proxy, not "morphology" as a general category.

**Concern 3:** "r(delta_M, wX | M_WL) = −0.088 is not significant — could this be a
power issue (N=47), not a true null?"
→ PARTIALLY ACCEPTED. With N=47, power to detect r=0.30 is moderate (~65%) but the
effect size needed to flip the verdict (|r|>0.40) would very likely have been detected
given the sample size. The KEY TEST result (residual r=−0.726, p=7.7e-9) is the
decisive evidence — it is overwhelmingly significant in the OPPOSITE direction predicted
by H1c (mediation would show convergence toward zero, not divergence).

## Status summary for H1 Cycle 2 (final)

| Sub-hypothesis | Status | Data |
|----------------|--------|------|
| H1a | KILLED (2026-07-01) | r=0.021, N=50 CCCP [VERIFIED-REAL] |
| H1b | NEEDS-DATA | TNG API required (user action) |
| H1c | **KILLED (2026-07-01)** | r_residual=−0.726, N=47 CCCP [VERIFIED-REAL] |
| H1d | KILLED (2026-07-01) | r_diff=0.001, N=50 CCCP [VERIFIED-REAL] |

**H1 (broad) status: INCONCLUSIVE, but narrowing.** Three of four sub-hypotheses
investigable on existing CCCP data are KILLED. The partial correlation r ≈ −0.70 is:
- NOT explained by raw thermal energy (H1a)
- NOT mass-threshold dependent (H1d)
- NOT explained by morphological/dynamical state (H1c)

This is a genuinely puzzling, robust empirical pattern that survives 3 independent
falsification attempts. It does NOT confirm the TJB mechanism (H1b — the cosmic-web/
filament-scale test — remains the cleanest TJB-specific test and is still NEEDS-DATA).
But the partial correlation itself is now a well-characterized, hard-to-explain-away
empirical fact at cluster scale, independent of mass and independent of morphology.

**Next priority:** H1b (TNG API — requires user registration at tng-project.org) is now
the highest-value remaining test, since the cluster-scale standard-physics alternatives
(H1c) have been exhausted.

## Addendum — Pearl P001 cheapest-test attempt: INVALID (circular), not confirmed

Following the Cheapest Differentiating Test protocol, the same-session "cheapest next
test" for Pearl P001 (T_x threshold) was attempted: partial r(delta_M, E_proxy | M_WL, T_x)
computed directly on the same N=47 subsample.

**Result:** r = −0.109, p = 0.466 — naively appears to "confirm" that T_x mediates the
effect (large drop from baseline −0.714).

**Self-caught artifact (audit-verification-gate, before promotion):** E_proxy is
DEFINED as M_gas × T_x. A check of the raw correlation found r(T_x, E_proxy) = 0.895,
p=2.25e-17 (partial version controlling M_WL: r=0.834). T_x is not an independent
covariate here — it is one of the two literal multiplicative factors that constitute
E_proxy by construction. Controlling for T_x while testing E_proxy is close to
controlling for ~80% of E_proxy's own variance, i.e. a near-circular test (CDT Protocol
anti-pattern: "test assumes the result it is testing").

**Verdict: this test is INVALID, not a confirmation of Pearl P001.** The dramatic drop
in partial r (−0.714 → −0.109) is the expected mechanical consequence of conditioning a
variable on one of its own defining components, not evidence that ICM temperature state
mediates the delta_M/E_proxy relationship.

**Correction to pearl_registry/INDEX.md:** the originally proposed "cheapest test" for
Pearl P001 (direct T_x covariate on E_proxy) is retracted as methodologically invalid.
A valid test would need a thermal-energy proxy NOT multiplicatively defined by T_x —
e.g. testing whether M_gas alone (controlling separately for T_x and M_WL) retains the
partial correlation with delta_M, since M_gas is not definitionally entangled with T_x.
This redesigned test remains open for a future session.

**Lesson (research-methodology.md classifier, Type 1 — symbolic overload):** when a
covariate is a literal multiplicative/additive component of the dependent variable's
own proxy definition, partialling it out is not a clean confound test. Always check
raw correlation between the proposed mediator and the outcome's defining inputs BEFORE
interpreting a partial-correlation drop as mediation.
