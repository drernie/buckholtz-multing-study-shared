"""Cluster schedule loader — Claude supplementary CSV. NOT_VALIDATION."""

from __future__ import annotations

import csv
import math
from dataclasses import dataclass
from pathlib import Path

import numpy as np

DEFAULT_CLAUDE_CSV = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "supplementary_extracted"
    / "claude_galaxy_cluster_parameters.csv"
)

H_OBS_DEFAULT = [73.0, 69.0, 74.0, 79.0, 82.0, 92.0, 105.0, 125.0, 150.0, 195.0, 270.0, 420.0]
SIGMA_H_DEFAULT = [1.0, 3.0, 4.0, 4.5, 5.0, 7.0, 8.0, 15.0, 20.0, 30.0, 50.0, 90.0]


def _parse_range(s: str) -> tuple[float, float]:
    text = s.strip()
    for i in range(len(text) - 1, 0, -1):
        if text[i] == "-" and text[i - 1].isdigit():
            return float(text[:i]), float(text[i + 1 :])
    raise ValueError(f"Cannot parse range: {s!r}")


def geom_mean_range(lo: float, hi: float) -> float:
    if lo <= 0 or hi <= 0:
        raise ValueError(f"Range must be positive: {lo}, {hi}")
    return math.sqrt(lo * hi)


@dataclass(frozen=True)
class ClusterRow:
    z: float
    m_A: float
    k_A: float
    r_A: float
    D: float
    time_gyr: float | None = None
    h_data_nominal: float | None = None
    h_data_sigma: float | None = None
    k_A_lo: float | None = None
    k_A_hi: float | None = None
    D_lo: float | None = None
    D_hi: float | None = None


def load_claude_cluster_params(
    csv_path: Path | str | None = None,
) -> list[ClusterRow]:
    path = Path(csv_path) if csv_path else DEFAULT_CLAUDE_CSV
    rows: list[ClusterRow] = []
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            m_lo, m_hi = _parse_range(row["m_a_msun_range"])
            k_lo, k_hi = _parse_range(row["k_a_c2_msun_range"])
            r_lo, r_hi = _parse_range(row["r_a_mpc_range"])
            d_lo, d_hi = _parse_range(row["d_cab_mpc_range"])
            rows.append(
                ClusterRow(
                    z=float(row["z"]),
                    m_A=geom_mean_range(m_lo, m_hi),
                    k_A=geom_mean_range(k_lo, k_hi),
                    r_A=(r_lo + r_hi) / 2.0,
                    D=(d_lo + d_hi) / 2.0,
                    time_gyr=float(row["time_gyr"]) if row.get("time_gyr") else None,
                    h_data_nominal=float(row["h_data_nominal"])
                    if row.get("h_data_nominal")
                    else None,
                    h_data_sigma=float(row["h_data_sigma"])
                    if row.get("h_data_sigma")
                    else None,
                    k_A_lo=k_lo,
                    k_A_hi=k_hi,
                    D_lo=d_lo,
                    D_hi=d_hi,
                )
            )
    return rows


def cluster_rows_to_params_list(
    rows: list[ClusterRow],
    D_override: list[float] | None = None,
    k_override: list[float] | None = None,
) -> list[tuple[float, float, float, float, float]]:
    out: list[tuple[float, float, float, float, float]] = []
    for i, r in enumerate(rows):
        k = k_override[i] if k_override else r.k_A
        d = D_override[i] if D_override else r.D
        out.append((r.z, r.m_A, k, r.r_A, d))
    return out


def fit_power_law_D(
    z_values: list[float] | np.ndarray,
    D_values: list[float] | np.ndarray,
) -> tuple[float, float]:
    z_arr = np.asarray(z_values, dtype=float)
    d_arr = np.asarray(D_values, dtype=float)
    mask = (z_arr >= 0) & (d_arr > 0)
    log_1pz = np.log1p(z_arr[mask])
    log_d = np.log(d_arr[mask])
    if len(log_1pz) < 2:
        return float(d_arr[0]), 0.0
    slope, intercept = np.polyfit(log_1pz, log_d, 1)
    return float(math.exp(intercept)), float(-slope)


def D_power_law(z: float, D0: float, gamma: float) -> float:
    return D0 * (1.0 + z) ** (-gamma)


def k_a_power_law(z: float, k0: float, alpha: float) -> float:
    return k0 * (1.0 + z) ** (-alpha)


def load_claude_params_list(
    csv_path: Path | str | None = None,
) -> list[tuple[float, float, float, float, float]]:
    return cluster_rows_to_params_list(load_claude_cluster_params(csv_path))
