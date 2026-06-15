"""
MULTING-H Audit Kit — Master Runner

Usage:
    python audit/run_audit.py

Outputs three sections:
    1. Beta provenance (three AI services)
    2. Dipole dominance audit
    3. H_MULT CPL vs DESI 2024

All numbers [VERIFIED] from Supplementary arXiv:2025.11.0598.v6
unless marked [UNKNOWN] or [INFERRED].
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from force_ratios import AI_BETA_VALUES, run_dipole_dominance_audit
from sigma_distance_desi import HMULT_CPL, run_desi_comparison, run_h0_comparison

DIVIDER = "=" * 70


def section(title: str) -> None:
    print(f"\n{DIVIDER}")
    print(f"  {title}")
    print(DIVIDER)


def beta_provenance_report() -> None:
    section("SECTION 1: BETA PROVENANCE (Supplementary, all three AI services)")
    print(f"\n{'AI Service':<22} {'β_d':>6} {'β_q':>6} {'β_q²':>8}  Source lines")
    print("-" * 60)
    bq_vals = [v["beta_q"] for v in AI_BETA_VALUES.values()]
    bd_vals = [v["beta_d"] for v in AI_BETA_VALUES.values()]
    for name, v in AI_BETA_VALUES.items():
        bq2 = v["beta_q"] ** 2
        print(
            f"{name:<22} {v['beta_d']:>6.2f} {v['beta_q']:>6.2f} {bq2:>8.2f}  Suppl. lines {v['source_lines']}"
        )
    print()
    print(
        f"β_d range:  {min(bd_vals):.2f} – {max(bd_vals):.2f}  ({max(bd_vals) / min(bd_vals):.1f}× spread)"
    )
    print(
        f"β_q range:  {min(bq_vals):.2f} – {max(bq_vals):.2f}  ({max(bq_vals) / min(bq_vals):.1f}× spread)"
    )
    print(
        f"β_q² range: {min(bq_vals) ** 2:.2f} – {max(bq_vals) ** 2:.0f}  ({max(bq_vals) ** 2 / min(bq_vals) ** 2:.0f}× spread in quadrupole amplitude)"
    )
    print("\n[VERIFIED] β values from Supplementary lines cited above.")
    print("[INFERRED] β_q² is the amplitude factor in F_q ~ β_q² / D⁴.")


def dipole_audit_report() -> None:
    section("SECTION 2: DIPOLE DOMINANCE AUDIT")
    r = run_dipole_dominance_audit()
    beta_crit = r.pop("_beta_d_critical")
    r_cluster = r.pop("_cluster_radius_Mpc")
    D_sep = r.pop("_separation_Mpc")

    print("\nFormula: F_d/F_m = 2·(k_A/c²)·β_d·r_A / (m_A·D)")
    print("[VERIFIED] from Claude Supplementary lines 1311-1319")
    print(f"\nD (inter-cluster) = {D_sep} Mpc  |  r_cluster = {r_cluster} Mpc")
    print(f"β_d_critical (F_d/F_m=1 at {D_sep} Mpc) = {beta_crit:.0f}")
    print()
    print(
        f"{'AI Service':<22} {'β_d':>6} {'F_d/F_m@50Mpc':>14} {'r_cross(Mpc)':>13} {'Dominates?':>11}"
    )
    print("-" * 72)
    for name, v in r.items():
        dom = "YES (impossible w/ current params)" if v["dominates_at_50Mpc"] else "no"
        print(
            f"{name:<22} {v['beta_d']:>6.2f} {v['Fd_over_Fm_at_50Mpc']:>14.5f} "
            f"{v['r_crossover_Mpc']:>13.4f} {dom:>11}"
        )
    print()
    print(f"β_d (Claude) = 4.5 → needs {beta_crit / 4.5:.0f}× increase for F_d/F_m=1 at 50 Mpc")
    print(f"r_crossover (Claude) = 0.153 Mpc < r_cluster = {r_cluster} Mpc")
    print("\n[VERIFIED] r_crossover=0.153 Mpc from Supplementary line 1326.")
    print("[VERDICT]  C11/C12 (dipole dominance at inter-cluster scales) FALSIFIED")
    print("           for all three AI-generated parameter sets.")


def desi_comparison_report() -> None:
    section("SECTION 3: H_MULT CPL PROJECTION vs DESI 2024")
    print("\nH_MULT CPL fit (internal diagnostic, NOT observational validation):")
    print(
        f"  w0={HMULT_CPL['w0']:.4f}  wa={HMULT_CPL['wa']:+.4f}  H0={HMULT_CPL['H0']}  MAE={HMULT_CPL['MAE_km_s_Mpc']} km/s/Mpc"
    )
    print("\nDESI 2024: arXiv:2404.03002 Table 3 (w0waCDM)\n")
    print(f"{'Dataset':<32} {'DESI w0':>8} {'Δw0/σ':>8} {'DESI wa':>8} {'Δwa/σ':>8}")
    print("-" * 70)
    for r in run_desi_comparison():
        w0_flag = "✅" if r["w0_ok"] else "❌"
        wa_flag = "✅" if r["wa_ok"] else "❌"
        print(
            f"{r['dataset']:<32} {r['DESI_w0']:>8.3f} {r['sigma_w0']:>6.2f}σ{w0_flag} "
            f"{r['DESI_wa']:>8.3f} {r['sigma_wa']:>6.2f}σ{wa_flag}"
        )
    print()
    print("H0 comparison:")
    h0 = run_h0_comparison()
    for key, v in h0.items():
        if key == "H_MULT_H0":
            continue
        tag = (
            "[UNKNOWN]"
            if "UNKNOWN" in v["note"]
            else "[WRONG baseline]"
            if "WRONG" in v["note"]
            else ""
        )
        print(f"  vs {v['model']}: H0={v['DESI_H0']} → {v['sigma']:.2f}σ  {tag}")
    print()
    print("Supplementary sign error [VERIFIED Suppl. line 1413]:")
    print("  Claude output: 'DESI hints at w₀ < −1 and w_a > 0'")
    print(
        "  DESI+CMB+DESY5 actual: w₀ = −0.725 (> −1)  wa = −1.06 (< 0)  [VERIFIED JCAP 2025 021 Table 3]"
    )
    print("  Both signs reversed.")


if __name__ == "__main__":
    print(f"\nMULTING-H AUDIT KIT — {Path(__file__).parent.parent.name}")
    print("Scope: epistemic audit of AI-generated Supplementary parameters")
    print("Security: no MCMC, no prediction, no claim of validation\n")
    beta_provenance_report()
    dipole_audit_report()
    desi_comparison_report()
    print(f"\n{DIVIDER}")
    print("  END OF AUDIT")
    print(DIVIDER)
