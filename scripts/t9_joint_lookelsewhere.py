"""T9 — Joint (family-wise) look-elsewhere correction across TJB's numerical relations.

Audit-hardening task (NOT a validation of TJB, NOT a claim of author error). The #1
referee attack on any numerical-coincidence program is the family-wise trials factor:
each relation looks impressive alone, but how many were examined, and how many survive a
multiple-comparisons correction?

This script:
  1. Enumerates every distinct claimed numerical relation (from facts.json R001-R006 plus
     a preprint scan: Eqs.21-24 fermion masses, inflaton m_Z/3).
  2. Records each relation's individual deviation and its individual p-value, distinguishing
        - p_trials   : a look-elsewhere p that ALREADY includes a within-family trials factor
                       (exists ONLY for Eq.32, p~6e-5 over 83160 formulas -- OWNED BY TASK T1,
                        consumed here as an input, not recomputed);
        - p_raw      : a single-hypothesis p with NO trials factor (e.g. fsigma8 correlation);
        - None       : trials-corrected look-elsewhere p was NEVER computed -> [UNKNOWN].
  3. Applies Bonferroni (valid under ARBITRARY dependence) and Benjamini-Hochberg FDR
     (q=0.05; plus Benjamini-Yekutieli for the dependent case) over a range of plausible
     family sizes m.
  4. Reports the SURVIVING CORE and states the independence caveat honestly -- it does NOT
     fabricate a single precise joint p, because (a) most p's are [UNKNOWN] and (b) the
     particle-sector relations share PDG masses (dependence), so a naive product over-counts.

Reproducible, stdlib-only. Run:  python scripts/t9_joint_lookelsewhere.py
"""

from __future__ import annotations

import math
from dataclasses import dataclass


def norm_sf_twosided(sigma: float) -> float:
    """Two-sided tail probability for a |z|=sigma Gaussian deviation.

    For an AGREEMENT expressed in sigma this is a goodness-of-fit / consistency p
    (large sigma => discrepant), NOT an evidence-for-the-relation p. Reported for
    context only; never fed into the FDR ladder.
    """
    return math.erfc(abs(sigma) / math.sqrt(2.0))


@dataclass
class Relation:
    rid: str
    label: str
    deviation: str
    p_trials: float | None  # look-elsewhere p WITH within-family trials factor
    p_raw: float | None  # single-hypothesis p, NO trials factor
    marker: str
    note: str

    @property
    def p_for_ladder(self) -> float | None:
        """The p actually usable on a multiple-comparisons ladder.

        Prefer the trials-corrected p; fall back to the raw single-hypothesis p;
        None if neither exists (the relation's look-elsewhere p is UNKNOWN).
        """
        if self.p_trials is not None:
            return self.p_trials
        return self.p_raw


