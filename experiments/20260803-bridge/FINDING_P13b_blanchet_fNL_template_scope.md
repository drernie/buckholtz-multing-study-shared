# P13b — Blanchet et al.'s second-order non-Gaussianity template cannot be ported directly: the k-sector has no fluid description yet

**Date:** 2026-08-12 · checks the second lead from the literature sweep:
does Blanchet, Langlois, Le Tiec & Marsat 2013 (arXiv:1210.4106)'s worked
method for computing a second-order CMB non-Gaussianity signature from
dipolar dark matter apply directly to this project's own k-sector dipole —
the exact "second-order observable" `FINDING_P4` §8 named as Branch B's
natural home but never computed?
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Method:** structural/applicability check (does the borrowed formalism's
own premise hold for this project's construction?), citing this project's
own action and prior findings rather than attempting a new GR-perturbation-
theory derivation on an unverified foundation.

**Read before citing: like P13a, this is a scope-mismatch finding, not a
new numerical forecast. §2 is the load-bearing argument — it identifies a
genuine prerequisite this project has never built, not an excuse to skip
the calculation.**

---

## 1. What Blanchet et al.'s method actually requires

Their model (per the literature-sweep summary of 1210.4106, cross-checked
against the companion foundational papers 0804.3518 and 0901.3114) is built
as a **covariant fluid action**:

```
S = ∫d⁴x √-g L[J^μ, ξ^μ, ξ̇^μ, g_μν]
```

`ξ^μ(x)` is a **dynamical field** — a smooth function of spacetime position,
with its own equation of motion (sourced by an internal potential
`W(Π_⊥)`), its own perturbation `λ^i(x)` around a "primordial" background
value, and its own time-evolution equation (a Mészáros-type equation, whose
growing-mode solution `λ^+ = y+2/3` is what ultimately sources the
second-order curvature correction `ζ=ζ_CDM+W/3`). The entire second-order
non-Gaussianity calculation is a calculation about how **this field's own
cosmological perturbation** evolves and sources `ζ`.

## 2. Does this project's k-sector have an analogous field? No — it is built as a discrete, per-body structure

This project's own action (`two_field_action_closure.py`, P1):

```
S = ∫d⁴x[(1/2)(∂φ)²] + Σᵢ∫dτ [ g·mᵢ + pᵢ·∇ ] φ(xᵢ),   pᵢ = κ·kᵢ·rᵢ/c²
```

`φ` is the only dynamical field. The "dipole moment" `pᵢ` is not a field —
it is an **algebraic function of each individual body's own `kᵢ, rᵢ`**,
evaluated at each body's worldline. There is no `ξ^μ(x)` analogue: no
smooth "k-density perturbation" defined over spacetime, no equation of
motion for such a field, and consequently no Mészáros-type evolution
equation to solve. This is not an oversight specific to this finding — it
is consistent with how every prior finding in this track (P2, P6, P7, P9)
has treated `k`: as a **per-cluster observable**, measured or estimated for
individual real objects via real catalogues (CHEX-MATE, MCXC), never
coarse-grained into a continuum cosmological field. `FINDING_P4`'s own §8
(the origin of this whole line of inquiry) asked for the perturbative
*order* of each force tier — `F_km~O(δ^?)` — which P6 answered by treating
`kᵢ` as an ordinary astrophysical cluster property entering a **pairwise**
force law, not as a field with its own `δ_k(x)` perturbation spectrum.

**Consequence:** Blanchet's formalism cannot be mechanically applied. Their
entire calculation is "how does this project's `ξ^μ`'s own cosmological
perturbation evolve, and what does it source" — and this project has no
`ξ^μ`-equivalent for `k` to evolve in the first place.

## 3. What would actually be required — named, not attempted here

To make Blanchet's template applicable, this project would first need to
construct an explicit **coarse-grained fluid limit** of the k-sector: treat
the population of bodies carrying `kᵢ` (clusters, analogous to how discrete
galaxies are coarse-grained into a smooth CDM density field `δ_c(x)` in
standard cosmological perturbation theory) as a smooth field with its own
internal potential and equation of motion. This is not fundamentally
impossible — matter *is* discrete at a deeper level too, and fluid
descriptions of discrete populations are standard practice in cosmology —
but it is a **real, unbuilt construction step**, not a trivial relabeling.

**And even if that step were taken, it would immediately run into the same
obstruction P9 already found**: a coarse-grained k-density field built from
an isotropic ensemble of radially-aligned or randomly-oriented dipoles
inherits exactly the double-layer / `⟨p⟩=0` cancellation
(`FINDING_dipole_shell_is_a_double_layer.md`) at background/linear order —
so the coarse-grained field's OWN internal energy `W` (Blanchet's sourcing
quantity for `ζ`) would need the SAME symmetry-breaking ingredient (P9's
assumed `ε`, or P11's fixed-mass `μ~H₀/c`) to be nonzero in the first
place. This is the same open dependency every prior finding in this
sequence (P9–P12) has already been tracking — Blanchet's template does not
supply a way around it, only a way to compute a *forecast*, once a nonzero
source exists.

## 4. Bottom line

**P13b does not produce a new f_NL forecast.** It establishes that the
borrowed second-order machinery has a **prerequisite this project has never
built** — a fluid/coarse-grained description of the k-sector, distinct from
the point-charge/per-body picture used throughout P1–P12 — and that even
once built, that fluid's internal source term would inherit the same
open `ε`/`μ` dependency this track has been investigating all along. This
sharpens, rather than closes, `FINDING_P4` §8's named next step: the
"perturbative order" question P6 already answered *for the pairwise force*
is not the same question as "what is the k-sector's own cosmological
perturbation spectrum," which remains genuinely unasked and unbuilt.

## What this does NOT establish

1. **That a fluid description of the k-sector is impossible to build.**
   Only that it does not currently exist in this project, and porting
   Blanchet's formalism requires it as a precondition.
2. **A numerical estimate of what such a forecast would give**, even
   order-of-magnitude — that would require the coarse-graining step itself,
   not attempted here to avoid building on an unverified foundation.
3. **That second-order observables are the wrong place to look.**
   `FINDING_P4`'s own reasoning for why Branch B's natural home is
   second-order (not `H(z)` itself) is untouched by this finding.
4. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction,
   not a claim about TJB's own unpublished theory, and not a claim that
   Blanchet et al.'s own DDM formalism is wrong for their own model (it
   isn't — it's a well-posed fluid theory; the mismatch is that this
   project's construction is not, yet, one).

## Reproduction

No new computation — a structural/applicability argument citing this
project's own action (`two_field_action_closure.py`) and the double-layer
result (`FINDING_dipole_shell_is_a_double_layer.md`), both independently
reproducible per their own instructions.
