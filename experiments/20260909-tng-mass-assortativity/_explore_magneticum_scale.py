"""EXPLORATORY, not a claim -- check the natural typical nearest-
neighbor separation of the real Magneticum Box2_hr/snap_140 (z=0.033)
cluster catalog, both un-thinned and across a mass-threshold sweep, to
see whether v82's own 40-45 Mpc target is reachable without (or with
minimal) the same mass-rank-thinning confound already flagged in
FINDING_scale_matched_nearest_neighbor_rho.md.
"""

from pathlib import Path

import numpy as np

BOX_SIZE_KPC_H = 352000.0  # Box2_hr, per magneticum.org/simulations.html
HUBBLE = 0.704  # Magneticum WMAP7, per simulations.html
IN_FILE = Path(__file__).parent / "data_cache" / "magneticum_box2hr_snap140_cluster.txt"


def true_nn(pos_kpc_h: np.ndarray) -> np.ndarray:
    diff = pos_kpc_h[:, None, :] - pos_kpc_h[None, :, :]
    diff = diff - BOX_SIZE_KPC_H * np.round(diff / BOX_SIZE_KPC_H)
    sep_kpc_h = np.sqrt((diff**2).sum(axis=-1))
    np.fill_diagonal(sep_kpc_h, np.inf)
    return sep_kpc_h.min(axis=1) / HUBBLE / 1000.0  # -> physical Mpc, matching v82's own units


def main() -> None:
    data = np.genfromtxt(IN_FILE, comments="#")
    uid, x, y, z, m500c = data[:, 0], data[:, 1], data[:, 2], data[:, 3], data[:, 7]
    pos = np.stack([x, y, z], axis=1)
    print(f"N clusters = {len(uid)}, m500c range: {m500c.min():.3e} - {m500c.max():.3e} Msun/h")

    order = np.argsort(-m500c)
    pos, m500c = pos[order], m500c[order]

    nn_sep_full = true_nn(pos)  # physical Mpc
    print(
        f"\nFull catalog (N={len(m500c)}): median NN = {np.median(nn_sep_full):.2f} "
        f"Mpc, mean = {nn_sep_full.mean():.2f} Mpc"
    )

    print(f"\n{'N_sub':>8} {'mass_floor(Msun/h)':>20} {'med_NN(Mpc)':>15} {'mean_NN(Mpc)':>16}")
    for n_sub in [50, 75, 100, 125, 150, 175, 200, 500, 1000, 2000, 3000, 5000, len(m500c)]:
        n_sub = min(n_sub, len(m500c))
        nn_sep = true_nn(pos[:n_sub])
        print(
            f"{n_sub:>8} {m500c[n_sub - 1]:>20.3e} {np.median(nn_sep):>15.2f} {nn_sep.mean():>16.2f}"
        )


if __name__ == "__main__":
    main()
