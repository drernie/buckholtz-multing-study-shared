"""AIC/BIC model comparison: MULTING vs flat ΛCDM on Table A1 data.

Methodology reference: arXiv:2504.09054v2 (April 2025) — same methodology used
for CPL/JBP vs ΛCDM comparison on H(z) data.

Safety labels: NOT_VALIDATION · NOT_REFUTATION · INTERNAL_DIAGNOSTIC_ONLY
               NOT_AUTHOR_CONFIRMED · OUR_RECONSTRUCTION · TABLE_A1_ONLY

Key constraint: ε(z) taken directly from Table A1 (AI-fitted values).
This is IN-SAMPLE comparison — H_MULT was fitted to these same 11 points.
Out-of-sample test requires the bridge formula (Q1, AUTHOR_NEEDED).

Two scenarios:
  A — k_MULTING = 2: treat β as externally specified (same free params as ΛCDM)
  B — k_MULTING = 4: treat β_d, β_q as fitted parameters (+2 vs ΛCDM)

Three criteria: AIC, BIC, AICc (small-sample corrected).
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
from scipy.optimize import minimize

# ---------------------------------------------------------------------------
# Table A1 data (rows 2–12, z=0.06 to z=8.50; row 1 z=0 excluded: sign issue)
# Source: data/table_a1_reported.csv, M8-A-R1 verified (commit add7cba)
# ---------------------------------------------------------------------------

Z = np.array([0.06, 0.14, 0.25, 0.40, 0.65, 1.00, 1.50, 2.10, 3.20, 5.00, 8.50])
H_OBS = np.array([69.0, 74.0, 79.0, 82.0, 92.0, 105.0, 125.0, 150.0, 195.0, 270.0, 420.0])
SIGMA_H = np.array([3.0, 4.0, 4.5, 5.0, 7.0, 8.0, 15.0, 20.0, 30.0, 50.0, 90.0])

# H_FLRW and H_MULT directly from Table A1 (author's reported values)
H_FLRW_TABLE = np.array([68.1, 69.3, 71.5, 75.0, 83.0, 95.7, 114.8, 140.3, 187.6, 265.2, 398.5])
H_MULT_TABLE = np.array([70.2, 73.5, 78.8, 83.1, 91.4, 104.2, 126.5, 151.8, 197.3, 271.5, 418.1])

N = len(Z)  # 11 data points

REPORTS_DIR = Path(__file__).parent.parent / "reports"

# ---------------------------------------------------------------------------
# Flat ΛCDM model
# ---------------------------------------------------------------------------


def h_lcdm(z: np.ndarray, h0: float, omega_m: float) -> np.ndarray:
    """Flat ΛCDM: H(z) = H0 * sqrt(Ω_m*(1+z)³ + Ω_Λ)."""
    omega_lambda = 1.0 - omega_m
    return h0 * np.sqrt(omega_m * (1.0 + z) ** 3 + omega_lambda)


def chi2(h_model: np.ndarray, h_obs: np.ndarray, sigma: np.ndarray) -> float:
    return float(np.sum(((h_obs - h_model) / sigma) ** 2))


# ---------------------------------------------------------------------------
# AIC / BIC / AICc
# ---------------------------------------------------------------------------


def aic(chi2_val: float, k: int) -> float:
    return 2.0 * k + chi2_val


def bic(chi2_val: float, k: int, n: int) -> float:
    return k * np.log(n) + chi2_val


def aicc(chi2_val: float, k: int, n: int) -> float:
    """AIC with small-sample correction (Sugiura 1978)."""
    correction = 2.0 * k * (k + 1) / (n - k - 1)
    return aic(chi2_val, k) + correction


def interpret_delta_aic(delta: float) -> str:
    """Burnham & Anderson (2002) scale."""
    if delta < -10:
        return "decisive (>10 evidence units)"
    if delta < -6:
        return "strong (6–10 units)"
    if delta < -2:
        return "substantial (2–6 units)"
    if abs(delta) <= 2:
        return "equivalent (<2 units, no discrimination)"
    if delta < 6:
        return "model 1 substantially favored (2–6 units)"
    return "model 1 strongly favored (>6 units)"


def interpret_delta_bic(delta: float) -> str:
    """Kass & Raftery (1995) scale: 0–2 barely, 2–6 positive, 6–10 strong, >10 very strong."""
    if delta < -10:
        return "very strong evidence for MULTING"
    if delta < -6:
        return "strong evidence for MULTING"
    if delta < -2:
        return "positive evidence for MULTING"
    if abs(delta) <= 2:
        return "barely worth mentioning"
    if delta < 6:
        return "positive evidence for ΛCDM"
    if delta < 10:
        return "strong evidence for ΛCDM"
    return "very strong evidence for ΛCDM"


# ---------------------------------------------------------------------------
# Step 1: χ² from Table A1 values directly
# ---------------------------------------------------------------------------


def table_chi2_comparison() -> dict:
    chi2_flrw_table = chi2(H_FLRW_TABLE, H_OBS, SIGMA_H)
    chi2_mult_table = chi2(H_MULT_TABLE, H_OBS, SIGMA_H)

    # Verify against sigma columns in Table A1
    sigma_flrw_from_table = np.array(
        [-0.3, -1.2, -1.7, -1.4, -1.3, -1.2, -0.7, -0.5, -0.2, -0.1, -0.2]
    )
    sigma_mult_from_table = np.array(
        [0.4, -0.1, -0.04, 0.2, -0.1, -0.1, 0.1, 0.1, 0.1, 0.03, -0.02]
    )
    chi2_flrw_check = float(np.sum(sigma_flrw_from_table**2))
    chi2_mult_check = float(np.sum(sigma_mult_from_table**2))

    return {
        "source": "Table A1 reported values (not re-fitted)",
        "chi2_LCDM": round(chi2_flrw_table, 4),
        "chi2_MULTING": round(chi2_mult_table, 4),
        "chi2_LCDM_from_sigma_col": round(chi2_flrw_check, 4),
        "chi2_MULTING_from_sigma_col": round(chi2_mult_check, 4),
        "delta_chi2": round(chi2_mult_table - chi2_flrw_table, 4),
    }


# ---------------------------------------------------------------------------
# Step 2: Optimise flat ΛCDM (2 params) to get minimum χ²
# ---------------------------------------------------------------------------


def fit_lcdm() -> dict:
    def neg_loglike(params: list) -> float:
        h0, omega_m = params
        if h0 < 40 or h0 > 100 or omega_m < 0.1 or omega_m > 0.9:
            return 1e10
        return chi2(h_lcdm(Z, h0, omega_m), H_OBS, SIGMA_H)

    result = minimize(
        neg_loglike,
        [70.0, 0.3],
        method="Nelder-Mead",
        options={"xatol": 1e-6, "fatol": 1e-8, "maxiter": 10000},
    )
    h0_best, omega_m_best = result.x
    chi2_min = result.fun
    h_best = h_lcdm(Z, h0_best, omega_m_best)
    residuals = (H_OBS - h_best) / SIGMA_H

    return {
        "H0_best": round(float(h0_best), 3),
        "Omega_m_best": round(float(omega_m_best), 4),
        "chi2_min": round(float(chi2_min), 4),
        "residuals": [round(float(r), 4) for r in residuals],
        "converged": bool(result.success),
    }


# ---------------------------------------------------------------------------
# Step 3: AIC/BIC/AICc for both scenarios
# ---------------------------------------------------------------------------


def model_selection_table(chi2_lcdm: float, chi2_multing: float) -> dict:
    k_lcdm = 2  # H0, Ω_m
    k_mult_a = 2  # Scenario A: β treated as externally given
    k_mult_b = 4  # Scenario B: β_d, β_q as fitted params

    results = {}

    for scenario, k_mult in [("A_beta_fixed", k_mult_a), ("B_beta_fitted", k_mult_b)]:
        aic_lcdm = aic(chi2_lcdm, k_lcdm)
        aic_mult = aic(chi2_multing, k_mult)
        bic_lcdm = bic(chi2_lcdm, k_lcdm, N)
        bic_mult = bic(chi2_multing, k_mult, N)
        aicc_lcdm = aicc(chi2_lcdm, k_lcdm, N)
        aicc_mult = aicc(chi2_multing, k_mult, N)

        d_aic = aic_mult - aic_lcdm
        d_bic = bic_mult - bic_lcdm
        d_aicc = aicc_mult - aicc_lcdm

        results[scenario] = {
            "k_LCDM": k_lcdm,
            "k_MULTING": k_mult,
            "AIC_LCDM": round(aic_lcdm, 3),
            "AIC_MULTING": round(aic_mult, 3),
            "BIC_LCDM": round(bic_lcdm, 3),
            "BIC_MULTING": round(bic_mult, 3),
            "AICc_LCDM": round(aicc_lcdm, 3),
            "AICc_MULTING": round(aicc_mult, 3),
            "delta_AIC": round(d_aic, 3),
            "delta_BIC": round(d_bic, 3),
            "delta_AICc": round(d_aicc, 3),
            "AIC_verdict": interpret_delta_aic(d_aic),
            "BIC_verdict": interpret_delta_bic(d_bic),
            "AICc_verdict": interpret_delta_aic(d_aicc),
        }

    return results


# ---------------------------------------------------------------------------
# Step 4: Epsilon(z) diagnostics
# ---------------------------------------------------------------------------


def epsilon_diagnostics() -> dict:
    # ε = H_MULT²/H_FLRW² - 1
    eps_from_table = (H_MULT_TABLE / H_FLRW_TABLE) ** 2 - 1
    eps_known = np.array(
        [0.063, 0.125, 0.215, 0.228, 0.213, 0.186, 0.214, 0.171, 0.106, 0.048, 0.101]
    )
    return {
        "z": list(Z),
        "epsilon_from_table": [round(float(e), 4) for e in eps_from_table],
        "epsilon_m8a_r1": list(eps_known),
        "max_diff": round(float(np.max(np.abs(eps_from_table - eps_known))), 5),
        "peak_z": float(Z[int(np.argmax(eps_from_table))]),
        "peak_epsilon": round(float(np.max(eps_from_table)), 4),
        "is_non_monotone": bool(np.argmax(eps_from_table) not in [0, len(Z) - 1]),
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def run_comparison() -> dict:
    table_raw = table_chi2_comparison()
    lcdm_fit = fit_lcdm()

    # Use optimized ΛCDM chi² for primary comparison; Table A1 ΛCDM as secondary
    chi2_lcdm_opt = lcdm_fit["chi2_min"]
    chi2_lcdm_table = table_raw["chi2_LCDM"]
    chi2_mult = table_raw["chi2_MULTING"]

    sel_opt = model_selection_table(chi2_lcdm_opt, chi2_mult)
    sel_tab = model_selection_table(chi2_lcdm_table, chi2_mult)

    eps_diag = epsilon_diagnostics()

    report = {
        "audit": "AIC_MODEL_COMPARISON",
        "labels": [
            "NOT_VALIDATION",
            "NOT_REFUTATION",
            "INTERNAL_DIAGNOSTIC_ONLY",
            "NOT_AUTHOR_CONFIRMED",
            "OUR_RECONSTRUCTION",
            "IN_SAMPLE_ONLY",
            "TABLE_A1_ONLY",
        ],
        "N_data_points": N,
        "methodology_reference": "arXiv:2504.09054v2 (2025) — AIC/BIC for 2-param dark energy extensions",
        "chi2_summary": {
            "LCDM_table_a1": table_raw["chi2_LCDM"],
            "LCDM_optimized": lcdm_fit["chi2_min"],
            "MULTING_table_a1": table_raw["chi2_MULTING"],
            "delta_chi2_table": table_raw["delta_chi2"],
            "delta_chi2_optimized": round(chi2_mult - chi2_lcdm_opt, 4),
            "note_multing_fitted_on_same_data": (
                "H_MULT was fitted to minimize residuals on these same 11 points. "
                "This is IN-SAMPLE comparison. Out-of-sample test requires bridge (Q1)."
            ),
        },
        "lcdm_best_fit": lcdm_fit,
        "model_selection_primary": {
            "comparison": "optimized_ΛCDM vs Table_A1_MULTING",
            "results": sel_opt,
        },
        "model_selection_secondary": {
            "comparison": "Table_A1_ΛCDM vs Table_A1_MULTING (both at same H0)",
            "results": sel_tab,
        },
        "epsilon_diagnostics": eps_diag,
        "key_findings": _key_findings(chi2_lcdm_opt, chi2_mult, sel_opt),
        "what_this_does_not_mean": [
            "MULTING is validated or refuted as a physical theory",
            "MULTING predictions are correct for future/unseen H(z) data",
            "beta_d=4.5 and beta_q=18.0 are physically motivated constants",
            "The bridge formula F_oP→H_MULT(z) is known or correct",
            "This analysis is publishable without author confirmation (Q1, Q2, Q3)",
        ],
        "next_step": (
            "Out-of-sample test with DESI 2024 H(z) data requires bridge formula (Q1 from TJB). "
            "Current comparison is descriptive: MULTING fits Table A1 data better than ΛCDM, "
            "but this is expected since H_MULT was optimized on these data."
        ),
    }

    REPORTS_DIR.mkdir(exist_ok=True)
    out_path = REPORTS_DIR / "aic_model_comparison.json"
    out_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Report written to: {out_path}")
    _print_summary(report)
    return report


def _key_findings(chi2_lcdm: float, chi2_mult: float, sel: dict) -> list[str]:
    delta = chi2_mult - chi2_lcdm
    findings = [
        f"χ²_ΛCDM (optimized) = {chi2_lcdm:.3f}, χ²_MULTING = {chi2_mult:.4f}",
        f"Δχ² = {delta:.3f} (negative = MULTING fits better)",
    ]
    for scenario, res in sel.items():
        findings.append(
            f"Scenario {scenario}: ΔAIC={res['delta_AIC']:.2f} ({res['AIC_verdict']}), "
            f"ΔBIC={res['delta_BIC']:.2f} ({res['BIC_verdict']}), "
            f"ΔAICc={res['delta_AICc']:.2f} ({res['AICc_verdict']})"
        )
    return findings


def _print_summary(report: dict) -> None:
    print("\n" + "=" * 62)
    print("AIC/BIC MODEL COMPARISON — Table A1 (MULTING vs flat ΛCDM)")
    print("=" * 62)
    cs = report["chi2_summary"]
    print(f"\nN = {report['N_data_points']} data points (z=0.06 to z=8.50)\n")
    print(f"χ²_ΛCDM  (optimized H0, Ωm)  = {cs['LCDM_optimized']:.3f}")
    print(f"χ²_MULTING (Table A1, fixed β) = {cs['MULTING_table_a1']:.4f}")
    print(f"Δχ² = {cs['delta_chi2_optimized']:.3f}")

    print("\n--- SCENARIO A (β treated as external, k_MULTING=2) ---")
    a = report["model_selection_primary"]["results"]["A_beta_fixed"]
    print(f"  ΔAIC  = {a['delta_AIC']:+.2f}  → {a['AIC_verdict']}")
    print(f"  ΔBIC  = {a['delta_BIC']:+.2f}  → {a['BIC_verdict']}")
    print(f"  ΔAICc = {a['delta_AICc']:+.2f}  → {a['AICc_verdict']}")

    print("\n--- SCENARIO B (β_d, β_q as fitted, k_MULTING=4) ---")
    b = report["model_selection_primary"]["results"]["B_beta_fitted"]
    print(f"  ΔAIC  = {b['delta_AIC']:+.2f}  → {b['AIC_verdict']}")
    print(f"  ΔBIC  = {b['delta_BIC']:+.2f}  → {b['BIC_verdict']}")
    print(f"  ΔAICc = {b['delta_AICc']:+.2f}  → {b['AICc_verdict']}")

    eps = report["epsilon_diagnostics"]
    print(
        f"\nε(z) peak: {eps['peak_epsilon']} at z={eps['peak_z']} "
        f"(non-monotone: {eps['is_non_monotone']})"
    )

    print("\nINSIGHT: IN-SAMPLE comparison only. H_MULT was fitted on these")
    print("same 11 points → χ² improvement expected by construction.")
    print("Out-of-sample test requires bridge formula (Q1 from TJB).")
    print("=" * 62)


if __name__ == "__main__":
    run_comparison()
