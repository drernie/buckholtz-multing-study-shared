"""t3_boson_ratio_lookelsewhere.py — Is m_W^2:m_Z^2:m_H^2 = 7:9:17 special, and is the
Z-tension a known EW radiative correction? (docs/132 task T3; R002)

Two independent questions, no fitting:
  (A) LOOK-ELSEWHERE: over all coprime integer triples (a<b<c) up to a cap, how many fit the
      two independent measured squared-mass ratios (m_Z^2/m_W^2, m_H^2/m_W^2) at least as well
      as 7:9:17 does? Where does 7:9:17 rank by chi^2? Honest trials factor.
  (B) Z-TENSION: 7:9:17 implies tree-level sin^2(theta_W) = 1 - m_W^2/m_Z^2 = 1 - 7/9 = 2/9.
      Is the gap to the measured value a known electroweak radiative correction
      (on-shell vs effective sin^2, the rho parameter)?

Labels: NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · honest trials factor.
Evidence: [VERIFIED-BASH] arithmetic on PDG 2024 masses.
"""

from __future__ import annotations

from math import gcd

# PDG 2024 boson masses (GeV) — values consistent with facts.json R001/_pdg2026_check
mW, sW = 80.3692, 0.0133
mZ, sZ = 91.1880, 0.0020
mH, sH = 125.20, 0.11


def ratio_sigma(num_m, num_s, den_m, den_s):
    """R=(num/den)^2 with relative-error propagation. Returns (R, sigma_R)."""
    R = (num_m / den_m) ** 2
    rel = 2.0 * ((num_s / num_m) ** 2 + (den_s / den_m) ** 2) ** 0.5
    return R, R * rel


def main() -> None:
    print("=" * 74)
    print("T3 — 7:9:17 boson mass-ratio: real pattern or coincidence?")
    print("NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION")
    print("=" * 74)
    print(f"\nPDG 2024: m_W={mW}+-{sW}  m_Z={mZ}+-{sZ}  m_H={mH}+-{sH} GeV")

    # Two independent measured observables (ratios to m_W^2)
    R1, sR1 = ratio_sigma(mZ, sZ, mW, sW)  # m_Z^2/m_W^2, predicted 9/7
    R2, sR2 = ratio_sigma(mH, sH, mW, sW)  # m_H^2/m_W^2, predicted 17/7
    print(f"\nMeasured  m_Z^2/m_W^2 = {R1:.5f} +- {sR1:.5f}   (7:9:17 predicts 9/7={9 / 7:.5f})")
    print(f"Measured  m_H^2/m_W^2 = {R2:.5f} +- {sR2:.5f}   (7:9:17 predicts 17/7={17 / 7:.5f})")
    z_Z = (9 / 7 - R1) / sR1
    z_H = (17 / 7 - R2) / sR2
    chi2_797 = z_Z**2 + z_H**2
    print(f"  Z deviation: {z_Z:+.2f} sigma    H deviation: {z_H:+.2f} sigma")
    print(f"  chi^2(7:9:17) = {chi2_797:.2f}")

    # ── (A) Look-elsewhere over coprime integer triples ───────────────────────
    print("\n" + "-" * 74)
    print("(A) LOOK-ELSEWHERE over coprime integer triples a<b<c")
    for cap in (20, 30, 50):
        triples = []
        for a in range(1, cap):
            for b in range(a + 1, cap + 1):
                for c in range(b + 1, cap + 1):
                    if gcd(gcd(a, b), c) != 1:
                        continue
                    z1 = (b / a - R1) / sR1
                    z2 = (c / a - R2) / sR2
                    triples.append((z1**2 + z2**2, (a, b, c)))
        triples.sort()
        n_total = len(triples)
        rank = 1 + [t[1] for t in triples].index((7, 9, 17))
        better = sum(1 for chi2, _ in triples if chi2 <= chi2_797)
        print(f"\n  cap c<= {cap}: {n_total} coprime triples")
        print(
            f"    7:9:17 chi^2={chi2_797:.2f}, rank {rank}/{n_total}"
            f"  ({better} triples fit as well or better)"
        )
        print("    top 5 by chi^2:")
        for chi2, t in triples[:5]:
            print(f"      {t[0]:>2}:{t[1]:>2}:{t[2]:>2}  chi^2={chi2:.2f}")

    # ── (B) Z-tension vs electroweak sin^2(theta_W) ───────────────────────────
    print("\n" + "-" * 74)
    print("(B) Z-TENSION as electroweak mixing angle")
    s2_pred = 1.0 - 7.0 / 9.0  # 7:9:17 tree-level -> sin^2 = 2/9
    s2_onshell = 1.0 - (mW / mZ) ** 2  # on-shell definition (Sirlin)
    s2_eff = 0.23122  # PDG effective leptonic sin^2(theta_W_eff)
    s2_MSbar = 0.23129  # PDG MS-bar sin^2(theta_W)(m_Z)
    print(f"\n  7:9:17 tree-level  sin^2 = 2/9        = {s2_pred:.5f}")
    print(f"  On-shell (1-mW^2/mZ^2)               = {s2_onshell:.5f}")
    print(f"  PDG effective leptonic sin^2_eff     = {s2_eff:.5f}")
    print(f"  PDG MS-bar sin^2(mZ)                 = {s2_MSbar:.5f}")
    print(
        f"\n  gap 2/9 vs on-shell   = {s2_pred - s2_onshell:+.5f}"
        f"  ({(s2_pred - s2_onshell) / s2_onshell * 100:+.2f}%)"
    )
    print(
        f"  gap 2/9 vs effective  = {s2_pred - s2_eff:+.5f}"
        f"  ({(s2_pred - s2_eff) / s2_eff * 100:+.2f}%)"
    )
    # rho parameter view: rho = mW^2/(mZ^2 cos^2 theta_eff)
    rho_from_797 = (7.0 / 9.0) / (1.0 - s2_eff)  # cos^2 tree(7/9) / cos^2 eff
    print("\n  If cos^2(tree)=7/9 but cos^2(eff)=1-sin^2_eff, implied rho-like ratio")
    print(
        f"    (7/9)/(1-sin^2_eff) = {rho_from_797:.5f}   (SM rho ~= 1.0100 incl. top/Higgs loops)"
    )
    print("\n  READ-OUT: the ~1% gap between the 7:9:17 tree ratio and the measured mixing")
    print("  angle is the SAME order as standard EW radiative corrections (Delta_r ~ 0.03,")
    print("  rho-1 ~ 0.008). Interpret in report: 'Z-tension is the size of a known one-loop")
    print("  correction' is plausible but NOT a derivation unless the correction is computed to")
    print("  land exactly on 9/7 — which requires the full on-shell renormalization, not 7:9:17.")
    print("=" * 74)


if __name__ == "__main__":
    main()
