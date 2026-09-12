"""flamingo_subvolume_same_mcut_global_nn.py -- executes
CLAIM_flamingo_subvolume_same_mcut_global_nn.md (user-designed fix):
for each of the 10 already-frozen (cube_id, local_N) sub-cube samples,
recovers that cube's own implicit mass cutoff M_cut(k), then searches
each halo's nearest neighbor among {mass >= M_cut(k)} across
FLAMINGO's REAL, full 1000 Mpc periodic box (not an artificial
sub-cube wrap) -- holding the population fixed while fixing the
geography. A geometric gate (does the resulting NN scale still land
near 40-45 Mpc) is evaluated and printed BEFORE any rho_NN is
computed, per the frozen claim's own explicit ordering.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * L0 descriptive
NO_AUTHOR_ERROR
"""

import hdfstream
import numpy as np

FLAMINGO_BOX_MPC = 1000.0
TNG300_MPC = 302.6267
N_GRID = 3
GLOBAL_N_TOP = 5000
BAND_LO, BAND_HI = 40.0, 45.0

# frozen, from flamingo_subvolume_replication.py's own already-committed
# real output -- NOT re-derived here
MATCHED_CUBES = {1: 40, 2: 55, 4: 35, 5: 30, 7: 30, 8: 30, 12: 40, 17: 45, 25: 45, 26: 50}


def pearson(x: np.ndarray, y: np.ndarray) -> float:
    return float(np.corrcoef(x, y)[0, 1])


