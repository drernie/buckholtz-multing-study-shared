"""Double-inversion diagnostic orchestrator — isolines then grid search."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.bridge_phi import h_mult_from_params_list, phi_force_sum
from src.cluster_schedule import (
    H_OBS_DEFAULT,
    SIGMA_H_DEFAULT,
    cluster_rows_to_params_list,
    load_claude_cluster_params,
)
from src.double_inversion_grid import run_parametric_grid_search
from src.double_inversion_isoline import run_isoline_diagnostic
from src.double_inversion_plots import generate_all_plots, plot_h_comparison

BETA_D = 4.5
BETA_Q = 18.0
H_ANCHOR = 73.0
DIV = "=" * 72


def main() -> None:
    rows = load_claude_cluster_params()
    H = H_OBS_DEFAULT
    r0 = rows[0]
    phi0 = phi_force_sum(r0.m_A, r0.k_A, r0.r_A, r0.D, BETA_D, BETA_Q)

    print(f"\n{DIV}")
    print("  DOUBLE INVERSION DIAGNOSTIC  [VERIFIED_DIAGNOSTIC | NOT_VALIDATION]")
    print(DIV)

    print("\n  Stage 1 — isoline bins:")
    iso = run_isoline_diagnostic(rows, H, BETA_D, BETA_Q, H_ANCHOR)
    n_adm = sum(1 for b in iso if b.admissible_exists)
    n_csv_in = sum(1 for b in iso if b.csv_in_physical_box)
    for b in iso:
        print(
            f"    z={b.z:5.2f}  adm={b.admissible_exists}  "
            f"csv_in_box={b.csv_in_physical_box}  dist={b.distance_csv_to_isoline:.2f}"
        )
    print(f"  Summary: {n_adm}/{len(iso)} bins have admissible (D,k_A); CSV in box: {n_csv_in}/{len(iso)}")

    print("\n  Stage 2 — grid search gamma × alpha:")
    summary = run_parametric_grid_search(rows, H, SIGMA_H_DEFAULT, n_gamma=21, n_alpha=25)
    bu = summary.best_unconstrained
    bp = summary.best_physical
    if bu:
        print(f"    best unconstrained: gamma={bu.gamma:.3f} alpha={bu.alpha:.3f} MAE={bu.mae:.2f}")
    if bp:
        print(f"    best physical:      gamma={bp.gamma:.3f} alpha={bp.alpha:.3f} MAE={bp.mae:.2f}")
    else:
        print("    best physical: NONE in grid")

    plot_paths = generate_all_plots(rows, H, summary, phi0, H_ANCHOR, BETA_D, BETA_Q)
    params_csv = cluster_rows_to_params_list(rows)
    H_csv = h_mult_from_params_list(params_csv, BETA_D, BETA_Q, H_ANCHOR)
    H_unc = H_phys = None
    if bu:
        from src.cluster_schedule import D_power_law, k_a_power_law

        Dv = [D_power_law(r.z, r0.D, bu.gamma) for r in rows]
        kv = [k_a_power_law(r.z, r0.k_A, bu.alpha) for r in rows]
        H_unc = h_mult_from_params_list(
            cluster_rows_to_params_list(rows, D_override=Dv, k_override=kv),
            BETA_D, BETA_Q, H_ANCHOR,
        )
    if bp:
        from src.cluster_schedule import D_power_law, k_a_power_law

        Dv = [D_power_law(r.z, r0.D, bp.gamma) for r in rows]
        kv = [k_a_power_law(r.z, r0.k_A, bp.alpha) for r in rows]
        H_phys = h_mult_from_params_list(
            cluster_rows_to_params_list(rows, D_override=Dv, k_override=kv),
            BETA_D, BETA_Q, H_ANCHOR,
        )
    hz_path = plot_paths[0].parent / "h_z_comparison.png"
    plot_h_comparison([r.z for r in rows], H, H_csv, H_unc, H_phys, hz_path)
    plot_paths.append(hz_path)

    print("\n  Plots:")
    for p in plot_paths:
        print(f"    {p}")
    print("\n  See docs/DOUBLE_INVERSION_DIAGNOSTIC.md")
    print(f"{DIV}\n")


if __name__ == "__main__":
    main()
