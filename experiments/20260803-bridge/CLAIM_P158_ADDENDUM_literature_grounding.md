# CLAIM — P158 addendum: literature-ground the two open unknowns

**Date:** 2026-09-02
**Trigger:** user explicit go-ahead to start "the real finite-r derivation"
named in `docs/153` §3a; redirected (with the user's approval, see the
approved plan) from a literal re-derivation of the S-S closure at finite
`r` toward literature-grounding `FINDING_P157`/`P158`'s more precise,
already-skeptic-reviewed reframing of the same underlying bottleneck.
**Scope, explicitly bounded:** this does NOT re-derive anything new
mathematically — `FINDING_P158`'s Jensen's-inequality machinery
(`jensen_enhancement_symbolic`, `jensen_enhancement_correlated` in
`P158_jensen_mass_averaging_v82_force_terms.py`) is reused unmodified. The
only new work is: (a) find real, cited astrophysical values for the two
inputs P158 left illustrative/unknown, (b) re-evaluate P158's own formulas
at those real values, (c) report honestly whether this resolves P158's
`CONDITIONAL-DIRECTIONAL-PREDICTION` verdict.
**L0:** descriptive — "what does the published literature say about two
specific numbers" is not a new causal or physics claim about MULTING/v82.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR

---

## The two falsifiable sub-questions

**(a) Mass-observable scatter.** What does real, published literature
report for cluster mass–observable scatter (a `σ_lnm`-equivalent) at a
mass/redshift range comparable to v82's own target
(`~5–6×10¹⁴ M_☉`, `0.07 ≲ z ≲ 2`, per `FINDING_P155`'s context and v82's
own Table III z-values)? `FINDING_P158`'s own illustrative table used
`σ_lnm = 0.2–0.7` with no citation — is a real, sourced value inside,
outside, or spanning that range?

**Falsifier:** if no real source addressing this mass/redshift range is
found, the sub-question is `SOURCE_NOT_FOUND` — reported as such, not
filled in from memory or a plausible-sounding guess.

**(b) Mass correlation between paired nodes.** What does real, published
literature say about the sign of log-mass correlation (`ρ`) between
paired, interacting, or nearby halos — "mass assortativity" in cosmic-web
connectivity — at a separation scale comparable to v82's own node pairs
(~40–45 Mpc)? `FINDING_P158` §2.1 derived `ρ > −0.5` as the exact
threshold above which its `F^(2) > F^(1)` enhancement ordering holds, and
named this as a real, studied effect in cosmic-web literature, not
checked there.

**Falsifier:** if the literature reports `ρ < −0.5` (or `ρ < −0.7467`, the
second, more negative threshold at which even `F^(1)`'s own enhancement
crosses below 1 — see `P158` §2.1) for a comparable regime, `P158`'s
directional claim is reversed, not merely left conditional. If literature
addresses `ρ`'s sign but not its magnitude relative to these exact
thresholds, report the sign alone with an explicit note that the
magnitude comparison remains unresolved.

## Positive control

Before trusting any new numeric evaluation: re-run `P158_jensen_mass_
averaging_v82_force_terms.py`'s own existing test suite
(`test_jensen_positive_controls`, `test_correlated_recovers_independence_
case`, `test_correlation_threshold`, `test_monte_carlo_matches_analytic`,
`test_monte_carlo_matches_correlated_analytic`) unmodified — if any of
these fail, the machinery itself is not to be trusted, and no new
evaluation with real inputs should be reported.

## Negative control

Evaluate `jensen_enhancement_correlated` at a deliberately wrong `ρ` value
known to reverse the ordering (`ρ = −0.9`, well below the `−0.7467`
threshold) and confirm `F^(1)` and `F^(2)` enhancements both fall below
their `ρ=0` baseline, and `F^(2) < F^(1)` — i.e. the calculation actually
responds to the sign of `ρ`, not a fixed output regardless of input.

## What this does NOT establish

1. Not a re-derivation of P158's own Jensen's-inequality mechanism, which
   stands unchanged — this only supplies real inputs to an already-built,
   already-verified formula.
2. Not a claim that resolves `docs/153`'s 3 pre-conditions outright — at
   best this narrows pre-condition 3's cost/consequence question with a
   real, evidence-grounded number instead of an illustrative one.
3. Not a re-fit of v82's own `β₁`, `β₂`, `H₀,anchor` — out of scope, same
   as `P158` itself already stated.
4. If literature is silent or ambiguous on either sub-question, this does
   NOT manufacture a verdict — `SOURCE_NOT_FOUND` / "remains conditional"
   is a legitimate, honestly-reported outcome, not a failure to avoid.

## Artifacts

- This file.
- `FINDING_P158_ADDENDUM_literature_grounding.md` — the write-up.
- Reused unmodified: `P158_jensen_mass_averaging_v82_force_terms.py`.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
