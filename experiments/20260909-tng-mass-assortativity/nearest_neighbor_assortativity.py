"""
Nearest-neighbor-restricted mass assortativity -- closes the scope gap
FINDING_mass_assortativity_and_scatter.md named explicitly: the original
pair_mass_correlation.py measurement used EVERY pair in the 40-45 Mpc
separation band, which over-counts halos that are also close to several
other massive neighbors. v82's own bridge treats a specific pair
(nearest-neighbor-like), not "any two halos that happen to be ~40 Mpc
apart amid 1500 other massive halos."

Reuses top_halos_pos_mass.csv (N=1461, already fetched -- no new API
calls). For each halo, finds its single nearest neighbor among the same
sample, then asks the more precisely-matched question: among halos whose
TRUE nearest neighbor separation falls in the 40-45 Mpc band, is there
still a real mass correlation?

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
TARGET_BAND_MPC = (40.0, 45.0)


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


def main() -> None:
    rows = list(csv.DictReader(open(IN_CSV)))
    n = len(rows)
    masses = np.array([float(r["m200_msun"]) for r in rows])
    pos = np.array([[float(r["pos_x"]), float(r["pos_y"]), float(r["pos_z"])] for r in rows])
    log_m = np.log10(masses)

    print(f"N halos = {n}")

    diff = pos[:, None, :] - pos[None, :, :]
    diff = diff - BOX_SIZE_CKPC_H * np.round(diff / BOX_SIZE_CKPC_H)
    sep_ckpc_h = np.sqrt((diff**2).sum(axis=-1))
    sep_mpc = sep_ckpc_h / HUBBLE / 1000.0
    np.fill_diagonal(sep_mpc, np.inf)  # exclude self

    nn_idx = np.argmin(sep_mpc, axis=1)
    nn_sep = sep_mpc[np.arange(n), nn_idx]
    nn_log_m_self = log_m
    nn_log_m_neighbor = log_m[nn_idx]

    print("\n=== Nearest-neighbor separation distribution (all N=1461 halos) ===")
    print(
        f"min={nn_sep.min():.3f}  max={nn_sep.max():.3f}  "
        f"median={np.median(nn_sep):.3f}  mean={nn_sep.mean():.3f} Mpc"
    )

    print("\n=== Mass correlation among ALL nearest-neighbor pairs (any separation) ===")
    r_all_nn = pearson(nn_log_m_self, nn_log_m_neighbor)
    t_all, p_all = t_p(r_all_nn, n)
    print(
        f"N={n}, r(log M_self, log M_nearest_neighbor) = {r_all_nn:.4f} (t={t_all:.2f}, p{p_all})"
    )

    print(
        f"\n=== Headline: nearest-neighbor pairs whose separation falls in "
        f"{TARGET_BAND_MPC[0]}-{TARGET_BAND_MPC[1]} Mpc (v82's own node separation) ==="
    )
    mask_band = (nn_sep >= TARGET_BAND_MPC[0]) & (nn_sep < TARGET_BAND_MPC[1])
    n_band = int(mask_band.sum())
    print(f"N halos whose true nearest neighbor is in this band = {n_band} (of {n})")
    if n_band >= 10:
        r_band = pearson(nn_log_m_self[mask_band], nn_log_m_neighbor[mask_band])
        t_band, p_band = t_p(r_band, n_band)
        print(f"r(log M_self, log M_nearest_neighbor) = {r_band:.4f} (t={t_band:.2f}, p{p_band})")
    else:
        print("Too few nearest-neighbor pairs land in this exact band for a reliable number.")

    print("\n=== Negative control: shuffle masses, recompute on the same band-restricted set ===")
    rng = np.random.default_rng(42)
    shuffled = log_m.copy()
    rng.shuffle(shuffled)
    shuffled_neighbor = shuffled[nn_idx]
    if n_band >= 10:
        r_shuf = pearson(shuffled[mask_band], shuffled_neighbor[mask_band])
        print(f"Shuffled-mass r (band-restricted) = {r_shuf:.4f} (expected ~0)")

    print("\n=== Comparison against the original all-pairs (non-nearest-neighbor) result ===")
    print("Original pair_mass_correlation.py (all pairs, 40-45 Mpc band): r=0.3827, N_pairs=4694")
    print(
        f"This nearest-neighbor-restricted result: "
        f"r={pearson(nn_log_m_self[mask_band], nn_log_m_neighbor[mask_band]) if n_band >= 10 else float('nan'):.4f}, "
        f"N_halos={n_band}"
    )


if __name__ == "__main__":
    main()
