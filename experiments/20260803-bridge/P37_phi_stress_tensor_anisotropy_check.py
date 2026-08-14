"""P37 -- fourth step of the covariant-completion campaign (see
PLAN_final_goal_20260814.md), resuming at a deliberately slower pace per
explicit user instruction (one step at a time). Directly targets the
narrowest, safest piece of P35's own flagged open question (its section
5/6.8): does phi's own stress-energy, for the static solution
phi(r)=g_hat*M/(4*pi*r) already derived in P35, actually have a nonzero
ANISOTROPIC (traceless spatial) part?

SCOPE, DELIBERATELY NARROW. This does NOT attempt to solve the full
linearized Einstein ij-equation for the resulting metric slip (Phi-Psi)
-- that is a larger, separate step, appropriately deferred. This ONLY
computes T_munu^phi explicitly from the definition and checks whether
its spatial part is proportional to the identity (isotropic, no slip
source) or has a genuine traceless remainder (anisotropic, a real slip
SOURCE, though not yet its magnitude on the metric).

METHOD. Standard canonical (minimally-coupled) scalar stress tensor,
T_munu = d_mu(phi)*d_nu(phi) - (1/2)*g_munu*(d(phi))^2, evaluated on the
ALREADY-DERIVED static flat-background field phi(r)=g_hat*M/(4*pi*r)
from P35 (re-used, not re-derived). Using the flat background for this
leading-order check is the standard, correct procedure -- metric
perturbations would only affect T_munu at a HIGHER order than the
question being asked here (does a nonzero source exist at all).

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - L0 descriptive
"""

import sympy as sp


def scalar_stress_tensor_spatial(phi_expr, x, y, z, coords):
    """T_ij = d_i(phi)*d_j(phi) - (1/2)*delta_ij*(grad phi)^2, the spatial
    part of the standard canonical scalar stress tensor, static case
    (d_t phi = 0), evaluated in Cartesian coordinates -- avoids any risk
    of a spherical-coordinate conversion error."""
    grad = [sp.diff(phi_expr, c) for c in coords]
    grad_sq = sum(g**2 for g in grad)
    T = sp.zeros(3, 3)
    for i in range(3):
        for j in range(3):
            delta_ij = 1 if i == j else 0
            T[i, j] = sp.simplify(grad[i] * grad[j] - sp.Rational(1, 2) * delta_ij * grad_sq)
    return T


def main():
    x, y, z = sp.symbols("x y z", real=True)
    ghat, M = sp.symbols("g_hat M", positive=True)
    r = sp.sqrt(x**2 + y**2 + z**2)

    print("=" * 78)
    print("P37 -- does phi's own static stress tensor have anisotropic stress?")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    print("\n[STEP 1] Re-use P35's already-derived static field (not re-derived):")
    phi_expr = ghat * M / (4 * sp.pi * r)
    print(f"  phi(r) = {phi_expr}")

    print("\n[STEP 2] Compute T_ij = d_i(phi)*d_j(phi) - (1/2)*delta_ij*(grad phi)^2")
    print("  in Cartesian coordinates (avoids spherical-coordinate conversion risk):")
    T = scalar_stress_tensor_spatial(phi_expr, x, y, z, [x, y, z])
    print(f"  T_xx = {T[0, 0]}")
    print(f"  T_yy = {T[1, 1]}")
    print(f"  T_zz = {T[2, 2]}")
    print(f"  T_xy = {T[0, 1]}")

    print("\n[STEP 3] Evaluate on the z-axis (x=0,y=0,z=r>0) -- a convenient point")
    print("  where the radial direction is manifestly z-hat, so T_zz is the")
    print("  RADIAL stress and T_xx=T_yy is the TANGENTIAL stress by symmetry:")
    r_sym = sp.Symbol("r", positive=True)
    subs_on_axis = {x: 0, y: 0, z: r_sym}
    T_radial = sp.simplify(T[2, 2].subs(subs_on_axis))
    T_tangential_x = sp.simplify(T[0, 0].subs(subs_on_axis))
    T_tangential_y = sp.simplify(T[1, 1].subs(subs_on_axis))
    print(f"  T_radial (T_zz on z-axis)     = {T_radial}")
    print(f"  T_tangential_x (T_xx on z-axis) = {T_tangential_x}")
    print(f"  T_tangential_y (T_yy on z-axis) = {T_tangential_y}")
    assert sp.simplify(T_tangential_x - T_tangential_y) == 0, (
        "tangential components disagree -- not axially symmetric as expected"
    )

    print("\n[STEP 4] The load-bearing check -- is T_radial equal to T_tangential?")
    print("  (isotropic stress, NO slip source) or different (anisotropic,")
    print("  a GENUINE slip source, magnitude not yet computed here):")
    anisotropy = sp.simplify(T_radial - T_tangential_x)
    print(f"  T_radial - T_tangential = {anisotropy}")
    is_isotropic = anisotropy == 0
    print(f"  Isotropic (no anisotropic stress)?  {is_isotropic}")
    assert not is_isotropic, (
        "UNEXPECTED: T_ij came out isotropic -- would need re-examination, "
        "contradicts the standard result for a static scalar gradient"
    )

    print("\n[STEP 5] Cross-check via the trace -- sum of the three diagonal")
    print("  components should equal -(1/2)*(grad phi)^2 (trace(T_ij) =")
    print("  sum_i[(d_i phi)^2] - 3*(1/2)*(grad phi)^2 = (grad phi)^2 - (3/2)*(grad")
    print("  phi)^2 = -(1/2)*(grad phi)^2 in 3 spatial dimensions):")
    trace = sp.simplify(T[0, 0] + T[1, 1] + T[2, 2])
    grad_sq_full = sp.simplify(
        sp.diff(phi_expr, x) ** 2 + sp.diff(phi_expr, y) ** 2 + sp.diff(phi_expr, z) ** 2
    )
    expected_trace = sp.simplify(-grad_sq_full / 2)
    trace_check = sp.simplify(trace - expected_trace)
    print(f"  trace(T_ij) - (-(1/2)*(grad phi)^2) = {trace_check}")
    assert trace_check == 0, "trace does not match the expected standard formula"

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("Phi's own static stress tensor, for the SAME field P35 already derived,")
    print("has a GENUINELY nonzero anisotropic (radial vs. tangential) part:")
    print(f"  T_radial - T_tangential = {anisotropy}  (nonzero for all r>0)")
    print("This is the standard, well-known structure for a static scalar-field")
    print("gradient's own stress-energy (same pattern as, e.g., a global monopole's")
    print("gradient energy in cosmology). CONSEQUENCE for P35's own withdrawn slip")
    print("claim: a genuine SOURCE for a metric slip (Phi != Psi) exists at the SAME")
    print("O(g_hat^2) order as Delta_G itself -- confirming, via direct calculation,")
    print("that P35's original 'second-order-small, no slip' claim could not have")
    print("been right, and that its later withdrawal (genuinely open, not resolved)")
    print("was the correct, honest status -- now sharpened: a source DOES exist, its")
    print("MAGNITUDE on the actual metric potentials Phi,Psi is NOT computed here")
    print("(would require solving the linearized Einstein ij-equation sourced by")
    print("this T_ij, a separate, larger next step, not attempted in this finding).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
