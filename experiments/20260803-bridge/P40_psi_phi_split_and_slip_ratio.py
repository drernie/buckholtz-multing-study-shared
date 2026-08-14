"""P40 -- seventh step of the covariant-completion campaign (see
PLAN_final_goal_20260814.md), continuing at the deliberately slower,
one-step-at-a-time pace per explicit user instruction. P39 showed the
planned P22/P31 numeric (SI-unit) comparison is blocked, so this step
takes the OTHER available next step from the campaign plan's own table
(the "P36" row: derive the slip ratio gamma and check the plan's own kill
signal, "does gamma come out exactly 1?") -- staying entirely within the
c=1-relative, already-internally-verified P37/P38 chain, not touching the
still-open SI-units question P39 raised.

MOST IMPORTANT MOTIVATION FOR THIS STEP: during the P38 correction, the
context-blind skeptic reviewer suggested (as a bonus, not its core
criticism) that "Phi_phi=0 exactly" might follow from pairing P38's own
Phi-Psi result with the 00-sector solve. That was explicitly DECLINED at
the time, after "an independent hand-check during correction found this
specific claim does NOT hold (Phi_phi came out nonzero)" -- but that
check was itself a quick, undocumented, unverified hand calculation, not
a mechanically-checked one. Redoing it carefully here, with sympy, found
a DIFFERENT answer than the quick hand-check did (the quick check appears
to have used the wrong Poisson-equation normalization -- the standard
"Laplacian(Psi)=4*pi*G_N*rho" instead of P38's own carefully-DERIVED
"G_00=2*Laplacian(Psi)" relation). This script resolves that discrepancy
mechanically before it propagates any further, and reports honestly which
of the two prior claims (P38's skeptic, or P38's own declining hand-check)
was actually right.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - L0 descriptive
"""

import sympy as sp


def linearized_christoffels(coords, h):
    """Identical to P38's own already-skeptic-confirmed implementation
    (P38_metric_slip_from_phi_anisotropic_stress.py) -- re-stated here, not
    re-derived, since standalone scripts in this project don't cross-import.
    Gamma^(1)^lambda_{mu nu} = (1/2)*eta^{lambda sigma}*(d_mu h_{sigma nu}
    + d_nu h_{sigma mu} - d_sigma h_{mu nu}), linear order, mostly-plus
    signature."""
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
    """Identical to P38's own implementation -- see P38 for the standard
    linearized-gravity Gamma*Gamma-drops-out justification."""
    n = 4
    R = sp.zeros(n, n)
    for mu in range(n):
        for nu in range(n):
            term1 = sum(sp.diff(Gamma[(lam, mu, nu)], coords[lam]) for lam in range(n))
            term2 = sum(sp.diff(Gamma[(lam, mu, lam)], coords[nu]) for lam in range(n))
            R[mu, nu] = sp.simplify(term1 - term2)
    return R


