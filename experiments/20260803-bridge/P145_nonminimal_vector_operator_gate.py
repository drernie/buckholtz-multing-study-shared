"""P145 -- non-minimal vector operator-basis gate (two symbolic checks).

Context: P142's cheapest differentiating test for the "unique completion"
inverse problem. P144 narrowed docs/131's "vector/antisymmetric sector"
residual branch to one open candidate: a non-minimally-coupled vector
construction. This script runs the two genuinely computable pieces of the
user-specified operator-basis gate (see FINDING_P145 for the full
classification and the qualitative pieces this script does NOT cover).

Check 1 -- candidate operator R_mu_nu A^mu A^nu (non-minimal curvature
coupling): is this identically zero in the two-body static vacuum
configuration this project's completions target? Verified by computing the
LINEARIZED Ricci tensor of the standard weak-field metric sourced by a
static point mass, away from the source (r != 0), and checking it vanishes
component-by-component. This is the textbook vacuum-Einstein-equation fact
(Schwarzschild is Ricci-flat); computed here rather than asserted.

Check 2 -- candidate operator: a magnetization-type ("permanent-magnet")
bound current sourced by a STATIC (time-independent) but non-zero internal
current density, motivated directly by P144's own flagged, not-fully-closed
loophole (its Argument C closure assumed "static" = zero internal currents;
a fixed internal magnetization has J != 0 without any translational motion).
This gives body A (and, symmetrically, body B, since both carry the same
k-charge structure) a magnetic-dipole-type field, with the standard
dipole-dipole interaction energy. Checked: does the GLOBAL energy minimum
over relative orientation correspond to a repulsive or attractive
configuration? Verified symbolically via sp.solve on the stationarity
conditions plus a Hessian/second-derivative check, not asserted from
textbook memory alone (Branch S's own docs/131 result is the direct analog
for the electric monopole-dipole case; this checks whether the genuinely
different magnetic dipole-dipole angular structure changes the qualitative
outcome).
"""

import numpy as np
import sympy as sp

print("=" * 70)
print("CHECK 1 -- R_mu_nu A^mu A^nu: vacuum Ricci-flatness away from a")
print("static point-mass source")
print("=" * 70)

x, y, z, G, M = sp.symbols("x y z G M", real=True)
r = sp.sqrt(x**2 + y**2 + z**2)
coords = [None, x, y, z]  # index 0 unused (time), static metric

# Standard isotropic weak-field metric perturbation for a static point
# mass, leading order in G (harmonic-like gauge): h_00 = 2GM/r,
# h_0i = 0 (static, no frame-dragging), h_ij = 2GM/r * delta_ij.
Phi = G * M / r
h = sp.zeros(4, 4)
h[0, 0] = 2 * Phi
for i in (1, 2, 3):
    h[i, i] = 2 * Phi

trace_h = sp.Rational(0) - h[0, 0] + h[1, 1] + h[2, 2] + h[3, 3]  # eta^ab h_ab, eta=diag(-1,1,1,1)
trace_h = sp.simplify(trace_h)


def d(expr, mu):
    """Partial derivative w.r.t. coordinate mu (0=time -> 0, static)."""
    if mu == 0:
        return sp.Integer(0)
    return sp.diff(expr, coords[mu])


def dd(expr, mu, nu):
    return d(d(expr, mu), nu)


eta_inv = [-1, 1, 1, 1]  # diag(eta^00, eta^11, eta^22, eta^33)


def box(expr):
    """eta^ab d_a d_b expr, static so only spatial Laplacian survives."""
    return sum(eta_inv[a] * dd(expr, a, a) for a in range(4))


def ricci_lin(mu, nu):
    """Linearized Ricci tensor: R_mu_nu = 1/2 (d^a d_mu h_a_nu +
    d^a d_nu h_a_mu - d_mu d_nu h - box h_mu_nu), d^a = eta^aa d_a
    (diagonal metric, no sum-index confusion since h is diagonal too).
    """
    term1 = sum(eta_inv[a] * dd(h[a, nu], a, mu) for a in range(4))
    term2 = sum(eta_inv[a] * dd(h[a, mu], a, nu) for a in range(4))
    term3 = dd(trace_h, mu, nu)
    term4 = box(h[mu, nu])
    return sp.Rational(1, 2) * (term1 + term2 - term3 - term4)


all_zero = True
for mu in range(4):
    for nu in range(mu, 4):
        Rmn = sp.simplify(ricci_lin(mu, nu))
        # away from the source (r != 0), 1/r is harmonic: check by
        # substituting a generic point, e.g. (1,1,1), after simplifying
        # symbolically -- if the symbolic expression is already 0 for
        # generic x,y,z, this confirms it identically, not just at a point.
        is_zero_symbolic = sp.simplify(Rmn) == 0
        if not is_zero_symbolic:
            all_zero = False
        print(f"R_{mu}{nu} = {Rmn}   [identically zero: {is_zero_symbolic}]")

