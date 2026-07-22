"""T1 — Eq.32 second-prediction test + look-elsewhere v2.

Audit question (NOT a validation of TJB's theory): is
    (4/3) (m_tau/m_e)^12 = alpha_EM / alpha_G(m_e)
more like a physical structure (which would generate a SECOND independent,
falsifiable relation) or a single-label numerical coincidence (which would
not, and which competitors would eat once the search space is broadened)?

Three prongs, all printed to stdout:

  PRONG 1 — second-prediction search.
    Treat Eq.32 as one instance of the template
        C * (m_hi/m_lo)^n = alpha_EM / alpha_G(m_lo)          (self-consistent
    reference: the SAME lighter mass appears in the ratio denominator and in
    alpha_G, which is what puts both sides in "electron units" for Eq.32).
    The coefficient C is DICTATED, not fitted: we only allow the two SU(3)
    Casimirs named in the discriminator, C_F = 4/3 and C_A = 3, applied to the
    muon and the other lepton pairs. For each dictated (C, pair) we scan only
    the integer exponent n and report the BEST it can do. If even the best
    integer n misses by >> 0.1%, that companion is a NULL. A genuine second
    prediction would be a sub-0.1% hit at an integer n we did not fit.
    (Prong 1b "blind prediction" collapses into this: Eq.32 uses only
    {m_tau, m_e, alpha_EM, G}; the sole quantity it could independently predict
    is a companion lepton relation, i.e. exactly these muon templates.)

  PRONG 2 — look-elsewhere v2 (broadened).
    Reuse the family of scan_mass_ratio_formulas.py, then broaden it three
    ways and re-rank Eq.32:
      (a) rational coeffs p/q<=20 (was 10), exponent n<=30 (was 24);
      (b) additionally allow sqrt(p/q) coefficient forms (a second family);
      (c) a physically-honest restriction: SIMPLE coeffs only (p,q<=4) — a
          real theory produces small Casimir-like numbers, not 17/13, so this
          is the discriminating robustness check, not the free-for-all.

  PRONG 3 — verdict is written by the human in the report; this script only
    prints the numbers the verdict rests on.

No numerology-chaining: every target here is alpha_EM/alpha_G(m_ref) built from
measured masses + measured G/alpha_EM alone. We never chain Eq.32 with another
fitted formula.

Run:  python scripts/t1_eq32_second_prediction.py
Reproducible, prints only. Writes no repo artifacts.
"""

from __future__ import annotations

import math

# ── constants (identical to scan_mass_ratio_formulas.py / scan_reference_mass_
#    robustness.py; PDG 2024, verified in facts.json R001 _pdg_correction) ──
MASSES = {  # MeV
    "e": 0.51099895,
    "mu": 105.6583755,
    "tau": 1776.93,
    "u": 2.16,
    "d": 4.67,
    "s": 93.4,
    "c": 1270.0,
    "b": 4180.0,
    "t": 172570.0,
    "p": 938.27208816,
    "n": 939.56542052,
}
ALPHA_EM = 1.0 / 137.035999084
G_SI = 6.67430e-11
M_E_KG = 9.1093837015e-31
HBAR = 1.054571817e-34
C_SI = 2.99792458e8
ALPHA_G_E = G_SI * M_E_KG**2 / (HBAR * C_SI)  # alpha_G(m_e)
TARGET_E = ALPHA_EM / ALPHA_G_E  # ~4.166e42


def alpha_g_of(m_ref_mev: float) -> float:
    """alpha_G(m_ref) = G m_ref^2/(hbar c), scaled from the electron value."""
    return ALPHA_G_E * (m_ref_mev / MASSES["e"]) ** 2


def target_for_ref(m_ref_mev: float) -> float:
    """alpha_EM / alpha_G(m_ref) for a self-consistent reference mass."""
    return ALPHA_EM / alpha_g_of(m_ref_mev)


def best_integer_exponent(coeff: float, ratio: float, target: float, n_max: int = 40):
    """Best integer n minimizing |coeff*ratio^n/target - 1|; return (n, val, relerr)."""
    best = None
    for n in range(1, n_max + 1):
        val = coeff * ratio**n
        relerr = abs(val / target - 1.0)
        if best is None or relerr < best[2]:
            best = (n, val, relerr)
    return best


# ────────────────────────────────────────────────────────────────────────────
def prong0_confirm_eq32() -> None:
    print("=" * 74)
    print("PRONG 0 — re-verify Eq.32 itself (self-check)")
    print("=" * 74)
    val = (4 / 3) * (MASSES["tau"] / MASSES["e"]) ** 12
    relerr = abs(val / TARGET_E - 1.0)
    print(f"  alpha_G(m_e)            = {ALPHA_G_E:.6e}")
    print(f"  target alpha_EM/alpha_G = {TARGET_E:.6e}")
    print(f"  (4/3)(m_tau/m_e)^12     = {val:.6e}")
    print(f"  Eq.32 deviation         = {relerr * 100:.4f}%   [VERIFIED-BASH]")
    print()


