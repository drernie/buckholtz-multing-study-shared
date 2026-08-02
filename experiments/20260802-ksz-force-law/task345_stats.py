"""TASKS 3-5 — one-sided bound with calibrated coverage, xi uncertainty, bin policy.

TASK 3. MULTING's dipole is REPULSIVE, so the physical prior is l_d >= 0.
  A two-sided interval is then not the right object, and on the boundary of the
  parameter space the naive chi2_1 threshold (3.84) does NOT have 95% coverage.
  Chernoff's theorem says the null distribution of the LRT statistic is the
  mixture 0.5*delta(0) + 0.5*chi2_1, whose 95th percentile is 2.71, not 3.84.
  We do not assume this — we CALIBRATE it on synthetic nulls drawn from the
  measured covariance and report the empirical threshold.

TASK 4. xi(r) is measured, not exact. Propagate its errors: redraw xi from its
  quoted per-bin errors, rebuild K2 and K3, refit. Report the DISTRIBUTION of
  the bound rather than one number.

TASK 5. Bin policy: the published 15-bin range vs all 18 bins vs leave-one-out.
  If the answer hinges on the innermost bins, that is expected — the UV model
  matters most there — and must be shown, not hidden.

Safety: NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION
L0: descriptive.
"""

from __future__ import annotations

from pathlib import Path

import h5py
import numpy as np
from scipy.interpolate import interp1d

HERE = Path(__file__).resolve().parent / "artifacts"
H_LITTLE, R_MIN, R_MAX_INT = 0.677, 6.0, 400.0
RNG = np.random.default_rng(20260802)


def c3(rho):
    rho = np.asarray(rho, float)
    o = np.empty_like(rho)
    s = np.abs(rho - 1) > 1e-12
    r = rho[s]
    o[s] = 1 / (2 * (1 - r**2)) + np.log(np.abs((1 + r) / (1 - r))) / (4 * r)
    o[~s] = 0.0
    o[rho < 1e-12] = 1.0
    return o


def kernels(xi, rvals, s_min=2.0, n=40000):
    k2, k3 = [], []
    for R in rvals:
        x = np.linspace(R_MIN, R, n)
        k2.append(np.trapezoid(xi(x) * x**2, x) / R**2)
        x = np.linspace(R_MIN, R_MAX_INT, n)
        keep = np.abs(x - R) >= s_min
        k3.append(np.trapezoid(np.where(keep, xi(x) * x**2 * c3(x / R), 0.0), x) / R**3)
    return np.array(k2), np.array(k3)


def chi2_of(pobs, cinv, model):
    a = float(pobs @ cinv @ model)
    b = float(model @ cinv @ model)
    return float(pobs @ cinv @ pobs) - a * a / b


def scan(pobs, cinv, k2, k3, grid):
    return np.array([chi2_of(pobs, cinv, -(k2 - ld * k3)) for ld in grid])


