"""t8c_leave_one_out_refit.py — leave-one-out (LOO) HSE-slope refit for R010/T8.

Circularity concern (context-asymmetric skeptic review of T8.1, Attack 1, left OPEN):
the T8.1 measurement-error null (scripts/t8b_measurement_error_null.py) reconstructs the
null M_hydro from an HSE slope b_hse = polyfit(log T_X, log M_hydro) that is fit on the
SAME 50 clusters whose r(delta_M, E_ICM | M_WL) = -0.7008 is the test statistic. The
per-cluster HSE residuals that Variant B permutes are ALSO in-sample residuals from that
fit. If real cluster-specific physics (mass-dependent HSE bias, non-thermal pressure
fraction, dynamical state) is baked into that in-sample fit, the null could "launder" it
and look artificially consistent with the observation, making the "artifact" reading
circular.

This script re-runs the T8.1 Variant-B null-generation logic under LEAVE-ONE-OUT:
  For each cluster i (of 50): refit (a_-i, b_-i) on the OTHER 49 clusters, and define the
  OUT-OF-SAMPLE HSE residual  res_loo_i = log M_hydro_i - (a_-i + b_-i * log T_X_i).
  The null then reconstructs each cluster's baseline prediction from its OWN out-of-sample
  slope/intercept and permutes the OUT-OF-SAMPLE residuals across clusters. No single
  in-sample slope and no in-sample residual enters the null.

Reports:
  (1) b_hse spread across the 50 LOO refits (std, min-max range) vs the in-sample value
      -> how much does the slope depend on individual clusters? (leverage / circularity risk)
  (2) out-of-sample vs in-sample residual scatter (LOO residuals are inflated if the fit
      leans on individual points).
  (3) the LOO null band + percentile of the observed r = -0.7008, compared DIRECTLY to the
      in-sample T8.1 Variant-B result (obs at 46.1 percentile).
  (4) [optional] an externally-calibrated literature HSE slope as an alternative to any
      in-sample fit (see LIT_B_HSE below; provenance in the report / [UNKNOWN] if unset).

Observed statistic r = -0.7008 is computed on the REAL reported data (M_hydro from the
paper) and is UNCHANGED by the LOO refit — only the NULL model's reconstruction changes.

Data: experiments/20260713-h1e-agn-feedback-confound/artifacts/cccp_mahdavi2013_merged.csv
      (Mahdavi et al. 2013, arXiv:1210.3689), N=50, real per-cluster errors.
Labels: NOT_VALIDATION · NO_AUTHOR_ERROR · OUR_STATISTICAL_AUDIT (of a cluster-physics
        artifact; T8 already established this observable is NOT TJB's WHIM mechanism).
"""

from __future__ import annotations

import csv
from pathlib import Path

import numpy as np

CSV = (
    Path(__file__).resolve().parent.parent
    / "experiments"
    / "20260713-h1e-agn-feedback-confound"
    / "artifacts"
    / "cccp_mahdavi2013_merged.csv"
)

N_CATALOGS = 20_000
SEED = 20260722

# External literature HSE slope (log M_hydro vs log T_X) for the cross-check in step 6.
# Set to a real, cited value or leave None -> reported as [UNKNOWN]/not attempted.
# Populated after in-session WebSearch (see report for provenance).
# [VERIFIED-WebSearch 2026-07-22] M500-T slope alpha = 1.49 +/- 0.15 for HOT clusters
# (kT > 3.5 keV) — matches the CCCP sample regime (T_X ~ 5-12 keV). Full-sample slope is
# 1.71 +/- 0.09; hot-cluster value chosen as the temperature-matched external anchor.
LIT_B_HSE: float | None = 1.49  # Arnaud, Pointecouteau & Pratt 2005, hot-cluster M500-T500
LIT_B_HSE_SOURCE = "Arnaud, Pointecouteau & Pratt (2005), A&A 441, 893 (2005A&A...441..893A)"


def load():
    rows = list(csv.DictReader(CSV.open(encoding="utf-8")))

    def col(name):
        return np.array([float(r[name]) for r in rows])

    return col


def partial_r(x, y, z):
    """Exact partial correlation r(x, y | z) for a single control variable z."""
    rxy = np.corrcoef(x, y)[0, 1]
    rxz = np.corrcoef(x, z)[0, 1]
    ryz = np.corrcoef(y, z)[0, 1]
    denom = np.sqrt((1.0 - rxz**2) * (1.0 - ryz**2))
    return (rxy - rxz * ryz) / denom


