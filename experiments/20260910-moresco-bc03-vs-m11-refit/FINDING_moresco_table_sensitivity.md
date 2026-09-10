# FINDING — Moresco BC03-vs-M11 table swap: MATERIAL by chi2 on the full
# 15-point dataset, NOT MATERIAL on its 13 tightest-agreeing points; the
# split traces to Moresco et al. 2012's own self-flagged 1.6-sigma
# BC03-vs-M11 point, real data not a confound; H0,anchor barely moves
# either way; survives full-covariance propagation unchanged

**Date:** 2026-09-10
**Continues:** `FINDING_E5_class_I_carries_quantified_model_dependence.md`
(2026-09-06), whose own "What this does NOT establish" #1 named this exact
computation as unrun: "Whether propagating the full covariance [or table
swap] changes v82's conclusions is a separate, unrun computation."
**Trigger:** directly answers Dr. Buckholtz's own question, email
2026-09-09 ("thank you, plus follow-up discussion"): *"Do you think that
changing from one table to the other would significantly impact the
'Results'-section results or other aspects of my work or paper?"*

`NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * L0 descriptive`
`NO_AUTHOR_ERROR` — this tests this project's own reconstruction of v82's
published fit against a real, external, alternate input table. Not a claim
about which table TJB should use, and not a claim about v82 itself.

## L0 (EstimandOps)

**Question type: descriptive.** Does swapping Moresco's BC03 table for the
M11 table, holding everything else in the 31-point fit fixed, change the
fitted `(H0_anchor, beta1, beta2)` and chi2 of this project's own
reconstruction of TJB's `chi2_fixed_h0anchor` machinery by more than the
project's own pre-registered MCID (`Delta_chi2 >= 2.0`,
`CLAIM_E8_full_covariance_propagation.md`)?

## Positive control — PASS

