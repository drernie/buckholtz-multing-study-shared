# FINDING P136 — the early-transient hypothesis is REFUTED; REDIRECT
# triggered on the mechanism-diagnosis sub-thread

**Date:** 2026-08-24
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Verdict:** `EARLY-TRANSIENT-REFUTED` (2nd consecutive kill on this
sub-question — triggers `docs/147`'s own REDIRECT rule)
**Script:** `P136_early_transient_sensitivity.py`, positive-control-tested

---

## 1. Why this file

Round-2 strategic arbiter (this session) named this the strongest
surviving GO for bottleneck 2 (completion uniqueness): test `P135`'s own
live candidate mechanism — that the IC lever shifts the early
oscillatory transient (`P77`'s own ~160 zero-crossings at
`(ĝ=0.5, k=1)`), and that shift propagates into the late-time growing-
mode amplitude `P79`'s own anchors sample, producing the IC-sensitivity
`P79` found (and `P135` showed is *not* a local anchor-point pole).

## 2. Design

Estimator chosen to avoid the "seventh instance" category error
`FINDING_P80` named (a point sample of an oscillating quantity measures
*phase*, not *amplitude*): `RMS(contrast)` over an early window
`t ∈ [1, 100]` — well inside the oscillatory regime, well before `P79`'s
own anchors at `t ~ 10⁴ / 10⁸` — as the IC lever varies (`×0.1..×2`, the
same range `P79` used). Pre-registered: if the early-window spread is
substantially larger (`>1.5×`) at unstable `k ∈ {1,2,3}` than at the
`k=10` positive control, the transient carries the sensitivity.

## 3. Result

| k | early-RMS spread (lever ×0.1..×2) | ratio to control | P79 late-time instability |
|---|---|---|---|
| 1 | 1.038 | **0.85×** control | G3 spread 5.2× |
| 2 | 1.131 | **0.93×** control | G3 spread 4.4× |
| 3 | 1.169 | **0.96×** control | G3 sign flip |
| 10 (control) | 1.215 | 1.00× | (new: also a sign flip, `P135` Part B) |

**No discrimination — if anything, the reverse of the prediction.** The
early-window sensitivity to the IC lever is *comparable to or slightly
below* the control at every unstable `k`, not elevated. The
late-time instability (`5.2×`, `4.4×`, sign flip) has no counterpart in
the early-window amplitude spread (`1.04×`–`1.17×`, all close to 1).

## 4. Verdict

**`EARLY-TRANSIENT-REFUTED`.** Whatever mechanism connects the IC lever
to `P79`'s late-time separation instability, it is not simply "the early
oscillatory transient's amplitude shifts with the lever and that shift
carries through." The amplitude-level early-transient signature this
file measured does not track the late-time effect at all.

**Combined with `FINDING_P135` (pole-at-anchor, refuted): two consecutive
kills on the same sub-question** — why is `P79`'s separation IC-sensitive
— with no new discriminating mechanism surfacing between them. Per
`docs/147`'s own REDIRECT rule (*"два последовательных эксперимента дают
partial/fail без появления нового различающего механизма"*), **this
sub-thread REDIRECTS.** A third mechanism-diagnosis attempt of the same
general shape (instrument some summary statistic, correlate against the
lever) is not warranted without a genuinely new candidate mechanism —
none is currently in hand.

**What survives, honestly:** the IC-sensitivity itself is real and
robust (`P79`'s own numbers, reproduced identically here via `sep()`
reuse) — only its *cause* remains open. Two real candidates have now
been eliminated (anchor pole; early-amplitude transient), which is
itself useful negative information for anyone designing a replacement
observable later: whatever the mechanism is, it is not visible in either
the measurement-point value or the early-transient amplitude alone.

## 5. What this does NOT establish

1. **What the actual mechanism is.** Two candidates eliminated, none
   confirmed — genuinely open.
2. **That no early-transient signature exists at all** — only that
   `RMS(contrast)` over `t∈[1,100]` does not show one. A *phase*-based
   statistic (e.g. the timing of the last zero-crossing, or a spectral/
   envelope decomposition) was not tested and remains a candidate for a
   future attempt, IF a concrete new mechanism motivates it — not
   pursued now per the REDIRECT verdict above.
3. **A replacement, IC-robust observable.** Separate design task.
4. **Anything about G2/G5 directly.** Not rerun here.
5. **Anything observational.** Internal units; `NO_BRIDGE_FITTING` in
   force.
6. **Anything about MULTING itself** (Gate 1). Both completions are ours.

## 6. Controls

- **Positive control (rtol)**: early-window RMS stable to `4.6×10⁻⁹`
  relative shift across `rtol ∈ {10⁻⁸, 10⁻¹⁰, 10⁻¹²}` — numerically
  trustworthy.
- **Reuse, not re-derive**: `run`/`contrast`/`sep` imported directly from
  `P79`'s own module.
