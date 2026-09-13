"""flamingo_2pcf_gamma_range_diagnostic.py -- executes
CLAIM_flamingo_2pcf_gamma_range_diagnostic.md: re-fits the ALREADY-
RECORDED xi(r) values from FINDING_flamingo_2pcf_m500c_estimand.md's
own raw output over alternative r-ranges, to diagnose whether the
gamma mismatch vs. Basilakos & Plionis (2004) is a fit-range artifact
(real xi(r) curvature) rather than a genuine shape discrepancy.

No new FLAMINGO download -- these are the verbatim xi(r) values
already printed in the prior FINDING's raw output.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * L0 descriptive
NO_AUTHOR_ERROR
"""

import numpy as np

FLAMINGO_H = 0.681

BIN_CENTERS_MPC = np.array(
    [5.6, 7.0, 8.8, 11.1, 13.9, 17.4, 21.8, 27.4, 34.4, 43.1, 54.1, 67.8, 85.1, 106.8, 133.9]
)

# Verbatim xi(r) values from FINDING_flamingo_2pcf_m500c_estimand.md's raw output.
XI_BY_N = {
    200: [
        -1.0000,
        -1.0000,
        -1.0000,
        24.5971,
        -1.0000,
        2.2833,
        3.9889,
        3.2115,
        1.5597,
        0.7286,
        0.3133,
        0.5521,
        0.0108,
        -0.0757,
        0.0588,
    ],
    1000: [
        -1.0000,
        6.9504,
        9.0670,
        5.1187,
        2.0991,
        3.3166,
        1.5176,
        1.5503,
        0.7846,
        0.4032,
        0.2775,
        0.1263,
        0.0336,
        0.0102,
        0.0250,
    ],
    5000: [
        6.6853,
        6.5468,
        6.2022,
        3.8095,
        2.8295,
        1.7813,
        0.9595,
        0.6832,
        0.3532,
        0.2641,
        0.1176,
        0.0805,
        0.0396,
        0.0102,
        0.0201,
    ],
}

FIT_RANGES = [
    (5.0, 150.0, "full, as originally reported"),
    (5.0, 30.0, "small-r only"),
    (10.0, 50.0, "mid-range, literature-typical"),
    (30.0, 150.0, "large-r only"),
]

BASILAKOS_PLIONIS_2004 = {
    "richer": {"r0_hinv_mpc": 20.7, "gamma": 1.6},
    "poorer": {"r0_hinv_mpc": 9.7, "gamma": 2.0},
}


def fit_power_law_in_range(xi: np.ndarray, r_lo: float, r_hi: float) -> dict:
    mask = (BIN_CENTERS_MPC >= r_lo) & (BIN_CENTERS_MPC <= r_hi) & (xi > 0)
    if mask.sum() < 3:
        return {"r0_mpc": float("nan"), "gamma": float("nan"), "n_bins": int(mask.sum())}
    log_r = np.log(BIN_CENTERS_MPC[mask])
    log_xi = np.log(xi[mask])
    slope, intercept = np.polyfit(log_r, log_xi, 1)
    gamma = -slope
    r0_mpc = np.exp(intercept / gamma) if gamma != 0 else float("nan")
    return {"r0_mpc": float(r0_mpc), "gamma": float(gamma), "n_bins": int(mask.sum())}


def local_slopes(xi: np.ndarray) -> list[tuple[float, float, float]]:
    results = []
    for i in range(len(xi) - 1):
        if xi[i] > 0 and xi[i + 1] > 0:
            dlog_xi = np.log(xi[i + 1]) - np.log(xi[i])
            dlog_r = np.log(BIN_CENTERS_MPC[i + 1]) - np.log(BIN_CENTERS_MPC[i])
            gamma_local = -dlog_xi / dlog_r
            results.append((BIN_CENTERS_MPC[i], BIN_CENTERS_MPC[i + 1], gamma_local))
    return results


def main() -> None:
    print("=== Local (bin-to-bin) log-log slope -gamma_local, N=5000 (most robust) ===")
    xi_5000 = np.array(XI_BY_N[5000])
    for r_i, r_j, gamma_local in local_slopes(xi_5000):
        print(f"  r={r_i:6.1f}-{r_j:6.1f}: gamma_local={gamma_local:.3f}")

    print(
        "\n=== Refits over alternative r-ranges (same already-recorded xi(r), no new download) ==="
    )
    for n_key in (200, 1000, 5000):
        xi = np.array(XI_BY_N[n_key])
        print(f"\n-- N={n_key} --")
        for r_lo, r_hi, label in FIT_RANGES:
            fit = fit_power_law_in_range(xi, r_lo, r_hi)
            r0_hinv = fit["r0_mpc"] * FLAMINGO_H
            print(
                f"  [{r_lo:>5.0f}-{r_hi:>5.0f}] {label:32s}: r0={fit['r0_mpc']:6.2f} Mpc, "
                f"gamma={fit['gamma']:.3f}, r0_hinv={r0_hinv:.2f}, n_bins={fit['n_bins']}"
            )

    print("\n=== Literature comparison (Basilakos & Plionis 2004) ===")
    for label, vals in BASILAKOS_PLIONIS_2004.items():
        print(f"{label}: r0={vals['r0_hinv_mpc']} h^-1 Mpc, gamma={vals['gamma']}")


if __name__ == "__main__":
    main()
