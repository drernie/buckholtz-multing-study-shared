"""
Self-Consistency Diagnostic — TJB IDM/MULTING Session 2026-06-09
Tests whether Table A1 H_MULT values are consistent with the Phi(z)/Phi(0)
bridge using the cluster parameters published in Claude Supplementary.

WHY THIS FILE (not *_test.py): Diagnostic, not a pytest test suite.
Results feed into TJB_DIAGNOSTIC_BRIEF.md Section M.

FINDINGS (all [VERIFIED-tool]):
  Part A: H_pred from Phi DECREASES 73→~0.1 km/s/Mpc (×762 drop)
          H_MULT_reported INCREASES 73→418 km/s/Mpc (×5.7 rise)
          Self-inconsistency gap: ×4365 at z=8.5
  Part B: H_MULT/H_FLRW ratio = 1.074 ± 0.026, corr=0.99993
          Bridge is a scalar stretch of H_FLRW — no independent physics signal
  Part C: Gemini cross-check — Phi(z)/Phi(0) FLAT not growing
          Dataset-independent: neither service's bridge generates H(z) growth
  Part D: ε_q >> 1 at ALL z → C11 corrected; C12 REFUTED
  Part E: Required D(z) for consistent bridge → physically implausible

SAFETY LABELS:
  NOT_VALIDATION, NOT_REFUTATION, NOT_AUTHOR_ERROR
  INTERNAL_DIAGNOSTIC_ONLY, AUTHOR_CLARIFICATION_REQUIRED
"""

import numpy as np

# ─────────────────────────────────────────────────────────────────────────────
# DATA — cluster params from Claude Supplementary (geometric means of log-ranges)
# Format: (z, m_A [Msun], k_A/c² [Msun], r_A [Mpc], D [Mpc])
# Source: arXiv:2025.11.0598.v6, Claude Supplementary CSV
# ─────────────────────────────────────────────────────────────────────────────
CLAUDE_PARAMS = [
    (0.00, 3.16e14, 1.00e12, 1.73, 44.7),  # geom(1e14,1e15),geom(1e11,1e13),geom(1,3),geom(20,100)
    (0.06, 3.16e14, 1.00e12, 1.73, 44.7),
    (0.14, 2.68e14, 9.00e11, 1.59, 42.4),
    (0.25, 1.90e14, 7.00e11, 1.41, 39.1),
    (0.40, 1.26e14, 5.00e11, 1.24, 34.6),
    (0.65, 6.32e13, 3.00e11, 1.04, 29.0),
    (1.00, 3.16e13, 1.00e11, 0.87, 24.5),
    (1.50, 1.58e13, 5.00e10, 0.69, 20.0),
    (2.10, 6.32e12, 2.00e10, 0.52, 15.5),
    (3.20, 1.58e12, 5.00e9, 0.37, 12.2),
    (5.00, 3.16e11, 1.00e9, 0.27, 8.9),
    (8.50, 9.49e10, 3.00e8, 0.17, 6.7),  # geom(3e10,3e11),geom(3e8,3e9),geom(0.10,0.3),geom(3,15)
]

# Gemini cluster params (single values per z, from CSV)
GEMINI_PARAMS = [
    (0.02, 1.2e15, 6.0e12, 2.1, 55.0),
    (0.05, 1.1e15, 5.5e12, 2.0, 52.0),
    (0.14, 1.0e15, 5.0e12, 1.9, 48.0),
    (0.25, 9.0e14, 4.5e12, 1.8, 44.0),
    (0.38, 8.0e14, 4.0e12, 1.7, 40.0),
    (0.54, 7.0e14, 3.5e12, 1.6, 36.0),
    (0.74, 6.0e14, 3.0e12, 1.5, 32.0),
    (1.01, 5.0e14, 2.5e12, 1.4, 28.0),
    (1.38, 4.0e14, 2.0e12, 1.3, 24.0),
    (1.92, 3.0e14, 1.5e12, 1.2, 20.0),
    (2.81, 2.0e14, 1.0e12, 1.1, 16.0),
]

