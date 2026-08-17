# P58 — Route A (scalar-stress closure) vs Route B (worldline mass-coupling) `Q^0` consistency audit — routes agree EXACTLY once `ρ` is disambiguated, retracting `FINDING_P56`'s own Gate-2 correction

**Date:** 2026-08-17
**Status:** Built, run, ruff clean, all assertions pass, after two genuine
self-caught sign bugs (found and fixed before any skeptic review) and one
**substantial post-skeptic revision** — see below. **Skeptic review (Step
8a): COMPLETE. The skeptic's own independent counter-derivation
overturned this file's original C1 ("leading-order-only agreement")
verdict — independently re-verified before accepting, per
`audit-verification-gate.md`, and extended further: the correct
resolution not only resolves the Route A/B tension exactly, it also
**retracts `FINDING_P56`'s own same-day Gate-2 correction**, which turns
out to rest on a mathematically impossible assumption. See Verdict below.**
**Origin:** direct response to the user's own physics review, proposed as
a *replacement* for the originally-planned "just derive perturbed
`Q^0`/`Q^i`" next step. Before extending `Q^0`/`Q^1` to the `Φ,Ψ` metric
(which would unblock the `FINDING_P50A` re-scan), the user asked whether
`Q^μ` as derived by this campaign's own method (scalar-stress divergence)
is itself consistent with the matter sector's own already-established
worldline mass-coupling action (`FINDING_P33`'s `m_eff(φ)/m=1-ĝφ`,
verified *exact* there). If not, correcting `FINDING_P50A` on one of two
possibly-inconsistent `Q^μ` definitions would be premature.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P58_two_route_Qmu_consistency_audit.py`, ruff clean, all
assertions pass.

## Scope, stated up front

Background order only (no `ε`) — deliberately keeps the cosmological-
perturbation expansion parameter (`P48/P54/P55/P56/P57`'s own `ε`) and the
coupling-strength expansion parameter (`ĝφ̄`) strictly separate, per the
user's own explicit methodological caution against conflating the two.

## Route A — scalar-stress divergence (this campaign's own established method)

`T_φ^{μν}=∂^μφ∂^νφ-g^{μν}[(1/2)(∂φ)²+V(φ)]` (extends the `V=0` `T_φ^{μν}`
already reused verbatim since `FINDING_P55` by adding `V(φ)`). General
identity, independently verified fresh here:

```
∇_μT_φ^{μν} = (□φ-V'(φ))·∂^νφ
```

Verified with `V(φ)=λ₄φ̄⁴/4` (`FINDING_P45`'s own quartic) — a **nonzero**
test case, not the trivial `V=0` limit. Field equation re-derived via
Euler-Lagrange on the FRW background specifically (not assumed from
`FINDING_P45`'s static result): `φ̄̈+3Hφ̄̇+λ₄φ̄³=ĝρ̄`, reducing exactly to
`FINDING_P34`'s own `V=0` equation at `λ₄=0` (checked, not assumed).

Substituting the field equation into the identity: `λ₄` (i.e. `V'`)
**cancels entirely** — confirmed with a nonzero `V`, not just asserted:

```
Q⁰_A = -ĝρ̄φ̄̇       (EXACT in ĝφ̄, no truncation, any V(φ))
```

`ρ̄` here is literally whatever "ρ" the Lagrangian coupling term
`-ρ(1-ĝφ)` refers to — see Verdict for why this matters.

## Route B — worldline mass-coupling (`FINDING_P33`'s own already-established relation)

New assumption, not previously used anywhere in the `Q^μ` closure route
(`P55/P56/P57`): number density dilutes as pure dust, `n̄̇+3Hn̄=0`,
independent of `φ` (particle *number* is conserved regardless of the
mass-coupling). With `ρ:=n̄·m(φ̄)`, general result (any `m(φ)`, verified
symbolically):

```
ρ̄̇+3Hρ̄ = ρ̄·(d ln m/dφ)·φ̄̇        (this IS Q⁰_B, in general form)
```

Specialized to `FINDING_P33`'s own `m_eff(φ)/m=1-ĝφ` (verified *exact*
there — reused, not re-derived):

