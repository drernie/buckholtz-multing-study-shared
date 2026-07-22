"""T3b — Does the SM electroweak one-loop correction carry the Buckholtz tree
value sin^2(theta_W) = 2/9 onto the MEASURED effective mixing angle?

Audit of the numerical pattern m_W^2 : m_Z^2 : m_H^2 = 7 : 9 : 17.
NOT_VALIDATION / NO_AUTHOR_ERROR — this tests whether the ~3.9 sigma "Z-tension"
found in T3 is exactly the size and SIGN of the standard SM radiative correction,
or whether a residual remains.

Scheme discipline: every mixing-angle number is labelled with its scheme
(on-shell / effective / MS-bar). The decisive residual is reported with full
PDG error propagation and, where scheme choice matters, as a RANGE.

Standard formulas used (verified against PDG EW review / Sirlin on-shell scheme,
2026-07-22):
  Delta_rho   = 3 G_F m_t^2 / (8 sqrt2 pi^2)                     [leading top]
  Delta_rho_H = -3 G_F m_W^2 tan^2(theta) /(8 sqrt2 pi^2) * f(H) [Higgs log, small]
  sin^2_eff   = kappa * s_W^2(on-shell),  kappa = 1 + (c^2/s^2) Delta_rho + ...
  Delta_r     = Delta_alpha - (c^2/s^2) Delta_rho (1-Delta_alpha) + Delta_r_rem
  m_W^2 (1 - m_W^2/m_Z^2) = pi alpha / (sqrt2 G_F) * 1/(1 - Delta_r)   [Sirlin]

Sources checked this session:
  - PDG Electroweak review (kappa = 1 + Delta_kappa, Delta_kappa ~ (c^2/s^2)Delta_rho)
  - hep-ph/9708321 "Precise Predictions for the W-Boson Mass" (Delta_r structure)
"""

from __future__ import annotations

import math

SQRT2 = math.sqrt(2.0)
PI = math.pi

# ── Inputs [VERIFIED — PDG 2024/2026 world averages] ──────────────────────────
M_Z, SIG_MZ = 91.1880, 0.0020  # GeV, LEP
M_W, SIG_MW = 80.3692, 0.0133  # GeV, PDG 2024 world avg (dominant error)
M_H, SIG_MH = 125.20, 0.11  # GeV
M_T, SIG_MT = 172.57, 0.29  # GeV, direct (Tevatron+LHC)
G_F = 1.1663788e-5  # GeV^-2, muon lifetime (essentially exact here)
ALPHA0_INV = 137.035999  # alpha(0)^-1, fine-structure (essentially exact)
ALPHA0 = 1.0 / ALPHA0_INV
DELTA_ALPHA = 0.05903  # 1 - alpha(0)/alpha(m_Z); Delta_alpha_lep+had^(5)+top

# Measured mixing angles (three schemes) [VERIFIED — PDG]
S2_EFF, SIG_S2EFF = 0.23122, 0.00004  # effective leptonic sin^2_eff
S2_MSBAR = 0.23129  # MS-bar sin^2(m_Z)

# Buckholtz tree value
S2_TREE = 2.0 / 9.0  # = 1 - 7/9

SEP = "=" * 74
DASH = "-" * 74


def delta_rho_top() -> float:
    """Leading top-quark contribution to the rho parameter (on-shell)."""
    return 3.0 * G_F * M_T**2 / (8.0 * SQRT2 * PI**2)


def delta_rho_higgs(s2: float) -> float:
    """Sub-leading Higgs logarithmic contribution to Delta_rho (on-shell).

    Standard leading-log form (PDG EW review):
      Delta_rho_H ~ -(3 G_F m_W^2)/(8 sqrt2 pi^2) * (s2/c2) * [ln(m_H^2/m_W^2) - 5/6]
    Small and negative; included for honesty, does not change the verdict.
    """
    c2 = 1.0 - s2
    log_term = math.log(M_H**2 / M_W**2) - 5.0 / 6.0
    return -(3.0 * G_F * M_W**2) / (8.0 * SQRT2 * PI**2) * (s2 / c2) * log_term


def solve_mw(delta_r: float) -> float:
    """Solve the Sirlin relation m_W^2(1-m_W^2/m_Z^2)=A0^2/(1-Delta_r) for m_W."""
    a0_sq = PI * ALPHA0 / (SQRT2 * G_F)  # A0^2 = pi alpha /(sqrt2 G_F)
    rhs = a0_sq / (1.0 - delta_r)
    # x^2 - m_Z^2 x + m_Z^2 * rhs = 0, take the physical (larger) root
    a, b, c = 1.0, -(M_Z**2), M_Z**2 * rhs
    disc = b * b - 4.0 * a * c
    x = (-b + math.sqrt(disc)) / (2.0 * a)
    return math.sqrt(x)


