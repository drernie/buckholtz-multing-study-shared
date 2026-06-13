"""
LOO Leverage Analysis on ε(z) — Hypothesis Lab Test 1

Leave-One-Out (LOO) Pearson r analysis on Table A1 epsilon(z).
Tests which z-points are high-leverage in correlation with candidate k_A proxies.

Implements:
  U1: CI on z_peak from 11-point parametric fit
  U6: Is z=8.5 a high-leverage outlier?

Four proxy candidates:
  Proxy 0: Virial k_A ∝ H(z)^(4/3)              — expected monotone FAIL baseline
  Proxy 1: Gaussian bell at z_peak=0.40           — our hypothesis
  Proxy 2: dN/dz (M8-C survey rate, M_min=1e14)  — best prior result r=0.723
  Proxy 3: Parametric LogNormal fit               — U1 posterior on z_peak

Labels: INTERNAL_DIAGNOSTIC_ONLY · NOT_VALIDATION · TABLE_A1_ONLY
        OUR_RECONSTRUCTION · NOT_AUTHOR_CONFIRMED
"""

from __future__ import annotations

import json
import math
from pathlib import Path

# ── Table A1 data ──────────────────────────────────────────────────────────────
Z = [0.06, 0.14, 0.25, 0.40, 0.65, 1.00, 1.50, 2.10, 3.20, 5.00, 8.50]
H_FLRW = [68.1, 69.3, 71.5, 75.0, 83.0, 95.7, 114.8, 140.3, 187.6, 265.2, 398.5]
H_MULT = [70.2, 73.5, 78.8, 83.1, 91.4, 104.2, 126.5, 151.8, 197.3, 271.5, 418.1]

EPS = [(hm / hf) ** 2 - 1.0 for hm, hf in zip(H_MULT, H_FLRW, strict=False)]

N = len(Z)

# ── ΛCDM parameters (same as m8c) ─────────────────────────────────────────────
OM_M = 0.315
OM_L = 0.685
H0 = 70.0
SIGMA_8 = 0.811
DELTA_C = 1.686
GAMMA_CDM = 0.27
C_KMS = 299792.458


# ── Helper: Pearson r ──────────────────────────────────────────────────────────
def pearson_r(x: list[float], y: list[float]) -> float:
    n = len(x)
    if n < 3:
        return float("nan")
    mx = sum(x) / n
    my = sum(y) / n
    num = sum((xi - mx) * (yi - my) for xi, yi in zip(x, y, strict=False))
    sx = math.sqrt(sum((xi - mx) ** 2 for xi in x))
    sy = math.sqrt(sum((yi - my) ** 2 for yi in y))
    if sx < 1e-12 or sy < 1e-12:
        return float("nan")
    return num / (sx * sy)


# ── Proxy 0: Virial k_A ∝ H(z)^(4/3) (monotone baseline) ─────────────────────
def proxy_virial(z: float) -> float:
    h_z = H0 * math.sqrt(OM_M * (1 + z) ** 3 + OM_L)
    return h_z ** (4.0 / 3.0)


# ── Proxy 1: Gaussian bell at z_peak ──────────────────────────────────────────
def proxy_gaussian(z: float, z_peak: float = 0.40, sigma: float = 0.60) -> float:
    return math.exp(-0.5 * ((z - z_peak) / sigma) ** 2)


# ── Proxy 2: dN/dz survey rate (same M8-C formula, M_min=1e14) ───────────────
def _sigma_m(m_min: float, z: float) -> float:
    """Approx σ(M, z) from M8-C approach."""
    g_z = (OM_M * (1 + z) ** 3) / (OM_M * (1 + z) ** 3 + OM_L)
    g0 = OM_M
    growth = (g_z / g0) ** 0.6
    sigma_ref = SIGMA_8 * (m_min / 1e14) ** (-GAMMA_CDM)
    return sigma_ref * growth


