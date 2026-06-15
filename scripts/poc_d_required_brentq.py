"""PoC: D_required via brentq — beta=4.5/18.0. NOT_VALIDATION."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.cluster_schedule import H_OBS_DEFAULT, SIGMA_H_DEFAULT, load_claude_cluster_params
from src.d_required_solver import build_d_required_table, fit_gamma, gamma_sensitivity

BETA_D = 4.5
BETA_Q = 18.0
H_ANCHOR = 73.0
DIV = "=" * 72


def main() -> None:
    rows = load_claude_cluster_params()
    table = build_d_required_table(
        BETA_D, BETA_Q, H_ANCHOR, rows, H_OBS_DEFAULT, SIGMA_H_DEFAULT
    )

    print(f"\n{DIV}")
    print("  PoC: D_required solver  [NOT_VALIDATION]")
    print(f"  beta_d={BETA_D}, beta_q={BETA_Q}, H_anchor={H_ANCHOR}")
    print(DIV)
    print(f"  {'z':>6}  {'D_csv':>8}  {'D_req':>8}  {'ratio':>7}  {'H_obs':>7}")
    print(f"  {'-' * 45}")
    for r in table:
        ratio_s = f"{r.ratio_D_req_over_csv:.3f}" if r.ratio_D_req_over_csv == r.ratio_D_req_over_csv else "  NaN"
        print(f"  {r.z:>6.2f}  {r.D_csv:>8.1f}  {r.D_required:>8.1f}  {ratio_s:>7}  {r.H_obs:>7.1f}")

    for z_min, label in [(0.0, "z>=0"), (0.4, "z>=0.4"), (1.5, "z>=1.5")]:
        high = [r for r in table if r.z >= z_min]
        d0, gamma, r2 = fit_gamma(
            [r.z for r in high],
            [r.D_required for r in high],
            D0=table[0].D_csv,
            z_min=0.0,
        )
        print(f"\n  gamma_req ({label}): {gamma:.3f}  R2={r2:.4f}  D0={d0:.2f}")

    g_plus = gamma_sensitivity(BETA_D, BETA_Q, H_ANCHOR, 0.4, +1, rows)
    g_minus = gamma_sensitivity(BETA_D, BETA_Q, H_ANCHOR, 0.4, -1, rows)
    print(f"\n  Sensitivity H_obs +/- sigma (z>=0.4): gamma in [{g_minus:.3f}, {g_plus:.3f}]")
    print("  Document as gamma = 2.27 with sigma sensitivity range [2.21, 2.32]")
    print(f"\n{DIV}\n")


if __name__ == "__main__":
    main()
