# P41 — Bean & Tangmatitham's own `R` slip parameter is `1/γ`, not `γ`: closing P31's flagged gap, correcting a notation-inversion trap before it could propagate

**Date:** 2026-08-14
**Status:** **Reviewed after context-blind skeptic review, same day.**
The review's own tool sandbox lacked WebFetch access — it could not
perform the single most important check it identified (independent
primary-source re-verification), correctly reported this as a substrate
limitation rather than guessing, and returned `[PARTIALLY-REVIEWED]`
rather than a verdict. Per `falsification-ladder.md`'s own Substrate
Gate discipline, a tool-access limitation is a finding about the
review's infrastructure, not about this claim — so the required
follow-up was done directly (I have WebFetch, the review agent did not):
a *second*, independently-worded WebFetch against the same primary
source, requesting maximally literal quotes. **All three flagged quotes
confirmed exactly** (§1, unchanged). Two of the review's other points
were real and are fixed below: §5 point 1 was too optimistic about what
resolving P39 would unlock (§7), and the script's own algebra had no
external check at all (§7, a sanity check added, honestly scoped —
*not* claimed as independent verification of the ψ/φ direction, which
the primary-source re-fetch already settled). Full verdict in §7 below.
**Origin:** eighth step of the covariant-completion campaign
(`PLAN_final_goal_20260814.md`), continuing at the deliberately slower,
one-step-at-a-time pace per explicit user instruction ("продолжай P41,
медленно"). Neither of the two "big" available next steps (the
campaign plan's own quasi-static cosmological reduction, flagged in the
plan itself as expensive; or resolving P39's SI-units gap, which
requires reopening prior findings) fits a single careful step. A
smaller, well-motivated, and already-flagged gap does:
`FINDING_P31`'s own §4 point 2 explicitly noted that Bean & Tangmatitham's
`R` parameter — the literature's own slip/anisotropy parameter, cited
for their `Q` but never itself verified — "is not independently
re-derived." This step closes exactly that gap.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P41_R_slip_parameter_literature_correspondence.py`, ruff
clean, all assertions pass.

## 0. Honest scope

This is a **literature-correspondence and notation-translation
registration**, not new physics — the same category as P39's
symbol-provenance audit. It verifies, by direct WebFetch of the primary
source (not memory, not paraphrase), what Bean & Tangmatitham's own `R`
parameter actually means and how their metric convention relates to
this project's own, then checks algebraically whether their `R`
corresponds to this project's own `γ` (P40) — and finds it does **not**,
directly: it is `γ`'s reciprocal.

**What this does NOT do:** attempt any numeric comparison to their
reported `R∈[0.99,1.02]` bound. That comparison is blocked by the same
`ĝ`-has-no-established-SI-value gap `FINDING_P39` already identified —
inherited here, not newly introduced. This finding is a correctness/
translation step, not a bound-check.

## 1. Verified source quotes (direct WebFetch, `arxiv.org/html/1002.4197`)

**Metric convention (their eq. 1):**

> "ds² = −a(τ)²[1+2ψ(x,t)]dτ² + a(τ)²[1−2ϕ(x,t)]dx²"

`ψ` multiplies the time-time term, `ϕ` multiplies the spatial term —
**exactly** this project's own P38 convention
(`ds²=-(1+2Φ)dt²+(1-2Ψ)dx²`). This was checked directly, not assumed:
their `ψ` corresponds to this project's `Φ`; their `ϕ` corresponds to
this project's `Ψ`.

**Slip relation (their eq. 7, no-anisotropic-stress limit):**

> `ψ = Rϕ` (i.e. `R := ψ/ϕ`), described as allowing "an inequality
> between the two gravitational potentials, even at late times when
> anisotropic shear stresses are negligible."

**Reported bound (their Table 1, time-/scale-independent case, 95% CL, all data):**

> `R∈[0.99,1.02]`

