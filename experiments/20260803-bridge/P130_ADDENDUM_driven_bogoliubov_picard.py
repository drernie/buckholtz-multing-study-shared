"""P130 ADDENDUM -- does the psi<->dph coupling this file's own "not attempted
here" WKB/adiabatic-invariant step ignores actually matter for the resonant
amplitude, and does a Picard iteration on it converge?

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

WHY THIS FILE. FINDING_P130's own dphdd equation (P119_ln_a_state_
reformulation.py's make_system_lna) is a damped, driven oscillator:
    dphdd + 3H*dphd + (kk^2*exp(-2N)+Vpp)*dph = source(psi,psid,drA_hat,pd)
Removing the 3H*dphd friction term via the field redefinition u=a^1.5*dph
(standard for a canonical perturbation in an FRW-like background) turns this
into u''+Omega^2(t)*u=F(t), Omega^2=omega_k^2-(9/4)H^2-(3/2)Hdot -- a form a
driven-Bogoliubov / Green's-function treatment applies to directly. This
file numerically tests whether the psi-sourced part (F) is negligible for
the resonance (a pointwise |F| vs |Omega^2*u| check earlier suggested ~1e-6,
misleadingly small -- see Addendum text in the .md for why) via a genuine
2-step Picard iteration on the real, already-verified P130/P119 trajectory.

Background (lna,pb,pd,H,Hdot) is CLOSED under make_system_lna's own
equations -- never sourced by psi/dph/drA_hat/qm_hat (standard: no
backreaction on the background at linear order) -- so it is read as REAL,
exact, from the already-solved 9-dim trajectory at every iteration. Only
the psi<->dph coupling is iterated.

CONTROLS (both run before any iterate is trusted):
  REGRESSION 1 (u-equation): solving u''+Omega^2*u=F(t) with F(t) built
    from the TRUE psi(t) must reproduce a(t)^1.5*dph(t) from the original
    9-dim solve almost exactly -- confirms Omega^2/F are derived correctly.
  REGRESSION 2 (psi-sector): solving the psi-sector sub-system
    [psi,psid,drA_hat,qm_hat] sourced by the TRUE dph(t),dphd(t) must
    reproduce the true psi(t) almost exactly -- confirms the psi-sector
    formulas (copied verbatim from make_system_lna) are correct too.

Iterate 0: dph^(0)(t) = solve u''+Omega^2*u=0 (F=0), real IC at N=9.
Iterate 1: psi-sector sourced by dph^(0),dphd^(0) -> F^(1) -> dph^(1)(t).
Iterate 2: psi-sector sourced by dph^(1),dphd^(1) -> F^(2) -> dph^(2)(t).
Reports step0->1, step1->2 (at each k's own psi-peak, P130's own reported
N=13.455/13.620) and the error of iterate 1 and 2 against the true value --
does the second Picard step shrink relative to the first (convergence)?
"""

import importlib.util
import os
import sys
from functools import partial

import numpy as np
from scipy.integrate import solve_ivp

HERE = os.path.dirname(os.path.abspath(__file__))


def _load(stem, alias):
    spec = importlib.util.spec_from_file_location(alias, os.path.join(HERE, stem))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[alias] = mod
    spec.loader.exec_module(mod)
    return mod


p130 = _load("P130_matter_lambda_resonance_characterization.py", "p130_for_addendum")
p119 = p130.p119
C_MATTER = p130.C_MATTER
LAMBDA_FIXED = p130.LAMBDA_FIXED
G_N = p119.G_N
T_END = p130.T_END
PHIDOT_INIT = p130.PHIDOT_INIT

GH, LAM = 1.0, 1.0
IC0 = {"phidot0": 0.1 * PHIDOT_INIT}
PSI_PEAK_N = {0.3: 13.4537, 0.5: 13.6188}  # cross-checked against P130's own 13.455/13.620


def background(t, sol):
    """REAL background quantities at t -- unaffected by any iteration."""
    lna, pb, pd, _psi, _psid, _dph, _dphd, _drA, _qm = sol.sol(t)
    rho_A = C_MATTER * np.exp(-3.0 * lna)
    rho_phys = rho_A * (1.0 - GH * pb)
    V = LAM * pb**4 / 4.0 + LAMBDA_FIXED
    H = np.sqrt(max((8.0 * np.pi * G_N / 3.0) * (rho_phys + pd**2 / 2.0 + V), 0.0))
    Vp = LAM * pb**3
    Vpp = 3.0 * LAM * pb**2
    Hdot = -4.0 * np.pi * G_N * (rho_phys + pd**2)
    return {
        "lna": lna,
        "pb": pb,
        "pd": pd,
        "rho_A": rho_A,
        "H": H,
        "Vp": Vp,
        "Vpp": Vpp,
        "Hdot": Hdot,
        "a": np.exp(lna),
    }