def proxy_dndz(z: float, m_min: float = 1.0e14) -> float:
    """
    Model B survey dN/dz ∝ n(z) × r(z)² / H(z)
    Same formula as m8c_closure_schedule.py Model B.
    """
    sigma = _sigma_m(m_min, z)
    nu = DELTA_C / max(sigma, 1e-10)
    # PS mass function ∝ ν exp(-ν²/2)
    ps = nu * math.exp(-0.5 * nu**2)
    h_z = H0 * math.sqrt(OM_M * (1 + z) ** 3 + OM_L)
    # Comoving distance (trapezoidal, rough)
    r_z = C_KMS / H0 * _comoving_integral(z)
    dndz = ps * (r_z**2) / h_z
    return max(dndz, 0.0)


def _comoving_integral(z_max: float, n_steps: int = 200) -> float:
    dz = z_max / n_steps
    total = 0.0
    for i in range(n_steps):
        zi = (i + 0.5) * dz
        hi = math.sqrt(OM_M * (1 + zi) ** 3 + OM_L)
        total += dz / hi
    return total


# ── Parametric LogNormal fit: k_A(z) = exp(-(ln(z+ε) - μ)²/(2σ²)) ────────────
def proxy_lognormal(z: float, mu: float, sigma_ln: float) -> float:
    """Log-normal k_A proxy: peaks at z_peak = exp(mu) - epsilon."""
    lnz = math.log(z + 0.01)  # shift to avoid log(0)
    return math.exp(-0.5 * ((lnz - mu) / sigma_ln) ** 2)


def fit_lognormal_grid(z_list: list[float], eps_list: list[float]) -> tuple[float, float, float]:
    """
    Grid search over (mu, sigma_ln) to maximize Pearson r with eps.
    Returns (best_mu, best_sigma_ln, best_r).
    """
    best_r = -2.0
    best_mu = 0.0
    best_sigma = 1.0
    for mu_100 in range(-50, 200):  # mu from -0.5 to 2.0
        mu = mu_100 / 100.0
        for sig_100 in range(20, 200):  # sigma from 0.20 to 2.0
            sig = sig_100 / 100.0
            proxy = [proxy_lognormal(zi, mu, sig) for zi in z_list]
            r = pearson_r(proxy, eps_list)
            if not math.isnan(r) and r > best_r:
                best_r = r
                best_mu = mu
                best_sigma = sig
    return best_mu, best_sigma, best_r


# ── LOO Analysis ──────────────────────────────────────────────────────────────
def loo_analysis(proxy_values: list[float], eps_values: list[float], z_values: list[float]) -> dict:
    """
    Leave-One-Out: for each i, remove point i, compute Pearson r.
    Returns delta_r[i] = r_full - r_loo[i] (positive = high-leverage).
    """
    r_full = pearson_r(proxy_values, eps_values)
    results = []
    for i in range(len(z_values)):
        proxy_loo = [v for j, v in enumerate(proxy_values) if j != i]
        eps_loo = [v for j, v in enumerate(eps_values) if j != i]
        r_loo = pearson_r(proxy_loo, eps_loo)
        delta_r = r_full - r_loo
        results.append(
            {
                "i": i,
                "z": z_values[i],
                "eps": eps_values[i],
                "r_loo": round(r_loo, 4),
                "delta_r": round(delta_r, 4),
                "leverage": "HIGH" if abs(delta_r) > 0.05 else "LOW",
            }
        )
    return {"r_full": round(r_full, 4), "loo_points": results}


