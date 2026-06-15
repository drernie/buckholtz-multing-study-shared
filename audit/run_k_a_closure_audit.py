"""k_A closure audit orchestrator — PASS/FAIL/INCONCLUSIVE. INTERNAL_CLOSURE_TEST."""

from __future__ import annotations

import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.bridge_gate import OUTPUT_LABEL, is_mcmc_allowed
from src.cluster_schedule import H_OBS_DEFAULT, SIGMA_H_DEFAULT, load_claude_cluster_params
from src.d_required_solver import build_d_required_table, fit_gamma
from src.k_a_closure_test import run_k_a_closure_test
from src.k_a_independent import k_a_ratio_indep_vs_csv

DIV = "=" * 72
OUT = Path(__file__).resolve().parent / "output" / "k_a_closure_report.csv"


def main() -> None:
    rows = load_claude_cluster_params()
    print(f"\n{DIV}")
    print("  k_A CLOSURE AUDIT  [NOT_VALIDATION | MCMC BLOCKED]")
    print(DIV)

    ratios = k_a_ratio_indep_vs_csv(rows)
    print("\n  k_A_indep / k_A_csv:")
    for r, ratio in zip(rows, ratios, strict=True):
        print(f"    z={r.z:5.2f}  ratio={ratio:.4f}")

    d_table = build_d_required_table(
        4.5, 18.0, 73.0, rows, H_OBS_DEFAULT, SIGMA_H_DEFAULT
    )
    high = [r for r in d_table if r.z >= 0.4]
    _d0, gamma, r2 = fit_gamma(
        [r.z for r in high], [r.D_required for r in high], D0=d_table[0].D_csv
    )
    print(f"\n  D_required fit (z>=0.4): gamma={gamma:.3f}  R2={r2:.4f}")

    results = []
    for arm in ("D_csv", "D_eff"):
        res = run_k_a_closure_test(rows, H_OBS_DEFAULT, SIGMA_H_DEFAULT, arm=arm)
        sym = res.verdict.value
        print(f"\n  [{arm}] {sym}")
        print(f"    RMS_csv_k={res.rms_csv_k:.4f}  RMS_indep={res.rms_indep_k:.4f}")
        print(f"    threshold={res.rms_multiplier}× baseline={res.baseline_rms:.4f}")
        print(f"    {res.interpretation}")
        results.append(res)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["arm", "verdict", "rms_csv_k", "rms_indep_k", "label", "mcmc"])
        for r in results:
            w.writerow([r.arm, r.verdict.value, r.rms_csv_k, r.rms_indep_k, r.label, is_mcmc_allowed])
    print(f"\n  CSV: {OUT}")
    print(f"  Label: {OUTPUT_LABEL}")
    print(f"{DIV}\n")


if __name__ == "__main__":
    main()
