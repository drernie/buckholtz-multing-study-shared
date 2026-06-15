"""Stage 2 — parametric grid search over gamma and alpha. VERIFIED_DIAGNOSTIC."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from src.bridge_phi import h_mult_from_params_list, mae_h, rms_sigma_h
from src.cluster_schedule import (
    H_OBS_DEFAULT,
    SIGMA_H_DEFAULT,
    ClusterRow,
    D_power_law,
    cluster_rows_to_params_list,
    k_a_power_law,
)


@dataclass
class GridSearchResult:
    gamma: float
    alpha: float
    mae: float
    rms_sigma: float
    physically_admissible: bool
    flags: list[str]


@dataclass
class GridSearchSummary:
    best_unconstrained: GridSearchResult | None
    best_physical: GridSearchResult | None
    mae_grid: np.ndarray
    gamma_values: np.ndarray
    alpha_values: np.ndarray
    physical_mask: np.ndarray
    labels: list[str]


def _physical_schedule_ok(
    rows: list[ClusterRow],
    D_vals: list[float],
    k_vals: list[float],
) -> tuple[bool, list[str]]:
    flags: list[str] = []
    ok = True
    for i, (r, D, k) in enumerate(zip(rows, D_vals, k_vals, strict=True)):
        if D <= 2.0 * r.r_A:
            ok = False
            flags.append(f"z={r.z}: D<=2r_A")
        if k <= 0:
            ok = False
            flags.append(f"z={r.z}: k_A<=0")
        if r.k_A_hi and k > 50 * r.k_A_hi:
            ok = False
            flags.append(f"z={r.z}: k_A extreme high")
        if i > 0 and k_vals[i] / k_vals[i - 1] > 100:
            flags.append(f"z={r.z}: k_A jump")
    return ok, flags


def evaluate_gamma_alpha(
    rows: list[ClusterRow],
    gamma: float,
    alpha: float,
    H_obs: list[float],
    sigma_H: list[float],
    beta_d: float,
    beta_q: float,
    H_anchor: float,
) -> GridSearchResult:
    d0 = rows[0].D
    k0 = rows[0].k_A
    D_vals = [D_power_law(r.z, d0, gamma) for r in rows]
    k_vals = [k_a_power_law(r.z, k0, alpha) for r in rows]
    params = cluster_rows_to_params_list(rows, D_override=D_vals, k_override=k_vals)
    H_pred = h_mult_from_params_list(params, beta_d, beta_q, H_anchor)
    phys_ok, flags = _physical_schedule_ok(rows, D_vals, k_vals)
    return GridSearchResult(
        gamma=gamma,
        alpha=alpha,
        mae=mae_h(H_pred, H_obs),
        rms_sigma=rms_sigma_h(H_pred, H_obs, sigma_H),
        physically_admissible=phys_ok,
        flags=flags,
    )


def run_parametric_grid_search(
    rows: list[ClusterRow],
    H_obs: list[float] | None = None,
    sigma_H: list[float] | None = None,
    gamma_min: float = 0.0,
    gamma_max: float = 4.0,
    alpha_min: float = -6.0,
    alpha_max: float = 6.0,
    n_gamma: int = 41,
    n_alpha: int = 49,
    beta_d: float = 4.5,
    beta_q: float = 18.0,
    H_anchor: float = 73.0,
) -> GridSearchSummary:
    H = H_obs if H_obs is not None else H_OBS_DEFAULT
    sig = sigma_H if sigma_H is not None else SIGMA_H_DEFAULT
    gamma_values = np.linspace(gamma_min, gamma_max, n_gamma)
    alpha_values = np.linspace(alpha_min, alpha_max, n_alpha)
    mae_grid = np.full((n_alpha, n_gamma), np.nan)
    physical_mask = np.zeros((n_alpha, n_gamma), dtype=bool)

    best_unc: GridSearchResult | None = None
    best_phys: GridSearchResult | None = None

    for ia, alpha in enumerate(alpha_values):
        for ig, gamma in enumerate(gamma_values):
            res = evaluate_gamma_alpha(
                rows, float(gamma), float(alpha), H, sig, beta_d, beta_q, H_anchor
            )
            mae_grid[ia, ig] = res.mae
            physical_mask[ia, ig] = res.physically_admissible
            if best_unc is None or res.mae < best_unc.mae:
                best_unc = res
            if res.physically_admissible and (
                best_phys is None or res.mae < best_phys.mae
            ):
                best_phys = res

    return GridSearchSummary(
        best_unconstrained=best_unc,
        best_physical=best_phys,
        mae_grid=mae_grid,
        gamma_values=gamma_values,
        alpha_values=alpha_values,
        physical_mask=physical_mask,
        labels=[
            "VERIFIED_DIAGNOSTIC",
            "NOT_VALIDATION",
            "NOT_REFUTATION",
            "AUTHOR_BRIDGE_NEEDED",
        ],
    )
