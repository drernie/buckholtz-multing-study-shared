# P59 — perturbed `Q^0`/`Q^1` with explicit `ρ_A`/`ρ_phys` semantics: continuity corrects to the simple uncoupled form, Euler equation gets a genuinely new exact form

**Date:** 2026-08-17
**Status:** Built, run, ruff clean, all assertions pass. **Skeptic review
(Step 8a): COMPLETE.** Independently re-derived the entire chain by hand
from first principles (Christoffels, `T_m^{μν}` components, both
divergence components, expansion, background substitution) and confirmed
every core algebraic claim — no true kill. Found one genuine framing
weakness: the `ν=1` result, expressed in the raw `V_x` variable, looks
structurally different from `ν=0`, but is not actually more complex —
see Part 5 below, added after the review and independently re-verified
before accepting.
**Origin:** direct response to the user's own physics review of `FINDING_P58`,
proposed as the natural next step: `P58` resolved the Route A/Route B
tension at **background order only**. This file extends the same
resolution to **linear (perturbative) order**, following the user's own
pre-registered `Q1`/`Q2`/`Q3` outcome classification, never using a bare
`ρ` — only `ρ_A`, `ρ_phys`, `δρ_A`, `δρ_phys`, explicitly, throughout.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P59_perturbed_Qmu_density_semantics_explicit.py`, ruff clean,
all assertions pass.

## Scope, stated up front

Background + linear order only, `Φ=Ψ=0` (matching `FINDING_P55/P56`'s own
scope). Does not extend to the `Φ,Ψ`-perturbed metric (`FINDING_P57`'s own
extension). Does not yet feed the corrected equations into `FINDING_P50A`'s
own Poisson-type relation — the decisive `D1`/`D2`/`D3` test the user
pre-registered requires that further step.

## User's own pre-registered outcomes (tested, not assumed)

- **`Q1`** — exact agreement survives perturbations.
- **`Q2`** — agreement only after an extra term (P55/P56's equations need
  correcting).
- **`Q3`** — decomposition ambiguity: `Q^μ` itself not unique.

## Part 1 — the bare/physical relation at linear order

`ρ_phys:=ρ_A(1-ĝφ)` (exact, `FINDING_P33`/`FINDING_P58`), split into
`ρ_A=ρ̄_A+εδρ_A`, `φ=φ̄+εδφ`:

```
ρ̄_phys = ρ̄_A(1-ĝφ̄)                                   (ε⁰, matches P58 exactly)
δρ_phys = (1-ĝφ̄)δρ_A - ĝρ̄_Aδφ                         (ε¹, user's own pre-derived form)
```

Both verified via direct symbolic expansion — the user's own derivation
independently re-confirmed before use, per `audit-verification-gate.md`.

## Part 2 — Route A (reused, relabeled, not recomputed)

`FINDING_P55/P56`'s own `Q^0`/`Q^1`, unchanged numerically, symbols
relabeled to make the physical meaning explicit (per `FINDING_P58`):

```
Q⁰_A[ρ_A] = -ĝ(δρ_A·φ̄̇ + ρ̄_A·δφ̇)
Q¹_A[ρ_A] = ĝρ̄_A·∂_xδφ/a²
```

## Part 3 — Route B (genuinely new)

`T_m^{μν}:=ρ_phys·u^μu^ν` built **directly** from `ρ_phys` (expressed via
`ρ_A` per Part 1), same kinematic ansatz (`u⁰=1`, `u¹=εV_x`) as
`FINDING_P56`'s own Part 3. Covariant divergence computed via the same
already-verified machinery.

## Part 4 — the decisive comparison, done correctly

**Raw residuals are not the right test** — they mix `ρ̄_A`'s own defining
background relation into apparent "new content." Substituting `ρ̄_A`'s own
background relation (`ρ̄̇_A=-3Hρ̄_A`) first, *then* checking whether what
remains factors cleanly, is the correct test — mirrors `FINDING_P58`'s
own background-order method exactly.

**`ν=0` (continuity) — factors exactly:**

```
[∇_μT_m^{μ,0}]_B - Q⁰_A  =  (1-ĝφ̄)·[ρ̄_A∂_xV_x + δρ̇_A + 3Hδρ_A]
```

verified, zero remaining residual. Since `(1-ĝφ̄)` is generically nonzero,
the closure requires the bracket to vanish:

```
ρ̄_A∂_xV_x + δρ̇_A + 3Hδρ_A = 0        (simple, UNCOUPLED continuity)
```

**`ν=1` (Euler) — does not factor as simply.** The same `(1-ĝφ̄)ρ̄_A(V̇_x+2HV_x)`
factorization leaves a genuine, nonzero extra term. Dividing the full
closure equation by `ρ̄_A(1-ĝφ̄)` directly instead gives the exact, closed
form (verified, zero residual):

```
V̇_x + [2H - ĝφ̄̇/(1-ĝφ̄)]V_x = ĝ∂_xδφ / [a²(1-ĝφ̄)]
```

## Part 5 — [added after skeptic review] the natural momentum variable removes the asymmetry

The `1/(1-ĝφ̄)` form above is not the cleanest presentation. The skeptic
found — independently re-verified here before accepting, per
`audit-verification-gate.md` — that in the rescaled momentum variable
`W_x:=(1-ĝφ̄)V_x` (physically: `ρ_phys·V_x/ρ̄_A`, the momentum-per-bare-mass,
the natural quantity given `ρ_phys` is the actual gravitating mass), the
equation collapses to **exactly** the standard undressed form:

```
Ẇ_x + 2HW_x = ĝ∂_xδφ/a²
```

Verified via direct symbolic substitution: the `1/(1-ĝφ̄)` factor cancels
**completely**, on both the friction term and the force term, not just
one. In this variable, `ν=0` (continuity, for `δρ_A`) and `ν=1`
(momentum, for `W_x`) are **structurally identical** to standard
uncoupled dust equations, each carrying its own `ĝ`-sourced RHS. The
"`ν=0` clean, `ν=1` messy" asymmetry from Part 4 is a **variable-choice
artifact** (`V_x` vs `W_x`), not a genuine physical asymmetry between the
two equations.

## Verdict — mixed outcome, tested independently per component

**`ν=0`: `Q2`, clean.** `FINDING_P56`'s own Part 4 continuity equation
(built from the shared `ρ` symbol with a `ĝ`-sourced RHS) is corrected to
the simple, uncoupled form `ρ̄_A∂_xV_x+δρ̇_A+3Hδρ_A=0` — matching the
*same* pattern `FINDING_P58` already established at background order:
`ρ_A` is always simply, purely conserved, at every perturbative order.
All coupling content lives in the *algebraic*
`δρ_phys=(1-ĝφ̄)δρ_A-ĝρ̄_Aδφ` relation (Part 1), not in `δρ_A`'s own
dynamics. This is a genuine correction to `FINDING_P56`, simpler than the
original, not more complex.

**`ν=1`: `Q2` in the `V_x` variable, `Q1`-like in the natural physical
variable.** The corrected Euler equation,
`V̇_x+[2H-ĝφ̄̇/(1-ĝφ̄)]V_x=ĝ∂_xδφ/[a²(1-ĝφ̄)]`, is exact (no truncation)
and genuinely different in structure from both `FINDING_P56`'s
re-confirmed (post-Gate-2-retraction) form
(`V̇_x+2HV_x=ĝ∂_xδφ/a²`, correct only if `T_m` is built from `ρ_A`
directly) and the earlier *retracted* Gate-2 form
(`V̇_x+(2H-ĝφ̄̇)V_x=...`, which lacked the `1/(1-ĝφ̄)` factors entirely and
rested on an inconsistent premise). **But in the rescaled `W_x` variable
(Part 5), this collapses to the same standard undressed form as `ν=0`** —
the apparent extra complexity was a variable-choice artifact, not
physical content. Either form is the physically relevant one if
`T_m^{μν}` is meant to represent `ρ_phys` — the actual gravitating
density — which it should, for any downstream use feeding Einstein's
equations (e.g. `FINDING_P50A`'s own Poisson-type relation).

**`Q3` not invoked.** Both components resolved to a definite, exact
answer once `ρ_A`/`ρ_phys` were properly disambiguated — no decomposition
ambiguity was found necessary to explain the results. Whether `Q^μ`
itself is unique independent of the `ρ_A`/`ρ_phys` question remains
untested here — a separate, deeper question.

## What this establishes, precisely

1. `δρ_phys=(1-ĝφ̄)δρ_A-ĝρ̄_Aδφ`, the user's own pre-derived linear-order
   bare/physical relation, independently re-verified.
2. `FINDING_P55/P56`'s own `Q^0`/`Q^1` formulas are unchanged numerically
   (correctly understood as functions of `ρ_A`, not `ρ_phys`).
3. `T_m^{μν}` built correctly from `ρ_phys` gives, at `ν=0`, the simple
   uncoupled continuity equation for `ρ_A` — correcting `FINDING_P56`'s
   own Part 4.
4. At `ν=1`, an exact, genuinely new Euler equation with `1/(1-ĝφ̄)`
   factors in both the modified friction term and the force term — a real
   physics correction to `FINDING_P56`'s own re-confirmed Part 5.

## What this does NOT establish

1. **The actual correction commit to `FINDING_P56` itself.** This file
   identifies what needs correcting; applying it is a separate, immediate
   next step (per this campaign's own null-retroscan discipline).
2. **The `Φ,Ψ`-extension.** Scope unchanged from `FINDING_P55/P56`.
3. **The decisive `D1`/`D2`/`D3` test** the user pre-registered — whether
   `FINDING_P50A`'s own `μ_metric≠1` is a real observable effect or a
   density-definition artifact. Requires feeding these corrected
   equations into `FINDING_P50A`'s own Poisson-type relation, expressed
   through `δρ_phys` — a further, not-yet-attempted step.
4. **The `Q3` concern** (decomposition ambiguity of `Q^μ` itself,
   independent of the `ρ_A`/`ρ_phys` question) — untested here.
5. **Any numeric value.** `ĝ`, `φ̄`, `ρ_A`, `δφ` remain symbolic
   throughout.
6. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction,
   not a claim about TJB's own unpublished theory.

## Skeptic Verdict (Step 8a, context-blind — claim.md + code only, no session history)

| Sub-claim | Skeptic verdict | Response |
|---|---|---|
| Part 1 (`δρ_phys` linearization) | **CONFIRMED-REAL** — trivial Leibniz, independently re-derived | No change. |
| `ν=0` exact factorization `(1-ĝφ̄)·[δρ̇_A+3Hδρ_A+ρ̄_A∂_xV_x]` on-shell | **CONFIRMED-REAL** — independently re-derived from Christoffels/T^μν directly, exact, two genuine cancellations identified (pre- and post-background-substitution) | No change. |
| "`(1-ĝφ̄)≠0` ⇒ bracket must vanish" — is this circular? | **CONFIRMED-REAL, not circular** — standard use of a conservation law to derive an EOM, not assuming the conclusion. Local caveat named: points where `1-ĝφ̄=0` would need separate treatment, outside this finding's scope | **Noted**, no change needed — finding never claimed global coverage. |
| `ν=1` exact form `V̇_x+[2H-ĝφ̄̇/(1-ĝφ̄)]V_x=ĝ∂_xδφ/[a²(1-ĝφ̄)]` | **CONFIRMED-REAL** — independently re-derived, matches exactly, including the `5H→2H` reduction via background substitution and a `ĝ→0` sanity check reducing to standard decoupled dust | No change. |
| "`ν=0` clean, `ν=1` genuinely more complex" (original framing) | **WEAKENED** — true only for the raw `V_x` variable; in `W_x:=(1-ĝφ̄)V_x`, the `ν=1` equation collapses to the same standard undressed form as `ν=0`, revealing the asymmetry as a variable-choice artifact, not physical content | **Fixed.** Part 5 added, independently re-verified before accepting, Verdict section reworded throughout. |
| Sign errors anywhere | **CONFIRMED-REAL: none found** — cross-checked via from-scratch Christoffel/`T^μν` construction, both cancellation patterns, and the `ĝ→0` limit | No change. |

**True kill assessment:** no. Every core algebraic claim survived
independent from-scratch re-derivation (Christoffels, `T^{μν}` components,
both divergence components, background substitution, `ĝ→0` sanity check).
The one substantive finding — that the `ν=0`/`ν=1` asymmetry is a
variable-choice artifact, not a physical one — *strengthens* the result:
both equations are, in their natural variables, structurally identical to
standard uncoupled dust with a `ĝ`-sourced RHS, a cleaner and more
symmetric picture than the finding's own first-pass framing suggested.

## Reproduction

```bash
python experiments/20260803-bridge/P59_perturbed_Qmu_density_semantics_explicit.py
```
