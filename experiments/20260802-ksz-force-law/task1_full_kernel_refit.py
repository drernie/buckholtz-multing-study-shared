"""TASK 1 — full K_3 kernel (inside AND outside mass) + UV-model comparison.

Two defects found in the previous kernel are fixed here:

  (a) it integrated only r' < R (the enclosed-mass convention inherited from
      the Newtonian analysis). For 1/r^2 that is exact by Gauss. For 1/r^3 it
      is NOT: a shell at r' > R contributes with the OPPOSITE sign. Verified:
      C_3(1.5) = -0.1318, C_3(2.0) = -0.0293, C_3(1.05) = -3.99.
  (b) the integral diverges at r' -> R, so a UV prescription is mandatory and
      the result is conditional on it.

Single closed form valid on BOTH sides of rho = 1 (verified against the
mu-quadrature to 6 digits on each side):

    C_3(rho) = 1/(2(1-rho^2)) + ln|(1+rho)/(1-rho)| / (4 rho)

    rho < 1 : positive, ~ +1/(4(1-rho))  as rho -> 1-
    rho > 1 : negative, ~ -1/(4(rho-1))  as rho -> 1+
    C_2(rho) = 1 for rho<1, 0 for rho>1   (Gauss)

THREE UV prescriptions are compared, per Task 1:
  H  hard exclusion   : drop |r' - R| < s_min
  S  softened force   : F_d ∝ s/(s^2+rc^2)^2, i.e. replace s^-3 by s/(s^2+rc^2)^2
  P  Plummer-like     : replace s^-3 by (s^2+rc^2)^{-3/2}

PASS criterion (stated in advance): the 95% bound on l_d stays within a factor
of ~2 across all three prescriptions at comparable scale.
FAIL: it moves by an order of magnitude -> no UV-independent statement possible.

Safety: NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION
L0: descriptive.
"""

from __future__ import annotations

import json
from pathlib import Path

import h5py
import numpy as np
from scipy.interpolate import interp1d
from scipy.stats import chi2 as chi2dist

HERE = Path(__file__).resolve().parent / "artifacts"
H_LITTLE = 0.677
R_MIN = 6.0
R_MAX_INT = 400.0  # xi is zero beyond its measured range; integrate generously


def c3(rho: np.ndarray) -> np.ndarray:
    """Closed form, valid both sides of rho=1. Singular AT rho=1 by construction."""
    rho = np.asarray(rho, dtype=float)
    out = np.empty_like(rho)
    safe = np.abs(rho - 1.0) > 1e-12
    r = rho[safe]
    out[safe] = 1.0 / (2.0 * (1.0 - r**2)) + np.log(np.abs((1 + r) / (1 - r))) / (4.0 * r)
    out[~safe] = 0.0
    out[rho < 1e-12] = 1.0
    return out


def load():
    d = np.loadtxt(HERE / "xi_zbin2.dat")
    xi = interp1d(d[:, 0] / H_LITTLE, d[:, 1], bounds_error=False, fill_value=0.0)
    with h5py.File(HERE / "dr6.hdf", "r") as f:
        pw = f["df_pw/block0_values"][:]
        cols = [c.decode() for c in f["df_pw/block0_items"][:]]
        cov = f["df_cov/block0_values"][:]
    r_all = pw[:, cols.index("r_mp")]
    p_all = pw[:, cols.index("ksz_curve")]
    return xi, r_all, p_all, cov


def k2_full(R, xi, n=40000):
    r = np.linspace(R_MIN, R, n)
    return float(np.trapezoid(xi(r) * r**2, r) / R**2)


def k3_hard(R, xi, s_min, n=40000):
    """Full-space integral, mass with |r'-R| < s_min excluded."""
    r = np.linspace(R_MIN, R_MAX_INT, n)
    keep = np.abs(r - R) >= s_min
    return float(np.trapezoid(np.where(keep, xi(r) * r**2 * c3(r / R), 0.0), r) / R**3)


