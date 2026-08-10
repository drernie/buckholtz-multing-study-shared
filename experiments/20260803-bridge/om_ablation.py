"""P4: Omega_m ablation of the MULTING fit, done through the WHOLE chain.

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
2026-08-10 · plan item P4.

WHY THIS RUN, AND WHY THIS WAY. The archive's multing_core.py embeds Planck
Om = 0.315 inside T(z), Mgas(z), rho_crit(z) (hence R(z)) and the accretion
term's H_LCDM -- so "MULTING vs LCDM" comparisons carry a hidden architectural
dependence MULTING <- Planck E(z). An earlier attempt at exactly this ablation
returned a null effect that was an ARTEFACT: `def Efun(z, Om=Om_planck)` binds
the default AT DEFINITION TIME, so mutating the module attribute changed
nothing (caught by a manipulation check, recorded 2026-08-10). The fix here is
textual: the module SOURCE is rewritten with the new Om before exec, so every
default argument, module constant and closure sees the new value. A
manipulation check (Efun(1) must move with Om) is run per point before any
fit is trusted.

CONTROL. At Om = 0.315 the driver must reproduce the archive's own
unconstrained fit: H0 = 73.2160, chi2_33 = 15.7515, r_33 = 0.9659. If it does
not, the driver -- not the physics -- is wrong, and nothing else is reported.
"""

import sys
from pathlib import Path

import numpy as np
import yaml
from scipy.optimize import minimize
from scipy.stats import pearsonr

ARCH = Path(
    "C:/Users/serge/AppData/Local/Temp/claude/"
    "E-------------------------------------------------H---11-Dr--Thomas-J--Buckholtz/"
    "8db666d8-df59-4a3e-a644-a80e028bf583/scratchpad/tjb_repro/archive/code"
)

Z_SHOES, H_SHOES, SIG_SHOES = 0.0233, 73.04, 1.04
Z_DESI, H_DESI, SIG_DESI = 2.33, 236.1, 2.8


def load_core(om: float) -> dict:
    """Exec multing_core.py with Om_planck textually replaced (flat: OL = 1-Om)."""
    src = open(ARCH / "multing_core.py", encoding="utf-8").read()
    src = src.replace("Om_planck = 0.315", f"Om_planck = {om!r}")
    src = src.replace("OL_planck = 0.685", f"OL_planck = {1.0 - om!r}")
    ns: dict = {}
    exec(compile(src, "multing_core_ablated.py", "exec"), ns)  # noqa: S102
    return ns


def fit_unconstrained(core: dict, zd, Hd, sd):
    z33 = np.concatenate([zd, [Z_SHOES], [Z_DESI]])
    H33 = np.concatenate([Hd, [H_SHOES], [H_DESI]])
    s33 = np.concatenate([sd, [SIG_SHOES], [SIG_DESI]])
    zfine = np.sort(np.unique(np.concatenate([np.linspace(0, Z_DESI, 500), z33])))
    H_of = core["H_of_z_kms"]

    def chi2(p):
        H0a, b1, b2 = p
        if H0a <= 0 or b1 < 0 or b2 < 0:
            return 1e12
        Hm = H_of(zfine, H0a, b1, b2, Z_SHOES)
        if np.any(np.isnan(Hm)):
            return 1e12
        return float(np.sum(((np.interp(z33, zfine, Hm) - H33) / s33) ** 2))

    r = minimize(
        chi2,
        [73.2, 1.4e10, 7.6e17],
        method="Nelder-Mead",
        options={"xatol": 1e-4, "fatol": 1e-9, "maxiter": 20000, "maxfev": 20000},
    )
    H0f, b1f, b2f = r.x
    Hm = H_of(zfine, H0f, b1f, b2f, Z_SHOES)
    rp = pearsonr(np.interp(z33, zfine, Hm), H33)[0]
    return H0f, b1f, b2f, float(r.fun), float(rp)


def main() -> None:
    print("=" * 88)
    print("P4 -- Omega_m ABLATION through the full chain T->Mgas->k->R->F->H(z)")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION  |  L0: descriptive")
    print("=" * 88)

    sys.path.insert(0, str(ARCH))
    with open(ARCH / "assumptions.yaml") as f:
        pts = yaml.safe_load(f)["cosmic_chronometer_data"]["points"]
    zd = np.array([p[0] for p in pts])
    Hd = np.array([p[1] for p in pts])
    sd = np.array([p[2] for p in pts])

    # manipulation check + control at the archive's own value
    e_ref = load_core(0.315)["Efun"](1.0)
    e_low = load_core(0.20)["Efun"](1.0)
    print(f"\n[MANIPULATION CHECK] Efun(1): Om=0.315 -> {e_ref:.4f}, Om=0.20 -> {e_low:.4f}")
    if abs(e_ref - e_low) < 1e-6:
        print("  *** ablation did not reach Efun -- same failure as before. STOP. ***")
        return
    print("  -> the replacement propagates (the earlier default-arg failure is closed).")

    print(f"\n  {'Om':>6}{'H0_anchor':>11}{'beta_1':>13}{'beta_2':>13}{'chi2_33':>10}{'r_33':>9}")
    rows = []
    for om in (0.20, 0.25, 0.30, 0.315, 0.35, 0.40):
        core = load_core(om)
        H0f, b1, b2, c2, rp = fit_unconstrained(core, zd, Hd, sd)
        rows.append((om, H0f, b1, b2, c2, rp))
        mark = "   <- CONTROL (paper: 73.2160 / 15.7515 / 0.9659)" if om == 0.315 else ""
        print(f"  {om:>6.3f}{H0f:>11.4f}{b1:>13.4e}{b2:>13.4e}{c2:>10.4f}{rp:>9.4f}{mark}")

    om0 = next(r for r in rows if r[0] == 0.315)
    ok = abs(om0[1] - 73.2160) < 0.02 and abs(om0[4] - 15.7515) < 0.05
    print(f"\n  control reproduced: {ok}")
    if not ok:
        print("  *** driver does not reproduce the archive at Om=0.315 -- results void. ***")
        return

    lo, hi = rows[0], rows[-1]
    print("\n[SENSITIVITIES]  finite differences across the scanned range 0.20 -> 0.40")
    for i, (nm, scale) in enumerate(
        (("H0_anchor", 1.0), ("beta_1", None), ("beta_2", None), ("chi2_33", 1.0)), start=1
    ):
        d = (hi[i] - lo[i]) / (hi[0] - lo[0])
        if scale is None:  # log-derivative for the betas
            d = (np.log(hi[i]) - np.log(lo[i])) / (hi[0] - lo[0])
            print(f"  d ln({nm})/d Om = {d:+.3f}")
        else:
            print(f"  d {nm}/d Om     = {d:+.3f}")
    print("\n  Reading: if the betas move by O(1) in the log across a plausible Om range,")
    print("  the fitted beta values are properties of (data + assumed LCDM inputs), not")
    print("  of the data alone -- quantifying the reviewer's 'hidden architecture' point.")


if __name__ == "__main__":
    main()
