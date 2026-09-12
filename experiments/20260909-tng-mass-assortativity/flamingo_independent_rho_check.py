"""flamingo_independent_rho_check.py -- executes
CLAIM_flamingo_independent_rho_check.md: measures true nearest-
neighbor mass correlation (rho) among the N_sub=1200 most massive
halos in the real FLAMINGO L1_m9 fiducial z=0 catalog, downloaded via
hdfstream's targeted-field access (no account/token). ONE
pre-registered threshold only -- no nested sweep, per this test's own
design fix.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * L0 descriptive
NO_AUTHOR_ERROR
"""

import math

import hdfstream
import numpy as np

N_SUB = 1200  # pre-registered, per CLAIM_flamingo_independent_rho_check.md
BOX_MPC = 1000.0  # physical Mpc at z=0 (h-scale exponent=0 on positions, confirmed)
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


def true_nn(pos: np.ndarray, box_mpc: float) -> tuple[np.ndarray, np.ndarray]:
    diff = pos[:, None, :] - pos[None, :, :]
    diff = diff - box_mpc * np.round(diff / box_mpc)
    sep = np.sqrt((diff**2).sum(axis=-1))
    np.fill_diagonal(sep, np.inf)
    nn_idx = np.argmin(sep, axis=1)
    nn_sep = sep[np.arange(len(pos)), nn_idx]
    return nn_idx, nn_sep


def main() -> None:
    root = hdfstream.open("cosma", "/")
    halo_file = root["FLAMINGO"]["L1_m9"]["L1_m9"]["SOAP-HBT"]["halo_properties_0077.hdf5"]

    print("Downloading full SO/200_crit/TotalMass array (real, ~61MB)...")
    mass_ds = halo_file["SO"]["200_crit"]["TotalMass"]
    mass = np.asarray(mass_ds[:]) * 1e10  # -> Msun, confirmed via Conversion factor attr
    order = np.argsort(-mass)
    top_idx = np.sort(order[:N_SUB])  # sorted for the remote fancy-index read

    print(f"Targeted download: positions for top {N_SUB} most massive halos...")
    pos_ds = halo_file["InputHalos"]["FOF"]["Centres"]
    pos = np.asarray(pos_ds[top_idx, :])
    top_mass = mass[top_idx]

    # re-sort by mass descending (fancy-index read returns in index order)
    reorder = np.argsort(-top_mass)
    pos, top_mass = pos[reorder], top_mass[reorder]
    log_m = np.log10(top_mass)

    print(f"N={N_SUB}, mass range {top_mass.min():.3e} - {top_mass.max():.3e} Msun")

    nn_idx, nn_sep = true_nn(pos, BOX_MPC)
    print(f"median true-NN separation: {np.median(nn_sep):.2f} Mpc")
    print(f"mean true-NN separation:   {nn_sep.mean():.2f} Mpc")

    r_real = pearson(log_m, log_m[nn_idx])
    t_real, p_real = t_p(r_real, N_SUB)

    print(f"\nPRE-REGISTERED PRIMARY RESULT: r = {r_real:.4f} (t={t_real:.2f}, p{p_real})")

    print(f"Building permutation null ({N_PERMUTATIONS} draws)...")
    rng = np.random.default_rng(20260912)
    null_rs = np.empty(N_PERMUTATIONS)
    for i in range(N_PERMUTATIONS):
        shuffled = rng.permutation(log_m)
        null_rs[i] = pearson(shuffled, shuffled[nn_idx])
    null_mean, null_sd = null_rs.mean(), null_rs.std()
    perm_p = float(np.mean(np.abs(null_rs) >= abs(r_real)))
    sigma_from_null = (r_real - null_mean) / null_sd

    print(f"\nPermutation null: mean={null_mean:.4f}, SD={null_sd:.4f}")
    print(f"Permutation p-value (two-sided): {perm_p:.4f}")
    print(f"Sigma from null: {sigma_from_null:.2f}")

    print(
        "\nFor reference (already published, NOT re-derived here):\n"
        "  TNG300 all-pairs, 40-45 Mpc band:  r=+0.3827, N_pairs=4694, p<0.001\n"
        "  TNG300 scale-matched sweep:        FALSIFIED as resolving (nested/small-N)\n"
        "  Magneticum scale-matched sweep:    FALSIFIED as resolving (7 nested pts,\n"
        "    effectively 1 measurement, r~0.16, ~1.3-1.5 sigma)"
    )


if __name__ == "__main__":
    main()
