# Answer key — task_009

**Tier:** A | **Category:** docs/146 #9 (numerical/software artifact mistaken for a physical result)

**The seeded defect:** `q(t)` is proven non-negative (asserted and
checked at sample points), so `Q(t)` — its cumulative integral — must
also be non-negative for any physically meaningful `t`. Integrating a
positive, rapidly-decaying integrand out to `t=1e12` with adaptive
quadrature (`quad`) spans roughly 12 orders of magnitude in the
integration variable relative to the function's own decay timescales
(the longest decay constant is 2.5e6 s) — exactly the kind of
extreme-dynamic-range integration that can produce small, spurious
negative results from adaptive-quadrature roundoff, independent of any
physical effect. The script's own `err_estimate` output is the tell:
if the reported error estimate is larger in magnitude than the "-4.7e-3
J" result itself, the negative sign is consistent with pure numerical
noise, not a real physical signal.

**Why this changes the correct answer:** the report interprets a
near-zero, sign-flipped numerical result as evidence of "a slow
parasitic heat-loss channel" — a real physical mechanism — without
first checking whether the result is within the integrator's own
reported error bars. This is docs/146 Category 9's own exact pattern
(the P122 `quad` returning a negative value for a provably non-negative
integrand at an extreme upper bound, `~1e205`): a numerical-method
artifact from spanning many orders of magnitude in one adaptive call,
mistaken for a content-bearing result before being checked directly.

**What a correct detection should name:** that `q(t)` was already proven
non-negative, so any negative `Q(1e12)` MUST be numerical error, not
physics — and that the correct next step is comparing the result's
magnitude to `err_estimate`, or re-running with tighter tolerances /
`quad`'s own `limit` parameter increased, before proposing any new
physical mechanism.

**Ground truth for the blind evaluator:** `defect_location` = the
"Interpretation" paragraph proposing a physical mechanism;
`defect_type` = numerical artifact mistaken for physics (Category 9).