def periodic_sep(a: np.ndarray, b: np.ndarray, box_mpc: float) -> np.ndarray:
    """Pairwise periodic separation between rows of a (n_a,3) and b (n_b,3)."""
    diff = a[:, None, :] - b[None, :, :]
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

    edge = N_GRID * TNG300_MPC
    in_grid = np.all((pos >= 0) & (pos < edge), axis=1)
    grid_pos, grid_mass = pos[in_grid], top_mass[in_grid]

    cube_idx = np.floor(grid_pos / TNG300_MPC).astype(int)
    cube_idx = np.clip(cube_idx, 0, N_GRID - 1)
    flat_id = cube_idx[:, 0] * N_GRID * N_GRID + cube_idx[:, 1] * N_GRID + cube_idx[:, 2]

    # ---- PHASE 1: geometric gate only -- no rho computed yet ----
    print("\n=== PHASE 1: geometric gate (NN scale under same-M_cut, full-box search) ===")
    print(
        f"{'cube':>5} {'N':>4} {'M_cut':>11} {'pop_size':>9} "
        f"{'med_NN(local)':>14} {'med_NN(global)':>15} {'mean_NN(global)':>16}"
    )

    per_cube_local_idx = {}
    per_cube_med_global = {}
    all_global_seps = []

    for c, local_n in sorted(MATCHED_CUBES.items()):
        mask = flat_id == c
        cube_mass = grid_mass[mask]
        cube_pos = grid_pos[mask]
        local_order = np.argsort(-cube_mass)
        sel_mass = cube_mass[local_order][:local_n]
        sel_pos = cube_pos[local_order][:local_n]
        m_cut = sel_mass.min()

        # local (sub-cube-restricted) NN scale, for reference -- already reported before
        sep_local = periodic_sep(sel_pos, sel_pos, TNG300_MPC)
        np.fill_diagonal(sep_local, np.inf)
        med_local = float(np.median(sep_local.min(axis=1)))

        # population meeting the SAME mass cut, drawn from the FULL top-5000
        pop_mask = top_mass >= m_cut
        pop_pos = pos[pop_mask]
        pop_size = int(pop_mask.sum())

        # for each of this cube's own local_n halos, find its NN within pop_pos,
        # using FLAMINGO's real full-box periodicity -- excluding self-matches
        # by identifying rows of pop_pos that coincide with sel_pos
        sep_global = periodic_sep(sel_pos, pop_pos, FLAMINGO_BOX_MPC)
        # mask out self-pairs (a selected halo matched to itself in pop_pos)
        self_mask = sep_global < 1e-6
        sep_global = np.where(self_mask, np.inf, sep_global)
        nn_sep_global = sep_global.min(axis=1)
        nn_idx_global = sep_global.argmin(axis=1)

        med_global = float(np.median(nn_sep_global))
        mean_global = float(nn_sep_global.mean())

        per_cube_local_idx[c] = (sel_mass, sel_pos, pop_pos, pop_mask, nn_idx_global)
        per_cube_med_global[c] = med_global
        all_global_seps.extend(nn_sep_global.tolist())

        print(
            f"{c:>5} {local_n:>4} {m_cut:>11.3e} {pop_size:>9} "
            f"{med_local:>14.2f} {med_global:>15.2f} {mean_global:>16.2f}"
        )

    all_global_seps = np.array(all_global_seps)
    overall_median = float(np.median(all_global_seps))
    overall_mean = float(all_global_seps.mean())
    frac_in_band = float(((all_global_seps >= BAND_LO) & (all_global_seps <= BAND_HI)).mean())

    print(
        f"\nAggregate (n={len(all_global_seps)} halo-instances across all {len(MATCHED_CUBES)} cubes):"
    )
    print(
        f"  same-M_cut, full-box NN separation: median={overall_median:.2f} Mpc, "
        f"mean={overall_mean:.2f} Mpc"
    )
    print(f"  fraction in original [{BAND_LO},{BAND_HI}] Mpc target window: {frac_in_band:.1%}")

    # ---- GATE DECISION, before any rho is computed ----
    # threshold [35,55] frozen in CLAIM_flamingo_subvolume_same_mcut_global_nn.md
    # BEFORE this script ran -- not chosen after seeing the result
    gate_pass = 35.0 <= overall_median <= 55.0
    print("\n=== GATE DECISION ===")
    print(f"Original local (sub-cube) target: {BAND_LO}-{BAND_HI} Mpc")
    print(f"Same-M_cut, full-box median: {overall_median:.2f} Mpc")
    if gate_pass:
        print(
            "GATE: PASS (materially closer to the 40-45 Mpc target than the "
            "top-5000 attempt's ~22 Mpc) -- proceeding to compute rho_NN."
        )
    else:
        print(
            "GATE: FAIL -- scale still drifts well below the original target even "
            "at the SAME mass cut. Per the frozen claim, NOT computing/reporting "
            "rho_NN as a resolving number. This indicates the sub-cube scale-match "
            "itself may be a boundary artifact of the candidate-neighbor set, not a "
            "real property of this mass-defined population."
        )
        return

    # ---- PHASE 2: rho_NN under the same-M_cut, full-box treatment (only if gate passed) ----
    print("\n=== PHASE 2: rho_NN, same-M_cut full-box treatment ===")
    rho_list = []
    for c in sorted(MATCHED_CUBES):
        sel_mass, sel_pos, pop_pos, pop_mask, nn_idx_global = per_cube_local_idx[c]
        log_m = np.log10(sel_mass)
        pop_mass = top_mass[pop_mask]
        partner_log_m = np.log10(pop_mass[nn_idx_global])
        rho = pearson(log_m, partner_log_m)
        rho_list.append(rho)
        print(f"cube {c:>3}: rho_NN(same-M_cut, full-box) = {rho:.4f}")

    rho_arr = np.array(rho_list)
    print(
        f"\nAcross {len(MATCHED_CUBES)} cubes: mean={rho_arr.mean():.4f}, "
        f"SD={rho_arr.std(ddof=1):.4f}"
    )
    n_anom = int((np.abs(rho_arr) >= 0.42).sum())
    print(f"|rho_NN| >= 0.42: {n_anom}/{len(MATCHED_CUBES)}")


if __name__ == "__main__":
    main()
