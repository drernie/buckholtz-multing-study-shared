"""Stage 1 — bin-by-bin (D, k_A) isoline diagnostic. VERIFIED_DIAGNOSTIC."""

from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np

from src.bridge_phi import phi_force_sum
from src.cluster_schedule import ClusterRow


@dataclass
class IsolineBinResult:
    z: float
    H_target: float
    m_A: float
    r_A: float
    D_csv: float
    k_A_csv: float
    admissible_exists: bool
    min_k_A_admissible: float | None
    min_D_admissible: float | None
    csv_in_physical_box: bool
    distance_csv_to_isoline: float
    n_admissible_grid_points: int


def h_bridge_at(
    D: float,
    k_A: float,
    m_A: float,
    r_A: float,
    beta_d: float,
    beta_q: float,
    phi_anchor: float,
    H_anchor: float,
) -> float:
    phi_z = phi_force_sum(m_A, k_A, r_A, D, beta_d, beta_q)
    if phi_anchor <= 0 or phi_z <= 0:
        return math.nan
    return H_anchor * math.sqrt(phi_z / phi_anchor)


def physical_box_ok(
    D: float,
    k_A: float,
    r_A: float,
    k_lo: float | None,
    k_hi: float | None,
    d_lo: float | None,
    d_hi: float | None,
) -> bool:
    if D <= 2.0 * r_A or k_A <= 0:
        return False
    if k_lo is not None and k_A < 0.1 * k_lo:
        return False
    if k_hi is not None and k_A > 10.0 * k_hi:
        return False
    if d_lo is not None and D < 0.5 * d_lo:
        return False
    if d_hi is not None and D > 2.0 * d_hi:
        return False
    return True


def isoline_residual(
    D: float,
    k_A: float,
    m_A: float,
    r_A: float,
    beta_d: float,
    beta_q: float,
    phi_anchor: float,
    H_anchor: float,
    H_target: float,
) -> float:
    h = h_bridge_at(D, k_A, m_A, r_A, beta_d, beta_q, phi_anchor, H_anchor)
    if math.isnan(h):
        return 1e6
    return h - H_target


def scan_isoline_bin(
    row: ClusterRow,
    H_target: float,
    phi_anchor: float,
    H_anchor: float,
    beta_d: float,
    beta_q: float,
    n_D: int = 60,
    n_k: int = 60,
    rel_tol: float = 0.02,
) -> IsolineBinResult:
    d_min = max(2.01 * row.r_A, row.D_lo or row.r_A * 2)
    d_max = max(d_min * 1.5, (row.D_hi or row.D * 2) * 1.5)
    k_min = max((row.k_A_lo or row.k_A * 0.01) * 0.1, 1e6)
    k_max = (row.k_A_hi or row.k_A * 10) * 10

    D_grid = np.logspace(math.log10(d_min), math.log10(d_max), n_D)
    k_grid = np.logspace(math.log10(k_min), math.log10(k_max), n_k)

    admissible: list[tuple[float, float]] = []
    near_isoline: list[tuple[float, float, float]] = []

    for D in D_grid:
        for k_A in k_grid:
            res = isoline_residual(
                float(D), float(k_A), row.m_A, row.r_A,
                beta_d, beta_q, phi_anchor, H_anchor, H_target,
            )
            if abs(res) <= rel_tol * H_target:
                near_isoline.append((float(D), float(k_A), abs(res)))
                if physical_box_ok(
                    float(D), float(k_A), row.r_A,
                    row.k_A_lo, row.k_A_hi, row.D_lo, row.D_hi,
                ):
                    admissible.append((float(D), float(k_A)))

    csv_ok = physical_box_ok(
        row.D, row.k_A, row.r_A, row.k_A_lo, row.k_A_hi, row.D_lo, row.D_hi,
    )
    csv_dist = min(
        (abs(r[2]) for r in near_isoline),
        default=abs(
            isoline_residual(
                row.D, row.k_A, row.m_A, row.r_A,
                beta_d, beta_q, phi_anchor, H_anchor, H_target,
            )
        ),
    )

    min_k = min((k for _, k in admissible), default=None)
    min_d = min((d for d, _ in admissible), default=None)

    return IsolineBinResult(
        z=row.z,
        H_target=H_target,
        m_A=row.m_A,
        r_A=row.r_A,
        D_csv=row.D,
        k_A_csv=row.k_A,
        admissible_exists=len(admissible) > 0,
        min_k_A_admissible=min_k,
        min_D_admissible=min_d,
        csv_in_physical_box=csv_ok,
        distance_csv_to_isoline=csv_dist,
        n_admissible_grid_points=len(admissible),
    )


def run_isoline_diagnostic(
    rows: list[ClusterRow],
    H_obs: list[float],
    beta_d: float = 4.5,
    beta_q: float = 18.0,
    H_anchor: float = 73.0,
) -> list[IsolineBinResult]:
    r0 = rows[0]
    phi0 = phi_force_sum(r0.m_A, r0.k_A, r0.r_A, r0.D, beta_d, beta_q)
    return [
        scan_isoline_bin(row, H_obs[i], phi0, H_anchor, beta_d, beta_q)
        for i, row in enumerate(rows)
    ]
