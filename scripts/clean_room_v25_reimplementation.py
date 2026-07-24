"""Clean-room reimplementation of TJB v25's kinematic-route H(z) bridge.

Independent of src/pearson_fit.py (which implements a DIFFERENT bridge,
H_MULTING = H_anchor * sqrt(phi/phi_ref) -- NOT the model v25 actually specifies).

Built only from the equations printed in the paper
(260723_1330_to_MULT_260717_0525_v25_first_13_pages.pdf), re-read and transcribed
into docs/140 Table B (formula registry, EXTRACTION_ONLY) this session. Equation
numbers below (Eq N) refer to that paper's own numbering.

STATUS: NOT a validated reproduction. Two things are fully specified by the paper
and implemented exactly (node-property scalings Eq 10-17, force law Eq 1-4).
ONE thing is NOT specified in the available 13 pages and is filled here with an
explicitly-labeled, non-author assumption (see CLOSURE ASSUMPTION below) -- do not
read any number this script prints as confirming or refuting v25's Table II/III/VI
without that caveat attached.

--- Derivation notes (kept in-line since this is the load-bearing, previously-
unverified part of the whole bridge) ---

Working in cosmic time t as the independent variable avoids the implicit-ODE trap
that a literal reading of the paper's z-space prose ("integrating 2(addot/a)/(1+z)
w.r.t. z yields H(z)^2 - H0^2", p.5) falls into: that phrasing is only an exact
z-space quadrature if the H^2 term in the standard identity

    addot/a = H^2 - (1+z) H dH/dz                                    (identity-A)

is dropped or separately accounted for. identity-A was verified symbolically
against the paper's OWN Eq. 18 (q(z) = (1+z) dH/dz / H - 1, the standard
deceleration parameter) -- sympy confirms q_from_identity_A == q_eq18 exactly.
So Eq. 8 (addot/a = sdotdot(z)/s(z)) is a well-posed ODE, just not the one-line
quadrature the prose describes; it is solved here directly in t instead:

    s_ddot(t) = H(z(t))^2 * s(t)                     (Eq 8, rearranged)
    dz/dt     = -(1+z) H(z)                          (Eq 9)

F_P and F_acc (Eq 1-4, 15-17) depend only on (s, z), never on ds/dt -- BUT F_acc
DOES depend on H(z) itself (Eq 17: F_acc = 1.1*H(z)*m_X(z)*Delta_v_coh(z)), and
Eq 7 (mu*s_ddot = F_P - F_acc) plus Eq 8 (s_ddot = H^2*s) together make H(z) appear
on both sides: mu*s*H^2 = F_P(s,z) - 1.1*H*m_X(z)*Delta_v_coh(z). This is NOT a
free-standing unknown needing a fixed-point iteration or a stale value carried over
from the previous integration step (an earlier version of this script made exactly
that mistake -- passed the constant H0,anchor into F_acc at every z, confirmed by
review to shift F_acc by up to ~97% at z~0.5-1.0). Because F_acc is exactly LINEAR
in H, the equation above is a quadratic in H at each (s,z), solved exactly and
locally by h_self_consistent() below -- so the overall [s, v=ds/dt, z] system is
explicit in the sense that matters (no iteration, no lag), even though H(z) itself
is a solved, not assigned, quantity at every step.

CLOSURE ASSUMPTION (ours, NOT the author's -- flag every time this script's output
is quoted):
  - s0 = s(z=0) is fixed by requiring self-consistency with the paper's OWN fitted
    H0,anchor (Table II): H0,anchor^2 = [F_P(s0,0) - F_acc(0)] / (mu(0) * s0),
    solved by root-finding. This uses only already-specified quantities (beta1,
    beta2, H0,anchor, m0-derived node properties at z=0) -- no new free parameter.
  - v0 = ds/dt(z=0) is NOT pinned by anything in the 13 available pages (F_P and
    F_acc do not depend on velocity, so nothing in Eq 1-17 constrains it). We adopt
    v0 = H0,anchor * s0 (the node pair also participates in local Hubble flow at
    z=0) as the most parsimonious, zero-new-parameter closure. This is a modeling
    choice we are making, not one v25 states, and should be reported as such.
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

# --- Physical constants ---
G_NEWTON = 4.30091e-9  # Mpc (km/s)^2 / Msun  (G in convenient astro units)
C_KMS = 299792.458  # km/s
MU_MOL = 0.6
M_PROTON_MSUN = 8.40969e-58  # proton mass in Msun (for k_X unit consistency, Eq 14)

# --- Fixed empirical inputs the paper cites (Table pivot values, Eq 10-13) ---
T0_KEV = 3.7163  # Eq 12
T_PIV_KEV = 2.27  # Eq 13
M_GAS_PIV_MSUN = 2.28e13  # Eq 13
Z_PIV = 0.25  # Eq 13
B_EXP = 2.24  # Eq 13
C_EXP = -1.00  # Eq 13
F_MERGE = 0.25  # Eq 15 text
F_COH = 1.0 / 3.0  # Eq 16 text (kappa=3)


def omega_e(z: float, omega_m: float = 0.3) -> float:
    """E(z), flat LCDM form used by v25 itself for r_X(z) (Eq 11 text, p.6)."""
    return np.sqrt(omega_m * (1 + z) ** 3 + (1 - omega_m))


def m_x(z: float, m0: float) -> float:
    """Eq 10: node mass evolution."""
    return m0 * (1 + z) ** (-1.1)


def r_x(z: float, m0: float, r0: float) -> float:
    """Eq 11: R500-type effective radius (Class III / circular per p.9 -- carried
    through as-is, not "fixed", per NO_AUTHOR_ERROR)."""
    return r0 * (m_x(z, m0) / m0) ** (1.0 / 3.0) * omega_e(z) ** (-2.0 / 3.0)


def t_x_kev(z: float, m0: float) -> float:
    """Eq 12: self-similar X-ray temperature."""
    return T0_KEV * (m_x(z, m0) / m0) ** (2.0 / 3.0) * omega_e(z) ** (2.0 / 3.0)


def m_gas_x(z: float, m0: float) -> float:
    """Eq 13: data-fitted gas mass from real M_gas-T scaling relation."""
    tx = t_x_kev(z, m0)
    return M_GAS_PIV_MSUN * (tx / T_PIV_KEV) ** B_EXP * (omega_e(z) / omega_e(Z_PIV)) ** C_EXP


def k_x(z: float, m0: float) -> float:
    """Eq 14: total ICM thermal energy (the k_A / k_P of Eq 3-4), in Msun*(km/s)^2
    (energy, in the same unit system G_NEWTON/C_KMS use -- so that k_X/C_KMS**2,
    exactly as Eq 3-4 divide by c^2, comes out in Msun, matching the paper's own
    "k_A/c^2 has dimensions of mass" statement, p.4)."""
    tx = t_x_kev(z, m0)
    n_particles = m_gas_x(z, m0) / (MU_MOL * M_PROTON_MSUN)
    # WHY: (3/2) n k_B T is the thermal energy; k_B T is quoted in keV (p.6's own
    # convention), so it must be converted to Msun*(km/s)^2 -- NOT to Msun*c^2 --
    # since c^2 is applied separately, symbolically, inside Eq 3-4 (via C_KMS**2).
    # 1 keV = 1.602176634e-16 J = 1.602176634e-16 kg*m^2/s^2; divide by 1.98892e30
    # kg/Msun and by 1e6 (m/s)^2 per (km/s)^2.
    kev_to_msun_kms2 = 1.602176634e-16 / 1.98892e30 / 1.0e6
    return 1.5 * n_particles * tx * kev_to_msun_kms2


def v_infall(z: float, m0: float, r0: float) -> float:
    """Eq 15."""
    return np.sqrt(G_NEWTON * m_x(z, m0) / r_x(z, m0, r0))


def delta_v_coh(z: float, m0: float, r0: float) -> float:
    """Eq 16."""
    return F_COH * F_MERGE * v_infall(z, m0, r0)


def m_x_dot(z: float, h_of_z: float, m0: float) -> float:
    """m_X_dot(z) = 1.1 H(z) m_X(z), stated directly under Eq 17."""
    return 1.1 * h_of_z * m_x(z, m0)


def f_acc(z: float, h_of_z: float, m0: float, r0: float) -> float:
    """Eq 17."""
    return m_x_dot(z, h_of_z, m0) * delta_v_coh(z, m0, r0)


def f_p_identical_nodes(
    s: float, z: float, beta1: float, beta2: float, m0: float, r0: float
) -> float:
    """Eq 1-4 for the identical-typical-node case (m_A=m_P, r_A=r_P, k_A=k_P), per
    Sec II.E's own simplification. Returns F_P (Eq 1), NOT yet accretion-corrected."""
    mx = m_x(z, m0)
    rx = r_x(z, m0, r0)
    kx = k_x(z, m0)
    f0 = -G_NEWTON * mx**2 / s**2
    f1 = -2 * beta1 * G_NEWTON * kx * mx * rx / (C_KMS**2 * s**3)
    f2 = beta2 * (-G_NEWTON * kx**2 * rx**2 / (C_KMS**4 * s**4))
    return f0 - f1 + f2


