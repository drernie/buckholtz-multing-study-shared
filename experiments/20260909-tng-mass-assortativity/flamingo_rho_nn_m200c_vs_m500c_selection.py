"""flamingo_rho_nn_m200c_vs_m500c_selection.py -- executes
CLAIM_flamingo_rho_nn_m200c_vs_m500c_selection.md: direct before/after
recompute of rho_NN on M200c-top-N vs M500c-top-N FLAMINGO selections
(N=50 primary, N=35/1200 for context) -- replacing the set-overlap
proxy (FINDING_flamingo_m500c_m200c_overlap.md) with the real
downstream statistic.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * L0 descriptive
NO_AUTHOR_ERROR
"""

import math

import hdfstream
import numpy as np

FLAMINGO_BOX_MPC = 1000.0
GLOBAL_N_TOP = 5000
CANDIDATE_NS = [35, 50, 1200]  # 50 is the primary, user-requested case


def pearson(x: np.ndarray, y: np.ndarray) -> float:
    return float(np.corrcoef(x, y)[0, 1])


def periodic_sep_matrix(pos: np.ndarray, box_mpc: float) -> np.ndarray:
    diff = pos[:, None, :] - pos[None, :, :]
    diff = diff - box_mpc * np.round(diff / box_mpc)
    return np.sqrt((diff**2).sum(axis=-1))


def rho_nn_for_selection(
    mass_for_selection: np.ndarray, pos: np.ndarray, n: int
) -> tuple[float, float]:
    """Select top-n by mass_for_selection, compute rho_NN within that set
    using its OWN mass values (native to the selection criterion)."""
    order = np.argsort(-mass_for_selection)
    idx = order[:n]
    sel_mass = mass_for_selection[idx]
    sel_pos = pos[idx]
    log_m = np.log10(sel_mass)

    sep = periodic_sep_matrix(sel_pos, FLAMINGO_BOX_MPC)
    np.fill_diagonal(sep, np.inf)
    nn_idx = np.argmin(sep, axis=1)
    r = pearson(log_m, log_m[nn_idx])
    analytic_sd = 1 / math.sqrt(n - 2) if n > 2 else float("nan")
    return r, analytic_sd


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
        f"\n{'N':>6} {'rho_NN(M200c-sel)':>18} {'analytic_SD':>12} "
        f"{'rho_NN(M500c-sel)':>18} {'analytic_SD':>12} {'delta':>8}"
    )
    for n in CANDIDATE_NS:
        r200, sd200 = rho_nn_for_selection(m200, pos, n)
        r500, sd500 = rho_nn_for_selection(m500, pos, n)
        delta = r500 - r200
        marker = "  <-- primary (user-requested)" if n == 50 else ""
        print(
            f"{n:>6} {r200:>18.4f} {sd200:>12.4f} {r500:>18.4f} {sd500:>12.4f} "
            f"{delta:>8.4f}{marker}"
        )


if __name__ == "__main__":
    main()