# --- Family enumeration ------------------------------------------------------
# Deviations/p's transcribed from memory facts.json (R001-R006) + preprint scan.
# Anti-cherry-pick: where a relation carries BOTH a favourable and an unfavourable
# component (Eq.31: m_W/m_H good, m_Z 5.5sigma bad), the LEAST favourable is noted.
RELATIONS: list[Relation] = [
    Relation(
        rid="R001",
        label="Eq.32  (4/3)(m_tau/m_e)^12 = alpha_EM/alpha_G",
        deviation="0.061% (1.0 sigma)",
        p_trials=6.0e-5,  # INPUT from task T1 (83160-formula rank #1). Do NOT recompute here.
        p_raw=None,
        marker="[VERIFIED-INPUT: T1]",
        note="ONLY relation with a real trials-corrected look-elsewhere p.",
    ),
    Relation(
        rid="R002",
        label="Eq.31  boson m_W^2:m_Z^2:m_H^2 = 7:9:17",
        deviation="m_W/m_H 0.04% (0.4 sigma); BUT m_Z 5.5 sigma tension",
        p_trials=None,
        p_raw=None,
        marker="[MIXED / no trials factor]",
        note="Least-favourable component m_Z=5.5sigma is a FAILURE. No look-elsewhere p computed.",
    ),
    Relation(
        rid="R00x-fermion",
        label="Eqs.21-24  fermion mass relations (muon, quarks)",
        deviation="muon 0.47%, quarks <0.31% (sigma not established)",
        p_trials=None,
        p_raw=None,
        marker="[UNKNOWN]",
        note="Percent deviations only; no trials-corrected p; shares lepton masses with Eq.32.",
    ),
    Relation(
        rid="R003",
        label="IDM N_opt = Omega_cdm/Omega_b = 5.364 vs DESI 5.31+-0.13",
        deviation="0.46 sigma (consistency)",
        p_trials=None,
        p_raw=None,
        marker="[UNKNOWN / pre-registered postulate]",
        note="N=5 postulated before DESI DR1 -> look-elsewhere partly N/A; consistency not a discovery p.",
    ),
    Relation(
        rid="R004",
        label="f*sigma8 bell-shape correlation r(eps,f*sig8)=0.851",
        deviation="r=0.851, n=10",
        p_trials=None,
        p_raw=0.0018,  # correlation p, single hypothesis, NO trials factor for proxy choice
        marker="[VERIFIED-inline / RAW p, no trials factor]",
        note="Raw p; does not account for how many proxy correlations were tried -> optimistic.",
    ),
    Relation(
        rid="R006",
        label="H-FLRW power law H(z)=54.07(1+z)^0.884",
        deviation="MAE 5.04 (a FIT, not a sharp coincidence)",
        p_trials=None,
        p_raw=None,
        marker="[FIT — not a coincidence claim]",
        note="Fitted 2-parameter curve; not a trials-factor hypothesis. Excluded from ladder.",
    ),
    Relation(
        rid="R-inflaton",
        label="Inflaton rest energy = m_Z/3 = 30.4 GeV",
        deviation="undetected particle; refs [188-190] hint incompatibility",
        p_trials=None,
        p_raw=None,
        marker="[UNTESTED / undetected]",
        note="No measured endpoint -> no p at all.",
    ),
    # R005 (Delta N_eff 130-477 sigma) and R011 (MULTING dipole) are ACTIVE FAILURES /
    # NULLs, not claimed coincidences -> not part of the 'surviving coincidence' family,
    # but noted in the report: TJB reporting misses REDUCES the pure-cherry-pick concern.
]


def bonferroni(p_min: float, m: int) -> float:
    """Family-wise error bound for the single most significant p (valid under any dependence)."""
    return min(1.0, p_min * m)


def harmonic(m: int) -> float:
    return sum(1.0 / i for i in range(1, m + 1))


def bh_survivors(pvals: list[float], q: float, m: int, dependent: bool) -> list[bool]:
    """Benjamini-Hochberg (dependent=False) or Benjamini-Yekutieli (dependent=True).

    pvals: the p-values that EXIST (subset of the family). m: TOTAL family size
    (>= len(pvals)); unknown-p members still inflate m, making the test conservative.
    Returns survival flags aligned to sorted(pvals).
    """
    c = harmonic(m) if dependent else 1.0
    order = sorted(range(len(pvals)), key=lambda i: pvals[i])
    survive = [False] * len(pvals)
    max_k = -1
    for rank, idx in enumerate(order, start=1):
        threshold = (rank / (m * c)) * q
        if pvals[idx] <= threshold:
            max_k = rank
    for rank, idx in enumerate(order, start=1):
        if rank <= max_k:
            survive[idx] = True
    return survive


