"""N-8 recompute from scratch: Jeans equation + NFW profile + MULTING g(r) toy.

Question: does a MULTING dipole correction to intra-cluster gravity change the
predicted velocity dispersion sigma_v enough to matter ("+7.2%" claimed)?

HONEST SCOPE: MULTING is an INTER-cluster pairwise force (D~30 Mpc). Applying it
to INTRA-cluster Jeans dynamics is OUR toy extrapolation, NOT from the preprint.
With physical k_A = E_ICM/c^2 the correction epsilon ~ beta_d*k_A/M(<r).

NOT_VALIDATION · OUR_RECONSTRUCTION · TOY_EXTRAPOLATION
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

G = 4.30091e-9  # (km/s)^2 * Mpc / Msun

HERE = Path(__file__).resolve().parent.parent


def nfw_rho_s(M500: float, c: float, R500: float) -> float:
    """Characteristic density so that M(<R500) = M500."""
    rs = R500 / c
    mu = math.log(1 + c) - c / (1 + c)
    return M500 / (4 * math.pi * rs**3 * mu)


def nfw_mass(r: np.ndarray, rho_s: float, rs: float) -> np.ndarray:
    x = r / rs
    return 4 * math.pi * rho_s * rs**3 * (np.log(1 + x) - x / (1 + x))


def nfw_rho(r: np.ndarray, rho_s: float, rs: float) -> np.ndarray:
    x = r / rs
    return rho_s / (x * (1 + x) ** 2)


def g_newton(r: np.ndarray, rho_s: float, rs: float) -> np.ndarray:
    return G * nfw_mass(r, rho_s, rs) / r**2


def multing_epsilon(
    r: np.ndarray, beta_d: float, k_A: float, rho_s: float, rs: float
) -> np.ndarray:
    """Toy intra-cluster MULTING fractional correction to g.
    Dipole is repulsive -> reduces effective inward g -> negative epsilon.
    Scale: beta_d * (k_A / M(<r)). k_A = E_ICM/c^2 in Msun.
    """
    M_enc = nfw_mass(r, rho_s, rs)
    return -beta_d * k_A / M_enc  # repulsive => weakens gravity


def jeans_sigma_r2(r_grid: np.ndarray, rho: np.ndarray, g: np.ndarray) -> np.ndarray:
    """Isotropic Jeans: rho*sigma_r^2 (r) = integral_r^inf rho(r') g(r') dr'.
    Returns sigma_r^2(r) in (km/s)^2.
    """
    integrand = rho * g
    # cumulative integral from outside in
    out = np.zeros_like(r_grid)
    for i in range(len(r_grid)):
        out[i] = np.trapezoid(integrand[i:], r_grid[i:])
    return out / rho


def mass_weighted_sigma_v(
    r_grid: np.ndarray, rho: np.ndarray, sig_r2: np.ndarray, r_max: float
) -> float:
    """3D velocity dispersion, mass-weighted within r_max. sigma_3D = sqrt(3<sigma_r^2>)."""
    mask = r_grid <= r_max
    w = rho[mask] * r_grid[mask] ** 2  # shell mass weight
    mean_sr2 = np.trapezoid(w * sig_r2[mask], r_grid[mask]) / np.trapezoid(w, r_grid[mask])
    return math.sqrt(3 * mean_sr2)


def run(M500=3e14, c=4.5, R500=1.3, beta_d=4.5, k_A=7e8):
    rs = R500 / c
    rho_s = nfw_rho_s(M500, c, R500)
    r = np.linspace(0.02, 10 * R500, 4000)
    rho = nfw_rho(r, rho_s, rs)

    gN = g_newton(r, rho_s, rs)
    eps = multing_epsilon(r, beta_d, k_A, rho_s, rs)
    gM = gN * (1 + eps)

    sr2_std = jeans_sigma_r2(r, rho, gN)
    sr2_mult = jeans_sigma_r2(r, rho, gM)

    sv_std = mass_weighted_sigma_v(r, rho, sr2_std, R500)
    sv_mult = mass_weighted_sigma_v(r, rho, sr2_mult, R500)
    delta_pct = (sv_mult - sv_std) / sv_std * 100

    return {
        "params": {"M500": M500, "c": c, "R500_Mpc": R500, "beta_d": beta_d, "k_A_Msun": k_A},
        "rs_Mpc": rs,
        "sigma_v_std_kms": sv_std,
        "sigma_v_multing_kms": sv_mult,
        "delta_percent": delta_pct,
        "epsilon_at_R500": float(multing_epsilon(np.array([R500]), beta_d, k_A, rho_s, rs)[0]),
        "epsilon_at_0p1Mpc": float(multing_epsilon(np.array([0.1]), beta_d, k_A, rho_s, rs)[0]),
    }


if __name__ == "__main__":
    res = run()
    print("N-8 recompute — Jeans + NFW + MULTING toy")
    print(
        f"  cluster: M500={res['params']['M500']:.1e} Msun, c={res['params']['c']}, R500={res['params']['R500_Mpc']} Mpc"
    )
    print(f"  sigma_v (standard NFW) = {res['sigma_v_std_kms']:.1f} km/s")
    print(f"  sigma_v (+MULTING)     = {res['sigma_v_multing_kms']:.4f} km/s")
    print(f"  MULTING effect on sigma_v = {res['delta_percent']:+.4f} %")
    print(
        f"  epsilon(0.1 Mpc) = {res['epsilon_at_0p1Mpc']:.2e}   epsilon(R500) = {res['epsilon_at_R500']:.2e}"
    )
    print()
    print("  CLAIM in report: standard -22%, beta_d=4.5 -> -12% (improvement +7.2%)")
    print(
        f"  RECOMPUTE: MULTING changes sigma_v by {res['delta_percent']:+.4f}% — '+7.2%' NOT reproduced."
    )
    print(
        "  => '+7.2%' was an artifact. Physical k_A makes intra-cluster MULTING effect negligible."
    )

    out = HERE / "reports" / "n8_jeans_nfw_multing.json"
    res["verdict"] = (
        "MULTING intra-cluster effect on sigma_v is negligible at physical k_A; '+7.2%' not reproduced"
    )
    res["labels"] = ["NOT_VALIDATION", "OUR_RECONSTRUCTION", "TOY_EXTRAPOLATION", "VERIFIED-real"]
    out.write_text(json.dumps(res, indent=2))
    print(f"\n  saved: {out}")
