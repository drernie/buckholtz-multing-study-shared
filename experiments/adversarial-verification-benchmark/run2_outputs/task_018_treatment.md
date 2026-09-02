# Task 018 — treatment arm output (FL protocol)

## FL Standard-Ladder Review — Task 018

### 1. Two bundled claims
Claim A (numerical): quad at x=1e205 returned -3.2e188. Claim B (interpretive): this might be a genuine asymptotic sign change worth reporting.

### 2. Positive/negative control
**None supplied.** Only one call, at the single extreme point. The "sanity" print about g being a sum of squares was stated but never actually checked against the numeric output.

### 3. Executed checks
- Reproducing the exact script: `g(1e205)` raises `OverflowError` before quad can even run on plain floats — the reported -3.2e188 could not have come from an unmodified run under standard overflow-raising settings.
- With overflow silenced: quad returns `inf`, not -3.2e188.
- Ground truth via mpmath (60-digit precision), closed form `G(x)=(1.1/3)x^3-3.1x^2+9.1x`, always positive: quad matches at x=1e50, 1e100; degrades to `nan` at x=1e150 (with scipy's own IntegrationWarning about exhausted subdivisions); `inf` beyond ~1.3e154.
- Decisive computation-free check: g(x) is a sum of two squares with different roots (3 and 1) — cannot both vanish at once, so g(x)>0 strictly everywhere, and G(x) is strictly increasing for all x>0, with certainty, independent of any floating-point computation. No numerical result at any x can legitimately be negative.
- Overflow onset matches theory exactly: sqrt(float64_max)~=1.34e154, matching where g(x) itself starts overflowing.

### 4. Verdict
**REJECT the interpretive claim; Claim A is not even reproducible as stated.** The negative output is a textbook IEEE-754 overflow/cancellation artifact from evaluating an integral whose true magnitude (~1e614) exceeds float64's max (~1.8e308) by ~300 orders of magnitude. Refuted twice: trivially by the sum-of-squares proof, and empirically by rerunning (which gives nan/inf, not the reported number).

---

### DRAFT CLAIM
A numerical test evaluated G(x)=integral of g(x') from 0 to x at x=1e205, where g(x)=(x-3)^2+0.1(x-1)^2 is provably strictly positive everywhere. The report obtained a negative value and floated the interpretation that this might indicate a genuine asymptotic sign change. This is false by elementary calculus: the cumulative integral of a strictly positive function is strictly positive and increasing everywhere, no computation needed. Independently rerunning the script shows the numerics are unreliable at this scale because g(x) itself overflows IEEE-754 double precision past x~1.34e154 — quad matches a 60-digit mpmath ground truth up to x=1e100, degrades to nan by 1e150, and to inf (with an explicit scipy warning) beyond 1.3e154. No positive or negative control was supplied, and quad's own error estimate (itself inf) was never examined, which should have been the first flag. Verdict: REJECT — floating-point overflow artifact, not a property of the mathematical integral, which remains provably positive at every x.
