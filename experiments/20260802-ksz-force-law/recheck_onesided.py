"""INDEPENDENT re-check of the one-sided upper limit reported by Blind A.

Blind A is an EXTERNAL PROVISIONAL artifact (see blind_a/). Its numbers are not
accepted until reproduced here. This file imports nothing from it and was
written without reading its working scripts.

WHAT OUR EARLIER ATTEMPT GOT WRONG
    It used the TWO-SIDED profile statistic q_mu = chi2(mu) - chi2(mu_hat) to
    build a ONE-SIDED upper limit. The correct object is

        q~_mu = 0                          if mu_hat > mu
              = chi2(mu) - chi2(mu_hat)    if 0 <= mu_hat <= mu

    with mu_hat the CONSTRAINED MLE (argmin over mu >= 0), not an unconstrained
    minimum clipped afterwards. The difference is tested, not assumed.

SPEED
    With the amplitude profiled analytically, chi2 is a RATIONAL function of mu.
    Writing t(mu) = u + mu*v with u = -K2, v = K3:

        chi2(mu) = dCd - (dCu + mu*dCv)^2 / (uCu + 2*mu*uCv + mu^2*vCv)

    uCu, uCv, vCv are data-independent and precomputed once; each simulated
    dataset costs three matrix-vector products, and the whole mu-grid is then
    evaluated in one vectorised numpy expression. Roughly 10^3 faster than
    rescanning the grid per simulation.

GATES, stated before running
    G1 analytic amplitude profiling == direct 2-parameter optimisation
    G2 constrained MLE != unconstrained-then-clipped (tested, not assumed)
    G3 q~ correct in three hand-checked regimes
    G4 threshold calibrated at EACH mu on a dense grid
    G5 nuisance amplitude varied: A_cond, A_cond +- 1 sigma_A
    G6 coverage validated on an INDEPENDENT ensemble, not the calibration one

PASS CRITERION vs Blind A (set in advance)
    weighted endpoint within 0.5 Mpc of 8.00 (stat-only)
    raw      endpoint within 0.5 Mpc of 11.00 (stat-only)
    validation coverage 0.95 within MC error

Safety: NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION
L0: descriptive.
"""

from __future__ import annotations

import json
from pathlib import Path

import h5py
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.optimize import minimize

HERE = Path(__file__).resolve().parent / "artifacts"
H_LITTLE, R_LO, R_HI = 0.677, 6.0, 262.19
EPS_PV = 0.05  # symmetric exclusion around r'=R -> approximates the principal value
RNG = np.random.default_rng(11081987)
MU_GRID = np.arange(0.0, 60.0 + 1e-9, 0.05)  # physical domain mu >= 0


def c3(rho):
    """Geometric factor for a 1/s^3 force; simple antisymmetric pole at rho=1."""
    rho = np.asarray(rho, float)
    out = np.zeros_like(rho)
    ok = np.abs(rho - 1.0) > 1e-14
    r = rho[ok]
    out[ok] = 1.0 / (2.0 * (1.0 - r**2)) + np.log(np.abs((1 + r) / (1 - r))) / (4.0 * r)
    out[rho < 1e-14] = 1.0
    return out


def load():
    d = np.loadtxt(HERE / "xi_zbin2.dat")
    r_xi, xi_v = d[:, 0] / H_LITTLE, d[:, 1]
    spl = CubicSpline(r_xi, xi_v, extrapolate=False)

    def xi(x):
        x = np.atleast_1d(np.asarray(x, float))
        y = spl(np.clip(x, r_xi[0], r_xi[-1]))
        y[(x < r_xi[0]) | (x > r_xi[-1])] = 0.0
        return np.nan_to_num(y)

    with h5py.File(HERE / "dr6.hdf", "r") as f:
        pw = f["df_pw/block0_values"][:]
        cols = [c.decode() for c in f["df_pw/block0_items"][:]]
        cov = f["df_cov/block0_values"][:]
        n_boot = f["bs_curves/block0_values"].shape[0]
    r_all = pw[:, cols.index("r_mp")]
    p_all = pw[:, cols.index("ksz_curve")]
    m = (r_all >= 25) & (r_all <= 225)
    return xi, r_all[m], p_all[m], cov[np.ix_(m, m)], n_boot


