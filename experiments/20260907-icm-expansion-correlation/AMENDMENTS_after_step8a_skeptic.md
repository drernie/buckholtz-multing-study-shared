# AMENDMENTS — Step 8a skeptic pass, all repairs applied

**Date:** 2026-09-07
**Applies to:** `FINDING_stage1_*`, `FINDING_stage3_*`, `FINDING_stage3b_*`,
`FINDING_stage3c_*`, `FINDING_stage4_*` and their scripts.
**Labels:** `NOT_VALIDATION` · `NOT_REFUTATION` · `OUR_RECONSTRUCTION` ·
`NO_AUTHOR_ERROR`

A context-blind Step 8a skeptic was run on this branch (claim + verbatim
source only, no session history, no reasoning chain). **Its own Bash was
disabled**, so every verdict it returned was analytic or read-based —
`BLOCKED-INFRASTRUCTURE` on its side, which per FL is never evidence
against a claim, and here turned out to be a strength: forced onto closed
forms, it caught things a grid cannot see.

**Per `audit-verification-gate.md`, its `[VERIFIED]` was treated as my
`[INFERRED]`. Every finding below was independently re-run by me before
being accepted.** Its hand-arithmetic matched machine output to 4–5
significant figures in every case checked.

**No claim was killed.** Seven repairs, all applied in place with the
original wording quoted rather than deleted.

---

## The seven repairs

### FIX 1 — `q_discriminant`'s "iff Q < 1" was unconditional `[FALSIFIED → FIXED]`

**Old:** *"Sign is POSITIVE iff Q < 1."*
**Wrong for `b1 < 0`, undefined for `b1 = 0`.** The exact statement is

```
d(addot/a)/dk = [4G R/(c² d⁴)] · ( b1 − b2 k R/(M c² d) )
⇒ sign = sign( b1 − b2 k R/(M c² d) ),  NOT sign(1 − Q)
```

**Verified counterexample**, `z=0`, `b1 = −1.4335×10¹⁰`:

| | skeptic (by hand) | me (tool) |
|---|---|---|
| `Q` | −2.0593 | **−2.0594** (`< 1` ⇒ old wording predicts `+`) |
| total | −1.4216e-90 | **−1.4215e-90** ⇒ actual `−` |

`b1 = 0` → `ZeroDivisionError`, confirmed.

**Applied:** condition added, plus a new `sign_of_response()` valid for any
`b1`. `stage1`'s own NC1 was saved only by calling
`d_addot_dk_analytic` rather than `q_discriminant`.

### FIX 2 — "more thermal energy ⇒ less local expansion" `[WITHDRAWN]`

The most serious finding. `∂(ä/a)/∂k` has units **s⁻²·J⁻¹** — the response
of **acceleration**. "Less local expansion" is about **H**, s⁻¹. The
inference needs integration over history and initial conditions; it does
not follow pointwise.

`stage3b` lines 13-16 call this exact operation **"a CATEGORY ERROR"** for
a different pair of quantities. The same move was made here in the
opposite direction, in the same experiment, on the same day.

**Applied:** every sentence of that form is withdrawn. The surviving
statement is *"the acceleration response is negative"* — no claim about
`H` is made.

### FIX 3 — partial vs total derivative `[WEAKENED → LABELLED]`

Inside the construction `k` cannot move alone; `M`, `R`, `d` share the same
`z`. The realisable quantity is the total derivative along the trajectory.

| | value at `z=0` |
|---|---|
| partial (quoted throughout) | `−4.9224×10⁻⁹¹` |
| **total (realisable)** | **`−9.3492×10⁻⁹²`** |
| ratio | **5.265×** (skeptic said 5.3×) |

Same sign, so the **direction survives**; the magnitude must state which
is quoted. **Applied.**

### FIX 4 — the promised BAO variant was never implemented `[VERIFIED-READ → REMOVED]`

`stage3c`'s docstring promised *"T3 — T2 with a BAO-suppressed / enhanced
baryon fraction, **to bracket the wiggle's influence on the zero**."*
`TRANSFERS` holds exactly two entries, **both strictly smooth**, and
varying `Ω_b` only reshapes the smooth envelope through `s`, `alpha`,
`gamma_eff` — it cannot generate oscillations.

So the one spectrum class where `ξ` is guaranteed **not** monotone (the
baryon acoustic peak near 105 Mpc/h) was named and skipped, while the
conclusion says *"decays monotonically."*

**Applied:** the promise is removed rather than quietly kept; implementing
a real wiggle spectrum is recorded as **OPEN**.

### FIX 5 — the C4 implication is invalid, and its premise was never measured `[FALSIFIED → FIXED]`

