# ξ₂ computed without simulations — and a forecast that says the measurement will not separate the three structures

**Date:** 2026-08-10 · supplies item 2 of the shopping list in
`FINDING_quadrupole_channel_kernels.md`
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `xi2_from_correlation_function.py`, ruff clean

---

## 1. No simulation is needed at leading order

The density around halo A, given a companion B at separation `r`, is at leading
(Gaussian) order the sum of the two individual correlation contributions:

```
<delta(x) | A at 0, B at r>  =  b [ xi(|x|) + xi(|x - r|) ]  +  (connected 3pt)
```

The first term is isotropic about A and contributes only to `ℓ = 0`. **The entire
quadrupole comes from the second term**, which is a known function of the measured
`ξ`. So `ξ₂` follows from `ξ₀` by projection, with no simulation anywhere:

```
xi_l(s | r) = (2l+1)/2 * int_-1^1 xi( sqrt(s^2 + r^2 - 2 s r u) ) P_l(u) du
```

This is the leading term of the hierarchy, not the whole answer. The connected
three-point function adds a correction this calculation does not contain **and
cannot bound** — the one real limitation of the result.

## 2. Control, and the error it caught in itself

Expanding the projection for `s ≪ r` gives analytically
`ξ₂ → (s²/3)[ξ″(r) − ξ′(r)/r]`. Tested on a power-law `ξ = A xⁿ`, where the
derivatives are exact:

| n | r | s | numeric | analytic | ratio |
|---:|---:|---:|---:|---:|---:|
| −1.8 | 60 | 1 | 7.2301e−06 | 7.2295e−06 | 1.0001 |
| −1.8 | 120 | 3 | 4.6722e−06 | 4.6713e−06 | 1.0002 |
| −2.5 | 60 | 3 | 1.8827e−05 | 1.8794e−05 | 1.0017 |
| −2.5 | 120 | 1 | 9.2291e−08 | 9.2287e−08 | 1.0000 |

**Passes to 0.02–0.17 %**, testing quadrature, Legendre convention and geometry at once.

*A first version of this control failed — and the failure was in the control.* It
differenced the **measured** `ξ` to get `ξ″`, but the data are sampled every ~7.4 Mpc
and interpolated linearly, so a second derivative taken with `h = 2` Mpc reads the
interpolant's own kinks rather than the correlation function's curvature. A control
must test the machinery against a known answer; supplying that answer analytically
removes the data's smoothness from the test.

## 3. ξ₂, and the moment the kernels need

`ξ₂` is positive and rises steeply toward `s → r` — the quadrupole of the pair
environment is dominated by matter near the companion, as it must be:

| `s/r` | r=50 | r=100 | r=200 |
|---:|---:|---:|---:|
| 0.10 | 2.75e−03 | 2.95e−04 | −4.02e−07 |
| 0.50 | 6.91e−02 | 1.35e−02 | 1.37e−03 |
| 0.90 | 2.91e−01 | 7.83e−02 | 1.58e−02 |
| 0.99 | 3.88e−01 | 1.19e−01 | 3.24e−02 |

The `ℓ = 2` channel needs two moments, `I₃ = ∫ξ₂s³ds` (the `k·m` tier) and
`I₂ = ∫ξ₂s⁴ds` (the mass tier). Their ratio is an effective radius, and the
fractional size of the dipole correction is `ℓ_d/⟨a⟩`:

| r [Mpc] | ⟨a⟩ [Mpc] | ℓ_d giving a 10 % effect |
|---:|---:|---:|
| 50 | 43.5 | 4.3 |
| 100 | 88.5 | 8.8 |
| 200 | 181.8 | 18.2 |

**`⟨a⟩ ≈ 0.9r`.** And it is robust — recomputed at r = 100 Mpc under every
extrapolation the data force on us:

| variant | ⟨a⟩ [Mpc] |
|---|---:|
| baseline (`ξ ~ s^−1.8` below 3.7 Mpc, zero above 230) | 88.48 |
| steeper small-scale `ξ ~ s^−2.2` | 87.80 |
| flat below the first data point | 88.10 |
| `ξ` truncated at 150 Mpc | 88.70 |
| `ξ` kept to 262 Mpc including the noisy tail | 88.48 |

**Stable to under 1 %.** The forecast below therefore does not rest on any
unmeasured part of `ξ` — which was the main thing that could have invalidated it.

## 4. The forecast, and it is discouraging

The measured monopole (ACT DR6, 15 bins, 25–225 Mpc) has total amplitude
**S/N = 7.52**, i.e. 13.3 % fractional precision. A quadrupole measurement is
generally weaker than the monopole, so treat S/N ≤ 5 as the realistic range.

`σ(ℓ_d) = ⟨a⟩ / (S/N of the quadrupole)`, in Mpc:

| r [Mpc] | S/N=2 | S/N=5 | S/N=10 | S/N=20 |
|---:|---:|---:|---:|---:|
| 50 | 21.7 | 8.7 | 4.3 | 2.2 |
| 100 | 44.2 | 17.7 | 8.8 | 4.4 |
| 200 | 90.9 | 36.4 | 18.2 | 9.1 |

Now the separation power. The three structures predict `ℓ_q²/ℓ_d² =` **0.375**
(two-charge), **2** (single-field), **4** (AI-fitted β), and they enter the `ℓ=2`
model only through `ℓ_d − 4ℓ_q²/r`. At r = 100 Mpc:

| structure | at `ℓ_d = 5` Mpc | at `ℓ_d = 20` Mpc |
|---|---:|---:|
| two-charge | +4.62 | +14.00 |
| single-field | +3.00 | −12.00 |
| AI-fitted | +1.00 | −44.00 |

> **For `ℓ_d ~ 5` Mpc the three differ by under 1 Mpc — far inside every σ in the
> table above. The quadrupole channel constrains the combination, and separates the
> three structures only for `ℓ_d ≳ 20` Mpc.**

## Verdict

```
xi_2 from the correlation function     : COMPUTED, no simulation needed at leading order
Control vs analytic small-s limit      : PASSED, 0.02-0.17 %
<a> = I2/I3                            : ~0.9 r, stable to <1 % across every
                                         extrapolation the data force
Measured monopole S/N                  : 7.52 (13.3 % amplitude precision)
Forecast sigma(ell_d)                  : <a>/(S/N); 17.7 Mpc at r=100, S/N=5
Separation of the three structures     : ONLY for ell_d >~ 20 Mpc. Below that the
                                         predictions differ by < 1 Mpc, well inside
                                         any plausible error.
Omitted and unbounded                  : the connected three-point function
```

## What this means for the plan

The theory side of the quadrupole test is now complete — kernels, `ξ₂`, and a
forecast. The forecast says the test is **not worth building** unless `ℓ_d` is large:

- if `ℓ_d ~ 5` Mpc (the scale the kSZ monopole fit weakly preferred, itself
  regulator-dependent and not to be trusted), the measurement cannot distinguish
  two-charge from AI-fitted, let alone from zero;
- it becomes decisive only for `ℓ_d ≳ 20` Mpc, which is also where the effect would
  already be a ≳ 20 % distortion of the monopole and hard to have missed.

This is a **negative forecast reported before the work, not after** — the point of
computing it. The honest recommendation is to stop pursuing pairwise kSZ as the
discriminator and look for an observable where the `k·k` tier is not suppressed by
`ℓ_d/r` relative to the `k·m` tier, since that suppression is what collapses the
three predictions onto each other.
