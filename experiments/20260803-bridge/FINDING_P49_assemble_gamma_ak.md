# P49 — assembling P46+P47+P48: `Φ_k=Ψ_k` for every `k≠0`, so `γ(a,k)=1` at linear cosmological order for the canonical g-sector — pre-registered prediction confirmed, two gaps closed before assembling

**Date:** 2026-08-16
**Status:** Built, run, ruff clean, all assertions pass. **Skeptic review
(Step 8a): not yet run.**
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
**Regression check first:** `G₀₀^(1)` and `G₁₂^(1)` both reproduce
`FINDING_P48`'s own already-verified formulas exactly (script assertion) —
guards against silent drift between the two scripts before trusting the
new components.

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

**Structural argument, stated then checked:** any Lagrangian piece with no
explicit derivative-of-field-times-metric structure (the same rule that
gives a potential `V(φ)` its `T_μν=−g_μν V(φ)` contribution) contributes
`T_μν^(that term)=g_μν·f(φ,ρ)` — **proportional to `g_μν` by
construction**, regardless of the overall sign convention chosen for
`T_μν=∓(2/√-g)δS/δg^μν`. This alone already guarantees zero anisotropic
stress from any non-derivative interaction term.

**Checked, not left as the structural assertion alone:**

```
δT₀₀^(int) = ĝ(−ρ̄δφ−φ̄δρ)
δT₁₁^(int) = a²ĝ(ρ̄δφ+φ̄δρ)
δT₁₂^(int) = 0                    (all three off-diagonal — script assertion)
δT₁₁^(int) − δT₂₂^(int) = 0       (script assertion)
δT₂₂^(int) − δT₃₃^(int) = 0       (script assertion)
```

**Confirmed: all off-diagonal components zero, all diagonal spatial
components equal.** `δT_ij^(int)` is purely isotropic — zero anisotropic
stress from the interaction term, verified directly.

**Modeling choice, stated explicitly rather than presented as the only
possible reading:** the `−a³ρ` piece is treated as already captured by the
standard fluid ansatz (not re-derived via metric variation of the full
`−a³ρ(1−ĝφ)` term), consistent with `FINDING_P46`'s own "ρ as external
fixed function" treatment — an interpretive choice, not a uniquely forced
one.

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

**Verified by explicit case analysis, not asserted:** `sp.solve` on all
five coefficients simultaneously returns `k_x=k_y=k_z=0` as the **only**
solution. For every `k≠0`, at least one of the five conditions has a
nonzero coefficient, forcing `Φ_k=Ψ_k` — closing the "special direction"
gap a single-component check (`FINDING_P48`'s own `G₁₂`-only check) would
have left open.

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
   reading.
6. **Anything about the κ (dipole) sector** — monopole (`g`) sector only,
   matching every prior finding in this sub-arc.
7. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction,
   not a claim about TJB's own unpublished theory.

## Skeptic Verdict (Step 8a, context-blind — claim.md + code only, no session history)

**Not yet run.** To be completed before this finding is considered closed,
matching this campaign's standing discipline for every prior finding in
this sub-arc.

## Reproduction

```bash
python experiments/20260803-bridge/P49_assemble_gamma_ak.py
```
