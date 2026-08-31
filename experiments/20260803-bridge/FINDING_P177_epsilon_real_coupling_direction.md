# FINDING P177 — a properly-posed attempt to connect FINDING_P165's
# epsilon mechanism to the real degeneracy FINDING_P176 found

**Date:** 2026-08-31
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive (numeric evaluation of TJB's own real
fit surface — not a new physics claim)
**Continues/answers:** the open question both `FINDING_P175` and
`FINDING_P176` left unresolved after retracting their own two attempts
to connect `FINDING_P165`'s hypothetical monopole-tier `ε`-absorption
mechanism to something in v82's own real, published fit.
**Script:** `P177_epsilon_real_coupling_direction.py` (numpy/scipy, 6
tests incl. 3 skeptic-requested checks, ruff clean, 881/881 project
tests still pass).
**Status tags (per `docs/151_status_separation_rule.md`):**
> **Empirical/Model status:** MIXED — one sub-claim RETRACTED after
> skeptic review (see Correction), one sub-claim SUPPORTED and
> strengthened by the same review.
> **Ontological/mechanistic interpretation status:** OPEN — a real,
> precisely-quantified directional agreement is established; whether it
> reflects a genuine physical correspondence or is largely explained by
> the local model being a leading-order Taylor term of the same
> underlying force law is explicitly NOT resolved here.
> **Causal/cosmological claim status:** N/A.

## Correction (2026-08-31, context-asymmetric skeptic-caught, applied
before finalizing)

A skeptic review of this file's first draft found the headline claim
overreached, and separately found the supporting evidence miscast in
two ways. All three checked independently before accepting or rejecting.

**Retracted in full:** the claim that "a monopole-tier `ε` can be
compensated almost completely freely along this direction." The
reference point used (TJB's own fitted `β1,β2`, with `ε=0`) is **not a
joint critical point** of the full 3-parameter `χ²` — only `β1,β2` were
ever optimized; `ε=0` is just where TJB's own real, published force law
happens to sit, not a minimum in the `ε` direction. A near-zero Hessian
eigenvalue at a non-critical point does not mean "flat" — `χ²` can still
change **linearly** along that direction via the gradient, and a linear
term swamps a tiny quadratic one for any non-infinitesimal step.
**Checked directly**: the gradient of `χ²`, projected onto the near-null
eigenvector, gives a linear term of `~4.0×10⁻⁴` for a unit step, versus a
quadratic term of only `~5.7×10⁻⁷` — the **linear term is ~700× larger**.
The surface has real slope there, not flatness. Establishing the
"nearly free" claim properly would require re-optimizing `(β1,β2,ε)`
jointly to a genuine 3D critical point — not attempted here (the
surface's own known ill-conditioning makes this computationally
expensive, and a first, shorter re-optimization attempt in `FINDING_
P176` did not fully converge within a reasonable wall-clock budget).

**Checked and REFUTED (an alternative explanation the skeptic proposed,
which would have undermined the whole approach differently)**: that
`(1+ε)·F0` is close to a trivial rescaling of the total force, because
`F0` (the plain Newtonian monopole term) is "by far numerically
dominant." **Directly measured at four redshifts (z=0, 0.5, 1.0, 2.33)**:
`F1` and `F2` are actually **~800–1100× larger than `F0`**, at TJB's own
fitted `β1,β2` — `F0` is the *sub*dominant term, not the dominant one.
Perturbing `F0` alone via `ε` is therefore a genuinely targeted
perturbation, not a disguised `H0,anchor` rescale.

**Corrected, not retracted (a methodological fix)**: the first draft
reported two separate component-wise ratios (`1.11` for `β1`, `1.24` for
`β2`) between the real and predicted directions and called this "one
consistent factor" — the skeptic correctly noted these are not the same
number and are basis-dependent. **The correct, basis-independent
measure is the angle between the two 3-vectors**: computed directly,
`0.017°` (cosine similarity `0.99999995`) — an extremely tight
directional match, tighter and cleaner than the original component-ratio
framing suggested.

**Net result of the correction**: the file's central *quantitative*
claim ("ε is nearly free") does not survive and is dropped. A narrower,
still genuinely interesting *directional* claim survives and is
strengthened: **the compensation direction FINDING_P165's crude,
idealized, 2nd-order local Taylor construction predicts matches the real
full-`χ²`-surface's corresponding near-null direction to within 0.02
degrees** — verified not to be an artifact of `F0`-dominance, verified
step-size-convergent, verified `H0,anchor`-independent across 3 tested
rows. What this directional agreement *means* — genuine physical
correspondence, or mostly an artifact of the local model being the
leading Taylor term of the exact same underlying integrand this file
evaluates in full — is an open question this file does not resolve (the
skeptic's own proposed discriminating test, a low-`z`-only vs
high-`z`-only subsample comparison, was not run).

## 0. Premise — `NO_AUTHOR_ERROR`

Every function and constant is TJB's own, reproduced verbatim; `ε` is
this project's own hypothetical device (as in `FINDING_P165`), not a
claim about v82's own theory.

## 1. Method

Added `F0 → (1+ε)·F0` to TJB's own real force law (the exact same
substitution `FINDING_P165` defined, applied here to the real,
33-point-data-integrated `χ²`, not an idealized local expansion).
**Positive control**: `ε=0` reproduces `FINDING_P176`'s own already-
verified real `χ²` exactly. At TJB's own fitted `(β1,β2)` and `ε=0`,
computed the full `3×3` numeric Hessian in rescaled `(x1,x2,ε)`
coordinates; diagonalized; extracted the near-null eigenvector.