def main() -> None:
    print(SEP)
    print("T3b — SM one-loop check of Buckholtz 7:9:17  (tree sin^2 = 2/9)")
    print(SEP)

    # ── On-shell measured mixing angle ────────────────────────────────────────
    s2_os = 1.0 - M_W**2 / M_Z**2
    # error on on-shell s^2 (m_W dominates)
    ds2_dmw = 2.0 * M_W / M_Z**2
    ds2_dmz = 2.0 * M_W**2 / M_Z**3
    sig_s2os = math.hypot(ds2_dmw * SIG_MW, ds2_dmz * SIG_MZ)

    print("\n[schemes of the mixing angle]")
    print(f"  tree (Buckholtz 2/9)        sin^2 = {S2_TREE:.6f}")
    print(
        f"  on-shell 1-m_W^2/m_Z^2      sin^2 = {s2_os:.6f} +/- {sig_s2os:.6f} "
        f"[VERIFIED-BASH, m_W-dominated]"
    )
    print(f"  effective leptonic          sin^2 = {S2_EFF:.6f} +/- {SIG_S2EFF:.6f} [PDG]")
    print(f"  MS-bar sin^2(m_Z)           sin^2 = {S2_MSBAR:.6f} [PDG]")

    # ── Radiative correction pieces ───────────────────────────────────────────
    drho_t = delta_rho_top()
    drho_h = delta_rho_higgs(s2_os)
    drho = drho_t + drho_h
    sig_drho = drho_t * (2.0 * SIG_MT / M_T)  # m_t error dominates Delta_rho
    c2, s2 = 1.0 - s2_os, s2_os
    dkappa_lead = (c2 / s2) * drho  # leading Delta_kappa
    kappa_lead = 1.0 + dkappa_lead

    print("\n" + DASH)
    print("SM radiative pieces (on-shell scheme)")
    print(DASH)
    print(
        f"  Delta_rho (top, 3 G_F m_t^2/8 sqrt2 pi^2) = {drho_t:.6f} "
        f"+/- {sig_drho:.6f}  [m_t error]"
    )
    print(f"  Delta_rho (Higgs log)                     = {drho_h:+.6f}  [small]")
    print(f"  Delta_rho (total)                         = {drho:.6f}")
    print(f"  Delta_alpha (running alpha 0->m_Z)        = {DELTA_ALPHA:.5f}  [PDG]")
    print(f"  c^2/s^2 (on-shell)                        = {c2 / s2:.5f}")
    print(f"  Delta_kappa (leading = c^2/s^2 * Delta_rho) = {dkappa_lead:.6f}")
    print(f"  kappa (leading)                           = {kappa_lead:.6f}")

    # measured loop shift (on-shell -> effective) and SM leading prediction
    shift_meas = S2_EFF - s2_os
    shift_sm_lead = dkappa_lead * s2_os
    # kappa needed to map measured on-shell exactly onto measured effective
    kappa_meas = S2_EFF / s2_os
    print("\n  loop shift on-shell -> effective:")
    print(f"    measured  sin^2_eff - s^2_os = {shift_meas:+.6f}")
    print(
        f"    SM lead   Delta_kappa * s^2  = {shift_sm_lead:+.6f}  "
        f"({100 * shift_sm_lead / shift_meas:.0f}% of measured; "
        f"rest is 2-loop/rem, brings kappa {kappa_lead:.4f}->{kappa_meas:.4f})"
    )

    # ══ READING (a): 7:9:17 = TREE masses; loops shift the effective angle ═════
    print("\n" + SEP)
    print("READING (a): 7:9:17 as TREE masses -> tree sin^2 = 2/9,")
    print("             apply SM loop shift, compare to measured sin^2_eff")
    print(SEP)
    # Apply the genuine SM loop shift (use the FULL measured shift = best case for
    # the pattern; and the leading-only shift as a range endpoint).
    pred_eff_full = S2_TREE + shift_meas  # tree + full SM on-shell->eff shift
    pred_eff_lead = S2_TREE + shift_sm_lead  # tree + leading-only shift
    res_full = S2_EFF - pred_eff_full
    res_lead = S2_EFF - pred_eff_lead
    # error: measured sin^2_eff, the tree->eff shift carries the on-shell mass error
    sig_pred = math.hypot(SIG_S2EFF, sig_s2os)  # 2/9 exact; shift ties to on-shell
    sig_a = math.hypot(sig_pred, SIG_S2EFF)
    print(f"  predicted sin^2_eff = 2/9 + shift(full SM) = {pred_eff_full:.6f}")
    print(f"  predicted sin^2_eff = 2/9 + shift(leading) = {pred_eff_lead:.6f}")
    print(f"  measured  sin^2_eff                         = {S2_EFF:.6f}")
    print(f"  residual (full shift)   = {res_full:+.6f}  = {res_full / sig_a:+.1f} sigma")
    print(f"  residual (leading shift)= {res_lead:+.6f}  = {res_lead / sig_a:+.1f} sigma")
    print("  >> the SM loop shift is a COMMON additive/multiplicative map; it moves")
    print("     tree (2/9) and measurement together, so the on-shell gap survives.")

    # ══ READING (b): 7:9:17 = ON-SHELL physical masses ════════════════════════
    print("\n" + SEP)
    print("READING (b): 7:9:17 as ON-SHELL physical masses -> s^2_os = 2/9")
    print(SEP)
    res_b = s2_os - S2_TREE
    sig_b = sig_s2os
    print(f"  Buckholtz on-shell sin^2 = 2/9 = {S2_TREE:.6f}")
    print(f"  measured  on-shell sin^2       = {s2_os:.6f} +/- {sig_b:.6f}")
    print(f"  residual = {res_b:+.6f}  = {res_b / sig_b:+.1f} sigma  (the Z-tension)")

    # W-mass form of the same statement, incl. SM Delta_r prediction
    mw_buck = M_Z * math.sqrt(7.0 / 9.0)
    delta_r_lead = DELTA_ALPHA - (c2 / s2) * drho * (1.0 - DELTA_ALPHA)
    # SM Delta_r remainder ~ +0.006 brings total to the known ~0.036; use a range
    mw_sm_lead = solve_mw(delta_r_lead)
    mw_sm_full = solve_mw(delta_r_lead + 0.006)  # + rem -> Delta_r ~ 0.036
    # Delta_r that 7:9:17 would REQUIRE
    a0_sq = PI * ALPHA0 / (SQRT2 * G_F)
    dr_needed = 1.0 - a0_sq / (mw_buck**2 * (1.0 - mw_buck**2 / M_Z**2))
    print(f"\n  m_W(Buckholtz) = m_Z*sqrt(7/9)        = {mw_buck:.4f} GeV")
    print(f"  m_W(measured)                          = {M_W:.4f} +/- {SIG_MW:.4f} GeV")
    print(f"  m_W residual = {mw_buck - M_W:+.4f} GeV = {(mw_buck - M_W) / SIG_MW:+.1f} sigma")
    print(f"  Delta_r (SM leading)   = {delta_r_lead:.5f}")
    print(f"  Delta_r (SM +rem ~full)= {delta_r_lead + 0.006:.5f}  (~PDG 0.036)")
    print(f"  m_W(SM predicted, Delta_r range) = [{mw_sm_full:.4f}, {mw_sm_lead:.4f}] GeV")
    print(
        f"  Delta_r REQUIRED by 7:9:17 = {dr_needed:.5f}  "
        f"(SM cannot reach: needs Delta_r ~0.003 SMALLER than SM value)"
    )
    print("  >> SM Delta_r already predicts m_W ~ measured (80.36-80.37); the loop")
    print("     correction is 'spent' reproducing the data, leaving no room for 80.42.")

    # m_W world-average sensitivity (skeptic caveat 2026-07-22): the residual is
    # NOT scheme-independent — it depends on which m_W average is adopted.
    print("\n  [m_W-average dependence — the residual's weakest premise]")
    for lbl, mw, sig in (
        ("PDG-2024 world avg", 80.3692, 0.0133),
        ("CDF-II raw (2022)", 80.4335, 0.0094),
        ("ATLAS-2024", 80.3670, 0.0160),
    ):
        print(
            f"    {lbl:<20} m_W={mw:.4f}+/-{sig:.4f} -> "
            f"7:9:17 residual {(mw_buck - mw) / sig:+.1f} sigma"
        )
    print("    >> under CDF-II raw the tension COLLAPSES (~1.6 sigma); PDG down-weights")
    print("       CDF for inconsistency, but the 3.8 sigma is not m_W-choice-invariant.")

    # ── rho-like cross check ──────────────────────────────────────────────────
    rho_like = (7.0 / 9.0) / (1.0 - S2_EFF)
    print("\n" + DASH)
    print("rho-like cross-check")
    print(DASH)
    print(f"  (7/9)/(1 - sin^2_eff) = {rho_like:.5f}  vs  SM rho ~ 1.0100 (top/Higgs loops)")
    print(f"  excess = {rho_like - 1.0100:+.5f}  (same ~0.001-in-sin^2 residual, re-expressed)")

    # ── Verdict summary table ─────────────────────────────────────────────────
    print("\n" + SEP)
    print("RESIDUAL SUMMARY")
    print(SEP)
    print(f"  (a) tree 2/9 + full SM loop shift   -> residual {res_full / sig_a:+.1f} sigma")
    print(f"  (b) on-shell 2/9 vs measured        -> residual {res_b / sig_b:+.1f} sigma")
    print(
        f"  (b) m_W form                        -> residual {(mw_buck - M_W) / SIG_MW:+.1f} sigma"
    )
    print("\n  VERDICT: NULL (with PARTIAL character).")
    print("  The SM one-loop shift is the RIGHT SIGN and ~right ORDER (0.008 vs the")
    print("  naive 0.009 gap), but it does NOT land 2/9 onto the measurement: a")
    print("  ~0.001-in-sin^2 (3.6-3.9 sigma, m_W-dominated) residual remains under")
    print("  BOTH readings. The Z-tension is loop-INVARIANT: it lives in the on-shell")
    print("  mass ratio, which the multiplicative kappa form factor cannot remove.")


if __name__ == "__main__":
    main()
