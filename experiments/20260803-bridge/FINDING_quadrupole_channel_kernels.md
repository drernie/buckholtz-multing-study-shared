# The quadrupole channel: exact kernels, finite at contact — and the data that are missing

**Date:** 2026-08-10 · follows `FINDING_dipole_shell_is_a_double_layer.md`, which killed
the isotropic route and named the anisotropic one
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Verification:** closed form reproduces all 12 numerical test points exactly; positive
control passes

---

## 1. Exact closed form for the dipole layer in every anisotropy channel

A shell of radius `a` carrying radially-aligned dipole density with angular weight
`P_ℓ(cos θ)`, evaluated at `r > a`:

```
Phi_l(r) = [2l/(2l+1)] * tau_l * (a/r)^(l+1) / a
```

Differentiating gives the shell factors the two k-tiers need — the force on a
**monopole** (the `k·m` tier) and on a **dipole** (the `k·k` tier):

```
C3_l(rho) = [2 l (l+1)     /(2l+1)] rho^(l+1)
C4_l(rho) = [2 l (l+1)(l+2)/(2l+1)] rho^(l+1)          rho = a/r
```

**Positive control**, run first: the same integral for a *monopole* layer returns
exterior potentials in the ratio `2^(ℓ+1)` across `ℓ = 0…4` — the textbook exterior
multipole. Geometry and quadrature are therefore correct, so what follows is physics.

Verified against numerics at `ℓ = 1…4` × `ρ = 0.2, 0.5, 0.9`: **every entry matches
to 6 decimal places**, potential and force alike.

## 2. Why this reopens the route

| `ℓ` | `C₃^ℓ(1)` | `C₄^ℓ(1)` |
|---:|---:|---:|
| 0 | **0** | **0** |
| 1 | 1.3333 | 4.0000 |
| **2** | **2.4000** | **9.6000** |
| 3 | 3.4286 | 17.1429 |
| 4 | 4.4444 | 26.6667 |

`ℓ = 0` vanishes for both — that is the double layer of the previous finding,
recovered here as a special case rather than assumed. **Every `ℓ ≥ 1` is finite and
non-zero, and finite *at contact*.** The old isotropic `C₃(ρ) ~ (1−ρ)⁻¹` diverged
there and had to be regulated by hand; `C₃^{ℓ=2}(1) = 2.4` needs no regulator at all.

So the anisotropic channel is not merely non-zero — it is the channel in which the
calculation is **well-posed**.

## 3. The quadrupole-channel kernels

With `ξ₂(r')` the quadrupolar component of the matter distribution around the pair:

```
K2_2(r) = int xi_2(r') r'^2 (r'/r)^2 dr' / r^2      [mass tier, standard]
K3_2(r) = 2.4 int xi_2(r') r'^5 dr' / r^6           [k.m tier]
K4_2(r) = 9.6 int xi_2(r') r'^5 dr' / r^7           [k.k tier]
```

**A structural result worth stating separately:** `K₄₂ / K₃₂ = 4/r` **exactly**. The
two k-tiers share one and the same radial integral and differ only by a power of `r`.
The model therefore collapses to a single k-sector shape with a linear modulation:

```
p^(2)(r)  ∝  K2_2(r)  -  [2.4 I(r)/r^6] * ( ell_d  -  4 ell_q^2 / r ) ,
        I(r) = int_6^r xi_2(r') r'^5 dr'
```

`ℓ_d` and `ℓ_q²` are separable over a finite `r` range (one enters flat, the other as
`1/r`) but **strongly anti-correlated**, so any constraint on `ℓ_q²/ℓ_d²` from this
channel will be a degenerate ellipse, not two independent numbers. Worth knowing
before the measurement rather than after.

*Caveat on the `4/r`:* it assumes the `k·k` tier is weighted by the same `ξ₂` as the
`k·m` tier. The `k·k` tier is sourced by the **k-density**, not the mass density, so
the two coincide only if `k/m` does not vary with environment. Untested.

## 4. What is missing, checked rather than assumed

Both data products the calculation needs are absent from the repository:

- **The measured quadrupole.** `dr6.hdf` was enumerated: `df_pw` carries
  `['cdT', 'c2', 'r_mp_over_h', 'ksz_curve', 'r_mp']` — `ksz_curve` is the
  **monopole** of the pairwise velocity. There is no `ℓ = 2` measurement, and the
  18×18 covariance is the monopole's.
- **`ξ₂(r')`.** Only the isotropic `ξ(r)` is present (`xi_zbin2.dat`). The
  quadrupolar component of the pair environment would come from simulations or from
  the anisotropic correlation function.

Only the **shape** of `ξ₂` is needed, not its amplitude — the amplitude is degenerate
with the profiled overall amplitude. That is a weaker requirement than it first
appears, but it is still data this repository does not have.

## Verdict

```
Closed-form shell factors, all l       : DERIVED and verified exactly (12/12 points)
Positive control (monopole layer)      : PASSED, ratios 2^(l+1) across l = 0..4
l = 0                                  : 0 -- the double layer, recovered not assumed
l >= 1                                 : finite, non-zero, FINITE AT CONTACT
                                         -> no regulator needed anywhere
Quadrupole channel (l = 2)             : C3 = 2.4 rho^3, C4 = 9.6 rho^3
Kernels                                : K3_2 = 2.4 I(r)/r^6, K4_2 = 9.6 I(r)/r^7
New degeneracy found                   : K4_2/K3_2 = 4/r exactly -- one shape, not two;
                                         ell_d and ell_q^2 anti-correlated by construction
Measurement                            : NOT POSSIBLE HERE. dr6.hdf has only the
                                         monopole; xi_2 is absent. Verified by
                                         enumerating the file, not assumed.
```

## What this does NOT establish

1. No constraint on `ℓ_q²/ℓ_d²` is obtained. The three candidate values — 1.2247
   (two-charge), 2.8284 (single-field), 4.0 (AI fit) — remain unseparated.
2. The kernels are derived for radially-aligned dipoles, the configuration the
   two-charge construction derived from `F_d`'s A↔B symmetry. The intrinsic-random
   branch would need its own calculation.
3. `ℓ = 2` was computed because it is the leading anisotropy an actual pairwise
   estimator measures; nothing here shows it is the *largest* k-sector channel —
   `C₃^ℓ(1)` grows with `ℓ`, so higher multipoles couple more strongly per unit
   `ξ_ℓ`, and whether that beats the fall-off of `ξ_ℓ` is not computed.

## The concrete shopping list

The theory side of the quadrupole test is now complete. To close it:

1. a measured **quadrupole of the pairwise velocity field** with its covariance —
   the ACT DR6 pairwise pipeline produces the monopole, so this is a re-analysis of
   existing maps rather than new observations;
2. the **shape** of `ξ₂(r')` between 6 and 225 Mpc, from simulations or the
   anisotropic correlation function;
3. then fit `K₂₂ − (2.4 I/r⁶)(ℓ_d − 4ℓ_q²/r)`, expecting a degenerate ellipse in
   `(ℓ_d, ℓ_q²)` rather than two clean numbers.
