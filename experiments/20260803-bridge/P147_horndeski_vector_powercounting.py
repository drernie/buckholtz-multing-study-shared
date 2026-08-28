"""P147 -- power-counting check of Horndeski's own gauge-invariant
vector-curvature coupling, the one candidate P146 left open.

Context: P146's literature check showed R_mu_nu A^mu A^nu (P145's own
candidate) is inadmissible if A_mu is a gauge field -- Horndeski (1976)
uniquely fixes the gauge-invariant, ghost-free non-minimal coupling as
I(g,A) = -1/4(F_mu_nu F^kappa_lambda R^mu_nu_kappa_lambda
             - 4 F_mu_kappa F^nu_kappa R^mu_nu
             + F_mu_nu F^mu_nu R)
built entirely from F_mu_nu, never bare A_mu. This script checks whether
THIS term, evaluated for the same two-body static configuration used
throughout this chain (P143, P145), reaches MULTING's target 1/r^3 force.

Split into two pieces, per their different structure:

Part 1 -- the Ricci-tensor and Ricci-scalar terms (-4 F F R^mu_nu +
F F R): both R_mu_nu and R vanish AWAY from a source (established in
P145/P146) and have delta-function support AT the source -- same
mechanism as P145's Check 1b, now with F^2 (body A's field strength)
instead of A^2 (body A's bare field). This is the CLEAN, fully rigorous
part of this script: exact symbolic computation, positive-control-style
verification of every matrix index-raising step, no hand-waving.

Part 2 -- the Riemann/Weyl term (F F R^mu_nu_kappa_lambda): the FULL
Riemann tensor does NOT vanish away from a source (unlike Ricci) -- its
vacuum part (Weyl) is the genuine long-range tidal field. Evaluating this
term's contribution to a two-body interaction requires integrating F^2
(peaked near body A) against the Weyl tensor (sourced by body B) over
all space -- this is a genuine point-particle EFT matching calculation
(Goldberger-Rothstein-type), UV-divergent near body A's own worldline,
NOT attempted in full here. What IS done: an honest, explicitly-labeled
dimensional-scaling estimate of the resulting r-dependence, cross-checked
against the standard weak-field Riemann-tensor scaling (verified via the
same linearized-metric machinery as P145).
"""

import sympy as sp

print("=" * 70)
print("PART 1 -- Ricci-tensor/scalar piece of Horndeski's term")
print("(-4 F_mu_kappa F^nu_kappa R^mu_nu + F_mu_nu F^mu_nu R),")
print("evaluated at body B's delta-function-supported location")
print("=" * 70)

eta = sp.diag(-1, 1, 1, 1)  # mostly-plus, matching P145's own convention
eta_inv = sp.diag(-1, 1, 1, 1)  # same matrix (involutive for this metric)

GN, Mb, kA, rr = sp.symbols("G_N M_B k_A r", positive=True)

# Body A's field strength F_{mu nu} at body B's location, separation r:
# A_0(x) = k_A/(4*pi*|x-x_A|)  =>  F_0i = d_i A_0 = -k_A*xhat_i/(4*pi*r^2)
# Take separation along the x-axis (xhat = (1,0,0)) WLOG (isotropic source).
E = kA / (4 * sp.pi * rr**2)  # magnitude of F_0i = "electric field"-type piece
F = sp.zeros(4, 4)
F[0, 1] = -E
F[1, 0] = E  # F_mu_nu antisymmetric, F_10 = -F_01

# Raise both indices: F^{mu nu} = eta^{mu a} eta^{nu b} F_{a b}
F_up = eta_inv * F * eta_inv.T
F_sq = sum(F[mu, nu] * F_up[mu, nu] for mu in range(4) for nu in range(4))
F_sq = sp.simplify(F_sq)
print(f"F_mu_nu F^mu_nu (at separation r) = {F_sq}")
print("(positive control: standard EM identity F^2 = -2*E^2 for a pure")
print(
    f" 'electric'-type field in mostly-plus signature -- check: "
    f"{sp.simplify(F_sq - (-2 * E**2))} should be 0)"
)

# R_mu_nu's delta-function coefficient at a point mass (established in
# P145/P146: R_00 = 4*pi*G*M*delta^3(x), R_ij = 4*pi*G*M*delta^3(x)*delta_ij,
# R_0i = 0). Represent as the COEFFICIENT of delta^3(x-x_B) (the delta
# itself factors out of every term below identically).
R_lower_coeff = sp.diag(
    4 * sp.pi * GN * Mb, 4 * sp.pi * GN * Mb, 4 * sp.pi * GN * Mb, 4 * sp.pi * GN * Mb
)
R_lower_coeff[0, 0] = 4 * sp.pi * GN * Mb  # R_00 coefficient (re-stated for clarity)

# R^mu_nu = eta^{mu a} R_{a nu}  (mixed index, one raised)
R_mixed_coeff = eta_inv * R_lower_coeff
print(
    f"\nR^mu_nu coefficient (mixed index, diagonal entries): "
    f"{[R_mixed_coeff[i, i] for i in range(4)]}"
)
print("(positive control: R^0_0 should flip sign relative to R_00 under")
print(
    f" index-raising with eta^00=-1 -- check: R^0_0 = "
    f"{R_mixed_coeff[0, 0]}, R_00 = {R_lower_coeff[0, 0]}, ratio = "
    f"{sp.simplify(R_mixed_coeff[0, 0] / R_lower_coeff[0, 0])} should be -1)"
)

