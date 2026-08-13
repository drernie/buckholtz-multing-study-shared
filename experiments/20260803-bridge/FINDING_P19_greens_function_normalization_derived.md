# P19 — the project's own dipole ansatz was missing the standard 1/4π Green's-function normalization; this closes one narrow piece of P18's gap, not the piece its skeptic actually raised

~~the missing geometric normalization is derived (1/4π, matching the
textbook dipole potential), and proven r_min-independent by construction,
not merely checked for one assumed form~~ **[CORRECTED after skeptic
review — retitled]**

**Date:** 2026-08-12 · corrected 2026-08-12 after context-blind skeptic
review · originally set out to answer `FINDING_P18`'s remaining open
item: the cross/self ratio cancellation was shown to hold only
*conditionally*, on the missing normalization constant being "a pure,
`r_min`-independent overall multiplier" — a plausible but unproven
assumption.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P19_greens_function_normalization.py`, ruff clean. Three
asserts (Green's function solves Laplace's equation away from the origin;
derived dipole potential matches the textbook form; the ratio to the
project's own prior convention is exactly `4π`) must pass before the
verdict is trusted.

**[CORRECTED after skeptic review — read before the rest of this file]**
A context-blind skeptic review independently re-derived the physics from
the action itself (variation + integration by parts) and confirmed it
CONFIRMED-REAL: the Green's function, the dipole potential, and the `4π`
ratio are all correct. But the interpretive claim was WEAKENED for two
distinct reasons this version corrects: (1) "derives, not assumes"
overstated novelty — `1/(4π)` is the same standard textbook Green's-
function normalization used throughout ordinary electrostatics (same
origin as `1/(4πε₀)`), not a new physics result; softened to "identifies."
(2) "Resolves `FINDING_P18`'s conditional gap" overreached in two ways:
it does not touch the renormalization/regularization concern P18's own
skeptic actually raised (a question about the energy *integral's*
structure, not `φ`'s field-equation normalization — a separate step this
finding never addresses), and it misses a genuinely new concern the P19
skeptic found: `E_self=∫_{r≥r_min}|∇φ|²d³x` is *dominated* by `r~r_min`
(integrand `~1/r⁶`, weighted by `r²dr`, giving the `1/r_min³` scaling) —
exactly the region where the point-dipole idealization used to derive
`1/(4π)` is weakest for a real, physically extended source. Both points
corrected below.

## Scope limit, stated up front

This identifies and verifies **one piece** of the missing normalization
`FINDING_P17` found — a pure **number**, `1/(4π)`, the standard
Green's-function normalization this project's own ansatz was missing —
and shows the point-source coefficient itself is `r_min`-independent.
**This does NOT resolve
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

**Step 3 — is this specific coefficient `r_min`-independent?** Not just
checked for one assumed form (as `FINDING_P18`'s Part 3 sensitivity check
did) — argued structurally, for the point-source idealization. The
Green's function `G(x)` solves `∇²G=δ³(x)`, a property of the field
equation **alone**, fixed once and for all, with no reference to any
particular source's physical extent. `r_min` never appears in this
derivation at all — it enters *later*, only as the lower limit of the
energy integral (`r≥r_min`), *after* `φ` is already fully determined.
Since `1/(4π)` comes entirely from solving `∇²G=δ³(x)` for an exact point
source — an equation `r_min` cannot appear in — **the `1/(4π)`
coefficient itself is `r_min`-independent for the point-dipole
idealization**. See §"What this does NOT establish" for why this narrower
statement is not the same as fully settling `r_min`-independence for the
physical (finite-size) self-energy calculation.

## Result

~~Resolves `FINDING_P18`'s conditional gap for the geometric piece of the
missing normalization~~ **[CORRECTED after skeptic review.]** **Closes
one narrow piece of `FINDING_P18`'s conditional gap**: the pure-number
`1/(4π)` Green's-function coefficient is `r_min`-independent for the
point-dipole idealization, with a structural reason rather than a checked
example. It does **not** close the piece `FINDING_P18`'s own skeptic
review actually raised.

**Two distinct things remain unaddressed, not one:**

1. **The renormalization/regularization concern.** `FINDING_P18`'s
   skeptic pointed out that `E_self`'s UV-divergent character (needing
   the `r_min` cutoff at all) is the classic sign of a quantity needing a
   renormalization counterterm — which would live in how the *energy
   integral itself* is regularized, a separate step from `φ`'s own
   field-equation normalization. Deriving `φ`'s coefficient (this
   finding) does not touch that separate step at all. In this project,
   `r_min` is used as a genuine physical cutoff (never taken to zero), so
   no calculation performed so far actually needs a counterterm — but
   this finding does not establish that as a general fact, only observes
   it is not currently triggered.
2. **[Added after skeptic review — a distinct, new concern.] Near-`r_min`
   multipole corrections.** `E_self=∫_{r≥r_min}|∇φ|²d³x` is *dominated*
   by the region `r~r_min` (integrand `~1/r⁶`, weighted by `r²dr`, giving
   the overall `1/r_min³` scaling) — precisely where the point-dipole
   idealization used to derive `1/(4π)` is weakest for a real,
   physically-extended source of size `r_min`. Multipole corrections to
   the field of a genuinely extended dipole distribution are largest near
   the source's own physical edge. The `1/(4π)` coefficient itself is
   unaffected by this (it's fixed by the far-field, point-source limit of
   the field equation), but the *actual* self-energy of a real extended
   cluster could still receive additional, `r_min`-dependent corrections
   beyond a uniform multiplier — a possibility this finding does not rule
   out, distinct from the renormalization concern above.

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
4. **[Added after skeptic review.] That the finite-size (real, extended
   cluster) self-energy is unaffected by `r_min`-dependent corrections.**
   `E_self` is dominated by `r~r_min`, exactly where the point-dipole
   idealization used here breaks down most for a genuinely extended
   source — see Result §2. This finding only establishes `r_min`-
   independence for the point-source coefficient, not for the full,
   physically-realistic self-energy integral.
5. **[Added after skeptic review.] That this is a novel physics
   derivation.** `1/(4π)` is the same standard Green's-function
   normalization used throughout ordinary electrostatics (same origin as
   `1/(4πε₀)`) — this finding identifies that this project's own ansatz
   was missing it, not a new physical result.
6. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction,
   not a claim about TJB's own unpublished theory.

## Skeptic verdict (Step 8a, context-blind — claim + code + cited files only)

Two separate verdicts, not merged:

**(1) Math/physics content: CONFIRMED-REAL.** The skeptic independently
re-derived `φ_dipole=p·∇G` from the action itself (variation of `φ`,
integration by parts on the `p·∇φ(x_i)` coupling term, solving the
resulting Poisson equation) — matching this finding's construction
exactly, not merely accepting it. Hand-verified all reported numerics to
the claimed tolerances. One minor note: the third assert (the `4π` ratio
check) is largely a restatement of the setup — since the "textbook form"
comparison target already contains `1/(4π)` by definition, the ratio
equaling `4π` follows close to automatically; asserts 1–2 (the Green's
function itself, and the positive-control match) carry the real content.

**(2) Interpretive claim ("derives... resolves P18's conditional gap for
the geometric piece"): WEAKENED.** Two distinct overclaims, both
corrected above: (a) "derives" overstated novelty for what is a standard
textbook result applied to this project's own coupling for the first
time — softened to "identifies" throughout. (b) "Resolves" the P18 gap
overstated reach in two ways — it does not touch the renormalization
concern P18's own skeptic actually raised (a separate question about the
energy integral's regularization, not `φ`'s normalization), and it
misses a new concern the P19 skeptic found: `E_self`'s dominance by
`r~r_min` is exactly where the point-dipole idealization is weakest for a
real extended source, so `r_min`-independence of the coefficient does not
guarantee `r_min`-independence of the full physical self-energy. Applied
per Response Matrix: retitled (Fix), "derives"→"identifies" throughout
(Fix), Result section split into "closes one narrow piece" vs. two
distinct remaining concerns (Fix), new "does NOT establish" items 4-5
added (Fix). No response fell to core-predicate-false — the `1/(4π)`
identification and its narrow `r_min`-independence argument for the
point-source coefficient survive fully intact.

## Reproduction

```bash
python experiments/20260803-bridge/P19_greens_function_normalization.py
```

All three asserts must pass before the verdict is trusted.
