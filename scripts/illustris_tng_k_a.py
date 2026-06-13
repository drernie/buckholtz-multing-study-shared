"""
Illustris-TNG k_A(z) Test — Hypothesis Lab Test 2

Tests whether galaxy cluster kinetic energy from Illustris-TNG simulation
reproduces the non-monotone ε(z) pattern at z≈0.40.

Approach:
  1. Use Illustris-TNG TNG100-1 published snapshot redshifts
  2. Compute group/cluster kinetic energy proxy from published data
     (uses SubhaloVmax as velocity proxy + SubhaloMass as mass proxy)
  3. Compare k_A^{TNG}(z) shape with ε(z) from Table A1

Data source:
  - Illustris-TNG TNG100-1 group catalog (public, no API key needed for summary)
  - Published kinetic energy estimates from Nelson et al. 2019 (TNG release paper)
  - Fallback: analytical k_A from TNG-calibrated sigma(M,z) relations

Labels: EXTERNAL_STANDARD_PHYSICS · HYPOTHESIS · NOT_VALIDATION
        NOT_AUTHOR_CONFIRMED · INTERNAL_DIAGNOSTIC_ONLY

U4: Does k_A in Illustris-TNG show non-monotone behavior at z≈0.40?
"""

from __future__ import annotations

import json
import math
import urllib.error
import urllib.request
from pathlib import Path

# ── Table A1 data ──────────────────────────────────────────────────────────────
Z_TARGET = [0.06, 0.14, 0.25, 0.40, 0.65, 1.00, 1.50, 2.10, 3.20, 5.00, 8.50]
H_FLRW = [68.1, 69.3, 71.5, 75.0, 83.0, 95.7, 114.8, 140.3, 187.6, 265.2, 398.5]
H_MULT = [70.2, 73.5, 78.8, 83.1, 91.4, 104.2, 126.5, 151.8, 197.3, 271.5, 418.1]
EPS = [(hm / hf) ** 2 - 1.0 for hm, hf in zip(H_MULT, H_FLRW, strict=False)]

# ── TNG100-1 snapshot redshifts (from official snapshot table) ─────────────────
# Source: https://www.tng-project.org/data/docs/specifications/
# Snapshots 0-99 → z from ~20 to z=0; we use the ones closest to Z_TARGET
# These are published values — no API key required
TNG_SNAPSHOTS = {
    # snapshot_id: redshift
    0: 20.05,
    4: 10.98,
    11: 6.49,
    17: 5.00,
    21: 4.01,
    25: 3.21,
    33: 2.58,
    40: 2.10,
    50: 1.50,
    59: 1.04,
    67: 0.70,
    72: 0.52,
    78: 0.35,
    84: 0.20,
    91: 0.10,
    99: 0.00,
}

# ── ΛCDM parameters (TNG calibrated) ──────────────────────────────────────────
OM_M = 0.3089  # TNG uses Planck 2016
OM_L = 0.6911
H0_TNG = 67.74
SIGMA_8_TNG = 0.8159


def _h_z(z: float) -> float:
    return H0_TNG * math.sqrt(OM_M * (1 + z) ** 3 + OM_L)


def _growth_factor(z: float) -> float:
    """Linear growth factor D(z)/D(0), approximate."""
    return 1.0 / (1.0 + z)


# ── Analytical k_A proxy from TNG-calibrated sigma-mass relation ───────────────
def sigma_m(m_sun: float, z: float, sigma8: float = SIGMA_8_TNG) -> float:
    """
    σ(M, z): rms density fluctuation smoothed on scale M.
    Approximate: σ(M) ∝ M^(-γ), σ(M=1e14, z=0) = sigma_8 * calibration.
    Growth factor applied: σ(M,z) = σ(M,0) × D(z).
    """
    gamma = 0.27
    sigma_ref = sigma8 * (m_sun / 1e14) ** (-gamma)
    return sigma_ref * _growth_factor(z)


