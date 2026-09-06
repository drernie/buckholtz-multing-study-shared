"""E8 -- propagate Moresco's own cosmic-chronometer covariance through this
project's own chi2 and (beta1,beta2) degeneracy analysis (P176), and measure
what changes versus the diagonal treatment everyone -- this project included --
has been using.

Covariance recipe copied from Moresco's own notebook
(gitlab.com/mmoresco/CCcovariance, examples/CC_covariance.ipynb, fetched this
session, cell 10-12):

    cov_diag[i,i]  = errHz[i]**2
    cov_X[i,j]     = Hz[i]*x_i * Hz[j]*x_j        x = data_MM20 column / 100,
                                                  np.interp'd to the data z
    cov            = cov_spsooo + cov_imf + cov_diag      <- HIS default

The modelling terms are rank-1 outer products: fully correlated across
redshift, exactly as his README states. np.interp clamps beyond the
data_MM20 range (0.075-1.475) -- that is also his own behaviour for his own
z=1.965 point, reproduced rather than "fixed".

See CLAIM_E8_full_covariance_propagation.md -- MCID pre-registered before
this file was run.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

from __future__ import annotations

import io

import numpy as np
import pandas as pd
import requests
from P176_v82_real_chi2_hessian_degeneracy import (
    CC_POINTS,
    H33,
    SIG_DESI,
    SIG_SHOES,
    TABLE_II,
    Z_SHOES,
    ZFINE,
    H_of_z_kms,
    chi2_fixed_h0anchor,
    s33,
    z33,
)
from scipy.linalg import cho_factor, cho_solve

# [VERIFIED v82.md:763-765] flat LCDM at published values, same 33 points
LCDM_FIXED = {"H0": 67.4, "Om": 0.315, "chi2_tjb": 36.96}
# [VERIFIED v82.md:780-783] flat LCDM freely optimised on the same 33 points
LCDM_FREE = {"H0": 71.83, "Om": 0.2724, "chi2_tjb": 16.31}

# Moresco's own 15 CC points (BC03 table, fetched this session) -- used only to
# decide which of TJB's 31 carry HIS correlated systematic in variant (b).
MORESCO_Z_H = [
    (0.1791, 74.91), (0.1993, 74.96), (0.3519, 82.78), (0.3802, 83.00),
    (0.4004, 76.97), (0.4247, 87.08), (0.4497, 92.78), (0.4783, 80.91),
    (0.5929, 103.80), (0.6797, 91.60), (0.7812, 104.50), (0.8754, 125.10),
    (1.0370, 153.70), (1.3630, 160.00), (1.9650, 186.50),
]  # fmt: skip

N_CC = len(CC_POINTS)
z_cc = np.array([p[0] for p in CC_POINTS])
H_cc = np.array([p[1] for p in CC_POINTS])
s_cc = np.array([p[2] for p in CC_POINTS])


def fetch_mm20() -> pd.DataFrame:
    url = "https://gitlab.com/mmoresco/CCcovariance/-/raw/master/data/data_MM20.dat"
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    return pd.read_csv(
        io.StringIO(r.text),
        sep=r"\s+",
        comment="#",
        header=None,
        names=["z", "imf", "stlib", "sps", "spsooo"],
    )


def moresco_mask() -> np.ndarray:
    """True for TJB points that are Moresco's own (z within 0.005 AND H within 1.0
    -- z alone is ambiguous: TJB has two points at z=0.40)."""
    m = np.zeros(N_CC, dtype=bool)
    for i, (z, h) in enumerate(zip(z_cc, H_cc, strict=True)):
        m[i] = any(abs(z - zm) < 0.005 and abs(h - hm) < 1.0 for zm, hm in MORESCO_Z_H)
    return m


def build_cov_cc(mm20: pd.DataFrame, components: list[str], corr_mask: np.ndarray | None):
    """Moresco's recipe. corr_mask=None -> fully correlated across all 31 (his
    stance, conservative). Otherwise: correlated only among masked points;
    unmasked points still carry the same fractional modelling variance on their
    own diagonal (their SPS dependence exists too) but uncorrelated."""
    C = np.diag(s_cc**2)
    zmod = mm20["z"].to_numpy(float)
    for name in components:
        x = np.interp(z_cc, zmod, mm20[name].to_numpy(float)) / 100.0
        v = H_cc * x
        if corr_mask is None:
            C += np.outer(v, v)
        else:
            vm = np.where(corr_mask, v, 0.0)
            C += np.outer(vm, vm)
            C += np.diag(np.where(corr_mask, 0.0, v**2))
    return C


def embed_33(C_cc: np.ndarray) -> np.ndarray:
    C = np.zeros((N_CC + 2, N_CC + 2))
    C[:N_CC, :N_CC] = C_cc
    C[N_CC, N_CC] = SIG_SHOES**2
    C[N_CC + 1, N_CC + 1] = SIG_DESI**2
    return C


def make_chi2_cov(C33: np.ndarray):
    cf = cho_factor(C33)  # raises LinAlgError if not SPD -> positive control 3

    def chi2(h0a: float, b1: float, b2: float) -> float:
        Hm = H_of_z_kms(ZFINE, h0a, b1, b2, Z_SHOES)
        if np.any(np.isnan(Hm)):
            return 1e12
        r = np.interp(z33, ZFINE, Hm) - H33
        return float(r @ cho_solve(cf, r))

    return chi2


def lcdm_H(z, H0, Om):
    return H0 * np.sqrt(Om * (1 + z) ** 3 + (1 - Om))


def chi2_lcdm_diag(H0, Om):
    r = lcdm_H(z33, H0, Om) - H33
    return float(np.sum((r / s33) ** 2))


def chi2_lcdm_cov(H0, Om, C33):
    r = lcdm_H(z33, H0, Om) - H33
    return float(r @ cho_solve(cho_factor(C33), r))


def hessian_small_eig_and_slope(chi2_fn, h0a, b1f, b2f, h=1e-4):
    """P176's hessian_null_slope, generalised to any chi2 callable."""

    def f(x1, x2):
        return chi2_fn(h0a, x1 * b1f, x2 * b2f)

    f00 = f(1, 1)
    d11 = (f(1 + h, 1) - 2 * f00 + f(1 - h, 1)) / h**2
    d22 = (f(1, 1 + h) - 2 * f00 + f(1, 1 - h)) / h**2
    d12 = (f(1 + h, 1 + h) - f(1 + h, 1 - h) - f(1 - h, 1 + h) + f(1 - h, 1 - h)) / (4 * h**2)
    eig, vec = np.linalg.eigh(np.array([[d11, d12], [d12, d22]]))
    v = vec[:, 0]
    return eig, (v[1] * b2f) / (v[0] * b1f)


