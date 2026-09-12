"""flamingo_addendum_jackknife_band_closure.py -- executes
CLAIM_flamingo_addendum_jackknife_band_closure.md: on the SAME frozen
N_SUB=1200 FLAMINGO L1_m9 subsample used by
flamingo_independent_rho_check.py, adds (1) the all-pairs-in-band
observable rho_band, and (2) a real CI for both rho_NN and rho_band via
spatial delete-one-block jackknife -- replacing the withdrawn
"permutation-null-SD as 13-sigma exclusion" claim with a properly
constructed test of H0: rho<=-0.5.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * L0 descriptive
NO_AUTHOR_ERROR
"""

import math

import hdfstream
import numpy as np

N_SUB = 1200  # SAME pre-registered N as the prior FLAMINGO test
BOX_MPC = 1000.0  # physical Mpc at z=0 (h-scale exponent=0, confirmed)
BAND_LO, BAND_HI = 40.0, 45.0  # v82's own target window
N_BLOCKS_PER_SIDE = 5  # 125 blocks, 200 Mpc/side >> ~42 Mpc typical NN sep
THRESHOLD = -0.5  # FINDING_P158's own directional-safety threshold


def pearson(x: np.ndarray, y: np.ndarray) -> float:
    return float(np.corrcoef(x, y)[0, 1])


def periodic_sep_matrix(pos: np.ndarray, box_mpc: float) -> np.ndarray:
    diff = pos[:, None, :] - pos[None, :, :]
    diff = diff - box_mpc * np.round(diff / box_mpc)
    return np.sqrt((diff**2).sum(axis=-1))


def rho_nn(log_m: np.ndarray, sep: np.ndarray) -> float:
    sep = sep.copy()
    np.fill_diagonal(sep, np.inf)
    nn_idx = np.argmin(sep, axis=1)
    return pearson(log_m, log_m[nn_idx])


def rho_band(log_m: np.ndarray, sep: np.ndarray, lo: float, hi: float) -> tuple[float, int]:
    n = len(log_m)
    iu, ju = np.triu_indices(n, k=1)
    s = sep[iu, ju]
    mask = (s >= lo) & (s <= hi)
    i_sel, j_sel = iu[mask], ju[mask]
    n_pairs = len(i_sel)
    if n_pairs < 3:
        return float("nan"), n_pairs
    x = np.concatenate([log_m[i_sel], log_m[j_sel]])
    y = np.concatenate([log_m[j_sel], log_m[i_sel]])
    return pearson(x, y), n_pairs


def block_id(pos: np.ndarray, box_mpc: float, n_per_side: int) -> np.ndarray:
    block_size = box_mpc / n_per_side
    idx = np.floor((pos % box_mpc) / block_size).astype(int)
    idx = np.clip(idx, 0, n_per_side - 1)
    return idx[:, 0] * n_per_side * n_per_side + idx[:, 1] * n_per_side + idx[:, 2]


def jackknife_se(
    pos: np.ndarray, log_m: np.ndarray, box_mpc: float, n_per_side: int, lo: float, hi: float
) -> dict:
    blocks = block_id(pos, box_mpc, n_per_side)
    unique_blocks = np.unique(blocks)
    nn_vals, band_vals, band_npairs = [], [], []
    for b in unique_blocks:
        keep = blocks != b
        if keep.sum() < 10:
            continue
        sub_pos, sub_log_m = pos[keep], log_m[keep]
        sub_sep = periodic_sep_matrix(sub_pos, box_mpc)
        nn_vals.append(rho_nn(sub_log_m, sub_sep))
        r_b, npairs = rho_band(sub_log_m, sub_sep, lo, hi)
        band_vals.append(r_b)
        band_npairs.append(npairs)

    nn_vals = np.array(nn_vals)
    band_vals = np.array(band_vals)
    k = len(nn_vals)

    def jack_se(vals: np.ndarray) -> float:
        vals = vals[~np.isnan(vals)]
        kk = len(vals)
        if kk < 2:
            return float("nan")
        mean = vals.mean()
        return math.sqrt((kk - 1) / kk * np.sum((vals - mean) ** 2))

    return {
        "k_blocks_used": k,
        "nn_se": jack_se(nn_vals),
        "band_se": jack_se(band_vals),
        "band_npairs_range": (min(band_npairs), max(band_npairs)) if band_npairs else (0, 0),
    }


def ci_report(point: float, se: float, label: str, threshold: float) -> None:
    for z, level in [(1.96, "95%"), (2.576, "99%")]:
        lo, hi = point - z * se, point + z * se
        excludes = "YES" if threshold < lo or threshold > hi else "NO"
        print(
            f"  {label} {level} CI: [{lo:.4f}, {hi:.4f}]  -- excludes rho={threshold}? {excludes}"
        )


def main() -> None:
    root = hdfstream.open("cosma", "/")
    halo_file = root["FLAMINGO"]["L1_m9"]["L1_m9"]["SOAP-HBT"]["halo_properties_0077.hdf5"]

    print("Downloading full SO/200_crit/TotalMass array (real, ~61MB)...")
    mass_ds = halo_file["SO"]["200_crit"]["TotalMass"]
    mass = np.asarray(mass_ds[:]) * 1e10  # -> Msun
    order = np.argsort(-mass)
    top_idx = np.sort(order[:N_SUB])

    print(f"Targeted download: positions for the SAME top {N_SUB} halos...")
    pos_ds = halo_file["InputHalos"]["FOF"]["Centres"]
    pos = np.asarray(pos_ds[top_idx, :])
    top_mass = mass[top_idx]

    reorder = np.argsort(-top_mass)
    pos, top_mass = pos[reorder], top_mass[reorder]
    log_m = np.log10(top_mass)

    print(f"N={N_SUB}, mass range {top_mass.min():.3e} - {top_mass.max():.3e} Msun")

    sep = periodic_sep_matrix(pos, BOX_MPC)

    r_nn = rho_nn(log_m, sep)
    r_band, n_pairs_band = rho_band(log_m, sep, BAND_LO, BAND_HI)

    print(f"\nrho_NN   (true nearest-neighbor, same as prior test): {r_nn:.4f}")
    print(f"rho_band (all pairs, {BAND_LO}-{BAND_HI} Mpc, N_pairs={n_pairs_band}): {r_band:.4f}")

    print(f"\nSpatial delete-one-block jackknife ({N_BLOCKS_PER_SIDE}^3 grid)...")
    jk = jackknife_se(pos, log_m, BOX_MPC, N_BLOCKS_PER_SIDE, BAND_LO, BAND_HI)
    print(f"blocks used: {jk['k_blocks_used']}")
    print(f"rho_NN jackknife SE:   {jk['nn_se']:.4f}")
    print(f"rho_band jackknife SE: {jk['band_se']:.4f}")
    print(f"rho_band N_pairs range across jackknife replicates: {jk['band_npairs_range']}")

    print(f"\nCI-based test of H0: rho <= {THRESHOLD}")
    print("rho_NN:")
    ci_report(r_nn, jk["nn_se"], "rho_NN", THRESHOLD)
    print("rho_band:")
    ci_report(r_band, jk["band_se"], "rho_band", THRESHOLD)

    print(
        "\nFor reference (already published, NOT re-derived here):\n"
        "  TNG300 all-pairs, 40-45 Mpc band:  r=+0.3827, N_pairs=4694, p<0.001\n"
        "  FLAMINGO rho_NN (prior test):      r=-0.0231, permutation-null SD=0.0359"
    )


if __name__ == "__main__":
    main()
