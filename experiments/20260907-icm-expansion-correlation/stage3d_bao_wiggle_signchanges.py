"""Stage 3d -- close the BAO branch: does a WIGGLE spectrum break the
"exactly one sign change" premise that FIX 5 measured for smooth ones?

FIX 4 removed a docstring promise of a BAO variant that was never
implemented, and recorded it OPEN. This implements it.

WHY IT MATTERS. C4's conclusion (no finite compensation radius) rests on
xi having exactly ONE sign change. For the two smooth transfer functions
that was measured: 1. But baryon acoustic oscillations put a real feature
at ~105 Mpc/h -- right where xi is small and approaching its zero. If the
wiggle adds crossings there, the monotonicity argument fails for real
LCDM, and C4's reason (not necessarily its answer) goes with it.

TWO INDEPENDENT ROUTES, because transcribing the full Eisenstein & Hu
1998 fitting formula is error-prone and a single implementation cannot
audit itself:

  W1  Full EH98 transfer function WITH wiggles (eqs 6-24 of the paper).
  W2  A BAO template: the smooth EH98 no-wiggle shape multiplied by
        1 + A * j0(k*s) * exp(-(k*Sigma)^2)
      with s the sound horizon and Sigma the damping scale. This is the
      standard template form used in BAO fitting, and its amplitude A is
      tunable -- so it also answers "how big would the wiggle have to be
      to break the premise at all?", which a single yes/no cannot.

If W1 and W2 disagree on the sign-change count, that disagreement is the
finding and neither is reported as settled.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))

from stage3c_compensation_scale import (  # noqa: E402
    H_LITTLE,
    NS,
    OB0,
    OM0,
    SIGMA8,
    TCMB,
    T_eh_nowiggle,
    count_sign_changes,
    first_zero,
    tophat_w,
    xi_of_r,
)


# ------------------------------------------------- W1: full EH98 with wiggles
def T_eh_full(k_hmpc, om=OM0, ob=OB0, h=H_LITTLE, tcmb=TCMB):
    """Eisenstein & Hu 1998 full transfer function, WITH acoustic wiggles.

    k is passed in h/Mpc and converted internally: every EH98 formula
    below uses k in Mpc^-1.
    """
    k = np.atleast_1d(np.asarray(k_hmpc, dtype=float)) * h  # Mpc^-1
    omh2, obh2 = om * h * h, ob * h * h
    oc = om - ob
    theta = tcmb / 2.7
    fb, fc = ob / om, oc / om

    z_eq = 2.50e4 * omh2 * theta**-4
    k_eq = 7.46e-2 * omh2 * theta**-2

    b1d = 0.313 * omh2**-0.419 * (1.0 + 0.607 * omh2**0.674)
    b2d = 0.238 * omh2**0.223
    z_d = 1291.0 * omh2**0.251 / (1.0 + 0.659 * omh2**0.828) * (1.0 + b1d * obh2**b2d)

    def Rz(z):
        return 31.5 * obh2 * theta**-4 * (1000.0 / z)

    R_d, R_eq = Rz(z_d), Rz(z_eq)
    s = (
        (2.0 / (3.0 * k_eq))
        * np.sqrt(6.0 / R_eq)
        * np.log((np.sqrt(1.0 + R_d) + np.sqrt(R_d + R_eq)) / (1.0 + np.sqrt(R_eq)))
    )
    k_silk = 1.6 * obh2**0.52 * omh2**0.73 * (1.0 + (10.4 * omh2) ** -0.95)

    a1 = (46.9 * omh2) ** 0.670 * (1.0 + (32.1 * omh2) ** -0.532)
    a2 = (12.0 * omh2) ** 0.424 * (1.0 + (45.0 * omh2) ** -0.582)
    alpha_c = a1 ** (-fb) * a2 ** (-(fb**3))

    bb1 = 0.944 / (1.0 + (458.0 * omh2) ** -0.708)
    bb2 = (0.395 * omh2) ** -0.0266
    beta_c = 1.0 / (1.0 + bb1 * (fc**bb2 - 1.0))

    y = (1.0 + z_eq) / (1.0 + z_d)
    sq = np.sqrt(1.0 + y)
    Gy = y * (-6.0 * sq + (2.0 + 3.0 * y) * np.log((sq + 1.0) / (sq - 1.0)))
    alpha_b = 2.07 * k_eq * s * (1.0 + R_d) ** -0.75 * Gy
    beta_node = 8.41 * omh2**0.435
    beta_b = 0.5 + fb + (3.0 - 2.0 * fb) * np.sqrt((17.2 * omh2) ** 2 + 1.0)

    q = k / (13.41 * k_eq)
    ks = k * s

    def T0(alpha, beta):
        C = 14.2 / alpha + 386.0 / (1.0 + 69.9 * q**1.08)
        L = np.log(np.e + 1.8 * beta * q)
        return L / (L + C * q * q)

    f = 1.0 / (1.0 + (ks / 5.4) ** 4)
    T_c = f * T0(1.0, beta_c) + (1.0 - f) * T0(alpha_c, beta_c)

    s_tilde = s / (1.0 + (beta_node / ks) ** 3) ** (1.0 / 3.0)
    x = k * s_tilde
    sinc = np.where(x < 1e-8, 1.0 - x * x / 6.0, np.sin(x) / np.where(x == 0, 1.0, x))
    T_b = (
        T0(1.0, 1.0) / (1.0 + (ks / 5.2) ** 2)
        + alpha_b / (1.0 + (beta_b / ks) ** 3) * np.exp(-((k / k_silk) ** 1.4))
    ) * sinc

    out = fb * T_b + fc * T_c
    return out if np.ndim(k_hmpc) else float(out[0])


# ------------------------------------------------------ W2: BAO template
def make_T_template(amp, s_mpch=150.0 * 0.674, sigma_mpch=7.0):
    """Smooth EH98 no-wiggle times a tunable acoustic modulation.

    s ~ 150 Mpc comoving is the sound horizon; Sigma ~ 7 Mpc/h is the
    standard nonlinear damping of the BAO feature. amp is the fractional
    wiggle amplitude at k*s ~ 1 (real BAO is a few percent).
    """

    def T(k_hmpc, om=OM0, ob=OB0, h=H_LITTLE, **kw):
        k = np.atleast_1d(np.asarray(k_hmpc, dtype=float))
        base = T_eh_nowiggle(k, om=om, ob=ob, h=h)
        x = k * s_mpch
        j0 = np.where(x < 1e-8, 1.0 - x * x / 6.0, np.sin(x) / np.where(x == 0, 1.0, x))
        mod = 1.0 + amp * j0 * np.exp(-((k * sigma_mpch) ** 2))
        # modulation is applied to T, and P ~ T^2, so keep it non-negative
        return base * np.sqrt(np.maximum(mod, 1e-12))

    return T


def make_pk(tfun, ns=NS, sigma8=SIGMA8):
    def pk_raw(kk):
        return kk**ns * tfun(kk) ** 2

    k = np.logspace(-5.0, 2.5, 400_000)
    w = tophat_w(k * 8.0)
    s2 = np.trapezoid(pk_raw(k) * k * k * w * w, k) / (2.0 * np.pi**2)
    norm = sigma8**2 / s2
    return lambda kk: norm * pk_raw(kk)


def analyse(name, tfun, rmax=400.0, n=700):
    pk = make_pk(tfun)
    r = np.concatenate((np.linspace(0.05, 1.0, 20)[:-1], np.linspace(1.0, rmax, n)))
    xi = xi_of_r(pk, r)
    integ = np.concatenate(
        ([0.0], np.cumsum(0.5 * (xi[1:] * r[1:] ** 2 + xi[:-1] * r[:-1] ** 2) * np.diff(r)))
    )
    dbar = 3.0 * integ / r**3
    return {
        "name": name,
        "n_xi": count_sign_changes(xi),
        "n_dbar": count_sign_changes(dbar),
        "R_xi0": first_zero(r, xi),
        "R_comp": first_zero(r, dbar),
        "r": r,
        "xi": xi,
        "dbar": dbar,
    }


def main() -> int:
    print("=" * 76)
    print("PC1 -- W1 sanity: T(k) -> 1 as k -> 0, and wiggles are PRESENT")
    print("=" * 76)
    ksmall = np.array([1e-5])
    t0 = float(T_eh_full(ksmall)[0])
    print(f"  T_full(1e-5 h/Mpc) = {t0:.5f}   {'PASS' if abs(t0 - 1) < 0.02 else 'FAIL'}")
    kk = np.logspace(-3, 0, 4000)
    ratio = T_eh_full(kk) / T_eh_nowiggle(kk)
    amp = float(np.max(np.abs(ratio - 1.0)))
    n_osc = count_sign_changes(ratio - np.mean(ratio), skip=0)
    print(f"  max |T_full/T_nowiggle - 1| = {amp:.4f}  (real BAO: a few %)")
    print(f"  oscillations in the ratio   = {n_osc} sign changes about its mean")
    if abs(t0 - 1) > 0.02:
        print("  FAIL -- transfer function does not normalise; ABORT")
        return 1
    if n_osc < 3:
        print("  FAIL -- no oscillatory structure; the 'wiggle' spectrum is smooth")
        return 1
    print("  PASS -- normalises AND oscillates, so W1 is a genuine wiggle spectrum")

    print("\n" + "=" * 76)
    print("THE MEASUREMENT -- sign changes with and without BAO")
    print("=" * 76)
    cases = [
        ("EH98 no-wiggle (FIX 5 baseline)", T_eh_nowiggle),
        ("W1  EH98 FULL, real wiggles", T_eh_full),
        ("W2  template, amp=0.05 (realistic)", make_T_template(0.05)),
        ("W2  template, amp=0.20 (4x real)", make_T_template(0.20)),
        ("W2  template, amp=0.60 (12x real)", make_T_template(0.60)),
        ("W2  template, amp=0.95 (extreme)", make_T_template(0.95)),
    ]
    print(
        f"  {'spectrum':36s} {'#sign(xi)':>10} {'#sign(db)':>10} {'R_xi0[Mpc]':>12} {'R_comp':>9}"
    )
    results = []
    for nm, tf in cases:
        res = analyse(nm, tf)
        results.append(res)
        rx = f"{res['R_xi0'] / H_LITTLE:.1f}" if res["R_xi0"] else "none"
        rc = "NONE" if res["R_comp"] is None else f"{res['R_comp'] / H_LITTLE:.1f}"
        print(f"  {nm:36s} {res['n_xi']:>10} {res['n_dbar']:>10} {rx:>12} {rc:>9}")

    print("\n" + "=" * 76)
    print("VERDICT")
    print("=" * 76)
    w1 = next(r for r in results if r["name"].startswith("W1"))
    w2 = next(r for r in results if "amp=0.05" in r["name"])
    base = results[0]
    agree = w1["n_xi"] == w2["n_xi"]
    print(
        f"  baseline (smooth)        : {base['n_xi']} sign change(s) in xi, R_comp {base['R_comp']}"
    )
    print(f"  W1 full EH98 wiggles     : {w1['n_xi']} sign change(s) in xi, R_comp {w1['R_comp']}")
    print(f"  W2 template amp=0.05     : {w2['n_xi']} sign change(s) in xi, R_comp {w2['R_comp']}")
    print(f"\n  W1 and W2 agree on the count: {agree}")
    if not agree:
        print("  -> DISAGREEMENT IS THE FINDING. Neither is reported as settled.")
        return 0
    if w1["n_xi"] == 1 and w1["R_comp"] is None:
        print("""
  BAO does NOT break the premise. xi still has exactly one sign change
  with real acoustic oscillations present, and delta_bar still never
  crosses zero -- so C4's conclusion survives the case FIX 4 flagged as
  the one that could have broken it.

  The amplitude ladder above says how much wiggle it would take: see
  where (if anywhere) the count leaves 1.""")
    else:
        print("""
  BAO DOES change the count. C4's monotonicity argument does NOT hold
  for a realistic wiggle spectrum, and its conclusion must be re-derived
  or withdrawn for real LCDM.""")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
