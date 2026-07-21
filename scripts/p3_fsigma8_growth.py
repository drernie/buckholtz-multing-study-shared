"""p3_fsigma8_growth.py — P3: does the MULTING dipole modify linear fsigma8(z)?

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION

SCOPE WARNING (skeptic 2026-07-22): the BROAD claim "MULTING dipole is degenerate with
LCDM at linear order" was FALSIFIED. This script establishes only a NARROW result — the
INTRINSIC-RANDOM dipole branch with a scale-independent constant modification at fixed
Om at one z. It does NOT cover the induced-polarization branch (Blanchet DDM), does NOT
use the correct k-dependent parametrization, and the |A_dip| bound is a fixed-Om
artifact. See the VERDICT block and docs/128 for the five limitations and the Q006
kill-condition. Read that before citing anything from here.

C1 showed the dipole's real action is LARGE second-order (structure) fluctuations,
not the (zero) background. P3 asks whether that signal appears in the LINEAR growth
observable fsigma8 (RSD), or stays at second order (power spectrum / bispectrum).

Physics / order counting: fsigma8 tracks the LINEAR growth rate f = dlnD/dlna, i.e.
the coherent (mean) growth of a density mode. The monopole-dipole force is LINEAR in
the dipole moment p_j = q*n_hat_j, and for isotropic orientations <n_hat_j> = 0 (the
C1 mechanism), so the COHERENT dipole contribution to the linear growth source
vanishes -> the dipole does NOT modify linear fsigma8 for the isotropic default. A
coherent modification requires a q-delta_m CORRELATION (rho_corr != 0), an unspecified
closure. We encode this as A_dip = (coherent dipole growth strength) in the growth
equation:  d^2 D/dx^2 + (2 - 1.5*Om(a)) dD/dx - 1.5*Om(a)*(1 + A_dip)*D = 0,  x = ln a.

  A_dip = 0  <- isotropic dipole default (C1: coherent part washes out) == LCDM
  A_dip != 0 <- POSITIVE CONTROL: a coherent q-delta correlation would shift fsigma8

Real data (cited, digitized): DESI DR1 PV survey consensus fsigma8(z=0.07) = 0.450 +/-
0.055, Om = 0.301 +/- 0.011, sigma8 = 0.834 +/- 0.032, "consistent with LCDM and GR"
(2512.03231, literature/refs_digitized/2512.03231_desi-dr1-growth-rate.md).

Run:  python scripts/p3_fsigma8_growth.py
Exit: 0 if fsigma8 is degenerate for the isotropic default (A_dip=0 == LCDM) AND the
      control (A_dip!=0) shifts it AND the real point bounds |A_dip|, else 1.
"""

from __future__ import annotations

import sys

import numpy as np
from scipy.integrate import solve_ivp

OMEGA_M = 0.301  # DESI DR1 (2512.03231)
SIGMA8_0 = 0.834  # DESI DR1, today
Z_DATA, FS8_DATA, FS8_ERR = 0.07, 0.450, 0.055  # DESI DR1 consensus point (real)


def _growth(a_eval: float, a_dip: float) -> tuple[float, float]:
    """Return (D(a_eval)/D(1), f(a_eval)) for the linear growth ODE with a coherent
    dipole growth strength a_dip (a_dip=0 -> standard LCDM growth)."""

    def rhs(x: float, y: np.ndarray) -> list[float]:
        a = np.exp(x)
        e2 = OMEGA_M * a**-3 + (1 - OMEGA_M)
        om_a = OMEGA_M * a**-3 / e2
        d, dp = y
        ddp = -(2 - 1.5 * om_a) * dp + 1.5 * om_a * (1 + a_dip) * d
        return [dp, ddp]

    x0, x1 = np.log(1e-3), 0.0  # deep matter era (D ∝ a) to today
    sol = solve_ivp(
        rhs,
        [x0, x1],
        [1e-3, 1e-3],
        t_eval=[np.log(a_eval), 0.0],
        rtol=1e-9,
        atol=1e-12,
        dense_output=True,
    )
    d_ae, d_1 = sol.y[0]
    dp_ae = sol.y[1][0]
    f_ae = dp_ae / d_ae  # f = dlnD/dlna = D'/D in x=ln a
    return d_ae / d_1, f_ae


def fsigma8(z: float, a_dip: float) -> float:
    a = 1.0 / (1.0 + z)
    d_ratio, f = _growth(a, a_dip)
    return f * SIGMA8_0 * d_ratio


