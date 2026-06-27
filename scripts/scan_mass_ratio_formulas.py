"""
Look-Elsewhere Audit for Eq.32: (4/3)(m_tau/m_e)^12 = alpha_EM / alpha_G

Scans ALL formulas of the form (p/q)(m_i/m_j)^n for:
  p, q in 1..P_MAX (rational prefactor numerator/denominator)
  n in 1..N_MAX  (integer exponent)
  i, j in particle mass pairs (i != j)

Target: alpha_EM / alpha_G(m_e)

Output: top hits, rank of Eq.32, empirical p-value.
"""

import itertools
import json
import math
from pathlib import Path

# ── PDG 2022/2024 constants ───────────────────────────────────────────────────
# Masses in MeV
MASSES = {
    "e": 0.51099895,  # electron
    "mu": 105.6583755,  # muon
    "tau": 1776.86,  # tau
    "u": 2.16,  # up quark (MS-bar 2 GeV)
    "d": 4.67,  # down quark
    "s": 93.4,  # strange quark
    "c": 1270.0,  # charm quark
    "b": 4180.0,  # bottom quark
    "t": 172760.0,  # top quark
    "p": 938.27208816,  # proton
    "n": 939.56542052,  # neutron
}

# Fine-structure constant
ALPHA_EM = 1.0 / 137.035999084

# Gravitational coupling at electron mass scale
# alpha_G = G * m_e^2 / (hbar * c)
G_SI = 6.67430e-11  # N m^2 kg^-2
M_E_KG = 9.1093837015e-31  # kg
HBAR = 1.054571817e-34  # J s
C_SI = 2.99792458e8  # m/s

ALPHA_G = G_SI * M_E_KG**2 / (HBAR * C_SI)

TARGET = ALPHA_EM / ALPHA_G  # ~4.166e42
LOG_TARGET = math.log(TARGET)

# ── Scan parameters ──────────────────────────────────────────────────────────
P_MAX = 10  # max numerator/denominator of rational prefactor
N_MAX = 24  # max exponent
REL_ERR_REPORT = 0.05  # report hits within 5%

# ── Eq.32 reference ─────────────────────────────────────────────────────────
# (4/3)(m_tau/m_e)^12 = alpha_EM/alpha_G
EQ32_PREFACTOR = (4, 3)
EQ32_PAIR = ("tau", "e")
EQ32_N = 12


def log_formula(p: int, q: int, m_hi: float, m_lo: float, n: int) -> float:
    """Compute log((p/q) * (m_hi/m_lo)^n) safely. m_hi > m_lo assumed."""
    return math.log(p) - math.log(q) + n * (math.log(m_hi) - math.log(m_lo))


def relative_error(log_val: float, log_tgt: float) -> float:
    return abs(math.exp(log_val - log_tgt) - 1.0)


def scan():
    hits = []
    n_trials = 0

    mass_names = list(MASSES.keys())
    mass_vals = MASSES

    # All ordered pairs (i, j) with i != j, take ratio m_i/m_j > 1
    pairs = []
    for a, b in itertools.permutations(mass_names, 2):
        if mass_vals[a] > mass_vals[b]:
            pairs.append((a, b))

    # Prefactors p/q with gcd=1, p,q in 1..P_MAX
    prefactors = []
    for p in range(1, P_MAX + 1):
        for q in range(1, P_MAX + 1):
            if math.gcd(p, q) == 1:
                prefactors.append((p, q))

    for p, q in prefactors:
        for a, b in pairs:
            m_hi = mass_vals[a]
            m_lo = mass_vals[b]
            for n in range(1, N_MAX + 1):
                n_trials += 1
                try:
                    log_val = log_formula(p, q, m_hi, m_lo, n)
                except (ValueError, ZeroDivisionError):
                    continue
                err = relative_error(log_val, LOG_TARGET)
                if err < REL_ERR_REPORT:
                    is_eq32 = (
                        p == EQ32_PREFACTOR[0]
                        and q == EQ32_PREFACTOR[1]
                        and a == EQ32_PAIR[0]
                        and b == EQ32_PAIR[1]
                        and n == EQ32_N
                    )
                    hits.append(
                        {
                            "p": p,
                            "q": q,
                            "hi": a,
                            "lo": b,
                            "n": n,
                            "rel_err": err,
                            "pct_err": err * 100,
                            "is_eq32": is_eq32,
                        }
                    )

    hits.sort(key=lambda h: h["rel_err"])
    return hits, n_trials