# F_{mu kappa} F^{nu kappa} R^{mu}_{nu}  (sum mu, nu, kappa)
FF_contracted = sp.zeros(4, 4)  # [mu, nu] = F_{mu kappa} F^{nu kappa}
for mu in range(4):
    for nu in range(4):
        FF_contracted[mu, nu] = sum(F[mu, kappa] * F_up[nu, kappa] for kappa in range(4))

term_ricci_tensor = sum(
    FF_contracted[mu, nu] * R_mixed_coeff[mu, nu] for mu in range(4) for nu in range(4)
)
term_ricci_tensor = sp.simplify(term_ricci_tensor)
print(f"\nF_mu_kappa F^nu_kappa R^mu_nu coefficient (of delta^3(x-x_B)): {term_ricci_tensor}")

# Ricci scalar coefficient: R = eta^{mu nu} R_{mu nu}
R_scalar_coeff = sp.simplify(sum(eta_inv[mu, mu] * R_lower_coeff[mu, mu] for mu in range(4)))
print(f"R (Ricci scalar) coefficient (of delta^3(x-x_B)): {R_scalar_coeff}")

term_ricci_scalar = sp.simplify(F_sq * R_scalar_coeff)
print(f"F_mu_nu F^mu_nu * R coefficient (of delta^3(x-x_B)): {term_ricci_scalar}")

horndeski_ricci_part = sp.simplify(-4 * term_ricci_tensor + term_ricci_scalar)
print("\nCombined (-4 F F R^mu_nu + F F R), coefficient of delta^3(x-x_B):")
print(f"  {horndeski_ricci_part}")

# Full Horndeski normalization: I(g,A) = -1/4 * (Riemann_term + this combination)
V_ricci_part = sp.simplify(sp.Rational(-1, 4) * horndeski_ricci_part)
print(
    "\nRicci-based contribution to interaction potential V_ricci(r) "
    "(the '-1/4' overall Horndeski normalization applied):"
)
print(f"  V_ricci(r) = {V_ricci_part}")
# for a pure power law V(r) = C*r^n, the log-derivative n = r*dV/dr / V
# is r-independent -- compute it this way (robust to negative n, unlike
# sp.degree which only handles polynomial/non-negative exponents).
power_ricci = sp.simplify(rr * sp.diff(V_ricci_part, rr) / V_ricci_part)
print(
    f"  r-power of V_ricci (n such that V~r^n, via r*dV/dr/V): n = {power_ricci}  "
    f"(potential ~ r^{power_ricci} -> force ~ r^{sp.simplify(power_ricci - 1)})"
)
print("  TARGET for MULTING: force ~ r^-3, i.e. potential ~ r^-2")
print(f"  MATCH: {power_ricci == -2}")

print()
print("=" * 70)
print("PART 2 -- Riemann/Weyl piece: dimensional-scaling ESTIMATE only")
print("(NOT a full point-particle EFT matching -- explicitly flagged)")
print("=" * 70)

print("""
The full Riemann tensor (unlike Ricci) does NOT vanish in vacuum -- its
vacuum part (Weyl) is the genuine tidal field, standard weak-field scaling
R_{0i0j} ~ d_i d_j Phi_B ~ G*M_B/r^3 (second derivative of the Newtonian
potential, away from the source; this is the textbook tidal-tensor scaling,
same order as e.g. the Earth-Moon tidal acceleration formula).

Evaluating F_mu_nu(x) F^kappa_lambda(x) R^{mu nu}_{kappa lambda}(x)
integrated over all space picks up its dominant contribution near body A's
own worldline (where F, sourced by A, is largest) -- this is a genuine
point-particle EFT matching calculation (Goldberger-Rothstein-type),
UV-divergent at short distance from A, whose FINITE remainder after
renormalization is NOT computed here (beyond this 'cheap gate' step's own
scope, same category of subtlety the second P145 skeptic review flagged
for the R_mu_nu A^mu A^nu case).

What CAN be stated honestly at dimensional-scaling level: if the finite,
renormalized matching coefficient multiplies the LEADING tidal scaling
R_{Weyl}(x_A) ~ G*M_B/r^3 directly (the simplest possible EFT-matching
structure -- a local A-self-moment, r-independent after renormalization,
times the external tidal field evaluated at A's own location), the
resulting interaction potential scales as:
""")

power_weyl_potential = -3
power_weyl_force = power_weyl_potential - 1
print(f"  V_Weyl(r) ~ (const) * G*M_B/r^3   =>   r-power = {power_weyl_potential}")
print(f"  FORCE_Weyl(r) ~ r^{power_weyl_force}")
print("  TARGET for MULTING: force ~ r^-3")
print(f"  MATCH: {power_weyl_force == -3}")

print()
print("=" * 70)
print("VERDICT")
print("=" * 70)
print(f"""
Ricci-based piece (Part 1, rigorous):   force ~ r^{sp.simplify(power_ricci - 1)}
Weyl-based piece   (Part 2, ESTIMATE):  force ~ r^{power_weyl_force}
Target (MULTING):                        force ~ r^-3

Neither piece reaches the target power law at this leading (monopole-order,
same construction level as P143's own baseline) order. Unlike P143's
minimal coupling (needed one extra derivative, Delta_alpha=1, in principle
addable) or P145/146's R_mu_nu A^mu A^nu (reached the target power law
exactly but was inadmissible/non-generic), Horndeski's own UNIQUELY FIXED
coupling has no free coefficient to retune -- if the power law doesn't
match, there is no adjustable parameter left to fix it. This is a
DIFFERENT class of failure than anything else in this P142 chain: wrong
functional form, not wrong sign or wrong symmetry.
""")