def kernels(xi, rvals, weighted, n=120000):
    k2, k3 = [], []
    for R in rvals:
        x = np.linspace(R_LO, R, n // 4)
        i2 = float(np.trapezoid(xi(x) * x**2, x) / R**2)
        x = np.linspace(R_LO, R_HI, n)
        keep = np.abs(x - R) >= EPS_PV
        i3 = float(np.trapezoid(np.where(keep, xi(x) * x**2 * c3(x / R), 0.0), x) / R**3)
        if weighted:
            w = 1.0 / (1.0 + float(xi(R)[0]))
            i2, i3 = i2 * w, i3 * w
        k2.append(i2)
        k3.append(i3)
    return np.array(k2), np.array(k3)


class Model:
    """t(mu) = u + mu*v, amplitude profiled analytically; vectorised over mu."""

    def __init__(self, Ci, k2, k3):
        self.Ci = Ci
        self.u = -k2
        self.v = k3
        self.uCu = float(self.u @ Ci @ self.u)
        self.uCv = float(self.u @ Ci @ self.v)
        self.vCv = float(self.v @ Ci @ self.v)

    def _proj(self, d):
        return (
            float(d @ self.Ci @ d),
            float(d @ self.Ci @ self.u),
            float(d @ self.Ci @ self.v),
        )

    def chi2_grid(self, d, mus=MU_GRID):
        dCd, dCu, dCv = self._proj(d)
        num = (dCu + mus * dCv) ** 2
        den = self.uCu + 2 * mus * self.uCv + mus**2 * self.vCv
        return dCd - num / den

    def chi2_at(self, mu, d):
        dCd, dCu, dCv = self._proj(d)
        return dCd - (dCu + mu * dCv) ** 2 / (self.uCu + 2 * mu * self.uCv + mu**2 * self.vCv)

    def amp(self, mu, d):
        _, dCu, dCv = self._proj(d)
        return (dCu + mu * dCv) / (self.uCu + 2 * mu * self.uCv + mu**2 * self.vCv)

    def q_tilde_grid(self, d):
        """q~ for every mu on MU_GRID, using the CONSTRAINED MLE."""
        ch = self.chi2_grid(d)
        i_hat = int(np.argmin(ch))
        mu_hat, chi_hat = MU_GRID[i_hat], ch[i_hat]
        q = ch - chi_hat
        q[MU_GRID < mu_hat] = 0.0  # q~ = 0 where mu < mu_hat
        return q, float(mu_hat)


def main():
    xi, r, d_obs, C, n_boot = load()
    p_dim = len(r)
    hartlap = (n_boot - p_dim - 2) / (n_boot - 1)
    Ci = np.linalg.inv(C) * hartlap
    L = np.linalg.cholesky(C + 1e-14 * np.eye(p_dim))

    print("=" * 78)
    print("INDEPENDENT RE-CHECK — one-sided upper limit")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)
    print(f"\n  bins={p_dim}  bootstrap N={n_boot}  Hartlap alpha={hartlap:.4f}")
    print(f"  PV epsilon={EPS_PV} Mpc   r_lo={R_LO}   r_hi={R_HI}")

    out = {}
    for tag, weighted in (("raw", False), ("weighted", True)):
        k2, k3 = kernels(xi, r, weighted)
        M = Model(Ci, k2, k3)
        print(f"\n{'=' * 28} {tag.upper()} {'=' * 28}")
        print(f"  K2(100)={np.interp(100, r, k2):.6f}   K3(100)={np.interp(100, r, k3):.6f}")

        # G1
        worst = 0.0
        for mu in (0.0, 3.0, 8.0, 15.0):
            t = M.u + mu * M.v

            def nll(a, t=t):
                rr = d_obs - a[0] * t
                return float(rr @ Ci @ rr)

            res = minimize(
                nll,
                [M.amp(mu, d_obs)],
                method="Nelder-Mead",
                options={"xatol": 1e-13, "fatol": 1e-15},
            )
            worst = max(worst, abs(res.fun - M.chi2_at(mu, d_obs)))
        print(
            f"  [G1] analytic vs direct optimisation: max|diff|={worst:.2e} "
            f"{'PASS' if worst < 1e-8 else 'FAIL'}"
        )

        # G2
        wide = np.arange(-60.0, 60.0 + 1e-9, 0.05)
        dCd, dCu, dCv = M._proj(d_obs)
        chw = dCd - (dCu + wide * dCv) ** 2 / (M.uCu + 2 * wide * M.uCv + wide**2 * M.vCv)
        mu_unc = float(wide[int(np.argmin(chw))])
        q_obs, mu_con = M.q_tilde_grid(d_obs)
        print(
            f"  [G2] unconstrained={mu_unc:+.2f}  clipped={max(mu_unc, 0.0):.2f}  "
            f"constrained={mu_con:.2f}  "
            f"{'identical' if abs(max(mu_unc, 0.0) - mu_con) < 0.06 else 'DIFFER'}"
        )

        # G3
        print("  [G3] q~ regimes:")
        for lab, mt in (
            ("mu > mu_hat", mu_con + 5.0),
            ("mu = mu_hat", mu_con),
            ("mu < mu_hat", max(mu_con - 2.0, 0.0)),
        ):
            j = int(np.argmin(np.abs(MU_GRID - mt)))
            print(f"       {lab:12s} mu={MU_GRID[j]:5.2f}  q~={q_obs[j]:8.4f}")

        # G4 + G5
        mus_cal = np.arange(0.0, 20.0 + 1e-9, 0.5)
        n_cal = 4000
        sigA = 1.0 / np.sqrt(float((M.u + mu_con * M.v) @ Ci @ (M.u + mu_con * M.v)))
        accept = {}
        for a_lab, fac in (("A_cond", 0.0), ("A+1s", 1.0), ("A-1s", -1.0)):
            acc = []
            for mu in mus_cal:
                A = M.amp(mu, d_obs) + fac * sigA
                base = A * (M.u + mu * M.v)
                j = int(np.argmin(np.abs(MU_GRID - mu)))
                qs = np.empty(n_cal)
                for i in range(n_cal):
                    qg, _ = M.q_tilde_grid(base + L @ RNG.standard_normal(p_dim))
                    qs[i] = qg[j]
                if q_obs[j] <= np.percentile(qs, 95):
                    acc.append(float(mu))
            accept[a_lab] = max(acc) if acc else float("nan")
            print(f"  [G4/G5] nuisance {a_lab:7s}: UL95 = {accept[a_lab]:.2f} Mpc")

        # G6 — independent validation ensemble
        mu_v = 6.0
        A = M.amp(mu_v, d_obs)
        base = A * (M.u + mu_v * M.v)
        j = int(np.argmin(np.abs(MU_GRID - mu_v)))
        cal = np.array(
            [M.q_tilde_grid(base + L @ RNG.standard_normal(p_dim))[0][j] for _ in range(n_cal)]
        )
        thr = float(np.percentile(cal, 95))
        n_val = 4000
        val = np.array(
            [M.q_tilde_grid(base + L @ RNG.standard_normal(p_dim))[0][j] for _ in range(n_val)]
        )
        cov_emp = float(np.mean(val <= thr))
        mce = float(np.sqrt(cov_emp * (1 - cov_emp) / n_val))
        print(
            f"  [G6] independent coverage at mu={mu_v}: {cov_emp:.4f} +- {mce:.4f} "
            f"(thr={thr:.3f}) {'PASS' if abs(cov_emp - 0.95) < 3 * mce else 'CHECK'}"
        )

        out[tag] = {
            "mu_hat": mu_con,
            "UL95_stat": accept["A_cond"],
            "nuisance": accept,
            "coverage_val": cov_emp,
            "K2_100": float(np.interp(100, r, k2)),
            "K3_100": float(np.interp(100, r, k3)),
        }

    print("\n" + "=" * 78)
    print("COMPARISON WITH BLIND A (stat-only)")
    for tag, ref in (("raw", 11.00), ("weighted", 8.00)):
        got = out[tag]["UL95_stat"]
        ok = abs(got - ref) < 0.5
        print(
            f"  {tag:9s} ours {got:6.2f}   Blind A {ref:6.2f}   diff {got - ref:+.2f} Mpc   "
            f"{'AGREE' if ok else 'DISAGREE — localise, do not average'}"
        )
    (HERE / "recheck_onesided.json").write_text(json.dumps(out, indent=2))
    print("=" * 78)


if __name__ == "__main__":
    main()
