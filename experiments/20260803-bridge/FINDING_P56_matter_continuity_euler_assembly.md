# P56 — Step B2 Part 2: the matter Euler equation `d/dt(ρ̄V)+5Hρ̄V=Q¹=ĝρ̄∂_xδφ/a²`, assembled from `∇_μT_m^{μν}=Q^ν`

**Date:** 2026-08-17
**Status:** Built, run, ruff clean, all assertions pass, after a genuine
in-build self-caught bug (see below — a hand-derivation error in a test
assertion, kept visible, not silently patched). **Skeptic review (Step
8a): COMPLETE. Not a true kill — the central `5H` Euler-equation
coefficient independently confirmed via two separate derivation routes
(geodesic + direct covariant divergence). Real gaps found: a closure
caveat inherited from P55 but not restated here, and — most
significant — a genuine cross-finding drift with `FINDING_P50A`'s own
(now superseded) continuity equation. See Skeptic Verdict below.**
**Addendum #2 (2026-08-17, second round of user physics review):** the
background matter continuity equation is itself **coupled**
(`ρ̄̇=-3Hρ̄-ĝρ̄φ̄̇`, not the standard uncoupled form) — a genuine new
implication of this file's own closure at background order, previously
unchecked. This corrects Addendum #1's `5H→2H→H` reduction (valid only
at `ĝ=0`, not as a general claim) to `V̇_x+(2H-ĝφ̄̇)V_x=ĝ∂_xδφ/a²`. See
Part 5 for the full derivation and verification.
**Origin:** direct continuation of `FINDING_P55` (B2 Part 1, which
derived only `Q⁰`). This file derives `Q¹` (spatial source, same method,
new index) and assembles the actual continuity + Euler equations from
`∇_μT_m^{μν}=Q^ν` — the user's own equation, now fully instantiated for
the committed monopole action.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P56_matter_continuity_euler_assembly.py`, ruff clean, all
assertions pass.

## Scope, stated up front

Same `Φ=Ψ=0` metric as `FINDING_P55` — required, per P55's own
self-caught scope-mismatch bug (mixing this scope with `FINDING_P54`'s
`Φ`-inclusive metric silently breaks the general covariant identity).
The `Φ,Ψ`-extension remains the named open gap before the B1↔B2
compatibility check (`FINDING_P54`'s `G_0i`) can be attempted honestly.

## Kill-gates satisfied (subset of the user's own seven)

**KG-B2a:** `Q¹` is not inserted by hand — reused from the *same* general
covariant identity as P55's `Q⁰`, independently re-checked for the `ν=1`
component (not assumed to carry over from `ν=0`).
**KG-B2b:** same gauge/scope as P55 throughout, stated explicitly.
**KG-B2c:** `θ=0` (irrotational dust) is **not** substituted before
derivation — the velocity field `V^i(t,x,y,z)` is kept fully general
throughout; `θ:=div(V)` is never assumed zero going in.
**KG-B2f:** `ĝ` used only symbolically — the P39 Reading-1-vs-Reading-2
ambiguity is not touched by this file at all.

## In-build self-caught bug (found and fixed before any skeptic review)

The first version of the decoupled (`ĝ=0`, force-free) Euler-equation
positive control asserted the expected form as `d/dt(ρ̄V)+3Hρ̄V=0`
(density dilution only). The assertion **failed**. Independently
re-derived the correct form from the geodesic equation directly, before
patching anything: for a free particle on `ds²=−dt²+a²dx²`, physical
momentum redshifts as `1/a`, i.e. the **peculiar velocity itself**
redshifts as `V̇+2HV=0` — a separate effect from density dilution. The
momentum-*density* equation combines both: `d/dt(ρ̄V)=ρ̄̇V+ρ̄V̇=
(−3Hρ̄)V+ρ̄(−2HV)=−5Hρ̄V`, i.e. `ρ̄V∼a⁻⁵` (density `∼a⁻³` **times**
velocity `∼a⁻²`). The corrected assertion (`5H`, not `3H`) matches the
script's own sympy output exactly.

## Part 1–2 — `Q¹`, same machinery, new index

Metric, Christoffels, `T_φ^{μν}`: identical construction to
`FINDING_P55`. `box(φ)^{(1)}` re-verified to match P55's own result
exactly (reuse-fidelity check).

```
∇_μT_φ^{μ,1}|^{(1)} = (□φ)·∂^1φ|^{(1)}   (script assertion, checked
                                          independently for ν=1, not
                                          assumed from P55's ν=0 case)
Q¹ := -∇_μT_φ^{μ,1}|^{(1)} = ĝρ̄·∂_xδφ/a²
```

## Part 3 — matter stress tensor, general velocity field

`T_m^{μν}=ρu^μu^ν`, with `u^0=1` (exact to `O(ε)` on this metric — no
`Φ` to source a correction) and `u^i=εV^i(t,x,y,z)` kept fully general
(KG-B2c). Pressureless dust: `T_m^{11}=O(ε²)`, no stress term needed at
linear order.

## Part 4 — continuity equation (`ν=0`)

```
ρ̄∂_xV_x + δρ̇ + 3Hδρ = ĝ(−δρ·φ̄̇−ρ̄·δφ̇)
```

**Positive control:** decoupled (`ĝ=0`) limit matches the standard
textbook pressureless-dust continuity equation exactly (script
assertion) — no metric-perturbation term here, since `Φ=Ψ=0` in this
scope (unlike `FINDING_P50A`'s own continuity, which used the
`Φ,Ψ`-perturbed metric and picked up a `3ρ̄Ψ̇` term).

## Part 5 — the matter Euler equation (`ν=1`) — the deliverable

```
d/dt(ρ̄V_x) + 5H·ρ̄V_x = ĝρ̄·∂_xδφ/a²
```

**Positive control (corrected, see above):** decoupled limit matches the
geodesic-verified momentum-density dilution form (`5H`, not the
originally-guessed `3H`) exactly.

**Addendum #1, prompted by the user's own physics review after this
file's first commit:** the `5H` coefficient is a property of the
*momentum-density* bookkeeping (`ρ̄V_x` combined), not an independent
physical statement — convention-sensitive, not anomalous. Dividing by
`ρ̄` and eliminating `ρ̄̇` reduces it to a velocity equation.

**[CORRECTED after a second round of user physics review, same day]**
~~Dividing the momentum-density Euler equation by `ρ̄` and eliminating
`ρ̄̇` via the background continuity equation (`ρ̄̇=-3Hρ̄`) collapses it
exactly to `V̇_x+2HV_x=F_φ/ρ̄`... in physical peculiar velocity `v:=aV_x`,
this is `v̇+Hv=F_φ/(aρ̄)` — the ordinary single-`H` peculiar-velocity
redshift.~~ The user's own re-review correctly flagged this as a
**"decoupled-control variable conversion" mislabeled as a general coupled
reduction**: it used the *uncoupled* background continuity
`ρ̄̇=-3Hρ̄`, but the *same* closure this file's own Euler equation rests
on (`∇_μT_m^{μν}=Q^ν`) also applies at **background order**, not just the
linear order `FINDING_P55/P56` actually computed.

**Independently checked before accepting the user's claim** (per
`audit-verification-gate.md`): computing `∇_μT_φ^{μ,0}` at background
order (`φ=φ̄(t)` only, general covariant identity `(□φ)·∂^0φ`) gives
`φ̄̇φ̄̈+3Hφ̄̇²`. Substituting `FINDING_P34`'s own background field equation
(`φ̄̈+3Hφ̄̇=ĝρ̄`) on-shell collapses this exactly to `ĝρ̄φ̄̇`. This means
`Q⁰_background:=-∇_μT_φ^{μ,0}|_{bg,onshell}=-ĝρ̄φ̄̇`, and the closure
`∇_μT_m^{μ,0}=Q^0` — applied consistently at background order —
implies a **coupled background continuity equation**:

```
ρ̄̇ = -3Hρ̄ - ĝρ̄φ̄̇   (NOT the standard uncoupled ρ̄̇=-3Hρ̄)
```

A genuine implication of this file's own closure, previously unchecked
within this project — `FINDING_P55/P56` only ever computed the
*linear-order* `Q⁰`/`Q¹`, never the background-order piece of the same
general identity. This solves to `ρ̄(t)=ρ̄_0a^{-3}\exp[-ĝ(φ̄(t)-φ̄_0)]`
rather than pure `a^{-3}` dilution.

**Context-blind skeptic review of this specific claim, independently
re-derived the full chain by hand from first principles (metric,
Christoffels, direct covariant divergence of `T_φ^μν` and `T_m^μν`, cross-
checked against the general identity) — CONFIRMED-REAL, no sign error, no
circularity.** Two flags from that review, both addressed: **(1) framing
— this is a *reproduction*, within this project's own framework, of a
known result, not a novel physical mechanism.** The structure
`ρ̄∝a^{-3}\exp[-ĝ(φ̄-φ̄_0)]` is exactly the standard coupled-quintessence
matter dilution (Wetterich 1995, *mass-varying particles*; Amendola,
*Coupled quintessence*, Phys. Rev. D 62, 043511 (2000), Eq. 5–6 —
already this campaign's own cited literature context via `FINDING_P49`).
**(2) retroscan check** — grepped the bridge experiments directory for
prior uses of the uncoupled `ρ̄̇=-3Hρ̄` substitution: found exactly one,
`FINDING_P50A`'s own script line 273 (`P50A_structural_mu_ak.py`), used
as an intermediate step deriving its own (already-flagged-for-re-scan)
Part 7 continuity equation. Not a new, separate finding — confirms and
localizes the *existing* `FINDING_P50A` re-scan dependency (this specific
line is exactly where the coupled substitution needs to replace the
uncoupled one), not an additional undiscovered drift site.

**Corrected reduction**, using the coupled background continuity:

```
V̇_x + (2H - ĝφ̄̇)V_x = ĝ∂_xδφ/a²
```

Verified via direct symbolic substitution, zero residual against the
expected form. The coupling **modifies the friction term itself**
(`2H → 2H-ĝφ̄̇`), not merely a separate force term on the RHS — the
standard structure of coupled-quintessence Euler equations. The earlier
`V̇_x+2HV_x=...`/`v̇+Hv=...` form is **not wrong as a decoupled-limit
statement** (it matches this file's own `ĝ=0` positive control exactly)
but is **wrong if read as the general coupled reduction** — retracted as
a general claim, correct only at `ĝ=0`.

`div(T_m^{μ,1})` itself contains **no `ĝ` at all** — the coupling enters
only through the equation `∇_μT_m^{μ,1}=Q^1`, not through `T_m`'s own
construction. So the force term is simply `Q¹` itself, moved to the RHS:

```
F_φ = Q¹ = ĝρ̄·∂_xδφ/a²
```

**Prediction check:** the user's own pre-registered prediction was
`F_φ∼ĝ²δρ`, obtained by substituting `FINDING_P46`'s quasi-static
`δφ_k=ĝa²δρ_k/k²`. That substitution is a **Fourier-space** statement;
this file's `Q¹` is in **real space** (`∂_x` of `δφ`). ~~A direct
real-space substitution would be a fabricated unit mismatch — stated as
an explicit next step, not attempted here.~~ **[CORRECTED after skeptic
review]** this framing was slightly overprotective: `FINDING_P46`'s
quasi-static reduction *also* has a real-space form directly available
(`∇²δφ=-ĝa²δρ`, the inverse-Fourier of its own k-space statement).
Substituting *that* (not the k-space `δφ_k`) into `Q¹` gives a genuine,
well-defined real-space next step: `Q¹=-ĝ²ρ̄∂_x(G∗δρ)/a²` (`G` = the flat-
space Laplacian Green's function) — an integro-differential statement,
**not** a local `F_φ∼ĝ²δρ` (that only holds mode-by-mode in Fourier
space). A reachable next step, not blocked on a full k-space translation
as the original framing implied.

## Verdict [CORRECTED after context-blind skeptic review, Step 8a]

Both the continuity and Euler equations are now assembled from the
user's own `∇_μT_m^{μν}=Q^ν` for the committed monopole action, within
the `Φ=Ψ=0` scope. Both decoupled limits verified against independently
re-derived standard forms — genuine positive controls, including one
that caught and fixed a real hand-derivation error before any skeptic
review.

**Closure caveat, inherited from `FINDING_P55` but not restated here —
fixed:** total stress-energy conservation, which *both* equations in
this file rest on, is **not** automatic in `FINDING_P46`'s own setup
(`ρ` treated as external, not dynamical) — it is a closure condition a
genuine matter model must satisfy, not a free-standing GR fact.

**Cross-finding drift, project-level, discovered by this file — not a
defect of this file's own derivation:** `FINDING_P50A`'s own matter
continuity equation (`∇_μT_m^{μ,0}=0`, no source term) is now
**inconsistent** with this file's own closure (`∇_μT_m^{μ,0}=Q⁰`, a real
`ĝ`-dependent source). P50A predates P55/P56's discovery that matter is
not separately conserved once coupled to `φ`. Per this campaign's own
null-retroscan discipline (a new result changing an assumption
underlying a prior finding is applied immediately, not deferred
silently), flagged explicitly here as an open item — `FINDING_P50A`'s
own Part 7 needs a re-scan against this closure before its continuity
equation is reused anywhere further. Not attempted in this file.
**Now a three-part dependency** (per Addendum #2 above): the `FINDING_P50A`
re-scan needs (a) the `Φ,Ψ`-extended `Q^0` (`FINDING_P57` supplies the
field equation prerequisite, not yet the extended `Q^0` itself), and (b)
the **coupled background continuity** discovered in Addendum #2
(`ρ̄̇=-3Hρ̄-ĝρ̄φ̄̇`), since `FINDING_P50A`'s own background solution
implicitly assumed the uncoupled `ρ̄∝a^{-3}`.

The Euler equation's decoupled limit correctly has no gravitational
force term, because this scope has no `Φ` to source one — a direct,
explicit consequence of scope, not evidence gravity is missing.

## What this establishes, precisely

1. `Q¹=ĝρ̄∂_xδφ/a²`, derived from the same general covariant identity as
   P55's `Q⁰`, independently re-checked for this component.
2. The matter continuity equation, with `Q⁰` as its source term, its
   `ĝ=0` limit matching the standard textbook form exactly.
3. The matter Euler equation, `d/dt(ρ̄V_x)+5Hρ̄V_x=ĝρ̄∂_xδφ/a²`, with `Q¹`
   as its fifth-force term, its `ĝ=0` limit matching the geodesic-derived
   momentum-density dilution form exactly (after a genuine self-caught
   correction from an initially-wrong `3H` guess).
4. A worked example of the campaign's own "no silent fixes" discipline:
   a wrong hand-derivation was caught by its own positive-control
   assertion failing, independently re-derived from first principles
   (the geodesic equation), and fixed with the correct physics — not
   patched to whatever sympy happened to output.
5. That the `5H` momentum-density coefficient is equivalent, under the
   background continuity relation, to the standard single-`H` peculiar-
   velocity redshift (`v̇+Hv=0` for physical peculiar velocity) — a
   convention clarification, independently verified, not a new result.

## What this does NOT establish

1. **The real-space quasi-static substitution.** Reachable (see Verdict),
   not blocked, but not attempted here.
2. **The `Φ,Ψ`-extension.** This equation has no gravitational force term
   because `Φ=Ψ=0` in this scope — not because gravity is absent from
   the physics. The B1↔B2 compatibility check against `FINDING_P54`'s
   `Φ`-inclusive `G_0i` requires this extension first.
3. **A test of the user's own pre-registered H0/H1/H2 split.** Requires
   both (1) and (2).
4. **Any numeric value.** `ĝ`, `φ̄`, `ρ̄` remain symbolic throughout.
5. **That total stress-energy conservation is automatic.** Inherited from
   `FINDING_P55`, it is a closure condition a genuine matter model must
   satisfy, not established here.
6. **Consistency with `FINDING_P50A`'s own continuity equation.**
   `FINDING_P50A`'s `∇_μT_m^{μ,0}=0` is now superseded by this file's own
   `∇_μT_m^{μ,0}=Q⁰` — a real, unresolved cross-finding drift, flagged
   explicitly, not fixed here.
7. **A fully general 3-component velocity field.** Only `V_x` is
   populated (sufficient for the x-Euler equation specifically); `θ:=
   div(V)` in full is not assembled.
8. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction,
   not a claim about TJB's own unpublished theory.

## Skeptic Verdict (Step 8a, context-blind — claim.md + code only, no session history)

| Sub-claim | Skeptic verdict | Response |
|---|---|---|
| Euler equation coefficient `5H` (corrected from `3H`) | **CONFIRMED-REAL** — independently re-derived via *two* separate routes (geodesic momentum conservation, and direct covariant divergence of `T^{μν}=ρU^μU^ν`), both giving `5H` exactly | No change. |
| `Q¹`'s `ν=1` identity check "independently meaningful" | **WEAKENED (wording)** — code genuinely re-executes with different index/Christoffel components, not a copy-paste, but the general identity holds for *any* `ν` once the machinery is correct, so this is a reuse-fidelity check on the helper, not new physics per se | **Fixed.** Wording corrected in both script and this document. |
| Four-velocity normalization `u⁰=1` exact to `O(ε)` | **CONFIRMED-REAL** — independently verified `(U⁰)²=1+O(ε²)` on this metric | No change. |
| `Q¹` genuinely fresh (not a temporal→spatial copy-paste) | **CONFIRMED-REAL** — the single-term structure of `Q¹` vs. the two-term structure of `Q⁰` correctly reflects that the background field has no spatial dependence; independently verified | No change. |
| `F_φ=Q¹` "substantive, not trivially definitional" | **WEAKENED** — genuinely two independent physical statements (LHS from `T_m`, RHS from `T_φ`), but both rest on the same unexamined closure condition inherited from `FINDING_P55` | **Fixed.** Closure caveat added explicitly to this file's own Verdict and "does NOT establish" list. |
| "Fabricated unit mismatch" framing for the Fourier/real-space gap | **WEAKENED** — technically correct against literal substitution, but overprotective: `FINDING_P46`'s quasi-static PDE has a real-space form directly available, giving a genuinely reachable next step | **Fixed.** Reworded; the real-space integro-differential form now stated explicitly. |
| `FINDING_P50A`'s own continuity equation vs. this file's closure | **Real cross-finding drift, project-level** — `FINDING_P50A`'s `∇_μT_m=0` predates and is now inconsistent with P55/P56's `∇_μT_m=Q^ν` discovery; not flagged despite this file citing P50A for a neighboring term | **Flagged explicitly**, not fixed — re-scanning `FINDING_P50A` is a separate, not-yet-started task. |
| "Fully general velocity field" (KG-B2c) | **WEAKENED (wording)** — only `V_x` is populated; correct and sufficient for the x-Euler equation, but the phrase overstates scope | **Fixed.** Wording corrected. |

**True kill assessment:** no. The central Euler-equation result (`5H`
coefficient, `Q¹=ĝρ̄∂_xδφ/a²` source term) survives independent
re-derivation via two separate routes. What required correction was
scope/framing precision (four wording fixes) and one genuine,
consequential project-level gap (P50A drift) — real, but not a defect of
this file's own computation.

## Reproduction

```bash
python experiments/20260803-bridge/P56_matter_continuity_euler_assembly.py
```
