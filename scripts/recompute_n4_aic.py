"""Recompute N-4 from scratch: AIC/BIC of LCDM vs MULTING-style polynomials
on real Moresco+2022 CC H(z) (data/hz_cc.csv, 27 points). Prints proof.
NOT_VALIDATION · OUR_RECONSTRUCTION.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

HERE = Path(__file__).resolve().parent.parent
df = pd.read_csv(HERE / "data" / "hz_cc.csv")
z = df["z"].to_numpy(float)
H = df["Hz_km_s_Mpc"].to_numpy(float)
sig = df["sigma_Hz"].to_numpy(float)
n = len(z)
x = 1.0 + z


def chi2(pred):
    return float(np.sum(((H - pred) / sig) ** 2))


def aic_bic(c2, k):
    aic = c2 + 2 * k
    bic = c2 + k * math.log(n)
    aicc = aic + (2 * k * (k + 1)) / (n - k - 1) if n - k - 1 > 0 else float("nan")
    return aic, bic, aicc


def lcdm(zz, H0, Om):
    return H0 * np.sqrt(Om * (1 + zz) ** 3 + (1 - Om))


def make_poly(powers):
    def f(zz, *c):
        xx = 1.0 + zz
        s = sum(ci * xx**p for ci, p in zip(c, powers, strict=True))
        return np.sqrt(np.clip(s, 1e-9, None))

    return f


models = {}

# LCDM (2 params: H0, Om) — the [0,3] structure
p, _ = curve_fit(lcdm, z, H, p0=[70, 0.3], sigma=sig, absolute_sigma=True, maxfev=100000)
models["LCDM (H0,Om) k=2"] = (chi2(lcdm(z, *p)), 2, {"H0": p[0], "Om": p[1]})

# MULTING-style polynomials in H^2 = sum c_n (1+z)^n
for label, powers in {
    "MULTING [2,3,4] k=3": (2, 3, 4),
    "MULTING [2,3] k=2": (2, 3),
    "poly [0,3] k=2": (0, 3),
    "poly [0,2,3,4] k=4": (0, 2, 3, 4),
}.items():
    f = make_poly(powers)
    p0 = [4000.0] * len(powers)
    try:
        pp, _ = curve_fit(f, z, H, p0=p0, sigma=sig, absolute_sigma=True, maxfev=200000)
        models[label] = (
            chi2(f(z, *pp)),
            len(powers),
            {f"c{n_}": float(v) for n_, v in zip(powers, pp, strict=True)},
        )
    except Exception as e:  # noqa: BLE001
        models[label] = (float("nan"), len(powers), {"error": str(e)})

print(f"N = {n} CC points (Moresco+2022, arXiv:2201.07241)\n")
print(f"{'model':<24}{'chi2':>9}{'k':>3}{'AIC':>9}{'BIC':>9}{'AICc':>9}")
rows = {}
for name, (c2, k, _params) in models.items():
    aic, bic, aicc = aic_bic(c2, k)
    rows[name] = aic
    print(f"{name:<24}{c2:>9.2f}{k:>3}{aic:>9.2f}{bic:>9.2f}{aicc:>9.2f}")

lcdm_aic = rows["LCDM (H0,Om) k=2"]
mult_aic = rows["MULTING [2,3,4] k=3"]
print()
print("=== N-4 verdict (recomputed from scratch) ===")
print(f"AIC(LCDM)            = {lcdm_aic:.2f}")
print(f"AIC(MULTING[2,3,4])  = {mult_aic:.2f}")
print(f"dAIC = AIC(MULT) - AIC(LCDM) = {mult_aic - lcdm_aic:+.2f}")
print("(claimed in report: LCDM 16.8, MULTING 19.3, dAIC +3.0)")

out = HERE / "reports" / "n4_aic_recompute.json"
out.write_text(
    json.dumps(
        {
            "data": "Moresco+2022 CC H(z), data/hz_cc.csv",
            "n": n,
            "models": {
                k: {"chi2": v[0], "k": v[1], "AIC": aic_bic(v[0], v[1])[0], "params": v[2]}
                for k, v in models.items()
            },
            "dAIC_MULT_minus_LCDM": mult_aic - lcdm_aic,
            "labels": ["NOT_VALIDATION", "OUR_RECONSTRUCTION", "VERIFIED-real"],
        },
        indent=2,
    )
)
print(f"\nsaved: {out}")
