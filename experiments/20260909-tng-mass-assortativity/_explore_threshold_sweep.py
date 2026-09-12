"""EXPLORATORY, not a claim -- cheap feasibility check (PVF/compute-first)
before writing any claim.md: does ANY mass-selection sub-threshold of the
already-downloaded top_halos_pos_mass.csv give a typical nearest-neighbor
separation near v82's own fitted s(0)=45 Mpc? If yes, a real test is
worth designing. If no feasible threshold exists, that is itself the
answer and this file's own output is the evidence for it.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * exploratory only
"""

import csv
from pathlib import Path

import numpy as np

BOX_SIZE_CKPC_H = 205000.0
HUBBLE = 0.6774
IN_CSV = Path(__file__).parent / "top_halos_pos_mass.csv"


def nn_stats(pos: np.ndarray) -> tuple[float, float, float]:
    diff = pos[:, None, :] - pos[None, :, :]
    diff = diff - BOX_SIZE_CKPC_H * np.round(diff / BOX_SIZE_CKPC_H)
    sep_mpc = np.sqrt((diff**2).sum(axis=-1)) / HUBBLE / 1000.0
    np.fill_diagonal(sep_mpc, np.inf)
    nn_sep = sep_mpc.min(axis=1)
    return float(np.median(nn_sep)), float(nn_sep.mean()), float(nn_sep.max())


def main() -> None:
    rows = list(csv.DictReader(open(IN_CSV)))
    masses = np.array([float(r["m200_msun"]) for r in rows])
    pos = np.array([[float(r["pos_x"]), float(r["pos_y"]), float(r["pos_z"])] for r in rows])
    order = np.argsort(-masses)  # most massive first
    masses, pos = masses[order], pos[order]

    print(f"Full sample: N={len(masses)}, mass range {masses.min():.3e} - {masses.max():.3e} Msun")
    print(f"{'N_sub':>8}  {'mass_floor':>12}  {'median_NN':>10}  {'mean_NN':>10}  {'max_NN':>10}")
    for n_sub in [50, 100, 150, 200, 300, 400, 500, 700, 1000, 1461]:
        n_sub = min(n_sub, len(masses))
        med, mean, mx = nn_stats(pos[:n_sub])
        print(f"{n_sub:>8}  {masses[n_sub - 1]:>12.3e}  {med:>10.2f}  {mean:>10.2f}  {mx:>10.2f}")


if __name__ == "__main__":
    main()
