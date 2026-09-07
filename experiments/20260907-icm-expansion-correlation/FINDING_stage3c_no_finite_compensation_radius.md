# FINDING — Stage 3c: linear ΛCDM has **no finite compensation radius**,
# so the standard picture has no reversal in either limit

**Date:** 2026-09-07
**Artifact:** `stage3c_compensation_scale.py`
**Labels:** `NOT_VALIDATION` · `NOT_REFUTATION` · `OUR_RECONSTRUCTION` ·
`NO_AUTHOR_ERROR` · L0 `descriptive`
**Status:** Stage-3c result, **not promoted**, no Step 8a pass.

---

## 0. What this replaces

Stage 3b left the compensation radius as `[INFERRED]` *"≤ d₀/2 = 22.5
Mpc"* from a geometric hand-argument. The user's instruction was to
**compute it, not estimate it**. Computed. **The guess was wrong in
kind, not merely in value: there is no such radius.**

## 1. Definition actually used

```
delta_bar(r) = (3/r³) · ∫₀ʳ ξ(s) s² ds
R_comp       = first zero of delta_bar
```

the radius inside which the mass excess is exactly cancelled by the
surrounding deficit.

**Bias-independent, and this matters:** around a halo the profile is
`b(M)·ξ(r)` in linear theory; `b(M) > 0` is a multiplicative constant and
cannot move a zero. `R_comp` does not depend on which cluster mass we pick
— so the answer below is not a property of TJB's `6×10¹⁴ M☉` node, it is a
property of ΛCDM.

## 2. Controls

| control | result |
|---|---|
| **PC1** `σ₈` renormalisation returns the input | `0.811000` for both transfer functions — PASS |
| **PC2** `T(k) → 1` as `k → 0` | BBKS `0.99987`, EH98 `1.00000` — PASS |
| **NC1** Gaussian `P(k)=exp(−k²R²)`, `ξ` strictly positive | `R_comp = None`, `delta_bar > 0` everywhere — PASS |
| **PC3** `P(0)=0` ⇒ `∫ξr²dr → 0` | `+3.22e2` at `r=1200` vs peak partial `2.01e3`, ratio `0.16` and falling — converging |
| **convergence** `R_comp` vs numerical damping `1.0 / 1.5 / 2.5` | `NONE / NONE / NONE`; `R_xi0` stable at `121.45 Mpc/h` in all three |

### 2.1 NC1's first version was withdrawn — recorded, not swapped

The original NC1 used a pure power law `P ∝ k^0.965` and expected no
zero. It **failed**, reporting `R_comp = 5.84 Mpc/h`. Diagnosis: the
numerical damping `exp(−(k·damp/10)²)` **itself introduces a scale**, so a
"featureless" power law is not featureless once damped — the control could
not have discriminated anything. Replaced with the Gaussian case, whose
`ξ` is analytically positive.

**NC1 also caught a real bug in my own tooling** before that: the
cumulative integral is identically `0` at the first grid point, which
`np.sign` read as a sign change, so `first_zero` returned the grid's own
first point. Fixed with an explicit `skip`. The negative control did its
job on the instrument, not only on the physics.

## 3. The result

`delta_bar(r)`, EH98 no-wiggle, Planck-like parameters:

| r [Mpc/h] | r [Mpc] | ξ(r) | **delta_bar(r)** |
|---|---|---|---|
| 5.00 | 7.42 | +9.784e-01 | **+1.574e+00** |
| 19.99 | 29.66 | +9.174e-02 | **+2.210e-01** |
| 44.98 | 66.74 | +1.089e-02 | **+4.368e-02** |
| 62.47 | 92.69 | +3.610e-03 | **+2.014e-02** |
| 92.46 | 137.18 | +6.298e-04 | **+7.278e-03** |
| 129.95 | 192.80 | −7.123e-05 | **+2.714e-03** |
| 199.92 | 296.61 | −1.452e-04 | **+6.343e-04** |
| 399.83 | 593.23 | −1.204e-05 | **+4.337e-05** |
| 800.17 | 1187.19 | −9.322e-07 | **+2.822e-06** |

> **`delta_bar(r)` is POSITIVE at every finite radius and decays
> monotonically toward zero. `R_comp` does not exist.**

`ξ(r)` itself does cross zero — at `121.45 Mpc/h = 180.19 Mpc` — but
**that is not the compensation radius** and must never be quoted as one.
It is where the correlation changes sign, not where the *integrated*
excess does.

## 4. Why — and this is analytic, not numerical

```
P(k) = 4π ∫ ξ(r) sinc(kr) r² dr      ⇒   P(0) = 4π ∫₀^∞ ξ(r) r² dr
```

For ΛCDM, `P(k) → A k^{n_s}` with `n_s = 0.965 > 0`, so **`P(0) = 0`** and
the total integral vanishes *exactly*. But `ξ > 0` at small `r` and `ξ < 0`
beyond `R_xi0`, so the cumulative integral rises, then decreases
monotonically back to its limit — **approaching zero from above, never
crossing it.**

Compensation in linear ΛCDM is exact only at infinity.

## 5. Consequence — the floor has no reversal in either limit

| standard limit | response `∂H_local/∂M` | reversal? |
|---|---|---|
| uncompensated point mass + `Λ` (Stage 3b §2) | `−G/r³`, negative at all `r` | **no** |
| compensated linear ΛCDM (**this stage**) | `delta_bar > 0` at all finite `r` | **no** |

**MULTING's sign reversal at `d_flip = 92.67 Mpc` has no standard
counterpart.** On the floor side the **shape test is discriminating** —
and that is now computed, not assumed.

## 6. What still stands against it

Stage 3b §5, unchanged and unaffected by this stage: `d_flip / d₀ = 2.06`.
MULTING's reversal sits at twice its own node separation, outside the
single-representative-pair construction (`FINDING_P157`) the `d⁻⁴`/`d⁻⁵`
competition is derived from. **The remaining objection is internal to
MULTING, not to the floor.**

## 7. What this does NOT establish

1. **Linear theory only.** Non-linear collapse, redshift-space effects and
   the actual selection of a cluster sample are not modelled. A real
   measurement's floor is not identical to `delta_bar(r)`.
2. **No BAO wiggles.** Both transfer functions are smooth
   (BBKS+Sugiyama, EH98 no-wiggle). The BAO feature sits near
   `100–150 Mpc` — the region of interest — and could in principle
   introduce a local sign structure in `ξ` that a smooth spectrum misses.
   `[UNKNOWN]`; the `delta_bar` integral is however heavily weighted to
   small `r`, where the wiggle is irrelevant.
3. **Not a claim that no astrophysical reversal exists** — only that
   *compensation* does not produce one. Other mechanisms (selection,
   sample definition, redshift-space distortion) are untested here.
4. **Nothing about MULTING's correctness** (`NO_AUTHOR_ERROR`).