def band(samples):
    return (
        float(np.median(samples)),
        float(np.percentile(samples, 5)),
        float(np.percentile(samples, 95)),
    )


def two_sided_tail(samples, r_obs):
    return float(np.mean(np.abs(samples) >= abs(r_obs)))


def percentile_of(samples, r_obs):
    return float(np.mean(samples <= r_obs) * 100.0)


def loo_fit(lt, lh):
    """Leave-one-out HSE fit.

    Returns per-cluster arrays (a_loo, b_loo) fit on all-but-i, and the out-of-sample
    residual res_loo_i = lh_i - (a_-i + b_-i * lt_i).
    """
    n = len(lt)
    a_loo = np.empty(n)
    b_loo = np.empty(n)
    res_loo = np.empty(n)
    idx_all = np.arange(n)
    for i in range(n):
        mask = idx_all != i
        b_i, a_i = np.polyfit(lt[mask], lh[mask], 1)
        b_loo[i] = b_i
        a_loo[i] = a_i
        res_loo[i] = lh[i] - (a_i + b_i * lt[i])
    return a_loo, b_loo, res_loo


def null_from_slopes(rng, m_wl, t_x, m_gas, a_vec, b_vec, res_vec):
    """Variant-B null using per-cluster (a_vec, b_vec) reconstruction + permuted res_vec.

    a_vec/b_vec/res_vec are indexed by cluster identity. Bootstrap rows, reconstruct each
    drawn cluster's baseline from ITS OWN slope/intercept, permute residuals across the
    drawn set to destroy any delta_M<->E_ICM link at fixed T_X.
    """
    n = len(m_wl)
    out = np.empty(N_CATALOGS)
    for c in range(N_CATALOGS):
        idx = rng.integers(0, n, n)
        wl_b, tx_b, gas_b = m_wl[idx], t_x[idx], m_gas[idx]
        base = a_vec[idx] + b_vec[idx] * np.log(tx_b)  # per-cluster out-of-sample baseline
        res_perm = rng.permutation(res_vec[idx])
        mhy_null = np.exp(base + res_perm)
        dM_null = wl_b - mhy_null
        E_b = gas_b * tx_b
        out[c] = partial_r(dM_null, E_b, wl_b)
    return out


