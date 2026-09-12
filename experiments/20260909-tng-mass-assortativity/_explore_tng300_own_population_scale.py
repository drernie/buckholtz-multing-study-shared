"""EXPLORATORY, not a claim -- fine-grained NN-scale bracket on TNG300's
own already-cached top_halos_pos_mass.csv (N=1461, no new API call).

Purpose: pick ONE N_sub for TNG300 whose median AND mean true-NN
separation both land in v82's own 40-45 Mpc target window, WITHOUT
looking at any correlation value -- mirroring
_explore_flamingo_scale.py's own role for the FLAMINGO test.

This deliberately does NOT reuse N_sub in {30,40,50,60,80,100}: those
six values already have a KNOWN r from FINDING_scale_matched_nearest_
neighbor_rho.md's own (FALSIFIED) nested sweep, so freezing any of them
now would not be a blind pre-registration -- it would be picking the
one whose r we already like. Scanning NEW N values here keeps the
eventual choice genuinely blind to its own correlation outcome.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * exploratory only
"""

import csv
from pathlib import Path

import numpy as np

BOX_SIZE_CKPC_H = 205000.0
HUBBLE = 0.6774
IN_CSV = Path(__file__).parent / "top_halos_pos_mass.csv"


def nn_stats(pos: np.ndarray) -> tuple[float, float]:
    diff = pos[:, None, :] - pos[None, :, :]
    diff = diff - BOX_SIZE_CKPC_H * np.round(diff / BOX_SIZE_CKPC_H)
    sep_mpc = np.sqrt((diff**2).sum(axis=-1)) / HUBBLE / 1000.0
    np.fill_diagonal(sep_mpc, np.inf)
    nn_sep = sep_mpc.min(axis=1)
    return float(np.median(nn_sep)), float(nn_sep.mean())


def main() -> None:
    with open(IN_CSV) as f:
        rows = list(csv.DictReader(f))
    masses = np.array([float(r["m200_msun"]) for r in rows])
    pos = np.array([[float(r["pos_x"]), float(r["pos_y"]), float(r["pos_z"])] for r in rows])
    order = np.argsort(-masses)
    masses, pos = masses[order], pos[order]

    print(f"Full cached sample: N={len(masses)} (top_halos_pos_mass.csv, no new API call)")
    print(
        f"{'N_sub':>8}  {'mass_floor':>12}  {'median_NN':>10}  {'mean_NN':>10}  {'both_in_40-45':>14}"
    )
    # deliberately NEW values, not the {30,40,50,60,80,100} already used
    # (and already correlation-tainted) in the prior falsified sweep
    for n_sub in [35, 42, 44, 45, 46, 47, 48, 52, 55, 58, 65, 70, 75]:
        n_sub = min(n_sub, len(masses))
        med, mean = nn_stats(pos[:n_sub])
        both_in = "YES" if (40.0 <= med <= 45.0 and 40.0 <= mean <= 45.0) else "no"
        print(f"{n_sub:>8}  {masses[n_sub - 1]:>12.3e}  {med:>10.2f}  {mean:>10.2f}  {both_in:>14}")


if __name__ == "__main__":
    main()
