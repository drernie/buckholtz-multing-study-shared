"""
M8-D: Minimal Assumption Virial Schedule (MAVS).

Constructs D_C:AB(z), k_A(z), r_A(z), r_P(z) from first principles:
  - Virial theorem + overdensity criterion for k_A and r_vir
  - Press-Schechter for mean cluster separation r_A = n^(-1/3)
  - Physical-to-comoving conversion for r_P = r_A / (1+z)
  - Minimal assumption: D_C:AB = r_A (mean separation)

Physical scaling relation used:
  sigma_v^2 = G * M / r_vir  (virial theorem self-similar limit;
  consistent with Evrard et al. 2008 M-sigma_v observed scaling)

No FLRW H(z) fitting as input.
No arbitrary power-law fit to Table A1.

Compares normalized MAVS schedule shapes to eps(z) from Table A1.

Labels:
  M8_D_MAVS | OUR_RECONSTRUCTION | CONDITIONAL_RECONSTRUCTION
  NOT_AUTHOR_CONFIRMED | NOT_VALIDATION | NOT_REFUTATION
  AUTHOR_SCHEDULE_NEEDED
"""

from __future__ import annotations

import json
import math
from pathlib import Path

# ── Constants ─────────────────────────────────────────────────────────────────

H0_KMS_MPC: float = 70.0
OM_MATTER: float = 0.315
OM_LAMBDA: float = 0.685
SIGMA_8: float = 0.811
DELTA_C: float = 1.686
GAMMA_CDM: float = 0.27

G_SI: float = 6.674e-11  # m^3 kg^-1 s^-2
M_PER_MPC: float = 3.086e22  # m per Mpc
KG_PER_MSUN: float = 1.989e30  # kg per M_sun

# G in (km/s)^2 Mpc M_sun^-1  [standard cosmological units]
# G_SI [m^3 kg^-1 s^-2] * KG_PER_MSUN / (M_PER_MPC * (1e3)^2)
G_COSMO: float = G_SI * KG_PER_MSUN / (M_PER_MPC * 1.0e6)  # ~4.302e-9

DELTA_VIR: float = 200.0  # overdensity criterion for virial radius

# Table A1 data [TRANSCRIBED from Table A1, arithmetic verified per M8-A-R1 PASS]
# OUR_RECONSTRUCTION — NOT_AUTHOR_CONFIRMED — NOT observational data
_TABLE_A1_RAW: list[tuple[float, float, float]] = [
    (0.06, 68.1, 70.2),
    (0.14, 69.3, 73.5),
    (0.25, 71.5, 78.8),
    (0.40, 75.0, 83.1),
    (0.65, 83.0, 91.4),
    (1.00, 95.7, 104.2),
    (1.50, 114.8, 126.5),
    (2.10, 140.3, 151.8),
    (3.20, 187.6, 197.3),
    (5.00, 265.2, 271.5),
    (8.50, 398.5, 418.1),
]

Z_DATA: list[float] = [r[0] for r in _TABLE_A1_RAW]
H_FLRW: list[float] = [r[1] for r in _TABLE_A1_RAW]
H_MULT: list[float] = [r[2] for r in _TABLE_A1_RAW]

M_MIN_VARIANTS: list[tuple[float, str]] = [
    (1.0e14, "1e14 Msun — group/cluster boundary"),
    (5.0e14, "5e14 Msun — rich cluster"),
    (2.0e15, "2e15 Msun — massive cluster"),
]

# ── LAMBDA-CDM background ─────────────────────────────────────────────────────


def hubble_lcdm(z: float) -> float:
    """H(z) in km/s/Mpc for flat LCDM."""
    return H0_KMS_MPC * math.sqrt(OM_MATTER * (1.0 + z) ** 3 + OM_LAMBDA)


def rho_crit_cosmo(z: float) -> float:
    """Critical density rho_crit(z) in M_sun/Mpc^3.

    rho_crit = 3 H^2 / (8 pi G)
    """
    hz = hubble_lcdm(z)
    return 3.0 * hz**2 / (8.0 * math.pi * G_COSMO)


def growth_factor_unnorm(z: float, z_max: float = 30.0, n_steps: int = 400) -> float:
    """D(z) unnormalized via trapezoidal integral: D = H(z) * INT_z^z_max (1+z')/H(z')^3 dz'."""
    dz = (z_max - z) / n_steps
    s = 0.0
    for i in range(n_steps):
        zp = z + (i + 0.5) * dz
        hp = hubble_lcdm(zp)
        s += (1.0 + zp) / hp**3 * dz
    return hubble_lcdm(z) * s


