# FINDING P167 — Phase 2 of the AIC/BIC calibration plan: a physically-
# empty 3-parameter model matches or beats MULTING's own χ² on the same
# 33 real data points

**Date:** 2026-08-30
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 predictive (real numerical curve-fit against real,
cross-verified external data — a genuine calibration experiment, not
symbolic derivation)
**Script:** `P167_dummy_model_calibration_fit.py` — positive control
(recovers a known injected synthetic curve, sane reduced-χ²) + negative
control (a `k=1` constant model fits substantially worse, confirming the
fitting procedure is genuinely sensitive to the data's own shape) +
explicit sensitivity check on the one flagged data-source discrepancy.
**Data:** 31-point Cosmic Chronometer H(z) compilation, cross-verified
against two independent primary sources (Gómez-Valent & Amendola 2018,
`arXiv:1802.01505`; Yu, Ratra & Wang 2018, `arXiv:1711.03437`) — 31/31
rows agree on `(z, H(z))`, 30/31 also agree on `σ_H` (one flagged
discrepancy, `z=0.47`: `σ=49.6` vs `σ=50.0`, resolved via sensitivity
check, §3). Plus v82's own quoted SH0ES and DESI points — same 33 points
v82 itself uses, no new data invented.
**Verdict (final, post-skeptic — see "Correction" below, this narrows
the claim's conditions, not just its wording):** `UNDER A SIMPLE DIAGONAL
(INDEPENDENT-ERRORS) χ² TREATMENT OF THE 31 COSMIC CHRONOMETER POINTS —
AN ASSUMPTION v82's OWN TEXT NEITHER STATES NOR RULES OUT — A
PHYSICALLY-EMPTY QUADRATIC-IN-z MODEL FOR Y≡H² (NO DARK-ENERGY STORY, NO
CLUSTER-GRAVITY STORY) FITS THE SAME 33 REAL DATA POINTS *BETTER* THAN
MULTING's OWN REPORTED FIT, AT EQUAL PARAMETER COUNT, BEFORE ANY AIC/BIC
PENALTY. Unconstrained (`k=3`): dummy `χ²=14.073` vs MULTING's own
`χ²=15.75` (`Δχ²=−1.677`). SH0ES-anchored (`k=2`): dummy `χ²=14.107` vs
MULTING's own `χ²=15.78` (`Δχ²=−1.673`). Since `k` is equal, `ΔAIC=ΔBIC=
Δχ²` exactly — no parameter-penalty asymmetry to resolve, IF the error
treatment matches. Sensitivity check on the one flagged data discrepancy
changes nothing detectable (`Δχ²<0.001`). **THE MARGIN (`≈1.7`, `~11%` of
MULTING's own `χ²`) IS SMALL ENOUGH THAT A FULL COVARIANCE-MATRIX
TREATMENT OF THE 31 CC POINTS' KNOWN SHARED SYSTEMATICS — STANDARD IN
MORE CAREFUL CC LITERATURE, NOT CONFIRMED OR RULED OUT BY v82's OWN
TEXT — COULD PLAUSIBLY CLOSE OR REVERSE IT.** This file's own comparison
is conditional on this unverified assumption, not a fully settled result.
COMBINED WITH `FINDING_P166`: MULTING does not clearly clear the
information-criterion bar against either a fair ΛCDM comparator (`P166`)
or, UNDER THIS UNVERIFIED ASSUMPTION, an even simpler physically-
unconstrained curve. THIS IS NOT EVIDENCE THAT MULTING's PHYSICS IS WRONG
(`NO_AUTHOR_ERROR`, §0) — read carefully (§4), it is at most evidence
that MULTING's own tiered force-law structure does not currently
demonstrate a *clear, assumption-independent* fit-quality advantage over
an unconstrained comparator, on this specific dataset.`
**Correction (2026-08-31, context-asymmetric skeptic-caught, two points,
both independently re-checked before applying — not accepted on the
skeptic's word alone):** the skeptic dispatched for this file (a) could
not execute the script directly in its own sandboxed environment (no
Bash tool available to it) and said so explicitly, flagging that its own
confirmation was code-review-level, not execution-level. This session
had already directly executed the script itself before writing this
finding (the printed output is what the verdict numbers above are
transcribed from) — that execution is the actual `[VERIFIED-tool]`
evidence for the numbers, now stated explicitly rather than left
implicit. (b) **The more substantive catch**: neither this file nor
`FINDING_P166` established whether MULTING's own reported `χ²=15.75/
15.78` was computed under the SAME error-weighting assumption this
script uses (a simple diagonal `1/σ²` sum, treating all 31 Cosmic
Chronometer points as statistically independent). Cosmic Chronometer
compilations are documented in the literature to carry non-trivial
covariance between redshift bins from shared systematics (stellar
population synthesis, metallicity, star-formation-history assumptions);
a full-covariance treatment can shift `χ²` by amounts comparable to or
larger than this file's own reported margin. **Checked directly**: v82's
own text contains zero mentions of a covariance matrix anywhere in
connection with its own `χ²` computation (`grep -i "covarian"` across the
full document — matches are all about unrelated topics: cluster-cluster
correlation length, weak-lensing shear correlations, galaxy velocity
correlations). This is consistent with, but does not prove, TJB having
used simple diagonal weighting — the paper simply does not specify this
methodological detail explicitly either way. Given the reported margin
(`Δχ²≈1.7`, roughly `11%` of MULTING's own `χ²`) is small enough that a
covariance-matrix treatment could plausibly close or reverse it, the
verdict below is corrected to state this explicitly as an open,
unresolved assumption — not a settled result — and the natural next
sensitivity check is named rather than silently skipped.
**Continues:** `FINDING_P166`'s own named Phase 2 — "fitting a
physically-empty dummy model of the same flexibility against real H(z)
data, as an independent calibration check on whether generic 3-parameter
flexibility alone could explain the fit."

## 0. Premise — `NO_AUTHOR_ERROR`, and what this result actually says

This file does not claim MULTING's own physics is incorrect. What it
shows is narrower and more precise: **the specific functional shape**
MULTING's dipole/quadrupole force law imposes on `H(z)` — derived from
real physical constraints (a two-tier multipole force law, specific
mass/radius/thermal-energy power laws) — is *more restrictive* than an
unconstrained quadratic in `H²`, and this restriction currently costs
fit quality rather than earning any. A bare 3-coefficient polynomial has
no physics attached to it at all — it can bend however the noisy data
wants; MULTING's own curve is constrained by everything else the theory
requires it to be consistent with (the force-law structure, the
evolution laws, the kinematic translation). That MULTING's more
constrained curve does not currently win, at equal `k`, is informative
about the SPECIFIC parametrization tested here — not a verdict on
whether cluster-gravity forces exist in nature.

## 1. Method — real data, real fit, not symbolic derivation

Unlike `P156`-`P166` (mostly symbolic/textual analysis), this file runs
an actual weighted least-squares fit (`scipy.optimize.curve_fit`,
equal-in-spirit to `χ²` minimization) against real external data.

**Model tested:** `H(z)² = Y0 + Y1·z + Y2·z²` — three free coefficients,
no physical interpretation attached to any of them. Chosen because it
mirrors the `Y≡H²` convention this project's own machinery already uses
throughout `FINDING_P161`/`P165`, making it a natural, non-arbitrary
"emptied out" analogue: same target variable, same polynomial-in-`z`
spirit as many phenomenological cosmology parametrizations, zero physical
content.

**Data:** the same 33 points v82 itself fits against — 31 Cosmic
Chronometer points (§ below) plus v82's own quoted SH0ES
(`z=0.0233, H=73.04±1.04`) and DESI DR2 Lyman-α (`z=2.33, H=236.1±2.8`)
points, both already used and verified in `FINDING_P163`/`P165`/`P166`.

**Two comparison regimes**, matching `FINDING_P166`'s own extraction from
v82's Table II exactly:
1. **Unconstrained** (`k=3`, all three coefficients free) vs. MULTING's
   own unconstrained fit (`χ²=15.75`, Table II row "(unconstrained)").
2. **SH0ES-anchored** (`k=2`, `Y0` fixed so `H(z=0)=73.04` exactly,
   mirroring MULTING's own `H0,anchor=73.04` constraint) vs. MULTING's
   own SH0ES-anchored fit (`χ²=15.78`, Table II row "(SH0ES exactly)").

## 2. Data provenance — `[VERIFIED-arXiv]`, cross-checked, not assumed

The 31-point Cosmic Chronometer compilation was fetched and cross-checked
against **two independent primary sources**, both read from raw source
(LaTeX), not summarized:

- Gómez-Valent & Amendola, JCAP 1804 (2018) 051, `arXiv:1802.01505`
  (unnumbered table, Sect. 2, "The data sets").
- Yu, Ratra & Wang, ApJ 856, 3 (2018), `arXiv:1711.03437`, Table 1
  (rows flagged method "a").

**31 of 31 rows independently confirmed matching on `(z, H(z))`.** 30 of
31 rows also match exactly on `σ_H`. One row (`z=0.47`) shows a genuine
printed discrepancy in `σ_H` (source A: `49.6`; source B: `50.0`) — not
silently resolved by picking one value; handled explicitly in §3.

## 3. Sensitivity check on the one flagged discrepancy

`[VERIFIED-python]`, `run_comparisons()` executed twice, once with each
`σ_H` value at `z=0.47`: `χ²` for both dummy-model regimes (unconstrained
and anchored) changes by less than `0.001` between the two choices —
this single row's uncertainty on which of two very close reported values
to use does not affect the result at any decimal place that matters.

## 4. Why the "more constrained" framing matters, and its own limits

The result reads, at first glance, as unfavorable to MULTING. The more
precise, fairer reading (§0): a bare polynomial's `k=3` and MULTING's
`k=3` are **not equally constrained kinds of flexibility** — the
polynomial can bend to fit anything with 3 numbers; MULTING's `k=3`
buys curve-bending ability only within whatever shapes its own physical
force-law structure permits. This is exactly `FINDING_P166`'s own §0
point about parameter-count asymmetry, now demonstrated numerically
rather than argued qualitatively: a naive equal-`k` comparison already
under-credits MULTING for its own structural constraints, in the sense
that a "fair" comparison arguably ought to correct for *effective*
flexibility, not just nominal parameter count. What this file adds is a
concrete number: on this specific comparator and this specific dataset,
that structural constraint currently costs MULTING roughly `1.7` `χ²`
units relative to the least-constrained alternative — a small but
nonzero, directly measured cost.

**What this does NOT prove:** that MULTING's own specific functional
form is a poor choice among *physically motivated* alternatives — only
that it does worse than a functional form with *no* physical constraints
at all. A different, still-physical modification to gravity (e.g. one of
the models found in today's earlier `negative-space-miner` literature
search, like `Λ_ωsCDM`) might do better or worse than both; this file
does not test that.

## 5. What this file does NOT establish

1. **Not a claim about v82's own theory being wrong** (`NO_AUTHOR_ERROR`,
   §0) — a physically-empty comparator outperforming a physically-
   constrained one is not evidence the physical constraints are false,
   only that they are not currently earning their own keep on this
   specific dataset, with this specific comparator.
2. **Tests only ONE "physically empty" functional form** (a bare
   quadratic in `H²`) — a different empty comparator (a different-degree
   polynomial, a rational/Padé form, a different variable transform)
   might fit better or worse; this file does not survey the space of
   possible empty comparators, only checks the single, natural one this
   project's own `Y≡H²` convention suggests.
3. **Does not use Bayesian evidence / Bayes-factor machinery** — the
   field's own preferred tool for exactly this question, per today's
   `negative-space-miner` literature search — only the simpler χ²/AIC/BIC
   framework `FINDING_P166` already used, for direct comparability.
4. **Does not quantify uncertainty on the dummy model's own best-fit
   parameters** — only point-estimate χ² comparisons, matching the level
   of rigor `FINDING_P166`'s own numbers (MULTING's own reported point
   values) already operate at.
5. **Does not re-examine whether MULTING's own currently-fixed inputs**
   (`f_coh`, accretion sign, `T_0` — `FINDING_P166` §0) would, if allowed
   to vary, change this comparison — a fuller accounting of MULTING's own
   true effective flexibility could shift this result in either
   direction, not attempted here.
6. **Does not establish which error-weighting convention v82's own
   `χ²=15.75/15.78` actually used** (skeptic-caught, correction above) —
   whether MULTING's own reported numbers assume independent, diagonal
   errors between the 31 Cosmic Chronometer points (matching this file's
   own treatment) or a full covariance matrix accounting for their known
   shared systematics is not stated in v82's own text and not resolved
   here. Given the reported margin is small (`~11%` of MULTING's own
   `χ²`), this is a live, unresolved possibility that could close or
   reverse this file's own comparison — the natural next check, not
   attempted in this session.