`P(0) = 0` does **not** imply "approached from above, never crossing."
That needs the extra premise **`ξ` has exactly one sign change**.

**Verified counterexample** — band-limited `P(k) = k^0.965 exp(−(k−k₀)²/2σ²)`,
`n_s > 0`, `P(0) = 0` exactly, giving `ξ ≈ A sin(k₀r)/(k₀r)`:

```
I(r) = (A/k₀³)[ sin(k₀r) − k₀r·cos(k₀r) ]
at k₀r = 3π/2 :  sin − x·cos = −1.000000   ⇒ NEGATIVE
numerically:     delta_bar reaches −0.0862, first crossing at k₀r = 4.49
```

So `P(0)=0` alone is **not sufficient**. And `grep` confirms **zero**
sign-change counters anywhere in `stage3c` — the premise was assumed, not
checked.

**Applied:** `count_sign_changes()` added and its output printed, so the
premise is now measured rather than assumed.

**Also still open, stated not hidden:** the convergence block varies only
`damp` (0.10 / 0.15 / 0.25 Mpc/h of smoothing — three orders below the
~130 Mpc/h scale of interest); `kmin`, `kmax`, `nk`, `rmax` are never
varied, despite `xi_of_r`'s docstring promising a convergence check.

### FIX 6 — "`d` is not a free variable" was refuted by our own file `[WEAKENED → RESTATED]`