Reusing `CC_POINTS`/`TABLE_II`/`chi2_fixed_h0anchor`/`z33`/`H33`/`s33`/
`ZFINE` verbatim from `experiments/20260803-bridge/
P176_v82_real_chi2_hessian_degeneracy.py` (already positive-control-verified
elsewhere in this project to reproduce TJB's Table II to <0.1%) and the
rescaled Nelder-Mead `opt_multing()` pattern from `experiments/20260906-
evidence-authority/E8b_reoptimize_under_covariance.py`:

Refitting under the **unmodified BC03** data, starting from TJB's own
`"unconstrained_spotlighted"` values, gives
`chi2=15.7515` at `H0_anchor=73.216, beta1=1.4335e10, beta2=7.8067e17`
against TJB's own published `chi2=15.75, H0_anchor=73.22, beta1=1.4335e10,
beta2=7.8067e17` — matches to `<=0.01` in chi2, well inside rounding.

## Method

1. Live-fetch both real Moresco tables (`gitlab.com/mmoresco/CCcovariance`,
   `HzTable_MM_BC03.dat`, `HzTable_MM_M11.dat`), HTTP 200 both.
2. Identify which 15 of TJB's own 31 `CC_POINTS` are Moresco/BC03-sourced
   by `(z, H)` match against the live BC03 table (tolerance matches
   `FINDING_E5`'s/`E8`'s own `moresco_mask` convention). Matched 15/15.
3. For each matched point, substitute the M11 table's `H(z)` at the same
   redshift (max `|z|` mismatch between the two tables' own grids:
   `0.0004` — confirms `FINDING_E5`'s own positive control that both
   tables share an identical z-grid). Keep `sigma_Hz`, all 16 non-Moresco
   CC points, and SH0ES/DESI anchors unchanged — isolates the central-value
   shift only, does not re-derive the error budget.
4. Re-optimize `(H0_anchor, beta1, beta2)` under the swapped data with the
   same rescaled Nelder-Mead, restarting from 3 independent `TABLE_II` rows
   (`unconstrained_spotlighted`, `sh0es_anchored_0pct`,
   `planck_exact_100pct`) per `E8b`'s own convergence-check convention.

## Result 1 — per-point shift cross-validates FINDING_E5 exactly

`[VERIFIED-REAL]`, computed live this session, not reused from memory:

| n | mean shift | range |
|---|---|---|
| 12 (uniform) | `+6.98%`* | `+4.93%` to `+7.64%` |
| 2 (large excursions, `z=0.7812`, `z=1.037`) | `-21.1%` | `-15.75%` to `-26.48%` |
| 1 (small excursion, `z=0.875`) | `-0.64%` | — |

*mean of the 12-point cluster only; the earlier combined mean/median printed
by the main script (`2.47%`/`6.68%`) mixes all 15 points including the 3
excursions — the large mean/median gap on first run was the tell that
triggered this per-point check rather than trusting the aggregate.

This reproduces `FINDING_E5`'s own numbers (12 points at a tight uniform
`+6.80%`, spread `0.99`pp; 2 large negative excursions at exactly these
same two redshifts) to within rounding, computed independently four days
later from a fresh live fetch — a real, unplanned cross-validation of that
earlier finding, not just of this new computation.

## Result 2 — full 15-point swap: MATERIAL by chi2, but not robustly

Convergence check passed: all 3 independent restarts land on the identical
optimum (`chi2=21.6613`, spread `0.0000`across starts) — a real global
optimum, not a local-minimum artifact.

| | BC03 (positive control) | M11 (all 15 swapped) |
|---|---|---|
| chi2 | `15.7515` | `21.6613` |
| H0_anchor | `73.216` | `73.343` |
| beta1 | `1.4335e10` | `1.1791e10` |
| beta2 | `7.8067e17` | `6.2554e17` |

`Delta chi2 = -5.9099` (i.e. the fit gets **worse**, not better, under
M11 — swapping tables costs `5.91` in chi2). Against the project's own
pre-registered `MCID=2.0` (`CLAIM_E8_full_covariance_propagation.md`):
**MATERIAL.**

`Delta H0_anchor = +0.127 km/s/Mpc` (small). `Delta beta1 = -17.75%`,
`Delta beta2 = -19.87%` (large).

## Result 3 — robustness check: the chi2-MATERIAL verdict is carried almost
## entirely by the 2 points `FINDING_E5` already flagged as unverified

`FINDING_E5` named an explicit, still-open caveat on exactly these same 2
excursion points: *"it was not verified from the artifacts that the fit
method was held fixed between the BC03 and M11 re-analyses at z>0.7. If it
was not, part of those excursions is method difference, not pure SPS
choice."* Since Result 2's MATERIAL verdict could be dominated by exactly
the 2 points carrying that unresolved confound, this reruns the identical
fit substituting M11 **only on the 13 "clean" points**, leaving the 2
flagged excursion points at their original BC03 value
(`robustness_exclude_excursions.py`):

| | BC03 baseline | M11 (13 clean points only) |
|---|---|---|
| chi2 | `15.7515` | `16.3365` |
| H0_anchor | `73.216` | `73.260` |
| beta1 | `1.4335e10` | `1.1067e10` |
| beta2 | `7.8067e17` | `5.8093e17` |

`Delta chi2 = -0.5850` — **well below MCID=2.0: NOT MATERIAL.**
`Delta H0_anchor = +0.044 km/s/Mpc` (even smaller than Result 2).
`Delta beta1 = -22.79%`, `Delta beta2 = -25.58%` — **larger** in percentage
terms than the full-15-point swap, despite the chi2 shift shrinking by a
factor of 10.

**Reading this pattern honestly:** chi2 materiality in Result 2 is carried
almost entirely by 2 of 15 points with a named, still-unverified
alternative explanation (method difference at high z, not SPS choice).
On the 13 points `FINDING_E5` itself called the trustworthy, load-bearing
part of the finding (the tight uniform `+6.80%` cluster), the chi2-based
verdict flips to NOT MATERIAL. Simultaneously, `beta1`/`beta2` shift by
even *more* on the clean-13-point-only swap than on the full swap — a chi2
surface that barely moves while a fitted parameter swings by a quarter of
its own value is consistent with (not new proof of, but not contradicting)
this project's own previously-established `beta1`/`beta2`-vs-`H0_anchor`
degeneracy in `chi2_fixed_h0anchor` (named directly in `P176`'s own
filename, "hessian degeneracy") — a flat direction in parameter space lets
`beta1`/`beta2` move substantially for very little chi2 cost.

## Result 4 — same two checks re-run under Moresco's own FULL, correlated
## systematic covariance (not just diagonal sigma_Hz): verdict unchanged
## either way

Diagonal `sigma_Hz` (used in Results 1-3) is known, per `FINDING_E5`, to
exclude the SPS/modelling systematic entirely — Moresco's own README calls
that component "fully correlated across redshift" and it lives only in
`Cov_model`, not in the quoted error column. This re-runs both the full
15-point swap and the 13-clean-point robustness check using the actual
`Cov_model` recipe (`spsooo+imf` components, Moresco's own default),
reusing the already positive-control-verified machinery from
`experiments/20260906-evidence-authority/E8_full_covariance_propagation.py`
and `E8b_reoptimize_under_covariance.py` verbatim
(`full_covariance_bc03_vs_m11.py`, `full_covariance_robustness_exclude_
excursions.py`). Two covariance variants tested, matching E8's own
convention: correlated only among the 15 Moresco points, vs correlated
across all 31 of TJB's CC points.

| | Diagonal (Results 1-3) | Full cov, his-15-correlated | Full cov, all-31-correlated |
|---|---|---|---|
| **Full 15-point swap** Delta chi2 | `-5.910` | `-6.066` | `-5.943` |
| verdict | MATERIAL | MATERIAL | MATERIAL |
| **13-clean-points-only** Delta chi2 | `-0.585` | `-0.628` | `-0.602` |
| verdict | NOT MATERIAL | NOT MATERIAL | NOT MATERIAL |

**The full-covariance treatment changes almost nothing about the qualitative
picture.** Every Delta chi2 above sits within ~3% of its diagonal-only
counterpart; every verdict (MATERIAL / NOT MATERIAL) is unchanged by
switching from diagonal to full covariance, in both covariance-structure
variants tested. `Delta H0_anchor` stays small throughout (`+0.05` to
`+0.14 km/s/Mpc`); `beta1`/`beta2` shifts stay in the same `13-26%` band.
Positive controls: diagonal chi2 at TJB's own optimum still reproduces his
published `15.75` (`15.7516`, this run); Cholesky factorization of the
full covariance matrix succeeds (SPD) in every variant; convergence checked
across the same 3 independent `TABLE_II` starting rows as Results 1-3, all
converged (`ok`) — matching E8b's own convergence convention.

**What this establishes, concretely:** the crux of whether today's Moresco
sensitivity check reads MATERIAL or NOT MATERIAL was never really about
diagonal-vs-covariance error treatment — it is almost entirely about
whether the 2 excursion points (`z=0.7812`, `z=1.037`) are trusted at face
value, exactly as Result 3 already found. Propagating the correlated
systematic budget (this section's own new work) does not change that
picture in either direction.

## Result 5 — the still-open caveat is now closed: read Moresco et al. 2020
## (arXiv:2003.07362) §3-4, then traced the real chain back to Moresco et
## al. 2012 (arXiv:1201.3609), the actual originating paper for both
## excursion points

`FINDING_E5`'s own named caveat was never actually about the 2020
covariance paper itself — §3-4 there (`[VERIFIED-arXiv:2003.07362]`, read
in full) builds a THEORETICAL bias budget across many candidate SPS
models (confirming the `8.91%` mean/`3.90-15.86%` range figures used
throughout this thread) and does not describe how the specific published
`HzTable_MM_BC03.dat`/`HzTable_MM_M11.dat` values were derived. The real
provenance sits elsewhere: the BC03 table's own `reference` column
(`[VERIFIED-BASH]`, fetched live — a 4th/5th/6th column this project had
not looked at before today) names the source paper per point directly.
Both excursion points trace to **Moresco et al. 2012**
(`[VERIFIED-arXiv:1201.3609]`, read `§3.3`/`§4`/`§5` in full):

- `z=0.7812` and `z=1.037` are both sourced to `Moresco et al. (2012)` —
  along with 5 other, non-excursion points from the same paper
  (`z=0.18, 0.20, 0.59, 0.68, 0.88`), so the paper-of-origin alone does
  not explain the excursion; something specific to these 2 points does.
- §3.3/§4 (`[VERIFIED-arXiv]`) describe ONE fitting procedure (the
  `D4000_n`-age calibration, `A(Z)` slope-interpolation) applied
  identically to BOTH stellar-population models compared in that paper —
  **"BC03" and "MaStro"** — with no redshift-dependent or model-dependent
  switching described anywhere in the method sections. This directly
  answers the open half of `FINDING_E5`'s caveat: **the fit method was
  held fixed.**
- **"MaStro" in the 2012 paper and "M11" in the CCcovariance repository
  are the same model**, confirmed numerically, not by name alone: Table
  1 of the 2012 paper (`§5`) reports BC03/MaStro values of `105/88` at
  `z=0.7812` and `154/113` at `z=1.037` — matching today's live-fetched
  `HzTable_MM_BC03.dat`/`HzTable_MM_M11.dat` values (`104.5/88.04` and
  `153.7/113.0`) to within rounding.
- **The 2012 paper self-reports the exact discrepancy this thread found,
  in its own words**, quoted verbatim: *"The measurements of H(z) have
  proven to be extremely robust even changing between completely
  different stellar population synthesis models: performing the analysis
  separately with the MaStro and the BC03 model, the values obtained are
  in agreement with a mean difference of `0.5±0.4σ`, except for the last
  point where there is a difference of `1.6σ`."* Recomputing that
  significance directly from their own Table 1 (`105±12` vs `88±11` at
  `z=0.7812`; `154±20` vs `113±15` at `z=1.037`, quadrature-combined
  errors): `z=1.037` gives `1.64σ` — an exact match to their own quoted
  `1.6σ` "last point" outlier, confirming this IS the self-flagged point.
  `z=0.7812` gives `~1.04σ`, elevated relative to the paper's own
  `0.5±0.4σ` typical band but not individually singled out in their text.
- The paper's own explanation for why the discrepancy grows at higher
  `z`: *"At higher redshifts, the error increases because of the smaller
  number of observed galaxies in the samples"* — a real, structural,
  sample-size reason, not a hidden methodology change.

**Verdict on `FINDING_E5`'s caveat: CLOSED, not a confound.** The 2
excursion points are not a fit-method inconsistency — they are the
original authors' own real, self-documented BC03-vs-MaStro/M11 sensitivity,
concentrated at their highest-`z`, smallest-sample point (`z=1.037`,
explicitly flagged by them at `1.6σ`). This means today's Result 2 vs
Result 3 split is not "trustworthy data vs a data artifact" — it is
"the full, real dataset including its most SPS-sensitive point" vs "the
subset the original authors themselves would recognize as their most
tightly-agreeing points." Both readings are legitimate; neither is more
"correct" than the other, and this finding does not adjudicate between
them — it only establishes that the split is real, not spurious.

## What this establishes

1. `[VERIFIED-REAL]` A real, live, previously-unrun computation: this
   project's own reconstruction of TJB's fit IS sensitive to the Moresco
   BC03-vs-M11 table choice, in the specific and narrow sense that the
   best-fit `beta1`/`beta2` shift by `18-26%` under either version of the
   swap tested. This is the answer TJB's own question was looking for, and
   it is not zero.
2. `[VERIFIED-REAL]` `H0_anchor` — the number most directly tied to v82's
   own headline framing — is essentially unchanged either way
   (`+0.04` to `+0.13 km/s/Mpc`, against a fitted value of `~73.2`).
3. `[VERIFIED-REAL]` The chi2-based "is this material" verdict is NOT
   robust to the 2 points `FINDING_E5` already flagged — it is MATERIAL
   if those 2 points are trusted at face value, NOT MATERIAL if they are
   set aside. **[UPDATED, Result 5]** Those 2 points are now confirmed
   real, author-acknowledged data (Moresco et al. 2012's own `1.6σ`
   self-flagged BC03-vs-MaStro/M11 discrepancy at their highest-`z`,
   smallest-sample point), not a fit-method confound — so this split is
   "full dataset vs. the original authors' own tightest-agreement
   subset," a legitimate choice either way, not "clean data vs. a
   suspect artifact."
4. `[VERIFIED-REAL]` Result 4: this crux is NOT an artifact of using
   diagonal instead of correlated errors. Propagating Moresco's own full
   systematic covariance (`Cov_model`, `spsooo+imf`, both his-15-only and
   all-31-correlated structures) reproduces the same MATERIAL/NOT MATERIAL
   split, within ~3% of the diagonal-only Delta chi2 values in every case.
5. `[VERIFIED-REAL]` Result 5: `FINDING_E5`'s own named caveat is CLOSED.
   Traced to the real source (Moresco et al. 2012, arXiv:1201.3609, via
   the BC03 table's own `reference` column) rather than the 2020
   covariance paper it was originally attributed to. The fit method
   (`D4000_n`-age calibration) was held fixed across BC03/MaStro(=M11)
   and across redshift — confirmed by reading the 2012 paper's own
   method sections directly, and by an independent recomputation of the
   `1.6σ` figure from its own published Table 1, matching to 3
   significant figures.

## What this does NOT establish

1. **[CLOSED, Result 5]** Previously: "does not resolve `FINDING_E5`'s
   own open caveat." Now resolved — see Result 5. What remains open: this
   finding does not adjudicate whether the 13-clean-point or the full
   15-point reading is the "right" one to use going forward — both are
   legitimate, real data; that choice is a modelling decision, not
   something this finding can settle.
2. Does not show v82's own published results are wrong, right, or
   sensitive — this is entirely this project's own reconstruction
   (`chi2_fixed_h0anchor`, `TABLE_II`), never checked against v82's
   actual, unpublished fitting code.
3. **[UPDATED, Result 4]** Full covariance propagation IS now done (both
   swap variants, both correlation structures) — this item previously said
   it was unrun; it no longer is. What remains genuinely untested: whether
   M11 itself warrants a *different* covariance recipe than BC03's (this
   script reuses one shared matrix for both, per Result 4's own stated
   design choice) — a separate, harder question this work does not attempt.
4. Does not establish which table (BC03 or M11) is "more correct" — both
   are real, published, peer-reviewed choices; this finding is silent on
   that question by design.
5. `NO_AUTHOR_ERROR` — every number above characterizes this project's own
   `chi2_fixed_h0anchor` reconstruction, never a claim about v82 itself or
   about Dr. Buckholtz's own work.

## Files

- `moresco_bc03_vs_m11_refit.py` — main refit (Result 1-2).
- `robustness_exclude_excursions.py` — Result 3 robustness check.
- `full_covariance_bc03_vs_m11.py` — Result 4, full 15-point swap under
  Moresco's own correlated systematic covariance.
- `full_covariance_robustness_exclude_excursions.py` — Result 4, the same
  13-clean-point robustness check under full covariance.
- All `ruff check` clean; full project test suite (`pytest tests/ -q`)
  unaffected, run before and after this work (all passing, one pre-existing
  unrelated `RuntimeWarning` in an unrelated test file).
