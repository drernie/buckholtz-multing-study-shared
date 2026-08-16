# P48 — perturbed Einstein tensor on FRW, extending P38's flat-Minkowski calculation, with three positive controls (one external-textbook, two against P38's own already-verified results)

**Date:** 2026-08-16
**Status:** Built, run, ruff clean, all assertions pass.
**Pending context-blind skeptic review (Step 8a) — not yet run.**
**Origin:** the machinery-extension step explicitly flagged as deferred
in `FINDING_P47`'s own scope note — extending `FINDING_P38`'s flat
Minkowski linearized-gravity calculation to a background with `H≠0`.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P48_frw_perturbed_einstein_tensor.py`, ruff clean, all
assertions pass.

## 0. Method — why not P38's own shortcut

`FINDING_P38`'s own linearized-gravity derivation drops all
`Γ·Γ` terms in the Ricci tensor, valid *only* because its flat
background has `Γ^(0)=0` identically. On FRW this is false — background
Christoffels are `O(H)`, and background×perturbation cross terms
survive at linear order. Rather than hand-deriving which `Γ·Γ` products
survive (real risk of a sign/index slip in exactly the derivation this
campaign has already found error-prone), this finding builds the
**exact** (unexpanded) perturbed metric, computes the **exact**
Christoffel/Ricci/Einstein tensor (all `Γ·Γ` terms included, not
dropped), and extracts the `O(ε)` piece via the same eps-linearization
method already used reliably in `P44`/`P46`/`P47` — `sympy` handles the
cross-term bookkeeping mechanically, with no hand-derived covariant
derivative operator to get wrong.

## Part 1 — metric convention

Matches `FINDING_P38`'s own `h₀₀=−2Φ`, `h_ii=−2Ψ` exactly, extended to
`a(t)²` and general `Φ(t,x,y,z)`, `Ψ(t,x,y,z)`:

```
ds² = −(1+2εΦ)dt² + a²(1−2εΨ)(dx²+dy²+dz²)
```

## Part 2 — exact Christoffels and Ricci tensor

`Γ·Γ` terms included throughout (the extension `P38`'s shortcut could
skip), built from the unexpanded metric.

## Part 3 — positive control 1: background Ricci vs. an external, independently-citable textbook result

```
R₀₀ (background, ε=0) = −3ä/a
R₁₁ (background, ε=0) = aä+2ȧ²
```

**Both match the standard flat-FRW textbook results exactly** (script
assertion) — this control is deliberately *not* self-referential to
this project's own prior work, unlike every other control this campaign
has used so far.

## Part 4 — linearized `G₀₀` and off-diagonal `G₁₂`

```
G₀₀^(1) = 2[∇²Ψ/a² − 3Hψ̇]
G₁₂^(1) = −∂_x∂_yΦ + ∂_x∂_yΨ
```

## Part 5 — positive controls 2 and 3: static+flat limit vs. `FINDING_P38`'s own results

Static+flat means `a`'s derivatives→0, `a`→1, **and** `Φ`/`Ψ`'s
time-derivatives→0 — matching `P38`'s own static `Φ(x,y,z)`, `Ψ(x,y,z)`
ansatz exactly (an intermediate check *during this derivation* first
caught that `a`→1 alone is insufficient — a real, self-caught precision
issue, fixed before finalizing).

```
G₀₀^(1) static+flat = 2∇²Ψ           — matches P38's G₀₀=2∇²Ψ exactly
G₁₂^(1) static+flat = −∂_x∂_y(Φ−Ψ)   — matches P38's trace-free structure
```

`G₁₂^(1)` vanishes identically at `Φ=Ψ` (script assertion) — the same
self-consistency property `P38`'s own Step 4 checked, now confirmed on
FRW too. **All three positive controls pass.**

## Part 6 — subhorizon quasi-static reduction

Reuses `FINDING_P46`'s own corrected enslaved-response closure argument
(not re-derived from scratch, not silently assumed): for `k/(aH)≫1`,
drop the `3Hψ̇` term relative to `(k/a)²Ψ`:

```
G₀₀^(1)_k  ≈  −2(k²/a²)Ψ_k        (quasi-static)
```

**`G₁₂^(1)`'s trace-free equation needs no quasi-static approximation at
all** — confirmed directly (`∂G₁₂^(1)/∂Ψ̇=0`, `∂G₁₂^(1)/∂Φ̇=0`, script
assertion), not assumed from the static-limit check alone: it is already
in algebraic (Poisson-type) form.

## What this establishes, precisely

1. The perturbed Einstein tensor on FRW, extending `P38`'s flat
   derivation, verified by three independent controls — one genuinely
   external (textbook FRW Ricci), two against this project's own
   already-verified `P38` results (`G₀₀=2∇²Ψ`, the trace-free structure
   and its `Φ=Ψ` self-consistency property).
2. That the trace-free (`G₁₂`) equation is exactly algebraic on FRW —
   no quasi-static approximation needed for it, unlike `G₀₀`.
3. The quasi-static-reduced `G₀₀` equation, ready for sourcing.

## What this does NOT establish

1. **`Ψ_k`, `Φ_k`, or `γ(a,k)`.** This finding supplies the LHS
   (geometry) only. Combining with `FINDING_P46`'s `δφ_k` and
   `FINDING_P47`'s `δT_μν` to actually solve the sourced equations is
   explicitly **deferred to a further, not-yet-started step** — kept out
   of scope here, matching this campaign's established granularity (cf.
   the `P46`/`P47` split, for the same reason).
2. **Anything about matter's own contribution to the source.** Only the
   geometric (LHS) side is derived; the matter stress-energy perturbation
   is not addressed here (it was `P47`'s explicit non-scope too).
3. **Validity outside `k/(aH)≫1`** for the `G₀₀` equation specifically —
   the general FRW form (Part 4) remains exact and unapproximated.
4. **Anything about the κ (dipole) sector** — monopole (`g`) sector only,
   matching every prior finding in this sub-arc.
5. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction,
   not a claim about TJB's own unpublished theory.

## Reproduction

```bash
python experiments/20260803-bridge/P48_frw_perturbed_einstein_tensor.py
```
