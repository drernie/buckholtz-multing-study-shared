"""M2-G4 Fisher Rank Identifiability Test.

Question: under the reconstructed CLAUDE-SPECIFIC AI-mediated bridge
    H_MULT(z)^2 = H_anchor^2 * Phi(z) / Phi(z_anchor),
    Phi(z) = A_m - A_d + A_q,
are the hidden parameters (beta_d, beta_q, H_anchor, D-schedule) structurally
and practically identifiable from the reported Table A1 H_MULT(z) values?

Labels: CLAUDE_SPECIFIC_AI_MEDIATED_BRIDGE / OUR_RECONSTRUCTION /
        NOT_AUTHOR_CONFIRMED / NOT_VALIDATION / NOT_REFUTATION.

This analyzes identifiability of OUR reconstruction of ONE AI service's
(Claude's) bridge. It says nothing about Dr. Buckholtz's intended physics.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.bridge_phi import h_mult_from_params_list  # noqa: E402
from src.cluster_schedule import SIGMA_H_DEFAULT, load_claude_cluster_params  # noqa: E402

# Claude-reported values (Table A1 caption) — AI_CHOICE, not author-derived
BETA_D_CLAUDE = 4.5
BETA_Q_CLAUDE = 18.0
H_ANCHOR_CLAUDE = 73.0

# Reported H_MULT column (Table A1, rows 1..12) — the "observations"
H_MULT_REPORTED = [
    71.1,
    70.2,
    73.5,
    78.8,
    83.1,
    91.4,
    104.2,
    126.5,
    151.8,
    197.3,
    271.5,
    418.1,
]


def model_h(
    theta: np.ndarray,
    scenario: str,
    base_params: list[tuple[float, float, float, float, float]],
) -> np.ndarray:
    """H_pred(z) for each scenario. base_params rows: (z, m_A, k_A, r_A, D)."""
    if scenario == "A":  # [beta_d, beta_q]
        bd, bq = theta
        h0 = H_ANCHOR_CLAUDE
        params = base_params
    elif scenario == "B":  # [beta_d, beta_q, H_anchor]
        bd, bq, h0 = theta
        params = base_params
    elif scenario == "C":  # [beta_d, beta_q, alpha_D, H_anchor]; OUR_RECONSTRUCTION
        bd, bq, alpha, h0 = theta
        d0 = base_params[0][4]
        params = [(z, m, k, r, d0 * (1.0 + z) ** (-alpha)) for (z, m, k, r, _d) in base_params]
    else:
        raise ValueError(scenario)
    return np.array(h_mult_from_params_list(params, bd, bq, h0, anchor_index=0))


def jacobian_fd(
    theta: np.ndarray,
    scenario: str,
    base_params: list,
    rel_step: float = 1e-6,
) -> np.ndarray:
    """Central finite-difference Jacobian J[i,j] = dH(z_i)/dtheta_j."""
    n_obs = len(base_params)
    n_par = len(theta)
    J = np.zeros((n_obs, n_par))
    for j in range(n_par):
        h = max(abs(theta[j]) * rel_step, 1e-9)
        tp, tm = theta.copy(), theta.copy()
        tp[j] += h
        tm[j] -= h
        J[:, j] = (model_h(tp, scenario, base_params) - model_h(tm, scenario, base_params)) / (
            2 * h
        )
    return J


def analyze(J: np.ndarray, names: list[str], sigma: np.ndarray) -> dict:
    """Rank / SVD / conditioning / per-column sensitivity (sigma-weighted)."""
    Jw = J / sigma[:, None]  # weight rows by 1/sigma_H (Fisher convention)
    sv = np.linalg.svd(Jw, compute_uv=False)
    tol = max(Jw.shape) * np.finfo(float).eps * (sv[0] if sv.size else 0.0)
    rank = int(np.sum(sv > tol))
    # practical rank: singular values above 1e-8 * largest
    prac_rank = int(np.sum(sv > 1e-8 * sv[0])) if sv.size and sv[0] > 0 else 0
    cond = float(sv[0] / sv[-1]) if sv.size and sv[-1] > 0 else float("inf")
    col_norm = {n: float(np.linalg.norm(Jw[:, k])) for k, n in enumerate(names)}
    # collinearity: cosine between columns
    cos = {}
    for a in range(len(names)):
        for b in range(a + 1, len(names)):
            na, nb = np.linalg.norm(Jw[:, a]), np.linalg.norm(Jw[:, b])
            c = float(Jw[:, a] @ Jw[:, b] / (na * nb)) if na > 0 and nb > 0 else float("nan")
            cos[f"{names[a]}|{names[b]}"] = c
    fisher = Jw.T @ Jw
    return {
        "param_names": names,
        "n_obs": int(J.shape[0]),
        "n_par": int(J.shape[1]),
        "singular_values": [float(s) for s in sv],
        "rank_numeric": rank,
        "rank_practical_1e-8": prac_rank,
        "condition_number": cond,
        "column_norms_weighted": col_norm,
        "column_cosines": cos,
        "fisher_diag": [float(x) for x in np.diag(fisher)],
    }


def main() -> dict:
    rows = load_claude_cluster_params()
    base = [(r.z, r.m_A, r.k_A, r.r_A, r.D) for r in rows]
    sigma = np.array(
        [
            r.h_data_sigma if r.h_data_sigma else s
            for r, s in zip(rows, SIGMA_H_DEFAULT, strict=True)
        ]
    )
    h_obs = np.array(H_MULT_REPORTED)

    # sanity: reconstruction reproduces reported H_MULT? (context, not a gate)
    h_at_claude = model_h(np.array([BETA_D_CLAUDE, BETA_Q_CLAUDE]), "A", base)
    recon_rms = float(np.sqrt(np.mean(((h_at_claude - h_obs) / sigma) ** 2)))

    out: dict = {
        "test": "M2-G4 Fisher Rank Identifiability",
        "labels": [
            "CLAUDE_SPECIFIC_AI_MEDIATED_BRIDGE",
            "OUR_RECONSTRUCTION",
            "NOT_AUTHOR_CONFIRMED",
            "NOT_VALIDATION",
            "NOT_REFUTATION",
        ],
        "data": {
            "n_rows": len(base),
            "source": "claude_galaxy_cluster_parameters.csv (geom-mean midpoints)",
            "H_MULT_reported_rows": H_MULT_REPORTED,
            "reconstruction_rms_sigma_at_claude_betas": recon_rms,
        },
        "scenarios": {},
    }

    theta_A = np.array([BETA_D_CLAUDE, BETA_Q_CLAUDE])
    theta_B = np.array([BETA_D_CLAUDE, BETA_Q_CLAUDE, H_ANCHOR_CLAUDE])
    theta_C = np.array([BETA_D_CLAUDE, BETA_Q_CLAUDE, 1.0, H_ANCHOR_CLAUDE])

    for name, theta, scen, pnames in [
        ("A_beta_only", theta_A, "A", ["beta_d", "beta_q"]),
        ("B_beta_anchor", theta_B, "B", ["beta_d", "beta_q", "H_anchor"]),
        ("C_beta_alphaD_anchor", theta_C, "C", ["beta_d", "beta_q", "alpha_D", "H_anchor"]),
    ]:
        J = jacobian_fd(theta, scen, base)
        res = analyze(J, pnames, sigma)
        # relative sensitivity: dH/H per 100% change in param
        h0 = model_h(theta, scen, base)
        rel = {}
        for j, pn in enumerate(pnames):
            rel[pn] = float(np.max(np.abs(J[:, j] * theta[j] / h0)))
        res["max_relative_sensitivity_per_100pct"] = rel
        out["scenarios"][name] = res

    # Scenario D — counting argument (free per-row D or k_A schedule)
    n_obs = len(base)
    out["scenarios"]["D_flexible_schedule"] = {
        "param_names": "[beta_d, beta_q] + 12 per-row D_i (or k_A_i)",
        "n_obs": n_obs,
        "n_par": 2 + n_obs,
        "verdict": "FAIL_BY_COUNTING",
        "note": (
            "params (14) > observations (12); with anchor-ratio normalization "
            "one D_i is absorbed, leaving 13 > 11 effective dof. Any H(z) curve "
            "is exactly reproducible -> non-predictive, structurally "
            "non-identifiable."
        ),
    }
    return out


if __name__ == "__main__":
    result = main()
    out_path = ROOT / "reports" / "m2_g4_fisher_rank_identifiability.json"
    out_path.parent.mkdir(exist_ok=True)
    out_path.write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))
