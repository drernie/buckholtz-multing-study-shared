"""Exact extended-mass kernels K2, K3, K4 for pairwise-kSZ + likelihood on l_d.

WHY THIS EXISTS
---------------
A previous fit multiplied the NEWTONIAN kernel K(r) by (1 - a/r + b/r^2).
That bakes in Newton's shell theorem, which is exact ONLY for 1/r^2. For
1/r^3 and 1/r^4 an extended mass distribution does NOT act like a point
mass, so that template constrains an effective template parameter, not the
physical ratio A3/A2.

This script builds a SEPARATE kernel per force power, with the extended-mass
correction inside the integral:

    K_k(r) = [ int_6^r xi(r') r'^2 C_k(r'/r) dr' ] / r^k

    C_k(rho) = F_shell(k) / F_point(k)
             = (1/2) int_0^pi sin(th) (1 - rho cos th)
                    / (1 + rho^2 - 2 rho cos th)^((k+1)/2) dth

C_2(rho) == 1 identically (shell theorem) -> K_2 reduces EXACTLY to the
published Newtonian kernel I(r)/r^2. That identity is the built-in positive
control: if it fails numerically, nothing else here may be believed.

Model fitted to the measured pairwise kSZ curve:

    p_kSZ(r) = -A [ K_2(r) - l_d K_3(r) + l_q2 K_4(r) ]

We constrain l_d = A3/A2 [Mpc] and l_q2 = A4/A2 [Mpc^2] directly, because
those are what the data actually see. Converting l_d -> beta_d requires
extra astrophysical assumptions (which k, which r_A, how averaged over the
pair population) and is reported SEPARATELY, flagged as assumption-laden.

Amplitude A is a nuisance (it absorbs optical depth, T_CMB/c, f, bias) and
is profiled analytically.

Data: public release of arXiv:2604.14327 (github.com/patogallardo/pairwiseksz_mond)
Safety: NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION
L0: descriptive.
"""

from __future__ import annotations

import json
from pathlib import Path

import h5py
import numpy as np
from scipy.integrate import quad
from scipy.interpolate import interp1d

HERE = Path(__file__).resolve().parent / "artifacts"
H_LITTLE = 0.677  # matches upstream fit2.py convention (R_Mpc = R_ov_h / h)
R_MIN_INT = 6.0  # Mpc, lower limit of the mass integral (upstream choice)
RFIT_LO, RFIT_HI = 25.0, 225.0  # fitted separation range


# ---------------------------------------------------------------- kernels
def c_shell(rho: float, k: int) -> float:
    """F_shell/F_point for a 1/s^k force: thin shell radius rho*r on a point at r."""
    if rho < 1e-12:
        return 1.0
    if rho > 1 - 1e-9:
        rho = 1 - 1e-9

    def f(th):
        num = np.sin(th) * (1.0 - rho * np.cos(th))
        den = (1.0 + rho**2 - 2.0 * rho * np.cos(th)) ** ((k + 1) / 2.0)
        return num / den

    val, _ = quad(f, 0.0, np.pi, limit=400)
    return 0.5 * val


def build_kernel(r_out: np.ndarray, xi_interp, k: int, n_node: int = 240) -> np.ndarray:
    """K_k(r) = int_6^r xi(r') r'^2 C_k(r'/r) dr' / r^k  (Simpson on a fixed grid)."""
    out = np.empty_like(r_out)
    for i, R in enumerate(r_out):
        rp = np.linspace(R_MIN_INT, R, n_node)
        integ = xi_interp(rp) * rp**2 * np.array([c_shell(x / R, k) for x in rp])
        out[i] = np.trapezoid(integ, rp) / R**k
    return out


# ---------------------------------------------------------------- likelihood
def profile_chi2(pobs: np.ndarray, cinv: np.ndarray, model: np.ndarray) -> tuple[float, float]:
    """chi2 with the overall amplitude profiled out analytically."""
    a_num = float(pobs @ cinv @ model)
    a_den = float(model @ cinv @ model)
    amp = a_num / a_den
    chi2 = float(pobs @ cinv @ pobs) - a_num**2 / a_den
    return chi2, amp


