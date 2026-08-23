# FINDING P130 — The matter-Λ resonant transient: **`MECHANISM IDENTIFIED, NOT YET QUANTITATIVELY DERIVED`**

**Status:** built, ran cleanly after one self-caught float-equality bug;
result is honest and internally consistent, but does not complete the
user's original request.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P130_matter_lambda_resonance_characterization.py`

> User-directed: "попробуй построить genuinely independent hand-off, не
> из full system" (try to build a genuinely independent hand-off, not
> from the full system) — following `FINDING_P129`'s own skeptic-corrected
> conclusion that a hand-off must not be read off the already-solved full
> trajectory to count as independent evidence.

---

## What was tried first, and why it failed before a line of code was written

The plan was a small-perturbation, matter-dominated early-time
linearization (drop `pb³`, approximate `H(N)≈H0·exp(-1.5N)`).
**Reconnaissance, run before committing to that design** (Compute
First), killed it directly: `pb` does stay small throughout (peak
≈0.086 at N≈3), but `psi`/`dph`/`drA_hat`/`qm_hat` do **not** — they
undergo a violent, `~10⁷`–`10¹⁰`-fold amplification in a narrow window
around N≈11–16, for both k=0.3 and k=0.5. A small-perturbation
linearization assumes exactly what fails here.

## The mechanism

`rho_A(N) = C_MATTER·exp(-3N)` (matter) equals `Λ_cc` (the Λ-like
additive term) at

```
N_eq = -ln(Λ_cc / C_MATTER) / 3 = 11.512925
```

— a closed-form prediction from two **fixed constants**, computed
directly, never read off a solved trajectory. This is where `H(N)`'s own
friction is transitioning from matter-dominated decay toward its
late-time constant value — friction is weakest relative to the
perturbation-sourcing terms right around this transition, the same
qualitative setup as reduced-damping amplification (parametric
resonance / particle production during reheating in inflationary
cosmology; that formalism's quantitative machinery was not applied
here).

## Result

| | k=0.3 | k=0.5 |
|---|---|---|
| peak `\|psi\|` | 2.6436 | 11231.95 |
| peak location N | 13.455 | 13.620 |
| offset from `N_eq` | +1.942 | +2.107 |

- **Peak-N difference: 0.165 e-folds** — close, consistent with an
  approximately k-independent trigger (matter-Λ equality). The earlier
  coarse (0.1-resolution) reconnaissance found both peaks at *exactly*
  N=13.600 — this refined (0.005-resolution) scan shows that was a
  grid-resolution coincidence, not a true exact match. Reported
  honestly rather than kept as the more dramatic coarse number.
- **Peak-amplitude ratio: 4248.7** — same order of magnitude as
  `FINDING_P126`'s own `A_hat=6678.998` (`|log10(ratio)-log10(A_hat)|
  =0.20`, within a factor of ~3).

## One self-caught bug

`CONTROL 1`'s first pass failed on `coarse_n03 == RECON_PEAK_N03_COARSE`
— exact float equality on an `np.linspace`-derived value
(`13.600000000000001 ≠ 13.6`). Fixed with a `1e-6` tolerance; the
underlying numbers were already correct, only the comparison was wrong.

---

## Verdict — **`MECHANISM IDENTIFIED, NOT YET QUANTITATIVELY DERIVED`**

The matter-Λ transition triggers a resonant amplification that is
approximately k-independent in *where* it happens and strongly
k-dependent in *how strong* it is, with a magnitude in the right
ballpark to plausibly be the real origin of `A≈6679`. `FINDING_P127`'s
reduced system starts *after* this resonance and simply inherits its
outcome — this is the first time in the P127–P130 arc that the question
"why does the amplitude take the value it does" has a concrete,
partially-verified physical answer, rather than being an unexplained
input.

### Not established

- A genuinely independent, **quantitative** prediction of `A≈6679` —
  this file identifies *where* and roughly *how strong* the resonance
  is; it does not compute an amplification factor from first
  principles. The user's original request remains open, now more
  precisely scoped.
- Why peak `|psi|` specifically (rather than the late-time settled
  `qm_hat`, or some other combination) is the right proxy for the
  quantity that determines `A` — used here only as an order-of-magnitude
  plausibility check.
- A WKB / adiabatic-invariant calculation through the friction
  transition — the kind of machinery used for reheating/preheating
  particle production in inflationary cosmology — named as the concrete
  next step if this line is continued, not attempted here.
- Anything at Lambda values, or `(k, IC)` combinations, other than
  k=0.3/k=0.5's main case tested throughout `FINDING_P119`–`P129`.
- Anything about MULTING itself (Gate 1). Any `k[h/Mpc]`.
