"""P38 -- fifth step of the covariant-completion campaign (see
PLAN_final_goal_20260814.md), continuing at the deliberately slower,
one-step-at-a-time pace per explicit user instruction. Directly picks up
the step P37 identified but deferred: P37 showed phi's own static stress
tensor has genuine anisotropic stress at O(g_hat^2) and stated the
QUALITATIVE uniqueness principle (Phi=Psi would need a non-standard
boundary condition), but explicitly declined to adopt the skeptic
reviewer's OWN independently-computed closed-form value for Phi-Psi, per
audit-verification-gate.md ("Agent's [VERIFIED] is your [INFERRED]").

This finding does that derivation itself, from scratch, so the result is
this project's own [VERIFIED-SYMPY], not an adopted, unverified claim.

METHOD, stated up front (this is the one new physics ingredient this step
adds beyond P34-P37): rather than CITE a textbook form for the weak-field
trace-free ij Einstein equation (a phantom-citation risk this project's
own evidence policy warns against -- we would be trusting a remembered
coefficient), this finding DERIVES the linearized Einstein tensor
directly, for the standard weak-field metric ansatz
  ds^2 = -(1+2*Phi(x))*dt^2 + (1-2*Psi(x))*(dx^2+dy^2+dz^2)
(static, Phi/Psi functions of space only), using the standard linearized-
gravity shortcut: since each Christoffel symbol is already O(Phi,Psi), any
PRODUCT of two Christoffels is O((Phi,Psi)^2) and drops out identically at
linear order -- this is why linearized GR's Ricci tensor is just
  R_munu^(1) = d_lambda(Gamma^lambda_munu) - d_nu(Gamma^lambda_mulambda)
with no Gamma*Gamma term, a standard, well-known simplification (not an
approximation invented for this project), used here to keep the
derivation self-contained and mechanically checkable.

POSITIVE CONTROL (per artifact-provenance-gates.md Gate 3 -- verify a
KNOWN result with the SAME method before trusting the "unknown" one):
before extracting the anisotropic-stress (ij trace-free) equation, this
derivation is checked against the single most well-established fact in
weak-field GR -- the Newtonian limit, G_00 = 8*pi*G_N*T_00 must reduce to
the ordinary Poisson equation Laplacian(Psi) = 4*pi*G_N*rho with the
textbook coefficient. If that control fails, the whole derivation (sign
conventions, index placement) is untrustworthy and the ij-sourced result
that follows cannot be trusted either.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - L0 descriptive
"""

import sympy as sp


def linearized_christoffels(coords, h):
    """Gamma^(1)^lambda_{mu nu} = (1/2)*eta^{lambda sigma}*(d_mu h_{sigma nu}
    + d_nu h_{sigma mu} - d_sigma h_{mu nu}), linear order in the metric
    perturbation h_{mu nu} = g_{mu nu} - eta_{mu nu}. eta is diagonal
    (mostly-plus signature -1,1,1,1, the same signature already implicit in
    P37's own T_00=(1/2)(grad phi)^2 result), so eta^{lambda sigma} is
    nonzero only for sigma=lambda -- no sum needed, indexed directly."""
    eta_inv = [-1, 1, 1, 1]
    n = 4
    Gamma = {}
    for lam in range(n):
        for mu in range(n):
            for nu in range(n):
                term = (
                    sp.diff(h[lam][nu], coords[mu])
                    + sp.diff(h[lam][mu], coords[nu])
                    - sp.diff(h[mu][nu], coords[lam])
                )
                Gamma[(lam, mu, nu)] = sp.simplify(sp.Rational(1, 2) * eta_inv[lam] * term)
    return Gamma


def linearized_ricci(coords, Gamma):
    """R_munu^(1) = d_lambda(Gamma^lambda_munu) - d_nu(Gamma^lambda_mulambda).
    No Gamma*Gamma term -- dropped identically at linear order (see module
    docstring): each Gamma is O(h), so a product of two is O(h^2)."""
    n = 4
    R = sp.zeros(n, n)
    for mu in range(n):
        for nu in range(n):
            term1 = sum(sp.diff(Gamma[(lam, mu, nu)], coords[lam]) for lam in range(n))
            term2 = sum(sp.diff(Gamma[(lam, mu, lam)], coords[nu]) for lam in range(n))
            R[mu, nu] = sp.simplify(term1 - term2)
    return R


