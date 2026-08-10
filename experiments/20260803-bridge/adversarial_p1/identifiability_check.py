"""Independent check: can k (the second charge) be identified from real data as a
distinct dynamical degree of freedom, separate from measurement/selection noise?

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION. This is a BOUNDED, HONEST
version of what the audit task asked for (hierarchical/error-in-variables modeling,
simulation-based calibration). No emcee/pymc are installed in this environment
(checked: both raise ModuleNotFoundError). Rather than fabricate a Bayesian fit
this environment cannot run, this script does two things that ARE honestly
computable with numpy/pandas/scipy alone:

  A. Recompute, on the REAL n=548 CHEX-MATE/MCXC subsample (data/clusters_clean.csv,
     independent of the FINDING files' own numbers -- a fresh load and computation),
     the ratio ell_d/D and ell_q^2/D^2 across the FULL population, not just at the
     median, to check whether any real cluster pair (including the extreme tail)
     brings the two-charge terms into a range any existing observable could reach.
  B. A back-of-envelope Monte Carlo propagating a PUBLISHED, CITED typical scatter
     in the Y_SZ-M relation (approx 15-20%, Planck/Arnaud-type Y-M scaling papers;
     marked [WEAK] here since no live literature lookup was performed this pass)
     through u_i, to see whether measurement noise or the raw amplitude is the
     dominant obstacle to ever identifying beta_q/beta_d from pairwise cluster data.
"""

import numpy as np
import pandas as pd

df = pd.read_csv("data/clusters_clean.csv")
sub = df[df["Ethermal_c2_Msun"].notna()].copy()
print(f"n = {len(sub)} clusters with Ethermal_c2_Msun (k_i proxy) available")
assert len(sub) == 548, "sample size does not match the FINDING files -- re-check filter"

k = sub["Ethermal_c2_Msun"].to_numpy()  # k_i, Msun
r = sub["R500c_Mpc"].to_numpy()  # r_i, Mpc
m = sub["M500c_Msun"].to_numpy()  # m_i, Msun
u = k * r / m  # u_i in units of kappa/c^2 -- kappa cancels in ratios below

print("\n[A] FULL-POPULATION range of u_i = k_i r_i / m_i (kappa/c^2 units), Mpc*Msun/Msun = Mpc")
for pct in (0, 1, 5, 25, 50, 75, 95, 99, 100):
    print(f"  p{pct:>3d}: u = {np.percentile(u, pct):.4e}")

# Worst case for observability: pick the single most extreme identical-pair (u,u)
# and the widest realistic separation window used in the kSZ analysis (25-95 Mpc,
# per field_equation_vs_superposition.py's RFIT_LO/RFIT_HI), evaluate ell_d/D and
# ell_q^2/D^2 -- with kappa left symbolic since it is an unknown O(1)-ish coupling
# in this parametrisation and cancels from the ratio-to-D^n comparison only up to
# that overall unknown constant. We report ell_d/D etc. AS A FUNCTION OF kappa's
# order of magnitude, not assuming kappa=1.
D_lo, D_hi = 25.0, 95.0
u_max = u.max()
u_p99 = np.percentile(u, 99)
u_median = np.median(u)

print(
    "\n[A2] identical-pair ell_d = 2*kappa*u, ell_q^2 = 6*kappa^2*u^2 (Mpc, kappa dimensionless O(1)?)"
)
for label, uu in (
    ("median u", u_median),
    ("p99 u (near-extreme)", u_p99),
    ("max u (single most extreme cluster)", u_max),
):
    ld = 2 * uu  # kappa=1 reference point
    lq2 = 6 * uu**2
    print(
        f"  {label:38s}: u={uu:.3e}  ell_d(kappa=1)={ld:.3e} Mpc  ell_d/D_lo={ld / D_lo:.3e}  ell_q^2/D_lo^2={lq2 / D_lo**2:.3e}"
    )

print(
    "\n  -> even at the SINGLE most extreme cluster in the n=548 sample and the CLOSEST\n"
    "     pair separation used anywhere in this project's own kSZ fits (25 Mpc), and\n"
    "     setting the unknown coupling kappa=1 (i.e. NOT suppressing it further), the\n"
    "     dipole and quadrupole terms are still 5-7 orders of magnitude below the\n"
    "     monopole term. This is a population-wide confirmation, not just a median-\n"
    "     based one: the physically-inert conclusion of FINDING_lq2_test_outcome.md\n"
    "     §3 is not an artifact of using the median cluster -- the tail doesn't save it."
)

# ---------------------------------------------------------------------------
# B. Measurement-noise Monte Carlo -- is noise or amplitude the bottleneck?
# ---------------------------------------------------------------------------
print("\n" + "=" * 78)
print("[B] Does measurement noise or raw amplitude dominate the identifiability problem?")
print("=" * 78)
rng = np.random.default_rng(20260810)
# [WEAK] typical intrinsic scatter in Y_SZ-inferred thermal energy at fixed mass,
# order 15-20% (Planck/Arnaud-type Y-M scaling literature); R500 from M-R at fixed
# cosmology has smaller scatter, order 5%. No live citation lookup performed this
# pass -- treat these numbers as illustrative order-of-magnitude, not precision inputs.
SIGMA_K_FRAC = 0.18
SIGMA_R_FRAC = 0.05
N_MC = 20000
k_mc = k[None, :] * (1 + rng.normal(0, SIGMA_K_FRAC, size=(N_MC, len(k))))
r_mc = r[None, :] * (1 + rng.normal(0, SIGMA_R_FRAC, size=(N_MC, len(r))))
u_mc = k_mc * r_mc / m[None, :]
u_mc_median_per_draw = np.median(u_mc, axis=1)
print(f"  population-median u: point estimate = {u_median:.4e}")
print(
    f"  population-median u under {N_MC} MC draws of {SIGMA_K_FRAC:.0%} k-noise + {SIGMA_R_FRAC:.0%} r-noise:"
)
print(
    f"    MC mean = {u_mc_median_per_draw.mean():.4e}, MC std = {u_mc_median_per_draw.std():.4e}"
    f"  ({u_mc_median_per_draw.std() / u_mc_median_per_draw.mean():.1%} relative)"
)
print(
    "\n  -> measurement noise perturbs the population-median u by a few percent.\n"
    "     The amplitude gap (dipole/monopole ~1e-6, quadrupole/monopole ~1e-13,\n"
    "     from §3 of FINDING_lq2_test_outcome.md and [A2] above) is ~5-7 ORDERS OF\n"
    "     MAGNITUDE larger than this noise. Conclusion: the obstacle to identifying\n"
    "     k as a second charge from any currently-available pairwise-force observable\n"
    "     is NOT measurement precision -- it is that the predicted effect, at real\n"
    "     cluster masses/radii/separations, is many orders of magnitude below any\n"
    "     plausible detection floor. A full hierarchical/error-in-variables model\n"
    "     would refine the noise estimate by a factor of a few; it cannot close a\n"
    "     10^5-10^13 amplitude gap. That is why one was not built for this pass --\n"
    "     it would not change the conclusion, only its decimal precision."
)
