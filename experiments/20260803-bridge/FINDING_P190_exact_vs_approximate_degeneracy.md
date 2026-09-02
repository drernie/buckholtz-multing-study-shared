# FINDING P190 — v82's own (β1,β2) degeneracy is APPROXIMATE, not an
# exact parametrization redundancy

**Date:** 2026-09-02
**Continues:** `FINDING_P176`'s own explicit open item ("Does not explain
WHY the slope is 6.073×10⁷ specifically"). Answers a narrower, different
question than "why": is the found near-null direction an EXACT symmetry
of v82's own `H²(z)` construction (for all z simultaneously), or only a
local/data-range-specific near-flatness?
**Script:** `P190_exact_vs_approximate_degeneracy.py` (numpy/scipy, 2
positive controls, ruff clean, project's own 881 tests unaffected —
no shared module touched).
**Skeptic review:** dispatched context-blind (claim.md + script only, no
reasoning history) per Step 8a — verdict **CONFIRMED-REAL**. Found and
fixed one real (cosmetic) issue: a hardcoded "12.7%" string in the
verdict print statement that would go stale if the spread ever changed
on a future edit — replaced with the live `{spread:.4%}` format string.
No issue affecting the substance of the result.
**Status tags (per `docs/151_status_separation_rule.md`):**
> **Empirical/Model status:** SUPPORTED — the (β1,β2) degeneracy in
> v82's own real `H²(z)` construction is confirmed APPROXIMATE, not
> exact. Two independent positive controls pass (< 1e-6 and < 0.1%
> relative error); the skeptic independently re-derived the qualitative
> conclusion by hand from the power-law structure of `M(z),R(z),k(z),d(z)`
> alone, without running the script.
> **Ontological/mechanistic interpretation status:** N/A — this is a
> structural/mathematical fact about the construction, not a claim about
> physical mechanism.
> **Causal/cosmological claim status:** N/A.

## 0. Premise — `NO_AUTHOR_ERROR`

Every function and constant here is TJB's own, reproduced verbatim from
his own supplemental code (same source `P176` already positive-
controlled). This evaluates the mathematical structure of his own
published construction; it does not evaluate whether his theory is
correct.

## 1. Method

`forces(z,b1,b2)` is linear in `(b1,b2)` at fixed `z` (F1 ∝ b1, F2 ∝ b2,
z-dependent but b-independent coefficients; F0 and F_accretion don't
depend on b1,b2 at all — `R(z)` uses the fixed `H0_planck_si`, not the
fitted `H0_anchor`). Since `H²(z)` is built from `addot_over_a(z)/(1+z)`
by a LINEAR operation (cumulative trapezoid integration), `H²(z)` is
itself affine in `(b1,b2)` at each z:
```
H²(z; H0_anchor, b1, b2) = P(z) + b1·E1(z) + b2·E2(z)
```
An EXACT degeneracy direction — one that leaves H²(z) unchanged for
**every** z simultaneously, not just locally at one fit point — exists
if and only if `−E1(z)/E2(z)` (the level-set slope `d(β2)/d(β1)` holding
H²(z) fixed at that single z) is the SAME number for every z.

`E1(z), E2(z)` computed by propagating the pointwise derivatives
`d(addot_over_a)/db1, db2` (closed-form, from `forces()`) through the
same cumulative-trapezoid integration `H2_of_z` uses — exact, since
integration is linear, not an approximation.

**Positive control 1**: analytic `d(addot_over_a)/db1, db2` match a
direct finite-difference on `addot_over_a` at 5 test z-values (0.07 to
2.33) to < 1e-6 relative error.
**Positive control 2**: the propagated `E1(z), E2(z)` match a direct
finite-difference on `H2_of_z` itself (P176's own already-verified
function, including its `zref`-subtraction logic) at z=0.5, 1.965, to
< 0.1% relative error — confirms the linear-propagation shortcut is
faithful to the real, full pipeline, not just the pointwise piece.

## 2. Results

