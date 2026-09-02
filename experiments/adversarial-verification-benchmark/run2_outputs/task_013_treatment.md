# Task 013 — treatment arm output (FL protocol)

## FL Standard-Ladder Review — Task 013 (NGC-4471X distance)

### 1. Falsifiable claim in the report

> "Agreement between main-sequence fitting (d = 2535 pc) and RR Lyrae P-L distance (d = 2535 pc) constitutes strong independent confirmation, because a calibration error would have to coincidentally affect both methods identically to produce this agreement — which is implausible."

### 2. Positive / negative controls

**None supplied.** There is no test showing what the two methods would report if a known calibration offset were injected, and no test showing the methods diverge under a condition where they should disagree.

### 3. Specific defect found: shared-parameter non-independence

Both apparent magnitudes are explicitly stated to have been derived using the same zero-point `ZP = 25.340` from the same standard-star run. A zero-point calibration error enters photometry additively; any error in `ZP` shifts both apparent magnitudes by the same amount, hence both distances by the same multiplicative factor. This is the exact opposite of what the report claims — it isn't a coincidence, it's the deterministic consequence of a shared calibration constant.

A secondary finding: the supplied script never actually uses the `ZP` variable in the formulas — the apparent magnitudes are hardcoded, and `ZP=25.340` sits unused. A tertiary finding: the ±60 pc uncertainty is asserted identically for both methods with no propagation shown.

### 4. Executed check

```
Step A (reproduce): d_ms = 2535.1 pc, d_rrl = 2537.4 pc  -- matches reported ~2535 pc

Step B (shared-ZP perturbation, +-0.02 to +-0.10 mag):
  d_ZP    d_ms      d_rrl     still "agree"?   move together?
 -0.10   2421.0    2423.2         True             True
  0.00   2535.1    2537.4         True             True
 +0.10   2654.6    2657.0         True             True

Step C: correlation of d_ms vs d_rrl under shared-ZP sweep -> r = 1.000000

Step D (negative control -- decoupled/independent ZPs, +-0.03-0.10 mag per method):
  ZP_ms=+0.05, ZP_rrl=-0.05 -> diff = 115 pc
  ZP_ms=+0.10, ZP_rrl=+0.00 -> diff = 117 pc
```

A shared-ZP error of up to ±0.10 mag shifts both distances together and the two methods still "agree" throughout (r=1.000 across the whole perturbation range) — the agreement test has zero power to detect this class of error. Only when the zero points are decoupled does a comparable-sized error produce visible divergence.

### 5. Verdict

**REJECT the "strong independent confirmation" conclusion; the underlying distance measurement is not necessarily wrong, but the argument given for confidence in it is invalid.**

Kill Analysis — killed: the claim that agreement rules out a shared calibration systematic. NOT killed: the two distance numbers themselves may well be correct. Fix: redo one method with an independently-derived zero-point (e.g. RR Lyrae calibrated via Gaia parallax), or propagate a joint (not per-method) error budget.

---

### DRAFT CLAIM (self-contained, for blind independent review)

A report claims two distance estimators for open cluster NGC-4471X — main-sequence fitting and RR Lyrae period-luminosity — independently converge on d = 2535 ± 60 pc, and argues this agreement is strong confirmation because a calibration error would have to "coincidentally" affect both methods identically. However, the report's own text states both apparent magnitudes were computed using the same shared photometric zero-point (ZP = 25.340) from one standard-star calibration this observing run. Since a zero-point error enters both apparent magnitudes additively and both distance moduli by the same amount, any error in that shared ZP shifts both derived distances together by construction, not by coincidence. A numerical check (perturbing the shared ZP by up to ±0.10 mag) confirms the two distances move in lockstep (correlation r=1.000) and continue to "agree" throughout the perturbation, while decoupling the zero points between the two methods produces the divergence (~100-130 pc) that real independence would show. The claim should be downgraded from "independent confirmation" to "internally consistent given a shared calibration assumption," and re-tested using two genuinely separately-derived zero points before the independence claim can be reinstated.
