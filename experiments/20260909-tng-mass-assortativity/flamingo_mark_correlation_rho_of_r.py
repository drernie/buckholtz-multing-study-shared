"""flamingo_mark_correlation_rho_of_r.py -- executes
CLAIM_flamingo_mark_correlation_rho_of_r.md: a mass-marked
generalization of rho -- Pearson correlation of paired log10(M500c)
values among ALL pairs in each separation bin, across the full 5-150
Mpc range, replacing the closed rho_NN/rho_band single-scale designs.
Significance via a mark-shuffle permutation null (conditions on the
real point pattern, randomizes only the marks). Includes a positive
control (cell-block synthetic marks with a known signature) to close
the "no canary" gap the prior 2PCF pipeline's skeptic review flagged.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * L0 descriptive
NO_AUTHOR_ERROR
"""

import hdfstream
import numpy as np

FLAMINGO_BOX_MPC = 1000.0
CANDIDATE_NS = [200, 1000, 5000]
R_MIN_MPC = 5.0
R_MAX_MPC = 150.0
N_BINS = 15
N_SHUFFLE = 200
MIN_PAIRS_FOR_RHO = 10
RNG_SEED = 20260913
POSITIVE_CONTROL_CELL_MPC = 50.0
POSITIVE_CONTROL_NOISE_SD = 0.1


def pair_indices_and_seps(
    pos: np.ndarray, box_mpc: float
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    n = pos.shape[0]
    iu, ju = np.triu_indices(n, k=1)
    diff = pos[iu] - pos[ju]
    diff = diff - box_mpc * np.round(diff / box_mpc)
    sep = np.sqrt((diff**2).sum(axis=-1))
    return iu, ju, sep


def pearson(x: np.ndarray, y: np.ndarray) -> float:
    if len(x) < 3:
        return float("nan")
    return float(np.corrcoef(x, y)[0, 1])


def rho_of_r_with_shuffle_null(
    marks: np.ndarray,
    iu: np.ndarray,
    ju: np.ndarray,
    bin_idx: np.ndarray,
    n_bins: int,
    n_shuffle: int,
    rng: np.random.Generator,
) -> dict:
    dd = np.zeros(n_bins, dtype=int)
    observed = np.full(n_bins, np.nan)
    null_mean = np.full(n_bins, np.nan)
    null_std = np.full(n_bins, np.nan)
    z_score = np.full(n_bins, np.nan)
    p_emp = np.full(n_bins, np.nan)

    bin_masks = [bin_idx == b for b in range(n_bins)]
    for b, mask in enumerate(bin_masks):
        dd[b] = int(mask.sum())
        if dd[b] >= MIN_PAIRS_FOR_RHO:
            observed[b] = pearson(marks[iu[mask]], marks[ju[mask]])

    null_vals = np.full((n_shuffle, n_bins), np.nan)
    for s in range(n_shuffle):
        shuffled = rng.permutation(marks)
        for b, mask in enumerate(bin_masks):
            if dd[b] >= MIN_PAIRS_FOR_RHO:
                null_vals[s, b] = pearson(shuffled[iu[mask]], shuffled[ju[mask]])

    for b in range(n_bins):
        if dd[b] >= MIN_PAIRS_FOR_RHO:
            col = null_vals[:, b]
            null_mean[b] = np.nanmean(col)
            null_std[b] = np.nanstd(col)
            if null_std[b] > 0:
                z_score[b] = (observed[b] - null_mean[b]) / null_std[b]
            p_emp[b] = float(np.mean(np.abs(col) >= abs(observed[b])))

    return {
        "dd": dd,
        "observed": observed,
        "null_mean": null_mean,
        "null_std": null_std,
        "z_score": z_score,
        "p_emp": p_emp,
    }


def make_cell_block_marks(
    pos: np.ndarray, box_mpc: float, cell_mpc: float, noise_sd: float, rng: np.random.Generator
) -> np.ndarray:
    cell_id = np.floor(pos / cell_mpc).astype(int)
    n_side = int(np.ceil(box_mpc / cell_mpc))
    cell_flat = cell_id[:, 0] * n_side**2 + cell_id[:, 1] * n_side + cell_id[:, 2]
    unique_cells, inverse = np.unique(cell_flat, return_inverse=True)
    cell_levels = rng.normal(0.0, 1.0, size=len(unique_cells))
    return cell_levels[inverse] + rng.normal(0.0, noise_sd, size=pos.shape[0])


def print_table(label: str, bin_centers: np.ndarray, result: dict) -> None:
    print(f"\n{label}")
    print(
        f"{'r_mpc':>8} {'dd':>8} {'rho(r)':>9} {'null_mean':>10} {'null_std':>9} "
        f"{'z':>7} {'p_emp':>7}"
    )
    for i in range(len(bin_centers)):
        print(
            f"{bin_centers[i]:>8.1f} {result['dd'][i]:>8d} {result['observed'][i]:>9.4f} "
            f"{result['null_mean'][i]:>10.4f} {result['null_std'][i]:>9.4f} "
            f"{result['z_score'][i]:>7.2f} {result['p_emp'][i]:>7.3f}"
        )


def main() -> None:
    root = hdfstream.open("cosma", "/")
    halo_file = root["FLAMINGO"]["L1_m9"]["L1_m9"]["SOAP-HBT"]["halo_properties_0077.hdf5"]

    print("Downloading full SO/500_crit/TotalMass array for direct M500c ranking...")
    m500_ds = halo_file["SO"]["500_crit"]["TotalMass"]
    m500_all = np.asarray(m500_ds[:]) * 1e10
    order_500 = np.argsort(-m500_all)
    pos_ds = halo_file["InputHalos"]["FOF"]["Centres"]

    bin_edges = np.geomspace(R_MIN_MPC, R_MAX_MPC, N_BINS + 1)
    bin_centers = np.sqrt(bin_edges[:-1] * bin_edges[1:])
    rng = np.random.default_rng(RNG_SEED)

    idx_1000 = np.sort(order_500[:1000])
    pos_1000 = np.asarray(pos_ds[idx_1000, :])
    iu_pc, ju_pc, sep_pc = pair_indices_and_seps(pos_1000, FLAMINGO_BOX_MPC)
    bin_idx_pc = np.digitize(sep_pc, bin_edges) - 1
    marks_synthetic = make_cell_block_marks(
        pos_1000, FLAMINGO_BOX_MPC, POSITIVE_CONTROL_CELL_MPC, POSITIVE_CONTROL_NOISE_SD, rng
    )
    result_pc = rho_of_r_with_shuffle_null(
        marks_synthetic, iu_pc, ju_pc, bin_idx_pc, N_BINS, N_SHUFFLE, rng
    )
    print_table(
        f"=== Positive control: cell-block synthetic marks on REAL N=1000 positions "
        f"(cell={POSITIVE_CONTROL_CELL_MPC} Mpc) ===",
        bin_centers,
        result_pc,
    )

    for n in CANDIDATE_NS:
        idx = np.sort(order_500[:n])
        pos = np.asarray(pos_ds[idx, :])
        m500_sel = m500_all[idx]
        log_mass = np.log10(m500_sel)

        iu, ju, sep = pair_indices_and_seps(pos, FLAMINGO_BOX_MPC)
        bin_idx = np.digitize(sep, bin_edges) - 1

        result = rho_of_r_with_shuffle_null(log_mass, iu, ju, bin_idx, N_BINS, N_SHUFFLE, rng)
        print_table(f"=== M500c-selected FLAMINGO clusters, N={n}: rho(r) ===", bin_centers, result)


if __name__ == "__main__":
    main()