# ---------------------------------------------------------------------------
# Controls
# ---------------------------------------------------------------------------
def test_positive_control_table_ii_diag():
    for lab in ("unconstrained_spotlighted", "planck_exact_100pct"):
        h0a, b1, b2, ref = TABLE_II[lab]
        assert abs(chi2_fixed_h0anchor(h0a, b1, b2) - ref) / ref < 1e-3, lab


def test_positive_control_lcdm_diag():
    for lab, d in (("fixed", LCDM_FIXED), ("free", LCDM_FREE)):
        got = chi2_lcdm_diag(d["H0"], d["Om"])
        rel = abs(got - d["chi2_tjb"]) / d["chi2_tjb"]
        assert rel < 5e-3, f"LCDM {lab}: got {got:.3f}, TJB {d['chi2_tjb']} (rel {rel:.2%})"
        yield lab, got, rel


def test_positive_control_zero_components_reduces_to_diag(mm20):
    C = embed_33(build_cov_cc(mm20, [], None))
    chi2c = make_chi2_cov(C)
    h0a, b1, b2, _ = TABLE_II["unconstrained_spotlighted"]
    a, b = chi2c(h0a, b1, b2), chi2_fixed_h0anchor(h0a, b1, b2)
    assert abs(a - b) / b < 1e-9, f"{a} vs {b}"


