"""Bridge Phi — shared forward-bridge math. NOT_VALIDATION."""
from __future__ import annotations

import math
from collections.abc import Sequence

_NOT_VALIDATION = "NOT_VALIDATION"


def phi_force_sum(
    m_A: float,
    k_A: float,
    r_A: float,
    D: float,
    beta_d: float,
    beta_q: float,
) -> float:
    if D <= 0 or r_A <= 0:
        raise ValueError("D and r_A must be > 0")
    f_m = m_A / D**2
    f_d = 2 * k_A * beta_d * r_A / D**3
    f_q = k_A**2 * beta_q**2 * r_A**2 / D**4
    return f_m - f_d + f_q


def h_from_phi_ratio(phi_z: float, phi_anchor: float, H_anchor: float) -> float:
    if phi_anchor <= 0 or phi_z <= 0:
        return math.nan
    ratio = phi_z / phi_anchor
    return math.nan if ratio <= 0 else H_anchor * math.sqrt(ratio)


def h_mult_from_params_list(
    params_list: Sequence[tuple[float, float, float, float, float]],
    beta_d: float,
    beta_q: float,
    H_anchor: float,
    anchor_index: int = 0,
) -> list[float]:
    _z0, m0, k0, r0, d0 = params_list[anchor_index]
    phi0 = phi_force_sum(m0, k0, r0, d0, beta_d, beta_q)
    if phi0 <= 0:
        return [math.nan] * len(params_list)
    return [
        h_from_phi_ratio(phi_force_sum(m, k, r, d, beta_d, beta_q), phi0, H_anchor)
        for _z, m, k, r, d in params_list
    ]


def rms_sigma_h(
    H_pred: Sequence[float],
    H_obs: Sequence[float],
    sigma_H: Sequence[float],
) -> float:
    residuals = [
        (hp - ho) / sh
        for hp, ho, sh in zip(H_pred, H_obs, sigma_H, strict=True)
        if not math.isnan(hp) and sh > 0
    ]
    return 999.0 if not residuals else float(
        math.sqrt(sum(r**2 for r in residuals) / len(residuals))
    )


def mae_h(H_pred: Sequence[float], H_obs: Sequence[float]) -> float:
    vals = [abs(hp - ho) for hp, ho in zip(H_pred, H_obs, strict=True) if not math.isnan(hp)]
    return 999.0 if not vals else float(sum(vals) / len(vals))


def get_label() -> str:
    return _NOT_VALIDATION


phi = phi_force_sum
H_mult = h_mult_from_params_list
rms_sigma = rms_sigma_h