def h_self_consistent(
    s: float, z: float, beta1: float, beta2: float, m0: float, r0: float
) -> float:
    """Solve H(z) self-consistently at a given (s, z) -- NOT a fixed point from a
    previous integration step, an exact analytic solve.

    F_acc is LINEAR in H (Eq 17: F_acc = m_X_dot(z)*Delta_v_coh(z) =
    1.1*H*m_X(z)*Delta_v_coh(z)), so Eq 8's requirement mu*s*H^2 = F_P(s,z) -
    F_acc(z,H) is a quadratic in H, not a circular reference:

        mu*s * H^2 + [1.1*m_X(z)*Delta_v_coh(z)] * H - F_P(s,z) = 0

    Returns NaN where the discriminant is negative (no real H solves the
    self-consistency equation at this (s,z) -- this happens where F_P is so
    strongly attractive, at small s, that no expansion rate satisfies Eq 8; it is
    a real boundary of the physically valid (s,z) region, not a bug to paper over
    with a floor like max(x, 1e-12)).

    P1 review fix (2026-07-24): earlier version passed a caller-supplied h_of_z
    (often the CONSTANT H0,anchor, wrongly reused at every z along the whole
    trajectory) into s_ddot/f_acc instead of solving for the locally-consistent
    value -- confirmed by the reviewer agent to shift F_acc by up to ~97% at
    z~0.5-1.0 versus this exact solve. This function replaces that pattern
    everywhere; s_ddot(s,z,...) below is now DERIVED from this H, not the other
    way around.
    """
    mu = m_x(z, m0) / 2.0
    fp = f_p_identical_nodes(s, z, beta1, beta2, m0, r0)
    # f_acc(z, h_of_z, ...) is exactly linear in h_of_z (Eq 17), so evaluating it
    # at h_of_z=1.0 gives exactly its coefficient of H -- reusing f_acc/m_x_dot
    # here instead of re-deriving "1.1*m_X(z)*Delta_v_coh(z)" a second time.
    b_coef = f_acc(z, 1.0, m0, r0)
    a_coef = mu * s
    discriminant = b_coef**2 + 4 * a_coef * fp
    if discriminant < 0:
        return float("nan")
    return (-b_coef + np.sqrt(discriminant)) / (2 * a_coef)