def main() -> None:  # noqa: PLR0915 (single linear report script)
    col = load()
    m_wl = col("M_WL_1e14Msun")
    t_x = col("T_X_keV")
    m_gas = col("M_Gas_1e14Msun")
    m_hy = col("M_hydro_1e14Msun")
    n = len(m_wl)

    dM = m_wl - m_hy
    E = m_gas * t_x
    r_obs = partial_r(dM, E, m_wl)

    print("=" * 78)
    print("T8c — LEAVE-ONE-OUT HSE refit for r(delta_M, E_ICM | M_WL)")
    print("NOT_VALIDATION · NO_AUTHOR_ERROR · OUR_STATISTICAL_AUDIT")
    print("=" * 78)
    print(f"N = {n} CCCP clusters | observed r(dM,E|M_WL) = {r_obs:+.4f} (real data, fixed)")
    print(f"({N_CATALOGS:,} null catalogs, seed={SEED})")

    lt, lh = np.log(t_x), np.log(m_hy)

    # ---- in-sample fit (T8.1 baseline) ----
    b_in, a_in = np.polyfit(lt, lh, 1)
    res_in = lh - (a_in + b_in * lt)
    sig_in = float(np.std(res_in, ddof=2))
    print(f"\n[in-sample fit]  log M_hydro = {a_in:+.3f} + {b_in:+.3f} log T_X")
    print(f"[in-sample]      residual scatter(ln) = {sig_in:.4f}")

    # ---- leave-one-out fits ----
    a_loo, b_loo, res_loo = loo_fit(lt, lh)
    b_std = float(np.std(b_loo, ddof=1))
    b_min, b_max = float(b_loo.min()), float(b_loo.max())
    sig_loo = float(np.std(res_loo, ddof=1))

    print("\n" + "-" * 78)
    print("(1) b_hse SPREAD across 50 leave-one-out refits")
    print(f"    in-sample b_hse      = {b_in:+.4f}")
    print(f"    LOO mean b_hse       = {b_loo.mean():+.4f}")
    print(f"    LOO std  b_hse       = {b_std:.4f}  ({100 * b_std / abs(b_in):.2f}% of |b_in|)")
    print(f"    LOO range b_hse      = [{b_min:+.4f}, {b_max:+.4f}]  span={b_max - b_min:.4f}")
    max_shift = float(np.max(np.abs(b_loo - b_in)))
    print(f"    max |b_-i - b_in|    = {max_shift:.4f}  ({100 * max_shift / abs(b_in):.2f}%)")

    print("\n(2) out-of-sample vs in-sample residual scatter")
    print(f"    in-sample residual std(ln) = {sig_in:.4f}")
    print(f"    LOO  residual std(ln)      = {sig_loo:.4f}  (inflation x{sig_loo / sig_in:.3f})")

    # ---- (3) LOO null vs in-sample Variant-B null ----
    rng_a = np.random.default_rng(SEED)
    null_in = null_from_slopes(
        rng_a,
        m_wl,
        t_x,
        m_gas,
        np.full(n, a_in),
        np.full(n, b_in),
        res_in,
    )
    rng_b = np.random.default_rng(SEED)
    null_loo = null_from_slopes(rng_b, m_wl, t_x, m_gas, a_loo, b_loo, res_loo)

    med_i, lo_i, hi_i = band(null_in)
    med_l, lo_l, hi_l = band(null_loo)

    print("\n" + "-" * 78)
    print("(3) NULL comparison — observed r vs null band (Variant B logic)")
    print(
        f"{'construction':>26} | {'null med':>9} {'p5':>8} {'p95':>8} | "
        f"{'obs %ile':>8} {'2-sided tail':>12}"
    )
    print(
        f"{'in-sample (T8.1 repro)':>26} | {med_i:+9.3f} {lo_i:+8.3f} {hi_i:+8.3f} | "
        f"{percentile_of(null_in, r_obs):7.1f}% {two_sided_tail(null_in, r_obs):12.3f}"
    )
    print(
        f"{'LEAVE-ONE-OUT':>26} | {med_l:+9.3f} {lo_l:+8.3f} {hi_l:+8.3f} | "
        f"{percentile_of(null_loo, r_obs):7.1f}% {two_sided_tail(null_loo, r_obs):12.3f}"
    )

    # ---- (4) external literature-slope cross-check ----
    print("\n" + "-" * 78)
    print("(4) externally-calibrated HSE slope cross-check")
    if LIT_B_HSE is None:
        print("    [UNKNOWN] — no literature slope set; not attempted.")
    else:
        # re-anchor intercept so the literature slope passes through the data centroid
        # (a_lit chosen so mean(lh) = a_lit + b_lit*mean(lt); isolates the SLOPE effect)
        b_lit = float(LIT_B_HSE)
        a_lit = float(lh.mean() - b_lit * lt.mean())
        res_lit = lh - (a_lit + b_lit * lt)
        rng_c = np.random.default_rng(SEED)
        null_lit = null_from_slopes(
            rng_c,
            m_wl,
            t_x,
            m_gas,
            np.full(n, a_lit),
            np.full(n, b_lit),
            res_lit,
        )
        med_t, lo_t, hi_t = band(null_lit)
        print(f"    literature b_hse = {b_lit:+.3f}  [{LIT_B_HSE_SOURCE}]")
        print(f"    (in-sample b_hse = {b_in:+.3f}; literature is external, not fit here)")
        print(
            f"    null med = {med_t:+.3f}  5-95% = [{lo_t:+.3f}, {hi_t:+.3f}]  "
            f"obs %ile = {percentile_of(null_lit, r_obs):.1f}%  "
            f"tail = {two_sided_tail(null_lit, r_obs):.3f}"
        )

    print("\n" + "=" * 78)
    print("READ-OUT:")
    print("  Circularity would show as: (a) large b_hse swing LOO (fit driven by individual")
    print("  clusters), AND (b) the LOO null percentile shifting toward the tail (obs no")
    print("  longer typical of the out-of-sample null). Small b_hse spread + LOO percentile")
    print("  staying near median => the in-sample fit did NOT launder cluster-specific")
    print("  physics; the artifact reading survives the out-of-sample refit.")
    print("=" * 78)


if __name__ == "__main__":
    main()