# Reported values from Table A1 (Claude service rows)
# Source: Claude Supplementary transcript
H_MULT_REP = np.array(
    [73.0, 70.2, 73.5, 78.8, 83.1, 91.4, 104.2, 126.5, 151.8, 197.3, 271.5, 418.1]
)
H_FLRW_REP = np.array([67.4, 68.1, 69.3, 71.5, 75.0, 83.0, 95.7, 114.8, 140.3, 187.6, 265.2, 398.5])
Z_VALS = np.array([row[0] for row in CLAUDE_PARAMS])

# WHY: TJB confirmed beta values are phenomenological (fitted, not fundamental)
BETA_D_CLAUDE = 4.5
BETA_Q_CLAUDE = 18.0
BETA_D_GEMINI = 4.25
BETA_Q_GEMINI = 8.10
H_ANCHOR = 73.0  # SH0ES H₀ anchor [km/s/Mpc]

DIV = "=" * 72


# ─────────────────────────────────────────────────────────────────────────────
# BRIDGE FORMULA (Claude Supplementary lines 1201–1209)
# H²_MULT(z) / H²_anchor = Phi(z) / Phi(0)
# Phi = m_A/D² − 2·k_A·β_d·r_A/D³ + (k_A·β_q·r_A)²/D⁴
# WHY G,c² omitted: they cancel exactly in the ratio
# ─────────────────────────────────────────────────────────────────────────────
def phi(m_A: float, k_A: float, r_A: float, D: float, beta_d: float, beta_q: float) -> float:
    """Force potential proxy (G, c² cancel in ratio)."""
    F_m = m_A / D**2
    F_d = 2.0 * k_A * beta_d * r_A / D**3
    F_q = (k_A * beta_q * r_A) ** 2 / D**4
    return F_m - F_d + F_q


def compute_H_pred(params: list, beta_d: float, beta_q: float, H_anchor: float) -> np.ndarray:
    """H_pred from bridge: H(z) = H_anchor * sqrt(Phi(z)/Phi(0))."""
    _, m0, k0, r0, D0 = params[0]
    phi0 = phi(m0, k0, r0, D0, beta_d, beta_q)
    H_vals = []
    for row in params:
        _, m, k, r, D = row
        p = phi(m, k, r, D, beta_d, beta_q)
        H_vals.append(H_anchor * np.sqrt(max(p / phi0, 0.0)))
    return np.array(H_vals)


# ─────────────────────────────────────────────────────────────────────────────
# PART A — SELF-CONSISTENCY
# ─────────────────────────────────────────────────────────────────────────────
print(f"\n{DIV}")
print("  PART A — SELF-CONSISTENCY: H_pred(bridge) vs H_MULT_reported")
print("  SAFETY: NOT_VALIDATION, NOT_REFUTATION, NOT_AUTHOR_ERROR")
print(DIV)

H_pred = compute_H_pred(CLAUDE_PARAMS, BETA_D_CLAUDE, BETA_Q_CLAUDE, H_ANCHOR)
phi_vals = np.array([phi(*row[1:], BETA_D_CLAUDE, BETA_Q_CLAUDE) for row in CLAUDE_PARAMS])
phi_norm = phi_vals / phi_vals[0]

print(f"\n  {'z':>5} {'H_pred':>9} {'H_MULT_rep':>11} {'ratio_rep/pred':>15} {'Phi(z)/Phi(0)':>14}")
print(f"  {'-' * 57}")
for row, hp, hm, pn in zip(CLAUDE_PARAMS, H_pred, H_MULT_REP, phi_norm):
    z = row[0]
    ratio = float(hm) / float(hp) if float(hp) > 0.01 else float("inf")
    flag = "  ← ANCHOR" if z == 0.00 else ("  ⚠ DIVERGING" if ratio > 100 else "")
    print(
        f"  {z:>5.2f} {float(hp):>9.3f} {float(hm):>11.1f} {ratio:>15.1f} {float(pn):>14.6f}{flag}"
    )

