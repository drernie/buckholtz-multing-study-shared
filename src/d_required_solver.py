"""Inverse bridge: solve D_required from H_obs. INTERNAL_DIAGNOSTIC_ONLY."""

from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np
from scipy.optimize import brentq

from src.bridge_phi import phi_force_sum
from src.cluster_schedule import ClusterRow, load_claude_cluster_params


@dataclass
class DRequiredRow:
    z: float
    H_obs: float
    sigma_H: float
    m_A: float
    k_A: float
    r_A: float
    D_csv: float
    D_required: float
    D_hubble: float
    ratio_D_req_over_csv: float


def _bracket_root(f, d_lo: float = 0.05, d_hi: float = 500.0) -> tuple[float, float]:
    ds = np.logspace(math.log10(d_lo), math.log10(d_hi), 400)
    vals = [f(d) for d in ds]
    for i in range(len(ds) - 1):
        if vals[i] == 0:
            return ds[i], ds[i]
        if vals[i] * vals[i + 1] < 0:
            return ds[i], ds[i + 1]
    raise ValueError("No sign change for D_required root")


def solve_D_required(
    m_A: float,
    k_A: float,
    r_A: float,
    H_target: float,
    H_anchor: float,
    phi_anchor: float,
    beta_d: float,
    beta_q: float,
    d_lo: float = 0.05,
    d_hi: float = 500.0,
) -> float:
    target_ratio = (H_target / H_anchor) ** 2

    def f(D: float) -> float:
        return phi_force_sum(m_A, k_A, r_A, D, beta_d, beta_q) / phi_anchor - target_ratio

    try:
        lo, hi = _bracket_root(f, d_lo, d_hi)
        return float(brentq(f, lo, hi, maxiter=200))
    except (ValueError, RuntimeError):
        return math.nan


def fit_gamma(
    z_values: list[float],
    D_values: list[float],
    D0: float | None = None,
    z_min: float = 0.0,
) -> tuple[float, float, float]:
    pts = [(z, d) for z, d in zip(z_values, D_values, strict=True) if z >= z_min and d > 0]
    if len(pts) < 2:
        return math.nan, math.nan, math.nan
    zv = np.array([p[0] for p in pts])
    dv = np.array([p[1] for p in pts])
    log_1pz = np.log1p(zv)

    if D0 is not None:
        d0_use = D0
        log_d = np.log(dv / d0_use)
        # Fixed-D0 diagnostic: fit log(D/D0) = -gamma log(1+z).
        slope = float(np.sum(log_1pz * log_d) / np.sum(log_1pz * log_1pz))
        fitted = slope * log_1pz
    else:
        log_d_abs = np.log(dv)
        slope, intercept = np.polyfit(log_1pz, log_d_abs, 1)
        d0_use = float(math.exp(intercept))
        log_d = log_d_abs - intercept
        fitted = slope * log_1pz

    ss_res = float(np.sum((log_d - fitted) ** 2))
    ss_tot = float(np.sum((log_d - log_d.mean()) ** 2))
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else math.nan
    return d0_use, float(-slope), r2


def gamma_sensitivity(
    beta_d: float = 4.5,
    beta_q: float = 18.0,
    H_anchor: float = 73.0,
    z_min: float = 0.4,
    sign: int = 1,
    rows: list[ClusterRow] | None = None,
) -> float:
    cluster_rows = rows if rows is not None else load_claude_cluster_params()
    r0 = cluster_rows[0]
    phi0 = phi_force_sum(r0.m_A, r0.k_A, r0.r_A, r0.D, beta_d, beta_q)
    z_vals: list[float] = []
    d_vals: list[float] = []
    for row in cluster_rows:
        if row.z < z_min:
            continue
        H = (row.h_data_nominal or H_anchor) + sign * (row.h_data_sigma or 0.0)
        if H <= 0:
            continue
        d_req = solve_D_required(
            row.m_A, row.k_A, row.r_A, H, H_anchor, phi0, beta_d, beta_q
        )
        if not math.isnan(d_req):
            z_vals.append(row.z)
            d_vals.append(d_req)
    _d0, gamma, _r2 = fit_gamma(z_vals, d_vals, D0=r0.D, z_min=0.0)
    return gamma


def build_d_required_table(
    beta_d: float = 4.5,
    beta_q: float = 18.0,
    H_anchor: float = 73.0,
    rows: list[ClusterRow] | None = None,
    H_obs: list[float] | None = None,
    sigma_H: list[float] | None = None,
) -> list[DRequiredRow]:
    cluster_rows = rows if rows is not None else load_claude_cluster_params()
    r0 = cluster_rows[0]
    phi0 = phi_force_sum(r0.m_A, r0.k_A, r0.r_A, r0.D, beta_d, beta_q)
    D0 = r0.D
    out: list[DRequiredRow] = []
    for i, row in enumerate(cluster_rows):
        H = H_obs[i] if H_obs else (row.h_data_nominal or H_anchor)
        sigma = sigma_H[i] if sigma_H else (row.h_data_sigma or 1.0)
        if i == 0:
            d_req = row.D
        else:
            d_req = solve_D_required(
                row.m_A, row.k_A, row.r_A, H, H_anchor, phi0, beta_d, beta_q
            )
        ratio = d_req / row.D if (not math.isnan(d_req) and row.D > 0) else math.nan
        out.append(
            DRequiredRow(
                z=row.z,
                H_obs=H,
                sigma_H=sigma,
                m_A=row.m_A,
                k_A=row.k_A,
                r_A=row.r_A,
                D_csv=row.D,
                D_required=d_req,
                D_hubble=D0 / (1.0 + row.z),
                ratio_D_req_over_csv=ratio,
            )
        )
    return out
