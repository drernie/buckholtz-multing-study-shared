# CLAIM E16 — propagate `E15`'s Jensen's-gap correction through an actual
# re-fit of `(H0_anchor, β1, β2)`, per `docs/157`'s named next step

**Date:** 2026-09-06 (pre-registered before any numeric result)
**Continues:** `FINDING_E15` (force-term-level corrections
`exp(σ²/2)=1.1276`, `exp(2σ²)=1.6164` at `E13`'s real `σ=0.49`), `E8`'s
Hessian-slope machinery, `E8b`'s re-optimizer. Named as the cheapest,
most-differentiating next step in `docs/157_next_steps_plan_20260906.md`.

## EstimandOps L0

**Descriptive/characterization** — "what does TJB's own already-published
fit's parameter interpretation look like under a stated, real correction
to one input's treatment," not a causal claim about MULTING's physics.

## The mechanism, verified directly in the code

`[VERIFIED-CODE]` `P176_v82_real_chi2_hessian_degeneracy.py:125-130`:
`forces(z, beta_1, beta_2)` returns `F1 = beta_1 * (z-only term)`,
`F2 = beta_2 * (z-only term)` — each **linear** in its own beta, with no
beta-beta cross term. `E13`'s correction (`σ=0.49`, fixed, not
z-dependent) rescales `F1,F2` by fixed constants at every `z` — so
substituting population-averaged `F1,F2` is **exactly** equivalent to
substituting `beta1*CORR_F1, beta2*CORR_F2` into the **unchanged**
`chi2_fixed_h0anchor` — no new physics code, only a wrapped chi2 function:

```
CORR_F1 = exp(σ²/2) = 1.1276   (E15's dipole correction)
CORR_F2 = exp(2σ²)  = 1.6164   (E15's quadrupole correction)
chi2_corrected(h0a, b1, b2) := chi2_fixed_h0anchor(h0a, b1*CORR_F1, b2*CORR_F2)
```

## Self-correction of `docs/157`'s own prior claim

`docs/157` speculated this step would need genuine numerical
re-optimization because "H(z) is nonlinear in F_total" and a naive
per-term rescale wouldn't respect the `(β1,β2)` degeneracy. Re-deriving
carefully **before writing code** (per this project's estimand-before-code
discipline): the map `(b1,b2) → (b1·CORR_F1, b2·CORR_F2)` is a bijection
of `ℝ²`, so the family of curves reachable by `chi2_corrected` over all
`(b1,b2)` is **identical** to the family reachable by
`chi2_fixed_h0anchor` — meaning the **global minimum chi2 is unchanged**,
achieved at the closed-form point `b1_true = b1_TJB/CORR_F1`,
`b2_true = b2_TJB/CORR_F2`. **No numerical optimizer is needed to find
this minimum — it is an algebraic identity, not a fit result.** This
corrects `docs/157`'s framing; recorded here rather than silently, per
this project's no-silent-correction discipline.

## What IS genuinely new here (not already known from `E15` or the identity above)

**Self-corrected after running the numbers, before any skeptic dispatch
(recorded here, not silently):** the original plan below asked whether
`E8`'s own `hessian_small_eig_and_slope`, applied to `chi2_corrected` at
`(b1_true,b2_true)`, would show a materially different valley SLOPE than
the baseline. It does (`30.24%`, over the `20%` MCID) — but running the
actual numbers shows this is **not independent information**: in that
function's own normalised coordinates (`x=b/b_f`), `chi2_corrected` and
`chi2_fixed_h0anchor` are *the same function of `x`* (substitution shows
`chi2_corrected(x·b1_true, x·b2_true) ≡ chi2_fixed_h0anchor(x·b1_TJB,
x·b2_TJB)` identically), so their near-null eigenvector components in
`x`-space are identical, and the reported raw-space slope ratio is
**algebraically forced to equal `CORR_F1/CORR_F2`** — the exact same
number as the closed-form ratio shift below. Reporting both as
independently MATERIAL would be double-counting one fact as two.

**What survives as the real finding, corrected after Step 8a skeptic
review (verdict: `CONFIRMED-REAL` on the algebra, `WEAKENED` on this
framing — applied in place, not silently):** the chi2 *minimum* is
invariant under this reparametrization (confirmed two ways: closed-form
algebra, and `E8b`'s own optimizer converging to the closed-form point
independently). That means chi2 **cannot distinguish** "TJB's own
`(β1,β2)` are point-evaluated couplings" from "TJB's own `(β1,β2)` are
population-averaged couplings, with the true coupling smaller by
`1/CORR_F1`, `1/CORR_F2` respectively."

