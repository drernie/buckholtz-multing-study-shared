# FINDING P147 — Horndeski's own gauge-invariant vector-curvature
# coupling fails on power law, not sign — no relative or overall
# coefficient rescaling can fix a wrong shape

**Date:** 2026-08-26
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 math
**Verdict:** `HORNDESKI-VECTOR-WRONG-POWER-LAW` — split by confidence, per
second independent skeptic review (§0 below): the Ricci-based piece is
`RIGOROUSLY-WRONG-POWER-LAW` (`1/r⁵`, exact symbolic computation,
independently re-verified by hand for a general axis); the Weyl-based
piece is `WRONG-POWER-LAW-PER-DIMENSIONAL-ESTIMATE` (`1/r⁴`, explicitly
not a full derivation, cross-checked but not proven).
**Origin:** the one genuinely new, unexamined candidate `P146` surfaced —
Horndeski's (1976) uniquely-fixed, gauge-invariant non-minimal vector-
curvature coupling, checked here at the same leading (monopole) order
`P143` used for the minimal-coupling case.
**Script:** `P147_horndeski_vector_powercounting.py` (2 checks — one exact
symbolic computation, one explicitly-labeled dimensional estimate — ruff
clean, does not touch the 881-test suite)

## 0. Second independent skeptic review (same day) — read this first

Independently re-derived both computations by hand — for Part 1, using a
**general** separation axis (not just the script's `x̂`-axis choice), and
confirmed the `F_μκF^νκR^μ_ν=0` cancellation is axis-independent, not a
coordinate artifact; for Part 2, cross-checked the dimensional estimate
via an independent momentum-space argument and a position-space
near-A/near-B/middle region decomposition, both agreeing with the file's
`1/r⁴` estimate and confirming the near-A (file's own) contribution
dominates at long range. **Verdict CONFIRMED to survive, with two
precision fixes applied** (folded into §3/§4 below): (1) the original
verbal explanation of *why* the Ricci-tensor term cancels was flat-out
wrong (claimed "oppositely-signed, traceless Maxwell-stress structure" —
actually same-signed and not traceless; the real mechanism is entirely
`R^μ_ν`'s own alternating sign under index-raising) — the *arithmetic*
was always right, only the prose explanation was wrong, now corrected;
(2) "no free coefficient left to adjust" overstated things — Horndeski's
theorem fixes the *relative* coefficients among its three terms, not an
overall Wilson coefficient, though rescaling that overall coefficient
cannot change a power law either, so the substantive conclusion is
unaffected. The skeptic also confirmed the logical structure is sound: a
positive result in *either* part (not both) would have overturned the
"no escape" framing, since the softer power law dominates at long range —
so the file's own requirement that *both* parts fail is the right
standard, not an inflated one.

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
zero** — not approximately small, an exact symbolic cancellation,
independently re-verified by hand (§0, second skeptic pass below) for a
general separation axis, not just the script's `x̂`-axis choice, so this
isn't a coordinate-choice artifact either.

**Mechanism, corrected (per second independent skeptic review — the
original description here was wrong, both parts of it):** for a purely
"electric"-type `F_μν` (only `F_0i` nonzero), the contraction
`F_μκF^νκ` is diagonal with entries `(−E²,−E²,0,0)` — **same-sign**
timelike and along-field-spacelike components, *not* oppositely-signed,
and this object is *not* traceless (its trace is `−2E²=F²≠0`; true
Maxwell-stress tracelessness requires subtracting `¼η^μ_νF²`, which this
raw contraction doesn't have). The actual cancellation comes entirely
from `R^μ_ν`'s own alternating sign under index-raising
(`R^0_0=−4πGM_Bδ³` vs. `R^i_i=+4πGM_Bδ³`, from `η^00=−1` vs. `η^ii=+1`):
the timelike piece (`FF[0,0]×R^0_0`, both negative → positive product)
exactly cancels the spatial trace piece (`Σ_iFF[i,i]×R^i_i`, negative
times positive → negative product, same magnitude). A clean structural
fact, verified by direct symbolic computation and confirmed by an
independent by-hand rederivation — but the earlier "Maxwell tracelessness"
framing was a wrong just-so explanation for a correctly-computed number.

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
  simply wrong (`1/r⁵` and `1/r⁴`, not `1/r³`). **Wording corrected per
  second skeptic review:** Horndeski's theorem fixes the *relative*
  coefficients among the three terms (`1, −4, 1`) — it does not forbid an
  overall Wilson coefficient `ξ` multiplying the whole combination.
  Rescaling `ξ` changes the interaction's *magnitude*, never its
  *r-power* — so the substantive point survives exactly as stated, just
  with the right reason: no *relative* tuning among Horndeski's fixed
  terms, and no *overall* rescaling either, can turn a `1/r⁴`-`1/r⁵`
  result into `1/r³`. Unlike every other candidate in this chain, this
  isn't a "wrong sign" or "needs tuning" failure — it's a "wrong shape,
  and no knob (relative or overall) changes a shape" failure.

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
