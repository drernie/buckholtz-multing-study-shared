"""GATE 1 — is the raw over-coverage a grid artefact, or real?

The raw endpoint came out at 11.00 Mpc with validation coverage
0.9605 +- 0.0031, i.e. 3.4 sigma above nominal 0.95. That is CONSERVATIVE
(interval too wide, not too narrow), but the stated explanation — "it is the
0.5 Mpc calibration grid" — was a HYPOTHESIS, never demonstrated.

This tests it:
  * mu step 0.5 -> 0.1 around the crossing
  * 12000 sims per mu near the crossing (vs 4000 before)
  * endpoint by INTERPOLATING q95(mu) - q_obs(mu) to its zero crossing,
    instead of taking the last accepted grid point
  * coverage re-validated on an INDEPENDENT ensemble at the refined endpoint

PASS: refined coverage within 3 sigma_MC of 0.95, and the endpoint shift is
      consistent with grid quantisation (<= half the old step, 0.25 Mpc).
FAIL: coverage stays high after refinement -> the over-coverage is a property
      of the statistic/boundary, not the grid, and must be reported as such.

Safety: NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION
L0: descriptive.
"""

from __future__ import annotations

import json
from pathlib import Path

import h5py
import numpy as np
from scipy.interpolate import CubicSpline

HERE = Path(__file__).resolve().parent / "artifacts"
H_LITTLE, R_LO, R_HI, EPS_PV = 0.677, 6.0, 262.19, 0.05
RNG = np.random.default_rng(20260802)
MU_GRID = np.arange(0.0, 60.0 + 1e-9, 0.05)


def c3(rho):
    rho = np.asarray(rho, float)
    out = np.zeros_like(rho)
    ok = np.abs(rho - 1.0) > 1e-14
    r = rho[ok]
    out[ok] = 1.0 / (2.0 * (1.0 - r**2)) + np.log(np.abs((1 + r) / (1 - r))) / (4.0 * r)
    out[rho < 1e-14] = 1.0
    return out


def load():
    d = np.loadtxt(HERE / "xi_zbin2.dat")
    r_xi, xi_v = d[:, 0] / H_LITTLE, d[:, 1]
    spl = CubicSpline(r_xi, xi_v, extrapolate=False)

    def xi(x):
        x = np.atleast_1d(np.asarray(x, float))
        y = spl(np.clip(x, r_xi[0], r_xi[-1]))
        y[(x < r_xi[0]) | (x > r_xi[-1])] = 0.0
        return np.nan_to_num(y)

    with h5py.File(HERE / "dr6.hdf", "r") as f:
        pw = f["df_pw/block0_values"][:]
        cols = [c.decode() for c in f["df_pw/block0_items"][:]]
        cov = f["df_cov/block0_values"][:]
        nb = f["bs_curves/block0_values"].shape[0]
    r_all = pw[:, cols.index("r_mp")]
    p_all = pw[:, cols.index("ksz_curve")]
    m = (r_all >= 25) & (r_all <= 225)
    return xi, r_all[m], p_all[m], cov[np.ix_(m, m)], nb


