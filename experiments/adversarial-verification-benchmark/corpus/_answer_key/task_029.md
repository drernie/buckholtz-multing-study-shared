# Answer Key — Task 029

**Tier:** Clean negative control (no seeded defect)

## Ground truth

This is a clean, correctly-executed analysis — deliberately constructed
as the "correct" counterpart to Task 018's quadrature-overflow defect.
Checks a correct-flagging solving agent should confirm are actually
satisfied:

- The integration interval (0 to 120 days) is finite, bounded, and
  matches the actual physical domain of the problem (one wet season) —
  not an extreme, unphysical extrapolation like Task 018's `1e205`.
- The integrand (`q(t)`, a sum of two Gaussian pulses) is smooth and
  well-behaved over the entire integration domain — exactly the regime
  `quad`'s adaptive quadrature is designed for.
- `quad`'s own error estimate is explicitly checked and reported, and
  is many orders of magnitude smaller than the result — the report
  doesn't just assume reliability, it verifies it via the tool's own
  diagnostic.
- The result is cross-checked against an independent expectation
  (historical seasonal range, 1.5-2.0 million m^3) rather than accepted
  on numerical grounds alone.
- The individual pulse parameters are stated as validated against
  historical gauge data, not free-fit to hit a target total.

## Ground truth for the blind evaluator

- **defect_location:** none
- **defect_type:** none — this is a clean task; a correct response
  should not flag a numerical-artifact concern here (unlike Task 018,
  the integration domain and integrand behavior here are both squarely
  within `quad`'s reliable operating range, and the error estimate is
  correctly checked)