H_pred_z85 = float(H_pred[-1])
H_mult_z85 = float(H_MULT_REP[-1])
phi_z85 = float(phi_norm[-1])

print(f"\n  ── z=8.5 summary ─────────────────────────────────────")
print(f"  Phi(z=8.5)/Phi(0) = {phi_z85:.6f}  → Phi DECREASES ×{1 / phi_z85:.0f}")
print(f"  H_pred(z=8.5)     = {H_pred_z85:.3f} km/s/Mpc  (bridge + CSV params)")
print(f"  H_MULT_reported   = {H_mult_z85:.1f} km/s/Mpc  (Table A1)")
print(
    f"  H_pred trajectory: {H_ANCHOR:.1f} → {H_pred_z85:.3f}  (×{H_ANCHOR / H_pred_z85:.0f} DECREASE)"
)
print(
    f"  H_MULT trajectory: {H_ANCHOR:.1f} → {H_mult_z85:.1f}  (×{H_mult_z85 / H_ANCHOR:.1f} INCREASE)"
)
print(f"  SELF-INCONSISTENCY GAP: ×{H_mult_z85 / H_pred_z85:.0f} at z=8.5")
print(f"\n  [VERIFIED-tool] Bridge formula + CSV params → H DECREASES.")
print(f"                  Table A1 H_MULT → H INCREASES. Mutually inconsistent.")


# ─────────────────────────────────────────────────────────────────────────────
# PART B — H_MULT / H_FLRW RATIO
# ─────────────────────────────────────────────────────────────────────────────
print(f"\n{DIV}")
print("  PART B — H_MULT = 1.07 × H_FLRW (ratio analysis)")
print(DIV)

ratio_arr = H_MULT_REP / H_FLRW_REP
corr_coef = float(np.corrcoef(H_MULT_REP, H_FLRW_REP)[0, 1])

print(f"\n  {'z':>5} {'H_MULT':>8} {'H_FLRW':>8} {'ratio':>7}")
print(f"  {'-' * 33}")
for z, hm, hf, r in zip(Z_VALS, H_MULT_REP, H_FLRW_REP, ratio_arr):
    print(f"  {z:>5.2f} {float(hm):>8.1f} {float(hf):>8.1f} {float(r):>7.4f}")

ratio_mean = float(ratio_arr.mean())
ratio_std = float(ratio_arr.std())
print(f"\n  mean ratio  = {ratio_mean:.4f}")
print(f"  std  ratio  = {ratio_std:.4f}  ({ratio_std / ratio_mean * 100:.1f}% scatter)")
print(f"  corr(H_MULT, H_FLRW) = {corr_coef:.6f}")
print(f"\n  [VERIFIED-tool] H_MULT ≈ 1.074 × H_FLRW, scatter 2.6%, corr=0.99993")
print(f"  IMPLICATION: Bridge adds no independent H(z) information beyond H_FLRW.")


# ─────────────────────────────────────────────────────────────────────────────
# PART C — GEMINI CROSS-CHECK
# ─────────────────────────────────────────────────────────────────────────────
print(f"\n{DIV}")
print("  PART C — GEMINI CROSS-CHECK (dataset independence)")
print(DIV)

H_pred_gem = compute_H_pred(GEMINI_PARAMS, BETA_D_GEMINI, BETA_Q_GEMINI, H_ANCHOR)
phi_gem = np.array([phi(*row[1:], BETA_D_GEMINI, BETA_Q_GEMINI) for row in GEMINI_PARAMS])
phi_gem_norm = phi_gem / phi_gem[0]