_D0_CACHE: float | None = None


def _get_d0() -> float:
    global _D0_CACHE
    if _D0_CACHE is None:
        _D0_CACHE = growth_factor_unnorm(0.0)
    return _D0_CACHE


def growth_factor_norm(z: float) -> float:
    """D(z)/D(0) — normalized linear growth factor."""
    return growth_factor_unnorm(z) / _get_d0()


# ── Press-Schechter ───────────────────────────────────────────────────────────

_M8_CACHE: float | None = None


def compute_m8() -> float:
    """M_8: mass in sphere of radius 8 Mpc/h for LCDM params."""
    global _M8_CACHE
    if _M8_CACHE is not None:
        return _M8_CACHE
    rho_m0 = OM_MATTER * rho_crit_cosmo(0.0)
    h = H0_KMS_MPC / 100.0
    r8_mpc = 8.0 / h
    _M8_CACHE = (4.0 / 3.0) * math.pi * r8_mpc**3 * rho_m0
    return _M8_CACHE


def sigma_mass_z(m_min_solar: float, z: float) -> float:
    """sigma(M_min, z) = sigma_8 * (M_8/M_min)^gamma * D(z)/D(0)."""
    m8 = compute_m8()
    sigma_z0 = SIGMA_8 * (m8 / m_min_solar) ** GAMMA_CDM
    return sigma_z0 * growth_factor_norm(z)


def ps_comoving_fraction(m_min_solar: float, z: float) -> float:
    """Press-Schechter complementary error function: f(>M_min, z)."""
    nu = DELTA_C / sigma_mass_z(m_min_solar, z)
    return math.erfc(nu / math.sqrt(2.0))


def n_comoving_mpc3(m_min_solar: float, z: float) -> float:
    """Comoving number density of halos >M_min in Mpc^-3."""
    rho_m0 = OM_MATTER * rho_crit_cosmo(0.0)
    return (rho_m0 / m_min_solar) * ps_comoving_fraction(m_min_solar, z)


# ── MAVS schedule functions ───────────────────────────────────────────────────


def r_vir_mpc(m_min_solar: float, z: float) -> float:
    """Virial radius [Mpc] from overdensity criterion.

    M = (4pi/3) * Delta_vir * rho_crit(z) * r_vir^3
    => r_vir = [ 3M / (4pi * Delta_vir * rho_crit) ]^(1/3)
    """
    rho_c = rho_crit_cosmo(z)
    return (3.0 * m_min_solar / (4.0 * math.pi * DELTA_VIR * rho_c)) ** (1.0 / 3.0)


def k_A_virial(m_min_solar: float, z: float) -> float:
    """Virial energy scale [(km/s)^2/Mpc]: k_A = G*M / r_vir^2.

    Virial theorem: 2K + U = 0 => sigma_v^2 = G*M/r_vir.
    k_A = sigma_v^2 / r_vir = G*M / r_vir^2.

    Physical meaning: characteristic kinetic energy per unit volume of cluster A.
    Consistent with self-similar Evrard (2008) M-sigma scaling in the limit
    sigma_v ~ (G*M/r_vir)^(1/2).

    Scaling: k_A propto H(z)^(4/3) — monotonically increasing with z.
    """
    r = r_vir_mpc(m_min_solar, z)
    return G_COSMO * m_min_solar / r**2


def r_A_comoving_mpc(m_min_solar: float, z: float) -> float:
    """Mean comoving cluster separation [Mpc]: r_A = n^(-1/3).

    Monotonically increasing with z (fewer clusters at earlier times).
    Diverges as n -> 0 at very high z; capped at 1e12 Mpc (>> Hubble horizon).
    """
    n = n_comoving_mpc3(m_min_solar, z)
    if n < 1.0e-50:
        return 1.0e12
    return n ** (-1.0 / 3.0)


def r_P_physical_mpc(m_min_solar: float, z: float) -> float:
    """Mean physical (proper) cluster separation [Mpc]: r_P = r_A / (1+z).

    Competes with (1+z) factor; may have extremum at intermediate z.
    """
    return r_A_comoving_mpc(m_min_solar, z) / (1.0 + z)


def D_C_AB_mpc(m_min_solar: float, z: float) -> float:
    """Cluster-pair comoving distance [Mpc].

    Minimal assumption: D_C:AB = r_A (mean separation between clusters).
    WHY: no author-confirmed D_C:AB schedule available (Q2 blocker).
    """
    return r_A_comoving_mpc(m_min_solar, z)


