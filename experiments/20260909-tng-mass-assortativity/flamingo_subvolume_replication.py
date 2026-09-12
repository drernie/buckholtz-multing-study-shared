"""flamingo_subvolume_replication.py -- executes
CLAIM_flamingo_subvolume_replication.md: carves FLAMINGO's real 1000
Mpc box into 27 non-overlapping, TNG300-sized (302.6267 Mpc) sub-
cubes, independently scale-matches each to v82's own 40-45 Mpc target
(local NN-geometry only, no correlation seen before N is chosen), and
computes rho_NN in every sub-cube that yields a match -- building a
real, empirical distribution to test whether TNG300's own N=35
rho_NN=-0.42 anomaly is common or rare under this exact protocol.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * L0 descriptive
NO_AUTHOR_ERROR
"""

import math

import hdfstream
import numpy as np

TNG300_MPC = 302.6267
N_GRID = 3
GLOBAL_N_TOP = 5000
CANDIDATE_NS = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]
BAND_LO, BAND_HI = 40.0, 45.0
ANOMALY_THRESHOLD = 0.42  # |rho_NN| this large or larger = "matches TNG300's own anomaly"


def pearson(x: np.ndarray, y: np.ndarray) -> float:
    return float(np.corrcoef(x, y)[0, 1])


def periodic_sep_matrix(pos: np.ndarray, box_mpc: float) -> np.ndarray:
    diff = pos[:, None, :] - pos[None, :, :]
    diff = diff - box_mpc * np.round(diff / box_mpc)
    return np.sqrt((diff**2).sum(axis=-1))


def nn_stats(pos: np.ndarray, box_mpc: float) -> tuple[float, float, np.ndarray]:
    sep = periodic_sep_matrix(pos, box_mpc)
    np.fill_diagonal(sep, np.inf)
    nn_idx = np.argmin(sep, axis=1)
    nn_sep = sep[np.arange(len(pos)), nn_idx]
    return float(np.median(nn_sep)), float(nn_sep.mean()), nn_idx


def pick_local_n(sorted_log_m: np.ndarray, sorted_pos: np.ndarray) -> tuple[int, np.ndarray] | None:
    """Scan CANDIDATE_NS on NN-geometry only; return the best match (or None)."""
    n_avail = len(sorted_log_m)
    candidates = []
    for n in CANDIDATE_NS:
        if n > n_avail:
            continue
        med, mean, nn_idx = nn_stats(sorted_pos[:n], TNG300_MPC)
        if BAND_LO <= med <= BAND_HI and BAND_LO <= mean <= BAND_HI:
            score = abs(med - 42.5) + abs(mean - 42.5)
            candidates.append((score, n, nn_idx))
    if not candidates:
        return None
    candidates.sort(key=lambda c: c[0])
    _, best_n, best_nn_idx = candidates[0]
    return best_n, best_nn_idx


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

    print(f"\n{27} sub-cubes, side={TNG300_MPC:.4f} Mpc, {in_grid.sum()} halos in grid region")
    print(f"{'cube':>5} {'n_avail':>8} {'local_N':>8} {'med_NN':>8} {'mean_NN':>8} {'rho_NN':>9}")

    results = []
    for c in range(N_GRID**3):
        mask = flat_id == c
        n_avail = int(mask.sum())
        if n_avail < 15:
            print(f"{c:>5} {n_avail:>8} {'--':>8} {'--':>8} {'--':>8} {'--':>9}  (too few halos)")
            continue

        cube_mass = grid_mass[mask]
        cube_pos = grid_pos[mask]
        local_order = np.argsort(-cube_mass)
        sorted_mass = cube_mass[local_order]
        sorted_pos = cube_pos[local_order]
        sorted_log_m = np.log10(sorted_mass)

        picked = pick_local_n(sorted_log_m, sorted_pos)
        if picked is None:
            print(f"{c:>5} {n_avail:>8} {'--':>8} {'--':>8} {'--':>8} {'--':>9}  (no N matched)")
            continue

        local_n, nn_idx = picked
        sub_log_m = sorted_log_m[:local_n]
        med, mean, _ = nn_stats(sorted_pos[:local_n], TNG300_MPC)
        r_nn = pearson(sub_log_m, sub_log_m[nn_idx])
        results.append(r_nn)
        print(f"{c:>5} {n_avail:>8} {local_n:>8} {med:>8.2f} {mean:>8.2f} {r_nn:>9.4f}")

    results = np.array(results)
    n_matched = len(results)
    print(f"\nSub-cubes matched: {n_matched} / 27")
    if n_matched == 0:
        print("No sub-cube yielded a matched local N -- cannot build a distribution.")
        return

    print(
        f"rho_NN distribution: mean={results.mean():.4f}, SD={results.std(ddof=1) if n_matched > 1 else float('nan'):.4f}"
    )
    print(f"  min={results.min():.4f}, max={results.max():.4f}")
    n_anomalous = int((np.abs(results) >= ANOMALY_THRESHOLD).sum())
    print(
        f"\n|rho_NN| >= {ANOMALY_THRESHOLD} (matches/exceeds TNG300's own N=35 anomaly): "
        f"{n_anomalous} / {n_matched} ({n_anomalous / n_matched:.1%})"
    )

    if n_matched >= 2:
        se = results.std(ddof=1) / math.sqrt(n_matched)
        print(f"SE of the mean (n={n_matched}): {se:.4f}")


if __name__ == "__main__":
    main()
