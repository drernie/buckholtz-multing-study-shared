# P45 — Minimal `V(φ)=λφ⁴/4`: reopens `w_φ≠1` and closes P44's stability loop, without the P11 conflict originally expected

**Date:** 2026-08-14
**Status:** Built, run, ruff clean, all assertions pass.
**Pending context-blind skeptic review (Step 8a) — not yet run.**
**Origin:** thirteenth step of the covariant-completion campaign
(`PLAN_final_goal_20260814.md`), third and final of three
symmetry/action-theoretic checks the user authorized in sequence
("го все по очереди"). Directly closes P34's own §4 point 8 gap
(canonical no-potential scalar is a forced stiff fluid, `w_φ=1`) and
P44's own corrected requirement (`V` must be non-quadratic for a
solution-specific stability question to exist at all).
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P45_minimal_potential_stiff_fluid_escape.py`, ruff clean,
all assertions pass.

## 0. A scope check performed before choosing `V`, not after

An earlier working assumption carried into this session (from an
interrupted pre-compaction summary) held that adding *any* `V(φ)` here
would collide with `FINDING_P11`'s masslessness requirement. Before
writing any code, `FINDING_P11` was re-read directly (Gate 1 discipline —
never recall a prior finding's exact claim from memory). **That
requirement is about the κ/dipole-sector mediator** (`β_q/β_d=√6/2 ⟺
Λ=3/2`, requiring an exactly-massless Green's function in that sector) —
a different sector from the monopole-sector `φ` studied throughout
`P34`–`P44`. **The expected conflict does not apply**, corrected here
before it could become a silent, uninspected premise. The real,
applicable constraint is self-contained: adding a *mass term*
(`V''(0)≠0`) would turn `FINDING_P35`'s long-range Coulomb-like
`φ(r)=ĝM/(4πr)` into a short-range Yukawa profile — that is what
actually needs checking, done in Part 2 below.

## Part 1 — the chosen `V(φ)=λφ⁴/4`, both required properties verified

Two properties required, both checked symbolically (not asserted):

```
V(φ)    = λφ⁴/4
V'(φ)   = λφ³
V''(φ)  = 3λφ²
V'''(φ) = 6λφ   (nonzero for φ≠0)
```

- **`V''(0)=0`** — massless at the natural vacuum, unlike a mass term
  `m²φ²/2` whose `V''=m²` is nonzero everywhere (script assertion).
- **`V''(φ)` genuinely `φ`-dependent** (not constant) — satisfies
  `FINDING_P44`'s own corrected requirement that `V'''≠0` somewhere for a
  solution-specific stability question to exist at all (script assertion).

## Part 2 — field equation re-derived, `λ=0` positive control, and the residual on P35's own solution

Euler-Lagrange (not by hand) on `L` with `−λφ⁴/4` added gives:

```
φ̈ − ∇²φ + λφ³ = ĝρ
```

**At `λ=0`: reduces exactly to `FINDING_P35`'s own `φ̈−∇²φ=ĝρ`**
(script assertion, positive control).

Plugging `P35`'s own static solution `φ₀(r)=ĝM/(4πr)` into the *new*
equation, for `r>0`:

```
λφ₀(r)³ = M³ĝ³λ/(64π³r³)   — NONZERO
```

`φ₀(r)` is no longer an *exact* solution once `V` is added — only
approximate, valid when this residual is small compared to the other
terms, i.e. `λφ₀²≪1` near the source. This is a *more restrictive*
version of the same `ĝφ≪1` perturbative regime `FINDING_P34` already
uses throughout — not a new assumption. **Solving the full nonlinear
equation is not attempted here — flagged explicitly as future work.**

## Part 3 — `δ²L` now genuinely depends on the background, closing P44's loop

Redoing `FINDING_P44`'s own generic-background second-variation
calculation with `V(φ)=λφ⁴/4` included:

```
d²L/dε²|_(ε=0) = δ̇²−(∇δ)² − 3λφ_bg²δ²
∂/∂φ_bg (above) = −6λφ_bgδ²   — NONZERO
```

**Confirmed: `L₂` now genuinely depends on `φ_bg`** (script assertion) —
unlike `P44`'s `V=0` case. This closes the loop `P44` predicted: "is
*this* solution stable" is now a well-posed, solution-specific question.
**Not answered here** — that would require evaluating at the actual
`φ_bg=φ₀(r)` and checking the sign of the resulting mass-squared term,
which is a genuine next step beyond this three-step authorized sequence.

## Part 4 — is `w_φ=1` still forced?

Using the same `ρ_φ=(1/2)φ̇²+V`, `p_φ=(1/2)φ̇²−V` formula that reproduces
`FINDING_P34`'s own `V=0` result exactly (`ρ_φ=p_φ=φ̇²/2` — checked
first, before trusting the formula for `V≠0`):

```
w_φ = p_φ/ρ_φ = (2φ̇²−λφ⁴) / (2φ̇²+λφ⁴)
λ=0:                              w_φ = 1   (P34's forced stiff fluid)
kinetic-dominated (φ→0):          w_φ → 1   (recovers P34's dead end)
potential-dominated (φ̇→0):        w_φ → −1  (de-Sitter-like)
```

**`w_φ=1` is no longer forced** — it now depends on the actual balance of
kinetic vs. potential energy along the solution's own trajectory. Both
limits are structurally available. **This does not show the actual
dynamics of this system (with the `ĝρ` source term driving `φ`) reaches
the potential-dominated regime** — that requires solving the modified
EOM from Part 2 for specific initial conditions, a dynamical-systems
question not attempted here.

## What this establishes, precisely

1. A minimal `V(φ)` that satisfies both the requirement `FINDING_P44`
   derived (non-quadratic `V''`) and preserves `FINDING_P35`'s static
   solution at leading order (Parts 1–2), verified symbolically.
2. `δ²L` now genuinely depends on the background — the solution-specific
   stability question `P44` predicted now exists, but is not answered
   (Part 3).
3. `w_φ=1` is no longer forced by the theory — both the stiff-fluid dead
   end and a de-Sitter-like limit are structurally available (Part 4).
4. A prior expected conflict with `FINDING_P11`'s masslessness
   requirement, checked directly against `P11`'s own text and found not
   to apply — the requirement is about a different sector (§0).

## What this does NOT establish

1. **That this system's actual dynamics reaches the potential-dominated
   (accelerating) regime** — Part 4 shows the possibility is reopened,
   not realized; that requires solving the modified EOM for specific
   initial conditions.
2. **Whether the specific static solution `φ(r)=ĝM/(4πr)` is stable once
   `V` is added** — Part 3 shows the question is now well-posed, not that
   it has been answered either way.
3. **A full nonlinear static solution once `λ≠0`** — Part 2 shows `φ₀(r)`
   is only an approximate solution in the `λφ₀²≪1` regime; the exact
   modified solution is not derived.
4. **That `λφ⁴/4` is the unique or "correct" minimal `V(φ)`** — it is *a*
   choice satisfying the two required properties, explicitly flagged as
   such; other non-quadratic, massless-at-origin choices (e.g. `φ⁶`)
   would also qualify and were not compared.
5. **Anything about the κ (dipole) sector** — monopole (`g`) sector only,
   matching every prior finding in this sub-arc.
6. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction,
   not a claim about TJB's own unpublished theory.

## Reproduction

```bash
python experiments/20260803-bridge/P45_minimal_potential_stiff_fluid_escape.py
```
