# FINDING P178 — the low-z vs high-z discriminator FINDING_P177 named,
# run and retracted: an honest null result about the TEST, not the physics

**Date:** 2026-08-31
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive (numeric evaluation of a specific test
design — not a new physics claim)
**Continues/answers:** the skeptic's own proposed discriminating test
from `FINDING_P177`'s review (low-z-only vs high-z-only subsample
comparison, to separate "genuine directional correspondence" from
"Taylor-truncation leverage" as explanations for the 0.017° directional
match `FINDING_P177` found).
**Script:** `P178_low_z_vs_high_z_discriminator.py` (numpy/scipy, 4
tests incl. 2 skeptic-requested verification checks, ruff clean,
881/881 project tests still pass).
**Status tags (per `docs/151_status_separation_rule.md`):**
> **Empirical/Model status:** the raw numbers (angles of 0.0062° and
> 0.0195° for the two subsamples) are computed correctly and reproduce
> under step-size sweeps — but their INTERPRETATION as evidence is
> RETRACTED (see Correction). This is a null result about test validity.
> **Ontological/mechanistic interpretation status:** UNCHANGED from
> `FINDING_P177` — genuine correspondence vs. Taylor-truncation leverage
> remains open; this file did not resolve it.
> **Causal/cosmological claim status:** N/A.

## Correction (2026-08-31, context-asymmetric skeptic-caught, applied
before finalizing — this retraction is total, not a softening)

A skeptic review of this file's first draft found the headline
conclusion ("the ordering low-z < full < high-z narrows the question
toward partial Taylor-truncation leverage") does not survive, for two
independent, directly-verified structural reasons:

1. **SH0ES contributes zero to the Hessian.** SH0ES (`z=0.0233`) is the
   anchoring reference point (`zref`) the whole `H(z)` construction is
   built around — `H(Z_SHOES)` is *identical* to `H0,anchor` by
   construction, for any `(β1,β2,ε)`. **Verified directly**: perturbing
   `β1`, `β2`, or `ε` each leave the SH0ES-alone χ² term exactly
   unchanged, to full double-precision display (not merely small — zero).
   So "low-z, 8 points" is really **7 constraining points**, not 8 —
   while the high-z subsample has no equivalent issue (DESI is a genuine
   data point). The two subsamples were not on equal footing.
2. **Far more seriously: both 8-point subsamples have a near-2D-flat
   curvature subspace, not a single well-defined near-null direction.**
   The ratio of the second-smallest to largest eigenvalue (`λ2/λ3`) is
   **`1.6×10⁻⁶` for low-z and `3.5×10⁻⁶` for high-z — 30–80× smaller**
   than the same ratio in the full 33-point sample (`1.2×10⁻⁴`, from
   `FINDING_P177`). With only 8 (7 effective) data points and 3
   parameters, there is not enough independent constraining power to pin
   down a *unique* near-null direction the way the full sample could —
   the specific eigenvector `numpy.linalg.eigh` returns from within that
   near-flat 2D plane is not shown to track the true physics rather than
   the specific finite-difference discretization's own residual bias.
   This file's own step-size-convergence check only demonstrates that
   the *same scheme* reproduces the *same answer* — not that the answer
   is *accurate*, which is exactly the distinction that matters when the
   surface is this ill-conditioned.

**Net result**: the observed ordering (low-z angle smaller than high-z
angle) may be real, or may be a pure artifact of (1) and (2) — this test
cannot tell the two apart, and therefore cannot be read as evidence
either way. `FINDING_P177`'s original open question is **unchanged, not
narrowed**. This file's value is as an honest record that this specific
test design does not work, and a name for what a working version would
require.

## 0. Premise — `NO_AUTHOR_ERROR`

This file evaluates a specific test design against TJB's own real data
and functions (reproduced verbatim); it makes no claim about v82's own
theory.

## 1. What was attempted and what survives

Split the real 33-point dataset into low-z (`z≤0.2`, 8 points) and
high-z (`z≥1.0`, 8 points) subsamples, holding `(β1,β2)` fixed at TJB's
own real fit, and recomputed the `ε`-compensation near-null direction
(same construction as `FINDING_P177`) for each subsample independently.

```
LOW-z only:  angle to P165's prediction = 0.0062 deg
HIGH-z only: angle to P165's prediction = 0.0195 deg
Full 33-pt (FINDING_P177):              ~0.0169 deg
```

These numbers themselves are reproducible (step-size-converged to <0.01°
across a 3× bracket) — **what does NOT survive is treating them as
evidence about Taylor-truncation leverage**, per the Correction above.

## 2. What this file does NOT establish

1. **Not a claim about v82's own theory** (`NO_AUTHOR_ERROR`, §0).
2. **Does not resolve, or even narrow, `FINDING_P177`'s open question**
   (genuine correspondence vs. Taylor-truncation leverage for the 0.017°
   directional match) — the attempted resolution failed for structural
   reasons named in the Correction.
3. **Does not establish that low-z data "matches better" than high-z
   data** in any trustworthy sense — the raw numbers point that way, but
   the near-2D-degeneracy of both subsamples means this cannot be
   distinguished from numerical-method artifact.
4. **A properly-designed version of this test remains undone.** At
   minimum it would need: a leave-one-out uncertainty estimate on the
   angle (the skeptic's own proposed fix — swap one point at a time
   within each 8-point subsample and see how much the direction moves);
   comparing `FINDING_P165`'s predicted direction to the near-degenerate
   *plane* the small eigenvalues span, not to one arbitrary vector
   picked from within it; and a random-subsample control (any 8 points,
   any redshift) to check whether *any* small subsample gives a
   similarly tiny angle regardless of redshift range at all — none of
   this is attempted here.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
