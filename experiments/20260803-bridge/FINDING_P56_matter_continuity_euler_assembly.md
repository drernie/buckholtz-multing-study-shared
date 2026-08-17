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