**[Added per skeptic review]** All three quotes above were **independently
re-confirmed** with a second, differently-worded WebFetch query against
the same primary source, specifically checking: (a) the LHS/RHS
direction of `R`'s defining equation (confirmed literally: `"ψ−Rϕ=..."`,
not the reversed `"ϕ−Rψ=..."`); (b) that Table 1's `R` column is the
*same* `R` as eq. 7, not an overloaded reuse of the letter (e.g. the
unrelated CMB shift parameter, also commonly denoted `R` in this
literature) — confirmed via the table's own caption, "1D marginalized
95% confidence limits for modified gravity parameters `Q` and `R`..."
naming the same pair; (c) the exact sign convention in eq. 1. All three
matched the original fetch exactly, closing the specific gap the
skeptic review flagged as unverifiable with its own tool access.

## 2. Translating `R` into this project's own notation — and the inversion trap

Using the verified metric correspondence (§1), their `R:=ψ/ϕ` becomes,
in this project's own `Φ,Ψ` labels:

```
R = Φ/Ψ
```

This project's own `γ` (P40, skeptic-confirmed standard PPN convention,
`γ:=Ψ/Φ`) is the *inverse* structure:

```
R − 1/γ = 0     (script assertion, exact)
```

**`R=1/γ`, not `R=γ`.** This is a genuine, easy-to-miss notation
inversion between two legitimate but different literature conventions —
PPN's own `γ:=Ψ/Φ` versus Bean & Tangmatitham's own `R:=ψ/ϕ=Φ/Ψ` in this
project's labels. Verified algebraically here, not assumed; getting this
backwards would have silently inverted every downstream qualitative
statement about which direction of deviation from 1 this reconstruction
predicts.

## 3. This project's own reconstruction's predicted `R`

Substituting P40's own `γ=1−ĝ²M/(16πr)`:

```
R = 1/γ = 16πr/(16πr − ĝ²M)
R, leading order in ĝ² = 1 + ĝ²M/(16πr)
```

`R>1` at leading order (script assertion) — the *opposite* side of 1
from `γ`'s own `<1` result, but this is the **same physics, correctly
translated**, not a contradiction: `γ<1` and `1/γ>1` are the same
statement about the same slip.

## 4. What this establishes, precisely

Closes `FINDING_P31`'s own explicitly-flagged gap (§4 point 2: "whether
`φ` in eq. 6 is the Newtonian potential... if the latter, the
growth-relevant effective coupling could involve `Q` combined with `R`")
by directly verifying `R`'s own defining equation and metric convention,
rather than leaving it as an unresolved aside. Establishes the *correct*
translation between this project's own `γ` (P40) and the literature's
own `R` — `R=1/γ`, confirmed algebraically — a real, non-trivial
correspondence, not a trivial relabeling.

## 5. What this does NOT establish

1. **Any numeric comparison to their `R∈[0.99,1.02]` bound.** `ĝ` here is
   `FINDING_P39`'s still-unresolved symbol; this project's own predicted
   `R` cannot yet be assigned a real SI value. **[Corrected per skeptic
   review — this point understated the size of the gap.]** ~~Inherited
   blocker, not a new one~~ — resolving P39's SI-units gap alone would
   *not* by itself make this comparison meaningful. `R∈[0.99,1.02]` is a
   *cosmological* bound (constant across the scales/redshifts a specific
   large-scale-structure dataset probes); this project's own `R` is a
   *static, two-body* PPN quantity. Treating the two as directly
   comparable, even with SI units in hand, requires an additional,
   unestablished assumption — that this reconstruction's slip is
   universal across environment and scale, not merely constant in time.
   Two blockers stack here, not one.
2. **Whether their `R` bound, even once P39's gap is resolved, actually
   applies to MULTING's own mechanism.** `FINDING_P31` §4 point 8 already
   flagged that Bean & Tangmatitham's own likelihood is calibrated to a
   scenario where growth and lensing move *together* — the same
   mechanism-frame caveat applies here, inherited unchanged, not
   re-examined in this finding.
