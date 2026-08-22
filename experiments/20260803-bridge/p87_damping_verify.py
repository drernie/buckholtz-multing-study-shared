"""Is the deviation of phibar_peak from eta^0.5 CAUSED by Hubble damping?

P87's Part C measured phibar_peak ~ eta^0.873 against the free-field energy
prediction eta^0.500. The deviation runs in the direction damping would give --
peak time falls 21.6 -> 4.9 as eta grows, so small eta spends longer under
friction, its peak is suppressed more, and the apparent exponent steepens. But
that was noticed AFTER seeing the direction, which makes it a consistency
observation, not a test.

DECISIVE TEST: delete the -3*H*phibar_dot term and re-measure. With damping gone,
energy is exactly conserved between phibar=0 and the turning point, so the
prediction eta^0.5 becomes EXACT and the residual must collapse to round-off.

  exponent -> 0.5 with a tiny residual  => damping IS the cause, confirmed
  exponent stays near 0.873             => damping is NOT the cause, and the
                                           post-hoc story is withdrawn
"""

import importlib.util
import os
import sys

import numpy as np
from scipy.integrate import solve_ivp

BASE = (
    r"E:\Проверка Гипотез\работаю над проверкой гипотез\H - 11 Dr. Thomas J. Buckholtz"
    r"\buckholtz-idm-multing-mvp\experiments\20260803-bridge"
)
sp = importlib.util.spec_from_file_location("p80", os.path.join(BASE, "P80_onshell_attribution.py"))
p80 = importlib.util.module_from_spec(sp)
sys.modules["p80"] = p80
sp.loader.exec_module(p80)

LAM, PHIDOT = 1.0, p80.PHIDOT


def peak(eta, damping=True):
    def rhs(_t, y):
        a_, pb, pd = y
        rho_A = p80.C_MATTER / a_**3
        arg = (8 * np.pi * p80.G_N / 3) * (rho_A + pd**2 / 2 + LAM * pb**4 / 4)
        H = np.sqrt(arg) if arg > 0 else 0.0
        fric = 3.0 * H * pd if damping else 0.0
        return [a_ * H, pd, -fric - LAM * pb**3]

    with np.errstate(all="ignore"):
        s = solve_ivp(
            rhs,
            (1.0, 1e8),
            [p80.A3_INIT ** (1 / 3), 0.0, eta * PHIDOT],
            rtol=1e-12,
            atol=1e-24,
            dense_output=True,
        )
        tt = np.exp(np.linspace(0.0, np.log(1e8), 60000))
        pb, pd = s.sol(tt)[1], s.sol(tt)[2]
    i = np.where(np.diff(np.sign(pd)) != 0)[0]
    return (float(abs(pb[i[0]])), float(tt[i[0]])) if len(i) else None


def fit(x, y):
    lx, ly = np.log(x), np.log(y)
    p = np.polyfit(lx, ly, 1)
    return float(p[0]), float(np.max(np.abs(ly - np.polyval(p, lx))))


etas = np.array([0.25, 0.5, 1.0, 2.0, 4.0])
print("=" * 74)
print("Does deleting Hubble damping restore phibar_peak ~ eta^0.5 exactly?")
print("=" * 74)
print()
print(f"  {'eta':<8}{'peak WITH damping':<22}{'peak WITHOUT':<22}{'t_pk (no damp)'}")
w, wo = [], []
for e in etas:
    a = peak(e, True)
    b = peak(e, False)
    w.append(a[0])
    wo.append(b[0])
    print(f"  {e:<8.2f}{a[0]:<22.6e}{b[0]:<22.6e}{b[1]:.4g}")

nw, rw = fit(etas, np.array(w))
nn, rn = fit(etas, np.array(wo))
print()
print(f"  WITH damping    : exponent {nw:.6f}   max log-resid {rw:.4f}")
print(f"  WITHOUT damping : exponent {nn:.6f}   max log-resid {rn:.4f}")
print("  free-field prediction : 0.500000")
print()
if abs(nn - 0.5) < 0.01 and rn < 0.01:
    print("  => CONFIRMED. Without friction the exponent is 0.5 to 1 percent and")
    print("     the residual collapses, so the 0.873 measured WITH damping is")
    print("     caused by Hubble friction acting for longer at small eta.")
else:
    print("  => NOT CONFIRMED. Removing friction did not restore eta^0.5, so the")
    print("     post-hoc damping story is WITHDRAWN and the deviation is")
    print("     unexplained.")
