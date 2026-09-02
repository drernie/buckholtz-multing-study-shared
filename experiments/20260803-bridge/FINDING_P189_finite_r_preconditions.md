# FINDING P189 — `docs/153` §3a pre-conditions: REJECTED as originally framed

**Date:** 2026-09-02
**Status:** REJECT (of the original claim). The pre-conditions are now
**answered "not yet established / needs real derivation work"**, which
is itself a real, useful answer — the opposite of what
`CLAIM_P189_finite_r_preconditions.md` originally proposed.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR

---

## What happened, plainly

I proposed a shortcut: `docs/127`'s own closure formula,
`G_eff = G·lim_{r→∞}[f(r) - r·f'(r)]`, evaluated WITHOUT taking the
limit, would be a free finite-r analog — "no new derivation needed."
Positive and negative controls both passed (correctly reproduces
`docs/127`'s published `r→∞` values; correctly distinguishes tiers).
Numeric evaluation using v82's own real archive values then gave
absurd ratios (~1e37–1e75 relative to `G`), which I caught myself as a
units bug and did not use — but I still reported the *qualitative*
result ("nonzero at finite r, zero at `r→∞`") as if it were meaningful
evidence that the real finite-r calculation "has real content to
discover."

**A context-blind skeptic pass (Step 8a, given the claim + full code,
no reasoning chain) found this doesn't hold up**, on three points I
independently re-verified rather than took on trust:

1. **Category error on what "r" means.** `docs/127`'s `r→∞` limit is
   not a physical pair-separation going to infinity — in the
   Shtanov-Sahni formalism it is (per the derivation's own context) a
   homogenization/averaging-scale limit, tied to the *isotropic
   population* construction, not a single external pair. Reusing the
   *same symbol* `r` and the *same formula* for v82's actual physical
   node-pair separation (~40-45 Mpc) silently imports that
   population-averaging meaning into a single-pair calculation where it
   was never established to apply. This is exactly the "genuinely new
   derivation" pre-condition 1 asked whether we could avoid — and the
   honest answer is we cannot avoid it this way.

2. **The "nonzero at finite r" result is a tautology, not a finding.**
   `[VERIFIED-BASH]`: for *any* power-law `f(r)=c/r^n` (n≥1, c≠0),
   `f(r) - r·f'(r) = (n+1)c/r^n` — nonzero at every finite `r`, zero as
   `r→∞`, for every single power `n`, with no dependence on MULTING's
   specific tier structure at all. Presenting "the finite-r value is
   nonzero" as evidence that "the two regimes are not trivially the
   same" was circular: dropping a limit that was *constructed* to force
   zero cannot fail to be nonzero beforehand. This is not a physics
   result about MULTING or v82; it is a property of decaying functions
   in general.

3. **Pre-condition 2 was asserted, not verified within this artifact.**
   The script's `precondition_2()` is prose citing an earlier
   fact-finding pass (which DID read `two_charge_completion.py` and
   `two_field_action_closure.py` directly) — but the P189 script itself
   never imports or runs either file. Per this project's own standing
   discipline ("wherever checkable by running code, write and execute
   that check, don't just describe it" — the same rule this session's
   separate adversarial-verification-benchmark work spent all day
   testing on other people's reports), this is a real gap, not a
   nitpick.

The skeptic's overall verdict: **FALSIFIED / overclaims.** I re-derived
point 2 independently with `sympy` (confirmed above) before accepting
it, per `audit-verification-gate.md`'s rule that a skeptic's own
`[VERIFIED]` is my `[INFERRED]` until I check it myself. All three
points survive independent re-checking.

## Kill Analysis (per `falsification-ladder.md`)

**What is killed:**
- The claim that a finite-r analog of `docs/127`'s closure quantity
  falls out "for free" by removing one limit from an already-derived
  formula.
- Pre-condition 1's original answer ("YES, closed form exists
  trivially").
- The "qualitative result" offered for pre-condition 3 — it carried no
  actual information about MULTING/v82.

**What is NOT killed:**
- Pre-condition 2's underlying *factual* claim (that
  `two_charge_completion.py`/`two_field_action_closure.py` already do
  single-pair, finite-r symbolic work with no averaging) — established
  by direct source reading in the earlier fact-finding pass, not by the
  flawed P189 script. Worth re-confirming with a script that actually
  imports and exercises those files, not done here.
- `docs/127`'s own published `r→∞` result itself — untouched, still
  stands exactly as before.
- The real, sharper question this exercise surfaced: **before any
  finite-r calculation can mean anything, it needs its own derivation
  of what "the finite-r analog of `G_eff`" even means when the
  averaging/homogenization step is removed** — not a reuse of the
  existing asymptotic formula's algebra. That is a genuinely new,
  nontrivial derivation task, which is precisely what pre-condition 1
  asked whether we could avoid.

## Revised answers to `docs/153` §3a's 3 pre-conditions

1. **Does a finite-r closed form exist, or is new derivation needed?**
   **New derivation needed.** The r→∞ limit's algebra cannot be
   naively un-done; the physical meaning of "r" and the normalization
   of the tier constants both need to be re-established from the
   single-pair construction itself (most plausibly starting from
   `two_charge_completion.py`'s own already-finite-r kernel, not from
   `docs/127`'s population-limit formula).
2. **Tractable with existing machinery?** Likely yes, but not verified
   *in code* here — `two_charge_completion.py`/`two_field_action_closure.py`
   already operate single-pair/finite-r per direct source reading; a
   future attempt should build the finite-r closure calculation
   starting from these files' own kernel machinery, not from `docs/127`.
3. **Cost vs. consequence?** Materially higher cost than P189 assumed —
   this is real derivation work, not a numeric plug-in — so the
   proportionality question (`docs/153`'s own point) needs re-asking
   once a genuine finite-r derivation exists to estimate against, not
   before.

**Net effect on `docs/153`'s gate:** the 3 pre-conditions are **still
open**, now for a better-understood reason. This session's contribution
is negative-but-informative: it closes off a shortcut that looked
promising, and names specifically where the real work has to start
(the single-pair kernel machinery, not the population-limit formula).

## What this does NOT establish

1. Not a claim that bottleneck 1's finite-r/single-pair question is
   unanswerable — only that this specific shortcut attempt does not
   answer it.
2. Not a claim about `docs/127`'s own published result, which is
   completely unaffected.
3. Not authorization for, or progress on, the actual finite-r closure
   calculation — that remains a separate, bigger, not-yet-attempted
   task, exactly as `docs/153` already said.

## Artifacts

- `CLAIM_P189_finite_r_preconditions.md` — original claim (kept as
  written, not edited after the fact, per this project's no-silent-
  correction convention — this FINDING is the correction).
- `P189_finite_r_G_eff_preconditions.py` — the script; positive/negative
  controls both genuinely pass, but the CONCLUSION drawn from a passing
  control was itself wrong (the controls tested "is this algebra
  self-consistent," not "does this algebra mean what I claimed it
  means" — a distinction worth keeping in mind for future FL work in
  this project).

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