# ── Bootstrap CI on z_peak ────────────────────────────────────────────────────
def bootstrap_z_peak(z_list: list[float], eps_list: list[float], n_bootstrap: int = 2000) -> dict:
    """
    Bootstrap 2000 resamplings (with replacement, same N=11).
    For each, fit LogNormal → extract z_peak = exp(mu) - 0.01.
    Return p5, p16, p50, p84, p95.
    """
    import random

    random.seed(42)
    z_peaks = []
    for _ in range(n_bootstrap):
        indices = [random.randint(0, len(z_list) - 1) for _ in range(len(z_list))]
        z_s = [z_list[i] for i in indices]
        e_s = [eps_list[i] for i in indices]
        mu, _, r = fit_lognormal_grid(z_s, e_s)
        if r > 0.3:  # only accept fits with reasonable correlation
            z_peak_i = math.exp(mu) - 0.01
            z_peaks.append(z_peak_i)

    if not z_peaks:
        return {"error": "no valid bootstrap fits"}

    z_peaks.sort()
    n = len(z_peaks)

    def pctile(p: float) -> float:
        idx = int(p / 100.0 * n)
        return round(z_peaks[min(idx, n - 1)], 3)

    return {
        "n_valid": n,
        "p5": pctile(5),
        "p16": pctile(16),
        "p50": pctile(50),
        "p84": pctile(84),
        "p95": pctile(95),
        "width_68ci": round(pctile(84) - pctile(16), 3),
    }


# ── Main ───────────────────────────────────────────────────────────────────────
def main() -> dict:
    # Build proxy value lists
    p0 = [proxy_virial(z) for z in Z]
    p1 = [proxy_gaussian(z) for z in Z]
    p2 = [proxy_dndz(z, 1e14) for z in Z]

    # Fit LogNormal on full dataset
    mu_best, sig_best, r_lognormal = fit_lognormal_grid(Z, EPS)
    z_peak_best = math.exp(mu_best) - 0.01
    p3 = [proxy_lognormal(z, mu_best, sig_best) for z in Z]

    # LOO for each proxy
    loo_p0 = loo_analysis(p0, EPS, Z)
    loo_p1 = loo_analysis(p1, EPS, Z)
    loo_p2 = loo_analysis(p2, EPS, Z)
    loo_p3 = loo_analysis(p3, EPS, Z)

    # Bootstrap CI on z_peak
    boot = bootstrap_z_peak(Z, EPS, n_bootstrap=2000)

    # Find high-leverage points per proxy
    def high_leverage(loo: dict) -> list[dict]:
        return [p for p in loo["loo_points"] if p["leverage"] == "HIGH"]

    # z=8.5 leverage check (index 10)
    z85_leverage = {
        "proxy_virial": loo_p0["loo_points"][10],
        "proxy_gaussian_040": loo_p1["loo_points"][10],
        "proxy_dndz_1e14": loo_p2["loo_points"][10],
        "proxy_lognormal_best": loo_p3["loo_points"][10],
    }

    # Skeptic verdict on z=8.5
    z85_deltas = [v["delta_r"] for v in z85_leverage.values()]
    z85_max_abs = max(abs(d) for d in z85_deltas)
    if z85_max_abs > 0.10:
        z85_verdict = "HIGH_LEVERAGE — z=8.5 is critical outlier affecting correlation"
    elif z85_max_abs > 0.05:
        z85_verdict = "MEDIUM_LEVERAGE — z=8.5 has moderate influence"
    else:
        z85_verdict = "LOW_LEVERAGE — z=8.5 does not dominate correlation"

    # U6 falsification check
    r_with_z85 = loo_p1["r_full"]
    r_without_z85 = loo_p1["loo_points"][10]["r_loo"]
    u6_jump = r_without_z85 - r_with_z85

    report = {
        "analysis": "LOO_EPSILON_LEVERAGE",
        "labels": [
            "INTERNAL_DIAGNOSTIC_ONLY",
            "NOT_VALIDATION",
            "TABLE_A1_ONLY",
            "OUR_RECONSTRUCTION",
            "NOT_AUTHOR_CONFIRMED",
        ],
        "N": N,
        "epsilon_profile": [{"z": round(z, 2), "eps": round(e, 4)} for z, e in zip(Z, EPS, strict=False)],
        "full_pearson_r": {
            "proxy_virial": round(loo_p0["r_full"], 4),
            "proxy_gaussian_040": round(loo_p1["r_full"], 4),
            "proxy_dndz_1e14": round(loo_p2["r_full"], 4),
            "proxy_lognormal_best": round(loo_p3["r_full"], 4),
        },
        "lognormal_best_fit": {
            "mu": round(mu_best, 3),
            "sigma_ln": round(sig_best, 3),
            "z_peak": round(z_peak_best, 3),
            "pearson_r": round(r_lognormal, 4),
        },
        "bootstrap_z_peak_ci": boot,
        "z85_leverage": {
            "raw": {k: round(v["delta_r"], 4) for k, v in z85_leverage.items()},
            "max_abs_delta_r": round(z85_max_abs, 4),
            "verdict": z85_verdict,
        },
        "u6_falsification": {
            "r_gaussian_with_z85": round(r_with_z85, 4),
            "r_gaussian_without_z85": round(r_without_z85, 4),
            "jump_if_removed": round(u6_jump, 4),
            "interpretation": (
                "z=8.5 HURTS gaussian correlation"
                if u6_jump > 0.03
                else "z=8.5 does NOT dominate gaussian correlation"
            ),
        },
        "loo_tables": {
            "proxy_virial": loo_p0["loo_points"],
            "proxy_gaussian_040": loo_p1["loo_points"],
            "proxy_dndz_1e14": loo_p2["loo_points"],
            "proxy_lognormal_best": loo_p3["loo_points"],
        },
        "high_leverage_points": {
            "proxy_virial": high_leverage(loo_p0),
            "proxy_gaussian_040": high_leverage(loo_p1),
            "proxy_dndz_1e14": high_leverage(loo_p2),
            "proxy_lognormal_best": high_leverage(loo_p3),
        },
    }

    return report