**The skeptic correctly downgraded the original framing** ("a genuine,
third identifiability degeneracy for this project, after the `(A,g,κ)`
result and the `(β1,β2)` valley") as an overclaim: those two prior results
are **flat-valley degeneracies** — one chi2 function with multiple
minima/a flat direction, informationally irrecoverable from the data
alone. This result is structurally different — **two distinct chi2
functions** (`chi2_fixed_h0anchor` and `chi2_corrected`), each with a
*single, well-defined* minimum, related by a known linear reparametrization.
It resolves the instant an external estimate of `σ` exists (which `E13`
already supplies) — it is a **hidden-nuisance-parameter structure**, not
an information-theoretic degeneracy. Restated: `E15`'s own Reading A vs B
ambiguity is not resolvable from the `H(z)` fit alone, for *any* fixed
correction factor — that framing is correct; "identifiability degeneracy
of the same kind as `(A,g,κ)`/`(β1,β2)`" was not.

**A second skeptic finding, genuinely new, not previously noticed:** `E13`'s
correction is only ever applied to `F1`,`F2` here. But `forces()`'s `F0`
(`= -G·M²/d²`) and `F_accretion` (`= m_dot·dv_coh`, `m_dot∝M`,
`dv_coh∝√M/R∝√M`) are **also nonlinear functions of `M(z)`** — if `M(z)`'s
own population scatter is real (a live, unresolved question this project
has not measured), `F0` and `F_accretion` would carry their **own** Jensen
corrections, which are **not** absorbed by rescaling `β1,β2` alone, since
`F0` and `F_accretion` do not depend on `β1,β2` at all. This claim is
scoped to the `F1,F2` correction only — `[WEAK]` marker applies until
`F0`/`F_accretion`'s own scatter is checked or shown negligible.

## Falsifiable predicate

The closed-form identity (`chi2` minimum unchanged under the
reparametrization) must be confirmed **two independent ways** — direct
algebraic substitution, and `E8b`'s own numerical optimizer converging to
the same point from the same starting values — before it is reported as
established, per this project's Independent Verification Strength Ladder
(same-model-different-route counts as a real, if modest, upgrade over
algebra alone).

## Pre-registered MCID

- **Ratio shift** (`0.6976`, `≈30.2%`): reported as the finding's
  magnitude, not tested against a threshold — it is a derivation, not an
  estimate with a null to reject.
- **Valley-slope shift, `20%` MCID** (`E8`'s own convention): fires
  (`30.24%`), but per the self-correction above this is the *same fact*
  as the ratio shift, not independent confirmation — do not report both
  as separately material.

## Method

1. Build `chi2_corrected` as the wrapped function above — no new physics.
2. **Positive control 1 (identity check, σ→0):** `CORR_F1=CORR_F2=1` must
   make `chi2_corrected` exactly equal `chi2_fixed_h0anchor` at every
   point tested.
3. **Positive control 2 (closed-form check):** `chi2_corrected(h0a_TJB,
   b1_TJB/CORR_F1, b2_TJB/CORR_F2)` must equal `chi2_fixed_h0anchor(h0a_TJB,
   b1_TJB, b2_TJB)` (TJB's own reported `15.75`) to numerical precision —
   this is definitional, but confirms no algebra slip.
4. **Numerical confirmation of the identity:** run `E8b`'s own
   `opt_multing` optimizer on `chi2_corrected`, starting from TJB's own
   point — it must independently converge to the closed-form
   `(b1_true,b2_true)` and to chi2≈15.75. If it does not, the closed-form
   reasoning above has an error and must not be reported as established.
5. Compute the baseline and corrected Hessian small-eigenvalue + slope
   (`E8`'s own function, unmodified), report the % change.

## What this claim does NOT say

1. Does not claim population-averaging is the correct physical
   description of v82's construction (`E15`'s own open Reading A vs B
   ambiguity is inherited unchanged, not resolved here).
2. Does not claim TJB's own reported `(β1,β2)` were meant to be
   point-evaluated rather than already-representative — that
   interpretive question is `E15`'s, not this file's, to resolve.
3. `NO_AUTHOR_ERROR` — this is a direct, literal answer to a question this
   project itself posed (`docs/157`), not a claim about v82's correctness.