def prong1_second_prediction() -> None:
    print("=" * 74)
    print("PRONG 1 — second-prediction test (dictated Casimir, scan only n)")
    print("=" * 74)
    print("  Template: C * (m_hi/m_lo)^n = alpha_EM/alpha_G(m_lo)")
    print("  C is NOT fitted: only C_F=4/3 and C_A=3 (the two named SU(3) Casimirs).")
    print("  For each, the BEST integer exponent is reported. Sub-0.1% = a real")
    print("  second prediction; large miss = NULL for that companion.\n")

    # self-consistent lepton companions (ref = lighter lepton in the ratio)
    lepton_pairs = [("tau", "e"), ("mu", "e"), ("tau", "mu")]
    casimirs = [("C_F=4/3", 4 / 3), ("C_A=3", 3.0)]

    print(
        f"  {'pair':10} {'coeff':8} {'ref':4} {'best n':>6} "
        f"{'coeff*ratio^n':>14} {'target':>13} {'dev %':>10}  verdict"
    )
    print("  " + "-" * 84)
    rows = []
    for hi, lo in lepton_pairs:
        ratio = MASSES[hi] / MASSES[lo]
        target = target_for_ref(MASSES[lo])
        for cname, cval in casimirs:
            n, val, relerr = best_integer_exponent(cval, ratio, target)
            verdict = "HIT <0.1%" if relerr < 1e-3 else "NULL"
            rows.append((hi, lo, cname, cval, n, val, target, relerr, verdict))
            print(
                f"  m_{hi}/m_{lo:6} {cname:8} {lo:4} {n:>6} "
                f"{val:>14.4e} {target:>13.4e} {relerr * 100:>9.2f}%  {verdict}"
            )

    print()
    hits = [
        r
        for r in rows
        if r[7] < 1e-3 and not (r[0] == "tau" and r[1] == "e" and r[2].startswith("C_F"))
    ]
    # note: the (tau,e,C_F=4/3) row IS Eq.32 itself — exclude from "second" hits
    print(f"  Second-prediction HITS (<0.1%, excluding Eq.32 itself): {len(hits)}")
    print("  => a coincidence yields 0 here; a structure yields >=1.\n")


def _coprime_rationals(pmax: int) -> list[tuple[int, int]]:
    return [(p, q) for p in range(1, pmax + 1) for q in range(1, pmax + 1) if math.gcd(p, q) == 1]


def _pairs():
    names = list(MASSES)
    return [(a, b) for a in names for b in names if MASSES[a] > MASSES[b]]


def _rank_eq32(coeff_forms, pmax: int, nmax: int, label: str) -> None:
    """coeff_forms: list of (value, printable) coefficient candidates."""
    pairs = _pairs()
    log_target = math.log(TARGET_E)
    eq32_err = None
    n_at_least = 0
    total = 0
    for cval, _ in coeff_forms:
        log_c = math.log(cval)
        for a, b in pairs:
            log_ratio = math.log(MASSES[a]) - math.log(MASSES[b])
            for n in range(1, nmax + 1):
                total += 1
                relerr = abs(math.exp(log_c + n * log_ratio - log_target) - 1.0)
                is_eq32 = abs(cval - 4 / 3) < 1e-12 and a == "tau" and b == "e" and n == 12
                if is_eq32:
                    eq32_err = relerr
    # second pass now that we know eq32_err (single pass would need storage; cheap enough)
    for cval, _ in coeff_forms:
        log_c = math.log(cval)
        for a, b in pairs:
            log_ratio = math.log(MASSES[a]) - math.log(MASSES[b])
            for n in range(1, nmax + 1):
                relerr = abs(math.exp(log_c + n * log_ratio - log_target) - 1.0)
                if relerr <= eq32_err + 1e-18:
                    n_at_least += 1
    rank = n_at_least  # number of candidates at least as good (incl. Eq.32) = its rank
    p_emp = n_at_least / total
    print(f"  [{label}]")
    print(f"    coeff forms: {len(coeff_forms)}   pairs: {len(pairs)}   n<=... : {nmax}")
    print(f"    total trials       = {total:,}")
    print(f"    Eq.32 deviation    = {eq32_err * 100:.4f}%")
    print(f"    Eq.32 rank         = #{rank}   (candidates <= Eq.32 error)")
    print(f"    empirical p        = {p_emp:.2e}")
    print()


def prong2_look_elsewhere_v2() -> None:
    print("=" * 74)
    print("PRONG 2 — look-elsewhere v2 (broadened search space)")
    print("=" * 74)
    print("  Rank = how many candidates in the pool hit the SAME target at least")
    print("  as precisely as Eq.32 (so rank #1 = uniquely best).\n")

    # (a) baseline reproduction: p,q<=10, n<=24
    base = [(p / q, f"{p}/{q}") for p, q in _coprime_rationals(10)]
    _rank_eq32(base, 10, 24, "baseline: rationals p,q<=10, n<=24 (reproduce 83,160)")

    # (b) broaden rationals: p,q<=20, n<=30
    broad = [(p / q, f"{p}/{q}") for p, q in _coprime_rationals(20)]
    _rank_eq32(broad, 20, 30, "broadened: rationals p,q<=20, n<=30")

    # (c) add sqrt(p/q) coefficient family on top of the broadened rationals
    sqrt_forms = [(math.sqrt(p / q), f"sqrt({p}/{q})") for p, q in _coprime_rationals(20)]
    broad_plus_sqrt = broad + sqrt_forms
    _rank_eq32(broad_plus_sqrt, 20, 30, "broadened + sqrt(p/q) coeff family, n<=30")

    # (d) physically-honest restriction: SIMPLE coeffs only, p,q<=4, n<=24
    simple = [(p / q, f"{p}/{q}") for p, q in _coprime_rationals(4)]
    _rank_eq32(simple, 4, 24, "SIMPLE coeffs only p,q<=4, n<=24 (theory-plausible)")


def main() -> None:
    prong0_confirm_eq32()
    prong1_second_prediction()
    prong2_look_elsewhere_v2()
    print("Numbers above feed the verdict in boyko_T1_eq32_second_prediction.md")


if __name__ == "__main__":
    main()
