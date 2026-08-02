"""TASK 3 — xi(r) uncertainty via the upstream CORRELATED covariance, plus the
pair-weighting convention systematic.

Two things are fixed relative to the earlier attempt:

(1) CORRELATED realisations. Previously xi was redrawn with INDEPENDENT noise
    per bin, which destroys its correlated shape and understates the spread.
    Upstream ships `covariances_sdss_g.txt` — a full 15x15 covariance for the
    already-convolved kernel g(r), on exactly our separation bins. We draw
    from THAT, so the realisations keep the right correlation structure.

(2) PAIR-WEIGHTING CONVENTION. `export_sdss_pairwise_curve.py` (feeding fit1.py)
    defines
            g(r) = [1/(1+xi(r))] * I(r)/r^2 ,  I(r) = int_6^r xi(r') r'^2 dr'
    while fit2.py (the exponent fit) uses I(r)/r^2 with NO 1/(1+xi) factor.
    Our kernel so far followed fit2.py. The ratio g_upstream / K2_ours runs
    0.70 at 25 Mpc to 0.95 at 75 Mpc, i.e. this is a real O(30%) systematic at
    small separations, not a rounding difference. Both are computed here.

DECLARED ASSUMPTIONS (not hidden):
  A1. Cov(d_kSZ, xi) = 0. The kSZ measurement and the Ross+2016 xi come from
      related but not identical samples (ACT x SDSS DR15 LRG vs BOSS DR12
      post-recon). Adding two covariances ignores any cross term. No joint
      bootstrap indices are published, so this cannot currently be tested.
  A2. The relative fluctuation of K3 tracks that of K2 realisation-by-
      realisation. Upstream provides a covariance for g only; there is none
      for a 1/r^3 kernel. We therefore scale K3 by the same factor each
      realisation applies to K2. This is an approximation, and it is why the
      resulting spread is a LOWER bound on the true xi-induced uncertainty.

Safety: NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION
L0: descriptive.
"""

from __future__ import annotations

import json
from pathlib import Path

import h5py
import numpy as np
import pandas as pd
from scipy.integrate import quad
from scipy.interpolate import interp1d

HERE = Path(__file__).resolve().parent / "artifacts"
H_LITTLE, R_MIN, R_MAX_INT, S_MIN = 0.677, 6.0, 400.0, 2.0
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


class Chi2:
    def __init__(self, Ci, u, v):
        self.Ci, self.u, self.v = Ci, u, v
        self.uCu, self.uCv, self.vCv = (
            float(u @ Ci @ u),
            float(u @ Ci @ v),
            float(v @ Ci @ v),
        )

    def bind(self, p):
        self.pCp = float(p @ self.Ci @ p)
        self.pCu = float(p @ self.Ci @ self.u)
        self.pCv = float(p @ self.Ci @ self.v)
        return self

    def __call__(self, ld):
        return self.pCp - (self.pCu + ld * self.pCv) ** 2 / (
            self.uCu + 2 * ld * self.uCv + ld**2 * self.vCv
        )


def endpoint(Ci, k2, k3, p, thr=3.759):
    """thr = q95 at mu~15 from the Neyman belt (fiducial s_min=2)."""
    ch = Chi2(Ci, -k2, k3).bind(p)
    g = np.linspace(0.0, 300.0, 3001)
    y = ch(g)
    return float(g[y <= y.min() + thr].max()), float(g[int(np.argmin(y))])