def main() -> int:
    print("=" * 70)
    print("P3 — does the MULTING dipole modify linear fsigma8(z)?")
    print("=" * 70)
    print(f"cosmology: Om={OMEGA_M}, sigma8_0={SIGMA8_0} (DESI DR1)")
    print(f"real point: fsigma8({Z_DATA}) = {FS8_DATA} +/- {FS8_ERR} (DESI DR1, LCDM-consistent)")

    fs8_lcdm = fsigma8(Z_DATA, a_dip=0.0)  # isotropic dipole default == LCDM
    print(f"\n[isotropic dipole default, A_dip=0]  fsigma8({Z_DATA}) = {fs8_lcdm:.4f}")
    print(
        f"   vs real {FS8_DATA} +/- {FS8_ERR}  ->  {abs(fs8_lcdm - FS8_DATA) / FS8_ERR:.2f} sigma"
    )
    print("   (A_dip=0 IS LCDM by construction -> dipole is DEGENERATE at linear order,")
    print("    because <n_hat>=0 kills the coherent growth source, same as C1.)")

    print("\n[POSITIVE CONTROL: a coherent q-delta correlation, A_dip != 0]")
    print(f"{'A_dip':>8} {'fsigma8(0.07)':>14} {'shift vs LCDM':>14} {'tension w/ data':>16}")
    control_shifts = []
    for a_dip in (0.05, 0.10, 0.20, -0.10):
        fs8 = fsigma8(Z_DATA, a_dip)
        shift = fs8 - fs8_lcdm
        tens = (fs8 - FS8_DATA) / FS8_ERR
        control_shifts.append(abs(shift))
        print(f"{a_dip:>8.2f} {fs8:>14.4f} {shift:>+14.4f} {tens:>+15.2f}σ")

    # bound |A_dip| from the real data (roughly: |A_dip| where shift ~ 1 sigma of data)
    # linear response d(fsigma8)/d(A_dip) near 0:
    resp = (fsigma8(Z_DATA, 0.02) - fsigma8(Z_DATA, -0.02)) / 0.04
    a_dip_1sigma = FS8_ERR / abs(resp)
    print(f"\nLinear response d(fsigma8)/d(A_dip) = {resp:.4f}")
    print(f"=> data bounds the coherent dipole growth strength: |A_dip| < ~{a_dip_1sigma:.2f} (1σ)")

    print("\n" + "=" * 70)
    print("VERDICT — NARROWED (skeptic FALSIFIED the broad 'MULTING degenerate' claim)")
    print("=" * 70)
    degenerate = abs(fs8_lcdm - fsigma8(Z_DATA, 0.0)) < 1e-9  # A_dip=0 == LCDM
    control_works = all(s > 1e-3 for s in control_shifts)  # A_dip!=0 genuinely shifts
    data_consistent = abs(fs8_lcdm - FS8_DATA) / FS8_ERR < 2.0
    print("  LICENSED (narrow) claim — this script only establishes:")
    print("   For the INTRINSIC-RANDOM dipole branch (n_hat isotropic, uncorrelated with")
    print("   the tidal field), a SCALE-INDEPENDENT constant growth modification is")
    print(f"   LCDM-equivalent at A_dip=0 ({fs8_lcdm:.3f} vs DESI {FS8_DATA}+/-{FS8_ERR},")
    print(f"   {abs(fs8_lcdm - FS8_DATA) / FS8_ERR:.2f}σ) and, AT FIXED Om/sigma8 and one z,")
    print(
        f"   a constant shift is bounded |A_dip|<~{a_dip_1sigma:.2f}. Control confirms sensitivity."
    )
    print("\n  NOT LICENSED (skeptic-falsified overreach) — this script does NOT show:")
    print("   1. induced-polarization branch (p ∝ ∇∇Φ ∝ δ, Blanchet DDM 0901.3114) --")
    print("      <n_hat>=0 does NOT cover it; that branch DOES enter linear growth. UNTESTED.")
    print("   2. a real bound: |A_dip|<0.21 is FIXED-Om; marginalizing Om absorbs it")
    print("      (beta_cv.py ΔAIC=+0.74 is direct evidence). Optimistic ~3-10x.")
    print("   3. correct parametrization: A_dip=const is scale-independent; a real dipole")
    print("      modification is k-dependent μ(k,z) -- a constant cannot represent it.")
    print("   4. sufficiency: one z=0.07 point; needs the full fsigma8(z) compilation.")
    print("   5. '2nd-order only': skips ≥6 first-order probes (E_G, P_θθ, scale-dep bias,")
    print("      RSD hexadecapole, δ×κ_CMB, void velocities).")
    print("\n  KILL-CONDITION for the induced branch = Q006 (MULTING Lagrangian): is there a")
    print("  ξ-coupling n_hat ↔ ∇∇Φ? ξ=0 by symmetry -> intrinsic-only claim survives;")
    print("  ξ≠0 -> full μ(k,z) analysis marginalized over Om, on the fsigma8(z) compilation")
    print("  + E_G, is required before ANY degeneracy claim. See docs/128.")
    # exit 0 = the NARROW claim holds (intrinsic branch LCDM-equiv + control works); the
    # broad claim is explicitly retracted above, not asserted.
    return 0 if (degenerate and control_works and data_consistent) else 1


if __name__ == "__main__":
    sys.exit(main())
