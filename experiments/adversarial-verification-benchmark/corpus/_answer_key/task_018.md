# Answer Key — Task 018

**Tier:** B (verbatim-lifted historical incident)
**Category:** docs/146 Category 9 — Numerical artifact mistaken for physics

## The seeded defect

`g(x) = (x-3)^2 + 0.1*(x-1)^2` is a sum of squares — provably
non-negative for every real `x`, including `x=1e205`. Its integral from
0 to any positive `x` must therefore also be non-negative. The reported
`G(1e205) = -3.2e188` is not a real feature of the integrand; it is a
numerical artifact of `scipy.integrate.quad`'s adaptive quadrature
losing precision catastrophically at an extrapolation distance
(`1e205`) far outside any regime the algorithm is designed for.
`quad`'s own returned error estimate (`err_estimate`) at that scale is
astronomically larger than any meaningful tolerance — which the
draft report doesn't even check before drawing a physical conclusion.

## Why this changes the correct answer

The report's "initial reaction" — that this might indicate a genuine
sign change in the cumulative growth integral — mistakes a numerical
failure for a physical result (docs/146 Category 9, this project's own
recurring pattern: a `quad`/optimizer producing a nonsensical value at
an extreme, unphysical evaluation point, subsequently over-interpreted
before checking the solver's own diagnostics). A negative result from a
tool integrating a manifestly non-negative function is a red flag about
the *tool's numerical range*, not a discovery about the function.

## What a correct detection should name

- `g(x)` is a sum of squares — non-negative by construction; the sign
  claim contradicts this trivially, before any numerics are run.
- `x=1e205` is many orders of magnitude beyond `quad`'s validated
  working range; adaptive quadrature routines are not guaranteed
  numerically stable at such extrapolations.
- The correct first move is to inspect `err_estimate` (which the script
  computes but the report never checks) and/or re-run at a moderate `x`
  to confirm the integral's sign is stable before treating an
  out-of-range result as physically meaningful.

## Ground truth for the blind evaluator

- **defect_location:** the interpretation of `G(1e205)`'s sign as
  physically meaningful, without checking `err_estimate` or the
  integrand's provable non-negativity
- **defect_type:** numerical artifact (quadrature failure at extreme
  extrapolation) mistaken for a physical finding (docs/146 Category 9)
