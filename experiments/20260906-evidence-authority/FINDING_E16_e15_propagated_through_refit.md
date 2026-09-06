# FINDING E16 — propagating E15's correction through a re-fit turned out
# to be a closed-form identity, not a numerical result — and the skeptic
# downgraded the framing while finding a real, un-checked scope gap

**Date:** 2026-09-06
**Claim:** `CLAIM_E16_e15_propagated_through_refit.md` (pre-registered)
**Script:** `E16_e15_propagated_through_refit.py`
**Continues:** `FINDING_E15` (force-term corrections), `docs/157`'s named
next step. Step 8a skeptic dispatched with full pasted code (learning from
this project's own recorded failure mode — see global memory
`feedback_skeptic_dispatch_missing_code.md` — first dispatch attempt was
missing the code, correctly REFUSEd by the skeptic, re-dispatched with
everything inline).

## What was asked

`docs/157` named "propagate `E15`'s Jensen's-gap correction through an
actual re-fit of `(β1,β2)`" as the cheapest, most-differentiating open
item. `docs/157` itself speculated this would require genuine numerical
optimization.

## What was found — corrected twice, both times in place, never silently

**Self-correction #1 (before the skeptic, while interpreting the numbers):**
`docs/157`'s own speculation was wrong. `forces()` is linear in `β1`,`β2`
individually, so substituting population-averaged `F1,F2` is exactly a
reparametrization `(β1,β2)→(β1·CORR_F1, β2·CORR_F2)` — a bijection of `ℝ²`.
The chi2 **minimum is unchanged**; the "re-fit" result is a **closed-form
identity**: `β1_true = β1_TJB/1.1276`, `β2_true = β2_TJB/1.6164`
(`-11.3%`, `-38.1%`), shifting the fitted ratio `β2/β1` by `-30.2%` —
exactly `1/1.4335`, the same number `E15` already reported, now expressed
as a parameter-space statement instead of a force-term ratio.

**Self-correction #2 (also before the skeptic):** a planned second check
— whether `E8`'s own Hessian-slope machinery shows the `(β1,β2)` valley
direction shifting under the correction — turned out to be **the same
fact restated**, not independent evidence: in that function's own
normalised coordinates, `chi2_corrected` and `chi2_fixed_h0anchor` are
literally the same function, so the reported `30.24%` slope shift is
algebraically forced to equal the `-30.2%` ratio shift above.

**Step 8a skeptic verdict (full code pasted, per this project's own
recorded discipline against past skeptic-dispatch failures):**

| Point | Verdict | Detail |
|---|---|---|
| Algebraic identity holds | `CONFIRMED-REAL` | Traced every step of the real `forces→addot_over_a→H2_of_z→chi2_fixed_h0anchor` chain — nothing breaks the bijection argument (F0/F_accretion don't depend on β; `cumulative_trapezoid` and the `H2>0` mask are linear/bijection-preserving) |
| Slope-shift = ratio-shift, not independent | `CONFIRMED-REAL` | Verified the same algebra independently; flagged the earlier `PC2` control as **tautological** (tests the implementation, not the physics) — only `PC3` (the numerical optimizer converging via a route that doesn't know the closed form) is real independent confirmation |
| "Genuine third identifiability degeneracy" framing | `WEAKENED` | Correctly distinguished this from `(A,g,κ)`/`(β1,β2)`-valley: those are **flat-valley degeneracies** (one chi2, informationally irrecoverable); this is **two distinct chi2 functions** related by a *known* reparametrization, resolved the instant an external `σ` estimate exists (which `E13` already supplies) — a hidden-nuisance-parameter structure, not an information-theoretic degeneracy |
| Sign/reference/MCID gaming | `CONFIRMED-REAL` (none found) | Verified all 5 reported ratios arithmetically; explicitly praised the self-correction as anti-gaming, not overclaiming |

**A second, genuinely new finding from the skeptic, not previously noticed
in this session:** `E13`'s correction here only ever touches `F1,F2`. But
`F0 = -G·M²/d²` and `F_accretion` (`∝M`, `∝√M`) are **also** nonlinear
functions of `M(z)` — if `M(z)`'s own population scatter is real, `F0`
and `F_accretion` would carry their **own** Jensen corrections, which are
**not** absorbed by rescaling `β1,β2` (neither term depends on `β1,β2` at
all). This claim's scope is `F1,F2` only. `[WEAK]` marker applies until
this is checked.

## Result, corrected framing

Because `chi2` depends only on the product `β·(z-dependent term)`, and
`E13`'s correction is a fixed multiplicative constant, `chi2` cannot
distinguish "TJB's own `(β1,β2)` are point-evaluated" from "TJB's own
`(β1,β2)` are population-averaged, with the true coupling smaller by
`1/CORR_F1`, `1/CORR_F2`" — a **hidden-nuisance-parameter structure**,
resolvable the instant `σ` is known externally (which it already is, from
`E13`). Not an identifiability degeneracy of the `(A,g,κ)`/`(β1,β2)`-valley
kind.

## What this does and does NOT establish

**Does establish:** a closed-form, doubly-verified (algebra + independent
optimizer) answer to `docs/157`'s named question, correcting that
document's own prior speculation about needing numerical re-optimization.

**Does NOT establish:**
1. That population-averaging is the correct physical reading of v82's
   construction (`E15`'s Reading A vs B ambiguity is inherited, not
   resolved).
2. Anything about `F0`/`F_accretion`'s own possible Jensen corrections —
   open, flagged, not measured here (see Pearl Registry entry below).
3. `NO_AUTHOR_ERROR` — a direct answer to a question this project itself
   posed, not a claim about v82's correctness.

## Pearl Registry entry (Caveat Gate — a named, specific, untested alternative)

Per `falsification-ladder.md`'s Caveat Gate: the skeptic named a *specific*
untested construction (F0/F_accretion's own Jensen correction from M(z)
scatter), not a vague "more work needed." Logged in
`pearl_registry/INDEX.md`.

## Next step, named not done

Measure `M(z)`'s own population scatter (the analogue of `E13`'s
`M_gas|T` measurement, but for the mass-evolution law itself) and check
whether `F0`/`F_accretion`'s own correction factors are actually
negligible or not, before treating this claim's `F1,F2`-only scope as
settled.
