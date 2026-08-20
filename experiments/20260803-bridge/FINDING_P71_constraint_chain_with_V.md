# FINDING P71 — the constraint propagation is exactly `λ`-independent, and the obstruction is *precisely* the `Ḣ` equation

**Status:** Skeptic-reviewed (Step 8a) and **substantially rebuilt**. Verdict
**WEAKENED** → the reviewer's central charge was correct, the computation I had
declined to do was run, and it produced a **sharper result than the claim it was
sent to check**.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P71_constraint_chain_with_V.py`

---

## The headline result

```
dC/dt |_{C=0}   =   −Ψ · [ Ḣ + 4πG(ρ_tot + p_tot) ]        EXACTLY
```

where `C := Ψ̇ + HΨ + 4πG·δq_tot` is `FINDING_P61`'s `0i` momentum constraint.

Two things follow, both computed:

1. **The propagated residual contains no `λ` at all.** Every `V`-carrying
   substitution cancels.
2. **The obstruction is *precisely* the `Ḣ` equation** — not a vague "background
   inconsistency". And `ρ_tot + p_tot = ρ_phys + φ̄̇²` is **`λ`-free**, because
   `V` enters `ρ` and `p` with **opposite signs** and only `ρ+p` appears.

Imposing the `Ḣ` equation gives residual **exactly 0** (positive control);
leaving it free gives `−ΨR_Ḣ`, nonzero (negative control).

---

## How this file changed under review

The first draft argued from covariant conservation that `V` cannot matter, and
**declined to run the constraint-propagation computation**, citing
convention-matching risk. The context-blind reviewer's central charge:

> *"the constraint is V-free" does not imply "the PROPAGATION of the constraint
> is V-free" — `dC/dt` substitutes `Ψ̈` via the ij-trace equation (sourced by
> `δp_φ`, which contains `−V′δφ`) and `δφ̈` via the perturbed KG (which contains
> `V″δφ`).*

**That channel is real.** Both substitutions do carry `V`. The reviewer was right
that the inference was a non sequitur as stated, and right that the Verdict's
*"established, not assumed"* directly contradicted the file's own
"NOT ESTABLISHED #1".

So I ran it (Part F). The channel is real **and it closes** — but that had to be
computed, not argued.

---

## Concern-by-concern

| # | Concern | Sev | Response |
|---|---|---|---|
| 1 | V-free constraint ≠ V-free *propagation*; the substitutions carry `V` | **HIGH** | **ACCEPTED and RESOLVED by computation.** Part F runs the full differentiate-and-substitute test. Residual is `λ`-free — asserted, not asserted-about. The reviewer's channel exists; it cancels. |
| 2 | Part A is symbol substitution, not derivation — `assert not has(Vp)` proves only "I subtracted `V′` from `V′`" | **HIGH** | **ACCEPTED.** Correct. Part A's `[VERIFIED-SYMPY]` marker was misleading and is removed; Part A is now labelled a *statement of a standard identity plus a consistency check on the pairing*, and the load is carried by Part F, which derives nothing from Part A. |
| 3 | The four controls test the substitution machinery, not structural cancellation | MED | **ACCEPTED, and Part F supersedes it.** Part F's cancellation is over the *full* propagated expression with `V′` and `V″` entering through independent channels, so it is not "hand-typed matching". |
| 4 | Verdict overstates what was computed; contradicts own NOT ESTABLISHED #1 | **HIGH** | **ACCEPTED — the specific wording was wrong.** With Part F run, the strong form is now earned; the contradiction is gone because the missing computation is no longer missing. |
| 5 | Three falsification tests specified, not run (no Bash) | — | **Test F1 run.** It is the one that mattered, and it is now Part F. |

**Pattern worth naming, third file running:** the reviewer's *process instinct*
was right even where their prediction was not. They expected the `V`-terms
*might* survive; they don't. But the demand to compute rather than argue produced
the exact identification of the obstruction — a result the argument alone could
never have reached.

---

## What is established

**Part A** *(narrowed)* — for a minimally coupled scalar,
`∇_μT_φ^{μν} = (□φ − V′)∂^νφ`. This is a **standard identity, stated here, not
derived in code.** Imposing the coupled KG leaves `−ĝρ_A∂^νφ`. A free negative
control confirms the cancellation is specific: flipping the field equation alone
(an inconsistent pairing, not an alternative convention) leaves `∂φ(−2V′+ĝρ_A)`.

**Part B** — both background sectors' continuity equations are identities given
their own equations of motion **with `V` present**, and the exchange terms cancel
exactly. Four negative controls fire (wrong `V′` coefficient, wrong Hubble drag,
wrong matter continuity, dropped exchange).

**Part C** — `V` enters `δρ_φ` and `δp_φ` **equally and oppositely** and is
**absent from `δq_φ`** (the potential sits in the `g^{μν}` bracket and
`g^{0i}=0`).

**Part F** — the headline, above.

---

## Self-caught bug

**Sign of the exchange term.** A first version set `Q = −ĝρ_Aφ̄̇`; the on-shell
residual came out `2ĝρ_Aφ̄̇` — *exactly double*, the signature of a flipped sign
rather than a missing term. By hand:
`ρ̇_φ + 3H(ρ_φ+p_φ) = φ̄̇(φ̄̈+V′+3Hφ̄̇) = +ĝρ_Aφ̄̇`, so the **scalar gains** and
matter loses. Documented inline.

---

## What this does NOT establish

1. **`μ(a,k)` or `γ`.** Still blocked. Part F shows the constraint closes *once
   the `Ḣ` equation is imposed* — it does not solve for `Ψ_k`.
2. **That `FINDING_P69`'s numeric background satisfies the `Ḣ` equation.** It
   should, having been built from the Friedmann constraint, but that is not
   checked here.
3. **Convention-independence.** Part F uses one standard Newtonian-gauge
   convention set. The `λ`-independence is robust (it is a statement about which
   symbols survive), but the *exact form* `−ΨR_Ḣ` is convention-dependent.
4. **Anisotropic stress.** `δp` here is the isotropic part; a scalar has none at
   first order, asserted from theory, not derived.
5. **That Part A's identity holds "in any metric"** — stated, not derived. Part F
   does not rely on it.
6. **Anything about MULTING itself** (Gate 1): `V` is *our* construction.

---

## Verdict

**`V` does not change what closure requires — now computed, not inferred.**

The propagated residual is exactly `λ`-free, and the obstruction is exactly the
`Ḣ` equation, which is itself `λ`-free because `V` cancels between `ρ` and `p`.

**This localises `FINDING_P61`'s D5 rather than merely reproducing it.** P61
found "not Bianchi-consistent on a free background" and hypothesised that the
whole background must be mutually self-consistent. Part F says *which* equation:
the free-background failure is **the `Ḣ` equation going unimposed**, and P61's
own Part I failed because imposing the 00-Friedmann alone does not supply `Ḣ`.

**`P70`'s open question is closed, in the negative.** `V` was the last untouched
ingredient. It neither helps nor hurts. The `Ψ_k` blocker is exactly as hard as
before `V` was restored — but it is now a *named* obstruction rather than a
diffuse one.
