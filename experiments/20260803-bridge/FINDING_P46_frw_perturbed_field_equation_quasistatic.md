# P46 — FRW-perturbed field equation, solved in the subhorizon quasi-static limit: `δφ_k=ĝa²δρ_k/k²`, passing three positive controls back to already-established ground

**Date:** 2026-08-16
**Status:** Built, run, ruff clean, all assertions pass.
**Pending context-blind skeptic review (Step 8a) — not yet run.**
**Origin:** first of two steps toward the campaign's original `P36` row
(`PLAN_final_goal_20260814.md`): "quasi-static cosmological reduction,
subhorizon approximation." Explicitly the same category of step (local
static result → broader cosmological context) that produced this
campaign's single worst correction (`P36`, 5/6 skeptic issues FALSIFIED,
per the plan's own status log) — built with maximal explicit derivation
as a direct, deliberate response to that history.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P46_frw_perturbed_field_equation_quasistatic.py`, ruff
clean, all assertions pass.

## 0. Why this step exists, and why it is split in two

`FINDING_P40`'s slip ratio `γ(r)` is a *static, two-body* quantity — not
directly comparable to `FINDING_P31`'s phenomenological ceiling, which
constrains a *cosmological, quasi-static* parameter (Bean &
Tangmatitham's `Q`). The campaign's own governing plan already named the
missing bridge as its `P36` row. This finding builds the first half:
the perturbed field equation and its quasi-static solution for `δφ_k`.
A second step (`P47`, not yet built) will derive the perturbed Einstein
equations in the same limit and assemble `γ(a,k)`.

**Explicit risk acknowledgment, stated before any derivation:** this is
the same *shape* of extension (a locally-proven result generalized to a
broader context) that produced this campaign's worst correction. Every
equation below is therefore re-derived from the action via
Euler-Lagrange — never pattern-matched from a prior result by analogy —
and every new object is checked against an already-established one
before being trusted.

## Part 1 — general FRW field equation, via Euler-Lagrange

Same Lagrangian density `FINDING_P34`/`FINDING_P35` both used, restored
to a flat-FRW background (`√-g=a³`, `g^{ij}=δ^{ij}/a²`):

```
L = a³·(1/2)φ̇² − a·(1/2)(∇φ)² − a³ρ(1−ĝφ)
```

Euler-Lagrange gives:

```
φ̈ + 3Hφ̇ − ∇²φ/a² = ĝρ      (H:=ȧ/a)
```

## Part 2 — two positive controls, both required

**(a) Homogeneous limit.** Not checked by substituting into the
already-derived field equation (that would be tautological — comparing
a formula to itself). Instead, *independently* re-derived from a
genuinely homogeneous (`t`-only) candidate Lagrangian, by the same
method as Part 1:

```
φ̄̈ + 3Hφ̄̇ = ĝρ̄
```

**Matches `FINDING_P34`'s own equation exactly.** Since this reuses the
same underlying Lagrangian as Part 1's general derivation, exact
agreement is *required* by construction, not surprising independent
evidence — the same scoping discipline `FINDING_P43` applied to its own
Noether-current check. It still catches a real class of bug (a wrong
`a(t)`-power or sign slip in Part 1's own general derivation), since
Part 1's derivation itself was not reused here.

**(b) Static + flat limit** (`a=1`, so `H=0`, `1/a²=1`):

```
φ̈ − ∇²φ = ĝρ
```

**Matches `FINDING_P35`'s own equation exactly.**

## Part 3 — is "perturbation theory" here exact or approximate?

Split `φ=φ̄(t)+εδφ(t,x)`, `ρ=ρ̄(t)+εδρ(t,x)`, take `d/dε` at `ε=0`
(script, not asserted by hand):

```
δφ̈ + 3Hδφ̇ − ∇²δφ/a² = ĝδρ
```

**Exactly the same functional form as the full equation.** This is a
checked consequence of the field equation being exactly linear in `φ`
and `ρ` — no `V(φ)` term exists at this stage of the chain (the same
fact `FINDING_P44`/`FINDING_P45` already exploited for a different
purpose). There is **no perturbative approximation in this step** —
`δφ`'s equation is exact, not leading-order.

## Part 4 — Fourier transform (exact) + subhorizon quasi-static approximation (flagged, not exact)

Fourier space, exact:

```
δφ̈_k + 3Hδφ̇_k + (k²/a²)δφ_k = ĝδρ_k
```

**Subhorizon quasi-static approximation**, validity `k/(aH)≫1` (the
`(k/a)²` term then dominates over `δφ̈` and `3Hδφ̇` by an explicit factor
of `(k/(aH))²≫1` — the standard argument, stated with its regime, not
asserted as exact):

```
(k²/a²)δφ_k = ĝδρ_k   ⟹   δφ_k = ĝa²δρ_k/k²
```

**This is the only approximation introduced in this finding.**

## Part 5 — load-bearing consistency check back to already-verified ground

Static limit (`a=1`) of the quasi-static Fourier solution:

```
δφ_k|_(a=1) = ĝδρ_k/k²
```

This is exactly the standard Fourier-space Green's-function relation for
`−∇²φ=ĝρ` (Fourier transform of `−∇²` is `+k²`, so `1/k²` is its
Green's function in `k`-space). Using the *already-established*
(`FINDING_P19`, `CONFIRMED-REAL`) real-space Green's function
`∇²[1/(4πr)]=−δ³(x)`, the real-space inverse transform of `ĝM/k²`
(point mass, `δρ_k=M` in the standard convention) is exactly
`ĝM/(4πr)` — `FINDING_P35`'s own static solution, unchanged. Not
re-derived symbolically here (the `1/k²→1/(4πr)` Fourier pair is the
*same* already-cited `P19` Green's function fact, read in the other
direction) — reused, not re-proven, matching this project's own
established practice.

## What this establishes, precisely

1. The general FRW field equation, derived (not assumed) and shown to
   contain both `FINDING_P34`'s homogeneous equation and
   `FINDING_P35`'s static equation as exact limiting cases.
2. That the linear perturbation `δφ` obeys the field equation's full
   functional form exactly — a checked, not assumed, consequence of the
   chain's own linearity at this stage.
3. `δφ_k=ĝa²δρ_k/k²` in the subhorizon quasi-static limit, the sole
   approximation of this finding, explicitly scoped to its validity
   regime.
4. That this new quasi-static machinery connects back to `FINDING_P35`'s
   already-verified static solution via `FINDING_P19`'s already-`CONFIRMED-REAL`
   Green's function — not a free-floating new construction.

## What this does NOT establish

1. **`γ(a,k)`, `μ(a,k)`, or `Σ(a,k)`.** Only the scalar field's own
   quasi-static Fourier solution is derived here — the perturbed
   Einstein equations (analogous to `FINDING_P38`/`FINDING_P40`'s static
   derivations, extended to FRW) are `P47`'s job, not attempted here.
2. **Anything numerically comparable to `FINDING_P31`'s ceiling.** Even
   once `P47` gives a symbolic `γ(a,k)`, `FINDING_P39`'s SI-units gap
   (`[ĝ]`, two unresolved readings) still blocks any numeric comparison —
   deliberately deferred, matching this campaign's established sequencing.
3. **Validity outside the subhorizon regime `k/(aH)≫1`.** The full
   second-order-in-time equation from Part 4 (before the quasi-static
   step) remains exact and unapproximated; only the algebraic reduction
   in the final step is scope-limited.
4. **Anything about the κ (dipole) sector** — monopole (`g`) sector only,
   matching every prior finding in this sub-arc.
5. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction,
   not a claim about TJB's own unpublished theory.

## Reproduction

```bash
python experiments/20260803-bridge/P46_frw_perturbed_field_equation_quasistatic.py
```
