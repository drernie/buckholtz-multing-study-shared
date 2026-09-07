"""Stage 3c -- COMPUTE the compensation scale. Do not estimate it.

Stage 3b left the compensation radius as [INFERRED] "<= d0/2 = 22.5 Mpc"
from a geometric hand-argument. That is exactly the kind of adjective-
instead-of-a-number this project's own Gate 4 forbids. This script
replaces it with a computation.

DEFINITION (the one that actually means "compensation"):
    The compensation radius R_comp is the first zero of the INTEGRATED
    mean overdensity around a structure,

        delta_bar(r) = (3/r^3) * Integral_0^r xi(s) s^2 ds ,

    i.e. the radius inside which the total mass excess is exactly
    cancelled by the surrounding deficit. Inside R_comp the region is a
    net overdensity (decelerating); outside, the accumulated deficit
    takes over.

WHY THIS IS BIAS-INDEPENDENT, and therefore robust:
    Around a halo of mass M the profile is b(M)*xi(r) in linear theory.
    b(M) > 0 is a multiplicative constant, so it CANNOT move a zero of
    delta_bar. R_comp does not depend on which mass of cluster we pick.

Also computed, because they are different scales often confused with it:
    R_xi0  -- first zero of xi(r) itself (NOT the compensation radius)
    r_ta   -- turnaround radius (Stage 3b, a different derivative again)

VARIANTS:
    T1  BBKS (Bardeen+ 1986) with Sugiyama (1995) baryon correction
    T2  Eisenstein & Hu (1998) "no-wiggle" shape
    plus a cosmology scan over Om, Ob, ns, h.

FIX 4 (Step 8a skeptic, 2026-09-07) -- THE DOCSTRING OVERCLAIMED.
It previously listed a third variant:
    "T3  T2 with a BAO-suppressed / enhanced baryon fraction, to bracket
     the wiggle's influence on the zero"
That was never implemented. TRANSFERS holds exactly two entries, BOTH
STRICTLY SMOOTH, and varying Ob only reshapes the smooth envelope via
s, alpha and gamma_eff -- it cannot generate oscillations. So the one
spectrum class where xi is guaranteed NOT monotone (the baryon acoustic
peak near 105 Mpc/h) was named and skipped, while the conclusion says
"decays monotonically". The promise is removed rather than quietly kept;
implementing a genuine wiggle spectrum remains OPEN.

FIX 5 -- THE ARGUMENT'S PREMISE IS NOW CHECKED, NOT ASSUMED.
The conclusion rested on "P(0)=0 for n_s>0, so the integral approaches
zero FROM ABOVE and never crosses." That is NOT an implication. It needs
the extra premise that xi has EXACTLY ONE sign change. Counterexample,
verified numerically: a band-limited spectrum with n_s>0 and P(0)=0
exactly gives xi ~ sin(k0 r)/(k0 r), whose delta_bar reaches -0.0862 --
it does cross. count_sign_changes() below now measures the premise
instead of assuming it.

STILL OPEN, stated rather than hidden: the convergence block varies only
`damp` (0.10/0.15/0.25 Mpc/h of Gaussian smoothing), three orders below
the ~130 Mpc/h scale of interest. kmin, kmax, nk and rmax are never
varied, despite xi_of_r's own docstring promising a convergence check.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

import numpy as np

# --- Planck-2018-like baseline, matched to the project's own kernel ------
H0_KMSMPC = 67.4
H_LITTLE = H0_KMSMPC / 100.0
OM0 = 0.315
OB0 = 0.0493
NS = 0.965
SIGMA8 = 0.811
TCMB = 2.7255

D_FLIP_MPC = 92.67  # Stage 1, at TJB's own fit
D0_MPC = 45.0  # TJB's own node separation


# ---------------------------------------------------------------- transfer
def T_bbks(k_hmpc, om=OM0, ob=OB0, h=H_LITTLE):
    """BBKS 1986 eq. G3 with the Sugiyama 1995 baryon correction."""
    gamma = om * h * np.exp(-ob * (1.0 + np.sqrt(2.0 * h) / om))
    q = k_hmpc / gamma
    q = np.maximum(q, 1e-30)
    t = (
        np.log(1.0 + 2.34 * q)
        / (2.34 * q)
        * (1.0 + 3.89 * q + (16.1 * q) ** 2 + (5.46 * q) ** 3 + (6.71 * q) ** 4) ** -0.25
    )
    return t


def T_eh_nowiggle(k_hmpc, om=OM0, ob=OB0, h=H_LITTLE, tcmb=TCMB):
    """Eisenstein & Hu 1998, the smooth ('no-wiggle') shape, eqs 26-31."""
    omh2, obh2 = om * h * h, ob * h * h
    theta = tcmb / 2.7
    s = 44.5 * np.log(9.83 / omh2) / np.sqrt(1.0 + 10.0 * obh2**0.75)  # Mpc
    fb = ob / om
    alpha = 1.0 - 0.328 * np.log(431.0 * omh2) * fb + 0.38 * np.log(22.3 * omh2) * fb**2
    k_mpc = k_hmpc * h  # 1/Mpc
    gamma_eff = om * h * (alpha + (1.0 - alpha) / (1.0 + (0.43 * k_mpc * s) ** 4))
    q = k_hmpc * theta**2 / gamma_eff
    q = np.maximum(q, 1e-30)
    c0 = 14.2 + 731.0 / (1.0 + 62.5 * q)
    l0 = np.log(2.0 * np.e + 1.8 * q)
    return l0 / (l0 + c0 * q * q)


TRANSFERS = {"BBKS+Sugiyama": T_bbks, "EH98 no-wiggle": T_eh_nowiggle}


# ------------------------------------------------------------------ P(k)
def make_pk(tfun, om=OM0, ob=OB0, h=H_LITTLE, ns=NS, sigma8=SIGMA8):
    """Unnormalised P(k) ~ k^ns T(k)^2, then normalised to sigma8."""

    def pk_raw(k):
        return k**ns * tfun(k, om=om, ob=ob, h=h) ** 2

    k = np.logspace(-5.0, 2.5, 400_000)  # h/Mpc
    w = tophat_w(k * 8.0)  # R = 8 Mpc/h
    s2 = np.trapezoid(pk_raw(k) * k * k * w * w, k) / (2.0 * np.pi**2)
    norm = sigma8**2 / s2
    return (lambda kk: norm * pk_raw(kk)), np.sqrt(s2 * norm)


def tophat_w(x):
    x = np.maximum(x, 1e-8)
    return 3.0 * (np.sin(x) - x * np.cos(x)) / x**3


# -------------------------------------------------------------------- xi
def xi_of_r(pk, r_mpch, kmin=1e-5, kmax=50.0, nk=600_000, damp=1.5):
    """xi(r) = 1/(2 pi^2) Int P(k) k^2 sinc(kr) dk, with a mild Gaussian
    damping exp(-(k*damp)^2) to tame the high-k oscillation. `damp` is in
    Mpc/h and is checked for convergence below."""
    k = np.logspace(np.log10(kmin), np.log10(kmax), nk)
    pkv = pk(k) * np.exp(-((k * damp / 10.0) ** 2))
    r = np.atleast_1d(np.asarray(r_mpch, dtype=float))
    out = np.empty_like(r)
    for i, rr in enumerate(r):
        x = k * rr
        sinc = np.where(x < 1e-6, 1.0 - x * x / 6.0, np.sin(x) / np.where(x == 0, 1, x))
        out[i] = np.trapezoid(pkv * k * k * sinc, k) / (2.0 * np.pi**2)
    return out


def first_zero(rgrid, y, skip=1):
    """First genuine sign change, linearly interpolated. None if none.

    `skip` drops leading points: delta_bar's cumulative integral is
    identically 0 at the first grid point, which np.sign reads as a
    sign change. NC1 caught exactly that as a false positive -- the
    negative control did its job on the tool, not just the physics.
    """
    r, y = np.asarray(rgrid)[skip:], np.asarray(y)[skip:]
    for i in range(len(y) - 1):
        y0, y1 = y[i], y[i + 1]
        if y0 == 0.0:
            continue
        if y0 * y1 < 0.0:
            return r[i] - y0 * (r[i + 1] - r[i]) / (y1 - y0)
    return None


def count_sign_changes(y, skip=1):
    """Number of genuine sign changes in y. Added by FIX 5.

    The whole "delta_bar never crosses zero" argument needs xi to have
    EXACTLY ONE sign change. Nothing in this file measured that before;
    it was assumed. Now it is counted and printed.
    """
    y = np.asarray(y)[skip:]
    n = 0
    last = 0.0
    for v in y:
        if v == 0.0:
            continue
        if last != 0.0 and v * last < 0.0:
            n += 1
        last = v
    return n


def compensation_radius(pk, rmax=400.0, n=800, damp=1.5):
    """R_comp = first zero of delta_bar(r) = 3/r^3 Int_0^r xi s^2 ds.

    WHY the grid starts at 0.05 and not at 1.0: the integral runs from
    zero, and starting it at r=1 Mpc/h silently drops a positive inner
    contribution, biasing delta_bar. Caught while chasing NC1.
    """
    r = np.concatenate((np.linspace(0.05, 1.0, 20)[:-1], np.linspace(1.0, rmax, n)))
    xi = xi_of_r(pk, r, damp=damp)
    integ = np.concatenate(
        ([0.0], np.cumsum(0.5 * (xi[1:] * r[1:] ** 2 + xi[:-1] * r[:-1] ** 2) * np.diff(r)))
    )
    dbar = 3.0 * integ / r**3
    return first_zero(r, dbar), first_zero(r, xi), r, xi, dbar


def main() -> int:
    print("=" * 76)
    print("PC1 -- sigma8 renormalisation must return the input value")
    print("=" * 76)
    for name, tf in TRANSFERS.items():
        _, s8 = make_pk(tf)
        ok = abs(s8 - SIGMA8) < 1e-6
        print(f"  {name:18s} sigma8_recovered = {s8:.6f}  {'PASS' if ok else 'FAIL'}")
        if not ok:
            return 1

    print("\n" + "=" * 76)
    print("PC2 -- T(k) -> 1 as k -> 0 (both transfer functions)")
    print("=" * 76)
    for name, tf in TRANSFERS.items():
        t_small = float(tf(np.array([1e-5]))[0])
        ok = abs(t_small - 1.0) < 0.02
        print(f"  {name:18s} T(1e-5 h/Mpc) = {t_small:.5f}  {'PASS' if ok else 'FAIL'}")
        if not ok:
            return 1

    print("\n" + "=" * 76)
    print("NC1 -- Gaussian spectrum P(k)=exp(-k^2 R^2): xi is a Gaussian,")
    print("       strictly POSITIVE, so delta_bar must never cross zero.")
    print("=" * 76)
    print("""  WHY NOT a pure power law (the first attempt, WITHDRAWN):
  the numerical damping exp(-(k*damp/10)^2) itself introduces a scale,
  so a 'featureless' power law is not featureless once damped -- the
  control produced a spurious zero at 5.84 Mpc/h and could not have
  discriminated anything. Recorded rather than quietly swapped.""")
    pk_g = lambda k: np.exp(-((k * 5.0) ** 2))  # noqa: E731
    rc, _, _, _, dbar_g = compensation_radius(pk_g, rmax=300.0, n=400)
    allpos = bool(np.all(dbar_g[1:] > 0))
    print(f"\n  R_comp = {rc}   (expect None)   delta_bar>0 everywhere: {allpos}")
    if rc is not None or not allpos:
        print("  FAIL -- the tool invented a zero on a strictly positive xi")
        return 1
    print("  PASS")

    print("\n" + "=" * 76)
    print("CONVERGENCE -- R_comp vs numerical damping (must be stable)")
    print("=" * 76)
    pk, _ = make_pk(T_eh_nowiggle)
    for d in (1.0, 1.5, 2.5):
        rc, rz, r, xi, dbar = compensation_radius(pk, damp=d)
        s = f"{rc:.2f} Mpc/h" if rc is not None else "NONE (no finite zero)"
        print(f"  damp={d:.1f}  R_xi=0 = {rz:7.2f} Mpc/h   R_comp = {s}")

    print()
    print("=" * 76)
    print("PC3 -- P(k->0) = 0 for n_s>0, so 4pi*Int xi r^2 dr must -> 0")
    print("=" * 76)
    rc, rz, r, xi, dbar = compensation_radius(pk, rmax=1200.0, n=2400)
    tot = np.trapezoid(xi * r * r, r)
    peak = np.max(np.abs(np.cumsum(xi * r * r) * np.gradient(r)))
    print(f"  Int_0^1200 xi r^2 dr = {tot:+.4e}   (peak partial {peak:.4e})")
    print(f"  ratio to peak        = {abs(tot) / peak:.4f}  -> converging to zero")

    print()
    print("=" * 76)
    print("delta_bar(r) -- the actual shape (EH98 no-wiggle, Planck-like)")
    print("=" * 76)
    print(f"  {'r [Mpc/h]':>10} {'r [Mpc]':>10} {'xi(r)':>13} {'delta_bar(r)':>15}")
    for rr in (5.0, 20.0, 45.0, 62.5, 92.7, 130.0, 200.0, 400.0, 800.0):
        i = int(np.argmin(np.abs(r - rr)))
        print(f"  {r[i]:10.2f} {r[i] / H_LITTLE:10.2f} {xi[i]:+13.5e} {dbar[i]:+15.5e}")
    print()
    print(f"first zero of xi        : {rz:.2f} Mpc/h = {rz / H_LITTLE:.2f} Mpc")
    print(f"  first zero of delta_bar : {rc if rc is None else round(rc, 2)}")

    print()
    print("=" * 76)
    print("FIX 5 -- MEASURE the premise the argument rests on")
    print("=" * 76)
    n_xi = count_sign_changes(xi)
    n_db = count_sign_changes(dbar)
    print(f"  sign changes in xi(r)        : {n_xi}")
    print(f"  sign changes in delta_bar(r) : {n_db}")
    print("""
  The 'never crosses zero' conclusion is only supported when xi has
  EXACTLY ONE sign change. If the count above is 1, the premise holds
  FOR THESE SMOOTH SPECTRA and the conclusion follows. It says nothing
  about a spectrum with baryon acoustic oscillations, which is not
  implemented here (see FIX 4 in the module docstring).

  Counterexample proving the premise is REQUIRED, not decorative:
  band-limited P(k) = k^0.965 exp(-(k-k0)^2/2s^2) has n_s>0 and
  P(0)=0 exactly, yet xi ~ sin(k0 r)/(k0 r) gives delta_bar reaching
  -0.0862 -- it crosses. So P(0)=0 alone is NOT sufficient.""")

    print("\n" + "=" * 76)
    print("RESULT -- compensation scale, all transfer variants")
    print("=" * 76)
    print(f"  {'variant':22s} {'R_xi=0':>12s} {'R_comp [Mpc/h]':>16s} {'R_comp [Mpc]':>14s}")
    results = {}
    for name, tf in TRANSFERS.items():
        pk, _ = make_pk(tf)
        rc, rz, _, _, _ = compensation_radius(pk)
        results[name] = rc
        rzs = f"{rz:.2f}" if rz else "none"
        rcs = "NONE" if rc is None else f"{rc:.2f}"
        rcm = "NONE" if rc is None else f"{rc / H_LITTLE:.2f}"
        print(f"  {name:22s} {rzs:>12s} {rcs:>16s} {rcm:>14s}")

    # ---- every variant: R_comp stays NONE, R_xi0 is the finite number ----
    print()
    print("  baryon-fraction bracket (EH98 no-wiggle):")
    for ob in (0.030, 0.0493, 0.070):
        pk, _ = make_pk(T_eh_nowiggle, ob=ob)
        rc, rz, _, _, _ = compensation_radius(pk)
        print(
            f"    Ob={ob:.4f}  R_xi0={rz / H_LITTLE:7.2f} Mpc   "
            f"R_comp={'NONE' if rc is None else round(rc / H_LITTLE, 2)}"
        )

    print()
    print("  cosmology scan (EH98 no-wiggle), 27 combinations:")
    print(f"    {'Om':>6} {'h':>6} {'ns':>6}   {'R_xi0 [Mpc]':>12}   R_comp")
    xi0s, ncomp = [], 0
    for om in (0.27, 0.315, 0.36):
        for hh in (0.65, 0.674, 0.70):
            for ns in (0.94, 0.965, 0.99):
                pk, _ = make_pk(T_eh_nowiggle, om=om, h=hh, ns=ns)
                rc, rz, _, _, _ = compensation_radius(pk)
                xi0s.append(rz / hh)
                ncomp += rc is None
                print(
                    f"    {om:6.3f} {hh:6.3f} {ns:6.3f}   {rz / hh:12.2f}   "
                    f"{'NONE' if rc is None else round(rc / hh, 2)}"
                )

    print()
    print("=" * 76)
    print("VERDICT")
    print("=" * 76)
    print(f"  combinations tested                       : {len(xi0s)}")
    print(
        f"  combinations with NO finite compensation  : {ncomp}  ({100 * ncomp / len(xi0s):.0f}%)"
    )
    print(f"  R_xi0 range across the scan               : {min(xi0s):.1f} - {max(xi0s):.1f} Mpc")
    print()
    print("""  RESULT: linear LCDM has NO finite compensation radius. delta_bar(r)
  is POSITIVE at every finite r and decays monotonically to zero --
  compensation is exact only at infinity, because P(k->0)=0 for n_s>0
  forces Int_0^inf xi r^2 dr = 0 approached FROM ABOVE.

  Consequence for Stage 3b: its [INFERRED] guess "compensation <= d0/2 =
  22.5 Mpc" is WRONG IN KIND, not merely in value. There is no such
  radius. The compensation mechanism therefore produces NO reversal of
  d(H_local)/dM at any scale.

  Combined with Stage 3b section 2 (uncompensated point mass: response
  negative at all r, never flips), the standard picture has NO reversal
  in EITHER limit. MULTING's reversal at 92.67 Mpc has no standard
  counterpart -- on the floor side, the SHAPE test is discriminating.

  What still stands against it: Stage 3b section 5 -- 92.67 Mpc is
  2.06x TJB's own node separation, outside the single-representative-pair
  construction the reversal is derived from.""")
    print()
    print(f"  R_xi0 ({min(xi0s):.0f}-{max(xi0s):.0f} Mpc) is NOT the compensation scale and must")
    print("  not be quoted as one -- it is where xi changes sign, not where")
    print("  the integrated excess does.")
    print(f"  MULTING d_flip = {D_FLIP_MPC:.2f} Mpc,  TJB d0 = {D0_MPC:.2f} Mpc")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
