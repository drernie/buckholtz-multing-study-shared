"""flamingo_2pcf_m500c_estimand.py -- executes
CLAIM_flamingo_2pcf_m500c_estimand.md: a source-faithful 2PCF-style
estimand (xi(r) = DD(r)/RR(r) - 1, analytic RR for a periodic box) on
FLAMINGO's M500c-selected cluster population, fit to xi(r)=(r0/r)^gamma
and compared to v82's own cited Basilakos & Plionis (2004) values.

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
RNG_SEED = 20260912

BASILAKOS_PLIONIS_2004 = {
    "richer": {"r0_hinv_mpc": 20.7, "gamma": 1.6},
    "poorer": {"r0_hinv_mpc": 9.7, "gamma": 2.0},
}


def periodic_sep_upper(pos: np.ndarray, box_mpc: float) -> np.ndarray:
    n = pos.shape[0]
    iu, ju = np.triu_indices(n, k=1)
    diff = pos[iu] - pos[ju]
    diff = diff - box_mpc * np.round(diff / box_mpc)
    return np.sqrt((diff**2).sum(axis=-1))


def compute_xi(pos: np.ndarray, box_mpc: float, bin_edges: np.ndarray) -> dict:
    n = pos.shape[0]
    sep = periodic_sep_upper(pos, box_mpc)
    dd, _ = np.histogram(sep, bins=bin_edges)
    volume = box_mpc**3
    n_pairs_total = n * (n - 1) / 2.0
    shell_volume = (4.0 / 3.0) * np.pi * (bin_edges[1:] ** 3 - bin_edges[:-1] ** 3)
    rr = n_pairs_total * shell_volume / volume
    xi = dd / rr - 1.0
    xi_sigma = np.where(dd > 0, 1.0 / np.sqrt(dd), np.nan)
    return {"dd": dd, "rr": rr, "xi": xi, "xi_sigma": xi_sigma}


def fit_power_law(bin_centers: np.ndarray, xi: np.ndarray) -> dict:
    mask = xi > 0
    if mask.sum() < 3:
        return {"r0_mpc": float("nan"), "gamma": float("nan"), "n_bins_used": int(mask.sum())}
    log_r = np.log(bin_centers[mask])
    log_xi = np.log(xi[mask])
    slope, intercept = np.polyfit(log_r, log_xi, 1)
    gamma = -slope
    r0_mpc = np.exp(intercept / gamma) if gamma != 0 else float("nan")
    return {"r0_mpc": float(r0_mpc), "gamma": float(gamma), "n_bins_used": int(mask.sum())}


def main() -> None:
    root = hdfstream.open("cosma", "/")
    halo_file = root["FLAMINGO"]["L1_m9"]["L1_m9"]["SOAP-HBT"]["halo_properties_0077.hdf5"]

    h_flamingo = float(np.asarray(halo_file["Cosmology"].attrs["h"])[0])
    print(f"FLAMINGO cosmology h = {h_flamingo} [VERIFIED from file Cosmology attrs]")

    print("Downloading full SO/500_crit/TotalMass array for direct M500c ranking...")
    m500_ds = halo_file["SO"]["500_crit"]["TotalMass"]
    m500_all = np.asarray(m500_ds[:]) * 1e10
    order_500 = np.argsort(-m500_all)

    pos_ds = halo_file["InputHalos"]["FOF"]["Centres"]

    bin_edges = np.geomspace(R_MIN_MPC, R_MAX_MPC, N_BINS + 1)
    bin_centers = np.sqrt(bin_edges[:-1] * bin_edges[1:])

    print("\n=== Negative control: N uniform-random positions in the periodic box ===")
    rng = np.random.default_rng(RNG_SEED)
    for n in [1000]:
        rand_pos = rng.uniform(0.0, FLAMINGO_BOX_MPC, size=(n, 3))
        result = compute_xi(rand_pos, FLAMINGO_BOX_MPC, bin_edges)
        xi = result["xi"]
        sigma = result["xi_sigma"]
        n_within_2sigma = int(np.sum(np.abs(xi) <= 2 * np.where(np.isnan(sigma), np.inf, sigma)))
        n_valid = int(np.sum(~np.isnan(sigma)))
        print(f"N={n}: {n_within_2sigma}/{n_valid} bins have |xi| <= 2*sigma_Poisson")
        print(f"  xi range: [{np.nanmin(xi):.4f}, {np.nanmax(xi):.4f}], mean={np.nanmean(xi):.4f}")

    print("\n=== M500c-selected FLAMINGO clusters: xi(r) and power-law fit ===")
    print(
        f"{'N':>6} {'r0_mpc':>10} {'gamma':>8} {'n_bins_fit':>10} "
        f"{'r0_hinv_mpc':>12} {'M500c_min_1e14Msun':>20}"
    )
    fits = {}
    for n in CANDIDATE_NS:
        idx = np.sort(order_500[:n])
        pos = np.asarray(pos_ds[idx, :])
        m500_sel = m500_all[idx]
        result = compute_xi(pos, FLAMINGO_BOX_MPC, bin_edges)
        fit = fit_power_law(bin_centers, result["xi"])
        r0_hinv = fit["r0_mpc"] * h_flamingo
        m500_min = m500_sel.min() / 1e14
        fits[n] = {**fit, "r0_hinv_mpc": r0_hinv, "xi": result["xi"], "dd": result["dd"]}
        print(
            f"{n:>6} {fit['r0_mpc']:>10.2f} {fit['gamma']:>8.3f} {fit['n_bins_used']:>10} "
            f"{r0_hinv:>12.2f} {m500_min:>20.3f}"
        )

    print("\n=== Comparison to Basilakos & Plionis (2004), ref [91] ===")
    for label, vals in BASILAKOS_PLIONIS_2004.items():
        r0_phys = vals["r0_hinv_mpc"] / h_flamingo
        print(
            f"{label}: r0={vals['r0_hinv_mpc']} h^-1 Mpc = {r0_phys:.2f} Mpc physical "
            f"(FLAMINGO h={h_flamingo}), gamma={vals['gamma']}"
        )

    print("\nPer-N xi(r) raw values (bin_center_mpc: xi):")
    for n in CANDIDATE_NS:
        xi = fits[n]["xi"]
        dd = fits[n]["dd"]
        pairs_str = ", ".join(
            f"{bin_centers[i]:.1f}:{xi[i]:.4f}(dd={dd[i]})" for i in range(len(bin_centers))
        )
        print(f"N={n}: {pairs_str}")


if __name__ == "__main__":
    main()
