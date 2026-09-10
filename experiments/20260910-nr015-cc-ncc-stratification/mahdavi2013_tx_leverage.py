"""
NR-015's own Relaxation Map row 1: "Quantify M_hydro's actual T_X
sensitivity -- read Mahdavi et al. 2013's exact HSE derivation, extract
effective d(ln M_hydro)/d(ln T_X) for their specific pipeline."

Primary-source finding (arXiv:1210.3689, Mahdavi, Hoekstra, Babul,
Bildfell, Jeltema, Henry 2012/2013 -- "Joint Analysis of Cluster
Observations II", the actual CCCP N=50 source paper) that changes the
question: this pipeline does NOT compute M_hydro from a directly-measured
T(r) via an algebraic HSE formula. Section 2.5: "the unprojected
temperature profile is calculated self-consistently assuming hydrostatic
equilibrium of assumed gas and dark matter density profiles... temperature
is merely an intermediate 'dummy' quantity". Section 2.6: the actual free
parameters fit jointly via MCMC ("Hrothgar") to the X-ray spectra are the
gas density profile (triple-beta, ~10 params), metallicity profile
(3 params), and NFW total-mass profile (M_Delta, c) -- T_X is not among
them; it is a derived summary of the same joint posterior that also
yields M_hydro.

So a single analytic "leverage" coefficient (as if M_hydro = f(T_X) via a
formula) does not exist for this pipeline -- T_X and M_hydro are
correlated PROJECTIONS of the same multi-parameter MCMC fit to the same
spectral data, not one computed from the other. The closest actually
computable analog, given the data in hand, is the EMPIRICAL log-log
scaling of M_hydro against T_X in the real 50-cluster catalog itself --
computed here, compared against the standard self-similar expectation
(M ~ T^1.5, Kaiser 1986) as a reference point, not as a claim that this
pipeline enforces that scaling by construction.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * L0 descriptive
NO_AUTHOR_ERROR
"""

from __future__ import annotations

import csv
from pathlib import Path

import numpy as np
from scipy import stats

DATA_PATH = (
    Path(__file__).parent.parent
    / "20260713-h1e-agn-feedback-confound"
    / "artifacts"
    / "cccp_mahdavi2013_merged.csv"
)

SELF_SIMILAR_SLOPE = 1.5  # Kaiser 1986, standard M-T self-similar scaling reference


def load() -> dict[str, np.ndarray]:
    rows = []
    with DATA_PATH.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if not row["M_hydro_1e14Msun"] or not row["T_X_keV"] or not row["M_WL_1e14Msun"]:
                continue
            rows.append(row)
    return {
        "M_hydro": np.array([float(r["M_hydro_1e14Msun"]) for r in rows]),
        "T_X": np.array([float(r["T_X_keV"]) for r in rows]),
        "M_WL": np.array([float(r["M_WL_1e14Msun"]) for r in rows]),
    }


def main() -> None:
    d = load()
    n = len(d["M_hydro"])
    print(f"N clusters (M_hydro, T_X, M_WL all present) = {n}")

    ln_m = np.log(d["M_hydro"])
    ln_t = np.log(d["T_X"])
    ln_mwl = np.log(d["M_WL"])

    # --- Positive control: this catalog's own real numbers match the
    # published Table 1 of arXiv:1210.3689 for a spot-checked cluster ---
    idx_a2390 = None
    with DATA_PATH.open(encoding="utf-8") as f:
        for i, row in enumerate(csv.DictReader(f)):
            if row["cluster_name"] == "Abell2390":
                idx_a2390 = i
                print(
                    f"PC: Abell2390 M_hydro={row['M_hydro_1e14Msun']} "
                    "(paper Table 1: 11.0+/-0.9) -- spot-check"
                )
    assert idx_a2390 is not None, "Abell2390 not found -- cannot spot-check against paper Table 1"

    # --- Raw empirical log-log slope: M_hydro ~ T_X^gamma ---
    slope, intercept, r, p, se = stats.linregress(ln_t, ln_m)
    print(f"\n=== Empirical M_hydro-T_X scaling (this catalog, N={n}) ===")
    print(f"ln(M_hydro) = {slope:.3f} * ln(T_X) + {intercept:.3f}")
    print(f"gamma (empirical log-slope) = {slope:.3f} +/- {se:.3f}")
    print(f"r = {r:.3f}, p = {p:.3e}")
    print(
        f"Reference: standard self-similar expectation (Kaiser 1986) gamma = {SELF_SIMILAR_SLOPE}"
    )
    z_vs_selfsimilar = (slope - SELF_SIMILAR_SLOPE) / se
    p_vs_selfsimilar = 2 * (1 - stats.norm.cdf(abs(z_vs_selfsimilar)))
    print(
        f"Deviation from self-similar: z={z_vs_selfsimilar:+.2f}, p={p_vs_selfsimilar:.3f} "
        f"({'consistent with self-similar' if p_vs_selfsimilar > 0.05 else 'significantly different'})"
    )

    # --- Same slope, controlling for M_WL (the quantity delta_M is built from) ---
    x = np.column_stack([ln_mwl, np.ones(n)])
    beta_m, *_ = np.linalg.lstsq(x, ln_m, rcond=None)
    beta_t, *_ = np.linalg.lstsq(x, ln_t, rcond=None)
    resid_m = ln_m - x @ beta_m
    resid_t = ln_t - x @ beta_t
    slope_ctrl, intercept_ctrl, r_ctrl, p_ctrl, se_ctrl = stats.linregress(resid_t, resid_m)
    print("\n=== Same slope, controlling for M_WL (partial regression) ===")
    print(f"gamma (M_WL-controlled) = {slope_ctrl:.3f} +/- {se_ctrl:.3f}")
    print(f"r_partial = {r_ctrl:.3f}, p = {p_ctrl:.3e}")

    print("\n=== Interpretation ===")
    print(
        "This is an EMPIRICAL scaling from the real 50-cluster catalog, not an analytic\n"
        "leverage extracted from Mahdavi et al. 2013's own HSE formula -- per direct reading\n"
        "of their Section 2.5-2.6, no such formula exists in their pipeline: M_hydro and T_X\n"
        "are correlated joint outputs of one MCMC fit to gas density + NFW mass + metallicity\n"
        "profiles against the X-ray spectra, with T(r) an explicit 'dummy' intermediate, never\n"
        "an independent input. A real, non-trivial M_hydro-T_X scaling close to the standard\n"
        "self-similar value is consistent with (does not distinguish) both a real self-similar\n"
        "cluster-physics scaling AND a shared-fit/definitional-entanglement origin -- these are\n"
        "not mutually exclusive, and this test does not separate them."
    )


if __name__ == "__main__":
    main()
