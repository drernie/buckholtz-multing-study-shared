"""flamingo_subvolume_periodic_wrap_bias.py -- executes
CLAIM_flamingo_subvolume_periodic_wrap_bias.md: on the SAME 10
(cube_id, local_N) pairs already selected by
flamingo_subvolume_replication.py's own real output, compares rho_NN
under periodic (minimum-image, as already reported) vs. open-boundary
(plain Euclidean, no wraparound) nearest-neighbor treatment --
quantifying the periodic-wrap dilution bias named in that FINDING's
own Step 8a skeptic review.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * L0 descriptive
NO_AUTHOR_ERROR
"""

import hdfstream
import numpy as np

TNG300_MPC = 302.6267
N_GRID = 3
GLOBAL_N_TOP = 5000

# frozen, from flamingo_subvolume_replication.py's own already-committed
# real output -- NOT re-derived here
MATCHED_CUBES = {1: 40, 2: 55, 4: 35, 5: 30, 7: 30, 8: 30, 12: 40, 17: 45, 25: 45, 26: 50}


def pearson(x: np.ndarray, y: np.ndarray) -> float:
    return float(np.corrcoef(x, y)[0, 1])


def periodic_sep_matrix(pos: np.ndarray, box_mpc: float) -> np.ndarray:
    diff = pos[:, None, :] - pos[None, :, :]
    diff = diff - box_mpc * np.round(diff / box_mpc)
    return np.sqrt((diff**2).sum(axis=-1))


def open_sep_matrix(pos: np.ndarray) -> np.ndarray:
    diff = pos[:, None, :] - pos[None, :, :]
    return np.sqrt((diff**2).sum(axis=-1))


def nn_from_sep(sep: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    sep = sep.copy()
    np.fill_diagonal(sep, np.inf)
    nn_idx = np.argmin(sep, axis=1)
    nn_sep = sep[np.arange(len(sep)), nn_idx]
    return nn_idx, nn_sep


def main() -> None:
    root = hdfstream.open("cosma", "/")
    halo_file = root["FLAMINGO"]["L1_m9"]["L1_m9"]["SOAP-HBT"]["halo_properties_0077.hdf5"]

    print("Downloading full SO/200_crit/TotalMass array (real, ~61MB)...")
    mass_ds = halo_file["SO"]["200_crit"]["TotalMass"]
    mass = np.asarray(mass_ds[:]) * 1e10
    order = np.argsort(-mass)
    top_idx = np.sort(order[:GLOBAL_N_TOP])

    print(f"Targeted download: positions for top {GLOBAL_N_TOP} most massive halos...")
    pos_ds = halo_file["InputHalos"]["FOF"]["Centres"]
    pos = np.asarray(pos_ds[top_idx, :])
    top_mass = mass[top_idx]

    reorder = np.argsort(-top_mass)
    pos, top_mass = pos[reorder], top_mass[reorder]

    edge = N_GRID * TNG300_MPC
    in_grid = np.all((pos >= 0) & (pos < edge), axis=1)
    grid_pos, grid_mass = pos[in_grid], top_mass[in_grid]

    cube_idx = np.floor(grid_pos / TNG300_MPC).astype(int)
    cube_idx = np.clip(cube_idx, 0, N_GRID - 1)
    flat_id = cube_idx[:, 0] * N_GRID * N_GRID + cube_idx[:, 1] * N_GRID + cube_idx[:, 2]

    print(
        f"\n{'cube':>5} {'N':>4} {'swap%':>7} "
        f"{'rho_periodic':>13} {'rho_open':>10} {'delta':>8} "
        f"{'medNN_p':>8} {'medNN_o':>8}"
    )

    rho_p_list, rho_o_list, swap_frac_list = [], [], []
    for c, local_n in sorted(MATCHED_CUBES.items()):
        mask = flat_id == c
        cube_mass = grid_mass[mask]
        cube_pos = grid_pos[mask]
        local_order = np.argsort(-cube_mass)
        sorted_mass = cube_mass[local_order][:local_n]
        sorted_pos = cube_pos[local_order][:local_n]
        log_m = np.log10(sorted_mass)

        sep_p = periodic_sep_matrix(sorted_pos, TNG300_MPC)
        nn_idx_p, nn_sep_p = nn_from_sep(sep_p)
        rho_p = pearson(log_m, log_m[nn_idx_p])

        sep_o = open_sep_matrix(sorted_pos)
        nn_idx_o, nn_sep_o = nn_from_sep(sep_o)
        rho_o = pearson(log_m, log_m[nn_idx_o])

        # sanity check: periodic NN separation must never exceed open NN separation
        assert np.all(nn_sep_p <= nn_sep_o + 1e-9), f"cube {c}: periodic > open, implementation bug"

        swap_frac = float((nn_idx_p != nn_idx_o).mean())
        rho_p_list.append(rho_p)
        rho_o_list.append(rho_o)
        swap_frac_list.append(swap_frac)

        print(
            f"{c:>5} {local_n:>4} {swap_frac:>6.1%} "
            f"{rho_p:>13.4f} {rho_o:>10.4f} {rho_o - rho_p:>8.4f} "
            f"{np.median(nn_sep_p):>8.2f} {np.median(nn_sep_o):>8.2f}"
        )

    rho_p_arr = np.array(rho_p_list)
    rho_o_arr = np.array(rho_o_list)
    swap_arr = np.array(swap_frac_list)
    delta = rho_o_arr - rho_p_arr

    print(f"\nAcross {len(MATCHED_CUBES)} matched sub-cubes:")
    print(f"  mean swap fraction (nn_idx differs periodic vs open): {swap_arr.mean():.1%}")
    print(f"  rho_NN periodic: mean={rho_p_arr.mean():.4f}, SD={rho_p_arr.std(ddof=1):.4f}")
    print(f"  rho_NN open:     mean={rho_o_arr.mean():.4f}, SD={rho_o_arr.std(ddof=1):.4f}")
    print(
        f"  delta (open-periodic): mean={delta.mean():.4f}, SD={delta.std(ddof=1):.4f}, "
        f"min={delta.min():.4f}, max={delta.max():.4f}"
    )
    n_anom_p = int((np.abs(rho_p_arr) >= 0.42).sum())
    n_anom_o = int((np.abs(rho_o_arr) >= 0.42).sum())
    print(
        f"\n|rho_NN| >= 0.42: periodic {n_anom_p}/{len(MATCHED_CUBES)}, "
        f"open {n_anom_o}/{len(MATCHED_CUBES)}"
    )


if __name__ == "__main__":
    main()
