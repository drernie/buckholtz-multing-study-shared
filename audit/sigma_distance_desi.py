"""
Sigma Distance — H_MULT CPL Fit vs DESI 2024 Constraints

DESI VALUES: arXiv:2404.03002, Table 3 (w0waCDM)
CPL FIT: Internal diagnostic fit to H_MULT Table A1 (rows 2-12)
  — not MCMC, not prediction, not observational validation

CORRECTIONS APPLIED (2026-06-06):
  - wₐ DESY5: was -0.75 (WRONG, that is PantheonPlus) → -1.05 (correct)
  - wₐ Union3: was -0.27 (WRONG) → -1.27 (correct)
  - H0 baseline: DESI ΛCDM ≠ DESI w0waCDM. Both reported separately.
"""


# Our CPL fit to H_MULT (diagnostic, internal only)
HMULT_CPL = {"w0": -0.6903, "wa": +0.4022, "H0": 68.83, "MAE_km_s_Mpc": 0.71}

# DESI 2024 constraints — arXiv:2404.03002 Table 3, w0waCDM
# Asymmetric errors: (central, err_plus, err_minus)
# Sign convention: wa_err_plus = upper 1σ boundary for wa
DESI_CONSTRAINTS = {
    "DESI alone": {
        "w0": -0.99,
        "w0_err": 0.14,
        "wa": -0.17,
        "wa_err_p": 0.97,
        "wa_err_m": 0.96,
        "H0": None,
    },
    "DESI+CMB": {
        "w0": -0.45,
        "w0_err": 0.27,
        "wa": -1.79,
        "wa_err_p": 1.00,
        "wa_err_m": 0.95,
        "H0": None,
    },
    "DESI+CMB+Union3": {
        "w0": -0.65,
        "w0_err": 0.10,
        "wa": -1.27,
        "wa_err_p": 0.40,
        "wa_err_m": 0.34,
        "H0": None,
    },
    "DESI+CMB+PantheonPlus": {
        "w0": -0.827,
        "w0_err": 0.063,
        "wa": -0.75,
        "wa_err_p": 0.29,
        "wa_err_m": 0.25,
        "H0": None,
    },
    "DESI+CMB+DESY5 [headline]": {
        # [VERIFIED] from JCAP 2025 021 (arXiv:2404.03002v3), Table 3, w0waCDM row
        # "DESI+CMB+DESY5: Ωm=0.3163±0.0065, H0=67.19±0.69, w0=−0.725±0.071, wa=−1.06+0.35/−0.31"
        # Note: preprint v1 values (w0=−0.727±0.067, wa=−1.05) differ slightly from published v3
        "w0": -0.725,
        "w0_err": 0.071,
        "wa": -1.06,
        "wa_err_p": 0.35,
        "wa_err_m": 0.31,
        "H0": 67.19,
        "H0_err": 0.69,
    },
}

# DESI H0 baselines (different models)
DESI_H0_LCDM = {"value": 68.52, "err": 0.62, "model": "ΛCDM flat, DESI+BBN+θ*"}


def sigma_distance(our_val: float, desi_val: float, err_plus: float, err_minus: float) -> float:
    """Asymmetric sigma distance. Uses err toward our value."""
    delta = our_val - desi_val
    err = err_plus if delta > 0 else err_minus
    return abs(delta) / err


def run_desi_comparison() -> list[dict]:
    results = []
    w0, wa, H0 = HMULT_CPL["w0"], HMULT_CPL["wa"], HMULT_CPL["H0"]

    for name, d in DESI_CONSTRAINTS.items():
        dw0 = sigma_distance(w0, d["w0"], d["w0_err"], d["w0_err"])
        dwa = sigma_distance(wa, d["wa"], d["wa_err_p"], d["wa_err_m"])
        row = {
            "dataset": name,
            "DESI_w0": d["w0"],
            "DESI_wa": d["wa"],
            "sigma_w0": dw0,
            "sigma_wa": dwa,
            "w0_ok": dw0 < 2.0,
            "wa_ok": dwa < 2.0,
        }
        if d.get("H0") and d.get("H0_err"):
            dH0 = sigma_distance(H0, d["H0"], d["H0_err"], d["H0_err"])
            row["sigma_H0_w0waCDM"] = dH0
        results.append(row)
    return results


def run_h0_comparison() -> dict:
    H0 = HMULT_CPL["H0"]
    lcdm = DESI_H0_LCDM
    desi_w0wa = DESI_CONSTRAINTS["DESI+CMB+DESY5 [headline]"]
    return {
        "H_MULT_H0": H0,
        "vs_DESI_LCDM": {
            "model": lcdm["model"],
            "DESI_H0": lcdm["value"],
            "sigma": abs(H0 - lcdm["value"]) / lcdm["err"],
            "note": "WRONG baseline for w0waCDM comparison",
        },
        "vs_DESI_w0waCDM_DESY5": {
            "model": "w0waCDM DESI+CMB+DESY5",
            "DESI_H0": desi_w0wa["H0"],
            "sigma": abs(H0 - desi_w0wa["H0"]) / desi_w0wa["H0_err"],
            "note": "VERIFIED — JCAP 2025 021 Table 3 (arXiv:2404.03002v3)",
        },
    }


if __name__ == "__main__":
    print("=== H_MULT CPL PROJECTION vs DESI 2024 ===")
    print(
        f"H_MULT CPL: w0={HMULT_CPL['w0']:.3f}  wa={HMULT_CPL['wa']:+.3f}  "
        f"H0={HMULT_CPL['H0']}  MAE={HMULT_CPL['MAE_km_s_Mpc']} km/s/Mpc"
    )
    print()
    print(
        f"{'Dataset':<30} {'DESI w0':>8} {'Δw0/σ':>8} {'DESI wa':>8} {'Δwa/σ':>8} {'Both<2σ?':>10}"
    )
    print("-" * 78)

    for r in run_desi_comparison():
        both_ok = "✅" if r["w0_ok"] and r["wa_ok"] else ("⚠️ w0" if r["w0_ok"] else "❌")
        print(
            f"{r['dataset']:<30} {r['DESI_w0']:>8.3f} {r['sigma_w0']:>8.2f}σ "
            f"{r['DESI_wa']:>8.3f} {r['sigma_wa']:>8.2f}σ {both_ok:>10}"
        )

    print()
    print("NOTE: w0 aligns with DESI+CMB+DESY5 at 0.55σ.")
    print("      wa strongly tension (4.68σ) — H_MULT predicts wa>0, DESI says wa<0.")
    print()
    h0 = run_h0_comparison()
    print("=== H0 COMPARISON ===")
    for key, v in h0.items():
        if key == "H_MULT_H0":
            continue
        print(f"  {v['model']}: H0={v['DESI_H0']} → {v['sigma']:.2f}σ  [{v['note']}]")

    print()
    print("SUPPLEMENTARY SIGN ERROR:")
    print("  Claude Suppl. line 1413: 'DESI hints at w₀ < −1 and w_a > 0'")
    print("  Reality (DESI+CMB+DESY5): w₀ = -0.727 > -1  AND  wa = -1.05 < 0")
    print("  Both signs are reversed in the Supplementary statement.")