def omega2(t, sol, kk):
    b = background(t, sol)
    omega_k2 = kk**2 * np.exp(-2.0 * b["lna"]) + b["Vpp"]
    return omega_k2 - (9.0 / 4.0) * b["H"] ** 2 - (3.0 / 2.0) * b["Hdot"], b


def psi_sector_rhs(t, y, sol, kk, dph_f, dphd_f):
    """[psi,psid,drA_hat,qm_hat] sourced by EXTERNAL dph_f(t),dphd_f(t)."""
    psi, psid, drA_hat, qm_hat = y
    b = background(t, sol)
    pb, pd, H, Hdot, Vp = b["pb"], b["pd"], b["H"], b["Hdot"], b["Vp"]
    dph_t, dphd_t = dph_f(t), dphd_f(t)

    dp_phi = pd * dphd_t - psi * pd**2 - Vp * dph_t
    psidd = 4 * np.pi * G_N * dp_phi - 4 * H * psid - (2 * Hdot + 3 * H**2) * psi
    drA_hat_d = 3 * psid * C_MATTER + kk**2 * qm_hat * np.exp(-2.0 * b["lna"]) / (1 - GH * pb)
    qm_hat_d = C_MATTER * (GH * dph_t - (1 - GH * pb) * psi)
    return [psid, psidd, drA_hat_d, qm_hat_d]


def u_rhs(t, y, sol, kk, F_f):
    u, up = y
    Om2, _ = omega2(t, sol, kk)
    return [up, F_f(t) - Om2 * u]


def F_from_psi_sector(t, sol, psi_sol):
    b = background(t, sol)
    psi, psid, drA_hat, _qm = psi_sol.sol(t)
    drA_for_dphdd = drA_hat * np.exp(-3.0 * b["lna"])
    source = GH * drA_for_dphdd + 2.0 * psi * (GH * b["rho_A"] - b["Vp"]) + 4.0 * psid * b["pd"]
    return b["a"] ** 1.5 * source


def dph_and_dphd_from_u(t, sol, u_sol):
    b = background(t, sol)
    u, up = u_sol.sol(t)
    return u / b["a"] ** 1.5, (up - 1.5 * b["H"] * u) / b["a"] ** 1.5