`stage1` line 128 prints, verbatim, **"RADIAL LAW — d treated as a free
variable, not d_of(z)"**, and line 137 loops over `d_mpc ∈ {5, 10, 22.5,
45, 90, 180}` at frozen `z=0` values. **That block is where 92.67 Mpc came
from.**

Both statements are true once separated properly, and the separation is now
printed in the block itself: **the MODEL never varies `d` independently;
WE do, there, as a labelled extension.** The numbers are ours, not
MULTING's.

### FIX 7 — the reachability argument was a non sequitur `[FALSIFIED → REPLACED]`

`stage4` argued `d = 92.67 Mpc` is unreachable because `d ∈ (0, 45]` for
`z ≥ 0`. But **that script itself scans down to `z = −0.95`**, where
`d_of = 45/0.05 = 900 Mpc`. Over its own scan the reachable set is
`(0, 900]`, and 92.67 Mpc **is** reached, at `z = −0.5144`.

**The conclusion survives for a different reason**, which the file did
state but did not lead with:

```
Q(−0.5144) = 3.0222  ≫  1
```

because `k`, `R`, `M` moved along with `d`. So *"`d_flip` is not
derivable"* follows from **`Q(z) > 1` everywhere**, not from
unreachability. **Applied:** the reason is replaced, the old one quoted.

---

## Two repairs that STRENGTHEN the claims

### FIX 8 — the minimum's location was a grid node `[CORRECTED]`

Reported `z = 1.443`. That is node 38 of `np.linspace(0, 3, 80)`, step
`3/79 = 0.0379747`, landing on 1.44304.

Closed form: `Q ∝ u^(−0.6426667)·(0.315u³ + 0.685)^0.2466667`, so
`dQ/du = 0` at `u³ = 14.35834` ⇒ **`u* = 2.430533`, `z* = 1.430533`**.
Independently confirmed by `scipy.minimize_scalar`: **`z = 1.430532`** —
two methods, six-digit agreement.

The **value is unaffected** (1.74835 vs 1.7484, sixth digit); only the
location moves by `Δz = 0.0125`.

### FIX 9 — the claim was weaker than its own code supports `[STRENGTHENED]`

`Q → +∞` at **both** ends (`u^(−0.6427)` as `u→0⁺`, `u^(+0.0973)` as
`u→∞`) with a single stationary point. So **1.7484 is the global minimum
on all of `(−1, ∞)`**, not merely on the scanned window `[−0.95, 16.9]`.

The redshift range in the original statement was an unnecessary
restriction.

---

## Claims that survived untouched

**C3 — `k_of` is literally `(3/2) N k_B T`.** `CONFIRMED-REAL` by both
lines independently. I verified the identity numerically
(`1.5·N·kT = k_of(0) = 1.3880×10⁵⁶ J`); the skeptic derived `μ = 0.588`
from `X = 0.76, Y = 0.24` from first principles, matching the code's 0.6.

One nitpick accepted, not affecting the verdict: standard `μ` is defined
against the atomic mass unit `m_u`, the code divides by `m_p`
(`m_p/m_u = 1.00728`), so `N` is **0.73% low**. `ρ/(μ m_p)` is the
conventional cluster-literature form; no effect on sign or structure.

**C5's point-mass half** — `∂(r̈/r)/∂M = −G/r³ < 0` at all `r`, exact and
trivially correct. Its ΛCDM half inherits everything in FIX 5, and it
names `d(H_local)/dM` while showing `d(r̈/r)/dM` — the same substitution
FIX 2 withdraws.

---

## Net effect on the branch verdict

**Unchanged, and better founded.** `claim.md`'s
`REFUSE(no_falsifiable_predicate_yet)` stands. Both versions of the test
remain closed:

| test | verdict | now resting on |
|---|---|---|
| monotone sign | `CRITERION_INVALID` | Stage 3, untouched by this pass |
| shape (reversal) | no reversal in the model | `Q(z) > 1` globally (FIX 7/9), **not** unreachability |

**What the branch may now claim:** at TJB's own published fit the
**acceleration** response to thermal energy is negative at every epoch the
construction can represent, globally, with no crossover.

**What it may not claim:** anything about the expansion rate `H` (FIX 2),
and the compensation result's *reason* is conditional on a premise now
measured for smooth spectra only, with the BAO case open (FIX 4/5).

---

## FIX 5 — the measurement landed `[VERIFIED-run]`

Appended after the corrected `stage3c` finished (`exit 0`). The premise
the C4 argument rests on is no longer assumed — it is measured:

```
sign changes in xi(r)        : 1
sign changes in delta_bar(r) : 0
```

**Exactly one sign change in `ξ`.** So for these two smooth spectra the
premise the skeptic correctly identified as missing **does hold**, and
with it the conclusion follows properly rather than by assertion:
`δ̄` never crosses zero, `R_comp` does not exist, 0 sign changes measured.

**What this does and does not settle:**

- **Settles:** C4's conclusion is now *founded*, not merely *stated*. The
  gap the skeptic found was in the argument, not in the answer — the
  answer survives with a real premise under it.
- **Does NOT settle:** anything about a spectrum with baryon acoustic
  oscillations. That is FIX 4's removed T3, still **OPEN**, and it is
  precisely the case where `ξ` is not guaranteed to have one sign change.
  The counterexample of FIX 5 (band-limited, `δ̄` reaching `−0.0862`)
  remains the standing proof that the premise is load-bearing rather than
  decorative.
- **Also still open:** the convergence block varies only `damp`;
  `kmin`, `kmax`, `nk`, `rmax` remain untested.

**Net:** of the nine repairs, FIX 5 is now closed on the smooth-spectrum
branch and open on the BAO branch. The other eight stand as committed.

---

## FIX 4 / FIX 5 — the BAO branch is now CLOSED `[VERIFIED-run]`

`stage3d_bao_wiggle_signchanges.py` implements what `FIX 4` removed as an
empty promise, by two independent routes: the full Eisenstein & Hu 1998
transfer function with wiggles (W1) and a tunable BAO template (W2).

**W1 controls:** `T(k→0) = 1.00000`; wiggle amplitude `3.28%` (right order
for real BAO); `14` sign changes of `T_full/T_nowiggle` about its mean, so
the oscillatory structure is genuine and not a transcription artifact.

**Result — every spectrum, 1 sign change in `ξ`, 0 in `δ̄`, no `R_comp`:**

| spectrum | #sign(ξ) | `R_xi0` [Mpc] | `R_comp` |
|---|---|---|---|
| no-wiggle baseline | 1 | 180.2 | NONE |
| **W1 full EH98 wiggles** | **1** | 172.8 | NONE |
| W2 `A=0.05` realistic | 1 | 188.9 | NONE |
| W2 `A=0.20` | 1 | 203.2 | NONE |
| W2 `A=0.60` | 1 | 220.0 | NONE |
| W2 `A=0.95` (~19× real) | 1 | 227.3 | NONE |

W1 and W2 **agree on the count** while **disagreeing on the direction** of
the `R_xi0` shift (W1 down, W2 up) — which is what makes the agreement an
independent cross-check rather than two views of one object. `R_xi0`
spans 31% across the table, so the wiggle is doing something; the *count*
is what is invariant.

**Consequence:** C4's conclusion survives the one case `FIX 4` named as
capable of breaking it. The `FIX 5` counterexample still stands for
*narrow-band* spectra — BAO is a broad damped modulation, which is why it
does not break the premise.

**Status of the nine repairs: eight closed, FIX 4/5 now closed too.**
One item remains open across the whole pass: `stage3c`'s convergence block
still varies only `damp`, never `kmin`/`kmax`/`nk`/`rmax`.

Full detail: `FINDING_stage3d_bao_does_not_break_the_premise.md`.