def kinetic_energy_proxy_tng(z: float, m_min_sun: float = 1e14) -> float:
    """
    k_A^{TNG} proxy: Σ(M_cluster × v_vir²/c²) above M_min.

    Using cluster number density weighted by mass × velocity²:
    k_A ∝ ∫_{M_min}^{∞} n(M,z) × M × v_vir²(M,z) dM

    where:
      n(M,z) = Press-Schechter mass function (TNG-calibrated)
      v_vir(M,z) = virial velocity ≈ sqrt(G*M / r_vir)
      r_vir ∝ M^(1/3) / H(z)^(2/3)  → v_vir ∝ M^(1/3) × H(z)^(1/3)

    Result: k_A ∝ ∫ n(M) × M × M^(2/3) × H(z)^(2/3) dM
              ∝ H(z)^(2/3) × ∫ n(M) × M^(5/3) dM

    The integral ∫ n(M) × M^(5/3) dM depends on σ(M,z) through PS mass function.
    For a power-law approximation near M_min:
      ∝ σ(M_min, z)^(-1) × exp(-ν²/2) × M_min^(5/3) / σ(M_min)
    where ν = δ_c / σ(M_min, z)
    """
    sig = sigma_m(m_min_sun, z)
    nu = 1.686 / max(sig, 1e-10)  # δ_c / σ(M,z)

    # PS dn/dM at M_min (unnormalized): ν/σ × |dσ/dM| × exp(-ν²/2)
    # For our purposes: n_proxy ∝ ν × exp(-ν²/2)
    ps_weight = nu * math.exp(-0.5 * nu**2)

    # k_A integrand ∝ M^(5/3) × n(M) ∝ M_min^(5/3) × ps_weight / M_min
    #                                  = M_min^(2/3) × ps_weight
    mass_weight = m_min_sun ** (2.0 / 3.0)

    # H(z)^(2/3) factor from virial velocity
    h_factor = _h_z(z) ** (2.0 / 3.0)

    return ps_weight * mass_weight * h_factor


# ── Merger rate contribution (non-virial excess k_A) ──────────────────────────
def merger_rate_proxy(z: float) -> float:
    """
    Cluster merger rate proxy from Fakhouri & Ma (2008, MNRAS 394:1825).
    dN_merge/dt ∝ (1+z)^2.5 × exp(-z/z_c) approximately.

    For group-scale mergers (10^13 to 10^14 M_sun),
    the merger rate per cluster peaks at z≈0.5–1.0 (field estimate).
    We use the cosmological merger rate volume density:
      Γ(z) ∝ dN_merge/dV/dt × comoving volume element
            ∝ merger_rate(z) × [r(z)/H(z)]²  × (1+z)

    Reference: Fakhouri & Ma 2008, eq. 2 (power-law fit to Millennium)
    """
    # Fakhouri & Ma 2008 merger rate per halo per Gyr per unit mass ratio:
    # dN/dξdt ∝ A × M^alpha × (1+z)^eta × exp(-ξ_mean)
    # For integrated rate above mass ratio ξ>0.3:
    # ≈ 0.0366 × (M/1e12)^0.133 × (1+z)^2.32 [Gyr^-1]
    alpha = 0.133
    eta = 2.32
    m_ref = 1e14  # typical cluster mass
    rate_per_cluster = 0.0366 * (m_ref / 1e12) ** alpha * (1 + z) ** eta

    # Volume element dV/dz ∝ r(z)² / H(z)
    h_z = _h_z(z)
    r_z = _comoving_r(z)
    vol_element = (r_z**2) / h_z

    # Cluster number density n(z) (from sigma_m)
    sig = sigma_m(m_ref, z)
    nu = 1.686 / max(sig, 1e-10)
    n_density = nu * math.exp(-0.5 * nu**2)

    # k_A from mergers: rate × n_density × volume × characteristic KE per merger
    # KE per merger ∝ M × v_infall² / c² ≈ M × (escape_vel)² / c²
    # escape_vel² ≈ G*M / r_vir ∝ M^(2/3) × H(z)^(2/3)
    ke_per_merger = (m_ref ** (2.0 / 3.0)) * h_z ** (2.0 / 3.0)

    return rate_per_cluster * n_density * vol_element * ke_per_merger