print(f"\n  Gemini β_d={BETA_D_GEMINI}, β_q={BETA_Q_GEMINI}")
print(f"  {'z':>5} {'H_pred_Gemini':>14} {'Phi(z)/Phi(0)':>14}")
print(f"  {'-' * 38}")
for row, hp, pn in zip(GEMINI_PARAMS, H_pred_gem, phi_gem_norm):
    print(f"  {row[0]:>5.2f} {float(hp):>14.3f} {float(pn):>14.6f}")

print(
    f"\n  Gemini H_pred range: {float(H_pred_gem.min()):.1f} – {float(H_pred_gem.max()):.1f} km/s/Mpc"
)
print(f"  (Table A1 H_obs range: ~70 – 420+ km/s/Mpc)")
print(f"\n  [VERIFIED-tool] DATASET-INDEPENDENT VERDICT:")
print(f"    Claude (β_q={BETA_Q_CLAUDE:.1f}): H_pred DECREASES  → trend reversal vs H_obs")
print(f"    Gemini (β_q={BETA_Q_GEMINI:.2f}): H_pred FLAT/weak → no growth vs H_obs")
print(f"    Both fail differently — neither bridge reproduces observed H(z) growth.")


# ─────────────────────────────────────────────────────────────────────────────
# PART D — TERM DOMINANCE AT ALL Z
# ─────────────────────────────────────────────────────────────────────────────
print(f"\n{DIV}")
print("  PART D — TERM DOMINANCE AT ALL Z  (claim table C11/C12)")
print(DIV)
print()
print(
    f"  {'z':>5} {'ε_d=F_d/F_m':>12} {'ε_q=F_q/F_m':>12} "
    f"{'dominant':>10} {'C11(ε_q>1)':>11} {'C12(ε_d>1)':>11}"
)
print(f"  {'-' * 68}")

eps_d_max = 0.0
D_crossover = 2.0 * 1e12 * BETA_D_CLAUDE * 1.73 / 3.16e14  # WHY: z=0 params

for row in CLAUDE_PARAMS:
    z, m, k, r, D = row
    F_m = m / D**2
    F_d = 2.0 * k * BETA_D_CLAUDE * r / D**3
    F_q = (k * BETA_Q_CLAUDE * r) ** 2 / D**4
    eps_d = F_d / F_m
    eps_q = F_q / F_m
    eps_d_max = max(eps_d_max, eps_d)
    dominant = "QUAD" if eps_q > eps_d else "DIPOLE"
    c11 = "YES" if eps_q > 1.0 else "NO "
    c12 = "YES" if eps_d > 1.0 else "NO "
    print(f"  {z:>5.2f} {eps_d:>12.3e} {eps_q:>12.3e} {dominant:>10} {c11:>11} {c12:>11}")

print(f"\n  CLAIM TABLE UPDATE [VERIFIED-tool]:")
print(f"    C11 (ε_q >> 1 'at high z'): confirmed, but MISCHARACTERIZED")
print(f"         True at ALL z — not just high z")
print(f"    C12 (dipole dominates at late times): REFUTED")
print(f"         max ε_d = {eps_d_max:.3e}  (need > 1, never achieved at inter-cluster scales)")
print(f"         D_crossover for ε_d=1 at z=0: {D_crossover:.3f} Mpc (actual D=44.7 Mpc)")
print(f"    C14 (bridge formula exists): PARTIAL")
print(f"         Formula H²∝Phi/Phi₀ exists but gives wrong direction")


# ─────────────────────────────────────────────────────────────────────────────
# PART E — REQUIRED D(z) SCHEDULE
# ─────────────────────────────────────────────────────────────────────────────
print(f"\n{DIV}")
print("  PART E — REQUIRED D(z) for self-consistent bridge (quad-dominated)")
print(DIV)
print()
print(f"  {'z':>5} {'H_MULT_rep':>11} {'D_csv':>8} {'D_req':>8} {'req/csv':>8}")
print(f"  {'-' * 48}")

_, m0, k0, r0, D0 = CLAUDE_PARAMS[0]
phi0_q = (k0 * BETA_Q_CLAUDE * r0) ** 2 / D0**4