def linearized_einstein_tensor(R, eta_diag):
    """Identical to P38's own implementation."""
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
    ghat, M, G_N = sp.symbols("g_hat M G_N", positive=True)
    r = sp.sqrt(x**2 + y**2 + z**2)

    print("=" * 78)
    print("P40 -- solving the 00-sector for Psi_phi, combining with P38's own")
    print("Phi-Psi to get Phi_phi, then the leading-order slip ratio gamma")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    print("\n[STEP 1] Re-derive P38's own G_00=2*Laplacian(Psi) relation, as a")
    print("  POSITIVE CONTROL that this script's copy of the linearized-Einstein")
    print("  machinery is identical to P38's already-skeptic-confirmed version")
    print("  before using it to solve anything new:")
    Phi = sp.Function("Phi")(x, y, z)
    Psi = sp.Function("Psi")(x, y, z)
    h = [[0, 0, 0, 0] for _ in range(4)]
    h[0][0] = -2 * Phi
    h[1][1] = h[2][2] = h[3][3] = -2 * Psi
    Gamma = linearized_christoffels(coords, h)
    R = linearized_ricci(coords, Gamma)
    G, _ = linearized_einstein_tensor(R, eta_diag)
    G_00 = sp.simplify(G[0, 0])
    laplacian_Psi = sp.diff(Psi, x, 2) + sp.diff(Psi, y, 2) + sp.diff(Psi, z, 2)
    control_check = sp.simplify(G_00 - 2 * laplacian_Psi)
    print(f"  G_00 = {G_00}")
    print(f"  G_00 - 2*Laplacian(Psi) = {control_check}")
    assert control_check == 0, "does not match P38's own established G_00 relation"
    print("  -> PASSES: identical to P38's own result. Safe to build on.")

    print("\n[STEP 2] P37's own established T_00 = (1/2)*(grad phi)^2, for the")
    print("  SAME field phi(r)=g_hat*M/(4*pi*r) P35/P37/P38 all reuse unchanged:")
    phi_expr = ghat * M / (4 * sp.pi * r)
    grad_phi_sq = sum(sp.diff(phi_expr, c) ** 2 for c in (x, y, z))
    T_00 = sp.simplify(grad_phi_sq / 2)
    print(f"  T_00 = {T_00}")

    print("\n[STEP 3] Solve G_00 = 8*pi*G_N*T_00, i.e. 2*Laplacian(Psi) =")
    print("  8*pi*G_N*T_00, for Psi_phi -- same ansatz+solve+verify pattern P38")
    print("  used for Phi-Psi. Ansatz D/r^2 (Laplacian(1/r^2) gives a pure 1/r^4")
    print("  radial falloff, matching T_00's own r-dependence):")
    D = sp.Symbol("D")
    Psi_trial = D / (x**2 + y**2 + z**2)
    laplacian_trial = sp.simplify(
        sp.diff(Psi_trial, x, 2) + sp.diff(Psi_trial, y, 2) + sp.diff(Psi_trial, z, 2)
    )
    equation = sp.Eq(2 * laplacian_trial, 8 * sp.pi * G_N * T_00)
    solution = sp.solve(equation, D)
    print(f"  2*Laplacian(D/r^2) = {laplacian_trial}")
    print(f"  equation: {equation}")
    print(f"  solved D = {solution}")
    assert len(solution) == 1, f"expected exactly one solution, got {solution}"
    D_solved = solution[0]
    Psi_phi = D_solved / (x**2 + y**2 + z**2)
    print(f"  => Psi_phi = ({D_solved}) / r^2")

    print("\n[STEP 4] INDEPENDENT VERIFICATION -- substitute D back into the FULL")
    print("  equation (not just the ansatz-matching shortcut) at a generic point:")
    residual = sp.simplify(2 * laplacian_trial.subs(D, D_solved) - 8 * sp.pi * G_N * T_00)
    print(f"  residual = {residual}")
    assert residual == 0, "independent verification failed"
    print("  -> PASSES: exact zero residual for generic (x,y,z).")

    print("\n[STEP 5] Combine with P38's own (skeptic-confirmed) Phi-Psi to get")
    print("  Phi_phi = Psi_phi + (Phi-Psi). This is the SAME calculation the P38")
    print("  skeptic suggested and this project explicitly DECLINED to adopt at")
    print("  the time (per audit-verification-gate.md) pending independent")
    print("  verification -- done here, mechanically, for the first time:")
    phi_minus_psi = -G_N * ghat**2 * M**2 / (16 * sp.pi * (x**2 + y**2 + z**2))
    Phi_phi = sp.simplify(Psi_phi + phi_minus_psi)
    print(f"  Psi_phi       = {Psi_phi}")
    print(f"  Phi-Psi (P38) = {phi_minus_psi}")
    print(f"  Phi_phi = Psi_phi + (Phi-Psi) = {Phi_phi}")
    is_zero = Phi_phi == 0
    print(f"  Phi_phi == 0 exactly?  {is_zero}")

    print("\n[STEP 6] Honest reconciliation with this project's own prior record.")
    print("  FINDING_P38's own text recorded declining the skeptic's 'Phi_phi=0'")
    print("  suggestion because 'an independent hand-check ... found Phi_phi came")
    print("  out nonzero.' That hand-check is not reproducible from the committed")
    print("  record (no script, no shown work) and, redone here mechanically, the")
    print("  result is different. The most likely explanation: the undocumented")
    print("  hand-check used the standard-textbook Poisson form")
    print("  Laplacian(Psi)=4*pi*G_N*rho, NOT P38's own carefully-DERIVED")
    print("  G_00=2*Laplacian(Psi) relation (Step 1 above) -- a factor-of-2 slip")
    print("  in exactly the kind of quick, unverified aside this project's own")
    print("  discipline (audit-verification-gate.md) exists to catch.")

    print("\n[STEP 7] Only meaningful if Phi_phi==0 (checked above): assemble the")
    print("  FULL leading-order Phi, Psi (unmodified Newtonian base Phi_N, per")
    print("  P34's own flag that S_EH is standard/unmodified, plus this order's")
    print("  correction), and compute the slip ratio gamma:=Psi/Phi -- the")
    print("  campaign plan's own PLAN_final_goal_20260814.md 'P36' table row")
    print("  kill signal: 'if quasi-static mu,gamma come out EXACTLY Q=1,R=1 ...")
    print("  document and stop this branch, do not force a distinguishing claim':")
    gamma_minus_1 = None
    if is_zero:
        r_sym = sp.Symbol("r", positive=True)
        Phi_N = -G_N * M / r_sym
        Psi_full = Phi_N + D_solved / r_sym**2
        Phi_full = Phi_N  # + Phi_phi, but Phi_phi=0
        gamma = sp.simplify(Psi_full / Phi_full)
        gamma_minus_1 = sp.simplify(gamma - 1)
        print(f"  Phi_N (standard, unmodified)         = {Phi_N}")
        print(f"  Psi   = Phi_N + Psi_phi               = {Psi_full}")
        print(f"  Phi   = Phi_N + Phi_phi (Phi_phi=0)   = {Phi_full}")
        print(f"  gamma := Psi/Phi                      = {gamma}")
        print(f"  gamma - 1                             = {gamma_minus_1}")
        assert gamma_minus_1 != 0, (
            "gamma came out exactly 1 -- the plan's own null-result kill signal "
            "would apply; re-check before reporting a distinguishing claim"
        )
        print("  -> gamma != 1: this is a REAL, nonzero, O(g_hat^2) slip signature,")
        print("     not the null result the plan's own kill signal warned about.")
    else:
        print("  SKIPPED -- Phi_phi != 0, so Phi is not simply Phi_N; a full gamma")
        print("  computation would need Phi_phi included too, not attempted here.")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print(f"Psi_phi = {Psi_phi}")
    print(f"Phi_phi = {Phi_phi}")
    if is_zero:
        print("Phi_phi = 0 EXACTLY -- confirmed mechanically. This project's own")
        print("earlier decision to decline this claim (in FINDING_P38) was itself")
        print("based on an unverified, and apparently mistaken, quick hand-check --")
        print("not a failure of the discipline that declined it (declining an")
        print("unverified claim was the CORRECT process move at the time), but the")
        print("declining hand-check's own result does not survive mechanical")
        print("re-derivation and should be corrected in FINDING_P38's own record.")
        print(f"gamma - 1 = {gamma_minus_1}  (nonzero -- a real slip signature)")
    else:
        print("Phi_phi != 0 -- the P38 skeptic's suggestion does NOT hold, matching")
        print("(for once, on the actual arithmetic) the project's prior hand-check,")
        print("even though that hand-check's own reasoning was never documented.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
