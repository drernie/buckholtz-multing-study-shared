# Specification given to Blind A — verbatim

Recorded so the experiment can be judged on what it was actually asked.
Four decisions were DELIBERATELY left open: whether to include mass at r' > R,
which UV prescription to use, where to truncate, and which pair-weighting
convention to adopt. That is why this run measures analyst variation rather
than reproducibility.

## Data given (isolated directory, data only — no code, no results)

- `dr6.hdf` — pandas HDFStore; `df_pw/block0_values` (+ column names in
  `df_pw/block0_items`, needing `.decode()`), columns `r_mp` (Mpc) and
  `ksz_curve`; `df_cov/block0_values` 18x18 covariance; `bs_curves/block0_values`
  1000 bootstrap realisations.
- `xi_zbin2.dat` — Ross+2016 BOSS DR12 post-recon monopole; `R_ov_h` (Mpc/h),
  `xi`, `err_xi`; h = 0.677.
- `covariances_sdss_g.txt` — 15x15 covariance of the convolved kernel g(r).
- `sdss_g_sqrtg.csv` — g(r) on 15 separations.

Source: public release accompanying arXiv:2604.14327.

## Model specified

Force `F(s) = A2/s^2 - A3/s^3 + A4/s^4`. Target `ell_d = A3/A2` in Mpc.
Physical prior `ell_d >= 0`.

Geometric factor given as an INTEGRAL (closed form deliberately withheld):

    C_k(rho) = (1/2) int_0^pi sin(t) (1 - rho cos t)
                    / (1 + rho^2 - 2 rho cos t)^((k+1)/2) dt,   rho = r'/R

    K_k(R) = [ int xi(r') r'^2 C_k(r'/R) dr' ] / R^k

Lower limit 6 Mpc (upstream). **Upper limit and whether to include r' > R were
left to the agent to decide and justify.**

Fit over 25-225 Mpc:  `p_kSZ(R) = -A [ K2(R) - ell_d K3(R) ]`, A a nuisance
amplitude to be profiled, full covariance inverted over fitted bins only.

## Convention ambiguity flagged, resolution NOT given

Told that one upstream script uses `g(r) = [1/(1+xi(r))] I(r)/r^2` and another
omits the factor; asked to compute both, report both, and say which it would
adopt and why.

## Mandatory checks requested (design left to the agent)

1. A physics control on the kernel — identify the exact analytic statement that
   exists for one specific k, verify numerically, report the residual.
2. Convergence over at least two decades of integration nodes; characterise any
   failure rather than picking a stable-looking grid.
3. Coverage: a boundary parameter cannot use a naive chi2_1 threshold —
   calibrate against simulation, state which statistic and at which values.
4. xi uncertainty propagated using the correlation structure in the shipped
   covariance, not independent per-bin noise.

## What was NOT given

Our kernel values, our endpoints, our thresholds, our best-fit values, our
scripts, `docs/132`, or any indication of what we had found. The agent was told
explicitly that concluding "the specification is flawed" or "no bound can be
extracted this way" would be a more valuable finding than any number.
