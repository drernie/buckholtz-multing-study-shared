# P19 — the missing geometric normalization is derived (1/4π, matching the textbook dipole potential), and proven r_min-independent by construction, not merely checked for one assumed form

**Date:** 2026-08-12 · direct follow-up to `FINDING_P18`'s remaining open
item: the cross/self ratio cancellation was shown to hold only
*conditionally*, on the missing normalization constant being "a pure,
`r_min`-independent overall multiplier" — a plausible but unproven
assumption. This finding derives, rather than assumes, one real piece of
that missing normalization directly from the action's own field equation.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P19_greens_function_normalization.py`, ruff clean. Three
asserts (Green's function solves Laplace's equation away from the origin;
derived dipole potential matches the textbook form; the ratio to the
project's own prior convention is exactly `4π`) must pass before the
verdict is trusted.

## Scope limit, stated up front

This derives and verifies **one piece** of the missing normalization
`FINDING_P17` found — a pure **number**, `1/(4π)`, coming from the
Green's function's own geometric normalization — and proves it is
`r_min`-independent by construction. **This does NOT resolve
`FINDING_P17`'s full dimensional problem** (`Ω_φ` has units `kg/m`, not
dimensionless). `1/(4π)` is a pure number, not a quantity with physical
units, and cannot by itself fix a units mismatch. A separate, still
completely open problem remains: a genuinely *dimensional* constant,
needed to make the action's own kinetic term `(1/2)(∂φ)²` dimensionally
consistent as an energy density in the first place. Do not read this
finding as resolving `FINDING_P17`. Per NO_AUTHOR_ERROR: entirely about
this project's own reconstruction.

## The gap this addresses

Every finding that used a point-dipole field (`FINDING_P9`, `P11`, `P12`,
`P14`, `P15`, `P16`) used the ansatz `φ=p·cosθ/r²`, without deriving it
from this project's own action:

```
S = ∫d⁴x (1/2)(∂φ)² + Σᵢ ∫dτ [g·mᵢ + pᵢ·∇]φ(xᵢ)
```

`FINDING_P18` showed the cross/self ratio cancels a missing
normalization constant `C` *only if* `C` is a pure, `r_min`-independent
overall multiplier — flagged as a named assumption, not established.

## Method

**Step 1 — solve the field equation's Green's function directly.** For a
static point source, the field equation from varying `φ` in the action
above reduces to the standard 3D Poisson equation. The Green's function
`G(x)=-1/(4πr)` (the standard textbook result — electrostatics, Newtonian
gravity) is verified directly: `∇²G=0` away from the origin, checked by
symbolic differentiation, not quoted.

**Step 2 — derive the dipole potential.** For the action's own `p·∇φ`
coupling, a static point dipole sources `φ=p·∇G` (the standard
derivative-of-Green's-function construction). Computed symbolically:

```
phi_dipole (p along z) = p*z/(4*pi*(x**2+y**2+z**2)**(3/2))
```

**Positive control** — does this match the well-known textbook
dipole-potential form `p·cosθ/(4πr²)` (structurally identical to the
standard electrostatic/magnetostatic dipole potential)?

```
derived, numeric  : 0.0132306499
textbook form     : 0.0132306499     <- exact match
```

**Comparison to what every prior finding actually used** (`φ=p·cosθ/r²`,
no `1/(4π)`):

```
ratio (project_used / field-equation-derived) = 12.566371
4*pi                                          = 12.566371    <- exact match
```

**Every prior `E_self`/`U_cross` number in this project's bridge track is
missing exactly this `1/(4π)` geometric factor.**

**Step 3 — is this piece of the normalization `r_min`-independent?** Not
just checked for one assumed form (as `FINDING_P18`'s Part 3 sensitivity
check did) — argued structurally. The Green's function `G(x)` solves
`∇²G=δ³(x)`, a property of the field equation **alone**, fixed once and
for all, with no reference to any particular source's physical extent.
`r_min` never appears in this derivation at all — it enters *later*,
only as the lower limit of the energy integral (`r≥r_min`), *after* `φ`
is already fully determined. Since `1/(4π)` comes entirely from solving
`∇²G=δ³(x)` — an equation `r_min` cannot appear in — **this piece of the
normalization is `r_min`-independent by construction**, for any source
configuration (a single dipole's self-energy, or a pair's cross-term)
built from it.

## Result

**Resolves `FINDING_P18`'s conditional gap for the geometric piece of
the missing normalization** — with a structural reason (r_min cannot
enter a derivation that never involves it), not merely a checked example.
The cross/self ratios in `FINDING_P15`/`FINDING_P16` are unaffected by
this specific factor: it is a pure number, cancels in any ratio
regardless of `r_min`, confirmed structurally rather than only for the
one form `FINDING_P18` tested.

**What remains unresolved, and is likely the larger piece:**
`FINDING_P18`'s skeptic review raised a second, distinct possibility —
that the fix could instead resemble a renormalization counterterm tied
to `E_self`'s own UV divergence as `r_min→0`. This finding does not fully
rule that scenario out in general, but notes: in this project, `r_min` is
used throughout as a genuine **physical** cutoff (the cluster's own
finite size), never taken to zero — so there is no actual divergence
being renormalized away in any calculation this project has performed.
Whether a hypothetical, never-attempted `r_min→0` limit would require
additional, `r_min`-dependent structure is a separate question this
finding does not need to answer for the calculations already done.

## What this does NOT establish

1. **`FINDING_P17`'s full dimensional problem.** `1/(4π)` is a pure
   number; the missing *dimensional* constant needed to make `Ω_φ` truly
   dimensionless remains completely unresolved.
2. **A corrected numeric value for `Ω_φ` or `κ_cosmo_bound`.**
   Deliberately not computed here — doing so would risk implying the
   dimensional problem is fixed, when only one (non-dimensional) piece of
   it is addressed.
3. **A general proof that NO possible form of the missing constant could
   be `r_min`-dependent.** Only the specific geometric (Green's-function)
   piece derived here is shown to be `r_min`-independent; a separate,
   still-undiscovered dimensional constant could in principle carry
   different structure, though no candidate for one has been proposed
   anywhere in this project.
4. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction,
   not a claim about TJB's own unpublished theory.

## Reproduction

```bash
python experiments/20260803-bridge/P19_greens_function_normalization.py
```

All three asserts must pass before the verdict is trusted.
