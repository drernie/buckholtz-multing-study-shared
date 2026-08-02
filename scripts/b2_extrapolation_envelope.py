"""B-2 — envelope of statistically equivalent continuations into z < 0.

The headline claim rests on a +39% separation at z = -0.2. This asks the
only question that matters for that claim:

    Among ALL functional forms that fit the CC data equally well,
    how wide is the spread of H(-0.2)?

If the spread is wide, +39% is a property of the CHOSEN functional form,
not a consequence of the data. That is a much stronger statement than
"extrapolations are sometimes unstable".

Families fitted to the same 31 CC points, then continued to z = -0.2:
  1. flat LCDM                H0*sqrt(Om(1+z)^3 + 1-Om)
  2. CPL / w0-wa dark energy
  3. MULTING-like polynomial  A(1+z)^2 + B(1+z)^3 + C(1+z)^4
  4. quadratic in x = z/(1+z) (compactified, well-behaved)
  5. Pade [1/1] in z
  6. cubic polynomial in z

Acceptance: any fit with chi2 <= chi2_min + Delta (Delta = 2.30 for 2 params
at 1 sigma joint, and we also report the looser Delta = 6.17 / 2 sigma).

Safety: NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION
L0: descriptive.
"""

from __future__ import annotations

import re
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

REPO = Path(
    r"E:\Проверка Гипотез\работаю над проверкой гипотез"
    r"\H - 11 Dr. Thomas J. Buckholtz\buckholtz-idm-multing-mvp"
)
ZFUT = -0.20


def tjb31():
    csv = pd.read_csv(REPO / "data" / "hz_cc.csv", comment="#")
    csv = csv[["z", "Hz_km_s_Mpc", "sigma_Hz"]].to_numpy(float)
    src = (REPO / "code" / "beta_cv.py").read_text(encoding="utf-8")

    def arr(n):
        blk = re.search(n + r" = np.array\(\s*\[(.*?)\]", src, re.S).group(1)
        return [float(x) for x in re.findall(r"[\d.]+", blk)]

    bz, bh, bs = arr("z_obs"), arr("H_obs"), arr("sigma_obs")
    extra = [
        (z, h, s)
        for z, h, s in zip(bz, bh, bs, strict=False)
        if z in (0.4004, 0.4247, 0.4497, 0.47, 0.4783)
    ]
    d = np.array([r for r in csv if abs(r[0] - 0.75) > 1e-9] + extra)
    return d[np.argsort(d[:, 0])]


# ---- families ----
def f_lcdm(z, h0, om):
    return h0 * np.sqrt(np.clip(om * (1 + z) ** 3 + (1 - om), 1e-9, None))


def f_cpl(z, h0, om, w0, wa):
    a = 1.0 / (1.0 + z)
    de = (1 - om) * (1 + z) ** (3 * (1 + w0 + wa)) * np.exp(-3 * wa * (1 - a))
    return h0 * np.sqrt(np.clip(om * (1 + z) ** 3 + de, 1e-9, None))


def f_mult(z, a, b, c):
    x = 1 + z
    return a * x**2 + b * x**3 + c * x**4


def f_xpoly(z, a, b, c):
    x = z / (1 + z)
    return a + b * x + c * x**2


def f_pade(z, a, b, c):
    return (a + b * z) / (1 + c * z)


def f_cubic(z, a, b, c, d):
    return a + b * z + c * z**2 + d * z**3


FAMILIES = [
    ("flat LCDM", f_lcdm, [70.0, 0.3], 2),
    ("CPL w0-wa", f_cpl, [70.0, 0.3, -1.0, 0.0], 4),
    ("MULTING poly (1+z)^2,3,4", f_mult, [50.0, -10.0, 5.0], 3),
    ("quadratic in x=z/(1+z)", f_xpoly, [70.0, 50.0, 50.0], 3),
    ("Pade [1/1]", f_pade, [70.0, 60.0, 0.2], 3),
    ("cubic in z", f_cubic, [70.0, 50.0, 10.0, 0.0], 4),
]


def main():
    d = tjb31()
    z, H, S = d[:, 0], d[:, 1], d[:, 2]
    print("=" * 76)
    print("B-2 ENVELOPE OF EQUIVALENT CONTINUATIONS INTO z < 0")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION  |  L0: descriptive")
    print("=" * 76)
    print(f"\nfitted to n={len(z)} CC points, z in [{z.min():.3f}, {z.max():.3f}]")
    print(f"extrapolation target: z = {ZFUT}\n")

    res = []
    for name, fn, p0, k in FAMILIES:
        try:
            p, _ = curve_fit(fn, z, H, sigma=S, absolute_sigma=True, p0=p0, maxfev=200000)
            chi2 = float(np.sum(((H - fn(z, *p)) / S) ** 2))
            h_now = float(fn(np.array([0.0]), *p)[0])
            h_fut = float(fn(np.array([ZFUT]), *p)[0])
            res.append((name, k, chi2, h_now, h_fut))
        except Exception as e:  # noqa: BLE001
            print(f"  {name}: FIT FAILED ({type(e).__name__})")

    chi2min = min(r[2] for r in res)
    print(f"  {'family':28s} {'k':>2} {'chi2':>8} {'dchi2':>7} {'H(0)':>8} {'H(-0.2)':>9}")
    for name, k, chi2, hn, hf in sorted(res, key=lambda r: r[2]):
        print(f"  {name:28s} {k:2d} {chi2:8.2f} {chi2 - chi2min:7.2f} {hn:8.2f} {hf:9.2f}")

    for delta, lab in ((2.30, "1 sigma (dchi2<=2.30)"), (6.17, "2 sigma (dchi2<=6.17)")):
        ok = [r for r in res if r[2] - chi2min <= delta]
        if not ok:
            continue
        futs = [r[4] for r in ok]
        print(f"\n  [{lab}] {len(ok)} families acceptable")
        print(
            f"    H(-0.2) range = [{min(futs):.1f}, {max(futs):.1f}]  "
            f"spread = {max(futs) - min(futs):.1f} km/s/Mpc"
        )
        base = f_lcdm(
            np.array([ZFUT]),
            *curve_fit(f_lcdm, z, H, sigma=S, absolute_sigma=True, p0=[70.0, 0.3])[0],
        )[0]
        print(f"    LCDM reference at z=-0.2: {base:.1f}")
        print(f"    spread as % of LCDM ref  : {100 * (max(futs) - min(futs)) / base:.1f}%")
        print(
            f"    max deviation from LCDM  : {100 * max(abs(f - base) for f in futs) / base:+.1f}%"
        )

    print("\n" + "-" * 76)
    print("READING")
    ok1 = [r for r in res if r[2] - chi2min <= 2.30]
    if ok1:
        futs = [r[4] for r in ok1]
        base = float(
            f_lcdm(
                np.array([ZFUT]),
                *curve_fit(f_lcdm, z, H, sigma=S, absolute_sigma=True, p0=[70.0, 0.3])[0],
            )[0]
        )
        span = 100 * (max(futs) - min(futs)) / base
        print(f"  Statistically equivalent fits span {span:.0f}% at z=-0.2.")
        print("  The digitized MULTING curve sits ~+39% above LCDM there.")
        if span >= 39:
            print("  -> a +39% offset is INSIDE the spread the data already permit:")
            print("     it is a property of the chosen functional form, not of the data.")
        else:
            print("  -> +39% EXCEEDS what equivalent fits produce; the offset is not")
            print("     generic to extrapolation and needs its own justification.")
    print("-" * 76)


if __name__ == "__main__":
    main()
