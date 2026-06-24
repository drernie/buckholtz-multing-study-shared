#!/usr/bin/env python3
"""C6 preference statistic: which W/H measurement set does 7:9:17 prefer?

The boson relation m_W^2 : m_Z^2 : m_H^2 = 7:9:17 has NO free parameter once
stated scale-free (two independent ratios m_W/m_Z = sqrt(7/9), m_H/m_Z =
sqrt(17/9)). We compute a 2-dof chi^2 of these two predictions against three
measurement scenarios that differ only by the currently-discrepant W and H
values. The scenario with the lowest chi^2 is the one the relation "prefers".

WHY: the W=3.8sigma residual vs the PDG average is not random -- both the W and
H predictions sit at the heavy end of their tensions. This quantifies it
honestly (falsifiable: future W combinations move the preferred scenario).

Run: python scripts/c6_mass_preference.py
Source values: PDG 2024 (W-mass review, CDF-II excl), CDF-II 2022, CMS 2024 W,
CMS 2022 H, ATLAS 2023 H.
"""

from __future__ import annotations

import math

# 7:9:17 scale-free predictions (zero free parameters)
R_WZ = math.sqrt(7 / 9)  # m_W/m_Z
R_HZ = math.sqrt(17 / 9)  # m_H/m_Z

M_Z, S_Z = 91.1876, 0.0021  # PDG 2024, common to all scenarios

# (label, m_W, s_W, m_H, s_H)
SCENARIOS = [
    ("PDG-2024 avg", 80.3692, 0.0133, 125.20, 0.11),
    ("heavy (CDF-II W + CMS H)", 80.4335, 0.0094, 125.35, 0.15),
    ("light (CMS-24 W + ATLAS H)", 80.3602, 0.0099, 125.11, 0.11),
]


def ratio_sigma(a, sa, b, sb):
    """1-sigma on a/b via standard error propagation."""
    r = a / b
    return r * math.sqrt((sa / a) ** 2 + (sb / b) ** 2)


print(f"7:9:17 predicts (scale-free): m_W/m_Z = {R_WZ:.5f}, m_H/m_Z = {R_HZ:.5f}\n")
print(f"{'scenario':28s} {'chi2(2dof)':>10s} {'z_WZ':>7s} {'z_HZ':>7s} {'p-value':>9s}")
results = []
for label, mw, sw, mh, sh in SCENARIOS:
    rwz, srwz = mw / M_Z, ratio_sigma(mw, sw, M_Z, S_Z)
    rhz, srhz = mh / M_Z, ratio_sigma(mh, sh, M_Z, S_Z)
    z_wz = (rwz - R_WZ) / srwz
    z_hz = (rhz - R_HZ) / srhz
    chi2 = z_wz**2 + z_hz**2
    # 2-dof chi^2 survival = exp(-chi2/2)
    pval = math.exp(-chi2 / 2)
    results.append((label, chi2, pval))
    print(f"{label:28s} {chi2:10.2f} {z_wz:7.2f} {z_hz:7.2f} {pval:9.4f}")

# --- Boundary check: does the integer ladder extend to the top quark? ---
# (No: it is specific to the three EW bosons. Pre-empts "why only 3 bosons?")
U2 = (M_Z / 3.0) ** 2
M_TOP, S_TOP = 172.69, 0.30  # PDG 2024 top pole mass
top_units = (M_TOP**2) / U2
nearest = round(top_units)
top_dev_pct = abs(top_units - nearest) / nearest * 100
d_units = 2 * M_TOP / U2 * S_TOP
top_sig = abs(top_units - nearest) / d_units
print(
    f"\nBoundary: top quark (m_t/(m_Z/3))^2 = {top_units:.2f} vs nearest int {nearest} "
    f"-> {top_dev_pct:.2f}% ({top_sig:.1f}sigma); W/Z/H fit to 0.13-0.20%. "
    f"Ladder is EW-boson-specific; the top does NOT fit."
)

best = min(results, key=lambda r: r[1])
worst = max(results, key=lambda r: r[1])
print(f"\nPREFERRED (lowest chi2): {best[0]}  chi2={best[1]:.2f}")
print(f"DISFAVORED (highest):    {worst[0]}  chi2={worst[1]:.2f}")
print(f"chi2 ratio worst/best = {worst[1] / best[1]:.1f}x")
print(
    "\nInterpretation: 7:9:17 (zero free params) prefers the HEAVY measurement set."
    "\nFalsifiable: if the W world-average settles toward the light/SM value with"
    "\nshrinking error, the relation's error-weighted support is excluded."
)