```
z= 0.070:  -E1/E2 = 5.386e+07
z= 0.090:  -E1/E2 = 5.405e+07
z= 0.200:  -E1/E2 = 5.504e+07
z= 0.500:  -E1/E2 = 5.717e+07
z= 0.900:  -E1/E2 = 5.903e+07
z= 1.300:  -E1/E2 = 6.014e+07
z= 1.965:  -E1/E2 = 6.102e+07
z= 2.330:  -E1/E2 = 6.120e+07

Spread across z=0.07..2.33: 12.7355%
Range: [5.3855e+07, 6.1202e+07]
Compare: P176's own chi²-weighted near-null slope = 6.073104e+07
```

The single-z slope rises monotonically with z, from 5.39×10⁷ (z=0.07)
to 6.12×10⁷ (z=2.33) — a real, non-trivial, monotonic 12.7% variation,
not numerical noise (both positive controls pass to well under 0.1%).
P176's own χ²-weighted-average slope (6.073×10⁷) sits near the high-z
end of this range — consistent with the high-z anchor points (DESI
z=2.33, small relative weight but large lever arm) and the low-uncertainty
SH0ES point dominating the χ²-weighted fit, not a coincidence requiring
further explanation here.

**Independent skeptic derivation (context-blind, no script execution):**
working the power-law exponents of `M(z),R(z),k(z),d(z)` by hand from
the code as written, the pointwise ratio `d(addot)/db1 / d(addot)/db2`
has an effective log-slope in `(1+z)` of **+0.642 in the matter-only
limit** and **−0.098 in the DE-dominated limit** — the slope's sign
itself changes across the tested range, which independently forces
non-constancy of `−E1(z)/E2(z)` from the algebra alone, without running
any code. This matches the numerically-observed monotonic 12.7% rise.

## 3. Verdict

**The (β1,β2) degeneracy P176 found is APPROXIMATE, not an exact
parametrization redundancy.** `H²(z)` is exactly affine in `(β1,β2)`,
but the ratio of its two z-dependent coefficient functions is not
constant — no single linear direction in `(β1,β2)` leaves v82's own
`H²(z)` construction invariant at every z simultaneously. P176's found
near-flat Hessian direction is a real, strong, but data-range-specific
feature of the actual 33-point χ²-weighted fit — not a structural fact
about how `(β1,β2)` parametrize physical predictions.

**Consequence for bottleneck 3 (Absolute scale / observable mapping):**
this rules OUT the strongest possible version of the "structurally
non-identifiable by construction" reading (the exact-symmetry outcome
in `CLAIM_P190`'s own outcome table) — the degeneracy is NOT unbreakable
by any amount of H(z) data in principle. It rules IN, more precisely
than before, the weaker reading already implicit in P176: the
near-degeneracy is a real feature of TJB's ACTUAL 33-point compilation's
z-coverage and error weighting, and — in principle — a sufficiently
different z-coverage or tighter high-z constraints COULD narrow it,
though this does not by itself provide a practical path (see below).

## What this file does NOT establish

1. Does not identify what specific new data/observable WOULD break the
   degeneracy in practice — only that H²(z) alone, structurally, permits
   this in principle (unlike the exact-symmetry case, which would have
   ruled it out permanently).
2. Does not connect to `FINDING_P165`'s ε-absorption mechanism (out of
   scope here, and P175/P176 already retracted two attempts at that link).
3. Does not repeat or supersede `P182`-`P187`'s real-data/real-literature
   confound-breaking attempts — this is a purely structural/symbolic
   question about the construction's own functional form, answered
   without touching any real data beyond the fixed physics functions
   already reproduced in P176.
4. Does not establish anything about v82's own theory being right or
   wrong (`NO_AUTHOR_ERROR`) — a real degeneracy (exact or approximate)
   in a fit is a common, unremarkable feature of many multi-parameter
   models.
5. Does not quantify how much different z-coverage would be needed to
   meaningfully narrow the degeneracy — that would require a real Fisher-
   information/forecast calculation, not attempted here.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