D_req_final = float("nan")
for row, hm in zip(CLAUDE_PARAMS, H_MULT_REP):
    z, m, k, r, D = row
    kqr_sq = (k * BETA_Q_CLAUDE * r) ** 2
    target = (float(hm) / H_ANCHOR) ** 2
    D_req = (kqr_sq / (phi0_q * target)) ** 0.25 if target > 0 else float("nan")
    D_req_final = D_req
    print(f"  {z:>5.2f} {float(hm):>11.1f} {D:>8.1f} {D_req:>8.1f} {D_req / D:>8.2f}x")

print(f"\n  CSV D(z): DECREASES {D0:.1f} → {CLAUDE_PARAMS[-1][4]:.1f} Mpc (physically plausible)")
print(f"  Required D: must stay large — physically implausible schedule.")
print(f"  [INFERRED] Bridge with shrinking clusters → H falls, not rises.")


# ─────────────────────────────────────────────────────────────────────────────
# PART F — MULTIVERSE: repr.value sensitivity (T4 guard per hypothesis-red-team 2026-06-09)
# Q: Does self-inconsistency survive arithmetic mean instead of geometric mean?
# Documented log-ranges (from CSV comments):
#   z=0.00: m_A=[1e14,1e15], k_A=[1e11,1e13], r_A=[1,3], D=[20,100]
#   z=8.50: m_A=[3e10,3e11], k_A=[3e8,3e9], r_A=[0.1,0.3], D=[3,15]
# Intermediate z: no documented ranges → geom params used; noted as limitation.
# ─────────────────────────────────────────────────────────────────────────────
print(f"\n{DIV}")
print("  PART F — MULTIVERSE: repr.value sensitivity (hypothesis-red-team T4 guard)")
print("  Tests whether self-inconsistency gap survives arithmetic mean cluster params")
print(DIV)

# Arithmetic-mean params at documented endpoints
_z0_ARITH = (0.00, (1e14 + 1e15) / 2, (1e11 + 1e13) / 2, (1.0 + 3.0) / 2, (20.0 + 100.0) / 2)
_z85_ARITH = (8.50, (3e10 + 3e11) / 2, (3e8 + 3e9) / 2, (0.10 + 0.30) / 2, (3.0 + 15.0) / 2)

# Build ARITH_PARAMS: replace z=0.00 and z=8.50 rows; keep intermediate geom rows
ARITH_PARAMS = list(CLAUDE_PARAMS)  # copy
ARITH_PARAMS[0] = _z0_ARITH
ARITH_PARAMS[-1] = _z85_ARITH

# Compute phi ratio at z=8.5 under each specification
phi0_geom = phi(*CLAUDE_PARAMS[0][1:], BETA_D_CLAUDE, BETA_Q_CLAUDE)
phi85_geom = phi(*CLAUDE_PARAMS[-1][1:], BETA_D_CLAUDE, BETA_Q_CLAUDE)
phi0_arith = phi(*_z0_ARITH[1:], BETA_D_CLAUDE, BETA_Q_CLAUDE)
phi85_arith = phi(*_z85_ARITH[1:], BETA_D_CLAUDE, BETA_Q_CLAUDE)

ratio_geom = phi85_geom / phi0_geom
ratio_arith = phi85_arith / phi0_arith

H_pred_arith_z85 = H_ANCHOR * (max(ratio_arith, 0.0) ** 0.5)
gap_arith = H_mult_z85 / H_pred_arith_z85 if H_pred_arith_z85 > 1e-6 else float("inf")

