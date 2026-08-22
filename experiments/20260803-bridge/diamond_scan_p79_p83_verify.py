"""Diamond scan over P79-P83: the two candidate syntheses, CHECKED not asserted.

The scan's own rule (feedback_diamond_scan): after a research phase, ask what was
found that was NOT the goal, which discarded result gets reinterpreted, and which
two results form an unexpected pair -- then verify before calling it a Diamond.

D1 -- THE POTENTIAL'S ROLE IS CONFINING, NOT ENERGETIC.
  P82 measured the scalar's effective w -> 1/3: in V = lam*phi^4/4 the oscillating
  field redshifts like RADIATION, i.e. its ENERGY becomes negligible (Omega_phi
  falls 3.2e-04 -> 7.1e-07 over the span). P81/P83 found that at lam = 0 the
  background fails DISCONTINUOUSLY (min(1-g*phibar) drops 0.4712 -> 0.0285).
  Those two sit badly together: if the potential makes the scalar energetically
  irrelevant, why is removing it fatal?
  PROPOSED MECHANISM: lam's role is not energetic but CONFINING. With V=0,
  phibar_ddot = g*rho_A - 3H*phibar_dot has NO restoring force, so phibar grows
  without bound and 1-g*phibar is driven to zero. With lam>0 the lam*phibar^3
  term caps the amplitude. The same lam that makes the scalar's ENERGY
  irrelevant is what keeps its AMPLITUDE bounded -- and only the amplitude
  enters viability, through M(phibar) = 1-g*phibar.
  FALSIFIABLE: at lam=0, phibar must grow monotonically and without turning over;
  at lam>0 it must turn over / oscillate with a bounded envelope. If phibar is
  bounded at lam=0 too, the mechanism is wrong and the pairing is a coincidence.

D2 -- THE VIABILITY CONSTRAINT IS SET BY A PHASE THE LATE UNIVERSE HAS FORGOTTEN.
  min(1-g*phibar) is a minimum over eight decades. If it is attained EARLY, then
  the boundary P81/P83 mapped is fixed by a transient of a component that is
  provably negligible by the epoch P82's growth observable is measured in. That
  would be a real structural statement about this completion, not a curiosity.
  FALSIFIABLE: locate the time of the minimum. If it sits LATE, D2 is false.
"""

import importlib.util
import os
import sys

import numpy as np

BASE = (
    r"E:\Проверка Гипотез\работаю над проверкой гипотез\H - 11 Dr. Thomas J. Buckholtz"
    r"\buckholtz-idm-multing-mvp\experiments\20260803-bridge"
)


def load(name, fn):
    sp = importlib.util.spec_from_file_location(name, os.path.join(BASE, fn))
    m = importlib.util.module_from_spec(sp)
    sys.modules[name] = m
    sp.loader.exec_module(m)
    return m


p81 = load("p81_ref", "P81_background_viability.py")
from scipy.integrate import solve_ivp  # noqa: E402

T0, T_END = p81.T0, p81.T_END
A3, PHIDOT = p81.A3_INIT, p81.PHIDOT


def traj(g_hat, lam, phidot0=None, n=6000):
    y0 = [A3 ** (1.0 / 3.0), 0.0, PHIDOT if phidot0 is None else phidot0]
    with np.errstate(all="ignore"):
        s = solve_ivp(
            p81.background_rhs(g_hat, lam),
            (T0, T_END),
            y0,
            rtol=1e-10,
            atol=1e-22,
            dense_output=True,
        )
        if not s.success:
            return None
        tt = np.exp(np.linspace(np.log(T0), np.log(T_END), n))
        a_, pb, pd = s.sol(tt)
    if not np.all(np.isfinite(pb)):
        return None
    return {"t": tt, "a": a_, "pb": pb, "pd": pd, "M": 1.0 - g_hat * pb}


print("=" * 78)
print("D1 -- is lambda CONFINING (bounds phibar) rather than energetic?")
print("=" * 78)
print("\n  At g_hat = 0.5, where BOTH lam=0 and lam>0 are viable, so the")
print("  comparison is not confounded by one of them having already failed.")
print(f"\n  {'lam':<10}{'max phibar':<16}{'phibar monotone?':<20}{'turning points':<18}{'min M'}")
for lam in (0.0, 1e-8, 1e-4, 0.01, 1.0):
    r = traj(0.5, lam)
    if r is None:
        print(f"  {lam:<10g}{'trajectory not representable':<54}")
        continue
    pb = r["pb"]
    mono = bool(np.all(np.diff(pb) >= -1e-30))
    turns = int(np.sum(np.diff(np.sign(np.diff(pb))) != 0))
    print(f"  {lam:<10g}{np.max(pb):<16.6e}{str(mono):<20}{turns:<18}{np.min(r['M']):.6f}")
print("\n  READ: monotone-and-unbounded at lam=0, turning over at lam>0, is the")
print("  confining mechanism. If lam=0 also turns over, D1 is refuted.")

print("\n" + "=" * 78)
print("D2 -- is min(1-g*phibar) attained EARLY, in a phase later forgotten?")
print("=" * 78)
print("\n  Reported with Omega_phi AT THAT TIME, because the claim is precisely")
print("  that the constraint is set where the scalar still matters energetically.")
print(
    f"\n  {'(g,lam)':<14}{'t at min M':<14}{'a at min M':<14}{'min M':<12}"
    f"{'Omega_phi there':<18}{'decade of span'}"
)
for g, lam in ((0.5, 1.0), (1.0, 1.0), (2.0, 0.1), (0.75, 1e-4), (1.5, 0.01)):
    r = traj(g, lam)
    if r is None:
        continue
    i = int(np.argmin(r["M"]))
    pb_i, pd_i, a_i = r["pb"][i], r["pd"][i], r["a"][i]
    rho_phi = pd_i**2 / 2.0 + lam * pb_i**4 / 4.0
    rho_m = (p81.C_MATTER / a_i**3) * (1.0 - g * pb_i)
    om = rho_phi / (rho_phi + rho_m)
    dec = np.log10(r["t"][i] / T0) / np.log10(T_END / T0)
    print(
        f"  ({g:g},{lam:g})".ljust(14)
        + f"{r['t'][i]:<14.3e}{a_i:<14.4g}{r['M'][i]:<12.6f}{om:<18.3e}{dec:.2%}"
    )
print("\n  READ: a minimum in the first decades, at an Omega_phi orders above its")
print("  late value, means the viability boundary is fixed by an early transient")
print("  of a component that is negligible by the epoch f(a,k) is measured in.")
print("  A minimum at the END of the span refutes D2.")
