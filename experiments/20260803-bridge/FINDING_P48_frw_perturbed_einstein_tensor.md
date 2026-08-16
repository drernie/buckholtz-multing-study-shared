# P48 — perturbed Einstein tensor on FRW: two genuinely external positive controls after skeptic review closed a self-check gap, plus a strengthened no-quasi-static-needed result for G₁₂

**Date:** 2026-08-16
**Status:** Built, run, ruff clean, all assertions pass. **Corrected same
day after context-blind skeptic review — zero computational errors
found (skeptic independently re-derived the background Ricci and the
eps-linearization method by hand), but four real gaps: an overstated
"positive control" that couldn't discriminate correct from wrong
`H`-dependent structure, a claim about `G₁₂` verified only at the
static+flat limit rather than the general FRW level, an under-checked
"no time-dependence" claim missing second-derivative and `a(t)`
dependence, and a missing convention note. All fixed with real
computation — a second genuinely external check added, not softened
language.**
**Skeptic review (Step 8a): COMPLETE. See § Skeptic Verdict below.**
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

**[CORRECTED after skeptic review, added]** Convention note: `Φ=g₀₀`
perturbation, `Ψ=g_ii` perturbation is one standard labeling in modern
cosmology, but **not universal** — some sources assign the labels the
other way around. Stated explicitly to avoid a silent
literature-convention collision for a reader coming from a different
source.

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

**[CORRECTED after skeptic review]** The original text asserted
`G₁₂^(1)`'s expected form only at the static+flat limit (Part 5), never
at this general FRW level. Fixed — directly asserted here: `G₁₂^(1)`
matches `−∂_x∂_y(Φ−Ψ)` exactly at the **general** FRW level, with no
hidden `a(t)`-dependent prefactor.

## Part 5 — static+flat limit vs. `FINDING_P38`'s own results (project-internal control)

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
FRW too.

**[CORRECTED after skeptic review]** This static+flat comparison, *by
itself*, cannot distinguish the correct `G₀₀` from other `H`-dependent
forms that also reduce to `2∇²Ψ` at `a=1` — the skeptic constructed
three concrete counterexamples (e.g. an extra `βH²Φ` term, or a wrong
coefficient on the `Hψ̇` term) that would all pass this specific check.
**This is a project-internal control, correctly labeled as such** — not
claimed to independently pin down the `H`-dependent structure on its
own. Part 6 below adds a genuinely external check that does.

## Part 6 — subhorizon quasi-static reduction, plus a second external check

Reuses `FINDING_P46`'s own corrected enslaved-response closure argument
(not re-derived from scratch, not silently assumed): for `k/(aH)≫1`,
drop the `3Hψ̇` term relative to `(k/a)²Ψ`:

```
G₀₀^(1)_k  ≈  −2(k²/a²)Ψ_k        (quasi-static)
```

**[ADDED after skeptic review]** Genuinely external check, closing the
gap flagged above: combining this with `G₀₀=8πG_N T₀₀` gives
`Ψ_k=−4πG_N a²δρ_k/k²`, i.e. `∇²Ψ=4πG_N a²δρ` — **the standard,
well-known quasi-static Poisson equation of linear cosmological
perturbation theory** (the cosmological analogue of the ordinary
Newtonian Poisson equation, with the `a²` factor from comoving
coordinates). Used here only as an external check on the sign and
coefficient of the `H`-dependent structure this file derived, not as a
citation this file claims credit for.

**[CORRECTED, strengthened]** `G₁₂^(1)`'s trace-free equation needs no
quasi-static approximation at all — the original claim rested on only
two checks (`∂G₁₂^(1)/∂Ψ̇=0`, `∂G₁₂^(1)/∂Φ̇=0`), which do not exclude
*second*-time-derivative or `a(t)`-dependence. Now confirmed by **five**
checks at the **general** FRW level: `∂G₁₂^(1)/∂Ψ̇=0`,
`∂G₁₂^(1)/∂Φ̇=0`, `∂G₁₂^(1)/∂ψ̈=0`, `∂G₁₂^(1)/∂Φ̈=0`, and
`∂G₁₂^(1)/∂a=0` — all script assertions, none assumed. Zero dependence
on any time derivative (first or second) of `Φ` or `Ψ`, and zero
explicit `a(t)`-dependence: it is genuinely in algebraic (Poisson-type)
form already.

