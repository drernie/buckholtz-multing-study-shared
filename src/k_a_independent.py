"""Independent k_A(z) estimators — Press-Schechter virial MVP. NOT_VALIDATION."""

from __future__ import annotations

import csv
import math
from dataclasses import dataclass
from pathlib import Path

from src.cluster_schedule import (
    ClusterRow,
    load_claude_cluster_params,
)

# G/c² in Mpc/M_sun (consistent with virial bridge audit units)
_G_OVER_C2_MPC_PER_MSUN = 4.785e-20
# (km/s)² Mpc / M_sun for σ_v² ~ GM/r
_GM_R_KMS2_MPC = 4.302e-6


@dataclass(frozen=True)
class CosmoParams:
    """Minimal cosmology for Press-Schechter characteristic mass trend."""

    h: float = 0.73
    omega_m: float = 0.3
    sigma8: float = 0.8
    n_s: float = 0.96


def sigma_v_virial_kms(m_A: float, r_A: float) -> float:
    """σ_v ~ sqrt(GM/r) in km/s (order-of-magnitude virial)."""
    if r_A <= 0 or m_A <= 0:
        raise ValueError("m_A and r_A must be positive")
    return math.sqrt(_GM_R_KMS2_MPC * m_A / r_A)


def k_a_virial_kinetic(m_A: float, r_A: float) -> float:
    """k_A/c² = (3/2) M σ_v² / c² in M_sun units."""
    sigma_kms = sigma_v_virial_kms(m_A, r_A)
    sigma_ms = sigma_kms * 1000.0
    c = 299_792_458.0
    return 1.5 * m_A * (sigma_ms / c) ** 2


def k_a_ps_virial(m_A: float, r_A: float) -> float:
    """Alias: G m² / (r c²) virial estimate [M_sun]."""
    return _G_OVER_C2_MPC_PER_MSUN * m_A**2 / r_A


def characteristic_mass_msun(z: float, cosmo: CosmoParams) -> float:
    """Press-Schechter M_* ~ M_char (1+z)^(-3/2) scaling (diagnostic only)."""
    m_char = 1.0e14 * (cosmo.omega_m / 0.3) ** (-1) * (cosmo.h / 0.7) ** (-2)
    return m_char * (1.0 + z) ** (-1.5)


def k_a_press_schechter_virial(
    z: float,
    m_A: float,
    r_A: float,
    cosmo: CosmoParams | None = None,
    alpha: float = 1.0,
) -> float:
    """Press-Schechter + virial k_A(z); alpha fixed at z=0 to CSV (not H fit)."""
    _ = cosmo or CosmoParams()
    m_star = characteristic_mass_msun(z, cosmo or CosmoParams())
    mass_factor = (m_A / m_star) ** (2.0 / 3.0) * (1.0 + z)
    return alpha * k_a_virial_kinetic(m_A, r_A) * mass_factor / (1.0 + z)


def fit_alpha_at_z0(
    rows: list[ClusterRow],
    cosmo: CosmoParams | None = None,
) -> float:
    """Scale factor alpha so k_A_indep(z=0) matches CSV k_A at z=0."""
    r0 = rows[0]
    raw = k_a_press_schechter_virial(r0.z, r0.m_A, r0.r_A, cosmo, alpha=1.0)
    if raw <= 0:
        return 1.0
    return r0.k_A / raw


def k_a_schedule_independent(
    rows: list[ClusterRow],
    cosmo: CosmoParams | None = None,
    alpha: float | None = None,
) -> list[float]:
    alpha_use = alpha if alpha is not None else fit_alpha_at_z0(rows, cosmo)
    return [
        k_a_press_schechter_virial(r.z, r.m_A, r.r_A, cosmo, alpha_use) for r in rows
    ]


def load_k_a_csv_inferred(
    csv_path: Path | str | None = None,
) -> list[float]:
    return [r.k_A for r in load_claude_cluster_params(csv_path)]


def k_a_nbody_from_catalog(
    z: float,
    catalog_path: Path | str,
) -> float:
    """Scaffold: load external halo catalog CSV with columns z, k_A_msun."""
    path = Path(catalog_path)
    if not path.exists():
        raise FileNotFoundError(
            f"N-body catalog not found: {path}. See data/README_nbody_k_a.md"
        )
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if abs(float(row["z"]) - z) < 1e-6:
                return float(row["k_A_msun"])
    raise ValueError(f"No catalog row for z={z}")


def k_a_ratio_indep_vs_csv(rows: list[ClusterRow]) -> list[float]:
    k_ind = k_a_schedule_independent(rows)
    return [
        (ki / r.k_A) if (r.k_A > 0 and ki > 0) else math.nan
        for ki, r in zip(k_ind, rows, strict=True)
    ]
