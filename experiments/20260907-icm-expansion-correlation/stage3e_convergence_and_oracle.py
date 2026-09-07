"""Stage 3e -- the last numerical debt: convergence over the integration
domain and resolution, plus a partial external oracle and an independent
integrator path.

THREE THINGS, answering three separate criticisms:

A. PARTIAL EXTERNAL ORACLE for the EH98 transcription.
   Stage 3d claimed "14 alternating signs is not a transcription
   accident". That is TOO STRONG and is withdrawn: a typo can preserve
   oscillatory character while corrupting phase, acoustic scale, damping,
   or the baryon/CDM amplitude ratio. What the internal controls actually
   establish is "not obviously broken", NOT "proven correct". A real
   proof needs CLASS/CAMB, which is not available here. What IS available:
   compare EH98's own derived quantities (z_eq, z_d, sound horizon, k_eq)
   against published cosmological values. That is an EXTERNAL anchor, and
   it is partial -- stated as partial.

B. INDEPENDENT INTEGRATOR PATH.
   W1 and W2 in stage3d are only PARTIALLY independent: they differ in
   the wiggle physics but share the downstream chain
   P(k) -> xi(r) -> delta_bar(r) -> sign counter. So their agreement
   tests the wiggle model, NOT the integrator. Here xi(r) is recomputed
   at several radii by a structurally different method and compared.

C. CONVERGENCE SWEEP over kmin, kmax, nk, rmax (and n_r), which is the
   one item stage3c's own docstring promised and never delivered.
   Kill criterion, pre-registered: if a reasonable refinement changes
   the CROSSING COUNT, the branch is NOT closed. If only R_xi0 moves,
   it is.

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
)
from stage3d_bao_wiggle_signchanges import T_eh_full  # noqa: E402

# baseline numerics, exactly as stage3c/3d used them
K_MIN, K_MAX, N_K, R_MAX, N_R, DAMP = 1e-5, 50.0, 600_000, 400.0, 700, 1.5


# --------------------------------------------------- A: external anchors
def eh98_derived(om=OM0, ob=OB0, h=H_LITTLE, tcmb=TCMB):
    """The intermediate quantities EH98 computes, for comparison with
    published cosmology. Recomputed here rather than returned by
    T_eh_full so this check does not depend on that function's plumbing."""
    omh2, obh2, theta = om * h * h, ob * h * h, tcmb / 2.7
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
    return {"z_eq": z_eq, "z_d": z_d, "s_Mpc": s, "k_eq": k_eq, "R_d": R_d}


# ------------------------------------------------------ shared machinery
def make_pk(tfun, ns=NS, sigma8=SIGMA8):
    def raw(kk):
        return kk**ns * tfun(kk) ** 2

    k = np.logspace(-5.0, 2.5, 400_000)
    w = tophat_w(k * 8.0)
    s2 = np.trapezoid(raw(k) * k * k * w * w, k) / (2.0 * np.pi**2)
    return lambda kk: (sigma8**2 / s2) * raw(kk)


def xi_trapz(pk, r, kmin, kmax, nk, damp):
    """The stage3c method: log-grid trapezoid over k."""
    k = np.logspace(np.log10(kmin), np.log10(kmax), nk)
    pv = pk(k) * np.exp(-((k * damp / 10.0) ** 2))
    out = np.empty_like(r)
    for i, rr in enumerate(r):
        x = k * rr
        sc = np.where(x < 1e-6, 1.0 - x * x / 6.0, np.sin(x) / np.where(x == 0, 1, x))
        out[i] = np.trapezoid(pv * k * k * sc, k) / (2.0 * np.pi**2)
    return out


def xi_simpson_linear(pk, r, kmin, kmax, nk, damp):
    """INDEPENDENT PATH (criticism B): linear k-grid + Simpson's rule,
    integrating k*P(k)*sin(kr) and dividing by r, instead of a log-grid
    trapezoid over P*k^2*sinc. Different grid, different quadrature,
    different algebraic arrangement of the same integral."""
    n = nk if nk % 2 == 1 else nk + 1
    k = np.linspace(kmin, kmax, n)
    pv = pk(k) * np.exp(-((k * damp / 10.0) ** 2))
    h = k[1] - k[0]
    w = np.ones(n)
    w[1:-1:2] = 4.0
    w[2:-1:2] = 2.0
    out = np.empty_like(r)
    for i, rr in enumerate(r):
        integ = pv * k * np.sin(k * rr)
        out[i] = (h / 3.0) * np.dot(w, integ) / (2.0 * np.pi**2 * rr)
    return out


def measure(pk, kmin, kmax, nk, rmax, n_r, damp, xi_fn=xi_trapz):
    r = np.concatenate((np.linspace(0.05, 1.0, 20)[:-1], np.linspace(1.0, rmax, n_r)))
    xi = xi_fn(pk, r, kmin, kmax, nk, damp)
    integ = np.concatenate(
        ([0.0], np.cumsum(0.5 * (xi[1:] * r[1:] ** 2 + xi[:-1] * r[:-1] ** 2) * np.diff(r)))
    )
    db = 3.0 * integ / r**3
    rz = first_zero(r, xi)
    return {
        "n_xi": count_sign_changes(xi),
        "n_db": count_sign_changes(db),
        "R_xi0": None if rz is None else rz / H_LITTLE,
        "R_comp": first_zero(r, db),
    }


