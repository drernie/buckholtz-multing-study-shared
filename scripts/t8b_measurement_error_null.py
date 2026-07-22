"""t8b_measurement_error_null.py — measurement-error NULL for R010/T8.

Question (adversarial re-review P0): the T8 algebra explains WHY a negative partial
correlation r(delta_M, E_ICM | M_WL) exists (both variables share T_X: M_hydro is the
HSE mass built from T_X, so delta_M = M_WL - M_hydro anti-correlates with T_X, while
E_ICM = M_gas * T_X correlates with it). But the algebra does NOT guarantee the specific
observed value r = -0.701. Decisive closure test: build a generative NULL in which the
true state has NO delta_M<->E_ICM physics beyond the definitional T_X coupling, add
REALISTIC measurement errors, and ask where -0.701 sits in the resulting null band.

Two independent null constructions (guardrail: run both when a modeling choice is debatable):
  Variant B (headline, assumption-light): bootstrap the real 50 rows, then PERMUTE the
     HSE-residual-at-fixed-T_X across clusters. This destroys any real correlation between
     HSE-bias (at fixed T_X) and ICM energy, while preserving all marginals, the T_X
     coupling, AND the real per-cluster measurement errors baked into the data (no
     double-counting, no parametric assumption).
  Variant A (forward measurement-error model, enables error-level sensitivity): draw true
     (M_WL, T_X, M_gas) from a multivariate lognormal fit (standard cluster scalings), set
     true M_hydro from the empirical HSE relation M_hydro ~ T_X^b + INDEPENDENT intrinsic
     scatter (the "no extra physics" assumption), then add per-cluster measurement noise
     scaled by k in {0, 0.5, 1, 2}.

Data: experiments/20260713-h1e-agn-feedback-confound/artifacts/cccp_mahdavi2013_merged.csv
      (Mahdavi et al. 2013, arXiv:1210.3689). Per-cluster errors are REAL (paper columns
      T_X_err, M_WL_err, M_Gas_err, M_hydro_err) -> no [WEAK] fractional-error assumption.
Labels: NOT_VALIDATION · NO_AUTHOR_ERROR · OUR_STATISTICAL_AUDIT of a cluster-physics
        artifact (T8 already established this observable is NOT TJB's WHIM mechanism).
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
R_OBS = -0.7008  # recomputed below; constant kept for reference in prints


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
    """Return (median, p5, p95) of a null sample array."""
    return (
        float(np.median(samples)),
        float(np.percentile(samples, 5)),
        float(np.percentile(samples, 95)),
    )


def two_sided_tail(samples, r_obs):
    """Fraction of null draws at least as extreme (|r| >= |r_obs|) as observed."""
    return float(np.mean(np.abs(samples) >= abs(r_obs)))


def percentile_of(samples, r_obs):
    return float(np.mean(samples <= r_obs) * 100.0)


def main() -> None:  # noqa: PLR0915 (single linear report script)
    rng = np.random.default_rng(SEED)
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
    print("T8b — measurement-error NULL for r(delta_M, E_ICM | M_WL)")
    print("NOT_VALIDATION · NO_AUTHOR_ERROR · OUR_STATISTICAL_AUDIT")
    print("=" * 78)
    print(f"N = {n} CCCP clusters | observed r(dM,E|M_WL) = {r_obs:+.4f}")
    print(f"({N_CATALOGS:,} null catalogs per model, seed={SEED})")

    # ---- empirical HSE relation  log M_hydro = a + b log T_X  (natural log) ----
    lt, lh = np.log(t_x), np.log(m_hy)
    b_hse, a_hse = np.polyfit(lt, lh, 1)
    hse_resid = lh - (a_hse + b_hse * lt)
    sig_hse_obs = np.std(hse_resid, ddof=2)  # observed conditional scatter (ln units)

    # ---- real per-cluster FRACTIONAL measurement errors (Mahdavi+2013 columns) ----
    frac = {
        "wl": col("M_WL_err") / m_wl,
        "tx": col("T_X_err") / t_x,
        "gas": col("M_Gas_err") / m_gas,
        "hy": col("M_hydro_err") / m_hy,
    }
    print(
        "\n[errors] median fractional (real, per-cluster): "
        f"T_X={np.median(frac['tx']):.3f} M_WL={np.median(frac['wl']):.3f} "
        f"M_gas={np.median(frac['gas']):.3f} M_hydro={np.median(frac['hy']):.3f}"
    )
    print(
        f"[HSE fit] log M_hydro = {a_hse:+.3f} + {b_hse:+.3f} log T_X | "
        f"cond.scatter(ln)={sig_hse_obs:.3f}"
    )

    # deconvolve intrinsic HSE scatter: observed^2 = intrinsic^2 + measurement^2
    sig_meas_hy = np.sqrt(np.median(frac["hy"]) ** 2 + (b_hse * np.median(frac["tx"])) ** 2)
    sig_hse_int = np.sqrt(max(sig_hse_obs**2 - sig_meas_hy**2, 0.0))
    print(
        f"[HSE fit] measurement part(ln)={sig_meas_hy:.3f} -> intrinsic HSE "
        f"scatter(ln)={sig_hse_int:.3f}"
    )

    # ============================================================
    # VARIANT B — bootstrap + permute HSE residual (assumption-light headline)
    # ============================================================
    rB = np.empty(N_CATALOGS)
    for i in range(N_CATALOGS):
        idx = rng.integers(0, n, n)  # bootstrap rows (real errors baked in)
        wl_b, tx_b, gas_b = m_wl[idx], t_x[idx], m_gas[idx]
        res_b = hse_resid[idx]
        res_perm = rng.permutation(res_b)  # kill extra physics at fixed T_X
        mhy_null = np.exp(a_hse + b_hse * np.log(tx_b) + res_perm)
        dM_null = wl_b - mhy_null
        E_b = gas_b * tx_b
        rB[i] = partial_r(dM_null, E_b, wl_b)
    medB, lo5B, hi95B = band(rB)
    print("\n" + "-" * 78)
    print("VARIANT B (bootstrap + permuted HSE residual; real errors, no parametric model)")
    print(f"  null median = {medB:+.3f}   5-95% band = [{lo5B:+.3f}, {hi95B:+.3f}]")
    print(
        f"  observed {r_obs:+.4f} at percentile {percentile_of(rB, r_obs):5.1f}%  "
        f"| two-sided tail P(|r_null|>=|r_obs|) = {two_sided_tail(rB, r_obs):.3f}"
    )

    # ============================================================
    # VARIANT A — forward measurement-error model (MVN true + HSE + noise*k)
    # ============================================================
    log3 = np.column_stack([np.log(m_wl), np.log(t_x), np.log(m_gas)])
    mu = log3.mean(axis=0)
    cov = np.cov(log3.T)

    def variant_a(k):
        r = np.empty(N_CATALOGS)
        for i in range(N_CATALOGS):
            true = rng.multivariate_normal(mu, cov, size=n)
            wl_t, tx_t, gas_t = np.exp(true[:, 0]), np.exp(true[:, 1]), np.exp(true[:, 2])
            # HSE-definitional true M_hydro: depends ONLY on T_X + independent intrinsic scatter
            mhy_t = np.exp(a_hse + b_hse * np.log(tx_t) + rng.normal(0, sig_hse_int, n))
            if k > 0:
                fw = rng.choice(frac["wl"], n)
                ft = rng.choice(frac["tx"], n)
                fg = rng.choice(frac["gas"], n)
                fh = rng.choice(frac["hy"], n)
                wl_o = np.clip(wl_t * (1 + rng.normal(0, k * fw)), 0.05, None)
                tx_o = np.clip(tx_t * (1 + rng.normal(0, k * ft)), 0.05, None)
                gas_o = np.clip(gas_t * (1 + rng.normal(0, k * fg)), 0.01, None)
                mhy_o = np.clip(mhy_t * (1 + rng.normal(0, k * fh)), 0.05, None)
            else:
                wl_o, tx_o, gas_o, mhy_o = wl_t, tx_t, gas_t, mhy_t
            dM_o = wl_o - mhy_o
            E_o = gas_o * tx_o
            r[i] = partial_r(dM_o, E_o, wl_o)
        return r

    print("\n" + "-" * 78)
    print("VARIANT A (forward model) — measurement-error SENSITIVITY (anti-cherry-pick)")
    print(
        f"{'k*err':>7} | {'null med':>9} {'p5':>8} {'p95':>8} | "
        f"{'obs %ile':>8} {'2-sided tail':>12}"
    )
    for k in (0.0, 0.5, 1.0, 2.0):
        rA = variant_a(k)
        med, lo5, hi95 = band(rA)
        label = "0 (none)" if k == 0 else f"x{k:.1f}"
        print(
            f"{label:>7} | {med:+9.3f} {lo5:+8.3f} {hi95:+8.3f} | "
            f"{percentile_of(rA, r_obs):7.1f}% {two_sided_tail(rA, r_obs):12.3f}"
        )

    print("\n" + "=" * 78)
    print("READ-OUT:")
    print("  If -0.701 sits INSIDE the null 5-95% band (typical) -> R010 partial-r is a")
    print("  measurement-structure / definitional-coupling ARTIFACT; no extra physics needed.")
    print("  If -0.701 sits in the extreme tail -> residual beyond definitional coupling.")
    print("  Non-circularity check: k=0 row isolates definitional coupling (no meas. error);")
    print("  Variant B uses NO fitted forward model, only permutation of the real residual.")
    print("=" * 78)


if __name__ == "__main__":
    main()
