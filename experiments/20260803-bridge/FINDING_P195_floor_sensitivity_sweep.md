# FINDING P195 — floor-sensitivity sweep for `FINDING_P158_ADDENDUM2`'s
# grounded ρ result

**Date:** 2026-09-05
**Claim:** `CLAIM_P195_floor_sensitivity_sweep.md`
**Script:** `P195_floor_sensitivity_sweep.py`
**Continues:** `FINDING_P158` (Jensen's-inequality mechanism, threshold
`ρ>−0.5`), `FINDING_P158_ADDENDUM2` (real, computed `ρ>0` for `z≤0.5`,
its own `Objection 2` naming the floor choice as untested), `docs/156`
(this session's precondition check, §5, naming this exact sweep).
**Verdict (final, post-skeptic):** `SIGN-ROBUST-AND-THRESHOLD-SAFE-
BUT-NOT-MAGNITUDE-STABLE, WITHIN TESTED RANGE ONLY` — the pre-registered
MCID passes cleanly (no sign flip, no approach to the `ρ=−0.5`
threshold at any tested floor choice), but the underlying magnitude
varies by up to ~30× across those same choices, which the absolute-
delta MCID does not capture and a Step 8a skeptic pass correctly caught.

## Result

**Regression check** (renamed from an original, over-strong "positive
control" label — see Corrections below): at `f=2.0` (ADDENDUM2's own
baseline floor, `M≥M_of(z)/2`), this file's parameterized sweep
harness reproduces ADDENDUM2's own tabulated `ρ` values to <1% relative
error at all 4 already-trusted redshifts (`z=0, 0.0233, 0.07, 0.5`) —
`[VERIFIED-BASH]`, real `pytest` run.

**Floor sweep** (`M≥M_of(z)/f` for `f∈{4,2,1}`, plus a qualitatively
different bounded-bin construction `M_of(z)/2≤M<2·M_of(z)`):

| z | f=4 (lower floor) | f=2 (baseline) | f=1 (higher floor) | bounded bin | fold-change |
|---|---|---|---|---|---|
| 0.000 | 0.020543 | 0.004506 | 0.000766 | 0.002849 | **26.8×** |
| 0.023 | 0.042096 | 0.010071 | 0.001762 | 0.006380 | **23.9×** |
| 0.070 | 0.023679 | 0.005262 | 0.000899 | 0.003394 | **26.4×** |
| 0.500 | 0.004124 | 0.000836 | 0.000138 | 0.000625 | **29.9×** |

`ρ` stays strictly positive at every tested (z, floor) combination, at
every one of the 16 (4 redshifts × 4 constructions) computed values.
No sign flip anywhere. The maximum absolute value reached (0.042) is
still ~12× below the pre-registered MCID threshold (0.05) and ~12×
below the `ρ=−0.5` decision boundary in relative terms — the pre-
registered MCID cleanly passes.

**But the magnitude is not stable**: `ρ` varies by a **~24-30× fold-
change** across the tested floor choices at every redshift, and follows
a clear, monotonic pattern — `ρ` **decreases as the floor mass
increases** (lower `f`, i.e. a higher, more exclusive mass threshold,
gives a smaller `ρ`). This pattern is reported, not extrapolated: this
file does not know whether it continues, flattens, or reverses outside
the tested `f∈{4,2,1}` range.

## Verdict on `docs/156`/`CLAIM_P195`'s own question

**The qualitative conclusion survives; the exact number does not.**
`FINDING_P158_ADDENDUM2`'s directional claim — population-averaging
favors `F^(2)` over `F^(1)` at `z≤0.5`, because `ρ>0` there — is
**robust** to the arbitrary `M_of(z)/2` floor choice in the sense that
matters for `P158`'s own decision rule: `ρ` never gets close to flipping
sign or crossing `−0.5` under any tested alternative. It is **not
robust** in the sense of being a stable, precisely-known number — a
different, equally defensible floor choice changes the computed `ρ` by
up to 30×. Any future use of this specific `ρ` value (not just its
sign) should carry this caveat explicitly.

## Corrections applied (Step 8a context-blind skeptic pass, 2026-09-05)

The skeptic was given only `CLAIM_P195` + the code (no reasoning chain,
Context Asymmetry Rule), and returned an overall `WEAKENED` verdict on
5 probed items. Response Matrix:

1. **Probe 1 (MCID scale mismatch) — Accepted, fixed.** The
   pre-registered absolute-delta MCID (0.05) is calibrated against the
   mechanism's `−0.5` decision threshold, not against `ρ`'s own tiny
   scale (~0.0007-0.04) — it can pass even under a large *relative*
   swing. Fixed: the script now reports fold-change explicitly
   alongside the absolute spread (table above), and the verdict
   language is split into "sign/threshold-safe" (MCID's actual claim)
   vs. "magnitude-stable" (a claim the MCID never licensed). **This is
   not a retroactive MCID redefinition** — the pre-registered pass/fail
   criterion is unchanged and still cleanly passes; what changed is
   that an additional, honestly-labeled diagnostic (fold-change) is now
   reported alongside it, and the prose no longer calls the result
   flatly "ROBUST" without that qualifier.
2. **Probe 2 (bounded-bin formula faithfulness) — `CONFIRMED-OK`,** no
   fix needed. `pair_rho_exact`'s derivation is symbolic in the four
   population moments and does not assume unbounded support; the
   bounded-bin function re-integrates all four moments consistently on
   the restricted domain before calling the same formula.
3. **Probe 3 (regression-check independence) — Accepted, fixed.** The
   original claim/code called this a "positive control," which
   overclaims: it reuses the exact same imported functions ADDENDUM2
   itself used, so it cannot catch a units or conversion bug shared
   with ADDENDUM2 — it can only catch a discrepancy this file's own
   sweep harness introduces. Renamed throughout (function name, print
   output, this document) to "regression check (non-independent)."
4. **Probe 4 (ν lower-bound at low floors) — `CONFIRMED-OK`** for the
   tested range: at `f=4`, `ν` reaches down to ~3.9-5.4, still well
   inside Tinker et al.'s typical calibration span, not into a
   low-`ν` regime where linear bias itself becomes questionable for
   very common halos. Noted as a legitimate scope boundary, not an
   active failure.
5. **Probe 5 (untested extrapolation of the monotonic trend) —
   Accepted, fixed.** The original "ROBUST" verdict was too categorical
   for a directional pattern the sweep itself surfaces (`ρ` falls
   monotonically as the floor rises) without any evidence about
   floor choices outside `{4,2,1}`. Fixed: the verdict is renamed
   `SIGN-ROBUST-AND-THRESHOLD-SAFE-BUT-NOT-MAGNITUDE-STABLE, WITHIN
   TESTED RANGE ONLY`, and the monotonic pattern is stated explicitly
   as an open, unextrapolated observation.

No probe found a computational error in the core sweep or bounded-bin
calculations themselves — all 5 items were about the honesty and scope
of the *interpretation* layered on top of a correctly-computed result,
not about the numbers being wrong.

## What this does NOT establish

1. Does not extend trustworthy `ρ` coverage to `z≥1.07` — `ADDENDUM2`'s
   own finding that those redshifts extrapolate past Tinker et al.'s
   `ν` calibration is untouched.
2. Does not establish that `ρ`'s magnitude is known to any useful
   precision — only that its *sign* and its *distance from the
   decision threshold* are robust to the tested floor alternatives.
3. Does not test floor choices outside `f∈{4,2,1}` (e.g. `f=8` or
   `f=0.5`) — the monotonic trend's continuation, flattening, or
   reversal beyond this range is unknown.
4. Does not resolve `docs/153`'s literal "finite-r/single-pair
   calculation" — `docs/156` already established that specific test is
   not currently buildable (missing `q(a)` evolution law, proven
   underdetermined by `docs/126`); this file continues the different,
   mechanically-correct line of work `FINDING_P157`→`P158` identified.
5. Does not resolve bottleneck 1 as a whole — scoped entirely to one
   narrow sub-question about one already-narrow prior result.
6. `NO_AUTHOR_ERROR` — entirely about this project's own reconstruction
   and sensitivity analysis, never a claim about Dr. Buckholtz's own
   theory.

## Pearl / methodological carry-forward

Worth a `pearl_registry/INDEX.md` line: **an absolute-value MCID
calibrated against a decision threshold can silently pass through a
large relative swing when the underlying quantity's own natural scale
is far below that threshold** — the same general shape of gap as
P194's own "a monotonic trend correlated with one hypothesized
mechanism can hide a second, uncontrolled mechanism," but here about
metric *design* (MCID choice) rather than mechanism attribution. Both
surfaced the same day (2026-09-05) via targeted Step 8a skeptic passes
on two unrelated calculations.