def main() -> None:
    q = 0.05
    print("=" * 78)
    print("T9 — JOINT LOOK-ELSEWHERE (family-wise trials factor) across TJB relations")
    print("=" * 78)

    print("\n[1] FAMILY ENUMERATION")
    print("-" * 78)
    header = f"{'id':<14}{'deviation':<44}{'p (ladder)':<14}marker"
    print(header)
    print("-" * 78)
    for r in RELATIONS:
        p = r.p_for_ladder
        pstr = "UNKNOWN" if p is None else f"{p:.2e}"
        print(f"{r.rid:<14}{r.deviation[:43]:<44}{pstr:<14}{r.marker}")
        print(f"{'':<14}{r.label}")

    ladder_ps = [r.p_for_ladder for r in RELATIONS if r.p_for_ladder is not None]
    ladder_ids = [r.rid for r in RELATIONS if r.p_for_ladder is not None]
    n_known = len(ladder_ps)
    n_total_named = len(RELATIONS)
    p_min = min(ladder_ps)

    print("\n[2] HONEST P-INVENTORY")
    print("-" * 78)
    print(f"  named relations in family              : {n_total_named}")
    print(f"  relations with ANY usable p            : {n_known}  ({', '.join(ladder_ids)})")
    print("  relations with trials-corrected p      : 1  (Eq.32 only)")
    print(f"  relations with p = [UNKNOWN]           : {n_total_named - n_known}")
    print(f"  most significant p in family (p_min)   : {p_min:.2e}  (Eq.32)")

    print("\n[3] BONFERRONI (valid under arbitrary dependence)")
    print("-" * 78)
    print("  Corrected significance of the single best relation (Eq.32) vs family size m:")
    print(f"  {'m (family size)':<22}{'Bonferroni p = m*p_min':<26}survives 0.05?")
    for m in (n_known, n_total_named, 10, 20, 100, 800, 83160):
        bp = bonferroni(p_min, m)
        verdict = "YES" if bp < 0.05 else "NO (saturates/double-counts)"
        tag = ""
        if m == n_total_named:
            tag = "  <- named family"
        if m == 83160:
            tag = "  <- entire formula scan (DOUBLE-COUNTS Eq.32's own trials factor)"
        print(f"  m={m:<20}{bp:<26.3e}{verdict}{tag}")

    print("\n[4] BENJAMINI-HOCHBERG / -YEKUTIELI FDR (q=0.05)")
    print("-" * 78)
    print(f"  Ladder uses the {n_known} relations with a usable p; m = TOTAL family size")
    print("  (UNKNOWN-p members still inflate m, so the test is conservative).")
    for m in (n_total_named, 10, 20, 100):
        bh = bh_survivors(ladder_ps, q, m, dependent=False)
        by = bh_survivors(ladder_ps, q, m, dependent=True)
        order = sorted(range(len(ladder_ps)), key=lambda i: ladder_ps[i])
        bh_s = {ladder_ids[i] for i in order if bh[i]}
        by_s = {ladder_ids[i] for i in order if by[i]}
        print(f"  m={m:<4}  BH survivors : {sorted(bh_s) or 'none'}")
        print(f"  {'':<6}  BY survivors : {sorted(by_s) or 'none'}  (dependent-safe)")

    print("\n[5] INDEPENDENCE CAVEAT (why no single precise joint p is quoted)")
    print("-" * 78)
    print("  Eq.32, Eqs.21-24 SHARE lepton masses (m_tau, m_e) -> NOT independent.")
    print("  Eq.31 uses boson masses (indep. of leptons, same PDG methodology).")
    print("  N_opt, f*sigma8 use cosmological data (indep. of the particle sector).")
    print("  => a naive product-of-p over the particle relations OVER-COUNTS.")
    print("  => Bonferroni holds regardless; for FDR use BY (dependent) not BH.")
    print("  => most p's are [UNKNOWN]; a complete joint p would be FABRICATED. Not quoted.")

    print("\n[6] VERDICT — surviving core")
    print("-" * 78)
    print("  SURVIVES family-wise correction : Eq.32 (R001)")
    print("    - Bonferroni p < 0.05 for any named family up to ~800 relations;")
    print("    - passes BH AND BY at q=0.05 for m up to ~100.")
    print("  MARGINAL                        : f*sigma8 (R004)")
    print("    - passes BH/BY only for small m (<=~20-30); raw p, no proxy trials factor;")
    print("    - washes out for m>=100. Treat as suggestive, not established.")
    print("  UNQUANTIFIED (neither survive nor refuted here): Eq.31 favourable part,")
    print("    Eqs.21-24, N_opt, inflaton -> trials-corrected p = [UNKNOWN]; consistency")
    print("    checks, not trials-corrected detections.")
    print("  ACTIVE FAILURES within TJB's own relations: m_Z (5.5 sigma), Delta N_eff")
    print("    (130-477 sigma). That misses ARE reported slightly lowers the pure")
    print("    cherry-pick concern, but they must not be laundered into the 'core'.")


if __name__ == "__main__":
    main()