```
Q⁰_B = -ĝρ̄φ̄̇/(1-ĝφ̄)
```

## Comparison (naive, pre-resolution)

Not identical exactly (`Q⁰_A-Q⁰_B≠0` symbolically, taking the SAME symbol
`ρ̄` in both). Taylor-expanding `Q⁰_B` in `ĝ`: its `O(ĝ¹)` term matches
`Q⁰_A` exactly; `Q⁰_B`'s `O(ĝ²)` term is nonzero. **This apparent
discrepancy is fully resolved below — it is a same-symbol-two-meanings
artifact, not real physics disagreement.**

## Two self-caught sign bugs (found and fixed before any skeptic review)

1. The first version hardcoded `Q0_A=+ĝρ̄φ̄̇` (positive) to check against
   the substitution result — the assertion **failed**. Re-checked against
   `FINDING_P56`'s own already-established Gate-2 sign convention
   (`Q^0_background := -∇_μT_φ^{μ,0}|_bg,onshell = -ĝρ̄φ̄̇`) — the negative
   sign is the one already committed to this campaign's convention. Fixed
   by matching it, not by picking whichever sign made the assertion pass.
2. Route B's `Q⁰_B` was first computed with an extra, inconsistent overall
   minus sign relative to its own already-verified general relation
   (`ρ̄̇+3Hρ̄=ρ̄·(d ln m/dφ)·φ̄̇`, no extra sign flip) — caught by re-reading
   my own derivation, fixed to match the general relation directly.

## The resolution — `ρ` means two different things in Route A and Route B

**Context-blind skeptic review** independently re-derived the whole
chain and identified the actual source of the `O((ĝφ̄)²)` gap: Route A's
`ρ̄` is *literally* whatever "ρ" the field equation's own source term
refers to — per `FINDING_P33`'s fluid-limit construction (`N` worldlines,
each `S_i=-c∫dτ·m·(1-ĝφ)`, summed), this is the **bare** density
`ρ_A:=n̄·m₀` (`φ`-independent by construction — `m₀` is the *fixed
reference* mass, not the physical, `φ`-dependent `m_eff(φ)`). Route B's
own general relation, by contrast, used `ρ` directly as `n̄·m(φ̄)` — the
**physical**, `φ`-dependent energy density `ρ_phys`.

**Independently re-verified before accepting** (per
`audit-verification-gate.md`): can `ρ_A` — which by its own definition
satisfies pure decoupled dust dilution (`ρ̇_A+3Hρ_A=0`, since it tracks
conserved particle number times a *fixed* mass) — also satisfy a
self-sourced coupled evolution `ρ̇+3Hρ=-ĝρφ̄̇` (i.e. `FINDING_P56`'s own
Gate-2 closure, applied to the same symbol on both sides)? **No** —
these are equal only if `ĝρ_Aφ̄̇=0` identically, which is not true in
general. `ρ_A` cannot self-consistently satisfy Gate 2's own closure —
a genuine internal inconsistency in Gate 2's own reasoning, not merely
an unexamined modeling choice.

**The exact resolution:** `ρ_phys:=ρ_A(1-ĝφ̄)` (matching `FINDING_P33`'s
own mass law algebraically, no approximation) satisfies the closure
**exactly**, using `ρ_A` specifically on the source side (matching the
field equation's own `ρ`), not `ρ_phys`:

```
∇_μT_m^{μ,0}[ρ_phys=ρ_A(1-ĝφ̄)]  =  Q⁰_A[using ρ_A]  =  -ĝρ_Aφ̄̇   (exact, zero residual)
```

Confirmed via direct symbolic substitution — no Taylor truncation
needed at all.

## Verdict [SUBSTANTIALLY REVISED after context-blind skeptic review, Step 8a]

**Not C1** (leading-order-only truncation, as this file originally
concluded, before the skeptic's counter-derivation). **The routes agree
exactly**, once `ρ` is correctly disambiguated: Route A's `ρ` (field
equation / Lagrangian coupling term) is the bare density `ρ_A`; the
physical, gravitating density is `ρ_phys=ρ_A(1-ĝφ̄)` — an exact algebraic
relation, matching `FINDING_P33`'s own already-established mass law
directly, with no truncation, no approximation, and no new differential
equation to integrate at all.

**This retracts `FINDING_P56`'s own Gate-2 correction** (same-day,
earlier this session): Gate 2 assumed the same symbolic `ρ̄` (used
identically throughout `FINDING_P56` for both `T_m^{μν}` and, via the
shared field equation, `Q^0`/`Q^1`) satisfies a self-sourced coupled
background continuity `ρ̄̇=-3Hρ̄-ĝρ̄φ̄̇`, with exponential solution
`ρ̄∝a^{-3}\exp[-ĝ(φ̄-φ̄_0)]`. **Proven above: this is mathematically
impossible** for `ρ_A` (the bare density that `FINDING_P56`'s own
construction actually uses, by its shared-symbol internal consistency) —
`ρ_A`, by its own defining property, satisfies only the simple decoupled
`a^{-3}` dilution.

