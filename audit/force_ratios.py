"""
Force Ratios — Dipole Dominance Audit

FORMULAE: from Claude Supplementary, lines 1311-1326
  F_d / F_m = 2 * (k_A/c²) * β_d * r_A / (m_A * D)
  r_crossover = 2 * (k_A/c²) * β_d * r_A / (m_A)    [where F_d = F_m]

VERIFIED: Formula matches Supplementary line 1318-1319 numerics (≈3.1e-3 at D=50 Mpc).

SCOPE: Cluster-pair model at z=0. Not a cosmological expansion model.
"""

from dataclasses import dataclass


@dataclass
class ClusterParams:
    k_A_over_c2: float  # M_sun, kinetic energy / c²
    m_A: float  # M_sun, cluster mass
    r_A: float  # Mpc, cluster radius
    D: float  # Mpc, inter-cluster separation


# Verified values from Claude Supplementary, lines 1316-1317
Z0_PARAMS = ClusterParams(
    k_A_over_c2=3.16e12,
    m_A=3.16e14,
    r_A=1.7,
    D=50.0,
)


def fd_over_fm(beta_d: float, p: ClusterParams) -> float:
    """F_d / F_m = 2 * k_A * β_d * r_A / (m_A * D)"""
    return 2.0 * p.k_A_over_c2 * beta_d * p.r_A / (p.m_A * p.D)


def r_crossover_mpc(beta_d: float, p: ClusterParams) -> float:
    """r where F_d = F_m: r_cross = 2 * k_A * β_d * r_A / m_A"""
    return 2.0 * p.k_A_over_c2 * beta_d * p.r_A / p.m_A


def beta_d_critical(p: ClusterParams) -> float:
    """β_d needed for F_d/F_m = 1 at separation D"""
    return p.m_A * p.D / (2.0 * p.k_A_over_c2 * p.r_A)


# Three AI services from Supplementary
AI_BETA_VALUES = {
    "ChatGPT": {"beta_d": 0.78, "beta_q": 0.19, "source_lines": "670-675"},
    "Claude Sonnet 4.6": {"beta_d": 4.50, "beta_q": 18.00, "source_lines": "1221-1223"},
    "Gemini Thinking": {"beta_d": 4.25, "beta_q": 8.10, "source_lines": "1526-1527"},
}


def run_dipole_dominance_audit() -> dict:
    p = Z0_PARAMS
    beta_crit = beta_d_critical(p)
    results = {}

    for name, vals in AI_BETA_VALUES.items():
        bd = vals["beta_d"]
        ratio = fd_over_fm(bd, p)
        r_cross = r_crossover_mpc(bd, p)
        results[name] = {
            "beta_d": bd,
            "beta_q": vals["beta_q"],
            "Fd_over_Fm_at_50Mpc": ratio,
            "r_crossover_Mpc": r_cross,
            "dominates_at_50Mpc": ratio > 1.0,
            "r_cross_vs_r_cluster": r_cross / p.r_A,
        }

    results["_beta_d_critical"] = beta_crit
    results["_cluster_radius_Mpc"] = p.r_A
    results["_separation_Mpc"] = p.D
    return results


if __name__ == "__main__":
    r = run_dipole_dominance_audit()
    beta_crit = r.pop("_beta_d_critical")
    r_cluster = r.pop("_cluster_radius_Mpc")
    D_sep = r.pop("_separation_Mpc")

    print("=== DIPOLE DOMINANCE AUDIT ===")
    print(f"Inter-cluster separation D = {D_sep} Mpc | Cluster radius r_A = {r_cluster} Mpc")
    print(f"β_d_critical for F_d/F_m=1 at {D_sep} Mpc: {beta_crit:.0f}")
    print()
    print(
        f"{'AI Service':<22} {'β_d':>6} {'β_q':>6} {'F_d/F_m@50Mpc':>14} "
        f"{'r_cross(Mpc)':>13} {'r_cross/r_cluster':>18} {'Dominates?':>11}"
    )
    print("-" * 95)
    for name, v in r.items():
        dom = "YES" if v["dominates_at_50Mpc"] else "no"
        print(
            f"{name:<22} {v['beta_d']:>6.2f} {v['beta_q']:>6.2f} "
            f"{v['Fd_over_Fm_at_50Mpc']:>14.5f} "
            f"{v['r_crossover_Mpc']:>13.4f} "
            f"{v['r_cross_vs_r_cluster']:>18.4f} {dom:>11}"
        )
    print()
    print(f"β_d_current (Claude) = 4.5 → need {beta_crit / 4.5:.0f}× more for F_d/F_m=1 at 50 Mpc")
    print("r_crossover < r_cluster for all AI services → dipole sub-cluster only")
