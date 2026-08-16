# P49 — assembling P46+P47+P48: `Φ_k=Ψ_k` for every `k≠0`, so `γ(a,k)=1` at linear cosmological order for the canonical g-sector — pre-registered prediction confirmed, two gaps closed before assembling

**Date:** 2026-08-16
**Status:** Built, run, ruff clean, all assertions pass. **Corrected same
day after context-blind skeptic review — zero load-bearing errors found
(the core `Φ_k=Ψ_k`/`γ=1` result survives entirely), but real rigor/framing
gaps closed with real computation: a brute-force independent check added
alongside `sp.solve` (whose completeness on an arbitrary polynomial system
isn't guaranteed by API contract); Part 2's code honestly relabeled as
verifying the coded ansatz's self-consistency rather than an independent
re-derivation of the underlying GR identity; a missing `δg_μν` cross-term
in `T_μν^(int)` named explicitly (does not affect the conclusion); a
fluid-action-vs-scalar-density modeling ambiguity, gauge-dependence, and
scalar-sector-only scope all added as explicit caveats.**
**Skeptic review (Step 8a): COMPLETE. See § Skeptic Verdict below.**
**Origin:** the explicit culmination step the whole `P46→P47→P48` sub-arc
was built toward (`FINDING_P46`/`FINDING_P47`/`FINDING_P48` each explicitly
deferred this exact combination). User proposed this step with a
pre-registered prediction (`γ_linear=1`) stated before any calculation —
matching FL/EstimandOps' AOG-1 pre-registration discipline.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P49_assemble_gamma_ak.py`, ruff clean, all assertions pass.

## 0. Pre-registered prediction (stated before this script computed anything)

> `γ_linear(a,k) = 1` for the canonical g-sector, at linear cosmological
> perturbation order, in the quasi-static subhorizon regime.
> Falsified if the trace-free Einstein equation forces `Φ_k≠Ψ_k` for any
> `k≠0` once every source of anisotropic stress is actually assembled.

Secondary, explicitly **not** addressed by this finding (registered by the
user as future-relevant, not as something P49 must compute): `μ(a,k)≠1`
may hold even with `γ=1` — no-slip does not imply no modified growth.

## 1. Two gaps closed before assembling, not skipped

Simply re-using P46+P47+P48 verbatim would have left two real gaps open,
named before writing any code:

**Gap 1 — the interaction term's own `T_μν`.** `FINDING_P47` linearized
only `φ`'s *bare kinetic* stress tensor
(`T_μν=∂_μφ∂_νφ−½g_μν(∂φ)²`). `FINDING_P46`'s own Lagrangian has a
**second** `φ`-dependent piece — the interaction term
`+a³ρĝφ` (from expanding `P46`'s matter term `−a³ρ(1−ĝφ)`). This piece's
own contribution to `T_μν` was never checked. Checked explicitly in Part 2
of the script — not assumed isotropic by analogy with the bare kinetic
piece.

**Gap 2 — only one of five traceless components checked.** `FINDING_P48`
verified the trace-free Einstein tensor's structure using **only**
`G₁₂`. A symmetric traceless 3×3 tensor has **five** independent
components. Checking one does not by itself establish `Φ_k=Ψ_k` for every
Fourier mode — a mode purely along the `z`-axis (`k_x=k_y=0`) gives **zero**
constraint from `G₁₂` alone (`k_x·k_y=0` regardless of `Φ_k−Ψ_k`). Closed
by computing the remaining four independent components
(`G₁₃`, `G₂₃`, `G₁₁−G₂₂`, `G₂₂−G₃₃`) — free to compute, reusing the exact
same Ricci tensor `FINDING_P48`'s own method already built, no new heavy
symbolic work.

## Part 1 — full traceless tensor structure, five components

Rebuilt `FINDING_P48`'s exact-metric + eps-linearization machinery
(self-contained, not imported — matching this campaign's convention).
**Cross-check first, against expected closed-form textbook results
(Ma & Bertschinger-type conformal-Newtonian forms), not against P48's own
computed numbers directly:** `G₀₀^(1)` and `G₁₂^(1)` both reproduce the
expected textbook forms exactly (script assertion) — since the
Christoffel/Ricci pipeline is independently re-run in this script, this is
really a check that the algorithm `FINDING_P48` also independently
implemented produces the same textbook answer when rebuilt here, and, as a
byproduct, matches `FINDING_P48`'s own results — guards against silent
drift/copy error before trusting the new components.

```
G₁₃^(1)      = −∂_x∂_z(Φ−Ψ)
G₂₃^(1)      = −∂_y∂_z(Φ−Ψ)
G₁₁^(1)−G₂₂^(1) = −(∂_x²−∂_y²)(Φ−Ψ)
G₂₂^(1)−G₃₃^(1) = −(∂_y²−∂_z²)(Φ−Ψ)
```

All four match the expected `−(∂_i∂_j−⅓δ_ij∇²)(Φ−Ψ)` structure exactly
(script assertions). Combined with `FINDING_P48`'s own `G₁₂`, **all five**
independent traceless components confirmed to share the single common
structure — **computed**, not assumed from the metric ansatz's rotational
symmetry alone.

## Part 2 — `T_μν^(int)`, checked not assumed isotropic

`FINDING_P46`'s Lagrangian: `L=a³·½φ̇²−a·½(∇φ)²−a³ρ(1−ĝφ)`. Expanding
the matter term: `−a³ρ(1−ĝφ)=−a³ρ+a³ρĝφ`. The `−a³ρ` piece is the
standard matter action already captured by the external perfect-fluid
ansatz `T^(matter)_μν=diag(ρ,0,0,0)` (`FINDING_P46`'s own explicit
treatment of `ρ` as a fixed external function). Only the **new**
interaction piece, `+a³ρĝφ=√-g·(ρĝφ)`, needs its own `T_μν` — a genuine
`g_μν`-dependent term in the total action distinct from the bare fluid
piece.

**Structural argument, cited not derived fresh:** any Lagrangian piece with
no explicit derivative-of-field-times-metric structure (the same rule that
gives a potential `V(φ)` its `T_μν=−g_μν V(φ)` contribution) contributes
`T_μν^(that term)=g_μν·f(φ,ρ)` — **proportional to `g_μν` by
construction**, regardless of the overall sign convention chosen for
`T_μν=∓(2/√-g)δS/δg^μν`. This is a standard, citable GR identity
(`δ√-g=−½√-g g_μν δg^μν`), not re-derived from a symbolic functional
variation in this script.

**[CORRECTED after skeptic review]** The original text called the code
below a check of this identity "not left as the structural assertion
alone." The skeptic caught this precisely: `T_int(μ,ν)` is coded as
`g_bg[μ,ν]·ĝ·ρ·φ` — **literally proportional to `g_bg[μ,ν]` by
construction** — so asserting the off-diagonal components vanish is
checking `0·(stuff)=0`, not independently re-deriving the
`g_μν`-proportionality claim. **Fixed** — relabeled honestly: the code
verifies the *coded ansatz's* internal self-consistency (that it correctly
implements isotropy given its construction), not a from-scratch
re-derivation of the identity itself, which rests on the cited standard GR
identity above (same status as how `FINDING_P48` cites, rather than
re-derives, the standard cosmological Poisson equation).

```
δT₀₀^(int) = ĝ(−ρ̄δφ−φ̄δρ)
δT₁₁^(int) = a²ĝ(ρ̄δφ+φ̄δρ)
δT₁₂^(int) = 0                    (all three off-diagonal — script assertion)
δT₁₁^(int) − δT₂₂^(int) = 0       (script assertion)
δT₂₂^(int) − δT₃₃^(int) = 0       (script assertion)
```

**Confirmed (of the coded ansatz's self-consistency): all off-diagonal
components zero, all diagonal spatial components equal.** `δT_ij^(int)` as
coded is purely isotropic.

**[CORRECTED after skeptic review, added] Missing term, stated explicitly:**
this computation used the **background** metric `ḡ_μν` only. `T_int` is
explicitly `g_μν`-proportional, so a full treatment would also include a
`δg_μν·ĝρ̄φ̄` cross-term — dropped here, matching `FINDING_P47`'s own
identical convention for the analogous `−½g_μν(∂φ)²` piece of its own
`T_μν` (`P47` also never combined metric perturbations with its own
`g_μν`-proportional term, consistent with this whole sub-arc's `P46`–`P48`
split of "matter/scalar perturbations" from "metric perturbations").
**Does not affect the `Φ_k=Ψ_k` conclusion:** the dropped term is
proportional to `δg_μν` itself, which for this metric ansatz
(`h₀₀=−2Φ`, `h_ii=−2Ψa²δ_ij`) is already purely diagonal/isotropic —
including it would still give zero anisotropic stress. **It does mean**
Part 5's `δT₀₀^(int)` formula below is incomplete by a further
`+ĝρ̄φ̄·(−2Φ)` term, on top of the already-flagged `δρ_k`-dynamics gap —
Part 5 already declines to claim `Ψ_k` is closed, so this does not change
that section's conclusion.

**[CORRECTED after skeptic review] Modeling choice, now with the
alternative named explicitly:** the `−a³ρ` piece is treated as already
captured by the standard fluid ansatz (not re-derived via metric variation
of the full `−a³ρ(1−ĝφ)` term), consistent with `FINDING_P46`'s own "ρ as
external fixed function" treatment — an interpretive choice, not a
uniquely forced one. The skeptic named the concrete alternative: the
standard dust convention `T_μν=ρu_μu_ν` (from a fluid action with a
4-velocity) is a different, more standard derivation route, and if the
interaction term inherited this structure instead
(`T^(int)_μν=ĝφρ u_μu_ν`), it would **also** give zero anisotropic stress
(`u_μu_ν` is `diag(1,0,0,0)` in the fluid rest frame — isotropic, same as
`g_μν`'s spatial part). **`γ=1` is unaffected either way** — but the
`T_int` split used here is not the unique variationally-consistent choice,
only a convenient one that happens to agree with the fluid-action route on
the one property (isotropy) this finding actually needs.

## Part 3 — total anisotropic stress, and the resulting slip condition

```
δT_ij|TF (total) = δT_ij|TF^(φ, P47)      = 0
                  + δT_ij|TF^(int, Part 2) = 0
                  + δT_ij|TF^(matter)      = 0
                                            -----
                                            = 0
```

The matter term is the **standard pressureless-dust assumption** (zero
anisotropic stress at linear order), already flagged as inherited — not
independently re-derived — in `FINDING_P47`'s own "What this does NOT
establish" §3. Unchanged here, stated explicitly rather than silently
reused.

Einstein's equation, trace-free part: `δG_ij|TF=8πG_N·δT_ij|TF=0`, for
**all five** independent components (Part 1). In Fourier space
(`∂_i→ik_i`), each condition becomes a polynomial in `(k_x,k_y,k_z)` times
`(Φ_k−Ψ_k)`:

```
G₁₂,k    = k_xk_y(Φ_k−Ψ_k)         = 0
G₁₃,k    = k_xk_z(Φ_k−Ψ_k)         = 0
G₂₃,k    = k_yk_z(Φ_k−Ψ_k)         = 0
(G₁₁−G₂₂)_k = (k_x²−k_y²)(Φ_k−Ψ_k) = 0
(G₂₂−G₃₃)_k = (k_y²−k_z²)(Φ_k−Ψ_k) = 0
```

`sp.solve` on all five coefficients simultaneously returns
`k_x=k_y=k_z=0` as the only solution.

**[CORRECTED after skeptic review]** The skeptic flagged that a single
`sp.solve` call is not by itself a rigorous proof — `sp.solve`'s
completeness on an arbitrary polynomial system is not guaranteed by API
contract (and an `assert` on its output could in principle pass vacuously
if the solver returned an empty or under-constrained result, though it did
not in this run). **Fixed with real computation, not softened language:**
added an independent brute-force enumeration over a dense half-integer
grid (`[-3,3]³`, 2743 candidate points), checking all five coefficients
directly with no solver involved — **zero counterexamples found**,
confirmed independently before accepting. This also matches the manual
algebraic proof: `k_x²=k_y²=k_z²` (from the three difference-conditions)
together with "at most one of `k_x,k_y,k_z` nonzero" (from the three
product-conditions) forces all three to zero. For every `k≠0`, at least
one of the five conditions has a nonzero coefficient, forcing `Φ_k=Ψ_k` —
closing the "special direction" gap a single-component check
(`FINDING_P48`'s own `G₁₂`-only check) would have left open.

## Part 4 — verdict: `γ(a,k)`

```
Φ_k = Ψ_k   for every k≠0
γ(a,k) := Ψ_k/Φ_k = 1   identically, for every k≠0
```

**Pre-registered prediction: `γ_linear(a,k)=1`. Result: MATCH.**

**Standard-physics framing, stated explicitly to avoid overclaiming
novelty:** this is the well-known "no slip for a minimally-coupled
canonical scalar (quintessence-type), including its non-derivative matter
coupling" result from cosmological perturbation theory — **not a
MULTING-specific discovery.** This finding's actual value: it confirms
this reconstruction's g-sector, once covariantized through the full
`P46→P49` chain (including the interaction term and the full traceless
tensor structure, both gaps this finding closed rather than inherited
silently), reproduces this standard property rather than accidentally
introducing new anisotropic stress — a consistency result, matching
`FINDING_P47`'s own precedent for how to correctly frame this class of
result.

**[CORRECTED after skeptic review, added] Three scope caveats:**

1. **Fluid-action ambiguity** (see Part 2's correction above) — both
   plausible derivation routes for the interaction term give zero
   anisotropic stress, so `γ=1` is unaffected, but the specific route used
   here is not the unique variationally-consistent choice.
2. **Gauge dependence.** `Φ`, `Ψ` are gauge-dependent quantities in
   conformal-Newtonian/longitudinal gauge (implicitly used throughout,
   matching `FINDING_P38`/`P40`/`P46`–`P48`'s own convention). The
   gauge-**invariant** content of this result is "zero anisotropic
   stress" — `Φ_k=Ψ_k` is the standard way this is stated in this
   specific gauge, not itself a gauge-invariant statement.
3. **Scalar sector only.** No vector or tensor perturbation modes are
   analyzed here or anywhere in the `P46`–`P49` sub-arc — `γ=1` is a
   scalar-sector statement only.

## Part 5 — bonus: `Ψ_k` itself, closed only under a stated assumption

`δT₀₀`(total)`=δT₀₀^(φ)+δT₀₀^(int)+δT₀₀^(matter)`, with
`δT₀₀^(φ)=φ̄̇δφ̇` (`P47`), `δT₀₀^(int)=ĝ(−ρ̄δφ−φ̄δρ)` (Part 2 above),
`δT₀₀^(matter)=δρ` (standard). `FINDING_P46`'s own field equation gives
`δφ_k=ĝa²δρ_k/k²`, but `δφ̇_k` (needed for `δT₀₀^(φ)`) requires
`δρ_k(t)`'s functional form — which `FINDING_P46` explicitly left
undetermined ("`δρ` has no dynamical equation imposed",
`FINDING_P46` Part 3). **A real, already-flagged gap, not newly
discovered here.**

Closing `Ψ_k` fully needs either (a) a continuity equation for `δρ_k`
(not attempted, out of scope) or (b) the standard leading-order
approximation that `δT₀₀^(φ)`/`δT₀₀^(int)` are subdominant to
`δT₀₀^(matter)=δρ`, recovering `FINDING_P48`'s own already-established
`Ψ_k=−4πG_N a²δρ_k/k²`. **Not claimed as a new, independent derivation of
`Ψ_k`** — an explicit re-use of `P48`'s own result under a stated
subdominance assumption, distinct from the `Φ_k=Ψ_k` result (Parts 3–4),
which needed **no** such assumption.

## What this establishes, precisely

1. `Φ_k=Ψ_k` for every Fourier mode `k≠0`, hence `γ(a,k)=1` identically at
   linear cosmological perturbation order for the canonical g-sector —
   established using **no quasi-static approximation** (the trace-free
   equation needed none, per `FINDING_P48`'s own already-strengthened
   result) and **no new free assumption** beyond the standard
   pressureless-dust ansatz already flagged in `FINDING_P47`.
2. This matches the pre-registered prediction exactly — a clean example of
   AOG-1 pre-registration discipline (the prediction was stated before any
   assembly, not fitted to the result afterward).
3. Two real gaps (interaction-term `T_μν`; only one of five traceless
   components) were identified and closed before assembling, not silently
   inherited from `P46`–`P48`.

## What this does NOT establish

1. **`Ψ_k` or `Φ_k` individually, as a new independent result.** Part 5's
   `Ψ_k` is a re-use of `FINDING_P48`'s own Poisson-equation result under
   an explicitly stated subdominance assumption — not re-derived fresh
   here.
2. **`μ(a,k)`.** Not attempted — explicitly named by the user as a further,
   separate step; `γ=1` does not imply `μ=1`.
3. **A numeric value.** `FINDING_P39`'s SI-units gap for `ĝ` still blocks
   any numeric comparison to `FINDING_P31`'s ceiling — deliberately
   unaddressed here, matching every prior finding in this sub-arc.
4. **That matter (dust) genuinely has zero anisotropic stress.** Inherited
   from the standard ΛCDM linear-perturbation-theory assumption, not
   independently derived from a fluid action in this reconstruction.
5. **That the `−a³ρ`/interaction-term split in Part 2 is the only valid
   modeling choice.** Stated explicitly as an interpretive choice
   consistent with `FINDING_P46`'s own treatment, not a uniquely forced
   reading — the standard fluid-action alternative (`T_μν=ρu_μu_ν`) gives
   the same isotropy conclusion but is not identical to the route used
   here.
6. **A gauge-invariant statement.** `Φ_k=Ψ_k` is stated in
   conformal-Newtonian gauge; the gauge-invariant content is "zero
   anisotropic stress."
7. **Anything about vector or tensor perturbation modes** — scalar sector
   only, throughout the entire `P46`–`P49` sub-arc.
8. **That `T_μν^(int)`'s code (Part 2) independently re-derives the
   `g_μν`-proportionality identity from a symbolic functional variation of
   the action.** It verifies the coded ansatz's self-consistency given
   that identity, which is cited as standard, not re-derived fresh.
9. **The `δg_μν·ĝρ̄φ̄` cross-term's exact value.** Named as missing, shown
   not to affect the `Φ_k=Ψ_k` conclusion, but not computed.
10. **Anything about the κ (dipole) sector** — monopole (`g`) sector only,
    matching every prior finding in this sub-arc.
11. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction,
    not a claim about TJB's own unpublished theory.

## Skeptic Verdict (Step 8a, context-blind — claim.md + code only, no session history)

| Sub-claim | Skeptic verdict | Response |
|---|---|---|
| Only `k=0` satisfies all five traceless polynomial equations simultaneously over ℝ | **CONFIRMED** — manual case analysis independently verified watertight | No change to the math; robustness of the *check* addressed below. |
| `sp.solve` alone as rigorous proof of the above | **WEAKENED** — completeness on an arbitrary polynomial system not guaranteed by API contract; an `assert` on its output could in principle pass vacuously | **Fixed with real computation** — independent brute-force enumeration added (2743 candidate points, half-integer grid `[-3,3]³`), zero counterexamples, independently re-verified before accepting. |
| `T_μν^(int) ∝ g_μν` by construction (structural argument) | **CONFIRMED** — the verbal argument is sound (standard GR identity) | No change. |
| Code Part 2 independently verifies isotropy rather than assuming it | **FALSIFIED** (of the code-independence claim only, not the physics) — `T_int(μ,ν)=g_bg[μ,ν]·(scalars)` hardcodes the isotropic structure; asserting off-diagonal components vanish checks `0=0` | **Fixed** — relabeled honestly: the code verifies the coded ansatz's self-consistency, not an independent re-derivation; the identity itself is cited as standard, not re-derived. |
| Code captures ALL of `δT_μν^(int)` | **WEAKENED** — a `δg_μν·ĝρ̄φ̄` cross-term is missing (background metric used throughout) | **Fixed** — named explicitly, shown not to affect `Φ_k=Ψ_k` (the dropped term is itself `∝δg_μν`, already isotropic for this ansatz), but flagged as making Part 5's `δT₀₀^(int)` further incomplete. |
| `−a³ρ`/interaction-term split is the unique modeling choice | **WEAKENED** — the standard fluid-action route (`T_μν=ρu_μu_ν`) is a different, more standard derivation giving the same isotropy conclusion | **Fixed** — alternative named explicitly, `γ=1` shown unaffected either way. |
| `Φ_k=Ψ_k` for every `k≠0` | **CONFIRMED**, conditional on the stated assumptions (pressureless dust, scalar sector, this gauge) | No change to the conclusion. |
| `γ(a,k)=1` at linear order, quasi-static subhorizon regime, scalar sector | **CONFIRMED within scope** — scope caveats (gauge, scalar-sector-only) should be stated more explicitly | **Fixed** — added as explicit caveats in Part 4. |
| Standard-physics framing (not novel) | **CONFIRMED** — matches Ma & Bertschinger 1995 / coupled-quintessence literature (Amendola 2000, Wetterich) | No change. |
| Not under-claimed — the interaction doesn't deserve more credit as a "nontrivial extension" | **CONFIRMED** — the interaction is non-derivative, cannot introduce anisotropic stress on structural/dimensional grounds | No change. |
| Part 5's `Ψ_k` treatment appropriately scoped | **CONFIRMED** — neither overclaims nor is unnecessarily hedged | No change (compounded slightly by the now-named `δg_μν` gap, already noted there). |
| Regression checks (`G₀₀`, `G₁₂` vs P48) catch bugs in the new code | **WEAKENED** — wording implied "vs P48's output"; the check is actually against hardcoded textbook forms, independently re-implementing P48's algorithm | **Fixed** — wording corrected in Part 1. |

**Overall verdict, in the skeptic's own words: "NOT a true kill... None of
these are load-bearing to the `γ=1` conclusion."** Every issue found was a
rigor/framing gap, not a computational error in the core result — matching
this campaign's established pattern (P46–P48 each had the same shape of
correction). All fixes applied with real computation (the brute-force
check) or honest relabeling (Part 2, the regression-check wording),
consistent with this session's standing discipline of not just softening
language.

## Reproduction

```bash
python experiments/20260803-bridge/P49_assemble_gamma_ak.py
```