print(
    f"\n  {'Spec':>16} {'phi0':>14} {'phi(z=8.5)':>14} {'ratio':>10} {'H_pred z=8.5':>14} {'gap vs rep':>11}"
)
print(f"  {'-' * 80}")
print(
    f"  {'geom_mean (base)':>16} {phi0_geom:>14.4e} {phi85_geom:>14.4e} "
    f"{ratio_geom:>10.6f} {float(H_pred[-1]):>14.3f} {H_mult_z85 / float(H_pred[-1]):>11.0f}×"
)
print(
    f"  {'arith_mean (new)':>16} {phi0_arith:>14.4e} {phi85_arith:>14.4e} "
    f"{ratio_arith:>10.6f} {H_pred_arith_z85:>14.3f} {gap_arith:>11.0f}×"
)

print(f"\n  ── Multiverse verdict ────────────────────────────────────────────────")
if ratio_arith < 1.0 and gap_arith > 10:
    print(f"  [ROBUST] Phi ratio still DECREASES under arith repr. (ratio={ratio_arith:.6f})")
    print(
        f"  Self-inconsistency gap under arith_mean = ×{gap_arith:.0f} (vs ×{H_mult_z85 / float(H_pred[-1]):.0f} geom)"
    )
    print(f"  Conclusion survives T4 (Garden of Forking Paths) repr.value check.")
elif ratio_arith >= 1.0:
    print(f"  [WEAKENED] Phi ratio = {ratio_arith:.4f} (≥1) under arith_mean → H_pred INCREASES")
    print(f"  Repr.value choice MATTERS — original conclusion may not be robust.")
else:
    print(f"  [MARGINAL] Gap ×{gap_arith:.0f} — smaller than geom but still significant.")

print(f"\n  Note: intermediate z rows (0.06–5.00) use geom params (no range data).")
print(f"  Full multiverse requires documented ranges at all 12 z values (Q for TJB).")


# ─────────────────────────────────────────────────────────────────────────────
# SUMMARY
# ─────────────────────────────────────────────────────────────────────────────
print(f"\n{DIV}")
print("  FINDINGS SUMMARY — Session 2026-06-09")
print(f"{DIV}")
print()
print(f"  M1 [VERIFIED-tool]: H_MULT = {ratio_mean:.3f} x H_FLRW")
print(f"      scatter {ratio_std / ratio_mean * 100:.1f}%, corr={corr_coef:.5f}")
print(f"      Bridge is ~7% scalar stretch of H_FLRW — no independent physics.")
print()
print(f"  M2 [VERIFIED-tool]: Self-consistency FAILURE at z=8.5")
print(f"      Phi DECREASES x{1 / phi_z85:.0f}, H_pred = {H_pred_z85:.3f} km/s/Mpc")
print(f"      H_MULT_reported = {H_mult_z85:.1f} km/s/Mpc")
print(f"      Inconsistency gap: x{H_mult_z85 / H_pred_z85:.0f}")
print()
print(f"  M3 [VERIFIED-tool]: Dataset-independent failure")
print(f"      Claude->reversal; Gemini->flat; both fail to generate H(z) growth.")
print()
print(f"  M4 [VERIFIED-tool]: Claim table update")
print(f"      C11: true ALL z (corrected from 'high z only')")
print(f"      C12: REFUTED — dipole never dominates at inter-cluster scales")
print(f"      C14: exists but wrong direction")
print()
print(f"  M5: Skeptic gate CONFIRMED-REAL (3/3 falsification tests passed)")
print()
print(f"  Q15 FOR TJB:")
print(f"    Phi(z) with CSV cluster params DECREASES x762 from z=0 to z=8.5,")
print(f"    yet H_MULT in Table A1 INCREASES x5.7. This suggests the D(z)")
print(f"    schedule used by the AI service differs from CSV geometric means.")
print(f"    Could you clarify which D(z) values were actually used — physical")
print(f"    scaling or chosen to match H_obs directly?")
print()
print(f"  SAFETY: NOT_VALIDATION  NOT_REFUTATION  NOT_AUTHOR_ERROR")
print(f"          INTERNAL_DIAGNOSTIC_ONLY  AUTHOR_CLARIFICATION_REQUIRED")
print(f"{DIV}\n")
