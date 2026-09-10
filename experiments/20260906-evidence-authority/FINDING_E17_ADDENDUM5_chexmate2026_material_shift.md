# FINDING E17 ADDENDUM 5 — a real, more current (2026), homogeneous
# weak-lensing measurement gives a MATERIALLY different scatter than
# ADDENDUM4's own anchor points

**Date:** 2026-09-10
**Continues:** `FINDING_E17_ADDENDUM4` (real cluster-scale `σ(log10 c)`
from Groener, Goldberg & Sereno 2015). Surfaced by the user pasting a
web-search-tool report naming candidate 2026 concentration-mass papers;
verified directly against arXiv before use (two of three candidates
checked; both real).

`NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * L0 descriptive`
`NO_AUTHOR_ERROR`

## The real source, `[VERIFIED-arXiv]`

Umetsu et al. 2026, *"CHEX-MATE: AMALGAM weak-lensing analysis of 41
Planck Sunyaev-Zel'dovich-selected galaxy clusters"*
(`arXiv:2606.24142`, published 2026-06-23). Confirmed directly via the
paper's own abstract: a homogeneous weak-lensing shear analysis of 41
Planck-SZ-selected clusters (single survey, single pipeline, hierarchical
Bayesian framework), not a heterogeneous literature compilation. Their
own quoted result, verbatim: *"At `M_200=10^15 M_☉` and `z=0.25`, we
find `c_200=3.53±0.71` with an intrinsic scatter of `0.22±0.04` dex...
consistent with recent ΛCDM predictions for massive haloes, with no
significant mass or redshift dependence over the probed range."*

A second candidate paper (Bocquet et al. 2026, `arXiv:2603.19898`, "On
the cosmology dependence of the cluster weak-lensing mass bias") was
also confirmed real via its abstract, but is about cosmology-dependent
mass-bias corrections from simulations, not a directly quotable
`σ(log10 c)` value — not used further here. A third candidate ("Yasin
et al., SWIFT collaboration") was not independently verified (no arXiv
ID given, general lab publication-list link only) — not used.

## Re-evaluated `ADDENDUM3`'s own `sigma_sweep()` at this real, newer
## value

| σ source | σ | divergence at `z=2.33` | shift vs Duffy `0.15` |
|---|---|---|---|
| Duffy 2008 (prior default) | 0.150 | 1.815× | — |
| `ADDENDUM4`: X-ray, Groener+2015 (closest method-match) | 0.160 | 1.725× | −4.9% |
| **`ADDENDUM5`: WL, CHEX-MATE 2026 (most current, homogeneous, single-survey)** | **0.220** | **1.307×** | **−28.0%** |

At `z=2.00`: `1.612×` (Duffy) vs `1.232×` (CHEX-MATE) — a `−23.6%` shift.

**Both shifts clear this project's own pre-registered MCID (`>20%`,
`ADDENDUM3`).** Unlike `ADDENDUM4`'s X-ray-method comparison (which
validated the old default to within `5%`), this real, more current
weak-lensing measurement gives a MATERIALLY different result.

## What this establishes

1. `[VERIFIED-arXiv]` A real, substantive update: the most current
   (2026), homogeneous, single-survey weak-lensing measurement of
   cluster concentration scatter disagrees materially with the
   Duffy-2008 default this thread has used throughout — not just in the
   sense `ADDENDUM4` already flagged (different techniques give
   different numbers), but specifically for weak lensing itself, where
   the older, heterogeneous 2015 literature compilation (Groener+2015's
   own `WL` row: `σ=0.118`) and the newer, homogeneous 2026 single-survey
   measurement (`σ=0.22`) disagree by nearly a factor of `2` with each
   other, not just with X-ray.
2. This sharpens `ADDENDUM4`'s own conclusion: the choice of which real,
   published `σ(log10 c)` to trust is not just a cross-technique
   question (lensing vs X-ray vs kinematics) but also a
   compilation-vintage question (older heterogeneous aggregate vs newer
   homogeneous single-survey measurement) — both axes move the
   divergence headline by amounts that clear this project's own MCID.
3. CHEX-MATE's own explicit finding of "no significant mass or redshift
   dependence" supports this project's own modelling choice (`σ` held
   constant across the `z` range swept) — a real, independent piece of
   methodological support, separate from the numeric value itself.

## What this does NOT establish

1. Which of the real, published `σ` values (X-ray `0.160`, WL-2015
   `0.118`, WL-2026 `0.220`, or the galaxy-kinematics values `0.228-
   0.246`) is the "correct" one for v82's own construction — this
   project does not adjudicate between real, competing measurements in
   the literature.
2. A single, final, corrected divergence number — `ADDENDUM3`'s own
   honest framing ("a range, not a point estimate") is, if anything,
   reinforced by this addendum, not resolved by it.
3. `NO_AUTHOR_ERROR` — entirely about this project's own reconstruction
   of the `F0`/`F_accretion` Jensen-correction sensitivity chain; no
   claim about v82's, Correa's, Groener/Goldberg/Sereno's, or Umetsu et
   al.'s own correctness.

## Files

- No new script — reused `ADDENDUM3`'s own `sigma_sweep()`/`divergence()`
  unchanged (`/tmp/chexmate_check.py`, not committed — trivial 15-line
  invocation, kept out of the repo per this project's own convention of
  not committing throwaway verification scripts; the two numbers it
  produces are quoted directly above and independently reproducible from
  `ADDENDUM3`'s own committed module).
