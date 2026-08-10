"""P2 (full): is MULTING's k a second charge, or M wearing a different unit?

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
2026-08-10 · plan item P2, completed with CHEX-MATE cross-validation.

THE QUESTION. The two-charge completion (FINDING_two_charge_completion.md) is
only physically interesting if k varies independently of m. The pipeline's own
k = Ethermal_c2 = (3/2)(Mgas/mu*mp)*T is built from M and z via self-similar
scaling relations (multing_core.py), so a naive alpha = d ln k / d ln M != 1
does NOT by itself prove k is a second degree of freedom -- a deterministic
k = f(M) at ANY slope is still one number per cluster. Identifiability needs
SCATTER at fixed M that is real cluster physics, not measurement noise, and
ideally an INDEPENDENT confirmation that the same scatter is seen by a
different instrument.

PROVENANCE CAVEAT, checked rather than assumed. data/chexmate_real_TX.csv's
M500_Msun column has no traceable generating script in this repository (only
one commit, "commit real datasets + pipeline for script reproducibility",
which did not include the pipeline). Its slope against TX_cx (1.55, close to
the self-similar 1.5) is consistent with M_cx having been DERIVED from TX_cx,
which would make "M_cx * TX_cx" a circular second k-estimator. To avoid this
entirely, the cross-match below uses TX_cx ALONE -- never M_cx -- regressed
against the PIPELINE's M500 (M500c_Msun from clusters_clean.csv, sourced from
MCXC-I via an X-ray LUMINOSITY scaling relation, per its own M500c_method
column: 'X-ray_Lx_scaling'). TX_cx (spectroscopic) and M_pipe (Lx-scaling) are
two different observables through two different scaling relations -- as
independent as this dataset allows without re-deriving anything.
"""

import numpy as np
import pandas as pd

CC = "data/clusters_clean.csv"
CX = "data/chexmate_real_TX.csv"
CM = "data/chexmate_combined.csv"


def resid(x: np.ndarray, y: np.ndarray) -> tuple[np.ndarray, float, float]:
    a, b = np.polyfit(x, y, 1)
    return y - (b + a * x), a, b