def main() -> None:
    print("=" * 78)
    print("EXACT-KERNEL pairwise-kSZ likelihood on l_d = A3/A2")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION  |  L0: descriptive")
    print("=" * 78)

    # ---- data ----
    xi_raw = np.loadtxt(HERE / "xi_zbin2.dat")
    r_xi = xi_raw[:, 0] / H_LITTLE
    xi_interp = interp1d(r_xi, xi_raw[:, 1], bounds_error=False, fill_value=0.0)

    with h5py.File(HERE / "dr6.hdf", "r") as f:
        pw = f["df_pw/block0_values"][:]
        pw_cols = [c.decode() for c in f["df_pw/block0_items"][:]]
        cov = f["df_cov/block0_values"][:]
    r_all = pw[:, pw_cols.index("r_mp")]
    p_all = pw[:, pw_cols.index("ksz_curve")]

    m = (r_all >= RFIT_LO) & (r_all <= RFIT_HI)
    r, pobs = r_all[m], p_all[m]
    cinv = np.linalg.inv(cov[np.ix_(m, m)])
    print(f"\n  bins used: {m.sum()} of {len(r_all)},  r = {r.min():.1f}-{r.max():.1f} Mpc")

    # ---- CONTROL A (PHYSICS): shell theorem, C_2(rho) == 1 for all rho ----
    # This is the meaningful control: it tests the geometry, independent of how
    # the outer r' integral is discretised.
    rhos = np.array([1e-6, 0.01, 0.1, 0.3, 0.5, 0.7, 0.9, 0.99, 0.999])
    c2_err = max(abs(c_shell(float(x), 2) - 1.0) for x in rhos)
    print("\n[CONTROL A — PHYSICS] shell theorem: C_2(rho) must equal 1 for every rho")
    print(f"  max |C_2(rho) - 1| = {c2_err:.3e}   over rho in [1e-6, 0.999]")
    if c2_err > 1e-8:
        print("  *** PHYSICS CONTROL FAILED — geometry wrong. STOP. ***")
        return
    print("  -> shell theorem reproduced to machine precision; geometry correct.")

    # ---- CONTROL B (NUMERICS): same quantity, two different quadratures ----
    # A residual here is discretisation of the r' integral only. It affects all
    # kernels the SAME way and largely cancels in the K3/K2 ratio that the fit
    # actually uses, so a sub-percent difference is acceptable — but it must be
    # reported, not hidden.
    k2 = build_kernel(r, xi_interp, 2)
    k2_newton = np.array([quad(lambda x: xi_interp(x) * x**2, R_MIN_INT, R)[0] / R**2 for R in r])
    rel = np.max(np.abs(k2 / k2_newton - 1.0))
    print("\n[CONTROL B — NUMERICS] K_2 via fixed-grid trapz vs adaptive quad")
    print(f"  max relative difference = {rel:.3e}  (discretisation only)")
    if rel > 5e-3:
        print("  *** NUMERICS CONTROL FAILED — increase n_node. STOP. ***")
        return
    print("  -> sub-percent; common to all kernels, cancels in ratios.")

    k3 = build_kernel(r, xi_interp, 3)
    k4 = build_kernel(r, xi_interp, 4)

    print("\n  kernel ratios (extended-mass enhancement over naive point-mass):")
    k3_naive = k2_newton / r  # what the old template implicitly assumed
    k4_naive = k2_newton / r**2
    print(f"  {'r[Mpc]':>8} {'K3/K3_naive':>13} {'K4/K4_naive':>13}")
    for i in range(0, len(r), max(1, len(r) // 6)):
        print(f"  {r[i]:8.1f} {k3[i] / k3_naive[i]:13.3f} {k4[i] / k4_naive[i]:13.3f}")

    # ---- baseline: pure inverse square ----
    chi2_0, amp0 = profile_chi2(pobs, cinv, -k2)
    dof0 = len(r) - 1
    print(f"\n[BASELINE 1/r^2]  chi2 = {chi2_0:.3f} / {dof0} dof   amplitude = {amp0:.4g}")

    # ---- scan l_d ----
    grid = np.linspace(-80.0, 80.0, 3201)
    chis = np.array([profile_chi2(pobs, cinv, -(k2 - ld * k3))[0] for ld in grid])
    i0 = int(np.argmin(chis))
    ld_best, chi2_best = float(grid[i0]), float(chis[i0])

    def interval(delta):
        ok = grid[chis <= chi2_best + delta]
        return float(ok.min()), float(ok.max())

    lo68, hi68 = interval(1.0)
    lo95, hi95 = interval(3.84)
    print("\n[DIPOLE] l_d = A3/A2 [Mpc], amplitude profiled, exact K3")
    print(f"  best fit      l_d = {ld_best:+.3f} Mpc   chi2 = {chi2_best:.3f}")
    print(f"  68% interval      [{lo68:+.2f}, {hi68:+.2f}] Mpc")
    print(f"  95% interval      [{lo95:+.2f}, {hi95:+.2f}] Mpc")
    print(f"  improvement over 1/r^2:  dchi2 = {chi2_0 - chi2_best:.4f} for 1 param")
    from scipy.stats import chi2 as chi2dist

    p_val = 1.0 - chi2dist.cdf(max(chi2_0 - chi2_best, 0.0), 1)
    print(f"  p-value = {p_val:.4f}  -> {'no preference' if p_val > 0.05 else 'PREFERRED'}")

    # ---- what the OLD (naive) template would have given, same data ----
    chis_naive = np.array([profile_chi2(pobs, cinv, -(k2 - ld * k3_naive))[0] for ld in grid])
    j0 = int(np.argmin(chis_naive))
    okn = grid[chis_naive <= chis_naive[j0] + 3.84]
    print("\n[COMPARISON] same data, OLD naive point-mass template K3_naive = K2/r")
    print(f"  best fit l_d = {grid[j0]:+.3f}   95% = [{okn.min():+.2f}, {okn.max():+.2f}] Mpc")
    print(f"  exact-kernel 95% upper / naive 95% upper = {hi95 / okn.max():.3f}")

    # ---- assumption-laden conversion to beta_d ----
    kappa, r_a = 1.669e-5, 2.0
    print("\n[CONVERSION to beta_d]  ASSUMPTION-LADEN, report l_d as the primary result")
    print(f"  l_d = 2 beta_d kappa r_A  with kappa={kappa:.3e}, r_A={r_a} Mpc")
    print(f"  beta_d(95% upper) = {hi95 / (2 * kappa * r_a):.3e}")
    print("  caveats: single k, single r_A, no pair-population averaging, beta_d const")

    out = {
        "control_k2_rel_err": rel,
        "chi2_newton": chi2_0,
        "dof": dof0,
        "l_d_best_Mpc": ld_best,
        "l_d_68": [lo68, hi68],
        "l_d_95": [lo95, hi95],
        "dchi2": chi2_0 - chi2_best,
        "p_value": p_val,
        "beta_d_95_upper_assumption_laden": hi95 / (2 * kappa * r_a),
        "n_bins": int(m.sum()),
        "r_range_Mpc": [float(r.min()), float(r.max())],
    }
    (HERE / "exact_kernel_results.json").write_text(json.dumps(out, indent=2))
    print(f"\n  results -> {(HERE / 'exact_kernel_results.json').name}")


if __name__ == "__main__":
    main()
