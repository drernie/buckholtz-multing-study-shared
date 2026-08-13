# P26 — the "Level 3" covariant-action route: T_μν gives a real ρ_φ, but its equation of state is curvature-like (w=-1/3), not dark-energy-like

**Date:** 2026-08-13
**Origin:** user-directed roadmap (P24→P27), third item — "Level B": derive
cosmology from the action itself (`S → T_μν → ρ_φ,p_φ → H(z)`), not the
old manual force-to-`H(z)` bridge. Before building this blind, checked the
project's own prior context — found this is the long-deferred endpoint of
the *entire* bridge programme, not a fresh question.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P26_stress_tensor_equation_of_state.py`

## 0. Context chain — this question has a real history in this project

1. **`FINDING_effective_fluid_energy_scale.md` (2026-08-03)** — the naive
   statistical-mechanics "pair-fluid" bridge (MULTING potential →
   Layzer–Irvine energy → `ρ_pair` → `H(z)`) fails by **4–5 orders of
   magnitude**. Its own closing table says explicitly: *"the covariant-
   action route of level 3 [is] the only surviving route."* P26 is that
   route, six weeks and 25 findings later.
2. **P1 §4.3 (2026-08-10)** — the *force* on a test particle from an
   isotropic, randomly-oriented shell of dipoles averages to **exactly
   zero** (the "double layer," `FINDING_dipole_shell_is_a_double_layer.md`)
   — a narrower, **first-moment** result about forces, not energy density.
3. **P13a (2026-08-12, corrected)** — explicitly flags that a zero mean
   *force* (`⟨δ⟩=0`) does **not** imply zero *energy density* or power
   spectrum (`P(k)=0`) — names this the genuinely open next calculation.
4. **P14 (2026-08-12)** — computes the self-energy channel, but its own
   corrected §1 flags a real, unresolved tension: does self-energy survive
   ensemble averaging, or does it cancel against cross-terms the way P9's
   idealized *continuous* shell does?
5. **P15/P16 (2026-08-12)** — **resolve** that tension for realistic,
   *discrete* populations: self-energy is real and **dominant** over
   cross-terms (~4×10⁻⁵ to 1.4×10⁻⁴) at realistic cluster separations. The
   continuum cancellation P9 found does not extend to the physically
   realistic discrete case.

Given (5) already resolves (4)'s tension in favor of "self-energy
survives," this finding does what (3) named as open: compute `T_μν`
directly and extract the equation of state.

## 1. Method

Canonical stress tensor `T_μν = ∂_μφ∂_νφ − η_μν(1/2)(∂φ)²`, matching the
action's own `(1/2)(∂φ)²` kinetic term (`two_field_action_closure.py` line
111) — static limit, consistent with every finding P9–P25. First proved a
**general** identity (sympy, arbitrary profile `f(r,θ)`, not special to the
dipole), then applied it to P19's normalized dipole field, then
cross-checked the volume integral of `T_00` against P14's own already-
verified `E_self` formula as a positive control.

## 2. Result

**General identity** (structural, any static scalar profile in 3D):

```
Trace(T_ij) = −T_00
```

verified symbolically for a generic `f(r,θ)`, not assumed. This makes what
follows a *robust* fact, not a fragile feature of the dipole's specific
angular shape.

**Applied to the P19-normalized dipole**, `φ=p·cosθ/(4πr²)`:

```
w = P/ρ = (1/3)·Trace(T_ij)/T_00 = −1/3   (POINTWISE, angle-independent)
```

Since `P(x)=−(1/3)ρ(x)` holds **pointwise**, this survives *any* linear
averaging or integration exactly — angle-averaging, volume-integrating
from `r_min` to `∞` (the same domain `E_self`'s own integral uses), or
ensemble-averaging over many randomly-oriented sources all give the same
`w=−1/3`, with no averaging-order-of-operations subtlety to worry about.

**Positive control**: volume-integrating `T_00` in P14's *own* (pre-P19,
un-normalized, no canonical `1/2` factor) convention reproduces P14's
already-skeptic-verified `E_self=(8π/3)p²/r_min³` **exactly** — confirming
the stress-tensor machinery here is consistent with this project's prior
work before trusting the new result built on top of it.

**A previously-unflagged factor-of-2, found via that same cross-check**:
P14's own `E_self` was computed as `∫(∇φ)²dV` — the *bare* gradient-squared
integral, **without** the canonical `(1/2)` factor from the action's own
kinetic term. Combined with P19's already-known `1/(4π)` geometric
normalization, the fully-corrected self-energy is:

```
E_self,correct = p²/(12πr_min³) = E_self,P14 / (32π²)
```

This does **not** change any qualitative conclusion — `Ω_φ`'s *absolute*
scale was already blocked by `A`, `κ` being individually unknown (P17,
P21, P22) — it's one more, now-identified, order-unity factor to fold in
whenever that gap is eventually resolved.

## 3. What this means, stated carefully

`w=−1/3` is the **curvature** equation of state: `ρ+3p=0` identically,
contributing **zero** to the Friedmann acceleration equation (`ä/a ∝
−(ρ+3p)`). This is **not** dark-energy-like — dark energy needs `w<−1/3`
to source accelerated expansion. `ρ_φ` redshifts as `a⁻²`, exactly like
spatial curvature `Ω_k` in the standard Friedmann equations — a real,
distinct redshift dependence from `Λ` or matter, but a **qualitatively
different** kind of modification than "new dark energy," not a
quantitatively-smaller version of one.

**This does not contradict P1's own force-based null result — they answer
different questions.** A zero *force* on a test particle from an isotropic
source distribution (P1 §4.3) is fully compatible with a nonzero *energy
density* sourcing the Friedmann equation (this finding) — the same way an
isotropic photon gas (e.g. the CMB) exerts zero net force on a test
particle at the center of symmetry by symmetry, while its energy density
and pressure absolutely source cosmological expansion. These are genuinely
different physical questions (Newtonian test-particle force vs.
GR-level stress-energy sourcing), not a tension needing resolution.

## 4. What this does NOT establish

1. **A numeric value for `ρ_φ` or `p_φ`.** `ρ_φ=n·E_self,correct` is a
   real structural formula, but its absolute scale is still blocked by the
   same open gaps as P17/P21/P22 — `A` and `κ` individually unknown.
2. **A solved `H(z)`.** Only `ρ_φ`, `p_φ` are derived here — actually
   solving the Friedmann equations with this `T_μν` as a source on an FLRW
   background (the final step of "`S→T_μν→ρ_φ,p_φ→H(z)`") is a further
   step, not attempted.
3. **Whether this component is large enough to matter at all.** `w=−1/3`
   only says *what kind* of term this is (curvature-like); whether `Ω_φ`'s
   magnitude is cosmologically significant remains exactly as unknown as
   before this finding.
4. **The monopole (`g`) sector's own equation of state.** The general
   trace identity applies structurally to *any* static profile, including
   the monopole's own gradient energy — not quantified here; this finding
   focuses on the `κ`/dipole sector, consistent with P14–P25's own scope.
5. **Whether the near-source region (`r<r_min`, where P20 found the
   point-dipole idealization breaks down) needs separate treatment.** The
   integral defining `E_self` already excludes this region (same `r_min`
   cutoff as P14–P20); this finding does not re-examine that boundary.
6. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction,
   not a claim about TJB's own unpublished theory.

## Reproduction

```bash
python experiments/20260803-bridge/P26_stress_tensor_equation_of_state.py
```

## Skeptic verdict (context-blind, Step 8a)

*Pending — to be run with only this file + `P26_stress_tensor_equation_of_state.py`
+ `two_field_action_closure.py` + `FINDING_P14_kappa_normalization_unfixed.md`
+ `FINDING_effective_fluid_energy_scale.md`, no session history.*
