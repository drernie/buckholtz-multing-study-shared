# FINDING P147 — Horndeski's own gauge-invariant vector-curvature
# coupling fails on power law, not sign — and has no free coefficient
# left to fix it

**Date:** 2026-08-26
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 math
**Verdict:** `HORNDESKI-VECTOR-WRONG-POWER-LAW-NO-FREE-PARAMETER`
**Origin:** the one genuinely new, unexamined candidate `P146` surfaced —
Horndeski's (1976) uniquely-fixed, gauge-invariant non-minimal vector-
curvature coupling, checked here at the same leading (monopole) order
`P143` used for the minimal-coupling case.
**Script:** `P147_horndeski_vector_powercounting.py` (2 checks — one exact
symbolic computation, one explicitly-labeled dimensional estimate — ruff
clean, does not touch the 881-test suite)

---

## 1. What's being tested

`P146` established that if `A_μ` is a genuine gauge field (matching
`P143`'s own baseline), the *only* legal non-minimal coupling of `A_μ` to
curvature — fixed uniquely by gauge invariance and second-order (ghost-
free) field equations, per Horndeski (1976) — is

```
I(g,A) = −¼(F_μνF^κλR^μν_κλ − 4F_μκF^νκR^μ_ν + F_μνF^μνR)
```

built entirely from the field strength `F_μν`, never bare `A_μ`. Unlike
`P145`'s `R_μνA^μA^ν` (a free coefficient `λ`), this term's coefficient is
**not adjustable** — it's fixed by the theorem itself. This file checks
whether it reaches MULTING's target `1/r³` force at leading order, before
any question of sign can even arise.

## 2. Method — split by structure, treat each part honestly

The three-term combination splits cleanly by whether it involves the
Ricci tensor/scalar (established in `P145`/`P146` to vanish *away* from a
source, with delta-function support *at* one) or the full Riemann tensor
(whose vacuum part, the Weyl tensor, does *not* vanish away from a
source — the genuine long-range tidal field).

**Part 1 (rigorous):** the Ricci-based terms
(`−4F_μκF^νκR^μ_ν + F_μνF^μνR`), evaluated exactly at body B's
delta-function location, using the same `R_μν` coefficients established
in `P145`/`P146` (`R_00=4πGM_Bδ³`, `R_ij=4πGM_Bδ³δ_ij`) and body A's
standard field `A_0=k_A/(4π|x−x_A|)`. Every index-raising step carries a
positive control (e.g. `F²=−2E²` for a pure "electric" field, checked;
`R^0_0/R_00=−1` under raising with `η^00=−1`, checked).

**Part 2 (explicitly an estimate, not a derivation):** the Riemann/Weyl
term. Its two-body contribution requires integrating body A's `F²`
(peaked near A) against body B's Weyl tensor (smooth, `~GM_B/r³` in the
weak field) over all space — a genuine point-particle EFT matching
calculation (Goldberger–Rothstein-type), UV-divergent near body A's own
worldline. **Not attempted in full here** — the same category of
subtlety the second `P145` skeptic review flagged for `R_μνA^μA^ν`'s own
self-force pieces. What *is* done: an honest dimensional-scaling estimate
(if the finite, renormalized matching coefficient multiplies the leading
tidal scaling `R_Weyl(x_A)~GM_B/r³` directly — the simplest possible
matching structure), stated as an estimate, not a proof.

## 3. Result — a genuine surprise en route: one Ricci-based term cancels
## exactly

Computing `F_μκF^νκR^μ_ν`'s delta-function coefficient gave **exactly
zero** — not approximately small, an exact symbolic cancellation. Tracing
why: for a purely "electric"-type `F_μν` (only `F_0i` nonzero), the
contraction `F_μκF^νκ` is diagonal with equal-magnitude but
oppositely-signed timelike/spacelike-along-field entries — this is the
familiar tracelessness structure of the Maxwell stress tensor for a pure
field — and `R^μ_ν`'s own mixed-index coefficients (`R^0_0=−4πGM_Bδ³` vs.
`R^i_i=+4πGM_Bδ³`) alternate sign in exactly the pattern needed to cancel
it. A clean structural fact, verified by direct symbolic computation, not
assumed.

