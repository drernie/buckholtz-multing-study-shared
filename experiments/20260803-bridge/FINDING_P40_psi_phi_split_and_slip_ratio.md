# P40 — φ's own energy density leaves Φ unmodified and shifts only Ψ: `Φ_φ=0` exactly, giving a real, nonzero slip ratio γ≠1 — and correcting an error in P38's own committed record

**Date:** 2026-08-14
**Status:** **Reviewed after context-blind skeptic review, same day — all
three core claims (`Φ_φ=0`, the correction to P38's record, `γ≠1`)
CONFIRMED-REAL.** The reviewer independently re-derived every step by
hand *and* found a second, structurally different route to the same
result (adding the `00` and spatial-trace Einstein equations, using
`T₀₀+T_kk=0` for any canonical static scalar) — showing `Φ_φ=0` is
actually a **general theorem** for this class of source, not specific to
this configuration as originally (over-cautiously) scoped. Four
framing-only fixes applied below (§0's error-cause claim corrected;
§4/§6's "kill signal" language tightened; a range-of-validity caveat
added to §3; §6 item 3 corrected to state the result's actual
generality). Full verdict in the new §7 below.
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
nonzero." Redone here mechanically, the result differs — confirmed twice
over (§7 below): once by this script's own ansatz-plus-solve, and again
independently by the skeptic reviewer via a *second, structurally
different route* (summing the `00` and spatial-trace Einstein equations
directly). **[CORRECTED per skeptic review]** ~~the undocumented
hand-check most likely used the standard textbook Poisson form
`∇²Ψ=4πG_N ρ`, not P38's own carefully-derived `G₀₀=2∇²Ψ` relation — a
factor-of-2 slip~~ — this specific mechanism claim does not hold up:
`∇²Ψ=4πG_N T₀₀` and `G₀₀=2∇²Ψ=8πG_N T₀₀` are algebraically the *same*
equation, so using one form instead of the other cannot by itself
introduce a factor of 2. The exact source of the original hand-check's
error cannot be reconstructed from the committed record (it was never
shown); what *is* established is that the hand-check's own result does
not survive mechanical re-derivation, confirmed independently twice.
**Declining the claim at the time was still the correct process move**
(an unverified claim should not have been adopted regardless of whether
it later turns out right) — but the declining hand-check's own result
does not survive mechanical re-derivation, and `FINDING_P38`'s own record
needs a correcting addendum (applied below, §5).

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
chain. **[Added per skeptic review]** This is a leading-order-in-`ĝ²`
expansion, valid in the far-field regime `r≫ĝ²M/(16π)`; near that scale
`Ψ_φ` becomes comparable to `Φ_N` and the perturbative truncation itself
breaks down (compounding the already-flagged `r→0` point-source
divergence, P38 §5 point 4).

## 4. What this establishes, precisely

Within P34–P38's own internal, `c=1`-relative, already-verified chain,
`φ`'s own energy density sources a metric slip that lands *entirely* in
`Ψ`, leaving `Φ` exactly unmodified at this order — a specific,
computed, non-trivial structural prediction, not merely "a slip exists"
(P37) or "the slip has this magnitude and sign" (P38). Combined, these
give a closed-form `γ=1−ĝ²M/(16πr)≠1` — a real, nonzero, static two-body
slip signature. **[Corrected per skeptic review]** ~~directly answering
(in the negative, i.e. NOT a null result) the campaign plan's own
originally-posed question for this stage~~ — this overstated the
connection: the plan's own kill signal is about the *quasi-static,
cosmological* `γ(a,k)`, not this static, two-body `γ(r)`. What this
finding actually shows is the **static-limit analog** of that question
— the same qualitative conclusion (not a null result) at the level this
construction has reached so far — with the actual cosmological reduction
still a separate, unattempted step (§6, item 2).

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
3. **A proof beyond `O(ĝ²)`, or for a non-canonical/non-static scalar.**
   **[Corrected per skeptic review — this point previously understated
   its own result.]** ~~this is the leading-order result for this specific
   static, point-source configuration only~~ — the reviewer identified a
   *general* mechanism behind `Φ_φ=0`: for any canonical, static, minimally-
   coupled scalar, `T₀₀+T_kk=0` identically (trace-reversal of the
   standard stress tensor), so summing the `00` and spatial-trace Einstein
   equations gives `∇²Φ_φ=0` identically, and standard boundary conditions
   (decay at infinity, regular for `r>0`) force `Φ_φ=0` uniquely — not
   specific to this particular point-source configuration. What remains
   genuinely unestablished is only *beyond* `O(ĝ²)`, or for a scalar with
   a non-canonical kinetic term or non-minimal coupling.
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

## 7. Skeptic verdict (context-blind, Step 8a, 2026-08-14)

Reviewed with this finding + script + `P38`'s own script and finding
(since this finding directly reuses P38's machinery and corrects P38's
own record), **no session history**, per Falsification Ladder Context
Asymmetry Rule. Given this finding claims to find an arithmetic error in
a previously-committed, already-corrected finding, the reviewer was
explicitly asked to treat that claim with extra scrutiny rather than
assume the newer, script-based calculation is automatically right. The
reviewer independently re-derived every step by hand and additionally
found a **second, structurally different route** to `Φ_φ=0` (summing the
`00` and spatial-trace Einstein equations, using `T₀₀+T_kk=0` for any
canonical static scalar) — genuinely independent verification, not a
restatement of this finding's own ansatz-and-solve.

| # | Issue | Verdict | Disposition |
|---|---|---|---|
| 1 | Is the reuse of P38's own linearized-tensor machinery faithful (no subtle sign/index change)? | CONFIRMED-REAL — character-for-character identical | No fix needed |
| 2 | Is `Ψ_φ=G_N ĝ²M²/(16πr²)` actually correct? | CONFIRMED-REAL — independent hand-derivation matches exactly | No fix needed |
| 3 | Is `Φ_φ=Ψ_φ+(Φ−Ψ)` the correct combination? | CONFIRMED-REAL — no sign trap, no missing piece | No fix needed |
| 4 | Is `Φ_φ=0` real or a symbolic coincidence? | CONFIRMED-REAL, and **stronger than claimed** — a general theorem for canonical static scalars (`T₀₀+T_kk=0`), confirmed by a second, independent route | Strengthened (§6 item 3) |
| 5 | Is the `FINDING_P38` correction accurately and fairly described? | CONFIRMED-REAL — addendum preserves history, correctly separates "hand-check was wrong" from "declining it was still correct" | No fix needed |
| 6 | Is the γ computation sound (convention, `Φ_N` base, `G_N` cancellation, convention-independence of `γ≠1`)? | CONFIRMED-REAL on all sub-points | No fix needed |
| 7 | "Factor-of-2 slip, generic Poisson form vs. `G₀₀=2∇²Ψ`" — is this mechanism claim correct? | WEAKENED — the two forms are algebraically equivalent, so this cannot be the actual mechanism | Fixed (§2): specific mechanism claim withdrawn, true cause left as unreconstructable from the record |
| 8 | "Directly answers the P36 kill signal" — fair, given this is static not cosmological? | WEAKENED — real overclaim in §4 (§6 already partly hedged it) | Fixed (§4): reframed as the "static-limit analog," cosmological reduction still separate |
| 9 | Missing range-of-validity caveat for `γ` | WEAKENED — real completeness gap | Fixed (§3): far-field validity + breakdown scale added |
| 10 | `Ψ_φ` ansatz uniqueness under the boundary conditions | Flag, standard, not a bug | Noted only, not a required fix |

**What survives:** all three core claims in full — `Φ_φ=0` exactly (now
established two independent ways, and shown to be a general result, not
a coincidence of this specific configuration); the correction to
`FINDING_P38`'s own record is accurate and fairly framed; `γ=1−ĝ²M/
(16πr)≠1` is correct under the standard PPN convention and
convention-independent in its conclusion. **What was corrected:** one
factual overclaim (the specific "factor-of-2" mechanism, which turned out
not to be algebraically possible), one scope overclaim (the P36
kill-signal connection), and one completeness gap (range of validity) —
plus one point of this finding's *own* excessive conservatism corrected
into a stronger, still-honest claim (`Φ_φ=0`'s actual generality). Kill
classification: none — all four fixes are framing/completeness, and one
of them strengthens rather than weakens the finding.

## Reproduction

```bash
python experiments/20260803-bridge/P40_psi_phi_split_and_slip_ratio.py
```
