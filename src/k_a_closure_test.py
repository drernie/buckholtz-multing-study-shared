"""k_A closure test — PASS/FAIL/INCONCLUSIVE without refit. INTERNAL_CLOSURE_TEST."""

from __future__ import annotations

import math
from dataclasses import dataclass
from enum import StrEnum

from src.bridge_gate import (
    AUTHOR_CONFIRMATION_REQUIRED,
    INTERNAL_CLOSURE_TEST,
    NOT_REFUTATION,
    OUTPUT_LABEL,
    is_mcmc_allowed,
)
from src.bridge_phi import h_mult_from_params_list, rms_sigma_h
from src.cluster_schedule import (
    H_OBS_DEFAULT,
    SIGMA_H_DEFAULT,
    ClusterRow,
    D_power_law,
    cluster_rows_to_params_list,
    load_claude_cluster_params,
)
from src.k_a_independent import k_a_schedule_independent, load_k_a_csv_inferred

BETA_D = 4.5
BETA_Q = 18.0
H_ANCHOR = 73.0
GAMMA_REQ_DEFAULT = 2.27
PASS_RMS_MULTIPLIER = 2.0


class ClosureVerdict(StrEnum):
    PASS = "PASS"
    FAIL = "FAIL"
    INCONCLUSIVE = "INCONCLUSIVE"


@dataclass
class ClosureResult:
    verdict: ClosureVerdict
    arm: str
    rms_csv_k: float
    rms_indep_k: float
    rms_multiplier: float
    baseline_rms: float
    epsilon_q_mean: float
    label: str
    internal_closure_test: str
    author_confirmation_required: str
    not_refutation: str
    is_mcmc_allowed: bool
    interpretation: str
    gamma_D: float | None = None


def _eps_q(k_A: float, beta_q: float, r_A: float, m_A: float, D: float) -> float:
    return (k_A * beta_q * r_A) ** 2 / (m_A * D**2) if m_A > 0 and D > 0 else math.nan


def _schedule_D_eff(rows: list[ClusterRow], gamma: float) -> list[float]:
    d0 = rows[0].D
    return [D_power_law(r.z, d0, gamma) for r in rows]


def run_k_a_closure_test(
    rows: list[ClusterRow] | None = None,
    H_obs: list[float] | None = None,
    sigma_H: list[float] | None = None,
    beta_d: float = BETA_D,
    beta_q: float = BETA_Q,
    H_anchor: float = H_ANCHOR,
    arm: str = "D_csv",
    gamma_req: float = GAMMA_REQ_DEFAULT,
    k_source: str = "press_schechter_virial",
) -> ClosureResult:
    """Compare independent k_A vs CSV-inferred k_A at fixed beta (no refit)."""
    cluster_rows = rows if rows is not None else load_claude_cluster_params()
    H = H_obs if H_obs is not None else H_OBS_DEFAULT
    sig = sigma_H if sigma_H is not None else SIGMA_H_DEFAULT

    if arm == "D_csv":
        D_vals = None
        arm_label = "Arm A: D_csv"
    elif arm == "D_eff":
        D_vals = _schedule_D_eff(cluster_rows, gamma_req)
        arm_label = f"Arm B: D_eff gamma={gamma_req:.2f}"
    else:
        raise ValueError(f"Unknown arm: {arm}")

    params_csv = cluster_rows_to_params_list(cluster_rows, D_override=D_vals)
    baseline_rms = rms_sigma_h(
        h_mult_from_params_list(params_csv, beta_d, beta_q, H_anchor),
        H,
        sig,
    )

    if k_source == "press_schechter_virial":
        k_ind = k_a_schedule_independent(cluster_rows)
    elif k_source == "csv":
        k_ind = load_k_a_csv_inferred()
    else:
        return ClosureResult(
            verdict=ClosureVerdict.INCONCLUSIVE,
            arm=arm_label,
            rms_csv_k=baseline_rms,
            rms_indep_k=math.nan,
            rms_multiplier=PASS_RMS_MULTIPLIER,
            baseline_rms=baseline_rms,
            epsilon_q_mean=math.nan,
            label=OUTPUT_LABEL,
            internal_closure_test=INTERNAL_CLOSURE_TEST,
            author_confirmation_required=AUTHOR_CONFIRMATION_REQUIRED,
            not_refutation=NOT_REFUTATION,
            is_mcmc_allowed=is_mcmc_allowed,
            interpretation="N-body catalog not connected — INCONCLUSIVE, not FAIL.",
            gamma_D=gamma_req if arm == "D_eff" else None,
        )

    params_indep = cluster_rows_to_params_list(
        cluster_rows, D_override=D_vals, k_override=k_ind
    )
    rms_indep = rms_sigma_h(
        h_mult_from_params_list(params_indep, beta_d, beta_q, H_anchor),
        H,
        sig,
    )

    eps_q = [
        _eps_q(r.k_A, beta_q, r.r_A, r.m_A, r.D)
        for r in cluster_rows
    ]
    eps_q_mean = float(sum(e for e in eps_q if not math.isnan(e)) / len(eps_q))

    threshold = PASS_RMS_MULTIPLIER * baseline_rms
    if rms_indep <= threshold:
        verdict = ClosureVerdict.PASS
        interpretation = (
            "Independent k_A schedule reaches Table A1 retrodiction within "
            f"{PASS_RMS_MULTIPLIER}× baseline RMS without refitting beta or k_A."
        )
    elif rms_indep > baseline_rms * 3:
        verdict = ClosureVerdict.FAIL
        interpretation = (
            "Independent k_A substantially worse than CSV-inferred k_A at fixed beta/D. "
            "Table A1 implementation may require fitted k_A schedule."
        )
    else:
        verdict = ClosureVerdict.INCONCLUSIVE
        interpretation = (
            "Difference between independent and CSV k_A is moderate; "
            "author confirmation of k_A physical meaning required."
        )

    return ClosureResult(
        verdict=verdict,
        arm=arm_label,
        rms_csv_k=baseline_rms,
        rms_indep_k=rms_indep,
        rms_multiplier=PASS_RMS_MULTIPLIER,
        baseline_rms=baseline_rms,
        epsilon_q_mean=eps_q_mean,
        label=OUTPUT_LABEL,
        internal_closure_test=INTERNAL_CLOSURE_TEST,
        author_confirmation_required=AUTHOR_CONFIRMATION_REQUIRED,
        not_refutation=NOT_REFUTATION,
        is_mcmc_allowed=is_mcmc_allowed,
        interpretation=interpretation,
        gamma_D=gamma_req if arm == "D_eff" else None,
    )
