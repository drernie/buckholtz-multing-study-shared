# FINDING P135 — the anchor-proximity-to-pole hypothesis is REFUTED; the
# real mechanism sits in the early transient, not at the measurement anchor

**Date:** 2026-08-24
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Verdict:** `POLE-AT-ANCHOR-REFUTED` (diagnostic, not a new observable)
**Script:** `P135_low_k_pole_diagnosis.py`, positive-control-tested (a first
version failed its own control and was corrected before any verdict)

---

## 1. Why this file

`FINDING_P134` synthesized bottleneck 2 (completion uniqueness) as
genuinely open: `P78`'s apparent discrimination signal failed `P79`'s own
robustness gates (G1 convergence, G3 lever) at low `k`, and `P79` names
"a better-conditioned low-`k` observable" as the prerequisite for
reopening the question — not a rescan at a different `k`. Before
attempting to design a replacement observable, this file does the
cheaper, logically prior step: diagnose *why* the current `ε`/separation
is IC-sensitive at low `k` in the first place.

The standing hypothesis, already in the record but never quantitatively
confirmed: `FINDING_P76` states *"the contrast passes near zero at an
anchor, so the ratio has a pole... a defect of the measurement... not a
physical divergence."* But `P76`'s own Skeptic Verdict records that the
one detector built to check this — counting zero-crossings of
`contrast(t)` over the *whole* trajectory — does not discriminate:
*"P77's sign-count is 1 at every k, including the clean ones"* — accepted
as an open item, never resolved.

## 2. A correction made mid-run, before any verdict

A first version of this diagnostic measured "closeness to a pole" as
`|contrast(t_anchor)|` divided by the max `|contrast|` sampled over a
wide `[0.3t, 3t]` window. Run once: it returned near-machine-zero
"closeness" values (e.g. `8.3e-106`) at **every** `k`, including `k=10`
— `FINDING_P76`'s own known-clean positive control. That is not a real
signal; the wide window was dominated by later, much larger
growing-mode values, not proximity to an actual zero. **The positive
control caught this before it was reported as a finding** — matching
this campaign's own repeated discipline (P76, P78, P80 all show the same
pattern: build, run, control fails or a check reveals a defect, fix,
rerun before writing the verdict).

**Fix:** replaced the window-max with a genuinely local metric —
`close(t) := |c(t)| / (|dc/dt|(t)·t)`, the number of e-folds in `t`, at
the local linear rate, to the nearest zero of `contrast`. Small (`<0.2`)
means the anchor sits next to a crossing; large means it does not.
Rerun: the positive control now passes cleanly (`k=10`: no sign flips,
minimum closeness `1.43`, far above the `0.2` threshold).

## 3. Result

| k | sub-run contrast sign-flip (lever 0.1→2.0) | P79 separation sign-flip | min closeness at anchor |
|---|---|---|---|
| 1 | No | No | 1.41 |
| 2 | No | No | 1.44 |
| 3 | No | **Yes** (P79's G3 failure) | 1.44 |
| 10 (control) | No | Yes (new — P79 never tested `k=10`) | 1.43 |

**No sub-run's individual contrast value at either anchor (`t1`, `t2`)
comes anywhere close to zero, at any tested `k` — including `k=1`, the
worst of P79's own failures.** The closeness values cluster tightly in
`[1.41, 1.50]` across the entire tested range, essentially flat in `k`.

**A striking regularity, not pre-registered but worth recording:** the
uncoupled (`ĝ=0`) reference branch gives closeness `≈1.500` to 3–4 digits
at *every* `k` and lever tested. `close(t) = |c|/(|dc/dt|t) = 1/p` exactly
for a pure power law `c(t) ∝ t^p` — so `1.500` corresponds to
`p ≈ 2/3`, the textbook matter-domination growing-mode exponent
(`δ ∝ a ∝ t^{2/3}`). **The anchors sit deep in a smooth, textbook growing
mode for every run tested — nowhere near the oscillatory regime.**

## 4. Verdict

**`POLE-AT-ANCHOR-REFUTED`.** `FINDING_P76`'s informal diagnosis — that
`P79`'s instability comes from the measurement anchor landing near a
zero of `contrast(t)` — does not hold. Anchor-point proximity to a pole
is not the mechanism; the anchors are uniformly far from any crossing,
at every `k` tested, including the ones where `P79` found real
instability.

**What the k=3 sign-flip actually looks like, given this:** with neither
completion's own `contrast` anywhere near a pole, the separation
(`ε_exponential − ε_linear`) changing sign as the lever varies means the
two completions' `ε` values *cross each other* at some lever value
between `×0.1` and `×2` — a zero of the *difference* of two smoothly
varying, non-pathological quantities, not a pole in either one. A
qualitatively different, and less alarming, kind of sensitivity than a
literal division-by-near-zero.

**A real, testable next hypothesis this file's own elimination points
to, `[INFERRED]`, not tested here:** `P77`'s own ~160 zero-crossings were
found at `(ĝ=0.5, k=1)` — almost certainly in the *early* transient
(small `t`), since by the time the trajectory reaches P79's own anchors
(`t1 ~ O(10^4)`, `t2 ~ O(10^8)`) it has long since settled into the smooth
power-law regime this file measures. If so, the IC-sensitivity `P79`
found is not a local anchor-point defect but an **accumulated**
sensitivity: small IC changes shift the phase/amplitude of the early
oscillatory transient, and that shift propagates, amplified or not,
into the late-time growing-mode amplitude the anchors sample. This is a
mechanism candidate, not a result — the early-transient regime itself
was not examined in this file.

## 5. What this does NOT establish

1. **A replacement, IC-robust observable.** A separate design task, only
   motivated — not attempted — by this file's elimination of the pole
   hypothesis.
2. **The early-transient-sensitivity hypothesis (§4).** Named as the
   natural next diagnostic step, not tested here — would require
   instrumenting `contrast(t)` at early `t` (near the ~160-crossing
   regime `P77` found) and tracing how the lever's IC change there maps
   to the late-time amplitude.
3. **Anything about G2 (anchor-`A1` spread) or G4/G5** — not rerun here;
   only G1/G3's own grid was used, reusing `P79`'s own thresholds where
   relevant.
4. **The k=10 separation sign-flip found in Part B.** `P79` never tested
   `k=10` for the separation; this file's own Part B found one there too
   — new information, outside this file's own scope to interpret,
   flagged for the record rather than analyzed.
5. **Anything observational.** Internal units; `NO_BRIDGE_FITTING` in
   force.
6. **Anything about MULTING itself** (Gate 1). Both completions are ours.

## 6. Controls

- **Positive control**: `k=10` (`FINDING_P76`'s own known-clean point)
  must show no sign flips and closeness well above threshold — FAILED on
  the first (window-based) metric, caught before reporting, PASSED after
  the fix (§2).
- **Reuse, not re-derive**: `run`/`contrast`/`t_of_a`/`eps`/`sep` imported
  directly from `P79`'s own module (which imports `P78`'s), not
  reimplemented.
