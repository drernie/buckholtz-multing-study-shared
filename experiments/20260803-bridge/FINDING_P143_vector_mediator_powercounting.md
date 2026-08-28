# FINDING P143 — docs/131's vector-mediator dismissal upgraded from
# qualitative claim to a derived, positive-control-tested result

**Date:** 2026-08-26
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 math
**Verdict:** `VECTOR-MONOPOLE-ROUTE-REQUIRES-AT-LEAST-ONE-EXTRA-DERIVATIVE`
(corrected from an earlier draft's `...-REQUIRES-DERIVATIVE-COUPLING` +
"docs/131's dismissal is CONFIRMED" wording, per an independent skeptic
review, §3a below — same-day correction, not silently fixed)
**Origin:** first executed step of `P142`'s cheapest differentiating test
(does `docs/131`'s EP/ghost/staticity tension for CANDIDATE-L1 generalize
across alternative completion ansätze?)

---

## 1. Why this file

`docs/131` (CANDIDATE-L1 weak-field matching, 2026-07-22) computed two branches
with full sympy rigor (harmonic-induced, sombrero-fixed) and additionally
*asserted*, without computation, that a vector-mediated alternative "gives a
1/r (or Yukawa) potential, not 1/r³; a static 1/r³ from a vector needs
higher-derivative couplings → ghost." Re-reading `docs/131` in full before
starting `P142`'s actual derivation found this was the only one of its
several residual branches argued qualitatively rather than derived — this
file closes that gap.

## 2. Method

Standard Riesz-potential Fourier-transform identity: an isotropic momentum-
space propagator `~1/k^α` in 3 spatial dimensions gives a position-space
potential `~1/r^(3-α)`. Derived here via the standard reduction to a 1D
Mellin-transform-of-sine integral (`∫₀^∞ x^{s-1} sin(x) dx = Γ(s)sin(πs/2)`,
`s=2-α`), not asserted from memory.

**Target:** MULTING's own dipole term is source-confirmed as a *force*,
`F_d ∝ 1/r³` (`buckholtz-log.md`, direct preprint quote). Force = −d/dr
(potential), so the target potential exponent is `n=2` — exactly what
`docs/131`'s own Branch S already reaches via ordinary scalar multipole
structure (monopole potential `1/r` → dipole potential `1/r²`, zero exotic
input). This file asks a *different* question: what would a vector-charge
sourced *directly at monopole order* (not via multipole structure) need,
propagator-wise, to reach the same `n=2` target?

## 3. Positive control (exponent AND coefficient, not exponent alone)

`α=2` (standard massless propagator) must reproduce Newton/Coulomb `1/r`
exactly. A naive substitution at `α=2` hits a removable `0·Γ-pole`
singularity (`s=2-α=0`) and evaluates to `nan` — caught, not glossed over.
The correct limit: `lim_{α→2} Γ(2-α)sin(π(2-α)/2) = π/2`, giving a full
coefficient `1/(4π)` — an **exact** match to the textbook Newtonian Green's-
function normalization, not just the exponent. **PASSES**, on both axes.

## 4. Result

Solving `n(α)=3-α=2` gives `α=1` — one full power of momentum *fewer* than
the standard massless vector's `α=2`, i.e. the coupling vertex needs
`k^{+1}` *extra* in the numerator relative to the minimal coupling. One
extra momentum factor in a vertex = one extra spatial derivative in the
interaction: reaching MULTING's target force law via a vector-charge-at-
monopole-order mechanism requires a non-minimal, derivative-enhanced
coupling — Branch S's own multipole route needs no such modification
(`Δα=0`, by construction), so the two routes are genuinely different claims,
not restatements of each other.

### 3a. Scope correction (same day, independent skeptic review)

An earlier draft's verdict line read `...gives an actual derivation, ...
confirming docs/131's qualitative claim ('needs higher-derivative
couplings')` and `docs/131's vector-mediator dismissal is CONFIRMED`. An
independent context-asymmetric skeptic review (code + claim only, no
reasoning chain) caught a real conflation: **"requires ≥1 extra derivative"
is not the same claim as "higher-derivative" in the Ostrogradsky sense.** A
single-derivative vertex (a Pauli term, a derivative Yukawa coupling) is
completely standard field theory and is generically ghost-free —
Ostrogradsky's instability specifically concerns Lagrangians whose equations
of motion become higher than 2nd order, which `Δα=1` alone does not
establish. This file derives *only* the derivative-count requirement (the
premise `docs/131`'s own dismissal rests on), not the ghost conclusion
`docs/131` built on top of that premise — that remains a separate, textbook
check this file does not perform. The skeptic independently re-derived the
core Fourier-transform identity and the positive control from scratch and
confirmed both (§2, §3) fully; the only finding was this scope overreach in
the prose, not an error in the computation itself.

## 5. What this does NOT establish

1. **Not a full ghost proof.** Ostrogradsky's theorem (that non-degenerate
   higher-derivative Lagrangians generically propagate a ghost) is a
   textbook result, cited not re-derived here — this file establishes the
   *derivative-coupling* premise Ostrogradsky's theorem would then apply to,
   not the ghost conclusion itself. A genuinely ghost-free UV completion of
   this specific `k^{+1}` vertex is not ruled out in general (Horndeski-style
   degenerate constructions exist for *some* higher-derivative theories) —
   named as the natural next check, not attempted here.
2. **Scoped to monopole-order vector coupling specifically** — does not
   cover a vector field entering at dipole/multipole order itself (a
   genuinely different, unexplored ansatz class, not this file's question).
3. **Does not touch the sign/EP-tension question directly** — this file is
   about *power counting* (can the right r-dependence be reached at all,
   cheaply), a logically prior question to the sign question `docs/131`'s
   Branch S/H already settled for the scalar case.
4. Anything about MULTING itself (Gate 1) — both the scalar and vector
   constructions checked here are this project's own candidate completions.

## 6. Answer to P142's cheapest-test question, so far

One of the alternative-construction classes actually checked (vector,
monopole-order) requires a *different* kind of exotic input (derivative
coupling, informative but distinct from the EP-violation `docs/131`'s
scalar branches hit) to reach MULTING's target power law at all — it doesn't
even get far enough to face the same *sign* question Branch S/H faced. This
is consistent with — not yet proof of — `P142`'s hypothesis that the
obstruction is structural across constructions, but the *specific* obstacle
differs by construction class (derivative-coupling cost for vector-monopole,
EP-tension for scalar-dipole). Recorded honestly as a partial, not complete,
answer to the cheapest test.