def main():
    d = np.loadtxt(HERE / "xi_zbin2.dat")
    r_xi, xi_c, xi_e = d[:, 0] / H_LITTLE, d[:, 1], d[:, 2]
    xi0 = interp1d(r_xi, xi_c, bounds_error=False, fill_value=0.0)

    with h5py.File(HERE / "dr6.hdf", "r") as f:
        pw = f["df_pw/block0_values"][:]
        cols = [c.decode() for c in f["df_pw/block0_items"][:]]
        cov_all = f["df_cov/block0_values"][:]
    r_all = pw[:, cols.index("r_mp")]
    p_all = pw[:, cols.index("ksz_curve")]

    grid = np.linspace(0.0, 300.0, 3001)  # one-sided: l_d >= 0

    def setup(mask):
        r, p = r_all[mask], p_all[mask]
        return r, p, np.linalg.inv(cov_all[np.ix_(mask, mask)])

    print("=" * 78)
    print("TASKS 3-5  |  L0: descriptive  |  NOT_VALIDATION - OUR_RECONSTRUCTION")
    print("=" * 78)

    m15 = (r_all >= 25) & (r_all <= 225)
    r, p, cinv = setup(m15)
    k2, k3 = kernels(xi0, r)

    # ---------------- TASK 3: calibrate the one-sided threshold ----------------
    print("\n[TASK 3] one-sided bound l_d >= 0, threshold CALIBRATED on synthetic nulls")
    a_null = float(p @ cinv @ (-k2)) / float((-k2) @ cinv @ (-k2))
    p_null = a_null * (-k2)  # best-fit pure-Newtonian model = the null hypothesis
    cov15 = cov_all[np.ix_(m15, m15)]
    L = np.linalg.cholesky(cov15 + 1e-12 * np.eye(cov15.shape[0]))

    n_sim = 2000
    qs = np.empty(n_sim)
    for i in range(n_sim):
        psim = p_null + L @ RNG.standard_normal(len(p_null))
        ch = scan(psim, cinv, k2, k3, grid)
        q = chi2_of(psim, cinv, -k2) - ch.min()
        qs[i] = max(q, 0.0)
    thr95 = float(np.percentile(qs, 95))
    frac0 = float(np.mean(qs < 1e-9))
    print(f"  simulations: {n_sim}")
    print(f"  P(q = 0) = {frac0:.3f}   (Chernoff predicts 0.5 for a boundary parameter)")
    print(f"  empirical 95th percentile of q = {thr95:.3f}")
    print("  naive chi2_1 threshold = 3.841   |   Chernoff mixture = 2.706")

    ch = scan(p, cinv, k2, k3, grid)
    qobs = chi2_of(p, cinv, -k2) - ch.min()
    for name, t in (("calibrated", thr95), ("Chernoff 2.706", 2.706), ("naive 3.841", 3.841)):
        ok = grid[ch <= ch.min() + t]
        print(f"  bound with {name:15s} threshold: l_d < {ok.max():6.2f} Mpc")
    print(f"  observed q = {qobs:.3f} -> {'no detection' if qobs < thr95 else 'DETECTION'}")

    # ---------------- TASK 4: propagate xi uncertainty ----------------
    print("\n[TASK 4] xi(r) uncertainty propagated (redraw from quoted per-bin errors)")
    bounds = []
    for _ in range(60):
        xi_s = interp1d(
            r_xi, xi_c + xi_e * RNG.standard_normal(len(xi_c)), bounds_error=False, fill_value=0.0
        )
        k2s, k3s = kernels(xi_s, r, n=8000)
        chs = scan(p, cinv, k2s, k3s, grid)
        bounds.append(grid[chs <= chs.min() + thr95].max())
    bounds = np.array(bounds)
    print(
        f"  60 realisations -> l_d bound: median {np.median(bounds):.2f}, "
        f"16-84% [{np.percentile(bounds, 16):.2f}, {np.percentile(bounds, 84):.2f}], "
        f"full [{bounds.min():.2f}, {bounds.max():.2f}] Mpc"
    )

    # ---------------- TASK 5: bin policy ----------------
    print("\n[TASK 5] bin policy")
    for lab, mask in (
        ("published 15 bins 25-225", m15),
        ("all bins", np.ones_like(m15, dtype=bool)),
        ("drop innermost", m15 & (r_all > r_all[m15].min())),
        ("drop outermost", m15 & (r_all < r_all[m15].max())),
    ):
        if mask.sum() < 4:
            continue
        rr, pp, ci = setup(mask)
        a, b = kernels(xi0, rr, n=8000)
        cc = scan(pp, ci, a, b, grid)
        print(
            f"  {lab:26s} n={int(mask.sum()):3d}  l_d < {grid[cc <= cc.min() + thr95].max():6.2f} Mpc"
        )

    print("\n  leave-one-bin-out (15-bin set):")
    idx = np.where(m15)[0]
    outs = []
    for j in idx:
        mk = m15.copy()
        mk[j] = False
        rr, pp, ci = setup(mk)
        a, b = kernels(xi0, rr, n=8000)
        cc = scan(pp, ci, a, b, grid)
        outs.append((r_all[j], grid[cc <= cc.min() + thr95].max()))
    lo = min(o[1] for o in outs)
    hi = max(o[1] for o in outs)
    worst = max(outs, key=lambda o: abs(o[1] - np.median([x[1] for x in outs])))
    print(
        f"    bound range {lo:.2f} .. {hi:.2f} Mpc   (most influential bin: r={worst[0]:.0f} Mpc)"
    )


if __name__ == "__main__":
    main()