Only the Ricci-*scalar* term (`F_μνF^μνR`) survives, giving

```
V_ricci(r) = G_N M_B k_A² / (4π r⁴)     [n=−4, force ~ 1/r⁵]
```

**Two full powers of `r` steeper than the target `1/r²` potential
(`1/r³` force).**

For Part 2 (the Weyl-based estimate): `V_Weyl(r) ~ (const) × GM_B/r³`
(`n=−3`), giving **force ~ 1/r⁴ — one power steeper than target.**

**Neither piece reaches `1/r³`.**

## 4. Why this is a different class of failure than anything else in
## this P142 chain

- `P143` (minimal vector coupling, monopole order): needed `Δα=1` — one
  extra derivative in the vertex — a *fixable* gap, in principle
  addressable by a different (non-minimal) coupling structure. That's
  exactly what motivated checking `P145`/`P146`/this file in the first
  place.
- `P145`/`P146` (`R_μνA^μA^ν`): reached the target power law *exactly*
  (`Δα=0`), but the operator itself was inadmissible (not gauge-invariant)
  or non-generic (needed special Generalized-Proca tuning plus a
  disformal fix).
- **This file (Horndeski's own term):** reaches neither `Δα=0` nor a
  power law fixable by retuning a coefficient — the functional form is
  simply wrong (`1/r⁵` and `1/r⁴`, not `1/r³`), and **there is no free
  parameter left to adjust**, since Horndeski's coefficient is uniquely
  fixed by the theorem that makes the term admissible in the first place.
  Unlike every other candidate in this chain, this isn't a "wrong sign"
  or "needs tuning" failure — it's a "wrong shape, structurally, with
  nothing left to turn" failure.

## 5. What this file does NOT establish

1. **Part 2 is an estimate, not a proof.** The full Weyl-term
   contribution requires point-particle EFT matching this file does not
   perform. If that matching produced a genuinely different r-dependence
   than the simple "local matching times leading tidal field" structure
   assumed here, the conclusion for Part 2 specifically could change —
   Part 1's conclusion (exact, rigorous) would not.
2. **Higher-multipole or dipole-order couplings of Horndeski's term are
   not checked.** This file tests the same leading (monopole) order
   `P143` used for its own baseline — consistent with this chain's own
   established convention, but not exhaustive of every way this operator
   could enter a more elaborate completion.
3. **Does not touch MULTING itself** (Gate 1) — this is entirely about
   this project's own candidate completion.
4. **Does not close the Proca-type reading of `A_μ`** — this file is
   specific to the gauge-field reading `P146` §3 established; the
   Proca-type reading was already separately addressed in `P146` §4/§5.

## 6. Answer to P142's cheapest-test question, cumulative picture

With `P143` (derivative-cost), `P144` (static-vector-dipole collapse to
Branch S), `P145`/`P146` (R_μνA^μA^ν closed on admissibility/genericity
grounds), and now `P147` (Horndeski's own term fails on power law, no
free parameter), **every vector-mediator construction actually checked in
this chain has now failed, each for a genuinely different structural
reason** — derivative cost, EP-tension-by-reduction-to-Branch-S,
gauge/genericity inadmissibility, and now wrong functional form with a
fixed coefficient. This is the strongest form yet of `P142`'s own
"structural tension" hypothesis for the vector-mediator class
specifically: not one obstacle recurring, but the *entire class of
natural vector constructions* running out of road by different
mechanisms each time. The scalar-mediator space (Branch S/H, `docs/131`)
and the still-open two-scalar/TeVeS routes (`docs/123`'s own STILL-OPEN
list) remain the only unexhausted directions for `P142`'s decision tree.
