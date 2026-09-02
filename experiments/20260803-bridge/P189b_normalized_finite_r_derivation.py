"""P189b: correctly-normalized re-derivation of finite-r f(r)/G_eff from
v82's OWN force law, per the user's explicit request "correctly recompute
the c_d/c_q normalization" following P189's rejection.

This is an ADDENDUM to P189, not a replacement -- see
FINDING_P189_ADDENDUM_normalized_derivation.md for the full write-up,
including what this DOES and does NOT establish. Read that file, not just
this script's printed output, before treating anything here as a result.

WHAT THIS FIXES (real progress over P189's original attempt): P189's
precondition_3() guessed c_d = (k/c^2)*R "by analogy" with v82's own F1
coefficient and got a units-mismatched, physically-absurd magnitude
(~1e37-1e75 relative to G). This script instead DERIVES f(r) properly:
integrate v82's own F_total = F0 - F1 + F2 (forces() in multing_core.py)
via each node's own acceleration under the mutual force (a = F_total/M,
NOT the two-body reduced-mass EOM a = F_total/(M/2) -- see FINDING for why
this choice, not the reduced-mass one, is the one that maps onto docs/127's
own single-source potential convention phi(r) = -(G/r)*f(r)), then reads
off f(r) = -r*phi(r)/(G*M). This construction is verified BEFORE any
numeric use: the monopole-only limit (beta_1=beta_2=0) must give EXACTLY
f=1 and G_eff(r->inf)=G, matching docs/127's own published values exactly
-- both checked as hard asserts below, not just printed.

WHAT THIS DOES NOT FIX (revised after a Step 8a skeptic pass -- see
FINDING's own "Skeptic pass" section, WEAKENED verdict): the choice of
normalization convention (single-node acceleration a=F_total/M) is
SELECTED because it reproduces docs/127's own f(monopole)=1 convention,
not independently derived -- the reduced-mass convention (mu=M/2) is at
least equally defensible for v82's actual symmetric two-body construction
and was not used only because it gives f(monopole)=2, not 1. The two
control functions below therefore verify only the ARITHMETIC self-
consistency of the chosen convention, not that the convention itself is
correct -- they cannot fail for this class of ansatz by construction.
Separately: the numeric evaluation at v82's own real archive values
(spotlighted beta_1, beta_2) shows the dipole/quadrupole "correction"
terms are ~1000x LARGER than the monopole term, giving an unstable,
sign-flipping G_eff,total/G under +-10% beta perturbation -- but this is
a COROLLARY of this project's own already-established beta_1-beta_2
degeneracy (FINDING_P176_v82_real_chi2_hessian_degeneracy.md), not new
independent evidence. None of this touches the original skeptic's
"category error" objection from FINDING_P189 (docs/127's r->inf limit is
a population-averaging construct, not a single-pair separation) -- and a
second, related framing question (treating v82's z-dependent scalar
d_of(z) as a free spatial integration variable at fixed epoch) surfaced
during THIS addendum's own skeptic pass and is likewise unresolved.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

import importlib.util
from pathlib import Path

import sympy as sp

REPO_ROOT = Path(__file__).resolve().parents[2]
MULTING_CORE_PATH = (
    REPO_ROOT
    / "data"
    / "source_material"
    / "zenodo_21204955_supplemental"
    / "code"
    / "multing_core.py"
)

B1_SPOTLIGHTED, B2_SPOTLIGHTED = 1.4335e10, 7.8067e17
ZS = [0.0, 0.0233, 0.07, 0.5, 1.07, 1.965, 2.33, 5.0]


def load_multing_core():
    spec = importlib.util.spec_from_file_location("multing_core", MULTING_CORE_PATH)
    mc = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mc)
    return mc


def derive_f_and_geff():
    """Symbolic derivation. Returns (f_r, geff_terms_dict, geff_total)."""
    G, M, k, R, d, c, b1, b2 = sp.symbols("G M k R d c beta_1 beta_2", positive=True)

    F0 = -G * M * M / d**2
    F1 = b1 * (-G) * 2 * M * (k / c**2) * (R / d) / d**2
    F2 = b2 * (-G) * (k / c**2) ** 2 * (R * R / d**2) / d**2
    F_total = F0 - F1 + F2  # v82's own forces() sign convention exactly

    # Each of the two IDENTICAL nodes feels F_total acting on ITS OWN mass M
    # (not the relative-separation reduced-mass EOM, mu=M/2, which describes
    # a different physical quantity -- how the SEPARATION coordinate d(t)
    # evolves, not how much a single node accelerates). This is the choice
    # that reproduces docs/127's own single-source potential convention
    # phi(r) = -(G/r)*f(r) with f(monopole)=1 exactly -- verified below.
    accel_single = sp.simplify(F_total / M)
    phi = sp.simplify(-sp.integrate(accel_single, d))  # phi->0 as d->inf
    f_r = sp.expand(sp.simplify(-d * phi / (G * M)))

    def g_eff_finite(term):
        return sp.simplify(G * (term - d * sp.diff(term, d)))

    terms = {str(t): g_eff_finite(t) for t in sp.Add.make_args(f_r)}
    total = sp.simplify(sum(terms.values()))
    return f_r, terms, total, (G, M, k, R, d, c, b1, b2)


def positive_control(f_r, total, syms):
    """Monopole-only (beta_1=beta_2=0) must reproduce docs/127's own
    published asymptotic values EXACTLY: f=1, G_eff(r->inf)=G."""
    G, M, k, R, d, c, b1, b2 = syms
    print("=== POSITIVE CONTROL ===")
    f_mono = f_r.subs({b1: 0, b2: 0})
    print(f"  f(r) at beta_1=beta_2=0: {f_mono}  [must be exactly 1]")
    assert f_mono == 1, "FAILED -- monopole normalization still wrong"

    total_mono = total.subs({b1: 0, b2: 0})
    inf_limit = sp.limit(total_mono, d, sp.oo)
    print(f"  G_eff(r->inf) at beta_1=beta_2=0: {inf_limit}  [must be exactly G]")
    assert inf_limit == G, "FAILED -- asymptotic value is not G"

    full_inf_limit = sp.limit(total, d, sp.oo)
    print(f"  G_eff(r->inf) with full f(r) (dipole/quad included): {full_inf_limit}")
    print("  [must ALSO be exactly G -- dipole/quad tiers vanish at r->inf,")
    print("   matching docs/127's own published dipole=0, quadrupole=0]")
    assert full_inf_limit == G, "FAILED -- dipole/quad terms do not vanish at r->inf"
    print("  PASS: monopole normalization correct, matches docs/127 exactly.\n")


def negative_control(f_r, syms):
    """Confirm dipole and quadrupole terms are functionally distinct (not
    a tautology returning the same form regardless of tier)."""
    G, M, k, R, d, c, b1, b2 = syms
    print("=== NEGATIVE CONTROL ===")
    dipole_term = f_r.coeff(b1, 1)
    quad_term = f_r.coeff(b2, 1)
    print(f"  dipole coefficient (in f(r)):     {dipole_term}")
    print(f"  quadrupole coefficient (in f(r)): {quad_term}")
    distinct = sp.simplify(dipole_term - quad_term) != 0
    assert distinct, "FAILED -- dipole and quadrupole terms are identical (tautology)"
    print("  PASS: dipole (~1/d) and quadrupole (~1/d^2) are functionally distinct.\n")


def numeric_evaluation(mc):
    """Evaluate G_eff at v82's own real archive values, across z and
    across a beta_1/beta_2 sensitivity sweep."""
    G, c = mc.G, mc.c
    B1, B2 = B1_SPOTLIGHTED, B2_SPOTLIGHTED

    def geff_ratio(z, b1=B1, b2=B2):
        M = mc.M_of(z)
        k = mc.k_of(z)
        R = mc.R_of(z)
        d = mc.d_of(z)  # NOT mc.d0_m -- d_of(z) = d0_m/(1+z), evolves with z
        c_d = -R * b1 * k / (M * c**2)
        c_q = R**2 * b2 * k**2 / (3 * M**2 * c**4)
        Gd = 2 * G * c_d / d
        Gq = 3 * G * c_q / d**2
        return (G + Gd + Gq) / G, Gd / G, Gq / G

    print("=== NUMERIC EVALUATION: G_eff,total/G across z (spotlighted beta) ===")
    print(f"{'z':>6}  {'total/G':>14}  {'dipole/G':>14}  {'quad/G':>14}")
    for z in ZS:
        tot, gd, gq = geff_ratio(z)
        print(f"{z:6.3f}  {tot:14.4e}  {gd:14.4e}  {gq:14.4e}")
    print()
    print("NOTE: dipole/G and quad/G are each ~1e3 in magnitude -- i.e. the")
    print("'correction' terms are ~1000x LARGER than the monopole term (=1)")
    print("at v82's own d0, not small perturbations. total/G is a delicate")
    print("cancellation between these two large, opposite-sign terms.\n")

    print("=== SENSITIVITY: +-10%/+-20% perturbation of beta_1, beta_2 at z=0 ===")
    for db1, db2 in [
        (1.0, 1.0),
        (1.1, 1.0),
        (0.9, 1.0),
        (1.0, 1.1),
        (1.0, 0.9),
        (1.1, 1.1),
        (0.9, 0.9),
        (1.2, 1.0),
        (0.8, 1.0),
    ]:
        tot, _, _ = geff_ratio(0.0, B1 * db1, B2 * db2)
        print(f"  beta_1 x{db1:.2f}, beta_2 x{db2:.2f}  ->  total/G = {tot:9.4f}")
    print()
    print("CONCLUSION: a 10% change in beta_1 alone swings total/G from +33 to")
    print("-75 or +142 -- sign-flipping, order-of-magnitude-unstable. This is")
    print("NOT a robust number. It cannot honestly be reported as 'the finite-r")
    print("effect is approximately N times G' -- see FINDING for full discussion.")


def main():
    f_r, terms, total, syms = derive_f_and_geff()
    print("Derived (dimensionless) f(d) =", f_r)
    print()
    positive_control(f_r, total, syms)
    negative_control(f_r, syms)
    mc = load_multing_core()
    numeric_evaluation(mc)


if __name__ == "__main__":
    main()
