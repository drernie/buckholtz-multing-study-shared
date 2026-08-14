# P40 — φ's own energy density leaves Φ unmodified and shifts only Ψ: `Φ_φ=0` exactly, giving a real, nonzero slip ratio γ≠1 — and correcting an error in P38's own committed record

**Date:** 2026-08-14
**Status:** Built, run, ruff clean, all assertions pass.
**Pending context-blind skeptic review (Step 8a) — not yet run.**
**Origin:** seventh step of the covariant-completion campaign
(`PLAN_final_goal_20260814.md`), continuing at the deliberately slower,
one-step-at-a-time pace per explicit user instruction ("продолжай P40,
медленно"). P39 showed the planned P22/P31 numeric (SI-unit) comparison
is currently blocked, so this step takes the *other* available next item
from the campaign plan's own table — the "P36" row's `γ`/kill-signal
question — staying entirely within the `c=1`-relative, already
internally-verified P37/P38 chain, deliberately not touching P39's
still-open SI-units question.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P40_psi_phi_split_and_slip_ratio.py`, ruff clean, all
assertions pass.

## 0. Honest scope, and why this step exists

During the P38 correction, the context-blind skeptic reviewer suggested
(as a secondary, bonus point, not its core criticism) that pairing P38's
own `Φ−Ψ` result with a solve of the `00`-sector equation might show
`Φ_φ=0` exactly. That was explicitly **declined** at the time — per
`audit-verification-gate.md`'s standard ("Agent's `[VERIFIED]` is your
`[INFERRED]`"), applied evenly to a reviewer's *suggestions*, not just
its criticisms — with the recorded reason: *"an independent hand-check
during correction found this specific claim does NOT hold exactly
(`Φ_φ` came out nonzero)."*

**That hand-check was never itself verified, has no script, and shows no
work in the committed record.** This step redoes the calculation
properly — mechanically, with sympy, reusing P38's own already-verified
machinery — specifically to check whether that declining hand-check was
actually right. **It was not.** Section 2 below reports the discrepancy
and its most likely cause honestly.

**What this does NOT do:** it does not touch P39's still-open SI-units
question (P38–P40's own `c=1`-relative internal chain remains valid on
its own terms, exactly as P39's own skeptic review confirmed); it does
not produce an SI-valued, observationally comparable number for `γ` —
only a symbolic, internally-consistent expression.

## 1. Method — solving the `00`-sector, reusing already-verified pieces

Three already-established, unchanged building blocks:

1. **P38's own linearized-Einstein-tensor machinery** (`linearized_christoffels`,
   `linearized_ricci`, `linearized_einstein_tensor`) — re-stated identically
   in this script (standalone scripts in this project don't cross-import),
   not re-derived.
2. **P38's own `G₀₀=2∇²Ψ` relation** — re-derived here first as a *positive
   control*, confirming this script's copy of the machinery is identical to
   P38's already-skeptic-confirmed version before using it to solve
   anything new.
3. **P37's own established `T₀₀=(1/2)(∂φ)²`**, for the same field
   `φ(r)=ĝM/(4πr)` P35/P37/P38 all reuse unchanged.

Solving `G₀₀=8πG_N T₀₀`, i.e. `2∇²Ψ=8πG_N T₀₀`, with the same
ansatz-plus-`sympy.solve`-plus-independent-verification pattern P38 used
for `Φ−Ψ`:

```
Ψ_φ = G_N·ĝ²·M² / (16π·r²)
```

Independently verified by substituting the solved coefficient back into
the *full* equation at a generic point (script assertion, exact zero
residual) — the same discipline P38 applied to its own result.

## 2. Combining with P38's own `Φ−Ψ` — resolving the discrepancy

```
Φ_φ = Ψ_φ + (Φ−Ψ) = G_N·ĝ²M²/(16πr²) + [−G_N·ĝ²M²/(16πr²)] = 0
```

**`Φ_φ = 0` exactly** (script assertion). This is the *same* combination
the P38 skeptic suggested and this project *declined* at the time.

**Correcting the record:** `FINDING_P38`'s own text states it declined
this because "an independent hand-check ... found `Φ_φ` came out
nonzero." Redone here mechanically, the result differs. The most likely
explanation, based on directly comparing the two calculations: the
undocumented hand-check most likely used the standard textbook Poisson
form `∇²Ψ=4πG_N ρ`, **not** P38's own carefully-*derived*
`G₀₀=2∇²Ψ` relation (confirmed as the positive control in §1 above) — a
factor-of-2 slip, exactly the class of error this project's own
`audit-verification-gate.md` discipline exists to catch. **Declining the
claim at the time was still the correct process move** (an unverified
claim should not have been adopted regardless of whether it later turns
out right) — but the declining hand-check's own result does not survive
mechanical re-derivation, and `FINDING_P38`'s own record needs a
correcting addendum (applied below, §5).

## 3. The slip ratio γ

Assembling the full leading-order potentials, using the standard,
unmodified Newtonian base `Φ_N=−G_N M/r` (per P34's own flag that `S_EH`
is standard, unmodified) plus each potential's own `O(ĝ²)` correction:

```
Ψ = Φ_N + Ψ_φ = −G_N M/r + G_N ĝ²M²/(16πr²)
Φ = Φ_N + Φ_φ = −G_N M/r + 0 = Φ_N     (unmodified — Φ_φ=0)

γ := Ψ/Φ = 1 − ĝ²M/(16πr)
```

**`γ≠1`** (script assertion) — this is the campaign plan's own
(`PLAN_final_goal_20260814.md`, "P36" table row) explicitly-named kill
signal, checked directly: *"if quasi-static `μ,γ` come out **exactly**
`Q=1,R=1`... document and stop this branch, do not force a distinguishing
claim."* That null result does **not** occur here — a real, nonzero,
`O(ĝ²)` slip signature survives. Note `G_N` cancels exactly out of
`γ−1` (both `Ψ_φ` and `Φ_N` carry one power of `G_N`) — a clean,
`G_N`-independent symbolic result within this construction's own internal
chain.

## 4. What this establishes, precisely

Within P34–P38's own internal, `c=1`-relative, already-verified chain,
`φ`'s own energy density sources a metric slip that lands *entirely* in
`Ψ`, leaving `Φ` exactly unmodified at this order — a specific,
computed, non-trivial structural prediction, not merely "a slip exists"
(P37) or "the slip has this magnitude and sign" (P38). Combined, these
give a closed-form `γ=1−ĝ²M/(16πr)≠1`, directly answering (in the
negative, i.e. NOT a null result) the campaign plan's own originally-posed
question for this stage.

## 5. Correction applied to `FINDING_P38`'s own record

Per this section's own finding, `FINDING_P38_metric_slip_from_phi_
anisotropic_stress.md` §6 (Skeptic Verdict table, item 6c) and its
associated prose are corrected with a clearly-marked addendum pointing
here, preserving the original historical record (what was believed and
why, at the time) rather than silently rewriting it — matching this
project's own established pattern (e.g. `FINDING_P34`'s addendum pointing
to `FINDING_P35`).

## 6. What this does NOT establish

1. **An SI-valued, observationally comparable `γ`.** `ĝ` here is P39's
   still-unresolved symbol — this `γ` formula is valid *within* the
   internal `c=1`-relative chain, exactly as P39's own skeptic review
   confirmed is a distinct property from SI-consistency; no numeric
   comparison to any real observational `γ`/slip bound is made or
   possible yet.
2. **Anything about `μ(a,k)` or `Σ(a,k)`** — only `γ` (via the static,
   two-body `Ψ/Φ` ratio) is computed here; the campaign plan's own
   quasi-static, cosmological-perturbation reduction of this static
   result is not attempted.
3. **A general proof that `Φ_φ=0` for any source, or at any order beyond
   `O(ĝ²)`** — this is the leading-order result for this specific static,
   point-source configuration only.
4. **Resolution of P39's dimensional-consistency gap** — deliberately not
   touched; this step's own `γ` inherits that gap's consequences (it
   cannot yet be assigned real SI units) without attempting to resolve it.
5. **That the earlier, declined hand-check was a failure of process** —
   declining an unverified claim was the correct move regardless of
   whether it later proves right or wrong; what's corrected here is the
   *hand-check's own arithmetic*, not the decision to require independent
   verification before adopting it.
6. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction,
   not a claim about TJB's own unpublished theory.

## Reproduction

```bash
python experiments/20260803-bridge/P40_psi_phi_split_and_slip_ratio.py
```
