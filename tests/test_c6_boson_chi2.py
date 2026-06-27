"""
Tests for 7:9:17 boson chi² preference statistic (paper Table ref:tab:c6pref).

Verified values from c6_mass_preference.py run 2026-06-27:
  heavy (CDF-II W + CMS H):      chi²=2.04  ← paper says 2.0
  PDG-2024 avg:                   chi²=15.56 ← paper says 15.6
  light (CMS-24 W + ATLAS H):    chi²=38.97 ← paper says 39
"""

import math

M_Z, S_Z = 91.1876, 0.0021  # PDG 2024

R_WZ = math.sqrt(7 / 9)  # scale-free prediction m_W/m_Z
R_HZ = math.sqrt(17 / 9)  # scale-free prediction m_H/m_Z


def _ratio_sigma(a: float, sa: float, b: float, sb: float) -> float:
    """1-sigma on ratio a/b via standard error propagation."""
    return (a / b) * math.sqrt((sa / a) ** 2 + (sb / b) ** 2)


def _chi2_2dof(m_w: float, sig_w: float, m_h: float, sig_h: float) -> float:
    """2-dof chi² using scale-free ratios (matches c6_mass_preference.py)."""
    rwz = m_w / M_Z
    rhz = m_h / M_Z
    srwz = _ratio_sigma(m_w, sig_w, M_Z, S_Z)
    srhz = _ratio_sigma(m_h, sig_h, M_Z, S_Z)
    z_wz = (rwz - R_WZ) / srwz
    z_hz = (rhz - R_HZ) / srhz
    return z_wz**2 + z_hz**2


def _predict() -> tuple[float, float]:
    """Return (m_W_pred, m_H_pred) from 7:9:17 Z anchor."""
    unit = M_Z / 3
    return unit * math.sqrt(7), unit * math.sqrt(17)


SCENARIOS = {
    "PDG-2024 avg": (80.3692, 0.0133, 125.20, 0.11, 15.6),
    "heavy (CDF-II W + CMS H)": (80.4335, 0.0094, 125.35, 0.15, 2.0),
    "light (CMS-24 W + ATLAS H)": (80.3602, 0.0099, 125.11, 0.11, 39.0),
}


def test_boson_chi2_heavy_consistent() -> None:
    """CDF-II W + CMS H gives chi²≈2.0 (paper: 2.0, p=0.36 → consistent)."""
    m_w, sig_w, m_h, sig_h, expected = SCENARIOS["heavy (CDF-II W + CMS H)"]
    chi2 = _chi2_2dof(m_w, sig_w, m_h, sig_h)
    assert abs(chi2 - expected) < 0.5, f"chi²={chi2:.2f}, expected {expected}"


def test_boson_chi2_pdg_disfavored() -> None:
    """PDG-2024 average gives chi²≈15.6 (paper: 15.6, p=4e-4 → disfavored)."""
    m_w, sig_w, m_h, sig_h, expected = SCENARIOS["PDG-2024 avg"]
    chi2 = _chi2_2dof(m_w, sig_w, m_h, sig_h)
    assert abs(chi2 - expected) < 0.5, f"chi²={chi2:.2f}, expected {expected}"


def test_boson_chi2_light_excluded() -> None:
    """CMS-24 W + ATLAS H gives chi²≈39 (paper: 39, p<1e-5 → excluded)."""
    m_w, sig_w, m_h, sig_h, expected = SCENARIOS["light (CMS-24 W + ATLAS H)"]
    chi2 = _chi2_2dof(m_w, sig_w, m_h, sig_h)
    assert abs(chi2 - expected) < 1.0, f"chi²={chi2:.2f}, expected {expected}"


def test_heavy_beats_light_by_large_factor() -> None:
    """Light chi² must be > 10× larger than heavy chi² (falsifiable discriminant)."""
    mw_h, sw_h, mh_h, sh_h, _ = SCENARIOS["heavy (CDF-II W + CMS H)"]
    mw_l, sw_l, mh_l, sh_l, _ = SCENARIOS["light (CMS-24 W + ATLAS H)"]
    chi2_heavy = _chi2_2dof(mw_h, sw_h, mh_h, sh_h)
    chi2_light = _chi2_2dof(mw_l, sw_l, mh_l, sh_l)
    ratio = chi2_light / chi2_heavy
    assert ratio > 15, f"chi² ratio light/heavy = {ratio:.1f}, expected >15"


def test_prediction_from_z_anchor() -> None:
    """7:9:17 Z-anchored predictions: m_W=80.420, m_H=125.33 GeV."""
    w_pred, h_pred = _predict()
    assert abs(w_pred - 80.420) < 0.001, f"m_W_pred={w_pred:.4f}"
    assert abs(h_pred - 125.33) < 0.01, f"m_H_pred={h_pred:.4f}"
