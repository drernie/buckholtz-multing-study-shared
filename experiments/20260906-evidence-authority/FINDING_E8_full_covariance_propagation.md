# FINDING E8 — propagating the cosmic-chronometer covariance: the
# `(β₁,β₂)` degeneracy this project reported is `4-7.6×` more severe than
# stated; the dataset does not discriminate MULTING from free ΛCDM in
# either direction; and a sub-noise "sign flip" that looked like a
# result was demoted by the skeptic's own kill test

**Date:** 2026-09-06
**Claim:** `CLAIM_E8_full_covariance_propagation.md` (pre-registered)
**Scripts:** `E8_full_covariance_propagation.py` (pre-registered),
`E8b_reoptimize_under_covariance.py` and `E8c_drop_non_moresco_points.py`
(**post-hoc**, added in response to results and to the Step 8a skeptic —
labelled as such throughout).
**Continues:** `FINDING_E5`, which named this "the separate, unrun
computation."

## Controls — all pass

| control | result |
|---|---|
| PC1: diagonal χ² reproduces TJB's Table II (2 rows) | `<0.1%` |
| PC2: diagonal χ² reproduces TJB's own ΛCDM benchmarks — fixed `36.955` vs `36.96`, free `16.313` vs `16.31` | `0.015%`, `0.016%` |
| PC3: covariance path with modelling terms zeroed `==` diagonal path | `<1e-9` |
| PC4: every covariance Cholesky-factorizes (SPD) | pass |
| Moresco-point identification: `(z,H)` match against his own BC03 table | exactly `15` of TJB's `31` |
| E8b PC: re-optimising under diagonal recovers TJB's own optima — free ΛCDM `16.313 @ (71.83, 0.2724)`, MULTING not worse than its own start | pass |

PC2 is worth a sentence: matching TJB's own two ΛCDM benchmark χ² to
`0.02%` proves the 33-point dataset and both model functions here are
identical to his, so every difference below is attributable to the error
treatment alone.

## Covariance construction — Moresco's, verbatim

From his own notebook (`examples/CC_covariance.ipynb`, cells 10-12):
`C = diag(errHz²) + Σ_k outer(H·x_k, H·x_k)`, `x_k` = `data_MM20.dat`
percentages interpolated to the data redshifts; **his default**
`k ∈ {spsooo, imf}` (mean `4.53%` + `0.36%` of `H`). The modelling terms
are rank-1 outer products — `100%` correlated across redshift, as his
README states. SH0ES and DESI keep their own diagonal errors.

## Result 1 (Endpoint 2, pre-registered) — the degeneracy is much worse
## than `P176`/`P190` reported. **MATERIAL. The lead finding for this
## project's own work.**

Hessian of χ² in `P176`'s rescaled `(β₁,β₂)` coordinates at TJB's
spotlighted row:

| error model | small eig | large eig | ratio | null slope `dβ₂/dβ₁` |
|---|---|---|---|---|
| diagonal (`P176`, everyone) | `70.60` | `588 321` | `8 334` | `6.073e7` |
| Moresco default, all 31 correlated | `17.46` | `534 741` | `30 636` | `6.110e7` (`+0.6%`) |
| Moresco default, his 15 only | `23.72` | `546 440` | `23 037` | `6.103e7` (`+0.5%`) |
| stress `[sps+imf]`, all 31 | `9.27` | `532 244` | `57 424` | `6.114e7` (`+0.7%`) |

- Small eigenvalue drops by **`4.0×`** (Moresco default) to **`7.6×`**
  (stress) — pre-registered MCID was a factor `2`. **MATERIAL.**
- The large eigenvalue drops only `9%`. **This is not a rescaling** — if
  it were pure error inflation, both would shrink together. The
  covariance flattens the surface *along one direction*: the near-null
  one. The condition number rises from `~8 000` to `~30 000-57 000`.
- The null slope is unchanged to `<1%`: **`P190`'s finding about the
  degeneracy's *direction* (approximate, not exact; `12.7%` variation
  across `z`) is untouched. Its finding about *severity* was understated
  by a factor of 4-8.**
- Direct consequence, stated not run: `P191`-`P194`'s Fisher forecasts
  (how much synthetic high-`z` data would break the degeneracy) were
  computed against a baseline `4-8×` too optimistic. Their *relative*
  conclusions (which `z`-windows are most informative) plausibly survive;
  their *absolute* shrinkage numbers need rerunning against this
  baseline. Flagged as the next step, not done here.

## Result 2 (Endpoint 1, pre-registered) — vs fixed Planck ΛCDM:
## NOT MATERIAL, and the reason is structural