def main():
    print(f"Target: alpha_EM/alpha_G = {TARGET:.6e}")
    print(f"alpha_G(m_e) = {ALPHA_G:.6e}")
    print(f"Scanning (p/q)(m_i/m_j)^n for p,q≤{P_MAX}, n≤{N_MAX} ...")
    print()

    hits, n_trials = scan()

    # ── Eq.32 rank ───────────────────────────────────────────────────────────
    eq32_rank = None
    eq32_err = None
    for i, h in enumerate(hits):
        if h["is_eq32"]:
            eq32_rank = i + 1
            eq32_err = h["rel_err"]
            break

    if eq32_rank is None:
        # Eq.32 didn't appear even in 5% window — compute manually
        log_eq32 = log_formula(4, 3, MASSES["tau"], MASSES["e"], 12)
        eq32_err = relative_error(log_eq32, LOG_TARGET)
        eq32_rank = "outside top hits"

    # ── Empirical p-value ────────────────────────────────────────────────────
    n_hits_1pct = sum(1 for h in hits if h["rel_err"] < 0.01)
    n_hits_01pct = sum(1 for h in hits if h["rel_err"] < 0.001)
    n_hits_014pct = sum(1 for h in hits if h["rel_err"] < 0.00014)  # Eq.32 threshold

    p_empirical = n_hits_1pct / n_trials

    # ── Print results ─────────────────────────────────────────────────────────
    print(f"Total trials:              {n_trials:,}")
    print(f"Hits within 5%:            {len(hits):,}")
    print(f"Hits within 1%:            {n_hits_1pct:,}")
    print(f"Hits within 0.1%:          {n_hits_01pct:,}")
    print(f"Hits within 0.014% (Eq32): {n_hits_014pct:,}")
    print(f"Empirical p (within 1%):   {p_empirical:.4f}")
    print()
    print(f"Eq.32 rank:   #{eq32_rank}")
    print(f"Eq.32 error:  {eq32_err * 100:.4f}%")
    print()
    print("Top-20 hits:")
    print(f"{'#':>3}  {'Formula':40}  {'Error%':>8}  {'Eq32?':>6}")
    print("-" * 65)
    for i, h in enumerate(hits[:20]):
        formula = f"({h['p']}/{h['q']})(m_{h['hi']}/m_{h['lo']})^{h['n']}"
        tag = "★ EQ32" if h["is_eq32"] else ""
        print(f"{i + 1:>3}  {formula:40}  {h['pct_err']:>7.4f}%  {tag}")

    # ── Save JSON ─────────────────────────────────────────────────────────────
    out = {
        "target": TARGET,
        "alpha_G": ALPHA_G,
        "alpha_EM": ALPHA_EM,
        "n_trials": n_trials,
        "n_hits_5pct": len(hits),
        "n_hits_1pct": n_hits_1pct,
        "n_hits_01pct": n_hits_01pct,
        "n_hits_014pct": n_hits_014pct,
        "p_empirical_1pct": p_empirical,
        "eq32_rank": eq32_rank,
        "eq32_rel_err": eq32_err,
        "top50": hits[:50],
    }
    out_path = (
        Path(__file__).parent.parent
        / "experiments"
        / "20260627-f4-eq32-synthesis"
        / "look_elsewhere_result.json"
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2))
    print(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()
