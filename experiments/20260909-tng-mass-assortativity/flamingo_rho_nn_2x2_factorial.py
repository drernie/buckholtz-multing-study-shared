"""flamingo_rho_nn_2x2_factorial.py -- executes
CLAIM_flamingo_rho_nn_2x2_factorial.md: fills the two missing
off-diagonal cells of the selection x correlated-value factorial,
separating "which halos are selected" from "which mass values are
correlated" as the driver of the rho_NN shift found in
FINDING_flamingo_rho_nn_m200c_vs_m500c_selection.md.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * L0 descriptive
NO_AUTHOR_ERROR
"""

import hdfstream
import numpy as np

FLAMINGO_BOX_MPC = 1000.0
GLOBAL_N_TOP = 5000
CANDIDATE_NS = [35, 50, 1200]


def pearson(x: np.ndarray, y: np.ndarray) -> float:
    return float(np.corrcoef(x, y)[0, 1])


def periodic_sep_matrix(pos: np.ndarray, box_mpc: float) -> np.ndarray:
    diff = pos[:, None, :] - pos[None, :, :]
    diff = diff - box_mpc * np.round(diff / box_mpc)
    return np.sqrt((diff**2).sum(axis=-1))


def factorial_cell(m200: np.ndarray, m500: np.ndarray, pos: np.ndarray, n: int) -> dict:
    """Returns all 4 cells for a given N: select by M200c or M500c,
    correlate via M200c or M500c values -- NN pairing depends only on
    position within the selected set, never on which mass correlates."""
    order_200 = np.argsort(-m200)
    order_500 = np.argsort(-m500)
    idx_200 = order_200[:n]
    idx_500 = order_500[:n]

    def nn_idx_for(idx: np.ndarray) -> np.ndarray:
        sep = periodic_sep_matrix(pos[idx], FLAMINGO_BOX_MPC)
        np.fill_diagonal(sep, np.inf)
        return np.argmin(sep, axis=1)

    nn_200 = nn_idx_for(idx_200)  # NN pairing within the M200c-selected set
    nn_500 = nn_idx_for(idx_500)  # NN pairing within the M500c-selected set

    log_m200_A = np.log10(m200[idx_200])
    log_m500_A = np.log10(m500[idx_200])  # SAME set as A, alternate mass values
    log_m200_D = np.log10(m200[idx_500])  # SAME set as D, alternate mass values
    log_m500_D = np.log10(m500[idx_500])

    cell_a = pearson(log_m200_A, log_m200_A[nn_200])  # select M200c, correlate M200c
    cell_b = pearson(log_m500_A, log_m500_A[nn_200])  # select M200c, correlate M500c
    cell_c = pearson(log_m200_D, log_m200_D[nn_500])  # select M500c, correlate M200c
    cell_d = pearson(log_m500_D, log_m500_D[nn_500])  # select M500c, correlate M500c

    return {"A": cell_a, "B": cell_b, "C": cell_c, "D": cell_d}


def main() -> None:
    root = hdfstream.open("cosma", "/")
    halo_file = root["FLAMINGO"]["L1_m9"]["L1_m9"]["SOAP-HBT"]["halo_properties_0077.hdf5"]

    print("Downloading full SO/200_crit/TotalMass array (real, ~61MB)...")
    m200_ds = halo_file["SO"]["200_crit"]["TotalMass"]
    m200_all = np.asarray(m200_ds[:]) * 1e10
    order_200 = np.argsort(-m200_all)
    top_idx = np.sort(order_200[:GLOBAL_N_TOP])

    print(
        f"Targeted download: positions, M200c, M500c for the SAME top "
        f"{GLOBAL_N_TOP} (by M200c) halos..."
    )
    pos_ds = halo_file["InputHalos"]["FOF"]["Centres"]
    pos = np.asarray(pos_ds[top_idx, :])
    m200 = m200_all[top_idx]
    m500_ds = halo_file["SO"]["500_crit"]["TotalMass"]
    m500 = np.asarray(m500_ds[top_idx]) * 1e10

    valid = (m200 > 0) & (m500 > 0)
    n_invalid = int((~valid).sum())
    if n_invalid:
        print(f"Excluding {n_invalid} halos with non-positive M200c or M500c.")
    pos, m200, m500 = pos[valid], m200[valid], m500[valid]
    print(f"Shared valid pool: N={len(m200)}")

    print(
        f"\n{'N':>6} {'A(sel200,cor200)':>17} {'B(sel200,cor500)':>17} "
        f"{'C(sel500,cor200)':>17} {'D(sel500,cor500)':>17}"
    )
    results = {}
    for n in CANDIDATE_NS:
        c = factorial_cell(m200, m500, pos, n)
        results[n] = c
        print(f"{n:>6} {c['A']:>17.4f} {c['B']:>17.4f} {c['C']:>17.4f} {c['D']:>17.4f}")

    print("\nDecomposition (selection effect vs value effect):")
    print(
        f"{'N':>6} {'sel_eff@200corr(C-A)':>21} {'sel_eff@500corr(D-B)':>21} "
        f"{'val_eff@200sel(B-A)':>20} {'val_eff@500sel(D-C)':>20} {'total(D-A)':>11}"
    )
    for n in CANDIDATE_NS:
        c = results[n]
        sel_eff_200corr = c["C"] - c["A"]
        sel_eff_500corr = c["D"] - c["B"]
        val_eff_200sel = c["B"] - c["A"]
        val_eff_500sel = c["D"] - c["C"]
        total = c["D"] - c["A"]
        print(
            f"{n:>6} {sel_eff_200corr:>21.4f} {sel_eff_500corr:>21.4f} "
            f"{val_eff_200sel:>20.4f} {val_eff_500sel:>20.4f} {total:>11.4f}"
        )


if __name__ == "__main__":
    main()