def s_ddot(s: float, z: float, beta1: float, beta2: float, m0: float, r0: float) -> float:
    """s_ddot = H(z)^2 * s, by construction of Eq 8, with H(z) solved
    self-consistently (see h_self_consistent). Returns NaN where no real H
    exists at this (s, z) -- see h_self_consistent docstring."""
    h_z = h_self_consistent(s, z, beta1, beta2, m0, r0)
    if not np.isfinite(h_z):
        return float("nan")
    return h_z**2 * s


def solve_s0(beta1: float, beta2: float, h0_anchor: float, m0: float, r0: float) -> float:
    """Root-find s0 such that H(z=0), solved self-consistently via
    h_self_consistent, equals H0,anchor exactly (see CLOSURE ASSUMPTION in module
    docstring -- s0 itself is pinned by this equation, not a free choice).

    h_self_consistent(s, 0, ...) is NOT monotonic in s (quadrupole/dipole terms
    fall off faster than the monopole, so it rises from NaN/undefined at small s
    once real, peaks somewhere, then falls back toward 0 as s->infinity) -- there
    can be zero, one, or two roots depending on whether H0,anchor is below/above
    that peak. We return the SMALLER root (rising branch) as the more physically
    sensible "adjacent node" separation; a RuntimeError is raised if H0,anchor
    exceeds the peak (no solution exists for this m0 at all)."""

    def residual(s0: float) -> float:
        h_z0 = h_self_consistent(s0, 0.0, beta1, beta2, m0, r0)
        if not np.isfinite(h_z0):
            return float("-inf")
        return h_z0 - h0_anchor

    # bracket search across orders of magnitude (Mpc); wide range needed since the
    # peak location itself shifts by orders of magnitude with m0 (see docs/140).
    grid = np.logspace(-2, 5, 4000)
    vals = [residual(s) for s in grid]
    finite_vals = [v for v in vals if np.isfinite(v)]
    if not finite_vals or max(finite_vals) < 0:
        peak = max(finite_vals) + h0_anchor if finite_vals else float("-inf")
        raise RuntimeError(
            f"No s0 solves the closure equation for this m0: peak H(0)={peak:.4g} "
            f"< H0_anchor={h0_anchor:.4g}"
        )
    # P2 review fix (2026-07-24): require an explicit RISING crossing (negative ->
    # positive) with both endpoints finite -- not "any sign change", which could
    # silently accept a falling crossing (the larger root) or a spurious flip
    # across the NaN/-inf "no real H here" boundary that isn't a real root at all.
    for i in range(len(grid) - 1):
        lo, hi = vals[i], vals[i + 1]
        if not (np.isfinite(lo) and np.isfinite(hi)):
            continue
        if lo == 0:
            return grid[i]
        if lo < 0 < hi:
            return brentq(residual, grid[i], grid[i + 1])
    raise RuntimeError(
        f"No rising sign change found for s0 root-search in [{grid[0]:.3g}, {grid[-1]:.3g}] Mpc"
    )


