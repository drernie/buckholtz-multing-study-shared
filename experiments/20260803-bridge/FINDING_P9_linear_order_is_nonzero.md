# P9 — the exact background zero does not survive to linear order

**Date:** 2026-08-11 · does the actual calculation P6/P8/skeptic all named
as the real next step: extend `FINDING_dipole_shell_is_a_double_layer.md`'s
exact background (zeroth-order) calculation one perturbative order higher,
rather than assuming either answer.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P9_perturbed_shell_linear_order.py`, ruff clean, two positive
controls (Newton shell theorem; the original double-layer zero) both pass
exactly before anything new is trusted.

---

## 1. What was extended, and how

`FINDING_dipole_shell_is_a_double_layer.md` computed that a spherical shell
of *perfectly uniform, radially-aligned* dipole surface density is a double
layer: potential constant inside, exactly zero outside, every derivative
vanishing off the shell. That result is explicitly for a perfectly isotropic
shell — its own §"What this does NOT mean" named the cosmological/perturbed
case as "the obvious next question, not answered here."

This finding reconstructs the exact same numerical method (direct
quadrature of the dipole surface-layer potential over a sphere) and adds a
small angular perturbation to the dipole density,

```
tau(theta') = tau0 * (1 + eps * cos(theta'))
```

— the natural leading (l=1) correction if the induced dipole strength
tracks an external direction, e.g. a local density-perturbation gradient.
Before trusting any new result, two positive controls were run and matched
exactly: a monopole shell reproduces Newton's shell theorem (`2/a` inside,
`2/r` outside); the *uniform* dipole shell reproduces the original finding's
double layer (constant inside, exactly zero outside, to machine precision).

## 2. The result: nonzero, linear, ordinary-dipole falloff

```
Phi_outside(north pole, r=2a)   = +5.235988e-02
Phi_outside(south pole, r=2a)   = -5.235988e-02
Phi_outside(equator,   r=2a)    =  ~0 (numerical noise, 1e-16)
```

Antisymmetric north/south, zero on the equator — the standard external
dipole-field angular pattern. Two checks confirm this is real, not an
artefact:

- **Linear in the perturbation.** `Phi/eps` is constant (`1.047198`) across
  `eps=0.01` to `0.20` — six significant figures, no drift. This is a
  genuine `O(δ)`-type effect, not a higher-order or numerical spurious term.
- **Falls off as an ordinary point dipole.** `Phi·r²` is constant
  (`0.209440`) across `r=1.2a` to `8a` — the perturbed shell's exterior
  field behaves exactly like a single point dipole's `1/r²` potential.

A second check with an `l=2` (quadrupole-type) angular perturbation,
`tau(θ')=τ₀(1+ε·P₂(cos θ'))`, also gives a nonzero exterior potential
(positive at the poles, negative at the equator) — **no angular
perturbation tried preserves the exact background zero.**

## 3. What this resolves — and what it still does not give

**Resolves:** P8's "undetermined — could plausibly be zero (if the
background's orientation-averaging symmetry survives to first order) or
nonzero (if it does not)" is resolved toward **nonzero**. The exact
cancellation found for the perfectly isotropic background is fragile — it
depends on exact angular uniformity, and breaks under any angular
asymmetry, linearly, in the direction that intuition (and P6's original
argument) expected. This directly validates the physical picture P6 started
from and P8's skeptic review left open: perturbing the density does restore
a genuine, non-contact, long-range force at `O(δ)`.

**Does NOT resolve:** the actual numerical coefficient. `ε` here is a bare
geometric parameter — "how much does the shell's dipole density vary in
strength with angle" — not yet connected to a physical relationship between
`ε` and `κ`, `k`, `∇δ`. Converting this geometric result into an actual
`ΔG_eff/G` forecast requires that connection, which has not been made.
**P8's retracted `~7×10⁻⁶` number is NOT restored by this finding** — this
result supports the *qualitative* direction (nonzero) that number assumed,
but does not supply or validate its *magnitude*.

**Not tested here:** the random-orientation (intrinsic, uncorrelated)
branch's own perturbative extension — whether partially correlating random
orientations with an external direction (the analogue of intrinsic-
alignment tidal correlation in weak lensing) gives a comparable nonzero
result. Only the radially-aligned branch (the one this project's own
two-charge completion derived as matching MULTING's actual `A↔B`-symmetric
`F_d`) was tested.

## What this does NOT establish

1. **A specific ΔG_eff/G value.** See §3 — this is a qualitative (zero vs
   nonzero) resolution with a verified functional form, not a magnitude.
2. **That this connects correctly to MULTING's actual physics.** The
   perturbation `ε` is a geometric toy parameter on a shell, standing in
   for "however a real density perturbation modulates the induced dipole
   density." The actual physical size of that modulation, for a real
   cosmological `δ`, is a separate, unaddressed question.
3. **The random-orientation branch's behavior**, per §3.
4. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction
   (the shell/double-layer toy model built from P1's two-charge
   completion), not a claim about TJB's own theory.

## Reproduction

```bash
python experiments/20260803-bridge/P9_perturbed_shell_linear_order.py
```

Two `assert` positive controls (Newton shell theorem; original double-layer
zero) must pass before the script proceeds — if either fails, the method
itself is broken and nothing downstream should be trusted.
