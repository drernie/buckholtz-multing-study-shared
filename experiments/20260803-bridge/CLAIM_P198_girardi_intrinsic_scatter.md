# CLAIM P198 — Girardi et al. (1998)'s own internal R_c inconsistency:
# does it, propagated, move `P196`'s own residual?

**Date:** 2026-09-06
**Continues:** `FINDING_P197` (mass-measurement systematics real but
does not close the gap); this file is candidate 2 of 2 named in
`FINDING_P196_ADDENDUM2`.
**Authorization:** explicit user go-ahead ("сделай это по очереди
действуй автономно"), 2026-09-06, naming Girardi's own intrinsic
scatter as candidate 2 of 2.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive.

## What is already verified this session (primary source, re-confirmed,
## not re-fetched)

`[VERIFIED-arXiv:astro-ph/9804187]`, Girardi et al. (1998), already
fully fetched earlier this session (used for `P196`'s own Positive
Control 1): their headline `R_vir=0.002σ_P` coefficient (Eq. 11) is
derived (Eq. 9+10) using a core radius `R_c=0.17 h⁻¹Mpc`, explicitly
attributed to **Girardi et al. (1995, "G95")** — an earlier paper's
value, obtained via a cruder cluster-centering method (averaging
galaxy coordinates).

**Later in the SAME paper (§4.3)**, applying their own improved
centering method (a 2D kernel-density peak, not galaxy-coordinate
averaging) to their own 170-cluster sample, they find a **substantially
smaller** core radius: `R_c = 0.05⁺⁰·⁰¹₋₀.₀₁ h⁻¹Mpc` (90% CL) — about
**1/3** of the G95 value used to derive their own headline formula.
Their own explanation, quoted directly: *"We verify that this
difference is due to the fact that we determine cluster centers from
the galaxy density peak... rather than from averaging galaxy
coordinates... in agreement with the suggestion of Beers & Tonry
(1986) that large core radii can be produced by inaccurate cluster
centers."*

**This is a real, internal inconsistency in Girardi et al.'s own
paper, not a construction of this project**: the paper's own headline,
most-cited formula (Eq. 11, `R_vir=0.002σ`) is built on an `R_c` value
their own later, improved analysis (same paper) suggests is too large
by a factor of `~3`.

## New estimand element specific to this file

**Method**: reuse `P196`'s own already-built, already-verified
self-consistency solver (`test_positive_control_girardi_formula_self_
consistent`, which solves Eq. 5 + spherical-collapse density criterion
+ Eq. 10, self-consistently at `A=R_vir`, to derive the implied
`R_vir/σ` coefficient from first principles) — but substitute Girardi's
own improved `R_c=0.05⁺⁰·⁰¹₋₀.₀₁ h⁻¹Mpc` (§4.3) in place of the G95
value (`0.17 h⁻¹Mpc`) the published Eq. 11 actually used.

**Honest methodological caveat, stated before running, per this
project's own no-overclaim discipline**: Eq. 10's own `R_PV(A)` formula
was itself *fit* by G95 using G95's own cluster sample and G95's own
(larger) `R_c` convention. Substituting a different `R_c` from a
different analysis into that same formula is a **sensitivity test of
Eq. 11's own `R_c`-dependence**, not a claim that this substitution is
the physically correct or endorsed procedure — Girardi et al.
themselves never re-derived Eq. 11 with their own improved `R_c`. This
file tests what their formula's own internal sensitivity implies, not
what the "correct" coefficient is.

**Endpoint 1**: the implied `R_vir/σ` coefficient using
`R_c=0.05, 0.04, 0.06` h⁻¹Mpc (median and 90% CL bounds), compared to
the published `0.002`.

**Endpoint 2**: re-run `P196`'s own full pipeline with the corrected
coefficient(s), report the resulting mean `ratio_2b` and scatter
against `P196`'s own `1.4665`/`11.1%` baseline.

**Falsifiable predicate**: if the `R_c=0.05`-based coefficient moves
`ratio_2b` into `P196`'s own pre-registered MCID band `[0.95,1.05]`,
this is a real, substantial contributor to the residual. If not,
candidate 2 is also structurally narrowed, same discipline as
candidates already tested.

**MCID**: reused unchanged from `CLAIM_P196`.

## Positive control

Reuse `P196`'s own already-passing `test_positive_control_girardi_
formula_self_consistent` at the PUBLISHED `R_c=0.17` first, confirming
it still reproduces `0.002` to `<5%` before trusting the same solver
machinery at the substituted `R_c=0.05`.

## What this does NOT establish

1. Does not claim Girardi et al.'s own published `0.002` coefficient is
   wrong — only that their own paper's later, improved analysis
   suggests a real internal sensitivity worth quantifying.
2. Does not re-derive Eq. 10 itself (`R_PV(A)`) — reuses it as
   published, substituting only the `R_c` value fed into it, an
   explicit, named approximation (see caveat above).
3. Does not propagate the King-profile exponent `α`'s own quoted
   uncertainty (`0.70⁺⁰·⁰⁸₋₀.₀₃`) — `α` does not enter Eq. 10's own
   functional form directly (it enters the earlier derivation of Eq.
   10 itself, a step further removed) — out of scope for this file.
4. Does not draft or send anything to TJB.
5. `NO_AUTHOR_ERROR`.