`Δχ² = χ²(ΛCDM fixed) − χ²(MULTING spotlighted)`: `21.20 → 20.88`
(change `0.32`, MCID `2.0`). A per-point decomposition (post-hoc, run
at the skeptic's request) shows why nothing could have moved it:

| contribution to the `21.20` gap | value |
|---|---|
| 31 CC points | **`−0.76`** (CC alone slightly favours *fixed ΛCDM*) |
| SH0ES (`z=0.0233`, `σ=1.04`) | **`+22.03`** |
| DESI | `−0.07` |

**The entire advantage over fixed-Planck ΛCDM is one data point.** Fixed
ΛCDM at `H₀=67.4` predicts `H(0.0233)≈68.2` against SH0ES's
`73.04±1.04` — the Hubble tension expressed as a single χ² term. This is
not a discovery: v82 says so itself (*"fixed ΛCDM is not permitted to
respond to SH0ES at all, and pays a heavy, avoidable price in χ²"*, its
§II.G). The decomposition quantifies his own sentence: `22.03` of `21.20`.
A CC-only covariance cannot touch a SH0ES-only gap, whatever its size.

## Result 3 (Endpoint 1 vs *free* ΛCDM) — a sign flip that the
## skeptic's kill test demoted. Reported in full, not smoothed over.

**What E8 found (pre-registered comparison, fixed parameters):**
`Δχ² = χ²(free ΛCDM) − χ²(MULTING)` goes from `+0.561` (diagonal) to
`−0.28 / −0.51 / −0.34` under the three covariance variants. Sign flip →
MATERIAL by the pre-registered criterion.

**E8b (post-hoc): does it survive re-optimising both models under the
covariance?** Yes: `−0.375 / −0.648 / −0.116`, convergence checked from
three starting rows. Mechanism (skeptic's, confirmed by decomposition):
MULTING's CC residual has **`0.0%`** of its power along the coherent
`∝H` direction — the one direction a rank-1 term frees — so its χ²
barely moves (`15.751→15.717`); free ΛCDM at `H₀=71.83` sits below the
CC-preferred normalisation, has a coherent component, and gains
`~0.97`. `Δ(Δχ²)≈0.94`, matching the observed swing.

**E8c (post-hoc, the skeptic's pre-stated kill criterion, adopted
verbatim):** *"if restricting to Moresco's own 15 points restores the
positive sign, the flip was manufactured by extending his fractions to
16 points where they don't apply."*

| variant | N | `Δχ²` (ΛCDM* − MULT*) |
|---|---|---|
| REF: 33 points, diagonal | 33 | `+0.561` |
| DROP to Moresco's 15 + anchors, diagonal | 17 | `+2.636` |
| DROP, Moresco default covariance | 17 | **`+1.205`** |
| DROP, stress covariance | 17 | **`+1.263`** |
| ZERO: 33 points, cov on his 15, *nothing* on the other 16 | 33 | `−0.934` |
| ZERO, stress | 33 | `−1.272` |

**Kill criterion outcome: `2/4` Moresco-only variants restore the
positive sign — the two that use only his points.** On the 15 points his
covariance is actually calibrated for, MULTING keeps a positive edge
under his own covariance; the covariance *reduces* it (`+2.64→+1.2`) but
does not flip it. The flip appears only when the 16 non-Moresco points
are present — and the DROP-diagonal row shows why: those 16 points, on
their own, pull `Δχ²` from `+2.64` to `+0.56` (they favour free ΛCDM
relative to MULTING). Any error model that lowers Moresco's 15 relative
to those 16 then tips the sum negative. **E8's sign flip is
substantially a *reweighting between two CC sub-samples that disagree*,
not a clean covariance effect.** C1 is **WEAKENED** to a footnote.

## The result that actually survives everything (C4)

Every `|Δχ²|` between MULTING and freely-optimised flat ΛCDM, across
every defensible choice — which points, which error model, re-optimised
or not — lies in `[−1.27, +2.64]` on `15-31` degrees of freedom. **The
33-point dataset does not discriminate between them, in either
direction.** v82's own wording ("edges it out, though narrowly rather
than substantially") and this file's initial "the edge reverses" are
*both* readings of a sign inside the noise floor. The variance across
defensible analysis choices (`~3.9`) exceeds the effect (`~0.5`).

## Corrections to the pre-registration, stated

1. **The negative control's premise was wrong.** It predicted a `100%`
   fully-correlated modelling term would "collapse discrimination". It
   did not (spread `32.02→32.02`), for two reasons now understood: a
   rank-1 term frees exactly one direction in residual space, leaving
   shape differences fully penalised; and the model-to-model gap lives
   in SH0ES (Result 2), outside the CC block entirely. PC3 (`<1e-9`
   equality with modelling terms zeroed) rules out the alternative
   explanation that the modelling term silently failed to enter. **A
   control that tests the wrong lever is a design error, not evidence of
   a bug** — recorded as such.
2. E8b and E8c were **not** pre-registered. E8b was added after seeing a
   sign flip (to check it against re-optimisation); E8c was added at the
   skeptic's direction. Both are labelled post-hoc in their own
   docstrings.
3. The skeptic's structural point is adopted: Results 1, 3 and the
   negative-control non-collapse are **one phenomenon** (a rank-1
   covariance downweights the coherent-`H` direction) seen from three
   angles — the count of independent findings here is closer to `1.5`
   than `3`.

## What this does NOT establish

1. **Nothing about which model is right.** `|Δχ²|<3` on these dof is not
   evidence for either; this file demotes its own sign-flip finding for
   exactly that reason.
2. Does not rerun `P191`-`P194` against the corrected degeneracy
   baseline — named as the next step.
3. Does not settle whether Moresco's fractions apply to the 16
   non-Moresco points. It shows the answer *matters* for the sub-noise
   sign, which is itself a reason not to lean on that sign.
4. Interpolation clamp: `data_MM20` ends at `z=1.475`; CC points to
   `1.965` get the systematic frozen at its `z=1.475` value. Likely
   *under*-estimates high-`z` systematics — conservative for every
   direction reported here (skeptic, confirmed).
5. `NO_AUTHOR_ERROR`. Result 2's decomposition *agrees* with v82's own
   stated reading of its fixed-ΛCDM benchmark; Result 3's demotion means
   this file makes **no** claim that v82's free-ΛCDM comparison is wrong
   — only that neither its sign nor its reverse is resolvable here.