if __name__ == "__main__":
    mm20 = fetch_mm20()
    print(f"data_MM20.dat fetched: {len(mm20)} bins, z={mm20.z.min():.3f}-{mm20.z.max():.3f}")
    print(
        "  mean % of H: "
        + ", ".join(f"{c}={mm20[c].mean():.2f}" for c in ("imf", "stlib", "sps", "spsooo"))
    )

    test_positive_control_table_ii_diag()
    print("PC1 diagonal chi2 reproduces TJB Table II (2 rows, <0.1%): PASS")
    for lab, got, rel in test_positive_control_lcdm_diag():
        print(
            f"PC2 diagonal chi2 LCDM-{lab}: {got:.3f} vs TJB {LCDM_FIXED['chi2_tjb'] if lab == 'fixed' else LCDM_FREE['chi2_tjb']} (rel {rel:.3%}): PASS"
        )
    test_positive_control_zero_components_reduces_to_diag(mm20)
    print("PC3 covariance path with zero modelling terms == diagonal path (<1e-9): PASS")

    mask = moresco_mask()
    print(f"\nMoresco's own points among TJB's 31: {mask.sum()} (expected 15)")

    variants = {
        "diag (as everyone uses)": None,
        "Moresco default [spsooo+imf], all 31 correlated": (["spsooo", "imf"], None),
        "Moresco default, only his 15 correlated": (["spsooo", "imf"], mask),
        "stress [sps+imf], all 31 correlated": (["sps", "imf"], None),
    }

    rows = [
        ("MULTING spotlighted", *TABLE_II["unconstrained_spotlighted"][:3]),
        ("MULTING sh0es_0pct", *TABLE_II["sh0es_anchored_0pct"][:3]),
        ("MULTING pct_50", *TABLE_II["pct_50"][:3]),
        ("MULTING planck_100pct", *TABLE_II["planck_exact_100pct"][:3]),
    ]

    print("\n" + "=" * 96)
    print(
        f"{'variant':<48} {'spot':>7} {'sh0es':>7} {'pct50':>7} {'plnck':>7} {'LCDMfx':>7} {'LCDMfr':>7}"
    )
    print("=" * 96)
    results = {}
    for vname, spec in variants.items():
        if spec is None:
            c = lambda h, a, b: chi2_fixed_h0anchor(h, a, b)  # noqa: E731
            lf = chi2_lcdm_diag(LCDM_FIXED["H0"], LCDM_FIXED["Om"])
            lr = chi2_lcdm_diag(LCDM_FREE["H0"], LCDM_FREE["Om"])
            C33 = None
        else:
            comps, cm = spec
            C33 = embed_33(build_cov_cc(mm20, comps, cm))
            c = make_chi2_cov(C33)  # PC4: Cholesky must succeed
            lf = chi2_lcdm_cov(LCDM_FIXED["H0"], LCDM_FIXED["Om"], C33)
            lr = chi2_lcdm_cov(LCDM_FREE["H0"], LCDM_FREE["Om"], C33)
        vals = [c(h, a, b) for _, h, a, b in rows]
        results[vname] = (vals, lf, lr, c)
        print(f"{vname:<48} " + " ".join(f"{v:7.2f}" for v in vals) + f" {lf:7.2f} {lr:7.2f}")

    print("\n" + "=" * 96)
    print("ENDPOINT 1 -- discriminating power: dchi2 = chi2(LCDM) - chi2(MULTING spotlighted)")
    print("=" * 96)
    base_fx = results["diag (as everyone uses)"][1] - results["diag (as everyone uses)"][0][0]
    base_fr = results["diag (as everyone uses)"][2] - results["diag (as everyone uses)"][0][0]
    print(
        f"{'variant':<48} {'vs LCDM fixed':>14} {'vs LCDM free':>13}  {'|change fx|':>10} {'|change fr|':>10}"
    )
    for vname, (vals, lf, lr, _) in results.items():
        dfx, dfr = lf - vals[0], lr - vals[0]
        print(
            f"{vname:<48} {dfx:14.2f} {dfr:13.2f}  {abs(dfx - base_fx):10.2f} {abs(dfr - base_fr):10.2f}"
        )
    print("\nMCID (pre-registered): MATERIAL if |change| > 2.0 or sign flips.")

    print("\n" + "=" * 96)
    print("ENDPOINT 2 -- (beta1,beta2) degeneracy at the spotlighted row (P176 Hessian)")
    print("=" * 96)
    h0a, b1, b2, _ = TABLE_II["unconstrained_spotlighted"]
    eig0, slope0 = None, None
    print(
        f"{'variant':<48} {'small eig':>10} {'large eig':>10} {'ratio':>8} {'null slope':>12} {'eig x':>7} {'slope %':>8}"
    )
    for vname, (_, _, _, cfn) in results.items():
        eig, slope = hessian_small_eig_and_slope(cfn, h0a, b1, b2)
        if eig0 is None:
            eig0, slope0 = eig, slope
        print(
            f"{vname:<48} {eig[0]:10.3f} {eig[1]:10.1f} {eig[1] / eig[0]:8.0f} {slope:12.4e} "
            f"{eig[0] / eig0[0]:7.2f} {100 * (slope / slope0 - 1):+8.2f}"
        )
    print(
        "\nMCID (pre-registered): MATERIAL if small-eig factor outside [0.5, 2.0] or |slope change| > 20%."
    )

    print("\n" + "=" * 96)
    print("NEGATIVE CONTROL -- 100% fully-correlated modelling term must collapse discrimination")
    print("=" * 96)
    mm_abs = mm20.copy()
    mm_abs["absurd"] = 100.0
    Cabs = embed_33(build_cov_cc(mm_abs, ["absurd"], None))
    cabs = make_chi2_cov(Cabs)
    va = [cabs(h, a, b) for _, h, a, b in rows]
    la = chi2_lcdm_cov(LCDM_FIXED["H0"], LCDM_FIXED["Om"], Cabs)
    print(f"MULTING rows: {', '.join(f'{v:.2f}' for v in va)} | LCDM fixed: {la:.2f}")
    print(
        f"spread across all 5 models: {max(va + [la]) - min(va + [la]):.3f}  (diag spread was "
        f"{max(results['diag (as everyone uses)'][0] + [results['diag (as everyone uses)'][1]]) - min(results['diag (as everyone uses)'][0] + [results['diag (as everyone uses)'][1]]):.2f})"
    )
