# FINDING P120 — Tail convergence test, redesigned mid-build after its own positive control caught a wrong premise: **`CONVERGENT-CONTRAST, CROSS-VALIDATED`**

**Status:** built exactly to the user's original specification, positive
control failed, redesigned honestly (not silently patched), rebuilt around
a corrected premise, and cross-validated with a held-out prediction test.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P120_tail_integrability_test.py`

> User-directed, precise specification: a block-integrability test on
> `h(N):=contrast(N)²` (`N:=ln(a)`), `R_j:=B_{j+1}/B_j` for
> `B_j:=∫_{N_j}^{N_j+ΔN} h dN`, expecting `R_j→r<1` for a genuinely
> convergent case, plus a power-law envelope fit `|contrast|~N^{-q}` with
> integrability threshold `q>1/2`.

---

## Part 1 — built exactly as specified, positive control failed

Before trusting anything on the harder `k=0.3` case, the design required a
positive control: `k=10`'s `G_E` is already known (`FINDING_P114`/`P117`)
to converge fast, so its own `R_j` had to show `r<1` clearly.

**It didn't.** `R_j` converged to *exactly* `1.0` from above
(`1.0072 → 1.0015 → 1.0003 → ... → 1.0000005`), not below.

## Part 2 — diagnosed directly, not patched around

`contrast(N)` — the raw, unsquared, *single-run* quantity, not a
coupled/reference ratio — does **not** approach zero as `N→∞`, even for
the smooth `k=10` case. It approaches a finite **nonzero** constant instead
(`drA_hat`, `qm_hat` settle to finite late-time values, per
`FINDING_P118`'s own derivation). So `h(N)=contrast(N)²` approaches a
positive constant, and `∫h dN` grows **linearly** in `N` — for *every*
case, convergent or not, because this integrates a single run, not the
coupled/reference ratio `G_E` actually is. "Integrability of `h(N)` alone"
was the wrong question — not because the block-ratio arithmetic was wrong,
but because its premise (`h(N)→0`) doesn't hold for this system.

## Part 3 — the corrected, simpler test

By a standard L'Hôpital-style argument: if `contrast_coupled(N)→A_c` and
`contrast_reference(N)→A_r` (both finite), then
`∫h_c dN' ~ A_c²·N + const_c` and `∫h_r dN' ~ A_r²·N + const_r` for large
`N`, so `G_E(N)` — the ratio of the two integrals — `→ (A_c/A_r)²`, a
**finite** limit. If `contrast_coupled(N)` instead grows without bound
(however slowly), its integral grows faster than linear while the
reference's stays linear, and `G_E(N)→∞`. So the decisive question is
simply: **does `contrast_coupled(N)` itself converge to a finite value?**
Tested with the same matched-jump / shrinking-increment diagnostic
`FINDING_P119` already validated on `G_E` itself — applied here directly
to the point value, no block integration needed.

## Results

- **Regression** vs `FINDING_P119`'s own values: agrees to `10⁻⁹`–`10⁻¹⁰`.
- **Positive control, redone**: `k=10`'s `contrast(N)` converges cleanly
  (final relative step `0.0000%`).
- **Resolution**: `n=200k` vs `400k` agree exactly (`0.000e+00`).
- **Main result**: `k=0.3` coupled `contrast(N)` shows a shrinking
  increment across the tail (`-34,958 → -38,455`, final relative step
  `0.09%`).

## The decisive check — held-out cross-validation, not eyeballing

A simple "increments are shrinking" check is exactly the kind of naive
signal that fooled `FINDING_P119`'s own retracted `PLATEAU-FOUND` draft.
Applied a materially stronger test instead: fit
`contrast(N) = c_∞ - A·N^{-p}` on all *but* the last point, then check how
well that fit **predicts** the excluded point.

- **Coupled branch**: fit (excluding the last point) gives `p=0.503`
  (remarkably close to exactly `1/2`), predicts the held-out point to
  **`0.0036%`** error. Full-data residuals: max `0.0043%` of the typical
  value, across all 14 points.
- **Reference branch**: found to be **exactly constant**
  (`0.030609...`) across the *entire* tested window — already fully
  converged before this file's measurement even begins. No power-law fit
  is meaningful here (confirmed explicitly, not silently mis-fit — `scipy`
  itself flagged an unconstrained covariance on a first attempt, which the
  final version detects and reports as a degenerate case rather than
  presenting a spurious fit).

**Predicted `G_E` limit** = `(c_∞,coupled / c_∞,reference)²` ≈
`1.5875×10¹²`, i.e. `√G_E → 1,259,961`. `FINDING_P119`'s own last measured
cumulative value was `1,254,870` — **below** the predicted limit, exactly
the relationship required if `G_E` is still climbing toward it rather than
diverging.

---

## Verdict — **`CONVERGENT-CONTRAST, CROSS-VALIDATED`**

The coupled branch's `contrast(N)` passes a held-out power-law fit — the
same style of adversarial check that caught `FINDING_P119`'s own false
plateau, applied here in the *confirming* direction and surviving it. The
reference branch needs no such fit; it's already exactly converged. By the
L'Hôpital argument, this predicts `G_E(N)` itself converges to a finite
limit — consistent with, and extending, `FINDING_P119`'s own
`STILL-CLIMBING`-but-not-yet-converged cumulative trend, which this fit
suggests is climbing *toward* the predicted value rather than diverging.

This does not contradict `FINDING_P119` — it explains *why* the cumulative
integral hadn't shown convergence yet within its tested window: a
cumulative integral of a power-law-converging quantity takes materially
longer to reveal its own convergence than the point-level quantity does,
since it has to "digest" the entire earlier history before its own rate of
change becomes small. Point-level convergence is easier to detect than
cumulative-integral-level convergence — exactly what happened here.

### Not established

- A rigorous asymptotic proof — the matched-jump diagnostic and the
  power-law fit characterize the tested, finite tail, not a mathematical
  limit.
- A fully independent confirmation of the predicted `G_E` limit itself
  (only cross-checked for directional/magnitude consistency against
  `FINDING_P119`'s own trend, not independently re-derived from the
  cumulative integral at comparable reach).
- Anything at `Λ` values, or `(k, IC)` combinations, other than the one
  tested.
- Any numeric value of `eps(k)`, `G_growth`, or `f(k)` in physical units,
  or any `k[h/Mpc]`.
- Anything about MULTING itself (Gate 1).
