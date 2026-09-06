# CLAIM E19 — is v82's H(z) "phantom turn" (minimum near the present,
# then rising) supported by real data, or is it below measurement
# precision / an extrapolation artifact? Answering Ernest Prabhakar's
# item 3, corrected version

**Date:** 2026-09-06
**Trigger:** Same email thread as `E18`. Ernest's item 3 (original):
"the 'phantom' turn is not a prediction — on your own figure the
minimum of H(z) is at z≈0, and the rise appears only on the future-
extrapolated dashed curve, not in any data." **Ernest's own follow-up
correction** (after TJB's own Claude dialogue): "the minimum is at
z≈0.086 (~1.1 Gyr ago), not z≈0 as I wrote — my conclusion that it is
currently untestable still stands, but the location was wrong."
**Explicit go-ahead given** ("теперь пункт 3, фантомный поворот").

## L0 (EstimandOps)

**Descriptive.** Does v82's own H(z) trajectory (spotlighted and
SH0ES-anchored configurations) have a real minimum, where is it located
relative to the actual cosmic-chronometer data's own redshift coverage,
and is the dip's depth larger or smaller than the real, quoted
measurement uncertainty at comparable redshifts? Not a claim about
whether MULTING's physics is correct, and not a re-litigation of TJB's
own Claude session's arithmetic — an independent check of it.

## What TJB's own (external) Claude session already found, to be
## independently checked, not re-derived from scratch

- (A) Minimum at `z≈0.086`, `t≈12.7` Gyr post-Big-Bang (~1.1 Gyr ago),
  `H_min≈72.4` km/s/Mpc (spotlighted) / `≈72.2` (SH0ES-anchored) — a
  shallow (~2%) dip relative to today's `H≈73.8`.
- (B) "Possibly falsifiable in principle, not decisively falsifiable at
  today's precision" — the ~2% dip sits where cosmic-chronometer errors
  are quoted as "~10-15% per point," swamping the signal.
- (C) A genuine but "weak/fragile" prediction — qualitatively distinct
  from the `w=-1` family, but obtained in a low-z, anchor-dependent
  regime.

## Falsifiable predicate and pre-registered MCID

**Predicate:** (1) an independently-computed H(z) minimum, using this
project's own already-verified reproduction of v82's own H(z) function
(`E18`'s `multing_fit_rerun.py`, not re-derived), matches TJB's Claude
session's claimed location/depth; (2) the minimum's redshift lies
inside, at the edge of, or below the real cosmic-chronometer data's own
lowest sampled redshift; (3) the dip depth (`H(present) − H_min`, as a
fraction of `H_min`) compared directly against the REAL, quoted
sigma/H fractional uncertainty of the actual nearest CC data points
(not an assumed "10-15%") — is the claimed signal bigger or smaller
than real, quoted noise at that redshift.

**MCID:**
- (1) MATERIAL DISCREPANCY if our independently-computed `z_min`/`H_min`
  differ from TJB's Claude session's claimed values by `>10%`
  (relative) — would flag either a reproduction error on our side or an
  error in his own AI session's arithmetic.
- (2)/(3): no numeric pass/fail threshold — this is a descriptive
  characterization (signal-vs-noise ratio at the relevant redshift),
  reported as a number, not gated by an arbitrary cutoff (per the
  Structure-Bias Guard — this is a reasoning-heavy comparison, not a
  binary pass/fail check).

## Method

1. Reuse (not re-derive) `E18`'s own already-verified `H_of_z_vec`/
   `H_of_z_single` from `multing_fit_rerun.py`, at TJB's own published
   `(β1,β2,H0_anchor)` for `unconstrained_spotlighted` and
   `sh0es_anchored_0pct`.
2. Find the precise minimum via a fine grid scan (`z∈[0,0.5]`, dense)
   plus local refinement (`scipy.optimize.minimize_scalar`), for both
   configurations.
3. Read the real CC data (`cosmic_chronometer_31pt.csv`, already used
   unchanged in `E18`) — report its own minimum sampled redshift and
   the quoted `sigma_kms_Mpc` at the 2-3 lowest-z points.
4. Compute the dip depth as `(H(z=0) − H_min)/H_min`, and separately
   compute the real fractional uncertainty (`sigma/H`) at the CC points
   nearest the claimed minimum — report both, directly comparable.
5. State explicitly whether `z_min` sits inside, at the edge of, or
   below the CC data's own coverage — a fact-check on Ernest's
   corrected claim, not assumed from his email.

## Controls

- **Positive control:** the independently-computed `H(z=0.0233)`
  (SH0ES's own anchor redshift) must equal `H0_anchor` exactly by
  construction (same check `E18`'s own machinery already relies on) —
  confirms the H(z) function is being called correctly here.
- **Sanity check**: `dH/dz` must change sign exactly once near the
  claimed minimum (confirms a genuine local minimum, not a numerical
  artifact of the grid).

## What this does and will NOT establish

1. Whether MULTING is physically correct — `NO_AUTHOR_ERROR`, Empirical/
   Model status only, per `docs/151`.
2. Whether the "phantom turn" is real physics or a fitting artifact —
   this claim characterizes the SIGNAL-TO-NOISE situation, it does not
   adjudicate whether the underlying mechanism is genuine.
3. A statistical significance test (a proper Bayesian/frequentist
   detection-significance calculation is a larger task than a
   descriptive signal-vs-noise comparison) — this reports magnitudes,
   not a p-value or a formal detection claim.
