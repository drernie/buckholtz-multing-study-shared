# FROZEN SPECIFICATION v1 — kSZ dipole upper limit

**Frozen 2026-08-02.** Every choice below is fixed. An implementation that
follows this document and reaches a different number indicates a real
discrepancy to be localised, not a different admissible model.

This is the input to **Blind B**. Expected values are deliberately absent.

Labels: NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0: descriptive

---

## 1. Data (public, unmodified)

Release accompanying arXiv:2604.14327.

| File | Content |
|---|---|
| `dr6.hdf` | pandas HDFStore. `df_pw/block0_values` + names in `df_pw/block0_items` (`.decode()`); columns `r_mp` (Mpc), `ksz_curve`. `df_cov/block0_values` 18×18. `bs_curves/block0_values` 1000×18 bootstrap |
| `xi_zbin2.dat` | Ross+2016 BOSS DR12 post-recon monopole; columns `R_ov_h` (Mpc/h), `xi`, `err_xi` |
| `covariances_sdss_g.txt` | 15×15 covariance of the convolved kernel g(r) |
| `sdss_g_sqrtg.csv` | g(r) on 15 separations |

## 2. Units — h enters exactly ONCE

```
adopted h                : 0.677
reported ell_d unit      : physical Mpc
xi coordinates as shipped: h^-1 Mpc  ->  divide by h at load, ONCE
pair separations r_mp    : already Mpc, no conversion
all integration limits   : physical Mpc
```

A dual-unit run (whole pipeline in h^-1 Mpc) must give the same physical
endpoint after conversion.

## 3. Kernel

Geometric factor for a 1/s^k force, thin shell radius r' acting on a point at R:

```
C_k(rho) = (1/2) integral_0^pi sin(t) (1 - rho cos t)
                 / (1 + rho^2 - 2 rho cos t)^((k+1)/2) dt,     rho = r'/R
```

Closed form for k = 3, valid on BOTH sides of rho = 1:

```
C_3(rho) = 1/(2(1-rho^2)) + ln|(1+rho)/(1-rho)| / (4 rho)
C_2(rho) = 1 for rho < 1, 0 for rho > 1        (shell theorem, exact)
```

Kernels:

```
K_k(R) = [ integral xi(r') r'^2 C_k(r'/R) dr' ] / R^k
```

**Mass at r' > R MUST be included.** For k = 3 the pole at rho = 1 is simple
and antisymmetric; one-sided truncation is logarithmically divergent, and the
integral exists only as a Cauchy principal value.

**K_4 is not computable this way** (double pole, no PV). The quadrupole is out
of scope for this specification.

## 4. UV prescription

Symmetric exclusion around the singularity:

```
exclude |r' - R| < eps,   eps = 0.05 Mpc        (approximates the PV)
```

This is a numerical regularisation of a singular integral, NOT a physical
model of small-scale structure. Its physical status is explicitly open.

## 5. Integration limits

```
r_lo = 6.0 Mpc        FIDUCIAL. This is an upstream convention, hard-coded in
                      export_sdss_pairwise_curve.py. It falls INSIDE a gap in
                      the xi data (first bin 3.69 Mpc, second 11.08 Mpc), so
                      the region around it rests on interpolation, not
                      measurement. Report the fiducial result AND a scan over
                      r_lo in [3.7, 11.1].
r_hi = 262.19 Mpc     full xi range; xi = 0 beyond (contribution of r' > r_hi
                      is < 0.01% of the kernel)
```

## 6. Estimator convention — pair-weighted, DERIVED not chosen

```
K_k^weighted(R) = [1/(1 + xi(R))] * K_k^raw(R)
```

Justification, not preference:

- Linear-theory mean pairwise velocity is
  `v12(r) = -(2/3) H a f r * xibar(r)/(1 + xi(r))`.
  The denominator normalises a CONDITIONAL mean: v12 is the velocity given
  that a pair exists at separation r, and the number of such pairs is
  proportional to (1 + xi(r)).
- `export_sdss_pairwise_curve.py` builds `g = [1/(1+xi)] I/r^2` as the TEMPLATE.
- `fit1.py:72` uses `delta = p_pw - p_sdss * amplitude`, i.e. `ksz_curve` is
  the DATA and `g` is the MODEL. The factor therefore lives in the template;
  applying it does not double-count.

`fit2.py` omits the factor. That is an incomplete model of v12 and is not used
here.

## 7. Interpolation

```
xi interpolation : cubic spline over the measured range
outside range    : xi = 0
```

## 8. Fit

```
model      : p_kSZ(R) = -A [ K_2(R) - ell_d K_3(R) ]
bins       : 15 bins, 25 <= r_mp <= 225 Mpc
covariance : shipped 18x18, sliced to the fitted bins
Hartlap    : alpha = (N - p - 2)/(N - 1), N = 1000, p = 15
amplitude A: nuisance, profiled ANALYTICALLY,
             A_hat(mu) = t^T C^-1 d / t^T C^-1 t,  t(mu) = -(K2 - mu K3)
parameter  : ell_d = A3/A2 in Mpc, domain ell_d >= 0
```

## 9. Statistic and coverage

One-sided, for an upper limit:

```
q~_mu = 0                        if mu_hat > mu
      = chi2(mu) - chi2(mu_hat)  if 0 <= mu_hat <= mu
```

`mu_hat` is the CONSTRAINED MLE, `argmin over mu >= 0`, not an unconstrained
minimum clipped afterwards.

Neyman construction:

```
mu grid, evaluation  : 0 .. 60 Mpc, step 0.05
mu grid, calibration : 0 .. 20 Mpc, step 0.1 near the crossing
sims per mu          : >= 12000 near the crossing
generation           : data drawn at ell_d = mu with A = A_hat(mu) from the
                       real data; also repeat with A_hat +- 1 sigma_A
threshold            : 95th percentile of q~_mu AT EACH mu separately
endpoint             : INTERPOLATE the zero crossing of q95(mu) - q_obs(mu);
                       do not take the last accepted grid point
coverage validation  : an ensemble SEPARATE from the calibration one
seed                 : implementer's choice, must be reported
```

## 10. What to report

1. K_2(100) and K_3(100).
2. Constrained best fit `ell_d_hat`.
3. Calibrated 95% upper limit at the fiducial `r_lo = 6 Mpc`.
4. The same limit scanned over `r_lo` in [3.7, 11.1].
5. Coverage on the independent validation ensemble, with MC uncertainty.
6. Delta chi2 and p-value for adding the 1/s^3 term.
7. Result of the dual-unit run.
8. Any point where this specification is ambiguous, under-determined, or
   internally inconsistent — that finding outranks any number.

## 11. Known open issues, stated so they are not rediscovered as errors

- The physical status of the PV prescription is OPEN. It is mathematically
  canonical for this singular integral; whether the physics instead requires
  halo exclusion, a finite-size convolution, softening, or a form factor is
  not established. It is also unfixed whether the symmetric removal should be
  in |r'-R|, in |s|, or in dimensionless rho — the Jacobian makes these differ
  at finite eps.
- `r_lo` is a MODEL-SUPPORT UNCERTAINTY, not an ordinary numerical systematic,
  because it sits in a gap in the data. It must NOT be conflated with eps.
- No cross-covariance between the kSZ data vector and xi is available; their
  independence is assumed, not verified.
