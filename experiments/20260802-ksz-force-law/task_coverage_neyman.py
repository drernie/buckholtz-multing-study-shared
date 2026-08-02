"""Neyman construction for l_d — proper coverage calibration.

WHY THIS EXISTS
---------------
An earlier step calibrated q_0 = -2 ln [ L(l_d=0) / L(l_d_hat) ] on synthetic
nulls and then used that single threshold (3.508) to read off an upper limit.
That is wrong: q_0 answers "how unusual is this if l_d = 0", which is a
DETECTION statistic. A confidence interval needs the distribution of

    q_mu = -2 ln [ L(l_d=mu) / L(l_d_hat) ]

at EVERY tested mu, because that distribution changes with mu (boundary at
l_d >= 0, nonlinear template, finite sample). Here we build the Neyman belt:
for each mu on a grid, simulate under that mu, get the 95th percentile of
q_mu, and accept mu iff the observed q_mu is below its OWN threshold.

Speed: chi2 with the amplitude profiled out is a RATIONAL function of l_d.
With model(l) = u + l*v (u = -K2, v = K3):

    chi2(l) = pCp - (pCu + l*pCv)^2 / (uCu + 2 l uCv + l^2 vCv)

so each simulation needs only three matrix-vector products, not a refit.
That makes ~10^7 evaluations feasible.

Safety: NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION
L0: descriptive.
"""

from __future__ import annotations

import json
from pathlib import Path

import h5py
import numpy as np
from scipy.interpolate import interp1d

HERE = Path(__file__).resolve().parent / "artifacts"
H_LITTLE, R_MIN, R_MAX_INT = 0.677, 6.0, 400.0
S_MIN_FID = 2.0  # fiducial UV prescription — stated, not hidden
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


def build():
    d = np.loadtxt(HERE / "xi_zbin2.dat")
    xi = interp1d(d[:, 0] / H_LITTLE, d[:, 1], bounds_error=False, fill_value=0.0)
    with h5py.File(HERE / "dr6.hdf", "r") as f:
        pw = f["df_pw/block0_values"][:]
        cols = [c.decode() for c in f["df_pw/block0_items"][:]]
        cov = f["df_cov/block0_values"][:]
    r_all = pw[:, cols.index("r_mp")]
    p_all = pw[:, cols.index("ksz_curve")]
    m = (r_all >= 25) & (r_all <= 225)
    r, p = r_all[m], p_all[m]
    C = cov[np.ix_(m, m)]
    Ci = np.linalg.inv(C)
    k2, k3 = [], []
    for R in r:
        x = np.linspace(R_MIN, R, 30000)
        k2.append(np.trapezoid(xi(x) * x**2, x) / R**2)
        x = np.linspace(R_MIN, R_MAX_INT, 30000)
        keep = np.abs(x - R) >= S_MIN_FID
        k3.append(np.trapezoid(np.where(keep, xi(x) * x**2 * c3(x / R), 0.0), x) / R**3)
    return r, p, C, Ci, -np.array(k2), np.array(k3)


class Chi2:
    """chi2(l) with amplitude profiled — precomputed quadratic forms."""

    def __init__(self, Ci, u, v):
        self.Ci, self.u, self.v = Ci, u, v
        self.uCu = float(u @ Ci @ u)
        self.uCv = float(u @ Ci @ v)
        self.vCv = float(v @ Ci @ v)

    def bind(self, p):
        self.pCp = float(p @ self.Ci @ p)
        self.pCu = float(p @ self.Ci @ self.u)
        self.pCv = float(p @ self.Ci @ self.v)
        return self

    def __call__(self, ld):
        num = (self.pCu + ld * self.pCv) ** 2
        den = self.uCu + 2 * ld * self.uCv + ld**2 * self.vCv
        return self.pCp - num / den

    def amp(self, ld):
        return (self.pCu + ld * self.pCv) / (self.uCu + 2 * ld * self.uCv + ld**2 * self.vCv)


def q_of(ch: Chi2, mu: float, grid: np.ndarray) -> float:
    """q_mu = chi2(mu) - min_l chi2(l), l >= 0 (physical boundary)."""
    return float(ch(mu) - np.min(ch(grid)))


def main():
    r, p, C, Ci, u, v = build()
    grid = np.linspace(0.0, 400.0, 4001)  # l_d >= 0
    L = np.linalg.cholesky(C + 1e-12 * np.eye(len(p)))

    obs = Chi2(Ci, u, v).bind(p)
    l_hat = float(grid[np.argmin(obs(grid))])

    print("=" * 78)
    print("NEYMAN CONSTRUCTION for l_d   |   L0: descriptive")
    print(f"fiducial UV prescription: hard exclusion, s_min = {S_MIN_FID} Mpc")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION")
    print("=" * 78)
    print(f"\n  observed best fit l_d_hat = {l_hat:.2f} Mpc")

    # sanity: rational form must equal the direct chi2
    direct = float(p @ Ci @ p) - (p @ Ci @ (u + 5.0 * v)) ** 2 / (
        (u + 5.0 * v) @ Ci @ (u + 5.0 * v)
    )
    print(
        f"  [CONTROL] rational form vs direct chi2 at l=5: "
        f"{obs(5.0):.9f} vs {direct:.9f}  diff={abs(obs(5.0) - direct):.2e}"
    )

    n_sim = 4000
    mus = np.array([0.0, 2.5, 5.0, 7.5, 10.0, 12.5, 15.0, 17.5, 20.0, 25.0, 30.0])
    print(f"\n  injection grid: {len(mus)} points, {n_sim} simulations each")
    print(f"\n  {'mu':>6} {'amp_mu':>10} {'q95(mu)':>9} {'q_obs(mu)':>10} {'accept':>7}")

    rows = []
    accepted = []
    for mu in mus:
        amp_mu = obs.amp(mu)
        p_mu = amp_mu * (u + mu * v)  # data generated UNDER mu
        sim = Chi2(Ci, u, v)
        qs = np.empty(n_sim)
        for i in range(n_sim):
            sim.bind(p_mu + L @ RNG.standard_normal(len(p_mu)))
            qs[i] = q_of(sim, mu, grid)
        q95 = float(np.percentile(qs, 95))
        qob = q_of(obs, mu, grid)
        ok = qob <= q95
        if ok:
            accepted.append(mu)
        rows.append({"mu": float(mu), "q95": q95, "q_obs": qob, "accept": bool(ok)})
        print(f"  {mu:6.1f} {amp_mu:10.5f} {q95:9.3f} {qob:10.3f} {'YES' if ok else 'no':>7}")

    print("\n" + "-" * 78)
    if accepted:
        lo, hi = min(accepted), max(accepted)
        print(f"  95% Neyman interval (on the injected grid): l_d in [{lo:.1f}, {hi:.1f}] Mpc")
        print(f"  -> calibrated 95% UPPER LIMIT ~ {hi:.1f} Mpc (grid-resolution limited)")
    else:
        print("  no grid point accepted — widen the grid")
    print("\n  comparison of thresholds actually used:")
    print("    naive chi2_1                 3.841")
    print("    Chernoff mixture             2.706")
    print("    earlier null-only q_0 calib  3.508  <- WRONG object for an upper limit")
    print(
        f"    q95 range across mu grid     {min(x['q95'] for x in rows):.3f}"
        f" .. {max(x['q95'] for x in rows):.3f}"
    )
    print("-" * 78)

    (HERE / "neyman_coverage.json").write_text(
        json.dumps({"l_hat": l_hat, "s_min": S_MIN_FID, "n_sim": n_sim, "rows": rows}, indent=2)
    )


if __name__ == "__main__":
    main()