# ── eps(z) from Table A1 ──────────────────────────────────────────────────────


def compute_eps() -> list[float]:
    """eps(z) = (H_MULT/H_FLRW)^2 - 1.

    [TRANSCRIBED from Table A1, arithmetic verified per M8-A-R1 PASS]
    OUR_RECONSTRUCTION — NOT observational data — NOT_AUTHOR_CONFIRMED
    """
    return [(hm / hf) ** 2 - 1.0 for hf, hm in zip(H_FLRW, H_MULT, strict=False)]


# ── Statistics ────────────────────────────────────────────────────────────────


def pearson_r(x: list[float], y: list[float]) -> float:
    """Pearson correlation coefficient."""
    n = len(x)
    mx = sum(x) / n
    my = sum(y) / n
    num = sum((xi - mx) * (yi - my) for xi, yi in zip(x, y, strict=False))
    denom = math.sqrt(sum((xi - mx) ** 2 for xi in x) * sum((yi - my) ** 2 for yi in y))
    return num / denom if denom > 1.0e-14 else 0.0


def normalize_to_max(vals: list[float]) -> list[float]:
    """Normalize so that max absolute value = 1."""
    m = max(abs(v) for v in vals)
    return [v / m for v in vals] if m > 0.0 else list(vals)


def is_monotone_increasing(vals: list[float]) -> bool:
    """Return True if vals is non-decreasing."""
    return all(vals[i + 1] >= vals[i] for i in range(len(vals) - 1))


# ── Main audit ────────────────────────────────────────────────────────────────