**Consequence for `FINDING_P56`'s Euler-equation reduction:** Gate 2's
own "corrected" `V̇_x+(2H-ĝφ̄̇)V_x=ĝ∂_xδφ/a²` form must also be retracted.
The campaign's *original* (pre-Gate-2) addendum #1 — `V̇_x+2HV_x=Q¹/ρ_A`,
i.e. `v̇+Hv=0` in physical peculiar velocity — is **re-confirmed as
correct**, using `ρ_A`'s own simple, uncoupled dilution (the
internally-consistent reading of `FINDING_P56`'s own shared `ρ̄` symbol).

**What survives from the whole Gate-2 excursion:** the closure does
produce a genuine nonzero `Q^0` at background order — this computation
itself was and remains correct, re-verified independently multiple
times. What was wrong was interpreting that nonzero `Q^0_background` as
evidence `ρ_A` itself must obey a *new* coupled ODE. The correct
interpretation: `Q^0_background` is exactly the derivative consequence
of an already-existing *algebraic* mass-coupling relation
(`FINDING_P33`'s own `m_eff/m=1-ĝφ`) between `ρ_A` and a different,
distinguishable quantity (`ρ_phys`) — no new physics needed integrating,
it falls straight out of `FINDING_P33`'s own already-established result.

**Scope caveat, stated honestly:** this resolution assumes
`FINDING_P56`'s own field-theoretic `ρ` (used throughout `P34`–`P57`'s
Lagrangian) *is* literally the fluid limit of `FINDING_P33`'s own
worldline action — an assumption `FINDING_P33` itself explicitly did
**not** establish beyond the single-point-particle level (its own §4,
point 2). This file treats that linkage as the most natural,
best-motivated reading available (it is the only one that resolves the
Route A/B tension exactly), not as something independently, separately
proven.

## What this establishes, precisely

1. `Q⁰_A=-ĝρ_Aφ̄̇`, exact in `ĝφ̄`, `V`-independent (verified with a
   nonzero test potential).
2. The general worldline-mass-coupling continuity relation
   `ρ̄̇+3Hρ̄=ρ̄(d ln m/dφ)φ̄̇`, verified for any `m(φ)`.
3. `ρ_phys:=ρ_A(1-ĝφ̄)` satisfies the closure exactly against `Q⁰_A`
   (using `ρ_A` on the source side) — zero residual, no truncation.
4. `ρ_A` cannot self-consistently satisfy a self-sourced coupled closure
   (proven directly) — `FINDING_P56`'s Gate-2 exponential-continuity
   claim is retracted; the original, pre-Gate-2 addendum #1 reduction is
   re-confirmed correct.
