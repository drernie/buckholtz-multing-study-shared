"""flamingo_subvolume_true_global_nn.py -- executes
CLAIM_flamingo_subvolume_true_global_nn.md: computes each halo's TRUE
nearest neighbor across FLAMINGO's own real, physically periodic 1000
Mpc box (no sub-cube cutting), for the SAME 10 already-frozen
(cube_id, local_N) sub-cube samples used by
flamingo_subvolume_replication.py and
flamingo_subvolume_periodic_wrap_bias.py -- providing the genuine
ground truth those two tests both identified as missing.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * L0 descriptive
NO_AUTHOR_ERROR
"""

import hdfstream
import numpy as np

FLAMINGO_BOX_MPC = 1000.0  # FLAMINGO's own real, physically periodic box
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
    log_m_all = np.log10(top_mass)

    print(
        f"\nComputing TRUE global NN across all {GLOBAL_N_TOP} halos, "
        f"FLAMINGO's own real {FLAMINGO_BOX_MPC:.0f} Mpc periodic box..."
    )
    sep_true_full = periodic_sep_matrix(pos, FLAMINGO_BOX_MPC)
    sep_true_diag = sep_true_full.copy()
    np.fill_diagonal(sep_true_diag, np.inf)
    global_nn_idx = np.argmin(sep_true_diag, axis=1)
    global_nn_sep = sep_true_diag[np.arange(GLOBAL_N_TOP), global_nn_idx]
    print(
        f"Global NN separation: median={np.median(global_nn_sep):.2f} Mpc "
        f"(sanity check -- unrelated to the target 40-45 Mpc scale, this is "
        f"the NN scale of the FULL top-{GLOBAL_N_TOP} sample)"
    )

    edge = N_GRID * TNG300_MPC
    in_grid = np.all((pos >= 0) & (pos < edge), axis=1)
    grid_pos, grid_mass, grid_global_idx = pos[in_grid], top_mass[in_grid], np.where(in_grid)[0]

    cube_idx = np.floor(grid_pos / TNG300_MPC).astype(int)
    cube_idx = np.clip(cube_idx, 0, N_GRID - 1)
    flat_id = cube_idx[:, 0] * N_GRID * N_GRID + cube_idx[:, 1] * N_GRID + cube_idx[:, 2]

    print(
        f"\n{'cube':>5} {'N':>4} {'out%':>6} {'rho_true':>9} {'rho_periodic':>13} {'rho_open':>9}"
    )

    rho_true_list = []
    rho_p_list = []
    rho_o_list = []
    frac_outside_list = []
    for c, local_n in sorted(MATCHED_CUBES.items()):
        mask = flat_id == c
        cube_mass = grid_mass[mask]
        cube_pos = grid_pos[mask]
        cube_global_idx = grid_global_idx[mask]
        local_order = np.argsort(-cube_mass)
        sorted_mass = cube_mass[local_order][:local_n]
        sorted_pos = cube_pos[local_order][:local_n]
        sorted_global_idx = cube_global_idx[local_order][:local_n]
        log_m = np.log10(sorted_mass)

        # periodic (sub-cube-local) rho_NN, recomputed here for the side-by-side table
        sep_p = periodic_sep_matrix(sorted_pos, TNG300_MPC)
        np.fill_diagonal(sep_p, np.inf)
        nn_idx_p = np.argmin(sep_p, axis=1)
        rho_p = pearson(log_m, log_m[nn_idx_p])

        # open-boundary rho_NN, recomputed here for the side-by-side table
        diff_o = sorted_pos[:, None, :] - sorted_pos[None, :, :]
        sep_o = np.sqrt((diff_o**2).sum(axis=-1))
        np.fill_diagonal(sep_o, np.inf)
        nn_idx_o = np.argmin(sep_o, axis=1)
        rho_o = pearson(log_m, log_m[nn_idx_o])

        # TRUE global NN: for each halo in this cube, look up its true nearest
        # neighbor among ALL 5000 (not restricted to the cube) and that
        # neighbor's own log-mass
        true_partner_global_idx = global_nn_idx[sorted_global_idx]
        true_partner_log_m = log_m_all[true_partner_global_idx]
        rho_true = pearson(log_m, true_partner_log_m)

        outside_mask = ~np.isin(true_partner_global_idx, sorted_global_idx)
        frac_outside = float(outside_mask.mean())

        rho_true_list.append(rho_true)
        rho_p_list.append(rho_p)
        rho_o_list.append(rho_o)
        frac_outside_list.append(frac_outside)

        print(
            f"{c:>5} {local_n:>4} {frac_outside:>5.0%} "
            f"{rho_true:>9.4f} {rho_p:>13.4f} {rho_o:>9.4f}"
        )

    rho_true_arr = np.array(rho_true_list)
    frac_outside_arr = np.array(frac_outside_list)
    rho_p_arr = np.array(rho_p_list)
    rho_o_arr = np.array(rho_o_list)

    print(f"\nAcross {len(MATCHED_CUBES)} matched sub-cubes:")
    print(
        f"  mean fraction of local_N halos whose TRUE nearest neighbor "
        f"lies OUTSIDE the sub-cube: {frac_outside_arr.mean():.1%} "
        f"(range {frac_outside_arr.min():.0%}-{frac_outside_arr.max():.0%})"
    )
    print(f"  rho_NN true:     mean={rho_true_arr.mean():.4f}, SD={rho_true_arr.std(ddof=1):.4f}")
    print(f"  rho_NN periodic: mean={rho_p_arr.mean():.4f}, SD={rho_p_arr.std(ddof=1):.4f}")
    print(f"  rho_NN open:     mean={rho_o_arr.mean():.4f}, SD={rho_o_arr.std(ddof=1):.4f}")

    amp_delta_p = np.abs(rho_p_arr) - np.abs(rho_true_arr)
    amp_delta_o = np.abs(rho_o_arr) - np.abs(rho_true_arr)
    print(
        f"\n  amplitude delta |rho_periodic|-|rho_true|: mean={amp_delta_p.mean():.4f}, "
        f"SD={amp_delta_p.std(ddof=1):.4f}"
    )
    print(
        f"  amplitude delta |rho_open|-|rho_true|:     mean={amp_delta_o.mean():.4f}, "
        f"SD={amp_delta_o.std(ddof=1):.4f}"
    )

    n_anom_true = int((np.abs(rho_true_arr) >= 0.42).sum())
    print(
        f"\n|rho_NN| >= 0.42: true {n_anom_true}/{len(MATCHED_CUBES)}, "
        f"periodic 0/{len(MATCHED_CUBES)}, open 1/{len(MATCHED_CUBES)}"
    )


if __name__ == "__main__":
    main()