## 2. Results

```
Near-null eigenvector (normalized to delta_eps=1):
  real:      (2.055851e-3, 1.109808e-3, 1.0)
  predicted: (1.844730e-3, 8.957642e-4, 1.0)   [FINDING_P165/P175's C]

Angle between the two directions: 0.0172 deg (cosine = 0.99999995)
H0,anchor-independence of this angle: confirmed at 3 rows (spotlighted,
  pct_50, planck_exact_100pct), component ratios agree to <1%.

F0 vs F1,F2 (at TJB's own fitted beta1,beta2):
  z=0.0:  F1/F0=1084, F2/F0=1116
  z=2.33: F1/F0=930,  F2/F0=821
  -> F0 is the SUBDOMINANT term, not dominant.

Linear vs quadratic term along the near-null direction (unit step):
  linear = 3.9955e-4, quadratic = -5.6868e-7, ratio = 702.6
  -> the "flat direction / epsilon nearly free" reading FAILS this check.
```

## 3. Verdict

Two separate, clearly-labeled outcomes, not one:

1. **RETRACTED**: `ε` is "nearly free" / cheaply absorbable near TJB's
   own real fit point. The reference point is not a joint critical
   point in `ε`, and the real gradient dominates the tiny curvature
   there by ~700×.
2. **SUPPORTED**: the *direction* `FINDING_P165`'s idealized local
   mechanism predicts for `ε`-compensation matches the real, full-data
   `χ²` surface's own corresponding near-null direction to within
   `0.02°` — a genuine, precisely quantified, `H0,anchor`-independent,
   basis-independent fact, verified not to be explained away by
   `F0`-dominance. Its ultimate physical meaning (real correspondence
   vs. Taylor-truncation self-consistency) is not resolved.

## What this file does NOT establish

1. **Not a claim about v82's own theory** (`NO_AUTHOR_ERROR`, §0).
2. **Does not establish that `ε` can be practically hidden/absorbed in
   TJB's real fit** — the opposite of what the first draft claimed; see
   Correction.
3. **Does not establish WHY the 0.02° directional match holds** — the
   skeptic's own proposed discriminating test (comparing the direction
   computed from a low-`z`-only subsample against a high-`z`-only
   subsample, which would separate "genuine structural correspondence"
   from "expected Taylor-truncation leverage from the high-`z` DESI
   point") was not run.
4. **Does not attempt a genuine joint 3-parameter re-optimization** of
   `(β1,β2,ε)` — the only way to properly test whether a real, practical
   `ε`-degeneracy exists near the true minimum, not just at TJB's own
   `ε=0` reference point.
5. **Does not connect back to this project's own external growth-rate
   ceiling** (`ε≤8.39×10⁻¹²`, `FINDING_P22`/`P132`) the way `FINDING_
   P175` attempted — that connection remains untested here, and would
   inherit the same "not a critical point" caveat unless redone at a
   genuine joint minimum.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
