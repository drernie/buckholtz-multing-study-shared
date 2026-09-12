"""flamingo_m500c_m200c_overlap.py -- executes
CLAIM_flamingo_m500c_m200c_overlap.md: real M500c vs M200c top-N
selection overlap on FLAMINGO's own real SOAP catalog, replacing the
Step 8a skeptic's own [MEMORY]-tier concentration-scatter estimate
(P230 Response Matrix item 2) with a direct measurement.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * L0 descriptive
NO_AUTHOR_ERROR
"""

import hdfstream
import numpy as np

GLOBAL_N_TOP = 5000
CANDIDATE_NS = [35, 50, 1200]


def main() -> None:
    root = hdfstream.open("cosma", "/")
    halo_file = root["FLAMINGO"]["L1_m9"]["L1_m9"]["SOAP-HBT"]["halo_properties_0077.hdf5"]

    print("Downloading full SO/200_crit/TotalMass array (real, ~61MB)...")
    m200_ds = halo_file["SO"]["200_crit"]["TotalMass"]
    m200_all = np.asarray(m200_ds[:]) * 1e10  # -> Msun
    order_200 = np.argsort(-m200_all)
    top_idx = np.sort(order_200[:GLOBAL_N_TOP])

    print(f"Targeted download: M200c and M500c for the SAME top {GLOBAL_N_TOP} (by M200c) halos...")
    m200 = m200_all[top_idx]
    m500_ds = halo_file["SO"]["500_crit"]["TotalMass"]
    m500 = np.asarray(m500_ds[top_idx]) * 1e10  # -> Msun, SAME halos, SAME indices

    valid = (m200 > 0) & (m500 > 0)
    n_invalid = int((~valid).sum())
    if n_invalid:
        print(
            f"Excluding {n_invalid} halos with non-positive M200c or M500c "
            f"(no SO/500_crit aperture converged for them)."
        )
    m200, m500 = m200[valid], m500[valid]

    ratio = m500 / m200
    print(f"\nShared pool: N={len(m200)} halos with valid M200c AND M500c")
    print(
        f"M500c/M200c ratio: mean={ratio.mean():.4f}, median={np.median(ratio):.4f}, "
        f"SD={ratio.std(ddof=1):.4f}"
    )
    print(
        "  (scatter in ratio, not log-concentration -- reported as the "
        "directly relevant number, not converted to a literature-style "
        "log(c) scatter)"
    )

    order_200_valid = np.argsort(-m200)
    order_500_valid = np.argsort(-m500)

    print(f"\n{'N':>6} {'overlap_count':>14} {'overlap_frac':>13}")
    for n in CANDIDATE_NS:
        if n > len(m200):
            print(f"{n:>6}  (skipped: only {len(m200)} valid halos available)")
            continue
        top_by_200 = set(order_200_valid[:n].tolist())
        top_by_500 = set(order_500_valid[:n].tolist())
        overlap = top_by_200 & top_by_500
        frac = len(overlap) / n
        print(f"{n:>6} {len(overlap):>14} {frac:>13.1%}")

    # boundary-region diagnostic: for the N=1200 case, how does the ratio
    # scatter near the selection boundary compare to the pool overall?
    n_ref = 1200
    if n_ref <= len(m200):
        boundary_lo, boundary_hi = max(0, n_ref - 100), min(len(m200), n_ref + 100)
        boundary_idx_200 = order_200_valid[boundary_lo:boundary_hi]
        boundary_ratio = ratio[boundary_idx_200]
        print(
            f"\nAt the N={n_ref} boundary (ranks {boundary_lo}-{boundary_hi} "
            f"by M200c): ratio mean={boundary_ratio.mean():.4f}, "
            f"SD={boundary_ratio.std(ddof=1):.4f}"
        )


if __name__ == "__main__":
    main()
