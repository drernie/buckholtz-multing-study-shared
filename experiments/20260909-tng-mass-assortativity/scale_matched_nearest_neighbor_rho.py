"""scale_matched_nearest_neighbor_rho.py -- executes
CLAIM_scale_matched_nearest_neighbor_rho.md: measures true nearest-
neighbor mass correlation (rho) at the mass-selection scale where the
SAMPLE's own typical nearest-neighbor separation matches v82's own
fitted s(0)=45 Mpc, sweeping N_sub in {30,40,50,60,80,100} rather than
one cherry-picked value. Reuses top_halos_pos_mass.csv (already
downloaded, no new API calls).

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * L0 descriptive
NO_AUTHOR_ERROR
"""

import csv
import math
from pathlib import Path

import numpy as np

BOX_SIZE_CKPC_H = 205000.0
HUBBLE = 0.6774
IN_CSV = Path(__file__).parent / "top_halos_pos_mass.csv"
N_SUB_SWEEP = [30, 40, 50, 60, 80, 100]


def pearson(x: np.ndarray, y: np.ndarray) -> float:
    return float(np.corrcoef(x, y)[0, 1])


def t_p(r: float, n: int) -> tuple[float, str]:
    if n < 3 or abs(r) >= 1.0:
        return float("nan"), "n/a"
    df = n - 2
    t = r * math.sqrt(df) / math.sqrt(1 - r**2)
    at = abs(t)
    p = "<0.001" if at > 3.29 else "<0.01" if at > 2.58 else "<0.05" if at > 1.96 else "n.s."
    return t, p


def true_nn(pos: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    diff = pos[:, None, :] - pos[None, :, :]
    diff = diff - BOX_SIZE_CKPC_H * np.round(diff / BOX_SIZE_CKPC_H)
    sep_mpc = np.sqrt((diff**2).sum(axis=-1)) / HUBBLE / 1000.0
    np.fill_diagonal(sep_mpc, np.inf)
    nn_idx = np.argmin(sep_mpc, axis=1)
    nn_sep = sep_mpc[np.arange(len(pos)), nn_idx]
    return nn_idx, nn_sep


def main() -> None:
    rows = list(csv.DictReader(open(IN_CSV)))
    masses = np.array([float(r["m200_msun"]) for r in rows])
    pos = np.array([[float(r["pos_x"]), float(r["pos_y"]), float(r["pos_z"])] for r in rows])
    order = np.argsort(-masses)
    masses, pos = masses[order], pos[order]
    log_m_full = np.log10(masses)

    print("=" * 88)
    print("Scale-matched true-nearest-neighbor rho, swept across mass-selection N_sub")
    print("=" * 88)
    print(
        f"{'N_sub':>6} {'mass_floor':>12} {'med_NN':>8} {'mean_NN':>8} "
        f"{'r(real)':>9} {'t':>7} {'p':>7} {'r(shuffled ctrl)':>18}"
    )

    rng = np.random.default_rng(42)
    for n_sub in N_SUB_SWEEP:
        sub_pos = pos[:n_sub]
        sub_log_m = log_m_full[:n_sub]
        nn_idx, nn_sep = true_nn(sub_pos)

        r_real = pearson(sub_log_m, sub_log_m[nn_idx])
        t_real, p_real = t_p(r_real, n_sub)

        shuffled = sub_log_m.copy()
        rng.shuffle(shuffled)
        r_ctrl = pearson(shuffled, shuffled[nn_idx])

        print(
            f"{n_sub:>6} {masses[n_sub - 1]:>12.3e} {np.median(nn_sep):>8.2f} "
            f"{nn_sep.mean():>8.2f} {r_real:>9.4f} {t_real:>7.2f} {p_real:>7} {r_ctrl:>18.4f}"
        )

    print(
        "\nFor reference (already published, NOT re-derived here):\n"
        "  All-pairs, N=1461, 40-45 Mpc band:            r=+0.3827, N_pairs=4694, p<0.001\n"
        "  True-NN, full N=1461 sample (any separation):  r=+0.0192, N=1461, n.s.\n"
        "  Full-sample median true-NN separation:         9.19 Mpc (v82's own s(0)=45 Mpc)"
    )


if __name__ == "__main__":
    main()
