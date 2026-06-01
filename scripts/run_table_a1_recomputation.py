"""Run Table A1 Independent Recomputation

Usage:
    python scripts/run_table_a1_recomputation.py

Outputs:
    - docs/66_table_a1_recomputation_comparison.csv
    - docs/66_table_a1_recomputation_report.md
"""

import sys
from pathlib import Path

# Allow `python scripts/run_table_a1_recomputation.py` from the project root by
# putting the repo root (parent of scripts/) on sys.path before importing src.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.table_a1_independent_recomputation import recompute_table_a1, save_results


def main() -> None:
    """Run full recomputation and save results"""
    print("Running Table A1 independent recomputation...")
    print("=" * 70)

    # Run recomputation
    result = recompute_table_a1()

    # Print summary to console
    print("\n## Summary")
    print(f"Total rows: {result.summary['total_rows']}")
    print(
        f"H_FLRW exact matches (<0.1 km/s/Mpc): {result.summary['h_flrw_exact_matches']}/{result.summary['total_rows']}"
    )
    print(
        f"H_FLRW close matches (<0.5 km/s/Mpc): {result.summary['h_flrw_close_matches']}/{result.summary['total_rows']}"
    )
    print(
        f"Sigma_FLRW exact matches (<0.1): {result.summary['sigma_flrw_exact_matches']}/{result.summary['total_rows']}"
    )
    print(f"Max H_FLRW discrepancy: {result.summary['max_h_flrw_discrepancy']:.2f} km/s/Mpc")
    print(f"Max sigma_FLRW discrepancy: {result.summary['max_sigma_flrw_discrepancy']:.3f}")

    print("\n## Row 1 (z=0) Diagnostic")
    print(f"Best matching hypothesis: {result.row_1_diagnostic.best_hypothesis}")
    print(
        f"  Hypothesis A (standard): {'✅ MATCH' if result.row_1_diagnostic.hypothesis_a_match else '❌ NO MATCH'}"
    )
    print(
        f"  Hypothesis B (anchor): {'✅ MATCH' if result.row_1_diagnostic.hypothesis_b_match else '❌ NO MATCH'}"
    )
    print(
        f"  Hypothesis C (alternate sigma): {'✅ MATCH' if result.row_1_diagnostic.hypothesis_c_match else '❌ NO MATCH'}"
    )

    print("\n## Assumptions Registered")
    print(f"Total assumptions: {len(result.assumptions.assumptions)}")
    for i, assumption in enumerate(result.assumptions.assumptions, 1):
        print(f"{i}. {assumption.statement}")
        print(f"   Evidence: {assumption.evidence.value}")
        print(f"   Confidence: {assumption.confidence.value}")

    # Save results
    print("\n## Saving Results")
    csv_path, md_path = save_results(result, output_dir="docs")
    print(f"✅ CSV saved: {csv_path}")
    print(f"✅ Markdown report saved: {md_path}")

    print("\n" + "=" * 70)
    print("✅ Recomputation complete!")
    print("\nNext steps:")
    print("1. Review docs/66_table_a1_recomputation_report.md")
    print("2. Check docs/66_table_a1_recomputation_comparison.csv")
    print("3. Verify all assumptions are explicit")
    print("4. DO NOT SEND to author without explicit approval")


if __name__ == "__main__":
    main()
