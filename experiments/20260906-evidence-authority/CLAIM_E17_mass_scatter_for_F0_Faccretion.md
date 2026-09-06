# CLAIM E17 — measure a real, sourced population scatter for `M(z)`,
# to close `E16`'s own Pearl Registry Caveat Gate entry (`F0`/`F_accretion`
# also nonlinear in `M(z)`, un-scoped by `E16`'s `F1,F2`-only correction)

**Date:** 2026-09-06 (pre-registered before any numeric result)
**Continues:** `FINDING_E16` (identified the gap), `E13` (the methodological
template — measure a real scatter, don't assume one), `P196_addendum_
concentration_scatter.py` (this project's own existing Duffy+2008 Monte
Carlo machinery, reused here, not reimplemented).

## EstimandOps L0

**Descriptive** — "what does the real, published literature say about the
scatter in cluster halo mass accretion histories at the mass/redshift
range this project's own `M_of(z)` targets," not a causal claim.

## Why `M(z)` is a different kind of question than `E13`'s `M_gas`

`[VERIFIED-CODE]` `P176`'s own `M_of(z) = M0_kg * (1+z)**(-1.1)` is not a
fit to a real scaling relation the way `M_gas(T)` is (`E13`'s target). Per
`E9`'s own provenance chain, it is v82's own **Class II, "retained-
theoretical"** input (v82.md:582-583: "an FLRW-flavored theoretical step,
kept deliberately"), citing refs **[18] Fakhouri, Ma & Boylan-Kolchin
(2010)** and **[19] Zhao, Jing, Mo & Börner (2009)** — real papers,
verified by fetching v82's own bibliography (v82.md:1970-1975) and
matching titles/DOIs against arXiv (`[VERIFIED-arXiv]` `1001.2304`,
`0811.0828`). There is no single "real cluster" whose mass was fit to
produce `-1.1` — it is an assumed functional form for a population's
*median* mass accretion trajectory. The relevant scatter is therefore not
"scatter in a fitted parameter" but **"how much do individual real
cluster mass histories spread around whatever `M(z)` represents as
typical"** — the same distinction v82's own §IV limitation (quoted in
`E15`'s claim) names directly: "a single representative value... not a
scattered population."

## What the two directly-cited references actually contain

`[VERIFIED-arXiv]` Neither v82's own cited ref gives a directly quotable
scalar `σ`:
- **Zhao et al. (2009)**, `0811.0828`: states directly, "individual MAHs
  show a log-normal distribution (D. H. Zhao et al. 2010, in
  preparation)" — confirms the functional FORM (log-normal, matching
  `E13`'s own convention) but defers the actual number to an unpublished
  follow-up not locatable on arXiv.
- **Fakhouri, Ma & Boylan-Kolchin (2010)**, `1001.2304`: reports mean
  merger rates/growth rates, not halo-to-halo `M(z)` scatter.

## The real, quotable source found

**Correa, Wyithe, Schaye & Duffy (2015)**, "The accretion history of dark
matter halos II," `arXiv:1501.04382` — cites the SAME Duffy et al. (2008)
concentration-mass relation this project's own `P196_addendum_
concentration_scatter.py` already uses (`σ(log10 c200)=0.15`,
`[VERIFIED-arXiv:0804.2486]`), and derives (their Appendix B, eqs. 46-51)
an explicit, N-body-validated **error-propagation model connecting
concentration scatter → formation-redshift scatter → fractional `M(z)`
scatter**: `M(z) = M0·(1+z)^α·exp(β·z)`, `β=-3/(1+z_{-2})`,
`α=[ln(Y(1)/Y(c)) - β·z_{-2}]/ln(1+z_{-2})`, `Y(x)=ln(1+x)-x/(1+x)`,
`z_{-2}` (formation redshift) from `c` via their eq. 49. They validate
this model against real N-body simulation output ("we find very good
agreement" between the analytic estimate and the simulated scatter).

## Method (Monte Carlo, reusing this project's own established pattern)

1. Draw `c ~ LogNormal(log10(c_median(M0,z=0)), σ=0.15)` — Duffy+2008's
   own quoted scatter, the EXACT distribution `P196_addendum_
   concentration_scatter.py` already draws from (imported, not
   reimplemented).
2. For each draw, compute `z_{-2}(c)` **deterministically** via Correa's
   own eq. 49 (their own median relation) — an explicit, stated
   simplification: Correa's own fuller analysis (their §B.0.1) finds
   `z_{-2}` carries some scatter *not* fully explained by `c` alone
   (driven, per their own words, by the underlying mass-history scatter
   itself — a partial circularity in their own error budget). Using only
   the `c`-driven channel gives a **lower-bound-flavored partial
   estimate**, the same honest framing `E13`/`E15` already established
   for this project's own convention.
3. Compute `α(c,z_{-2}(c))`, `β(z_{-2}(c))`, then `M(z)/M0` for each draw,
   at `E15`'s own `REAL_DATA_ZS = (0.07, 0.25, 1.00, 2.00, 2.33)`.
4. **[Found while running, not assumed in advance]** Correa's own eq. 50
   for `α` has a genuine mathematical singularity as `z_{-2}→0`
   (`ln(1+z_{-2})→0` in the denominator, numerator generically nonzero) —
   verified directly: draws with `z_{-2}∈[0,0.05)` give `α` ranging from
   `-6747` to `+0.26`. This is a real feature of the cited model at low
   concentration, not an implementation bug. `np.std` on such a
   distribution is unusable (blows up / NaNs from `log(0)`). **Report
   `σ_ln(M(z))` as `(P84−P16)/2`** — a percentile-based spread, matching
   Correa+2015's OWN reporting convention for their own Figures 8/12/13
   ("the error bars to 1σ confidence limits and the grey area to the
   scatter" — a percentile band, not a literal variance), and immune to
   the singular tail. Draws with unphysical `z_{-2}<0` are excluded
   explicitly (`5.6%` of `200,000` draws) and the excluded fraction is
   reported, not hidden.
5. Propagate through `F0 ∝ M²` (`Jensen correction = exp(2σ_ln(M(z))²)`)
   and `F_accretion ∝ M^1.5` (`Jensen correction = exp(1.125·σ_ln(M(z))²)`)
   — the same closed-form Jensen's-gap machinery `E15` already used for
   `F1,F2`, applied to the correct powers of `M`.
6. **Side-finding, not a new claim:** the MEDIAN of `ln(M(z)/M0)` across
   draws is negative and grows with `z` (not `0`) — the typical
   concentration-scattered trajectory runs systematically below the
   deterministic `M0·(1+z)^{-1.1}` curve, an asymmetric,
   Jensen's-gap-flavored effect. Reported alongside the spread, not
   folded into it.

## Falsifiable predicate

`σ_ln(M(z))` from concentration-scatter propagation alone is either
(a) comparable in size to `E13`'s `σ=0.49` (in which case `F0`/
`F_accretion`'s own corrections are of similar order to `F1`/`F2`'s, and
`E16`'s `F1,F2`-only scope is a materially incomplete accounting), or
(b) much smaller (in which case `E16`'s scope gap, while real, turns out
to be numerically minor).

## Pre-registered MCID

**MATERIAL if** the resulting `F0`/`F_accretion` Jensen corrections
exceed `10%` at any of `E15`'s own `REAL_DATA_ZS` — reusing `E15`'s own
threshold, for direct comparability.

**[Added after Step 8a Pass 2, WEAKENED verdict, applied in place]** the
single combined number this claim originally proposed
(`E[Mⁿ]/M_ref(z)ⁿ`) conflates two physically distinct effects: a real
**systematic offset** between v82's own assumed `M(z)=M0·(1+z)^{-1.1}`
and Correa's real MAH model (large, up to `~5×` at `z=2.33`, but NOT a
scatter/Jensen effect), and the actual **Jensen scatter correction**
(`E[Mⁿ]/E[M]ⁿ`, much smaller). **The MCID applies to the Jensen
component only** — the quantity this claim was actually asked to
measure, per `E16`'s Pearl Registry entry. The offset is reported
separately as a real, notable side-finding, not folded into the MCID.

## Controls

- **Positive control 1 (zero scatter):** `σ(log10 c)→0` must give
  `σ_ln(M(z))=0` at every `z` exactly.
- **Positive control 2 (z=0 boundary):** `σ_ln(M(z=0))` must be exactly
  `0` regardless of concentration scatter — `M(z=0)≡M0` by construction
  (every draw shares the same `M0`, only the trajectory AWAY from it
  varies), independent of the scatter model.
- **Positive control 3 (reuse check):** the Monte Carlo concentration
  distribution must reproduce `P196_addendum_concentration_scatter.py`'s
  own `duffy2008_concentration_median` output exactly at zero scatter —
  confirms no re-implementation drift.

## What this claim does NOT say

1. Does not claim this is the FULL `M(z)` scatter — only the
   concentration-driven channel (see Method, step 2's stated
   simplification). A real, named, un-closed gap remains: the
   independent formation-time-scatter channel Correa's own paper
   identifies but does not fully decompose numerically in the text this
   project could extract.
2. Does not re-derive `E16`'s own `(β1,β2)` closed-form result — this is
   a separate scope, feeding a potential future extension of it.
3. `NO_AUTHOR_ERROR` — measuring a real published scatter for a
   theoretical input v82 itself labels "retained-theoretical," not a
   claim about v82's own correctness.

## `[Added by FINDING_E17_ADDENDUM_validated_against_correa2015.md]`

This project's own `M0=6.0×10^14 M_☉` is `6×` above Duffy et al. (2008)'s
own stated calibration ceiling (`10^14 M_☉`) for the concentration-mass
relation this claim's Monte Carlo depends on. `A_cosmo=798` and the
`Ωm/ΩΛ` choice are both confirmed correct/negligible; this specific
extrapolation is not. Concentrated at high `z` (`z=2.00, 2.33`, per
Correa's own model-comparison discussion) — exactly where the Jensen
correction was found `MATERIAL`. Magnitudes at those two points carry
more uncertainty than the Monte Carlo convergence check alone showed;
direction and the `z≤0.25` points are less affected.
