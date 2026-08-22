# FINDING P119 — `ln(a)` state reformulation removes the last float64 wall; **`STILL-CLIMBING, FASTER-THAN-LOGARITHMIC-IN-TESTED-WINDOW`** (a `PLATEAU-FOUND` draft verdict was retracted before commit)

**Status:** built, regression-verified against `FINDING_P118` (not assumed),
extended to `T_END=1e13` (`a_reach/a_star ~ 10^397,506`). A first analysis
pass produced a `PLATEAU-FOUND` draft verdict from a naive step-to-step
percentage check; this was caught and retracted **before commit**, replaced
by two decade-scale-aware checks that rule a plateau out.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P119_ln_a_state_reformulation.py`

> User-directed: "rescale `a` itself via `ln(a)` tracking." `FINDING_P118`
> extended `contrast`'s validity by ~180 decades but left a *separate* wall
> untouched: `a` itself, tracked raw, still overflows float64's absolute
> maximum at `t≈7.634×10⁹`.

---

## The reformulation

Track `L := ln(a)` as the state variable instead of raw `a`. Then
`dL/dt = H` — no `a` at all in that derivative. Since `H` approaches a
constant once `Λ` dominates, `L` grows *linearly* in `t`, never overflowing
for any `t` this file can afford. Every other appearance of `a` is rewritten
as `exp(-n·L)` rather than `1/a^n` — `np.exp()` of a very negative number
returns exactly `0.0` smoothly, with no intermediate overflow step.

## Controls, all pass

- **Regression vs `FINDING_P118`**: agrees to `6×10⁻¹¹`–`2×10⁻⁹` across
  `x=2` to `x=1e250`.
- **Smooth-case regression** (`k=10`): agrees to `10⁻¹³`.
- **Reach**: `T_END=1e13` succeeds, reaching `a_reach/a_star ~ 10^397,506`
  (`1e15`/`1e17` were tried and found computationally impractical —
  `851,889` solver steps and `~166s` already at `1e13` — dropped rather than
  left to hang silently).

## The retracted draft, kept as history not erased

A first pass computed the `x_lo`-independence scan out to `x_lo=10^100,000`
and found `√G_E` rising only `0.23%` in total, with a naive last-step
change of `0.08%` — the file's own first-cut verdict logic (`last-step
change < 0.1% → plateau`) accordingly printed **`PLATEAU-FOUND`, converged
value `1,254,869.66`**.

**This was wrong, and was caught before commit — not smoothed over.**
Checked directly: the rise across matched, exact `10×` decade-jumps, at
increasing scale, was **growing**, not shrinking:

```
10^90   -> 10^900:    rise = 0.0228%
10^3000 -> 10^30000:  rise = 0.0911%
10^10000-> 10^100000: rise = 0.1299%
```

If a genuine plateau existed, this should shrink toward `0` as the jump
moves to larger decade-ranges. It does the opposite. A second check —
cumulative rise divided by `ln(decades+1)`, which should be roughly flat if
the growth were merely logarithmic-in-decades (the slowest non-plateau
shape) — also **grows monotonically** (`0.000033 → 0.000201` across the
scan), ruling out even that slower alternative.

**The naive last-step percentage was misleading, not wrong arithmetic** —
it was small only because the scan's own decade-step size itself grows
exponentially, so *any* smoothly-growing quantity will show a shrinking
per-step percentage near the end regardless of whether it is actually
leveling off. This is the same trap, in a new guise, that the earlier
(also-retracted) `P117` `TRUE-ASYMPTOTE-FOUND` draft fell into.

---

## Verdict — **`STILL-CLIMBING, FASTER-THAN-LOGARITHMIC-IN-TESTED-WINDOW`**

Both decade-scale-aware checks rule out a plateau within the tested domain,
and rule out even pure log-in-decades growth. `FINDING_P117`/`P118`'s
`STILL-NOT-CONVERGED` verdict stands, now characterized more precisely than
either could show alone — not merely "we haven't found the end," but "the
rate of accumulation is itself still growing, in a specific, checkable
sense, across the entire tested window."

**Important scope discipline, stated explicitly**: this is a claim about
*behavior on the measured tail*, not a proof of asymptotic divergence. The
honest boundary is between "no evidence of convergence, and specific
evidence the naive convergence signal was itself misleading" (established
here) and "proven to diverge faster than any logarithm, as a true
mathematical limit" (not established, and not claimed).

### What P119 gave the project

Not "failed to find a plateau." Concretely: eliminated the `a³` overflow
(`P118`), eliminated `a`'s own overflow (this file), confirmed both
reformulations by direct regression (not algebra alone), showed the earlier
apparent plateau was an estimator-design artifact — and pushed the branch
into a regime where computational reach is no longer the limiting question.

### Not established

- A rigorous asymptotic proof that the climb is unbounded, rather than
  converging at some yet-larger `x_lo` beyond this file's own tested
  `10^100,000` — this file tests a much larger but still finite domain.
- The precise functional form of the growth (power-law-in-decades,
  log-squared, or something else) — the two checks rule out a plateau and
  rule out pure log-in-decades; they do not identify what it actually is.
- Whether accumulated floating-point/quadrature error over such an enormous
  domain could itself explain part of the remaining rise.
- Anything at `Λ` values, or `(k, IC)` combinations, other than the one
  tested.
- Any numeric value of `eps(k)`, `G_growth`, or `f(k)` in physical units, or
  any `k[h/Mpc]`.
- Anything about MULTING itself (Gate 1).

### Where this goes next

Not a bigger `T_END` — computational reach stopped being the bottleneck
once `a` itself was rescaled. The next, cheaper, more decisive question is
about the *local* tail law of the integrand `h(N) := contrast(N)²`
(`N := ln(a)`), not the cumulative integral: does `h(N)` decay fast enough
for `∫h dN` to converge? A block-ratio integrability test
(`R_j := B_{j+1}/B_j` for `B_j := ∫_{N_j}^{N_j+ΔN} h dN`) and a power-law
envelope fit (`|contrast| ~ N^{-q}`, integrable iff `q > 1/2`) answer this
directly on the *already-computed* trajectory, without pushing `N` any
further — see `FINDING_P120`.
