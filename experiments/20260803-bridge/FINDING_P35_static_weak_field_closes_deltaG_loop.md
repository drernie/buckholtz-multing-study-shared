# P35 — the static, weak-field, point-source limit of MULTING's own action derives (not merely restates) P21's founding relation A·g²=4π·ΔG, with A=1 in the canonical convention

**Date:** 2026-08-14
**Origin:** second step of the covariant-completion campaign
(`PLAN_final_goal_20260814.md`), continuing directly from P34's explicit
gravitational-sector choice (standard, unmodified Einstein-Hilbert
gravity).
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P35_static_weak_field_closes_deltaG_loop.py`, ruff clean, all
assertions pass.

## 0. Honest scope

This is the static, weak-field, point-source (two-body Newtonian) limit
— not the cosmological perturbation theory of P34's own FRW background.
It reuses two already-established, already-verified building blocks
rather than re-deriving them (Using Wheels First):

1. **P34's own matter+scalar Lagrangian**, here kept fully
   space-*and*-time dependent (P34 only ever derived the spatially
   *homogeneous* FRW-restricted case — the general, non-homogeneous
   field equation is the genuinely new derivation step in this finding).
2. **P19's own already-skeptic-confirmed 3D Green's function**
   (`∇²[1/(4πr)]=−δ³(x)`, `CONFIRMED-REAL`,
   `FINDING_P19_greens_function_normalization_derived.md`) — cited
   directly, not re-derived from scratch.

**What this does NOT establish, stated up front (expanded in §4):** the
static two-body `G_eff` extracted here is **not automatically** the same
object as P30's *cosmological* growth-equation `G_eff` — connecting a
static, `k→∞`-subhorizon potential to the full perturbed cosmological
Poisson equation is a standard, well-established step in scalar-tensor
cosmology (the quasi-static, sub-horizon approximation), but that step
is **not performed here**, only asserted as plausible. This finding
closes the loop on P21's own *definition*, not on P30's cosmological
usage of `G_eff` — those remain linked only by name until a genuine
quasi-static reduction is done (deferred, flagged as the actual content
of the plan's still-open "P36" item).

**Relationship to `FINDING_P34`'s own correction (added after P34's
skeptic review landed, same day):** `FINDING_P34`'s original text claimed
`ΔG` "is structurally a linear-perturbation / two-body potential effect,"
a claim its own skeptic review withdrew as an unsupported leap — P34
*alone* only showed `ΔG` is absent from the *background*, not where it
actually lives. **This finding is the calculation that closes that gap**
— built independently, the same day, before the P34 skeptic verdict was
read — and its own result (§3–§4 below) is exactly what P34's corrected
text now points to. The two findings are complementary and mutually
consistent: P34 (corrected) says "not in the background, location not
shown by that finding alone"; this finding shows the location (the
static two-body potential) directly, from the same action.

## 1. Method — the general (non-homogeneous) scalar field equation

Same Lagrangian density P34 used, restored to full space+time dependence:

```
L = (1/2)φ̇² − (1/2)(∇φ)² − ρ(x)·(1−ĝφ)
```

Direct Euler-Lagrange variation (sympy, `general_scalar_field_equation`)
gives:

```
φ̈ − ∇²φ = ĝ·ρ(x)
```

**Static limit** (`φ̈=0`), point source `ρ(x)=M·δ³(x)`:

```
∇²φ = −ĝM·δ³(x)
```

## 2. Solving via P19's own already-confirmed Green's function

Using `∇²[1/(4πr)]=−δ³(x)` (P19, `CONFIRMED-REAL`):

```
φ(r) = ĝM/(4πr)
```

Verified (script, `sp.simplify` on the spherical Laplacian away from the
origin) to solve the source-free Laplace equation for `r>0` exactly.

## 3. Fifth-force potential energy, combined with the standard Newtonian term

From the *same* matter-action interaction term used throughout P33–P35
(`S_matter=−∫dτ·m(1−ĝφ)` ⟹ `U_5th=−m·ĝ·φ(r)`):

```
U_5th(r) = −ĝ²mM/(4πr)
```

Attractive for like-sign `ĝ`, matching `two_field_action_closure.py`'s
own docstring point 2 ("its m-m exchange renormalises G, attractive") —
an independent consistency check this finding did not have to construct,
already stated by the project's own earliest source file.

Combined with the standard (P34: `S_EH` unmodified) Newtonian potential
energy `U_N(r)=−G_N·mM/r` — **linear superposition of two independently-
sourced, leading-order-weak fields on a test particle, the standard
procedure for this class of problem (matches the implicit assumption
P21's own additive `G_eff=G_N+ΔG` framing already required, now made
explicit)**:

```
U_total(r) = −mM/r·[G_N + ĝ²/(4π)]
⟹ G_eff = G_N + ĝ²/(4π)
⟹ ΔG = ĝ²/(4π)
```

## 4. The load-bearing check — comparison to P21's own founding relation

P21 (start of the whole `ΔG`-normalization arc, everything since built
on it) **defined** the relation `A·g²=4π·ΔG` by dimensional matching to
Archidiacono's phenomenology — it was never derived from an actual field
equation. Setting `A=1` (the canonical-kinetic-term convention used
throughout P34–P35, one of the legitimate convention choices P24 flagged
as equally valid but never adopted consistently before now):

```
P21's ΔG (A left general):  A·ĝ²/(4π)
This derivation's ΔG:            ĝ²/(4π)
Difference at A=1:                    0    (script assertion, exact)
```

**P21's founding relation is derived here, not merely restated** — the
first time in the P21–P35 arc that this specific formula has followed
from an actual field-theoretic calculation rather than being assumed by
dimensional matching.

## 5. Qualitative slip observation (cheap, not independently computed)

Dust has zero anisotropic stress; `φ` is a canonical, minimally-coupled
scalar with no direct `R`-coupling (P34's own explicit choice) — its own
anisotropic-stress contribution at linear order is second-order-small
(`∇φ·∇φ`, with `φ` itself already first-order). This is the standard,
well-known reason canonical quintessence-type scalars give **no slip**
(`γ:=Φ/Ψ=1`) at this order. Stated qualitatively only — **not
independently derived or computed in this finding**, flagged explicitly
as a claim resting on a well-known general argument, not a fresh
calculation.

## 6. What this does NOT establish

1. The connection between this **static, two-body** `G_eff` and P30's
   **cosmological, perturbation-growth** `G_eff` — related by the
   standard quasi-static/sub-horizon approximation, but that reduction
   is **not performed here**. Until it is, treat the two `G_eff`s as
   linked by strong physical plausibility, not by an explicit derivation
   chain.
2. `γ(a,k)=Φ/Ψ` quantitatively — §5 is qualitative, citing a
   well-established general fact about this theory class, not computed
   from the actual perturbed field equations here.
3. `μ(a,k)`'s scale (`k`) dependence — the static result here is
   `k`-independent by construction (massless mediator, point-source
   limit), consistent with expectation, but the full `k`-dependent
   quasi-static Poisson equation is not derived.
4. A restored, explicit-`c`, SI-like version matching P21's own original
   unit convention — still deferred (same caveat as P34).
5. Anything about the `κ` (dipole) sector.
6. Any comparison against Table A1 — closed gate, not touched.
7. Per NO_AUTHOR_ERROR: entirely this project's own reconstruction
   (OUR_RECONSTRUCTION), not a claim about TJB's own unpublished theory.

## Reproduction

```bash
python experiments/20260803-bridge/P35_static_weak_field_closes_deltaG_loop.py
```