def main():
    d = np.loadtxt(HERE / "xi_zbin2.dat")
    r_xi, xi_v = d[:, 0] / H_LITTLE, d[:, 1]
    xi0 = interp1d(r_xi, xi_v, bounds_error=False, fill_value=0.0)

    with h5py.File(HERE / "dr6.hdf", "r") as f:
        pw = f["df_pw/block0_values"][:]
        cols = [c.decode() for c in f["df_pw/block0_items"][:]]
        cov = f["df_cov/block0_values"][:]
    r_all = pw[:, cols.index("r_mp")]
    p_all = pw[:, cols.index("ksz_curve")]
    m = (r_all >= 25) & (r_all <= 225)
    r, p = r_all[m], p_all[m]
    Ci = np.linalg.inv(cov[np.ix_(m, m)])

    gt = pd.read_csv(HERE / "sdss_g_sqrtg.csv")
    Cg = np.loadtxt(HERE / "covariances_sdss_g.txt")
    g_up = gt["g"].to_numpy(float)
    r_up = gt["rsep"].to_numpy(float)

    print("=" * 78)
    print("TASK 3 — correlated xi uncertainty + pair-weighting convention")
    print("L0: descriptive. NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION")
    print("=" * 78)
    print(f"\n  upstream g covariance: {Cg.shape}, bins {r_up.min():.0f}-{r_up.max():.0f} Mpc")
    print(f"  our bins match upstream: {np.allclose(r, r_up)}")

    # kernels, both conventions
    k2_nw = np.array([quad(lambda x: xi0(x) * x**2, R_MIN, R)[0] / R**2 for R in r])
    k2_w = k2_nw / (1.0 + xi0(r))

    def build_k3(weighted):
        out = []
        for R in r:
            x = np.linspace(R_MIN, R_MAX_INT, 30000)
            keep = np.abs(x - R) >= S_MIN
            val = np.trapezoid(np.where(keep, xi0(x) * x**2 * c3(x / R), 0.0), x) / R**3
            out.append(val / (1.0 + xi0(R)) if weighted else val)
        return np.array(out)

    k3_nw, k3_w = build_k3(False), build_k3(True)

    print("\n[CONVENTION CHECK] upstream g vs our weighted K2")
    print(
        f"  {'r':>6} {'g_upstream':>11} {'K2 weighted':>12} {'K2 unweighted':>14} {'ratio w/up':>11}"
    )
    for i in (0, 3, 7, 11, 14):
        print(
            f"  {r[i]:6.0f} {g_up[i]:11.5f} {k2_w[i]:12.5f} {k2_nw[i]:14.5f} "
            f"{k2_w[i] / g_up[i]:11.4f}"
        )

    print("\n[CONVENTION SYSTEMATIC] endpoint under each")
    for lab, a, b in (
        ("fit2 (unweighted, used so far)", k2_nw, k3_nw),
        ("fit1/export (1/(1+xi) weighted)", k2_w, k3_w),
    ):
        e, best = endpoint(Ci, a, b, p)
        print(f"  {lab:34s} l_d < {e:6.2f} Mpc   (best {best:.2f})")

    # correlated realisations from the upstream g covariance
    print("\n[CORRELATED REALISATIONS] drawn from upstream Cov(g), 1000 draws")
    Lg = np.linalg.cholesky(Cg + 1e-14 * np.eye(len(Cg)))
    res = {"unweighted": [], "weighted": []}
    for _ in range(1000):
        g_s = g_up + Lg @ RNG.standard_normal(len(g_up))
        scale = np.where(np.abs(g_up) > 0, g_s / g_up, 1.0)  # per-bin correlated factor
        for lab, a, b in (("unweighted", k2_nw, k3_nw), ("weighted", k2_w, k3_w)):
            e, _ = endpoint(Ci, a * scale, b * scale, p)  # assumption A2
            res[lab].append(e)
    for lab, vals in res.items():
        vv = np.array(vals)
        print(
            f"  {lab:12s} median {np.median(vv):6.2f}  16-84% "
            f"[{np.percentile(vv, 16):.2f}, {np.percentile(vv, 84):.2f}]  "
            f"2.5-97.5% [{np.percentile(vv, 2.5):.2f}, {np.percentile(vv, 97.5):.2f}]"
        )

    print("\n" + "-" * 78)
    print("READING")
    vv = np.array(res["unweighted"])
    print(
        f"  xi-induced spread (correlated, 1000 draws): "
        f"{np.percentile(vv, 2.5):.1f}-{np.percentile(vv, 97.5):.1f} Mpc "
        f"= +/-{100 * (np.percentile(vv, 97.5) - np.percentile(vv, 2.5)) / 2 / np.median(vv):.0f}%"
    )
    e_nw, _ = endpoint(Ci, k2_nw, k3_nw, p)
    e_w, _ = endpoint(Ci, k2_w, k3_w, p)
    print(
        f"  pair-weighting convention systematic: {min(e_nw, e_w):.1f} vs {max(e_nw, e_w):.1f} Mpc "
        f"= {100 * abs(e_w - e_nw) / min(e_nw, e_w):.0f}%"
    )
    print("  ASSUMPTIONS A1 (no kSZ-xi cross-covariance) and A2 (K3 tracks K2)")
    print("  are DECLARED, not verified. A2 makes this a LOWER bound on the spread.")
    print("-" * 78)

    (HERE / "task3_xi_covariance.json").write_text(
        json.dumps(
            {
                "endpoint_unweighted": e_nw,
                "endpoint_weighted": e_w,
                "xi_realisations": {k: [float(x) for x in v] for k, v in res.items()},
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