if __name__ == "__main__":
    result = main()
    out_path = Path(__file__).parent.parent / "reports" / "loo_epsilon_analysis.json"
    out_path.parent.mkdir(exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"Report written: {out_path}")

    # Console summary
    print("\n=== LOO Epsilon Analysis ===")
    print(f"N = {result['N']} points")
    print("\nFull Pearson r (all 11 points):")
    for k, v in result["full_pearson_r"].items():
        print(f"  {k}: {v:+.4f}")
    print("\nLogNormal best fit:")
    ln = result["lognormal_best_fit"]
    print(f"  z_peak = {ln['z_peak']:.3f}  (mu={ln['mu']}, sigma_ln={ln['sigma_ln']})")
    print(f"  Pearson r = {ln['pearson_r']:.4f}")
    print("\nBootstrap 68% CI on z_peak:")
    b = result["bootstrap_z_peak_ci"]
    if "error" not in b:
        print(f"  z_peak = [{b['p16']}, {b['p50']}, {b['p84']}]")
        print(f"  width_68CI = {b['width_68ci']:.3f}")
    print("\nz=8.5 leverage analysis (U6):")
    print(f"  Max |delta_r| = {result['z85_leverage']['max_abs_delta_r']:.4f}")
    print(f"  Verdict: {result['z85_leverage']['verdict']}")
    u6 = result["u6_falsification"]
    print("\nU6 falsification (Gaussian proxy):")
    print(f"  r WITH z=8.5:    {u6['r_gaussian_with_z85']:.4f}")
    print(f"  r WITHOUT z=8.5: {u6['r_gaussian_without_z85']:.4f}")
    print(f"  Jump:            {u6['jump_if_removed']:+.4f}")
    print(f"  → {u6['interpretation']}")

    print("\nHigh-leverage points (|delta_r| > 0.05):")
    for proxy_name, points in result["high_leverage_points"].items():
        if points:
            zs = [f"z={p['z']}" for p in points]
            print(f"  {proxy_name}: {', '.join(zs)}")
        else:
            print(f"  {proxy_name}: none")