def run_m8d_mavs_schedule() -> dict:
    """Compute MAVS schedule at all Table A1 z-values and compare to eps(z).

    Returns verdict dict and writes reports/m8d_mavs_schedule.json.
    """
    eps = compute_eps()
    eps_norm = normalize_to_max(eps)

    best_positive_r: float = -2.0
    results_by_m_min = []

    for m_min, label in M_MIN_VARIANTS:
        k_A_vals = [k_A_virial(m_min, z) for z in Z_DATA]
        r_A_vals = [r_A_comoving_mpc(m_min, z) for z in Z_DATA]
        r_P_vals = [r_P_physical_mpc(m_min, z) for z in Z_DATA]
        d_C_vals = [D_C_AB_mpc(m_min, z) for z in Z_DATA]

        k_A_norm = normalize_to_max(k_A_vals)
        r_A_norm = normalize_to_max(r_A_vals)
        r_P_norm = normalize_to_max(r_P_vals)
        d_C_norm = normalize_to_max(d_C_vals)

        r_k_A = pearson_r(eps_norm, k_A_norm)
        r_r_A = pearson_r(eps_norm, r_A_norm)
        r_r_P = pearson_r(eps_norm, r_P_norm)
        r_d_C = pearson_r(eps_norm, d_C_norm)

        best_pos_this = max(r_k_A, r_r_A, r_r_P, r_d_C)
        if best_pos_this > best_positive_r:
            best_positive_r = best_pos_this

        def _peak_z(vals: list[float]) -> float:
            return Z_DATA[vals.index(max(vals))]

        results_by_m_min.append(
            {
                "m_min_solar": m_min,
                "m_min_label": label,
                "sigma_z0": round(sigma_mass_z(m_min, 0.0), 4),
                "r_vir_z0_mpc": round(r_vir_mpc(m_min, 0.0), 3),
                "r_A_z0_mpc": round(r_A_vals[0], 1),
                "r_P_z0_mpc": round(r_P_vals[0], 1),
                "k_A_z0": float(f"{k_A_vals[0]:.4e}"),
                "monotone_k_A": is_monotone_increasing(k_A_vals),
                "monotone_r_A": is_monotone_increasing(r_A_vals),
                "pearson_r": {
                    "k_A_vs_eps": round(r_k_A, 4),
                    "r_A_vs_eps": round(r_r_A, 4),
                    "r_P_vs_eps": round(r_r_P, 4),
                    "D_C_AB_vs_eps": round(r_d_C, 4),
                },
                "peak_z": {
                    "k_A": _peak_z(k_A_vals),
                    "r_A": _peak_z(r_A_vals),
                    "r_P": _peak_z(r_P_vals),
                    "D_C_AB": _peak_z(d_C_vals),
                    "eps": _peak_z(eps),
                },
                "best_positive_r_this_m_min": round(best_pos_this, 4),
            }
        )

    # Verdict thresholds match M8-C for consistency
    if best_positive_r >= 0.85:
        overall_verdict = "PASS"
    elif best_positive_r >= 0.65:
        overall_verdict = "PARTIAL"
    elif best_positive_r > -2.0:
        overall_verdict = "FAIL"
    else:
        overall_verdict = "BLOCKED"

    # --- Q2 diagnosis ---
    q2_diagnosis = (
        "k_A(z) from virial theorem scales as H(z)^(4/3) — monotone. "
        "r_A(z) scales as n(z)^(-1/3) — monotone. "
        "r_P(z) = r_A/(1+z) may have extremum but is dominated by high-z divergence. "
        "None of the MAVS components reproduces the non-monotonic eps(z) structure. "
        "Q2 blocker confirmed: author-specific k_A(z) / D_eff(z) schedule essential."
    )

    conclusions = [
        "k_A(z) propto H(z)^(4/3) — monotonically increasing with z by virial theorem + overdensity criterion.",
        "r_A(z) = n^(-1/3) — monotonically increasing with z (fewer clusters at higher z).",
        "r_P(z) = r_A/(1+z) — shape depends on competition between cluster depletion and (1+z) factor.",
        "D_C:AB = r_A (minimal assumption) — monotone by construction.",
        f"Best positive Pearson r across all MAVS components and M_min variants: {best_positive_r:.3f}.",
        f"Overall verdict: {overall_verdict}.",
        "Secondary eps structure at z=1.0-1.5 NOT reproduced by any individual MAVS component.",
        "Uptick at z=8.5 NOT reproduced.",
        "AUTHOR_SCHEDULE_NEEDED: virial+PS MAVS is CONDITIONAL RECONSTRUCTION — not the author's method.",
        "<HYPOTHESIS>: k_A from virial theorem connects cluster kinetic energy to H_MULT scale — unconfirmed without bridge formula (Q1).",
        q2_diagnosis,
    ]

    result = {
        "gate": "M8-D-MAVS-schedule",
        "date": "2026-06-12",
        "labels": [
            "M8_D_MAVS",
            "OUR_RECONSTRUCTION",
            "CONDITIONAL_RECONSTRUCTION",
            "NOT_AUTHOR_CONFIRMED",
            "NOT_VALIDATION",
            "NOT_REFUTATION",
            "AUTHOR_SCHEDULE_NEEDED",
            "<HYPOTHESIS>",
        ],
        "physics_sources": {
            "k_A": "virial theorem: 2K+U=0 => k_A = G*M/r_vir^2",
            "r_vir": "overdensity criterion: M = (4pi/3)*Delta_vir*rho_crit(z)*r_vir^3, Delta_vir=200",
            "r_A": "Press-Schechter: r_A = n(>M_min,z)^(-1/3)",
            "r_P": "r_P = r_A / (1+z)",
            "D_C_AB": "minimal assumption: D_C:AB = r_A (mean separation)",
            "cluster_scaling": "sigma_v = sqrt(G*M/r_vir) [virial self-similar limit; cf. Evrard 2008]",
            "no_H_fitting": True,
            "no_TableA1_powerlaw_fit": True,
        },
        "m8_solar": compute_m8(),
        "eps_peak_z": 0.40,
        "eps_min_z": 5.00,
        "results_by_m_min": results_by_m_min,
        "overall_verdict": overall_verdict,
        "best_positive_pearson_r": round(best_positive_r, 4),
        "conclusions": conclusions,
        "safety": (
            "M8_D_MAVS · OUR_RECONSTRUCTION · CONDITIONAL_RECONSTRUCTION "
            "· NOT_AUTHOR_CONFIRMED · NOT_VALIDATION · NOT_REFUTATION "
            "· AUTHOR_SCHEDULE_NEEDED"
        ),
    }

    out_path = Path(__file__).parent.parent / "reports" / "m8d_mavs_schedule.json"
    out_path.parent.mkdir(exist_ok=True)
    out_path.write_text(json.dumps(result, indent=2), encoding="utf-8")

    return result


if __name__ == "__main__":
    result = run_m8d_mavs_schedule()
    print(f"Gate:    {result['gate']}")
    print(f"Verdict: {result['overall_verdict']}")
    print(f"Best r:  {result['best_positive_pearson_r']}")
    print(f"Safety:  {result['safety']}")