def main() -> int:
    print("=" * 78)
    print("A. PARTIAL EXTERNAL ORACLE -- EH98 derived quantities vs published")
    print("=" * 78)
    d = eh98_derived()
    print("""  WITHDRAWN from stage3d: "14 alternating signs is not a transcription
  accident". Too strong -- a typo can keep the oscillation while moving
  the phase, acoustic scale, damping or baryon/CDM ratio. The honest
  status of the internal controls is NOT OBVIOUSLY BROKEN, not PROVEN.
  No CLASS/CAMB here, so this is a PARTIAL oracle: EH98's own derived
  quantities against standard published values.\n""")
    ref = {
        "z_eq": (3400.0, "matter-radiation equality, Planck-like"),
        "z_d": (1060.0, "drag epoch, Planck-like"),
        "s_Mpc": (147.1, "sound horizon r_d; EH98's FIT is known to run ~2-3% high"),
    }
    ok = True
    for key, (val, note) in ref.items():
        got = d[key]
        dev = 100.0 * (got - val) / val
        flag = "OK" if abs(dev) < 6.0 else "OFF"
        if abs(dev) >= 6.0:
            ok = False
        print(f"  {key:8s} computed {got:10.3f}   published ~{val:8.1f}   {dev:+6.2f}%  {flag}")
        print(f"           ({note})")
    print(f"  k_eq = {d['k_eq']:.5f} Mpc^-1, R_d = {d['R_d']:.4f}")
    print(f"\n  PARTIAL ORACLE: {'consistent' if ok else 'INCONSISTENT -- transcription suspect'}")
    print("  This anchors the acoustic scale and epochs. It does NOT verify")
    print("  alpha_c, beta_c, alpha_b, beta_b, beta_node or the Silk term.")

    pk_w = make_pk(T_eh_full)
    pk_s = make_pk(T_eh_nowiggle)

    print("\n" + "=" * 78)
    print("B. INDEPENDENT INTEGRATOR -- log-trapezoid vs linear-Simpson")
    print("=" * 78)
    print("  Criticism accepted: stage3d's W1/W2 share the downstream chain,")
    print("  so their agreement tests the WIGGLE MODEL, not the integrator.\n")
    rtest = np.array([10.0, 50.0, 100.0, 150.0, 200.0])
    a = xi_trapz(pk_w, rtest, K_MIN, K_MAX, 200_000, DAMP)
    b = xi_simpson_linear(pk_w, rtest, 1e-4, 10.0, 200_001, DAMP)
    print(f"  {'r [Mpc/h]':>10} {'log-trapz':>14} {'lin-Simpson':>14} {'rel diff':>11}")
    worst = 0.0
    for i, rr in enumerate(rtest):
        rel = abs(a[i] - b[i]) / max(abs(a[i]), 1e-300)
        worst = max(worst, rel)
        print(f"  {rr:10.1f} {a[i]:+14.6e} {b[i]:+14.6e} {rel:11.2e}")
    print(f"\n  worst relative difference: {worst:.3e}")
    print("  (the two use different k-ranges too, so exact agreement is not")
    print("   expected -- what matters is that they agree on SIGN and order)")
    signs_match = all(np.sign(a[i]) == np.sign(b[i]) for i in range(len(rtest)))
    print(f"  signs agree at every test radius: {signs_match}")

    print("\n" + "=" * 78)
    print("C. CONVERGENCE SWEEP -- the item stage3c promised and never ran")
    print("=" * 78)
    print("  KILL CRITERION, pre-registered: if a reasonable refinement changes")
    print("  the CROSSING COUNT, the branch is NOT closed. If only R_xi0 moves,")
    print("  it is.\n")
    configs = [("BASELINE", K_MIN, K_MAX, N_K, R_MAX, N_R)]
    for f in (0.1, 10.0):
        configs.append((f"kmin x{f:g}", K_MIN * f, K_MAX, N_K, R_MAX, N_R))
    for f in (0.5, 2.0):
        configs.append((f"kmax x{f:g}", K_MIN, K_MAX * f, N_K, R_MAX, N_R))
    for f in (0.5, 2.0):
        configs.append((f"nk   x{f:g}", K_MIN, K_MAX, int(N_K * f), R_MAX, N_R))
    for f in (0.5, 2.0):
        configs.append((f"rmax x{f:g}", K_MIN, K_MAX, N_K, R_MAX * f, N_R))
    for f in (0.5, 2.0):
        configs.append((f"n_r  x{f:g}", K_MIN, K_MAX, N_K, R_MAX, int(N_R * f)))
    configs.append(
        ("WORST coarse", K_MIN * 10, K_MAX * 0.5, int(N_K * 0.5), R_MAX * 0.5, int(N_R * 0.5))
    )
    configs.append(("WORST fine", K_MIN * 0.1, K_MAX * 2, int(N_K * 2), R_MAX * 2, int(N_R * 2)))

    for label, pk in ((" WIGGLE (W1)", pk_w), (" SMOOTH", pk_s)):
        print(f"\n  --- {label} ---")
        print(
            f"  {'config':>14} {'#sign(xi)':>10} {'#sign(db)':>10} {'R_xi0[Mpc]':>12} {'R_comp':>8}"
        )
        counts = []
        for name, kmn, kmx, nk, rmx, nr in configs:
            m = measure(pk, kmn, kmx, nk, rmx, nr, DAMP)
            counts.append((m["n_xi"], m["n_db"]))
            rx = "none" if m["R_xi0"] is None else f"{m['R_xi0']:.1f}"
            rc = "NONE" if m["R_comp"] is None else f"{m['R_comp']:.1f}"
            print(f"  {name:>14} {m['n_xi']:>10} {m['n_db']:>10} {rx:>12} {rc:>8}")
        uniq = set(counts)
        print(f"\n  distinct (n_xi, n_db) across {len(configs)} configs: {sorted(uniq)}")
        print(f"  COUNT STABLE: {len(uniq) == 1}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
