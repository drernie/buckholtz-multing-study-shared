# P50A — structural `μ(a,k)` from the P46–P49 system: the canonical g-sector changes growth at leading order without slip — the "no-numbers" scope needed retracting twice before it was honest

**Date:** 2026-08-16
**Status:** Built, run, ruff clean, all assertions pass. **Corrected same
day after context-blind skeptic review — a real, independently-confirmed
computational error found (a missing metric-perturbation term in the
matter continuity closure) and a circular sanity check found (zero
discriminating power). Both fixed with real computation: the correct
continuity equation was derived from scratch via covariant divergence
(not patched from a citation), and the leading-order result was checked
for robustness against a generic closure coefficient rather than assumed.
The finding's headline scope was narrowed twice as a result — see §0 and
Part 8.**
**Skeptic review (Step 8a): COMPLETE. See § Skeptic Verdict below.**
**Origin:** direct continuation of the P46→P49 quasi-static-reduction
sub-arc, per the user's own P50A/B/C staging. User pre-registered two
competing hypotheses before this script ran: H1 (`μ≠1, γ=1`) vs H0
(`μ=1, γ=1`).
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P50A_structural_mu_ak.py`, ruff clean, all assertions pass.

## 0. Refinement #1 — the pre-registered H0 needed a correction before it could be tested

The user's literal H0 (`μ(a,k)=1` for all `k`) is **not the right null**,
given this campaign's own established convention: `FINDING_P46`
explicitly does not impose the Friedmann constraint on `a(t)`. Under that
convention, even the `ĝ=0` (no coupling) quasi-static Poisson equation
does not reduce to `μ=1` exactly — a bookkeeping artifact of a
three-findings-old modeling choice, not a new gap. **Refined null:**
`μ(a,k)` compared against the same `ĝ=0` matter-only baseline in the same
convention (Part 10).

## Part 1 — `g₀₀·g⁰⁰=1` identically

Trivial but load-bearing for Part 2.

## Part 2 — `δT₀₀^(φ)` with the full metric — closes an open question, matches P47 exactly

```
δT₀₀^(φ) = φ̄̇δφ̇
```

Confirmed Φ-independent with the full metric (script assertion, matches
`FINDING_P47`'s background-only result exactly).

## Part 3 — `δT₀₀^(int)` with the full metric — closes the gap `FINDING_P49` flagged

```
δT₀₀^(int) = ĝ(−ρ̄δφ−φ̄δρ) − 2ĝφ̄ρ̄Φ
```

Confirmed (script assertion) — exactly the `−2ĝφ̄ρ̄Φ` piece `FINDING_P49`
predicted was missing.

## Part 4 — `δT₀₀^(matter)`, derived via 4-velocity normalization

```
δT₀₀^(matter) = δρ + 2ρ̄Φ
```

Confirmed (script assertion) — standard result for a pressureless
perfect fluid, `u^i=0`.

**Parts 1–4 use no new assumption beyond P46–P49.**

## Part 5 — assemble, substitute `Φ_k=Ψ_k` — still no new assumption

`δφ̇_k` left as a free symbol; the "P50A-strict" result.

## Part 6 — combine with P48's exact quasi-static `G₀₀`, solve exactly

No term dropped beyond what `FINDING_P48` already established.

## Part 7 — matter's own continuity equation, derived — and a real error caught and independently re-confirmed

**[CORRECTED after skeptic review]** The original version of this Part
simply **postulated** `δρ̇_k=−3Hδρ_k` as "the simplest `θ=0` closure,"
without deriving it. The skeptic flagged this is **not** the correct
linear-order continuity equation on a perturbed FRW background — it is
missing a metric-perturbation term, and dropping it silently directly
**contradicted Part 4's own insistence** that metric perturbations matter
for `T₀₀`.

**Fixed by deriving it properly, not patching the citation in.** The
**same** `u^i=0` ansatz already used in Part 4 (matter exactly at rest —
this *is* `θ=0`, not a separate new assumption stacked on top of Part 4)
is applied to compute `∇_μT^μ_0=0` directly, via the same Christoffel
machinery this campaign has used since `FINDING_P48`. Independently
re-verified (a second, standalone derivation outside the script, before
accepting the skeptic's claim, per `audit-verification-gate.md`):

```
δρ̇_k = −3Hδρ_k + 3ρ̄Ψ̇_k
```

**Confirmed exactly** — matches the skeptic's cited Ma & Bertschinger-type
form, independently re-derived from scratch here via covariant
divergence, not merely taken on citation.

**Consequence:** `δφ̇_k` (via `FINDING_P46`'s own quasi-static solution,
differentiated) now depends on `Ψ̇_k`, not `δρ_k` alone. **Is this
automatically negligible by `k`-power-counting?** No — both pieces of
`δφ̇_k` carry the same explicit `1/k²` prefactor, so this is not a free
suppression argument. Closing it needs either (a) solving the resulting
first-order ODE for `Ψ_k(t)` at fixed `k` (not attempted — genuinely
larger scope), or (b) **reusing** (not inventing) the same
enslaved-response/quasi-static closure principle `FINDING_P46` already
established for `δφ_k` itself: `Ψ_k`, like `δφ_k`, tracks its source's
Hubble-timescale evolution, so `Ψ̇_k ~ cHΨ_k` for some `O(1)` coefficient
`c`. **Checked below (not assumed) that the leading `k→∞` result is
independent of `c`.**

## Part 8 — `μ(a,k)`: the leading term is robust; the "exact closed form" is retracted

**[CORRECTED after skeptic review]** The original Part 8 presented a full
"exact closed form" for `μ(a,k)` including `O(1/k²)` subleading terms.
Given `δφ̇_k` genuinely depends on `Ψ̇_k` at the **same order** as the
retained `O(1/k²)` terms (not extra-suppressed, per Part 7), that
subleading structure depends on the closure coefficient `c` — **not
parameter-free**.

**Retracted as "exact."** What survives, checked explicitly for a generic
`c` (script assertion):

```
μ(a,k) → 1 − ĝφ̄   as k→∞,   independent of c
```

**This is the robust result.** The full subleading `k`-dependence
requires either solving the `Ψ_k(t)` ODE or fixing `c` by a further
physical argument — explicitly deferred, not presented as closed.

## Part 9 — leading-order `μ`, restated precisely

```
μ(a,k) → 1 − ĝφ̄   as k→∞
```

Not assumed identical to `k/(aH)≫1` — Friedmann is not imposed, so no
fixed relation between `k` and `aH` is available.

## Part 10 — a real external check, replacing the circular one

**[CORRECTED after skeptic review]** The original "sanity check"
(`δμ→0` as `ĝ→0`) was true but had **zero discriminating power** —
`μ_baseline` was *defined* as `μ|_{ĝ=0}`, so the check was tautological
by construction (`0=0` for any formula built this way), not evidence the
refinement isolates real physics. **Removed.** Replaced with a genuine
external check: does the `ĝ=0` baseline reduce to the textbook GR result
(`μ=1`) under the additional, clearly-labeled **hypothetical** of also
imposing the Friedmann constraint (`H²=8πG_Nρ̄/3`) and taking the standard
subhorizon limit `k/(aH)≫1` — not adopted as this campaign's actual
convention, used only as an external check:

```
μ_baseline (Friedmann imposed) → 1   as k→∞ (script assertion, CONFIRMED)
```

Matches the textbook GR/ΛCDM Poisson equation — a genuine external check
against a convention this campaign does not itself adopt, not a
tautological subtraction.

## Part 11 — H0/H1 verdict, appropriately conditional

**Leading-order H1** (`μ(a,k)→1−ĝφ̄≠1` as `k→∞`, generically when
`ĝφ̄≠0`): **confirmed, robust** to the Part 7 correction and to any
reasonable `Ψ̇_k` closure (checked for generic `c`).

**Full-`k`-dependence H1/H0** (does `μ(a,k)` differ from the baseline at
*every* `k`, not just `k→∞`): **not established here.** Genuinely open,
deferred to a further step.

## What this establishes, precisely

1. `μ(a,k) → 1−ĝφ̄` as `k→∞`, robust to a real error the skeptic caught
   and to the choice of `Ψ̇_k` closure — a genuine, falsifiable
   leading-order structural result: the canonical g-sector changes growth
   without slip.
2. Matter's own continuity equation, derived (not postulated) for the
   first time in this sub-arc, closing yet another gap.
3. Two real errors were caught and fixed with real computation: a missing
   metric-perturbation term in the continuity closure (independently
   re-derived from scratch, not patched); a circular sanity check
   (replaced with a genuine external one).

## What this does NOT establish

1. **A numeric value.** `FINDING_P39`'s SI-normalization gap remains
   unresolved — deferred to P50B.
2. **The subleading (`O(1/k²)` and beyond) structure of `μ(a,k)`.**
   Genuinely open — requires either solving the `Ψ_k(t)` ODE this system
   now is, or matter's own Euler equation (`T₀ᵢ`/`G₀ᵢ`, not built
   anywhere in P46–P50A).
3. **A fully self-consistent closure.** The enslaved-response `Ψ̇_k~cHΨ_k`
   scaling is reused from `FINDING_P46`'s own established principle, not
   independently derived for `Ψ_k` specifically.
4. **Anything about the κ (dipole) sector** — monopole (`g`) sector only.
5. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction,
   not a claim about TJB's own unpublished theory.

## Skeptic Verdict (Step 8a, context-blind — claim.md + code only, no session history)

| Sub-claim | Skeptic verdict | Response |
|---|---|---|
| Part 2 (`δT₀₀^(φ)` Φ-independence via `g₀₀g⁰⁰=1`) | **CONFIRMED** (result), **WEAKENED** (rhetoric — the identity only "kills everything" after the spatial-gradient piece is already dropped on separate grounds) | No math change; framing already scoped correctly by citing `FINDING_P47` Part 5 for the spatial-gradient argument. |
| Part 3 (`δT₀₀^(int)` sign consistency with Part 2/4) | **CONFIRMED** — signs self-consistent with a single overall `T_μν=g_μν·L` convention | No change. |
| Part 4 (`δT₀₀^(matter)`, and whether `ρ` is the same object across Parts 1–4) | **CONFIRMED** (result), **WEAKENED** (the agreement between the Lagrangian-density and fluid-4-velocity derivations of `ρ` is specific to dust at linear order, not independently verified to generalize) | Noted as a scope limitation; not re-derived from a full fluid action here. |
| Parts 5–6 (solving `Ψ_k` with `Ψ_k` on both sides via `sp.solve`) | **CONFIRMED** (algebra) — no back-substitution residual check performed | Accepted as a minor completeness gap, not fixed (low priority relative to Part 7/10). |
| **Part 7 (`θ=0` continuity closure)** | **FALSIFIED** — missing `+3ρ̄Ψ̇_k` term, contradicts Part 4's own logic | **Fixed** — independently re-derived from scratch via covariant divergence (own standalone verification, not just accepting the citation), confirming the skeptic's exact formula. |
| Part 8/9 (exact `μ(a,k)`, large-`k` limit) | **WEAKENED** — "exact" formula rests on the flawed Part 7; leading term likely survives but wasn't checked for robustness | **Fixed** — leading term explicitly re-verified independent of a generic closure coefficient `c`; "exact" claim for the full form retracted. |
| **Part 10 (`δμ→0` as `ĝ→0` "sanity check")** | **FALSIFIED as evidence** — tautological by construction, zero discriminating power | **Fixed** — replaced with a genuine external check (Friedmann-imposed + subhorizon limit reduces to `μ=1`). |
| Part 11 (H1 verdict confidence) | **WEAKENED** — original wording overclaimed confidence given the compounded approximations | **Fixed** — split into leading-order (confirmed, robust) vs full-`k` (explicitly not established). |
| "Parts 1–6 need no new assumption beyond P46–P49" | **CONFIRMED technically, misleading semantically** — true for Parts 1–6, but the *closed* `μ(a,k)` only appears after Part 7's assumption | **Fixed** — language throughout now distinguishes the "P50A-strict" (no new assumption) result from the closed, assumption-dependent one. |

**No verdict here meets the Step 8a "true kill" bar** (per the skeptic's
own assessment) — the core leading-order predicate (`μ→1−ĝφ̄`, generically
`≠1`) survives both corrections intact, independently re-verified for
robustness rather than merely re-asserted. The errors found were real and
fixed with genuine re-derivation, not softened language — consistent with
this campaign's established pattern.

## Reproduction

```bash
python experiments/20260803-bridge/P50A_structural_mu_ak.py
```