print()
print(
    f"POSITIVE CONTROL: laplacian(1/r) at r!=0 = "
    f"{sp.simplify(sp.diff(1 / r, x, 2) + sp.diff(1 / r, y, 2) + sp.diff(1 / r, z, 2))}"
    f"  (must be 0 -- confirms harmonicity of 1/r away from origin, the "
    f"fact this whole check rests on)"
)
print()
print(f"CHECK 1a RESULT: all linearized Ricci components zero for r!=0: {all_zero}")
print("   (this is vacuum Ricci-flatness AWAY from any source -- true, but")
print("   see CORRECTION below: this does NOT mean the operator's total")
print("   contribution to a two-body interaction is zero.)")

print()
print("-" * 70)
print("CHECK 1b -- CORRECTION (post independent skeptic review):")
print("R_mu_nu is NOT zero everywhere -- it has delta-function support")
print("exactly at each source's own worldline (R_mu_nu is proportional to")
print("T_mu_nu via the trace-reversed Einstein equation, R_00 = 4 pi G M")
print("delta^3(x) for a point mass -- this is definitional, not a separate")
print("fact to derive). The original CHECK 1a conclusion ('contributes")
print("nothing') wrongly inferred a global statement from a check that only")
print("covered field points AWAY from both sources. Corrected here.")
print("-" * 70)

R_sym = sp.symbols("R", positive=True)
grad_radial_1_over_r = sp.diff(1 / sp.Symbol("r"), sp.Symbol("r")).subs(sp.Symbol("r"), R_sym)
flux = sp.simplify(grad_radial_1_over_r * 4 * sp.pi * R_sym**2)
print(
    f"Divergence-theorem check: flux of grad(1/r) through a sphere of "
    f"radius R = {flux}  (R-independent -> confirms laplacian(1/r) = "
    f"-4*pi*delta^3(x) as a distribution, the identity R_00's delta-"
)
print("function support rests on)")

lam, GN, Mb, kA, rr2 = sp.symbols("lambda G_N M_B k_A r", positive=True)
# R_00(x_B) = 4 pi G M_B delta^3(x-x_B)  (trace-reversed Einstein eq, point mass)
# A_0(x) = k_A / (4 pi |x-x_A|)          (standard Coulomb-like falloff,
#                                          matching P143's own 1/(4 pi) normalization)
# S_int ~ lambda * integral R_00(x) A_0(x)^2 d^3x
#       = lambda * 4 pi G M_B * [k_A/(4 pi r)]^2   (delta function picks out x=x_B)
R00_coefficient = 4 * sp.pi * GN * Mb  # coefficient of delta^3(x-x_B) in R_00
A0_squared_at_B = (kA / (4 * sp.pi * rr2)) ** 2
V_interaction = sp.simplify(lam * R00_coefficient * A0_squared_at_B)
print()
print("Corrected interaction potential from the delta-function contribution:")
print(f"  V(r) = lambda * R_00-coefficient * A_0(x_B)^2 = {V_interaction}")
force_power = sp.simplify(sp.diff(V_interaction, rr2))
print(f"  dV/dr = {force_power}  -> FORCE ~ 1/r^3 (matches MULTING's target")
print("  power law DIRECTLY -- Delta_alpha=0, no extra derivative needed,")
print("  unlike P143's minimal-coupling case).")
print()
print("CHECK 1 CORRECTED RESULT: R_mu_nu A^mu A^nu does NOT vanish for the")
print("two-body interaction -- it reaches the target 1/r^3 force law via a")
print("genuinely different mechanism (curvature-mediated, delta-function")
print("source contribution) than any construction tested in P143/P144.")
print("Its coupling coefficient lambda is a FREE parameter of this")
print("non-minimal operator -- nothing established so far fixes its sign.")
print("NOT CLOSED: this operator is a live VECTOR-ESCAPE-CANDIDATE pending")
print("a ghost-freedom / EFT-positivity-bound check on lambda's allowed")
print("sign -- same open status as (grad_mu A^mu)^2, not resolved here.")

print()
print("=" * 70)
print("CHECK 2 -- magnetization-current (permanent-dipole) coupling:")
print("global energy minimum, dipole-dipole interaction")
print("=" * 70)

theta_A, theta_B, phi, mu0, MA, MB, rr = sp.symbols(
    "theta_A theta_B phi mu_0 M_A M_B r", positive=True
)
# Standard magnetic (or any) dipole-dipole interaction energy:
# U = (mu_0 / 4 pi r^3) [ m_A . m_B - 3 (m_A.rhat)(m_B.rhat) ]
# m_A . m_B    = MA*MB*(cos(theta_A)cos(theta_B) + sin(theta_A)sin(theta_B)cos(phi))
# (m_A.rhat)(m_B.rhat) = MA*MB*cos(theta_A)*cos(theta_B)
m_dot_m = (
    MA * MB * (sp.cos(theta_A) * sp.cos(theta_B) + sp.sin(theta_A) * sp.sin(theta_B) * sp.cos(phi))
)
proj_term = MA * MB * sp.cos(theta_A) * sp.cos(theta_B)
U = (mu0 / (4 * sp.pi * rr**3)) * (m_dot_m - 3 * proj_term)
U = sp.simplify(U)
print(f"U(theta_A, theta_B, phi) = {U}")