def main() -> None:
    print("=" * 78)
    print("P130 ADDENDUM -- driven-Bogoliubov / Picard convergence on the real psi<->dph coupling")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    for kk in (0.3, 0.5):
        print(f"\n{'=' * 70}\nk = {kk}\n{'=' * 70}")
        sol = p119.run_lna(GH, LAM, kk, T_END, lam_cc=LAMBDA_FIXED, **IC0)
        assert sol is not None and sol.success

        t_lo = p119.t_of_lna(sol, 9.0, 1.0, T_END)
        t_hi = p119.t_of_lna(sol, 18.0, 1.0, T_END)
        t_peak = p119.t_of_lna(sol, PSI_PEAK_N[kk], 1.0, T_END)
        assert t_lo is not None and t_hi is not None and t_peak is not None

        lna0, pb0, pd0, psi0, psid0, dph0, dphd0, drA0, qm0 = sol.sol(t_lo)
        _, b0 = omega2(t_lo, sol, kk)
        u0 = b0["a"] ** 1.5 * dph0
        up0 = 1.5 * b0["a"] ** 1.5 * b0["H"] * dph0 + b0["a"] ** 1.5 * dphd0
        psi_ic = [psi0, psid0, drA0, qm0]

        # --- REGRESSION 1: true psi -> u-equation should reproduce true dph ---
        sol_u_true = solve_ivp(
            u_rhs,
            (t_lo, t_hi),
            [u0, up0],
            args=(sol, kk, lambda t, sol=sol: F_from_psi_sector(t, sol, _TrueAsPsiSol(sol))),
            rtol=1e-10,
            atol=1e-30,
            dense_output=True,
        )
        assert sol_u_true.success
        real_u_peak = background(t_peak, sol)["a"] ** 1.5 * sol.sol(t_peak)[5]
        reg1 = abs(sol_u_true.sol(t_peak)[0] - real_u_peak) / abs(real_u_peak)
        print(
            f"  REGRESSION 1 (u-eq, fed true psi): |u_reg-u_true|/|u_true| at psi-peak = {reg1:.3e}"
        )

        # --- REGRESSION 2: true dph -> psi-sector should reproduce true psi ---
        true_dph = lambda t, sol=sol: sol.sol(t)[5]  # noqa: E731
        true_dphd = lambda t, sol=sol: sol.sol(t)[6]  # noqa: E731
        sol_psi_reg = solve_ivp(
            psi_sector_rhs,
            (t_lo, t_hi),
            psi_ic,
            args=(sol, kk, true_dph, true_dphd),
            rtol=1e-10,
            atol=1e-30,
            dense_output=True,
        )
        assert sol_psi_reg.success
        reg2 = abs(sol_psi_reg.sol(t_peak)[0] - sol.sol(t_peak)[3]) / abs(sol.sol(t_peak)[3])
        print(
            f"  REGRESSION 2 (psi-sector, fed true dph): |psi_reg-psi_true|/|psi_true| = {reg2:.3e}"
        )

        # --- iterate 0: u_hom (F=0) ---
        sol_u0 = solve_ivp(
            u_rhs,
            (t_lo, t_hi),
            [u0, up0],
            args=(sol, kk, lambda t: 0.0),
            rtol=1e-10,
            atol=1e-30,
            dense_output=True,
        )
        assert sol_u0.success
        dph0_f = partial(lambda t, s, sol=sol: dph_and_dphd_from_u(t, sol, s)[0], s=sol_u0)
        dphd0_f = partial(lambda t, s, sol=sol: dph_and_dphd_from_u(t, sol, s)[1], s=sol_u0)

        # --- iterate 1 ---
        sol_psi1 = solve_ivp(
            psi_sector_rhs,
            (t_lo, t_hi),
            psi_ic,
            args=(sol, kk, dph0_f, dphd0_f),
            rtol=1e-10,
            atol=1e-30,
            dense_output=True,
        )
        assert sol_psi1.success
        sol_u1 = solve_ivp(
            u_rhs,
            (t_lo, t_hi),
            [u0, up0],
            args=(sol, kk, lambda t, sol=sol, sp1=sol_psi1: F_from_psi_sector(t, sol, sp1)),
            rtol=1e-10,
            atol=1e-30,
            dense_output=True,
        )
        assert sol_u1.success
        dph1_f = partial(lambda t, s, sol=sol: dph_and_dphd_from_u(t, sol, s)[0], s=sol_u1)
        dphd1_f = partial(lambda t, s, sol=sol: dph_and_dphd_from_u(t, sol, s)[1], s=sol_u1)

        # --- iterate 2 ---
        sol_psi2 = solve_ivp(
            psi_sector_rhs,
            (t_lo, t_hi),
            psi_ic,
            args=(sol, kk, dph1_f, dphd1_f),
            rtol=1e-10,
            atol=1e-30,
            dense_output=True,
        )
        assert sol_psi2.success
        sol_u2 = solve_ivp(
            u_rhs,
            (t_lo, t_hi),
            [u0, up0],
            args=(sol, kk, lambda t, sol=sol, sp2=sol_psi2: F_from_psi_sector(t, sol, sp2)),
            rtol=1e-10,
            atol=1e-30,
            dense_output=True,
        )
        assert sol_u2.success

        u0_peak = sol_u0.sol(t_peak)[0]
        u1_peak = sol_u1.sol(t_peak)[0]
        u2_peak = sol_u2.sol(t_peak)[0]

        step01 = abs(u1_peak - u0_peak) / abs(u0_peak)
        step12 = abs(u2_peak - u1_peak) / abs(u1_peak)
        err1 = abs(u1_peak - real_u_peak) / abs(real_u_peak)
        err2 = abs(u2_peak - real_u_peak) / abs(real_u_peak)

        print(f"\n  at psi-peak (N={PSI_PEAK_N[kk]}):")
        print(f"    u^(0) (F=0)           = {u0_peak:.6e}")
        print(f"    u^(1) (1st Picard it) = {u1_peak:.6e}")
        print(f"    u^(2) (2nd Picard it) = {u2_peak:.6e}")
        print(f"    u_true (exact, real)  = {real_u_peak:.6e}")
        print(f"\n    step 0->1: |u1-u0|/|u0| = {step01:.4e}")
        print(f"    step 1->2: |u2-u1|/|u1| = {step12:.4e}")
        print(
            f"    ratio (step1->2/step0->1) = {step12 / step01:.4e}  (geometric convergence if << 1)"
        )
        print(f"    |u1-u_true|/|u_true| = {err1:.4e}")
        print(f"    |u2-u_true|/|u_true| = {err2:.4e}")


class _TrueAsPsiSol:
    """Adapter so F_from_psi_sector can read the TRUE psi/psid/drA_hat via
    the same .sol(t) interface as a solve_ivp result, for REGRESSION 1."""

    def __init__(self, sol):
        self._sol = sol

    def sol(self, t):
        state = self._sol.sol(t)
        return [state[3], state[4], state[7], state[8]]  # psi, psid, drA_hat, qm_hat


if __name__ == "__main__":
    main()
