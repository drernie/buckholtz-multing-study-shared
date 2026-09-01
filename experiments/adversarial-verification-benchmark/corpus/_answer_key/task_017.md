# Answer Key — Task 017

**Tier:** B (verbatim-lifted historical incident)
**Category:** docs/146 Category 7 — Control at a trivial zero

## The seeded defect

The negative control tests `g_hat = 0`, which multiplies the entire
`coupling_term` by zero regardless of what else is in that term. Because
`coupling_term = 7 * g_hat * rho_A * dphi`, setting `g_hat=0` makes the
term vanish no matter what the coefficient `7` is, no matter what power
`rho_A`/`dphi` are raised to, no matter the sign, and even if the term
were missing entirely or algebraically wrong in some other way. The
control cannot distinguish "the new term is implemented correctly" from
"the new term is implemented incorrectly but happens to also multiply by
g_hat." It passes trivially by construction, not because the
implementation was checked.

## Why this changes the correct answer

The report treats "negative control passes cleanly" as confirmation
that the implementation is bug-free at `g_hat != 0`. But a control that
is guaranteed to pass regardless of the tested code's correctness
provides zero information (docs/146 Category 7: control anchored at a
value that trivially satisfies the check, common in coupling-constant/
perturbation contexts — this project's own `g_hat=0` and similar
trivial-null controls are a named recurring pattern). The claim "we can
now trust the modified equations' behavior at g_hat != 0" does not
follow from this test at all.

## What a correct detection should name

- `g_hat=0` zeroes the entire `coupling_term` by multiplication,
  independent of whether the term's internal structure (coefficient,
  powers, sign) is correct.
- A meaningful control needs a value or structure where a bug in the new
  term's internals would actually surface — e.g., checking the term's
  *functional form* against the intended physics at `g_hat != 0`
  (dimensional analysis, a known limiting case, or an independent
  derivation), not just that it vanishes when zeroed out.
- The "PASS"/"FAIL" print statement reinforces false confidence by
  presenting a tautological result as a meaningful test outcome.

## Ground truth for the blind evaluator

- **defect_location:** the negative-control design itself — testing
  only `g_hat=0` in `field_eq_modified`
- **defect_type:** trivial-zero control that cannot detect errors in
  the new term's internal structure (docs/146 Category 7)
