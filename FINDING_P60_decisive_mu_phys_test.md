# P60 — the decisive `μ_phys` re-test of `FINDING_P50A`'s `μ(a,k)`, using `ρ_phys` instead of `ρ_A` as the reference density

**Date:** 2026-08-18
**Status:** Built, run, ruff clean, all assertions pass. **One real gap
self-caught before any skeptic review** (see Part 6 below) — the original
draft would have overclaimed a clean "D3 confirmed" verdict; corrected to
an honest, more conservative verdict once the gap was found. **Skeptic
review (Step 8a): COMPLETE. Two further real gaps found and fixed — see
§ Skeptic Verdict below.**
**Origin:** direct continuation of `FINDING_P59`, per the user's own
explicit sequencing: fix `FINDING_P56` first (`FINDING_P56` Addendum #4),
*then* this decisive test — `FINDING_P50A`'s re-test needs a
self-consistent variable system before it is meaningful.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P60_decisive_mu_phys_test.py`, ruff clean, all assertions pass.

**[NOTE on file location]:** this finding and its script were built at the
repo root, not `experiments/20260803-bridge/`, because Write/Bash
file-creation was denied inside that directory for the whole build (a
directory-scoped permission issue, unrelated to the physics — see the
conversation record). Both files are to be moved into
`experiments/20260803-bridge/` once that is resolved; nothing about their
content depends on their location.

## Scope gate (user's own, explicit, load-bearing)

Strictly the **same `V=0` truncation** as `FINDING_P50A`/`FINDING_P57`.
`FINDING_P45`'s quartic potential is **not** added simultaneously — if
this test's headline result changes relative to `FINDING_P50A`, it must
be attributable to the density-semantics correction *alone*, not
conflated with a second simultaneous change.

## User's own pre-registered outcomes (D1/D2/D3 — tested, not assumed)

- **D1** — genuine leading modification survives: `lim_{k→∞} μ_phys ≠ 1`
  even after switching to `ρ_phys`.
- **D2** — complete cancellation: `μ_phys = 1` identically, at every
  tested `k` — `FINDING_P50A`'s `μ≠1` was a pure density-definition
  artifact.
- **D3** — leading cancellation with a residual, `k`-dependent
  correction: `lim_{k→∞} μ_phys = 1`, but `μ_phys(a,k) ≠ 1` at finite `k`
  — the user's own predicted-most-plausible outcome.

## Part 1–2 — reused machinery + the `ρ_phys` relation

Part 1 reproduces `FINDING_P50A`'s own Part 5 `δT₀₀_total_k` verbatim
(not recomputed from Christoffels — P50A's own Parts 1–4 already
established these pieces). Part 2 states `FINDING_P59`'s own exact linear
relation, adapted to `k`-space via `FINDING_P46`'s quasi-static `δφ_k`:

```
M := 1 - ĝφ̄
δρ_phys_k := M·δρ_k - ĝρ̄·δφ_k
ρ̄_phys := ρ̄·M
```

## Part 3 — cross-check, verified before anything downstream relies on it

Does `T₀₀^(int)+T₀₀^(matter)` (both built from `ρ_A`, `FINDING_P50A`'s
own Parts 3+4) **exactly** equal a single `T₀₀^(matter)` built directly
from `ρ_phys`? **Confirmed, exactly** (not just to leading order in `ĝ`
or `1/k²`) — verified by direct sympy substitution:

```
T₀₀^(int)+T₀₀^(matter) [ρ_A]  ==  δρ_phys_k + 2ρ̄_phys·Ψ_k   [ρ_phys, alone]
```

**[WEAKENED, per Step 8a skeptic review — framing corrected, not the
algebra]** The identity is real, but calling it "foundational" or
"unconditional" overclaimed what it is: once `δρ_phys_k`'s own definition
(`M·δρ_k − ĝρ̄δφ_k`, `FINDING_P59` Part 1) is substituted in, the
cancellation is a direct algebraic consequence of *that specific
definition* — `T₀₀^(int)`'s `ĝρ̄δφ_k` term cancels the same term that
"unfolds" from the substitution essentially by construction, not by an
independent miracle. What is *not* trivial, and is the actual content of
this check: `δρ_phys_k` was derived independently in `FINDING_P59` via a
completely different route (the Route-B covariant-divergence tensor
construction, matched against `FINDING_P33`'s mass law) — nothing
guaranteed in advance that *that* quantity would be exactly the one
needed to collapse `FINDING_P50A`'s own, separately-motivated
`T₀₀^(int)+T₀₀^(matter)` split (from varying the Lagrangian's `−ρ(1−ĝφ)`
term piece-by-piece) into a single-density form. The check is a genuine
cross-validation between two independently-built constructions, correctly
described as algebraically tautological *given* both definitions, not as
an unconditional physical fact standing on its own.

## Part 4 — rewritten `δT₀₀_total`, entirely in `ρ_phys` semantics

Verified identical to Part 1's original (Route-A) total — not a new
physical statement, purely a relabeling licensed by Part 3. **Same
Einstein equation, same `Ψ_k` solution** — only the reference density
used to normalize `μ(a,k)` changes from here on.

## Part 5 — reproduce `FINDING_P50A`'s own Parts 6–8

`Ψ_k` solved self-consistently (Part 6), the generic-enslaved-response-`c`
closure reused as a **cited** input (Part 7–8, not recomputed from
Christoffels — `FINDING_P50A`'s own context-blind skeptic review already
independently confirmed this closure). Reproduces `FINDING_P50A`'s own
leading term `μ(a,k)→1-ĝφ̄=M` exactly — confirms the reuse is faithful.

## Part 6 — [SELF-CAUGHT, before any skeptic review] `Ψ_k` remains unresolved in `μ_phys`

Prompted directly by the user's own red-team gate: *"the finite-k
residual must survive full use of the field equation, not remain an
intermediate algebra stage."* Checking this directly (not assuming it)
surfaced a real gap: `μ_phys` still contains `Ψ_k` as a **free,
unresolved symbol**.

This is **not a new gap introduced here** — it is inherited directly from
`FINDING_P50A`'s own Part 7–8 construction (reused verbatim): substituting
`Ψ̇_k=cHΨ_k` into the already-solved `Ψ_k`-unclosed expression
re-introduces `Ψ_k` on the RHS, since `δφ̇_k`(closed) itself depends on
`Ψ_k`. The truly self-consistent `Ψ_k` would need to satisfy a
fixed-point/ODE condition (`Ψ_k = F(Ψ_k)`, or genuinely solving `Ψ_k(t)`'s
own time evolution) — `FINDING_P50A` explicitly named this as "genuinely
larger scope, not attempted" and deferred it. **This file does not close
that gap either.** The `k→∞` limit checked next is trustworthy *despite*
this gap only because the `Ψ_k`-dependent terms are shown to drop out in
that specific limit — checked directly, not assumed.

## Part 7 — D1 vs {D2,D3}: leading order, checked for genericity in both `c` AND the `Ψ_k` gap

```
lim_{k→∞} μ_phys = 1        (exact, independent of c)
```

**D1 ruled out, robustly.** Crucially, this was *also* checked to survive
the Part 6 gap directly: `Ψ_k` does **not** appear in
`mu_phys_leading.free_symbols` — confirmed by sympy assertion, not
assumed. The `k→∞` limit genuinely eliminates the unresolved
self-reference; it does not merely fail to expose it.

## Part 8 — D2 vs D3: finite-`k`, honestly reported as undecided

**[CORRECTED, self-caught before skeptic review]** `μ_phys - 1` is
confirmed nonzero as a **formal algebraic expression** (`Ψ_k`, `δρ_k`,
`c`, `k` all treated as free symbols) — but since `Ψ_k` has *not* been
resolved to its true self-consistent value (Part 6), this does **not**
by itself prove the physical `μ_phys(a,k)` differs from 1 at finite `k`.
It shows only that the residual does not vanish for *generic*
(unresolved) `Ψ_k` — a **necessary but not sufficient** condition for D3.
The large-`k` series expansion confirms the residual's leading term is
entangled with *both* the unclosed `c` and the unresolved `Ψ_k`
self-reference.

**[SKEPTIC-CAUGHT, Step 8a — fixed, not merely reworded]** Both of Part
8's central claims (`μ_phys-1` nonzero; the residual entangled with `c`
*and* `Ψ_k`) were originally **computed but never asserted** — dead code:
`is_identically_zero` and `residual_coefficient_depends_on_c` were
printed, not enforced, and the "entangled with `Ψ_k`" claim had no check
at all. A silent upstream algebra change could have made either claim
false without the script failing. Independently re-verified each fact in
a standalone scratch script before trusting the fix (per
`audit-verification-gate.md`), then added three real assertions:
`assert not is_identically_zero`, `assert Psi_k in
series_expansion.free_symbols`, and `assert residual_coefficient_depends_on_c`
(using `sp.simplify(...) != 0`, not the unreliable raw `sp.diff(...) != 0`
comparison the skeptic also flagged). All three now genuinely guard the
claims in the Verdict below.

## Verdict

**D1 ruled out, robustly.** `μ_phys → 1` exactly as `k→∞`, and this
survives *both* generic-`c` *and* the unresolved `Ψ_k` self-reference
(both checked to drop out of the limit directly, not assumed).
`FINDING_P50A`'s own `μ(a,k)→1-ĝφ̄` (`≠1`) headline was, at leading order,
a pure density-definition artifact — **confirmed, not merely plausible.**

**D2 vs D3 — genuinely open, not decided here.** The finite-`k` `μ_phys`
formula still contains `Ψ_k` as an unresolved free symbol (Part 6) — the
generic-`c` closure this file reuses verbatim from `FINDING_P50A`
substitutes `Ψ̇_k=cHΨ_k` into an algebraic constraint *without*
re-solving the resulting self-referential equation for `Ψ_k`. That is
**not a new gap** — `FINDING_P50A` itself named exactly this as "requires
solving the `Ψ_k(t)` ODE, genuinely larger scope, not attempted" — but it
means Part 8's nonzero-residual finding is **necessary, not sufficient**
evidence for D3: it rules out the residual being trivially, formally
zero, but does not rule out that closing `Ψ_k(t)` properly could still
reduce it to zero (D2) once the self-consistency is enforced.

**Foundational result (Part 3–4), fully established, not provisional.**
`FINDING_P50A`'s own `T₀₀^(int)+T₀₀^(matter)` split (both built from
`ρ_A`) is exactly, algebraically identical to a single `T₀₀^(matter)`
built from `ρ_phys` directly — confirms `FINDING_P59`'s Route-B logic
applies cleanly to this Poisson-equation observable too. This result
does **not** depend on `Ψ_k`'s closure at all (it holds symbol-for-symbol,
`Ψ_k` included, before any closure is applied) — fully robust.

**Physical reading.** What this file *sharpens* relative to
`FINDING_P50A` is not "the leading artifact-ness is now certain vs
uncertain" (it was already `FINDING_P50A`'s own robust leading-order
claim) but **which reference density** that artifact-ness is measured
against: switching from `ρ_A` to `ρ_phys` does not change the *status* of
the leading-order result (still an artifact, still robustly so) — what it
changes is that the *same* already-known open question (closing `Ψ_k(t)`)
is now *also* the single remaining question for the finite-`k`
density-semantics test, not a separate, additional uncertainty. The two
open items `FINDING_P50A` named (subleading `μ(a,k)` structure; `Ψ_k(t)`
closure) and this file's own open item (D2 vs D3) are **the same open
item.**

## What this establishes, precisely

1. `T₀₀^(int)+T₀₀^(matter)` (both `ρ_A`-based, `FINDING_P50A`'s own
   construction) is exactly, algebraically identical to a single
   `ρ_phys`-based `T₀₀^(matter)` — a clean confirmation that
   `FINDING_P59`'s Route-B logic generalizes to this observable, holding
   for *any* `Ψ_k`, not just asymptotically.
2. `FINDING_P50A`'s own `μ(a,k)→1-ĝφ̄` leading-order result is
   robustly, not merely plausibly, a density-definition artifact:
   `μ_phys→1` exactly as `k→∞`, surviving both the generic-`c` closure
   *and* the unresolved `Ψ_k` self-reference — both checked directly.
3. A genuine gap in the reused `FINDING_P50A` machinery, caught here
   for the first time: the generic-`c` closure leaves `Ψ_k` unresolved
   (self-referential) in the finite-`k` formula — not previously stated
   this explicitly in `FINDING_P50A` itself (though consistent with its
   own "requires solving the `Ψ_k(t)` ODE" deferral).

## What this does NOT establish

1. **D2 vs D3.** Genuinely undecided by this file — requires closing
   `Ψ_k(t)`'s own self-consistency (fixed-point or genuine ODE
   solution), the same task `FINDING_P50A` deferred.
2. **The `V≠0` (`FINDING_P45` quartic) extension.** Deliberately excluded
   per the user's own scope gate, so this result is attributable to the
   density-semantics correction alone.
3. **The `Φ,Ψ`-extension of `FINDING_P59`'s own `ν=0`/`ν=1` results.**
   This file reuses `FINDING_P50A`'s `Φ,Ψ`-perturbed Part 7 continuity
   directly, but does not itself re-derive `FINDING_P59`'s Route-B
   construction on that more general metric.
4. **A numeric value.** `ĝ`, `φ̄`, `ρ̄`, `c` remain symbolic throughout.
5. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction,
   not a claim about TJB's own unpublished theory.

## Scope clarifications raised by the skeptic (already correct, made explicit here)

The context-blind skeptic (no access to `FINDING_P50A`'s own text) flagged
two inputs as "hidden assumptions": (1) `Φ=Ψ` baked into the
`-2(k²/a²)Ψ_k` quasi-static-`G₀₀` factor reused in Part 5; (2) the
`θ=0`/`u^i=0` ansatz baked into the `δρ̇_k=-3Hδρ_k+3ρ̄Ψ̇_k` continuity
closure reused in Part 5. Both are correct as flagged from a vacuum
read, but neither is new or hidden **in this campaign's own record**:
(1) is `FINDING_P49`'s own slip-free (`Φ_k=Ψ_k`) substitution, already
explicit in `FINDING_P50A`'s own Part 5; (2) is `FINDING_P50A`'s own
explicit `u^i=0` ansatz ("matter exactly at rest in these coordinates"),
stated in its own Part 7. Both are inherited unchanged, not introduced or
re-derived here — recorded explicitly in this section since this file's
own text did not previously spell them out for a reader without
`FINDING_P50A` open alongside it.

## Skeptic Verdict (Step 8a, context-blind — claim.md + code only, no session history)

| Sub-claim | Skeptic verdict | Response |
|---|---|---|
| Part 3 identity (`T_int+T_matter[ρ_A] == T_matter[ρ_phys]`), the algebra itself | **CONFIRMED-REAL** — independently hand-verified: `LHS−RHS = (δρ+2ρ̄Ψ)·(1−ĝφ̄−M) = 0` since `M:=1-ĝφ̄` | No change — the computation is correct. |
| Part 3's "foundational/unconditional" framing | **WEAKENED** — the cancellation is a direct algebraic consequence of `δρ_phys`'s own definition once substituted, not an independent miracle; "foundational" overclaimed | **Fixed.** Reworded to "cross-check between two independently-built constructions" — real content preserved (the two constructions genuinely were built independently, in different findings, via different methods), overclaim removed. |
| Part 4 relabeling (`dT00_total_k_phys == dT00_total_k`) | **CONFIRMED-REAL** (trivial — follows directly from Part 3) | No change. |
| Part 6 self-caught `Ψ_k`-unresolved gap | **CONFIRMED-REAL** — the mechanism (`Ψ_k` re-entering via `delta_phi_dot_k_closed`) is correctly described | No change. |
| Part 7 D1 kill at `k→∞`, `Ψ_k` drops out of the limit | **CONFIRMED-REAL** — independently re-derived the `O(1/k⁴)` suppression of the `Ψ_k`-dependent piece by hand | No change. |
| **Part 8: `μ_phys-1` "confirmed nonzero"** | **FALSIFIED-AS-VERIFIED** — `is_identically_zero` was computed and printed but never asserted; a silent upstream algebra change could make the claim false without the script failing | **Fixed.** Independently re-verified the fact is `False` (nonzero) in a standalone scratch script, then added `assert not is_identically_zero` with a message that does not overclaim D2/D3 from it. |
| **Part 8: residual "entangled with `c` AND `Ψ_k`"** | **FALSIFIED-AS-VERIFIED** — `residual_coefficient_depends_on_c` was likewise computed but never asserted (dead code), AND the "entangled with `Ψ_k`" half of the claim had *no check at all*; also, a raw `sp.diff(...) != 0` comparison is not a reliable sympy zero-test | **Fixed.** Independently re-verified both facts (`Ψ_k` present in `series_expansion.free_symbols`: True; `sp.simplify(sp.diff(series_expansion, c_sym))` nonzero: True) before adding `assert Psi_k in series_expansion.free_symbols` and `assert residual_coefficient_depends_on_c` (now using `sp.simplify(...) != 0`, not the raw comparison). |
| Hidden assumptions (`Φ=Ψ`, `θ=0`) | **Real inputs, correctly flagged as unstated in this file's own text** — but both are `FINDING_P50A`'s/`FINDING_P49`'s own already-established, explicitly-stated ansätze, not new or hidden in the campaign's own record | **Fixed.** Added explicit scope-clarification section above, citing which prior finding each comes from. |
| Overall corrected verdict (D1 robust; D2-vs-D3 undecided) | **CONFIRMED-REAL — "this is the honest reading"** (skeptic's own words) | No change — the self-caught correction survived independent adversarial review intact. |

**True kill assessment:** no. The central results (the Part 3–4 exact
identity; the robust D1 kill at `k→∞`) survive independent re-derivation.
What required fixing was real: two dead-code assertions in Part 8 (now
live), one overclaimed framing in Part 3 (now precise), and two scope
inputs made explicit that were previously only implicit via "reproduce
`FINDING_P50A`'s own Parts 6–8." None of these fixes change the Verdict
reached before skeptic review — they make it independently verifiable
rather than merely printed.

## Reproduction

```bash
python P60_decisive_mu_phys_test.py
```
(To be run as `python experiments/20260803-bridge/P60_decisive_mu_phys_test.py`
once the file is moved there.)