5. The nonzero background-order `Q^0` (Gate 2's genuine discovery) is
   the derivative consequence of `FINDING_P33`'s own already-established
   algebraic mass law, not a new differential equation.

## What this does NOT establish

1. **A fresh, independent derivation of `FINDING_P33`'s mass law from
   this campaign's own field-theoretic action.** The linkage between
   the two (field-theoretic `ρ` ≡ fluid limit of `FINDING_P33`'s
   worldline action) is treated as the best-motivated reading, not
   separately proven — `FINDING_P33` itself scoped its own result to the
   point-particle level only.
2. **`Q^i` (the spatial/Euler-equation source term itself, `FINDING_P55`
   `Q⁰`/`FINDING_P56` `Q¹`)** beyond the specific Euler-equation
   reduction consequence noted in the Verdict — the full Route A/B
   comparison for `Q^i` directly is not attempted here.
3. **The actual `FINDING_P56` correction commit** — this file identifies
   what needs correcting; applying the correction to `FINDING_P56` itself
   is a separate, immediate next step (per this campaign's own
   null-retroscan discipline: apply immediately, don't defer silently).
4. **Any numeric value.** `ĝ`, `φ̄`, `ρ_A`, `λ₄` remain symbolic
   throughout.
5. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction,
   not a claim about TJB's own unpublished theory.

## Skeptic Verdict (Step 8a, context-blind — claim.md + code only, no session history)

| Sub-claim | Skeptic verdict | Response |
|---|---|---|
| Identity `∇_μT_φ^{μν}=(□φ-V')∂^νφ` general for canonical scalar | **CONFIRMED-REAL** — independently re-derived from scratch | No change. |
| `V'` cancels entirely from `Q⁰_A` for any `V` | **CONFIRMED-REAL**, and structural (field equation reads `□φ-V'=source`, cancels by construction) — the quartic test is a redundant sanity check, not evidence of generality | No change. |
| `Q⁰_A=-ĝρ̄φ̄̇` "exact in `ĝφ̄`" | **WEAKENED (originally)** — exact only if `ρ̄` is read consistently as the Lagrangian parameter | **Fixed** — see Resolution: `ρ̄` in `Q⁰_A` is now explicitly identified as `ρ_A` (bare). |
| `Q⁰_B=-ĝρ̄φ̄̇/(1-ĝφ̄)` | **CONFIRMED-REAL**, with `ρ̄`=physical density `n̄·m_eff` | No change. |
| "Routes agree at `O(ĝ)`, diverge at `O(ĝ²)`" (original C1 headline) | **FALSIFIED (misframed)** — writing both formulas with the *same* physical `ρ` makes them identical to all orders once `ρ_A↔ρ_phys` is properly substituted | **Fixed** — full section added, verified, C1 verdict replaced. |
| "C1: both-legitimate parametrizations valid only to `O(ĝφ̄)`" | **WEAKENED** — right that it's the same physics, wrong that the equivalence is truncated; it is exact | **Fixed** — retracted, replaced with exact resolution. |
| `FINDING_P56`'s Gate-2 "coupled continuity, exponential solution" | **CONFIRMED, wrong mechanism** — the exponential is wrong beyond `O(ĝ)`; the exact answer is the *linear* factor `(1-ĝφ̄)`, not an exponential | **Fixed** — retraction propagated here; `FINDING_P56` itself to be corrected next. |
| "Route A exact, Route B has `O(ĝ²)` corrections" framing | **BACKWARDS-CANDIDATE / WEAKENED** — both are exact when properly interpreted; if anything Route B (direct mass-law route) is the less fragile reading | **Fixed** — framing corrected throughout. |
| "Deeper open question: bare vs. physical `ρ`" (originally listed as unresolved) | **CONFIRMED-REAL as an issue, but MIS-SCOPED** — this is not a possible deeper inconsistency to investigate later, it is the actual cause of every disagreement found | **Fixed** — promoted from a footnote to the Verdict's own load-bearing content. |
| Sign-convention self-consistency throughout | **CONFIRMED-REAL** — `(-,+,+,+)` signature, `∂^0φ=-φ̇`, `□φ=-φ̈-3Hφ̇`; `ĝφ̇>0⇒Q^0<0` matches `m_eff` decreasing with `φ` — no inconsistency found | No change. |

**True kill assessment:** the *original* C1 verdict was killed —
correctly, per the skeptic's own independent counter-derivation,
verified above before accepting. What replaces it is a stronger,
positive result (exact agreement, not approximate) that additionally
**retracts a same-day, already-committed correction** (`FINDING_P56`'s
Gate 2). This is exactly the kind of self-correction this campaign's own
discipline is built to catch — a real reversal, applied immediately, not
silently absorbed.

## Reproduction

```bash
python experiments/20260803-bridge/P58_two_route_Qmu_consistency_audit.py
```
