"""P189: answer docs/153 Sec3a's 3 pre-conditions for reopening
bottleneck 1 (F->H_MULT(z), finite-r/single-pair compatibility).

REJECTED -- see FINDING_P189_finite_r_preconditions.md. The controls
below genuinely pass (the algebra is self-consistent, tier-distinguishing,
and reproduces docs/127's own r->inf result exactly) -- but a skeptic
pass found the CONCLUSION drawn from that passing algebra does not
follow: removing docs/127's r->inf limit does not give a physically
meaningful finite-r closure (that limit encodes a population-averaging
scale, not a single-pair separation -- reusing the same "r" for both is
a category error), and "nonzero at finite r" is a tautology of any
power-law-decaying f(r), not a MULTING-specific result (verified with
sympy: f(r)=c/r^n gives f-r*f'=(n+1)c/r^n for EVERY n>=1). Kept as-run,
unedited, per this project's no-silent-correction convention -- read
this file's output alongside the FINDING, not instead of it.

Original framing: docs/127's own closure quantity
    G_eff = G * lim_{r->inf} [f(r) - r*f'(r)]
(their Eq. 22, phi(r) = -(G/r)*f(r)) was claimed to be ALREADY a
closed-form function of r before the limit is taken. See the FINDING
for why this claim was rejected.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
See CLAIM_P189_finite_r_preconditions.md for the full protocol.
"""

import sympy as sp

r = sp.Symbol("r", positive=True)
G = sp.Symbol("G", positive=True)


def g_eff_finite(f_expr):
    """docs/127 Eq. 22, WITHOUT taking the r->inf limit."""
    return sp.simplify(G * (f_expr - r * sp.diff(f_expr, r)))


def g_eff_asymptotic(f_expr):
    """docs/127 Eq. 22, exactly as published (the r->inf limit)."""
    return sp.limit(G * (f_expr - r * sp.diff(f_expr, r)), r, sp.oo)


# The three MULTING tiers' f(r), from docs/127's own table:
# monopole: phi ~ -G/r        -> f(r) = 1
# dipole:   phi ~ 1/r^2       -> f(r) = c_d/r
# quadrupole: phi ~ 1/r^3     -> f(r) = c_q/r^2
c_d, c_q = sp.symbols("c_d c_q", positive=True)
F_MONOPOLE = sp.Integer(1)
F_DIPOLE = c_d / r
F_QUADRUPOLE = c_q / r**2


def positive_control():
    """Reproduce docs/127's own published asymptotic result exactly."""
    print("=== POSITIVE CONTROL: reproduce docs/127's own G_eff (r->inf) ===")
    checks = [
        ("monopole", F_MONOPOLE, G),
        ("dipole", F_DIPOLE, sp.Integer(0)),
        ("quadrupole", F_QUADRUPOLE, sp.Integer(0)),
    ]
    all_ok = True
    for name, f_expr, expected in checks:
        got = g_eff_asymptotic(f_expr)
        ok = sp.simplify(got - expected) == 0
        all_ok &= ok
        print(f"  {name:12} G_eff(r->inf) = {got}   expected {expected}   {'OK' if ok else 'FAIL'}")
    assert all_ok, "positive control FAILED -- docs/127's own result not reproduced"
    print("  PASS: docs/127's published G_eff values reproduced exactly.\n")


def negative_control():
    """Confirm the finite-r expression is sensitive to which tier's kernel
    is used -- not a tautology that returns the same thing regardless."""
    print("=== NEGATIVE CONTROL: does tier choice actually matter? ===")
    g_mono = g_eff_finite(F_MONOPOLE)
    g_dip = g_eff_finite(F_DIPOLE)
    g_quad = g_eff_finite(F_QUADRUPOLE)
    distinct = len({sp.simplify(g_mono - g_dip), sp.simplify(g_dip - g_quad), 0}) > 1 or (
        sp.simplify(g_mono - g_dip) != 0 and sp.simplify(g_dip - g_quad) != 0
    )
    print(f"  G_finite(monopole)   = {g_mono}")
    print(f"  G_finite(dipole)     = {g_dip}")
    print(f"  G_finite(quadrupole) = {g_quad}")
    print(f"  distinct across tiers: {distinct}")
    assert distinct, "negative control FAILED -- calculation is tier-insensitive (tautology)"
    print("  PASS: calculation discriminates between tiers, not a tautology.\n")


