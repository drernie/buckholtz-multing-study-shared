"""tng300_own_population_rho_nn_and_band.py -- executes
CLAIM_tng300_own_population_rho_nn_and_band.md: on TNG300's own real,
already-cached top_halos_pos_mass.csv (N=1461, no new API call),
measures BOTH rho_NN and rho_band on the SAME frozen N_SUB=35 subsample
(the one candidate, among 13 scanned NEW values, whose median AND mean
true-NN separation both land in v82's own 40-45 Mpc target window) --
the real discriminating test named but not run in
FINDING_flamingo_addendum_jackknife_band_closure.md.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * L0 descriptive
NO_AUTHOR_ERROR
"""

import csv
import math
from pathlib import Path

import numpy as np

N_SUB = 35  # pre-registered, per CLAIM_tng300_own_population_rho_nn_and_band.md
BOX_SIZE_CKPC_H = 205000.0
HUBBLE = 0.6774
BAND_LO, BAND_HI = 40.0, 45.0
N_PERMUTATIONS = 1000
IN_CSV = Path(__file__).parent / "top_halos_pos_mass.csv"


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


def periodic_sep_matrix(pos: np.ndarray) -> np.ndarray:
    diff = pos[:, None, :] - pos[None, :, :]
    diff = diff - BOX_SIZE_CKPC_H * np.round(diff / BOX_SIZE_CKPC_H)
    return np.sqrt((diff**2).sum(axis=-1)) / HUBBLE / 1000.0  # -> physical Mpc


def rho_nn(log_m: np.ndarray, sep: np.ndarray) -> tuple[float, np.ndarray]:
    sep = sep.copy()
    np.fill_diagonal(sep, np.inf)
    nn_idx = np.argmin(sep, axis=1)
    return pearson(log_m, log_m[nn_idx]), nn_idx


def rho_band(log_m: np.ndarray, sep: np.ndarray, lo: float, hi: float) -> tuple[float, int, tuple]:
    n = len(log_m)
    iu, ju = np.triu_indices(n, k=1)
    s = sep[iu, ju]
    mask = (s >= lo) & (s <= hi)
    i_sel, j_sel = iu[mask], ju[mask]
    n_pairs = len(i_sel)
    if n_pairs < 3:
        return float("nan"), n_pairs, (i_sel, j_sel)
    x = np.concatenate([log_m[i_sel], log_m[j_sel]])
    y = np.concatenate([log_m[j_sel], log_m[i_sel]])
    return pearson(x, y), n_pairs, (i_sel, j_sel)


def main() -> None:
    with open(IN_CSV) as f:
        rows = list(csv.DictReader(f))
    masses = np.array([float(r["m200_msun"]) for r in rows])
    pos_all = np.array([[float(r["pos_x"]), float(r["pos_y"]), float(r["pos_z"])] for r in rows])
    order = np.argsort(-masses)
    masses, pos_all = masses[order], pos_all[order]

    top_mass = masses[:N_SUB]
    top_pos = pos_all[:N_SUB]
    log_m = np.log10(top_mass)

    print(f"N={N_SUB} (real TNG300, cached, no new API call)")
    print(f"mass range: {top_mass.min():.3e} - {top_mass.max():.3e} Msun")

    sep = periodic_sep_matrix(top_pos)

    r_nn, nn_idx = rho_nn(log_m, sep)
    nn_sep = sep[np.arange(N_SUB), nn_idx]
    print(f"median true-NN separation: {np.median(nn_sep):.2f} Mpc")
    print(f"mean true-NN separation:   {nn_sep.mean():.2f} Mpc")

    r_band, n_pairs_band, (i_sel, j_sel) = rho_band(log_m, sep, BAND_LO, BAND_HI)

    t_nn, p_nn = t_p(r_nn, N_SUB)
    print(f"\nrho_NN   = {r_nn:.4f} (t={t_nn:.2f}, p{p_nn})")
    print(f"rho_band = {r_band:.4f} (N_pairs={n_pairs_band}, {BAND_LO}-{BAND_HI} Mpc)")

    print(f"\nBuilding permutation null for rho_NN ({N_PERMUTATIONS} draws)...")
    rng = np.random.default_rng(20260912)
    null_nn = np.empty(N_PERMUTATIONS)
    for i in range(N_PERMUTATIONS):
        shuffled = rng.permutation(log_m)
        null_nn[i] = pearson(shuffled, shuffled[nn_idx])
    print(f"  null mean={null_nn.mean():.4f}, SD={null_nn.std():.4f}")
    print(f"  perm p-value (two-sided): {float(np.mean(np.abs(null_nn) >= abs(r_nn))):.4f}")

    if n_pairs_band >= 3:
        print(f"\nBuilding permutation null for rho_band ({N_PERMUTATIONS} draws)...")
        null_band = np.empty(N_PERMUTATIONS)
        for i in range(N_PERMUTATIONS):
            shuffled = rng.permutation(log_m)
            x = np.concatenate([shuffled[i_sel], shuffled[j_sel]])
            y = np.concatenate([shuffled[j_sel], shuffled[i_sel]])
            null_band[i] = pearson(x, y)
        print(f"  null mean={null_band.mean():.4f}, SD={null_band.std():.4f}")
        print(f"  perm p-value (two-sided): {float(np.mean(np.abs(null_band) >= abs(r_band))):.4f}")
    else:
        print("\nrho_band: too few pairs for a permutation null.")

    print(
        "\nFor reference (already published, NOT re-derived here):\n"
        "  TNG300 FULL sample (N=1461, non-mass-matched), 40-45 Mpc band:\n"
        "    r=+0.3827, N_pairs=4694, p<0.001\n"
        "  FLAMINGO (N=1200, mass-matched, SAME protocol as this test):\n"
        "    rho_NN=-0.0231, rho_band=+0.0271 (N_pairs=127)"
    )


if __name__ == "__main__":
    main()