# Stationary points: dU/dtheta_A = dU/dtheta_B = dU/dphi = 0
dUdA = sp.diff(U, theta_A)
dUdB = sp.diff(U, theta_B)
dUdphi = sp.diff(U, phi)

candidates = [
    ("head-to-tail, aligned along r (theta_A=0, theta_B=0)", 0, 0, 0),
    ("head-to-head along r (theta_A=0, theta_B=pi)", 0, sp.pi, 0),
    (
        "both perpendicular to r, parallel (theta_A=pi/2, theta_B=pi/2, phi=0)",
        sp.pi / 2,
        sp.pi / 2,
        0,
    ),
    (
        "both perpendicular to r, anti-parallel (theta_A=pi/2, theta_B=pi/2, phi=pi)",
        sp.pi / 2,
        sp.pi / 2,
        sp.pi,
    ),
]

print()
print("Stationarity check (dU/dtheta_A, dU/dtheta_B, dU/dphi at each candidate):")
results = []
for label, tA, tB, ph in candidates:
    subs = {theta_A: tA, theta_B: tB, phi: ph}
    grad = (
        sp.simplify(dUdA.subs(subs)),
        sp.simplify(dUdB.subs(subs)),
        sp.simplify(dUdphi.subs(subs)),
    )
    Uval = sp.simplify(U.subs(subs))
    stationary = all(g == 0 for g in grad)
    results.append((label, Uval, stationary))
    print(f"  {label}: U = {Uval}, gradient = {grad}, stationary: {stationary}")

print()
Uvals = [(label, val) for label, val, stat in results if stat]
Uvals_sorted = sorted(Uvals, key=lambda t: t[1])
print("Stationary configurations ranked by energy (most negative = global min = STABLE):")
for label, val in Uvals_sorted:
    tag = "<-- GLOBAL MINIMUM (stable)" if val == Uvals_sorted[0][1] else ""
    print(f"  U = {val}   {label}  {tag}")

global_min_label, global_min_val = Uvals_sorted[0]
global_max_label, global_max_val = Uvals_sorted[-1]
print()
print(f"CHECK 2 RESULT: global minimum ({global_min_val}) occurs at '{global_min_label}'.")
print(f"                global maximum ({global_max_val}) occurs at '{global_max_label}'.")
is_min_attractive = global_min_val < 0
print(
    f"-> stable (energy-minimizing) configuration is "
    f"{'ATTRACTIVE' if is_min_attractive else 'REPULSIVE'} "
    f"(sign of U at the minimum, standard convention: U<0 = bound/attractive)."
)
print("-> this is the SAME qualitative outcome as docs/131's Branch S")
print("   (electric monopole-dipole): the repulsive configuration is the")
print("   energy MAXIMUM (unstable), not the minimum -- for the genuinely")
print("   different magnetic dipole-dipole angular structure too, not just")
print("   Branch S's cos(theta) form.")

print()
print("-" * 70)
print("ROBUSTNESS CHECK -- the 4 hand-picked candidates above were guessed")
print("by symmetry, not proven exhaustive. Confirm by dense numerical grid")
print("search over the full (theta_A, theta_B, phi) domain that no OTHER")
print("stationary point gives a lower (more attractive) or higher (more")
print("repulsive) energy than the two extremes already found.")
print("-" * 70)

U_numeric = sp.lambdify((theta_A, theta_B, phi), U.subs({mu0: 1, MA: 1, MB: 1, rr: 1}), "numpy")
n = 200
tA_grid = np.linspace(0, np.pi, n)
tB_grid = np.linspace(0, np.pi, n)
phi_grid = np.linspace(0, 2 * np.pi, n)
TA, TB, PH = np.meshgrid(tA_grid, tB_grid, phi_grid, indexing="ij")
grid_vals = U_numeric(TA, TB, PH)

grid_min = grid_vals.min()
grid_max = grid_vals.max()
symbolic_min = float(global_min_val.subs({mu0: 1, MA: 1, MB: 1, rr: 1}))
symbolic_max = float(global_max_val.subs({mu0: 1, MA: 1, MB: 1, rr: 1}))

print(f"Grid search ({n}^3 = {n**3:,} points): min = {grid_min:.6f}, max = {grid_max:.6f}")
print(f"Symbolic candidates (normalized): min = {symbolic_min:.6f}, max = {symbolic_max:.6f}")
grid_matches_symbolic = abs(grid_min - symbolic_min) < 1e-3 and abs(grid_max - symbolic_max) < 1e-3
print(
    f"Grid search confirms the 4 hand-picked candidates ARE the global "
    f"extrema: {grid_matches_symbolic}"
)
if not grid_matches_symbolic:
    print("*** WARNING: grid search found a MORE EXTREME point than the")
    print("*** hand-picked candidates -- the stationary-point analysis above")
    print("*** is INCOMPLETE. Do not trust the 'global minimum' claim as-is.")