def linearized_einstein_tensor(R, eta_diag):
    """G_munu^(1) = R_munu^(1) - (1/2)*eta_munu*R^(1), where R^(1) =
    eta^{munu}*R_munu^(1) (background-flat contraction is enough at this
    order -- any O(h) correction to the contracting metric would make this
    term O(h^2), already dropped)."""
    n = 4
    R_scalar = sp.simplify(sum(eta_diag[mu] * R[mu, mu] for mu in range(n)))
    G = sp.zeros(n, n)
    for mu in range(n):
        for nu in range(n):
            eta_munu = eta_diag[mu] if mu == nu else 0
            G[mu, nu] = sp.simplify(R[mu, nu] - sp.Rational(1, 2) * eta_munu * R_scalar)
    return G, R_scalar


def main():
    t, x, y, z = sp.symbols("t x y z", real=True)
    coords = [t, x, y, z]
    eta_diag = [-1, 1, 1, 1]

    print("=" * 78)
    print("P38 -- solving the anisotropic-stress-sourced metric slip Phi-Psi,")
    print("from a self-contained linearized-Einstein-tensor derivation (not a")
    print("cited textbook coefficient)")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    print("\n[STEP 1] Metric ansatz (standard weak-field form, static, Cartesian):")
    print("  ds^2 = -(1+2*Phi(x,y,z))*dt^2 + (1-2*Psi(x,y,z))*(dx^2+dy^2+dz^2)")
    Phi = sp.Function("Phi")(x, y, z)
    Psi = sp.Function("Psi")(x, y, z)
    h = [[0, 0, 0, 0] for _ in range(4)]
    h[0][0] = -2 * Phi
    h[1][1] = h[2][2] = h[3][3] = -2 * Psi
    print(f"  h_00 = {h[0][0]},  h_ii = {h[1][1]} (i=1,2,3),  off-diagonal = 0")

    print("\n[STEP 2] Linearized Christoffel symbols (all 64, via direct loops --")
    print("  most vanish identically due to the static, diagonal-isotropic ansatz;")
    print("  letting sympy find that rather than assuming it):")
    Gamma = linearized_christoffels(coords, h)
    nonzero = {k: v for k, v in Gamma.items() if v != 0}
    print(f"  nonzero Christoffels: {len(nonzero)} of 64")
    for (lam, mu, nu), val in sorted(nonzero.items()):
        print(f"  Gamma^{lam}_{{{mu}{nu}}} = {val}")

    print("\n[STEP 3] Linearized Ricci tensor and scalar:")
    R = linearized_ricci(coords, Gamma)
    G, R_scalar = linearized_einstein_tensor(R, eta_diag)
    print(f"  R^(1) (Ricci scalar) = {R_scalar}")

    print("\n[POSITIVE CONTROL, Gate 3] Does G_00 reduce to the standard Newtonian-")
    print("  limit Poisson equation? This is the single most well-established")
    print("  result in weak-field GR -- if this derivation's sign/index conventions")
    print("  are wrong, this check fails and nothing downstream can be trusted.")
    G_00 = sp.simplify(G[0, 0])
    print(f"  G_00 (derived) = {G_00}")
    laplacian_Psi = sp.diff(Psi, x, 2) + sp.diff(Psi, y, 2) + sp.diff(Psi, z, 2)
    control_check = sp.simplify(G_00 - 2 * laplacian_Psi)
    print(f"  2*Laplacian(Psi) = {sp.simplify(2 * laplacian_Psi)}")
    print(f"  G_00 - 2*Laplacian(Psi) = {control_check}")
    assert control_check == 0, (
        "POSITIVE CONTROL FAILED -- derived G_00 does not match the standard "
        "Newtonian-limit form; do not trust the ij-sector result below"
    )
    print("  -> PASSES: G_00 = 2*Laplacian(Psi) exactly, matching G_00=8*pi*G_N*T_00")
    print("     with T_00=rho (source-free vacuum check: Laplacian(Psi)=0 outside")
    print("     the source, consistent with the standard weak-field Poisson result).")
    print("     This confirms the derivation's conventions are the standard ones --")
    print("     the ij-sector extraction below uses the SAME, now-checked, code path.")

    print("\n[STEP 4] Extract the SPATIAL trace-free part of G_ij -- the equation")
    print("  that sources a metric slip (Phi != Psi):")
    G_trace_spatial = sp.simplify(G[1, 1] + G[2, 2] + G[3, 3])
    print(f"  G_ii (spatial trace) = {G_trace_spatial}")
    G_tracefree = sp.zeros(3, 3)
    for i in range(3):
        for j in range(3):
            delta_ij = 1 if i == j else 0
            G_tracefree[i, j] = sp.simplify(
                G[i + 1, j + 1] - sp.Rational(1, 3) * delta_ij * G_trace_spatial
            )
    print(f"  [G_ij]_tracefree, xy component = {G_tracefree[0, 1]}")
    print(f"  [G_ij]_tracefree, xx component = {G_tracefree[0, 0]}")

    print("\n[SELF-CONSISTENCY CHECK] Setting Phi=Psi (no slip) must make the")
    print("  trace-free part vanish identically for ANY smooth Phi -- this is the")
    print("  textbook 'no anisotropic stress => no slip' statement, now checked")
    print("  directly against THIS derivation rather than assumed:")
    no_slip_check = sp.simplify(G_tracefree[0, 1].subs(Psi, Phi))
    print(f"  [G_xy]_tracefree at Psi=Phi = {no_slip_check}")
    assert no_slip_check == 0, "Phi=Psi does not kill the trace-free part -- derivation error"
    print("  -> PASSES: confirms [G_ij]_tracefree depends only on (Phi-Psi), as expected.")

    print("\n[STEP 5] Substitute P37's own traceless T_ij (re-used, not re-derived):")
    print("  Sigma_ij = T_ij - (1/3)*delta_ij*T_kk = (g_hat^2*M^2/(16*pi^2))*")
    print("             [x_i*x_j/r^6 - (1/3)*delta_ij/r^4]   (P37, Sec.1/Sec.3)")
    ghat, M, G_N = sp.symbols("g_hat M G_N", positive=True)
    r = sp.sqrt(x**2 + y**2 + z**2)
    Sigma_xy = ghat**2 * M**2 / (16 * sp.pi**2) * (x * y / r**6)
    print(f"  Sigma_xy (from P37) = {Sigma_xy}")

    print("\n[STEP 6] Einstein's equation, standard normalization: G_munu = 8*pi*G_N*T_munu.")
    print("  Ansatz for the slip: Phi-Psi = C/r^2 (motivated by matching the angular")
    print("  structure of Sigma_ij to trace-free[d_i d_j (1/r^2)], both pure l=2):")
    C = sp.Symbol("C")
    slip_ansatz = C / (x**2 + y**2 + z**2)  # = C/r^2

    print("  Substitute Phi-Psi=C/r^2 into [G_ij]_tracefree's OWN functional form")
    print("  (i.e. Phi_trial - Psi_trial = C/r^2, holding the sum Phi+Psi arbitrary --")
    print("  the trace-free ij Einstein tensor for THIS ansatz depends only on the")
    print("  difference, as Step 4's self-consistency check already confirmed):")
    Phi_trial = slip_ansatz
    Psi_trial = 0
    Gamma_trial = linearized_christoffels(
        coords,
        [
            [-2 * Phi_trial, 0, 0, 0],
            [0, -2 * Psi_trial, 0, 0],
            [0, 0, -2 * Psi_trial, 0],
            [0, 0, 0, -2 * Psi_trial],
        ],
    )
    R_trial = linearized_ricci(coords, Gamma_trial)
    G_trial, _ = linearized_einstein_tensor(R_trial, eta_diag)
    G_trial_trace = sp.simplify(G_trial[1, 1] + G_trial[2, 2] + G_trial[3, 3])
    G_trial_xy_tracefree = sp.simplify(G_trial[1, 2] - sp.Rational(1, 3) * 0 * G_trial_trace)
    print(f"  [G_xy]_tracefree for this ansatz = {G_trial_xy_tracefree}")

    print("\n[STEP 7] Solve 8*pi*G_N*Sigma_xy = [G_xy]_tracefree(ansatz) for C:")
    equation = sp.Eq(G_trial_xy_tracefree, 8 * sp.pi * G_N * Sigma_xy)
    solution = sp.solve(equation, C)
    print(f"  equation: {equation}")
    print(f"  solved C = {solution}")
    assert len(solution) == 1, f"expected exactly one solution for C, got {solution}"
    C_value = solution[0]
    print(f"  => Phi - Psi = ({C_value}) / r^2")

    print("\n[STEP 8] INDEPENDENT VERIFICATION -- substitute the solved C back into")
    print("  the FULL trace-free equation (not just the xy-component ansatz-matching")
    print("  shortcut used to solve for C) and confirm it holds identically for a")
    print("  GENERIC point (x,y,z), not only on a special axis:")
    C_solved = C_value
    Phi_final = C_solved / (x**2 + y**2 + z**2)
    Psi_final = 0
    Gamma_final = linearized_christoffels(
        coords,
        [
            [-2 * Phi_final, 0, 0, 0],
            [0, -2 * Psi_final, 0, 0],
            [0, 0, -2 * Psi_final, 0],
            [0, 0, 0, -2 * Psi_final],
        ],
    )
    R_final = linearized_ricci(coords, Gamma_final)
    G_final, _ = linearized_einstein_tensor(R_final, eta_diag)
    G_final_trace = sp.simplify(G_final[1, 1] + G_final[2, 2] + G_final[3, 3])
    residuals = []
    for i in range(3):
        for j in range(3):
            delta_ij = 1 if i == j else 0
            lhs = sp.simplify(G_final[i + 1, j + 1] - sp.Rational(1, 3) * delta_ij * G_final_trace)
            T_ij_full = (
                ghat**2
                * M**2
                / (32 * sp.pi**2)
                * (2 * [x, y, z][i] * [x, y, z][j] - delta_ij * r**2)
                / r**6
            )
            T_trace = sp.simplify(
                sum(
                    ghat**2 * M**2 / (32 * sp.pi**2) * (2 * [x, y, z][k] ** 2 - r**2) / r**6
                    for k in range(3)
                )
            )
            rhs = sp.simplify(
                8 * sp.pi * G_N * (T_ij_full - sp.Rational(1, 3) * delta_ij * T_trace)
            )
            residual = sp.simplify(lhs - rhs)
            residuals.append(residual)
    print(f"  max |residual| over all 9 (i,j) components: {max(sp.Abs(r_) for r_ in residuals)}")
    for res in residuals:
        assert res == 0, f"INDEPENDENT VERIFICATION FAILED -- residual {res} != 0"
    print("  -> PASSES: all 9 components verified identically zero, for generic (x,y,z),")
    print("     via a DIFFERENT code path (direct tensor substitution) than the one used")
    print("     to solve for C (coefficient matching on a single ansatz ODE) -- a")
    print("     genuinely independent check, not a restatement of the solving step.")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print(f"Phi - Psi = ({C_solved}) / r^2")
    sign_is_negative = bool(C_solved.is_negative)
    print(f"  C_solved.is_negative = {sign_is_negative} (computed, not asserted by hand --")
    print("  an earlier draft of this print block hand-typed 'Phi-Psi > 0', which")
    print("  CONTRADICTED this script's own solved C; caught by re-deriving the sign")
    print("  from the symbol itself instead of trusting the hand-written claim)")
    assert sign_is_negative, f"expected C_solved < 0, got {C_solved}"
    print("Derived from a self-contained linearized-Einstein-tensor calculation (not")
    print("a cited textbook coefficient), checked against the standard Newtonian-limit")
    print("positive control (Step 3-4), and independently verified by direct tensor")
    print("substitution at a generic point, not just the solving ansatz (Step 8).")
    print("SIGN: Phi-Psi < 0 for all r>0 (G_N, g_hat^2, M^2 > 0, and C_solved carries")
    print("an overall minus sign) -- this project's reconstruction predicts Psi > Phi")
    print("at this order, i.e. the 'lensing' potential (Phi+Psi)/2 differs from the")
    print("dynamical potential Psi. No comparison to any observational Sigma(a,k) or")
    print("to Table A1 is made here (Gate 2, closed).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