def precondition_1():
    print("=== PRE-CONDITION 1: does a finite-r closed form exist? ===")
    g_dip = g_eff_finite(F_DIPOLE)
    g_quad = g_eff_finite(F_QUADRUPOLE)
    print(f"  G_finite,dipole(r)     = {g_dip}")
    print(f"  G_finite,quadrupole(r) = {g_quad}")
    print("  Both are closed-form, elementary functions of r -- no new")
    print("  derivation needed beyond removing docs/127's own r->inf limit.")
    print("  ANSWER: YES, a finite-r closed form exists trivially.\n")
    return g_dip, g_quad


def precondition_2():
    print("=== PRE-CONDITION 2: tractable with existing machinery? ===")
    print("  two_field_action_closure.py::tiers_from_kernel(K) already")
    print("  computes single-pair, finite-r symbolic tier expressions for")
    print("  an arbitrary kernel K(s) -- confirmed by direct source read")
    print("  (see FINDING_P189 for the fact-finding trail). The f(r) forms")
    print("  used above (c_d/r, c_q/r^2) are the SAME functional forms that")
    print("  file's own K'', K''' derivatives produce for a massless kernel.")
    print("  ANSWER: YES, tractable with existing machinery -- no new code")
    print("  architecture needed, only evaluating an existing formula at a")
    print("  different point instead of a limit.\n")


def precondition_3(g_dip, g_quad):
    print("=== PRE-CONDITION 3: cost vs. consequence ===")
    print("  QUALITATIVE result (pure algebra, unit-independent, solid):")
    print("  G_finite,dipole(r) = 2*G*c_d/r and G_finite,quadrupole(r) = 3*G*c_q/r^2")
    print("  are IDENTICALLY NONZERO for any r < infinity and any c_d, c_q != 0 --")
    print("  this holds regardless of what units/normalization c_d, c_q carry,")
    print("  since it is a statement about the FUNCTIONAL FORM (1/r, 1/r^2),")
    print("  not about any specific numeric value.")
    print()
    print("  ATTEMPTED, NOT COMPLETED: a numeric magnitude at v82's own r=d0,")
    print("  using v82's own archive values. This requires mapping docs/127's")
    print("  abstract kernel normalization (phi(r) = -(G/r)*f(r), f(r)")
    print("  dimensionless by construction, since f(monopole)=1 -> G_eff=G)")
    print("  onto v82's own DIMENSIONED force expressions (F1, F2 in Newtons,")
    print("  from multing_core.py::forces()). A first attempt (c_d = (k/c^2)*R,")
    print("  by analogy with v82's own F1 coefficient) gives a ratio to G of")
    print("  order 1e37-1e75 -- physically implausible on its face, and traced")
    print("  to a genuine units mismatch: (k/c^2)*R has units of mass*length,")
    print("  not the dimensionless-f(r)-times-length that c_d/r requires for")
    print("  f(r) to match f(monopole)=1's own dimensionless convention.")
    print("  FLAGGED, NOT FIXED: getting this normalization right requires")
    print("  properly relating docs/127's per-unit-source-mass potential")
    print("  convention to v82's own two-body reduced-mass force law -- real")
    print("  derivation work, not a numeric plug-in. This is itself informative")
    print("  for pre-condition 1: the finite-r FUNCTIONAL FORM is free (already")
    print("  derived), but a properly-normalized finite-r NUMBER is not yet in")
    print("  hand -- pre-condition 1's closed-form claim should be read as")
    print("  'closed form for the r-dependence,' not 'a ready-to-evaluate number.'")
    print()
    print("  ANSWER TO PRE-CONDITION 3 (on the qualitative result alone):")
    print("  the finite-r and r->inf regimes are NOT trivially/tautologically")
    print("  the same (one is identically zero by construction, the other is")
    print("  identically nonzero by construction) -- so the real finite-r/")
    print("  single-pair closure calculation docs/153 names is NOT a")
    print("  foregone conclusion either way; it has real content to discover,")
    print("  which is what makes its cost worth paying. The specific magnitude")
    print("  -- how large the effect is relative to v82's own beta_1, beta_2 --")
    print("  remains open and would be the first concrete deliverable of that")
    print("  calculation, not something this pre-condition check could shortcut.")


def main():
    positive_control()
    negative_control()
    g_dip, g_quad = precondition_1()
    precondition_2()
    precondition_3(g_dip, g_quad)


if __name__ == "__main__":
    main()