3. **Anything about `Q` or `FINDING_P31`'s own `ΔG` mapping** — entirely
   about `R` and the slip sector; `Q`'s own mapping is untouched.
4. **The quasi-static, cosmological `k`-dependence of `R(a,k)`** — only
   the static, two-body limit (P40's own scope) is translated here.
5. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction
   and a published external paper's own equations — not a claim about
   TJB's own unpublished theory.

## 7. Skeptic verdict (context-blind, Step 8a, 2026-08-14)

Reviewed with this finding + script, **no session history**, per
Falsification Ladder Context Asymmetry Rule. **This review's own tool
sandbox did not include WebFetch**, so it could not perform primary-source
re-verification — it correctly identified this as its own limiting
factor rather than guessing, and returned a `[PARTIALLY-REVIEWED]`
status rather than a clean or failing verdict. Per
`falsification-ladder.md`'s Substrate Gate ("a `BLOCKED-INFRASTRUCTURE`
verdict must never be recorded as evidence against the claim"), this is
a finding about the review's own infrastructure, not about this
finding's correctness — the flagged gap was closed directly afterward
(§1 addendum: a second, independently-worded WebFetch against the same
source, all three quotes reconfirmed exactly).

| # | Issue | Verdict | Disposition |
|---|---|---|---|
| 1 | Direction of `R`'s definition (`ψ/ϕ` vs `ϕ/ψ`) — the single most load-bearing check | HYPOTHESIS (tool-blocked) → **CONFIRMED-REAL** on independent re-fetch | Closed (§1 addendum): literal `"ψ−Rϕ=..."` reconfirmed a second way |
| 2 | Is Table 1's `R` the same `R` as eq. 7, or an overloaded reuse (e.g. the CMB shift parameter)? | HYPOTHESIS (tool-blocked) → **CONFIRMED-REAL** | Closed (§1 addendum): table caption explicitly names the same `(Q,R)` pair |
| 3 | Metric sign convention (eq. 1) — real risk given multiple conventions exist in the literature | HYPOTHESIS (tool-blocked) → **CONFIRMED-REAL** | Closed (§1 addendum): exact signs reconfirmed |
| 4 | Internal algebra `R=Φ/Ψ`, `γ=Ψ/Φ` ⟹ `R=1/γ`, given the premises | CONFIRMED-REAL — trivial, correctly flagged as such | No fix needed |
| 5 | Is `γ:=Ψ/Φ` (cited from P40) a genuine standard PPN convention, not an inherited error? | CONFIRMED-REAL — independently re-derived from the PPN metric form, consistent | No fix needed |
| 6 | Cosmological `R` bound vs. static PPN `γ` — does §5 adequately block a false "once P39 is fixed, compare directly" impression? | WEAKENED — real, under-scoped | Fixed (§5 point 1): now names the second, independent blocker (universality-across-scale assumption) |
| 7 | Script's algebra is a tautology given its own premises — no external check at all | WEAKENING — real methodological gap | Fixed: added an honestly-scoped sanity check (Brans-Dicke `γ`), explicitly *not* claimed as verifying the ψ/ϕ direction (that's the primary-source re-fetch's job) |

**What survives:** the core claim in full — `R=1/γ`, with the specific
primary-source basis now verified two independent ways (not one), and
the translation's own algebra correctly scoped as trivial-given-true-
premises rather than overclaimed as itself doing verification work.
**What was corrected:** one real scope gap (the cosmological-vs-static
distinction needed a second, explicit blocker, not folded into P39's
alone) and one methodological gap (an external sanity check added, and
honestly labeled for what it does and does not establish — an earlier
draft of that same check briefly overclaimed independence before being
caught and corrected in the same edit). Kill classification: none — all
fixes are framing/completeness, and the load-bearing factual claim was
strengthened by an independent second verification, not merely defended.

## Reproduction

```bash
python experiments/20260803-bridge/P41_R_slip_parameter_literature_correspondence.py
```