def integrate_h_of_z(
    beta1: float,
    beta2: float,
    h0_anchor: float,
    m0: float,
    r0: float,
    z_max: float = 2.5,
    n_eval: int = 400,
):
    """Integrate the coupled [s, v, z] system forward in cosmic time until z_max,
    return (z_array, H_array) via dense interpolation.

    P1 review fix (2026-07-24): H(z) is now solved self-consistently at every
    step via h_self_consistent (an exact quadratic solve), not read from a
    caller-supplied h_of_z that was previously always the constant H0,anchor --
    see h_self_consistent's docstring for why that was wrong and by how much."""
    s0 = solve_s0(beta1, beta2, h0_anchor, m0, r0)
    v0 = h0_anchor * s0  # CLOSURE ASSUMPTION -- see module docstring

    def rhs(_t: float, y: np.ndarray) -> list[float]:
        s, v, z = y
        if s <= 0 or z < -0.999:
            return [0.0, 0.0, 0.0]
        z_c = max(z, -0.999)
        h_z = h_self_consistent(s, z_c, beta1, beta2, m0, r0)
        if not np.isfinite(h_z):
            return [0.0, 0.0, 0.0]  # guard; hit_boundary event should stop first
        sdd = h_z**2 * s
        dzdt = -(1 + z_c) * h_z
        return [v, sdd, dzdt]

    # integrate backward in time (t decreasing) == forward in z (z increasing);
    # use z as an event-driven stopping condition
    t_span = (0.0, -50.0)  # Gyr-ish units are irrelevant; s0,H0 set the scale

    def hit_zmax(_t, y):
        return y[2] - z_max

    hit_zmax.terminal = True
    hit_zmax.direction = 1

    def hit_boundary(_t, y):
        # +1 while a real self-consistent H(z) exists at this (s,z), -1 once it
        # doesn't (see h_self_consistent docstring) -- stops the integration
        # honestly at the edge of the physically valid region instead of letting
        # NaN propagate silently.
        s, _v, z = y
        if s <= 0:
            return -1.0
        h_z = h_self_consistent(s, max(z, -0.999), beta1, beta2, m0, r0)
        return 1.0 if np.isfinite(h_z) else -1.0

    hit_boundary.terminal = True
    hit_boundary.direction = -1

    sol = solve_ivp(
        rhs,
        t_span,
        [s0, v0, 0.0],
        max_step=abs(t_span[1]) / 20000,
        events=[hit_zmax, hit_boundary],
        dense_output=True,
        rtol=1e-8,
        atol=1e-10,
    )
    if not sol.success:
        raise RuntimeError(f"ODE integration failed: {sol.message}")

    t_grid = np.linspace(0.0, sol.t[-1], n_eval)
    s_t, v_t, z_t = sol.sol(t_grid)
    h_t = np.full_like(z_t, np.nan)
    for i, (s_i, z_i) in enumerate(zip(s_t, z_t, strict=True)):
        h_t[i] = h_self_consistent(s_i, z_i, beta1, beta2, m0, r0)
    return z_t, h_t