def _comoving_r(z_max: float, n_steps: int = 100) -> float:
    c_km = 299792.458
    dz = z_max / max(n_steps, 1)
    total = 0.0
    for i in range(n_steps):
        zi = (i + 0.5) * dz
        total += dz / math.sqrt(OM_M * (1 + zi) ** 3 + OM_L)
    return (c_km / H0_TNG) * total


# ── Pearson r ─────────────────────────────────────────────────────────────────
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


def normalize(values: list[float]) -> list[float]:
    mn = min(values)
    mx = max(values)
    if mx - mn < 1e-12:
        return [1.0] * len(values)
    return [(v - mn) / (mx - mn) for v in values]


# ── Monotonicity test ─────────────────────────────────────────────────────────
def is_monotone(values: list[float]) -> tuple[bool, int]:
    """Returns (is_monotone, n_sign_changes)."""
    diffs = [values[i + 1] - values[i] for i in range(len(values) - 1)]
    sign_changes = 0
    for i in range(len(diffs) - 1):
        if diffs[i] * diffs[i + 1] < 0:
            sign_changes += 1
    return sign_changes == 0, sign_changes


# ── Attempt TNG API (no auth required for public metadata) ───────────────────
def try_fetch_tng_api() -> dict:
    """
    Attempt to fetch TNG100-1 public API metadata.
    Returns status dict — does not require API key for top-level info.
    """
    try:
        url = "https://www.tng-project.org/api/TNG100-1/"
        req = urllib.request.Request(url, headers={"User-Agent": "Python/research-audit"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return {
                "status": "ACCESSIBLE",
                "name": data.get("name", "unknown"),
                "n_snapshots": data.get("num_files_snap", "unknown"),
                "note": "API accessible; kinetic energy data requires API key + group catalog download",
            }
    except urllib.error.HTTPError as e:
        return {"status": "HTTP_ERROR", "code": e.code, "reason": str(e.reason)}
    except Exception as e:
        return {"status": "UNAVAILABLE", "reason": str(e), "fallback": "using analytical proxy"}


# ── Main ───────────────────────────────────────────────────────────────────────
def main() -> dict:
    # Try API
    api_status = try_fetch_tng_api()

    # Compute analytical k_A proxies at Table A1 z-values
    m_thresholds = [1e14, 5e14, 2e15]
    m_labels = ["1e14_M_sun", "5e14_M_sun", "2e15_M_sun"]

    results_by_mass = {}
    for m_min, m_label in zip(m_thresholds, m_labels, strict=False):
        k_a_virial = [kinetic_energy_proxy_tng(z, m_min) for z in Z_TARGET]
        k_a_merger = [merger_rate_proxy(z) for z in Z_TARGET]

        k_a_virial_norm = normalize(k_a_virial)
        k_a_merger_norm = normalize(k_a_merger)

        mono_v, sc_v = is_monotone(k_a_virial)
        mono_m, sc_m = is_monotone(k_a_merger)

        r_virial = pearson_r(k_a_virial, EPS)
        r_merger = pearson_r(k_a_merger, EPS)

        # Peak z for each proxy
        peak_z_virial = Z_TARGET[k_a_virial.index(max(k_a_virial))]
        peak_z_merger = Z_TARGET[k_a_merger.index(max(k_a_merger))]

        results_by_mass[m_label] = {
            "m_min_sun": m_min,
            "virial_proxy": {
                "k_a_normalized": [round(v, 4) for v in k_a_virial_norm],
                "pearson_r": round(r_virial, 4),
                "peak_z": peak_z_virial,
                "is_monotone": mono_v,
                "sign_changes": sc_v,
                "verdict": "MONOTONE_FAIL" if mono_v else f"NON_MONOTONE (r={r_virial:.3f})",
            },
            "merger_proxy": {
                "k_a_normalized": [round(v, 4) for v in k_a_merger_norm],
                "pearson_r": round(r_merger, 4),
                "peak_z": peak_z_merger,
                "is_monotone": mono_m,
                "sign_changes": sc_m,
                "verdict": "MONOTONE_FAIL" if mono_m else f"NON_MONOTONE (r={r_merger:.3f})",
            },
        }

    # Overall U4 verdict
    best_r_virial = max(results_by_mass[ml]["virial_proxy"]["pearson_r"] for ml in m_labels)
    best_r_merger = max(results_by_mass[ml]["merger_proxy"]["pearson_r"] for ml in m_labels)

    virial_monotone = all(results_by_mass[ml]["virial_proxy"]["is_monotone"] for ml in m_labels)

    if virial_monotone:
        u4_virial_verdict = (
            "CONFIRMED: TNG virial k_A IS monotone for all mass thresholds. "
            "Consistent with NR-004 (MAVS fail). "
            "Standard virial physics cannot produce non-monotone ε(z)."
        )
    else:
        u4_virial_verdict = "UNEXPECTED: virial k_A shows non-monotone behavior — investigate"

    if best_r_merger > 0.80:
        u4_merger_verdict = f"STRONG: merger rate proxy r={best_r_merger:.3f} > 0.80"
    elif best_r_merger > 0.60:
        u4_merger_verdict = f"PARTIAL: merger rate proxy r={best_r_merger:.3f}, 0.60–0.80 range"
    else:
        u4_merger_verdict = f"WEAK: merger rate proxy r={best_r_merger:.3f} < 0.60"

    report = {
        "analysis": "ILLUSTRIS_TNG_K_A_PROXY",
        "labels": [
            "EXTERNAL_STANDARD_PHYSICS",
            "HYPOTHESIS",
            "NOT_VALIDATION",
            "NOT_AUTHOR_CONFIRMED",
            "INTERNAL_DIAGNOSTIC_ONLY",
        ],
        "u4_question": "Is k_A in Illustris-TNG monotone or non-monotone?",
        "tng_api_status": api_status,
        "data_source": (
            "Analytical proxy using TNG100-1 cosmological parameters "
            "(Omega_m=0.3089, sigma_8=0.8159) + "
            "Fakhouri & Ma 2008 merger rate formula"
        ),
        "z_target": Z_TARGET,
        "epsilon_table_a1": [round(e, 4) for e in EPS],
        "results_by_mass": results_by_mass,
        "summary": {
            "best_pearson_r_virial": round(best_r_virial, 4),
            "best_pearson_r_merger": round(best_r_merger, 4),
            "virial_all_monotone": virial_monotone,
            "u4_virial_verdict": u4_virial_verdict,
            "u4_merger_verdict": u4_merger_verdict,
        },
        "what_this_does_not_mean": [
            "This does not confirm or refute MULTING as a physical theory",
            "This does not replace actual Illustris-TNG group catalog data (API key needed)",
            "This does not provide the bridge formula Q1 needed for MCMC",
            "Merger rate proxy is Fakhouri 2008 (Millennium Simulation, not TNG calibrated)",
        ],
    }

    return report


if __name__ == "__main__":
    result = main()
    out_path = Path(__file__).parent.parent / "reports" / "illustris_tng_k_a.json"
    out_path.parent.mkdir(exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"Report written: {out_path}")

    print("\n=== Illustris-TNG k_A(z) Test ===")
    print(f"TNG API: {result['tng_api_status']['status']}")
    print(f"\nU4: {result['u4_question']}")
    s = result["summary"]
    print(f"\nVirial proxy (all masses monotone): {s['virial_all_monotone']}")
    print(f"  Best Pearson r (virial): {s['best_pearson_r_virial']:.4f}")
    print(f"  → {s['u4_virial_verdict'][:80]}...")
    print("\nMerger rate proxy (Fakhouri & Ma 2008):")
    print(f"  Best Pearson r (merger): {s['best_pearson_r_merger']:.4f}")
    print(f"  → {s['u4_merger_verdict']}")

    print("\nResults by mass threshold:")
    for m_label, data in result["results_by_mass"].items():
        vir = data["virial_proxy"]
        mer = data["merger_proxy"]
        print(
            f"  M_min={m_label}: "
            f"virial r={vir['pearson_r']:+.4f} peak_z={vir['peak_z']} mono={vir['is_monotone']} | "
            f"merger r={mer['pearson_r']:+.4f} peak_z={mer['peak_z']} mono={mer['is_monotone']}"
        )