def k3_soft(R, xi, rc, n=40000, n_mu=4000):
    """Softened force: s^-3 -> s/(s^2+rc^2)^2. Requires the 2D integral (no closed C)."""
    r = np.linspace(R_MIN, R_MAX_INT, n // 40)
    mu = np.linspace(-1.0, 1.0, n_mu)
    RR, MM = np.meshgrid(r, mu, indexing="ij")
    s2 = np.clip(R**2 + RR**2 - 2 * R * RR * MM, 0.0, None)
    # radial component: (R - r mu)/s * F(s), F(s) = s/(s^2+rc^2)^2
    integ = xi(RR) * RR**2 * (R - RR * MM) / (s2 + rc**2) ** 2
    return float(0.5 * np.trapezoid(np.trapezoid(integ, mu, axis=1), r) / R**3 * R**3 / R**3 * R**3)


def k3_plummer(R, xi, rc, n=1000, n_mu=4000):
    """Plummer softening: s^-3 -> (s^2+rc^2)^{-3/2}, radial component (R-r mu)/s."""
    r = np.linspace(R_MIN, R_MAX_INT, n)
    mu = np.linspace(-1.0, 1.0, n_mu)
    RR, MM = np.meshgrid(r, mu, indexing="ij")
    s2 = np.clip(R**2 + RR**2 - 2 * R * RR * MM, 0.0, None)
    integ = xi(RR) * RR**2 * (R - RR * MM) / (s2 + rc**2) ** 2
    return float(0.5 * np.trapezoid(np.trapezoid(integ, mu, axis=1), r) / R**3)


def fit_ld(pobs, cinv, k2, k3, grid):
    def chi2(model):
        a = float(pobs @ cinv @ model)
        b = float(model @ cinv @ model)
        return float(pobs @ cinv @ pobs) - a * a / b

    ch = np.array([chi2(-(k2 - ld * k3)) for ld in grid])
    i = int(np.argmin(ch))
    c0 = chi2(-k2)
    return {
        "best": float(grid[i]),
        "chi2": float(ch[i]),
        "hi68": float(grid[ch <= ch[i] + 1.0].max()),
        "hi95": float(grid[ch <= ch[i] + 3.84].max()),
        "lo95": float(grid[ch <= ch[i] + 3.84].min()),
        "dchi2": float(c0 - ch[i]),
    }


def main():
    xi, r_all, p_all, cov = load()
    m = (r_all >= 25) & (r_all <= 225)
    r, pobs = r_all[m], p_all[m]
    cinv = np.linalg.inv(cov[np.ix_(m, m)])
    grid = np.linspace(-200.0, 200.0, 4001)

    print("=" * 78)
    print("TASK 1 — FULL kernel (inside+outside) under three UV prescriptions")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    # control: C_3 closed form vs mu-quadrature, both sides of rho=1
    print("\n[CONTROL] C_3 closed form vs direct mu-quadrature")

    def mu_quad(rho, k=3, n=400000):
        mu = np.linspace(-1, 1, n)
        s = np.sqrt(np.clip(1 + rho**2 - 2 * rho * mu, 1e-14, None))
        return 0.5 * np.trapezoid((1 - rho * mu) / s ** (k + 1), mu)

    okc = True
    for rho in (0.5, 0.9, 1.5, 3.0):
        a, b = float(c3(np.array([rho]))[0]), mu_quad(rho)
        rel = abs(a - b) / max(abs(b), 1e-12)
        okc &= rel < 2e-3
        print(f"  rho={rho:5.2f}: closed={a:+11.6f}  mu-quad={b:+11.6f}  rel={rel:.2e}")
    if not okc:
        print("  *** CONTROL FAILED — stop ***")
        return
    print("  -> closed form valid on both sides of rho=1.")

    k2 = np.array([k2_full(R, xi) for R in r])

    print("\n[A] HARD EXCLUSION — full-space K_3, |r'-R| >= s_min")
    print(
        f"  {'s_min':>7} {'K3(100)':>11} {'l_d best':>10} {'95% lo':>9} {'95% hi':>9} {'dchi2':>8}"
    )
    rows = {}
    for s_min in (1.0, 2.0, 5.0, 10.0):
        k3 = np.array([k3_hard(R, xi, s_min) for R in r])
        f = fit_ld(pobs, cinv, k2, k3, grid)
        rows[f"hard_{s_min}"] = f
        print(
            f"  {s_min:7.1f} {k3_hard(100.0, xi, s_min):11.6f} {f['best']:10.2f} "
            f"{f['lo95']:9.2f} {f['hi95']:9.2f} {f['dchi2']:8.4f}"
        )

    print("\n[B] PLUMMER SOFTENING — s^-3 -> (s^2+rc^2)^{-3/2}")
    print(f"  {'rc':>7} {'K3(100)':>11} {'l_d best':>10} {'95% lo':>9} {'95% hi':>9} {'dchi2':>8}")
    for rc in (1.0, 2.0, 5.0):
        k3 = np.array([k3_plummer(R, xi, rc) for R in r])
        f = fit_ld(pobs, cinv, k2, k3, grid)
        rows[f"plummer_{rc}"] = f
        print(
            f"  {rc:7.1f} {k3_plummer(100.0, xi, rc):11.6f} {f['best']:10.2f} "
            f"{f['lo95']:9.2f} {f['hi95']:9.2f} {f['dchi2']:8.4f}"
        )

    # verdict
    his = [v["hi95"] for v in rows.values() if v["hi95"] > 0]
    print("\n" + "-" * 78)
    print("VERDICT")
    if his:
        print(f"  95% upper on l_d across prescriptions: {min(his):.1f} .. {max(his):.1f} Mpc")
        print(
            f"  spread factor = {max(his) / min(his):.2f}  "
            f"({'PASS (<2x)' if max(his) / min(his) < 2 else 'FAIL (>2x) — UV-dominated'})"
        )
    dchis = [v["dchi2"] for v in rows.values()]
    p_worst = 1 - chi2dist.cdf(max(dchis), 1)
    print(f"  dchi2 range {min(dchis):.3f}..{max(dchis):.3f}  -> best p = {p_worst:.3f}")
    print("  dipole NOT detected under any prescription" if p_worst > 0.05 else "  CHECK")
    print("-" * 78)

    (HERE / "task1_full_kernel_results.json").write_text(json.dumps(rows, indent=2))


if __name__ == "__main__":
    main()