def kernels(xi, rvals, weighted, n=120000):
    k2, k3 = [], []
    for R in rvals:
        x = np.linspace(R_LO, R, n // 4)
        i2 = float(np.trapezoid(xi(x) * x**2, x) / R**2)
        x = np.linspace(R_LO, R_HI, n)
        keep = np.abs(x - R) >= EPS_PV
        i3 = float(np.trapezoid(np.where(keep, xi(x) * x**2 * c3(x / R), 0.0), x) / R**3)
        if weighted:
            w = 1.0 / (1.0 + float(xi(R)[0]))
            i2, i3 = i2 * w, i3 * w
        k2.append(i2)
        k3.append(i3)
    return np.array(k2), np.array(k3)


class Model:
    def __init__(self, Ci, k2, k3):
        self.Ci, self.u, self.v = Ci, -k2, k3
        self.uCu = float(self.u @ Ci @ self.u)
        self.uCv = float(self.u @ Ci @ self.v)
        self.vCv = float(self.v @ Ci @ self.v)

    def _p(self, d):
        return float(d @ self.Ci @ d), float(d @ self.Ci @ self.u), float(d @ self.Ci @ self.v)

    def q_grid(self, d):
        dCd, dCu, dCv = self._p(d)
        ch = dCd - (dCu + MU_GRID * dCv) ** 2 / (
            self.uCu + 2 * MU_GRID * self.uCv + MU_GRID**2 * self.vCv
        )
        i = int(np.argmin(ch))
        q = ch - ch[i]
        q[MU_GRID < MU_GRID[i]] = 0.0
        return q, float(MU_GRID[i])

    def amp(self, mu, d):
        _, dCu, dCv = self._p(d)
        return (dCu + mu * dCv) / (self.uCu + 2 * mu * self.uCv + mu**2 * self.vCv)


def main():
    xi, r, d_obs, C, nb = load()
    p_dim = len(r)
    Ci = np.linalg.inv(C) * ((nb - p_dim - 2) / (nb - 1))
    L = np.linalg.cholesky(C + 1e-14 * np.eye(p_dim))

    print("=" * 78)
    print("GATE 1 — fine-grid coverage regression (raw convention)")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    k2, k3 = kernels(xi, r, weighted=False)
    M = Model(Ci, k2, k3)
    q_obs, mu_hat = M.q_grid(d_obs)
    print(f"\n  raw convention, mu_hat = {mu_hat:.2f} Mpc")

    # fine scan around the previous crossing at 11.0
    mus = np.round(np.arange(9.0, 14.0 + 1e-9, 0.1), 2)
    n_sim = 12000
    print(f"  fine grid {mus[0]}..{mus[-1]} step 0.1, {n_sim} sims per point")
    print(f"\n  {'mu':>6} {'q95':>8} {'q_obs':>8} {'diff':>9} {'accept':>7}")

    rows = []
    for mu in mus:
        A = M.amp(mu, d_obs)
        base = A * (M.u + mu * M.v)
        j = int(np.argmin(np.abs(MU_GRID - mu)))
        qs = np.empty(n_sim)
        for i in range(n_sim):
            qs[i] = M.q_grid(base + L @ RNG.standard_normal(p_dim))[0][j]
        q95 = float(np.percentile(qs, 95))
        qo = float(q_obs[j])
        rows.append((float(mu), q95, qo))
        if abs(mu - round(mu * 2) / 2) < 1e-9 or abs(qo - q95) < 0.35:
            print(
                f"  {mu:6.1f} {q95:8.3f} {qo:8.3f} {q95 - qo:+9.3f} "
                f"{'YES' if qo <= q95 else 'no':>7}"
            )

    # interpolate the crossing of q95(mu) - q_obs(mu)
    mm = np.array([x[0] for x in rows])
    dd = np.array([x[1] - x[2] for x in rows])
    sign = np.where(np.diff(np.sign(dd)) != 0)[0]
    if len(sign):
        i = sign[0]
        x0, x1, y0, y1 = mm[i], mm[i + 1], dd[i], dd[i + 1]
        ul_interp = float(x0 - y0 * (x1 - x0) / (y1 - y0))
    else:
        ul_interp = float(mm[dd >= 0].max()) if np.any(dd >= 0) else float("nan")
    ul_grid = float(mm[dd >= 0].max()) if np.any(dd >= 0) else float("nan")
    print(f"\n  endpoint, last accepted 0.1-grid point : {ul_grid:.2f} Mpc")
    print(f"  endpoint, interpolated zero crossing   : {ul_interp:.3f} Mpc")
    print("  previous 0.5-grid endpoint             : 11.00 Mpc")
    print(f"  shift from refinement                  : {ul_interp - 11.0:+.3f} Mpc")

    # coverage at the refined endpoint, INDEPENDENT ensemble
    mu_t = round(ul_interp, 2)
    j = int(np.argmin(np.abs(MU_GRID - mu_t)))
    A = M.amp(mu_t, d_obs)
    base = A * (M.u + mu_t * M.v)
    cal = np.array([M.q_grid(base + L @ RNG.standard_normal(p_dim))[0][j] for _ in range(n_sim)])
    thr = float(np.percentile(cal, 95))
    n_val = 12000
    val = np.array([M.q_grid(base + L @ RNG.standard_normal(p_dim))[0][j] for _ in range(n_val)])
    cov = float(np.mean(val <= thr))
    mce = float(np.sqrt(cov * (1 - cov) / n_val))
    print(f"\n  coverage at refined endpoint mu={mu_t}: {cov:.4f} +- {mce:.4f}")
    print(f"  deviation from nominal: {(cov - 0.95) / mce:+.2f} sigma_MC")

    ok_cov = abs(cov - 0.95) < 3 * mce
    ok_shift = abs(ul_interp - 11.0) <= 0.25
    print("\n" + "-" * 78)
    print("VERDICT")
    print(f"  coverage within 3 sigma_MC of 0.95 : {'PASS' if ok_cov else 'FAIL'}")
    print(f"  shift consistent with 0.5-grid     : {'PASS' if ok_shift else 'FAIL'}")
    if ok_cov and ok_shift:
        print("  -> the over-coverage WAS a grid artefact; refined endpoint stands.")
    elif not ok_cov:
        print("  -> over-coverage SURVIVES refinement: it is a property of the")
        print("     statistic/boundary, not the grid. Must be reported as such.")
    print("-" * 78)

    (HERE / "gate1_fine_coverage.json").write_text(
        json.dumps(
            {
                "ul_grid": ul_grid,
                "ul_interp": ul_interp,
                "coverage": cov,
                "mc_err": mce,
                "n_sim": n_sim,
                "rows": rows,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
