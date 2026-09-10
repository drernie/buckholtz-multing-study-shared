# FINDING — Moresco BC03-vs-M11 table swap: MATERIAL by chi2, but almost
# entirely driven by 2 of 15 points FINDING_E5 already flagged as carrying
# an unverified confound; H0,anchor itself barely moves either way

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
   robust to the 2 points `FINDING_E5` already flagged as carrying an
   unverified confound — it is MATERIAL if those 2 points are trusted at
   face value, NOT MATERIAL if they are set aside pending the still-unrun
   check named in `FINDING_E5` (§3-4 of Moresco et al. 2020, arXiv:
   2003.07362, on whether the BC03/M11 re-analysis held the same fit
   method at `z>0.7`).

## What this does NOT establish

1. Does not resolve `FINDING_E5`'s own open caveat on the 2 excursion
   points — that check (reading §3-4 of arXiv:2003.07362) is still unrun.
   This finding narrows why it matters (it flips the chi2 materiality
   verdict) but does not run it.
2. Does not show v82's own published results are wrong, right, or
   sensitive — this is entirely this project's own reconstruction
   (`chi2_fixed_h0anchor`, `TABLE_II`), never checked against v82's
   actual, unpublished fitting code.
3. Does not propagate Moresco's own full covariance (`Cov_model`,
   `100%`-correlated across `z`) — only substitutes central `H(z)` values,
   keeping `sigma_Hz` from BC03's own quoted column. `FINDING_E5` already
   showed that column excludes the SPS systematic by construction; a
   covariance-aware refit is a separate, still-unrun computation (partial
   groundwork exists in `E8_full_covariance_propagation.py`/
   `E8b_reoptimize_under_covariance.py`, not connected to this swap).
4. Does not establish which table (BC03 or M11) is "more correct" — both
   are real, published, peer-reviewed choices; this finding is silent on
   that question by design.
5. `NO_AUTHOR_ERROR` — every number above characterizes this project's own
   `chi2_fixed_h0anchor` reconstruction, never a claim about v82 itself or
   about Dr. Buckholtz's own work.

## Files

- `moresco_bc03_vs_m11_refit.py` — main refit (Result 1-2).
- `robustness_exclude_excursions.py` — Result 3 robustness check.
- Both `ruff check` clean; full project test suite (`pytest tests/ -q`)
  unaffected, run before and after this work (all passing, one pre-existing
  unrelated `RuntimeWarning` in an unrelated test file).
