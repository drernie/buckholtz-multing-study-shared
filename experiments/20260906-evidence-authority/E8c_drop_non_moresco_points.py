"""E8c -- the skeptic's decisive missing test for E8/E8b.

E8 applied Moresco's fractional modelling systematic to ALL 31 CC points. 16
of them are from other groups (Simon+05, Stern+10, Zhang+14, Ratsimbazafy+17,
...) whose own systematic budgets are NOT Moresco's -- extending his fractions
to their points may MANUFACTURE a systematic those groups never quoted.

Kill criterion (pre-stated by the skeptic, adopted verbatim): if restricting to
Moresco's own 15 CC points (+ SH0ES + DESI = 17 points) and re-optimising both
models under his covariance RESTORES the paper's positive dchi2, then most of
E8's sign flip was manufactured by the extension. If dchi2 stays negative, E8's
structure holds.

Two isolations, both run:
  (i)  DROP:  17-point set (15 Moresco CC + 2 anchors), diag vs Moresco cov.
  (ii) ZERO:  full 33-point set, Moresco cov on his 15 only, and ZERO modelling
              variance on the other 16 (pure errHz) -- unlike E8's variant (b),
              which still added his fractional variance to their diagonals.

Interpretation floor (from E8b): |dchi2| < 1 on these dof is not evidence for
either model. The question here is narrower still: is E8's SIGN an artefact of
the 16-point extension?

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

from __future__ import annotations

import numpy as np
from E8_full_covariance_propagation import (
    LCDM_FREE,
    TABLE_II,
    H_cc,
    fetch_mm20,
    lcdm_H,
    moresco_mask,
    s_cc,
    z_cc,
)
from E8b_reoptimize_under_covariance import opt_lcdm, opt_multing
from P176_v82_real_chi2_hessian_degeneracy import (
    H_DESI,
    H_SHOES,
    SIG_DESI,
    SIG_SHOES,
    Z_DESI,
    Z_SHOES,
    ZFINE,
    H_of_z_kms,
)
from scipy.linalg import cho_factor, cho_solve


def cov_subset(z, H, s, mm20, components, corr_mask=None):
    """Moresco's recipe on an arbitrary CC subset. corr_mask=None -> all
    correlated. Otherwise correlated only within mask, and -- unlike E8 --
    ZERO modelling variance outside it."""
    C = np.diag(s**2)
    zmod = mm20["z"].to_numpy(float)
    for name in components:
        x = np.interp(z, zmod, mm20[name].to_numpy(float)) / 100.0
        v = H * x
        if corr_mask is not None:
            v = np.where(corr_mask, v, 0.0)
        C += np.outer(v, v)
    return C


def with_anchors(z, H, C_cc):
    n = len(z)
    z_all = np.concatenate([z, [Z_SHOES, Z_DESI]])
    H_all = np.concatenate([H, [H_SHOES, H_DESI]])
    C = np.zeros((n + 2, n + 2))
    C[:n, :n] = C_cc
    C[n, n], C[n + 1, n + 1] = SIG_SHOES**2, SIG_DESI**2
    return z_all, H_all, C


def make_chi2s(z_all, H_all, C):
    cf = cho_factor(C)

    def chi2_m(h0a, b1, b2):
        Hm = H_of_z_kms(ZFINE, h0a, b1, b2, Z_SHOES)
        if np.any(np.isnan(Hm)):
            return 1e12
        r = np.interp(z_all, ZFINE, Hm) - H_all
        return float(r @ cho_solve(cf, r))

    def chi2_l(H0, Om):
        r = lcdm_H(z_all, H0, Om) - H_all
        return float(r @ cho_solve(cf, r))

    return chi2_m, chi2_l


def run(label, z_all, H_all, C):
    chi2_m, chi2_l = make_chi2s(z_all, H_all, C)
    fl, xl = opt_lcdm(chi2_l, x0=(LCDM_FREE["H0"], LCDM_FREE["Om"]))
    outs = sorted(
        opt_multing(chi2_m, TABLE_II[s][:3])
        for s in ("unconstrained_spotlighted", "pct_50", "planck_exact_100pct")
    )
    fm, xm = outs[0]
    conv = "ok" if abs(outs[1][0] - outs[0][0]) < 0.05 else "WARN"
    print(
        f"{label:<46} {len(z_all):>3} {fl:8.3f} {xl[0]:6.2f} {xl[1]:7.4f}  "
        f"{fm:8.3f} {xm[0]:6.2f}  {fl - fm:+7.3f} {conv:>5}"
    )
    return fl - fm


if __name__ == "__main__":
    mm20 = fetch_mm20()
    mask = moresco_mask()
    assert mask.sum() == 15, mask.sum()

    z15, H15, s15 = z_cc[mask], H_cc[mask], s_cc[mask]

    print("=" * 104)
    print(
        f"{'variant':<46} {'N':>3} {'LCDM*':>8} {'H0':>6} {'Om':>7}  "
        f"{'MULT*':>8} {'H0a':>6}  {'dchi2':>7} {'conv':>5}"
    )
    print("=" * 104)

    # Reference: the full 33-point diagonal case (must match E8b's +0.561)
    d_ref = run("REF 33 pts, diag (E8b baseline)", *with_anchors(z_cc, H_cc, np.diag(s_cc**2)))

    # (i) DROP to Moresco's 15 + anchors
    d_drop_diag = run("DROP 15+2, diag", *with_anchors(z15, H15, np.diag(s15**2)))
    d_drop_def = run(
        "DROP 15+2, Moresco default [spsooo+imf]",
        *with_anchors(z15, H15, cov_subset(z15, H15, s15, mm20, ["spsooo", "imf"])),
    )
    d_drop_str = run(
        "DROP 15+2, stress [sps+imf]",
        *with_anchors(z15, H15, cov_subset(z15, H15, s15, mm20, ["sps", "imf"])),
    )

    # (ii) ZERO: 33 pts, his 15 correlated, other 16 pure errHz
    d_zero_def = run(
        "ZERO 33 pts, cov on his 15, NOTHING on other 16",
        *with_anchors(z_cc, H_cc, cov_subset(z_cc, H_cc, s_cc, mm20, ["spsooo", "imf"], mask)),
    )
    d_zero_str = run(
        "ZERO 33 pts, stress on his 15, NOTHING on 16",
        *with_anchors(z_cc, H_cc, cov_subset(z_cc, H_cc, s_cc, mm20, ["sps", "imf"], mask)),
    )

    print("\n" + "=" * 104)
    print("KILL CRITERION (skeptic's, adopted verbatim):")
    print(
        "  if the Moresco-only variants RESTORE positive dchi2 -> E8's sign flip was manufactured"
    )
    print("  by extending his fractions to 16 points where they don't apply.")
    print("  if they stay negative -> E8's structure holds.")
    print("=" * 104)
    flipped_back = [d for d in (d_drop_def, d_drop_str, d_zero_def, d_zero_str) if d > 0]
    print(
        f"  sign of dchi2 under Moresco-only covariance, 4 variants: "
        f"{['+' if d > 0 else '-' for d in (d_drop_def, d_drop_str, d_zero_def, d_zero_str)]}"
    )
    print(f"  variants that restore the paper's positive sign: {len(flipped_back)}/4")
    print(
        f"  NOTE the drop-diag row: on 15+2 points with DIAGONAL errors dchi2 = {d_drop_diag:+.3f}"
        f" -- shows what the subset alone does before any covariance enters."
    )
