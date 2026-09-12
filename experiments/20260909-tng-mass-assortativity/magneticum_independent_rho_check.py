"""magneticum_independent_rho_check.py -- executes
CLAIM_magneticum_independent_rho_check.md: measures true nearest-
neighbor mass correlation (rho) in a real, independent Magneticum
Box2_hr cluster catalog (different code, different cosmology from TNG),
at the mass-selection scale matching v82's own 40-45 Mpc target,
sweeping N_sub across a bracketing range with a PROPER permutation-null
distribution (not a single shuffle draw).

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * L0 descriptive
NO_AUTHOR_ERROR
"""

import math
from pathlib import Path

import numpy as np

BOX_SIZE_KPC_H = 352000.0  # Box2_hr
HUBBLE = 0.704
IN_FILE = Path(__file__).parent / "data_cache" / "magneticum_box2hr_snap140_cluster.txt"
N_SUB_SWEEP = [100, 110, 120, 125, 130, 140, 150]
N_PERMUTATIONS = 1000


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


def true_nn(pos_kpc_h: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    diff = pos_kpc_h[:, None, :] - pos_kpc_h[None, :, :]
    diff = diff - BOX_SIZE_KPC_H * np.round(diff / BOX_SIZE_KPC_H)
    sep_kpc_h = np.sqrt((diff**2).sum(axis=-1))
    np.fill_diagonal(sep_kpc_h, np.inf)
    nn_idx = np.argmin(sep_kpc_h, axis=1)
    nn_sep_mpc = sep_kpc_h[np.arange(len(pos_kpc_h)), nn_idx] / HUBBLE / 1000.0
    return nn_idx, nn_sep_mpc


def main() -> None:
    data = np.genfromtxt(IN_FILE, comments="#")
    x, y, z, m500c = data[:, 1], data[:, 2], data[:, 3], data[:, 7]
    pos = np.stack([x, y, z], axis=1)
    order = np.argsort(-m500c)
    pos, m500c = pos[order], m500c[order]
    log_m_full = np.log10(m500c)
    print(f"N clusters = {len(m500c)}, m500c range {m500c.min():.3e} - {m500c.max():.3e} Msun/h")

    print("=" * 100)
    print(f"Scale-matched true-NN rho, Magneticum Box2_hr, permutation null (N={N_PERMUTATIONS})")
    print("=" * 100)
    print(
        f"{'N_sub':>6} {'mass_floor':>12} {'med_NN':>7} {'mean_NN':>8} "
        f"{'r(real)':>9} {'t':>7} {'p':>7} {'null_mean':>10} {'null_SD':>9} {'perm_p':>8}"
    )

    rng = np.random.default_rng(20260912)
    for n_sub in N_SUB_SWEEP:
        sub_pos = pos[:n_sub]
        sub_log_m = log_m_full[:n_sub]
        nn_idx, nn_sep = true_nn(sub_pos)

        r_real = pearson(sub_log_m, sub_log_m[nn_idx])
        t_real, p_real = t_p(r_real, n_sub)

        null_rs = np.empty(N_PERMUTATIONS)
        for i in range(N_PERMUTATIONS):
            shuffled = rng.permutation(sub_log_m)
            null_rs[i] = pearson(shuffled, shuffled[nn_idx])
        null_mean, null_sd = null_rs.mean(), null_rs.std()
        perm_p = float(np.mean(np.abs(null_rs) >= abs(r_real)))

        print(
            f"{n_sub:>6} {m500c[n_sub - 1]:>12.3e} {np.median(nn_sep):>7.2f} "
            f"{nn_sep.mean():>8.2f} {r_real:>9.4f} {t_real:>7.2f} {p_real:>7} "
            f"{null_mean:>10.4f} {null_sd:>9.4f} {perm_p:>8.4f}"
        )

    print(
        "\nFor reference (already published, NOT re-derived here):\n"
        "  TNG300 all-pairs, 40-45 Mpc band:  r=+0.3827, N_pairs=4694, p<0.001\n"
        "  TNG300 true-NN, full sample:       r=+0.0192, N=1461, n.s.\n"
        "  TNG300 scale-matched sweep:        FALSIFIED as a resolving test (see\n"
        "    FINDING_scale_matched_nearest_neighbor_rho.md)"
    )


if __name__ == "__main__":
    main()