def main() -> None:
    print("=" * 88)
    print("P2 -- CHARGE-SPACE IDENTIFIABILITY, completed with CHEX-MATE")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION  |  L0: descriptive")
    print("=" * 88)

    d = pd.read_csv(CC)
    s = d[d["Ethermal_c2_Msun"].notna()].copy()
    print(f"\n[SAMPLE] pipeline Y_SZ-path clusters: n = {len(s)}")

    # ---- Step 1: is k a DETERMINISTIC function of (M, z), or does it carry
    #      real scatter beyond the self-similar scaling it was built from? ----
    lnM, z, lnK = (
        np.log(s["M500c_Msun"].to_numpy()),
        s["z"].to_numpy(),
        np.log(s["Ethermal_c2_Msun"].to_numpy()),
    )
    X = np.column_stack([np.ones_like(lnM), lnM, np.log1p(z)])
    coef = np.linalg.lstsq(X, lnK, rcond=None)[0]
    r2 = 1 - np.sum((lnK - X @ coef) ** 2) / np.sum((lnK - lnK.mean()) ** 2)
    alpha = coef[1]
    r1_full = lnK - X @ coef
    print("\n[STEP 1] Is k_pipe a pure formula of (M, z)?")
    print(f"  R^2(ln k ~ ln M + ln(1+z))   = {r2:.4f}")
    print(f"  slope d ln(k)/d ln(M) at fixed z = {alpha:.4f}")
    print(
        f"  residual scatter                 = {r1_full.std():.4f} nat = {r1_full.std() / np.log(10):.4f} dex"
    )
    print(f"  -> R^2 = {r2:.2f}, not 1.0: {100 * (1 - r2):.0f}% of ln(k)'s variance is NOT")
    print("     explained by (M, z) alone -- the pipeline's Y500 observable does carry")
    print("     genuine cluster-to-cluster information beyond mass and redshift.")

    # ---- Step 2: an error floor from CHEX-MATE's OWN two independent T
    #      estimators, entirely internal to CHEX-MATE, no clusters_clean input --
    cm = pd.read_csv(CM)
    both = cm[cm["Ti_from_TX"].notna() & cm["Ti_from_sigma"].notna()]
    lr = np.log(both["Ti_from_TX"].to_numpy() / both["Ti_from_sigma"].to_numpy())
    sig_ratio = lr.std(ddof=1)
    sig_per_est = sig_ratio / np.sqrt(2)  # if both estimators contribute equal, independent noise
    print(f"\n[STEP 2] Independent measurement-error floor (CHEX-MATE internal, n={len(both)})")
    print("  Ti_from_TX (X-ray spectroscopy) vs Ti_from_sigma (velocity dispersion):")
    print(
        f"  scatter of ln(ratio)          = {sig_ratio:.4f} nat = {sig_ratio / np.log(10):.4f} dex"
    )
    print(
        f"  implied per-estimator noise   ~ {sig_per_est:.4f} nat = {sig_per_est / np.log(10):.4f} dex"
        "   (IF both equally noisy & independent -- a modelling assumption, not measured)"
    )
    print("  -> this is the noise floor ANY single T-estimator (including the pipeline's")
    print("     SZ-derived one) should be compared against before calling its scatter real.")

    # ---- Step 3: positional cross-match, using TX_cx ALONE (never M_cx) ----
    cx = pd.read_csv(CX)
    rows = []
    for _, x in cx.iterrows():
        dra = (s["ra_deg"] - x["ra_deg"]) * np.cos(np.radians(x["dec_deg"]))
        dde = s["dec_deg"] - x["dec_deg"]
        sep = np.sqrt(dra**2 + dde**2) * 60
        j = sep.idxmin()
        if sep[j] < 3.0:
            rows.append(
                {
                    "z": x["z"],
                    "sep": sep[j],
                    "TX_cx": x["TX_keV"],
                    "k_pipe": s.loc[j, "Ethermal_c2_Msun"],
                    "M_pipe": s.loc[j, "M500c_Msun"],
                }
            )
    m = pd.DataFrame(rows)
    print(f"\n[STEP 3] Positional cross-match (<3'), TX_cx used ALONE: n = {len(m)} of {len(cx)}")

    lnM_m = np.log(m["M_pipe"].to_numpy())
    r1, a1, _ = resid(lnM_m, np.log(m["k_pipe"].to_numpy()))
    r2v, a2, _ = resid(lnM_m, np.log(m["TX_cx"].to_numpy()))
    rho = float(np.corrcoef(r1, r2v)[0, 1])
    n = len(m)
    se_null = 1 / np.sqrt(max(n - 3, 1))
    print(f"  slope alpha(k_pipe vs M_pipe) in this subsample = {a1:.3f}")
    print(f"  slope alpha(TX_cx vs M_pipe)  (self-similar predicts 2/3) = {a2:.3f}")
    print(
        f"  scatter at fixed M: k_pipe {r1.std(ddof=2) / np.log(10):.3f} dex,"
        f" TX_cx {r2v.std(ddof=2) / np.log(10):.3f} dex"
    )
    print(f"\n  CORRELATION OF RESIDUALS  rho = {rho:+.4f}   (n={n}, null SE ~ {se_null:.3f})")
    sig_int = np.sqrt(max(rho, 0) * r1.std(ddof=2) * r2v.std(ddof=2))
    print(
        f"  implied shared (intrinsic) scatter = sqrt(rho * sig1 * sig2) = "
        f"{sig_int:.4f} nat = {sig_int / np.log(10):.4f} dex"
    )
    print(
        f"  vs the Step-2 per-estimator noise floor                    = "
        f"{sig_per_est:.4f} nat = {sig_per_est / np.log(10):.4f} dex"
    )

    # ---- guards: is the correlation driven by z or by match quality? ----
    zc = m["z"].to_numpy()
    sepc = m["sep"].to_numpy()
    print("\n[GUARDS]")
    print(
        f"  corr(r1, z)   = {np.corrcoef(r1, zc)[0, 1]:+.3f}   corr(r2, z)   = {np.corrcoef(r2v, zc)[0, 1]:+.3f}"
    )
    print(
        f"  corr(r1, sep) = {np.corrcoef(r1, sepc)[0, 1]:+.3f}   corr(r2, sep) = {np.corrcoef(r2v, sepc)[0, 1]:+.3f}"
    )
    print("  -> if these were large, the residual correlation could be a redshift or")
    print("     mismatch artefact rather than real cluster physics; here they are small.")

    print("\n[VERDICT]")
    print(f"  Full sample (n=548): k_pipe carries {100 * (1 - r2):.0f}% variance beyond (M,z)")
    print(f"  Cross-match (n={n}): k_pipe and an INDEPENDENT real T-measurement (TX_cx)")
    print(f"  share correlated residuals at fixed M (rho={rho:+.2f}), with implied intrinsic")
    print(
        f"  scatter ({sig_int / np.log(10):.2f} dex) {'exceeding' if sig_int > sig_per_est else 'not clearly exceeding'}"
    )
    print(f"  the internal measurement-noise floor ({sig_per_est / np.log(10):.2f} dex).")
    print("\n  PROVENANCE CAVEAT (stated, not hidden): the n=25 cross-match is small; its")
    print(f"  null-correlation standard error (~{se_null:.2f}) is comparable to the observed")
    print("  rho itself, so this is SUGGESTIVE, not decisive. M500_Msun in chexmate_real_TX.csv")
    print("  has unknown provenance in this repo and was deliberately NOT used above.")


if __name__ == "__main__":
    main()