## What this establishes, precisely

1. The perturbed Einstein tensor on FRW, extending `P38`'s flat
   derivation, verified by **two genuinely external** controls
   (textbook FRW background Ricci; the standard quasi-static Poisson
   equation of linear perturbation theory) plus a correctly-labeled
   **project-internal** control (static+flat vs. `P38`'s own already-
   verified `G₀₀=2∇²Ψ`, the trace-free structure, and its `Φ=Ψ`
   self-consistency property).
2. That the trace-free (`G₁₂`) equation is exactly algebraic on FRW,
   with zero dependence on any first or second time-derivative of `Φ`
   or `Ψ`, and zero explicit `a(t)`-dependence — confirmed by five
   direct checks at the general FRW level, not two checks at a limit.
3. The quasi-static-reduced `G₀₀` equation, verified against the
   standard external Poisson equation, ready for sourcing.

## What this does NOT establish

1. **`Ψ_k`, `Φ_k`, or `γ(a,k)`.** This finding supplies the LHS
   (geometry) only. Combining with `FINDING_P46`'s `δφ_k` and
   `FINDING_P47`'s `δT_μν` to actually solve the sourced equations is
   explicitly **deferred to a further, not-yet-started step**.
2. **Anything about matter's own contribution to the source.** Only the
   geometric (LHS) side is derived.
3. **Validity outside `k/(aH)≫1`** for the `G₀₀` equation specifically —
   the general FRW form (Part 4) remains exact and unapproximated.
4. **[CORRECTED, added]** **That the static+flat comparison to `P38`
   (Part 5) independently verifies the `H`-dependent structure of
   `G₀₀`.** It does not — a class of wrong `H`-dependent forms would
   also pass it. Part 6's external Poisson-equation check is what
   actually pins this down.
5. **[CORRECTED, added]** **That the `Φ`/`Ψ` labeling here is
   universal.** It matches one standard modern-cosmology convention but
   not every source's — stated explicitly in Part 1 to avoid a silent
   collision.
6. **Anything about the κ (dipole) sector** — monopole (`g`) sector only,
   matching every prior finding in this sub-arc.
7. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction,
   not a claim about TJB's own unpublished theory.

## Skeptic Verdict (Step 8a, context-blind — claim.md + code only, no session history)

| Sub-claim | Skeptic verdict | Response |
|---|---|---|
| Metric convention (Φ=g₀₀, Ψ=g_ii) | **CONFIRMED**, with a documentation gap noted | **Fixed** — explicit convention note added to Part 1. |
| Eps-linearization method | **CONFIRMED** — independently re-derived by hand | No change. |
| Background Ricci vs. textbook FRW | **CONFIRMED** — independently re-derived by hand, exact match | No change. |
| Static+flat vs. P38 "discriminates the FRW extension" | **WEAKENED** — concrete counterexamples constructed (wrong `H`-dependent forms that also pass) | **Fixed.** Relabeled as a project-internal control; added a genuinely external check (standard cosmological Poisson equation) that does discriminate the `H`-dependent structure. |
| "`G₁₂` needs no quasi-static approximation at all" | **WEAKENED** — only two of five possible dependencies checked, and only at the static+flat limit, not the general level | **Fixed.** Added the general-level assertion plus three more checks (second time-derivatives of both potentials, explicit `a`-dependence) — all confirmed zero, strengthening the original claim rather than retracting it. |
| Scope-gap list | **FALSIFIED** — missed all of the above | **Fixed** — items 4–5 added. |

No verdict here meets the Step 8a "true kill" bar — the skeptic found
**zero computational errors** (independently re-derived both the
background Ricci and the eps-linearization method by hand); every
correction strengthened either the verification rigor or the honesty of
the framing, consistent with this campaign's established discipline.

## Reproduction

```bash
python experiments/20260803-bridge/P48_frw_perturbed_einstein_tensor.py
```