if __name__ == "__main__":
    import json
    from pathlib import Path

    # Table II, Case 1 (free-floating anchor, the paper's nominal result)
    BETA1_CASE1 = 1.28e10
    BETA2_CASE1 = 7.10e17
    H0_ANCHOR_CASE1 = 76.46

    # baseline node properties: use a representative MCXC-like cluster mass/radius
    # as m0/r0 (identical-node case, Sec II.E) -- these are NOT fitted, just a
    # reference scale; results are reported for a SWEEP to show sensitivity.
    RHO_CRIT0_MSUN_MPC3 = 2.775e11 * 0.674**2  # standard rho_crit,0 = 2.775e11 h^2 Msun/Mpc^3
    RESULTS = []
    # 4e14-1e15 Msun brackets the closure crossing found in diagnostics for
    # Case-1's (beta1,beta2,H0_anchor) -- "node = one cluster or a few clusters"
    # (p.2) covers this range comfortably.
    for m0 in [4e14, 6e14, 8e14, 1e15]:
        r0 = (3 * m0 / (4 * np.pi * 500 * RHO_CRIT0_MSUN_MPC3)) ** (1.0 / 3.0)
        try:
            z_arr, h_arr = integrate_h_of_z(BETA1_CASE1, BETA2_CASE1, H0_ANCHOR_CASE1, m0, r0)
            h_at_233 = float(np.interp(2.33, z_arr, h_arr)) if z_arr.max() >= 2.33 else None
            RESULTS.append(
                {
                    "m0_Msun": m0,
                    "r0_Mpc": r0,
                    "z_max_reached": float(z_arr.max()),
                    "H_at_z0": float(h_arr[0]),
                    "H_at_z2.33": h_at_233,
                    "note": "H_at_z0 should equal H0_anchor by construction (closure check)",
                }
            )
        except Exception as exc:  # noqa: BLE001 -- diagnostic script, report and continue
            RESULTS.append({"m0_Msun": m0, "error": str(exc)})

    out_path = Path(__file__).resolve().parents[1] / "reports" / "clean_room_v25_sensitivity.json"
    out_path.parent.mkdir(exist_ok=True)
    out_path.write_text(json.dumps(RESULTS, indent=2))
    print(json.dumps(RESULTS, indent=2))
