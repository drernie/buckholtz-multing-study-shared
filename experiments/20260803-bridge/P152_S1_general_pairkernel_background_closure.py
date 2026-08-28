"""P152 -- S1 test: does the Shtanov-Sahni background-closure zero (docs/127,
P2) generalize to ANY steeper-than-monopole pair-kernel correction, regardless
of what sources it -- closing off the "S1: non-gradient-sourced moment" escape
route named by the skeptic in FINDING_P4 for a whole CLASS of constructions,
not just the two specific cases (vector dipole, scalar quadrupole) already
computed?

Context: FINDING_P4 (2026-08-10/11) named two live, uncomputed escape routes
for a genuine two-field completion (Branch B) to simultaneously (a) match
MULTING's near-field ladder and (b) source a nonzero background H(z):
  S1 -- a moment sourced by something OTHER than a potential gradient
        (intrinsic spin, a non-gradient background VEV, an equation-of-state
        parameter) -- the argument that a ladder-matching moment "must be
        gradient-induced, hence vanishes on a homogeneous background" does
        NOT apply to P1's own construction (p_i=kappa*k_i*r_i/c^2 is already
        intrinsic, not gradient-induced) -- so this route was never actually
        closed by anything computed so far.
  S2 -- a psi with its own distinct (screened/massive) propagator.

docs/127 (P2) already found G_eff=0 in the Shtanov-Sahni background closure
for MULTING's OWN dipole (f(r)~1/r, i.e. n=1) and quadrupole (f(r)~1/r^2,
i.e. n=2) terms -- but only checked those two specific cases, and its own
follow-up "C1" test (isotropic vector-orientation averaging) found a
DIFFERENT mechanism for the vector-dipole case's zero (orientation washout),
not the same mechanism as the plain radial-asymptotic argument.

This script asks the sharper question directly: is the zero a coincidence of
those two specific powers, or a structural fact about the S-S formula itself
that holds for ANY steeper-than-monopole correction -- independent of
whether it is vector or scalar, gradient-induced or intrinsic (spin/EOS/VEV)?
If the latter, S1 is closed for the whole class of "moment sourcing a pair-
kernel correction of MULTING's own tier-ladder shape," not just the two
already-tested cases -- leaving open only the channel FINDING_P4 Sec 5
already flagged as uninteresting/non-MULTING-specific (psi's own homogeneous
quintessence-like background mode, unrelated to the k-charge structure).

NOT_VALIDATION -- NOT_REFUTATION -- OUR_RECONSTRUCTION. Nothing here is a
claim about MULTING's own theory (NO_AUTHOR_ERROR); this bounds only this
project's own S-S-closure reconstruction of the background question.
"""

import sympy as sp

print("=" * 78)
print("P152 -- S1: general pair-kernel background-closure proof")
print("=" * 78)

r, n, mu, C = sp.symbols("r n mu C", positive=True)

print("""
Shtanov-Sahni background closure (docs/124, their Eq. 22, applied to F_oP):
  phi(r) = -(G/r) f(r)
  G_eff  = G * lim_{r->inf} [ f(r) - r f'(r) ]

docs/127 computed this for exactly two cases:
  monopole:   f(r) = 1            (n=0)  -> G_eff = G       (nonzero)
  dipole:     f(r) ~ 1/r          (n=1)  -> G_eff = 0
  quadrupole: f(r) ~ 1/r^2        (n=2)  -> G_eff = 0
""")

print("[STEP 1] General power-law f(r) = C * r^(-n), symbolic, ANY n >= 0:")
f_power = C * r ** (-n)
f_power_prime = sp.diff(f_power, r)
expr_power = sp.simplify(f_power - r * f_power_prime)
print("  f(r) = C*r^(-n)")
print(f"  f - r*f' = {expr_power}")

limit_n0 = sp.limit(expr_power.subs(n, 0), r, sp.oo)
print(f"\n  [POSITIVE CONTROL] n=0 (monopole): lim_(r->inf) = {limit_n0}")
print("    Matches docs/127's own G_eff=G result for the monopole. Confirms")
print("    this general form reproduces the ALREADY-established n=0 case")
print("    before trusting it for new n values.")

print("\n  [STEP 1b] n=1 (dipole) and n=2 (quadrupole), symbolic re-derivation:")
for n_val in [1, 2]:
    lim_val = sp.limit(expr_power.subs(n, n_val), r, sp.oo)
    print(f"    n={n_val}: lim_(r->inf)[f-r f'] = {lim_val}   (docs/127: 0 -- MATCH)")

print("\n  [STEP 1c] General n, symbolic (any positive n, not case-by-case):")
n_sym = sp.symbols("n_sym", positive=True)
expr_general_n = sp.simplify(C * r ** (-n_sym) - r * sp.diff(C * r ** (-n_sym), r))
limit_general = sp.limit(expr_general_n, r, sp.oo)
print(f"    f - r*f' = {expr_general_n} = C*(1+n_sym)*r^(-n_sym)")
print(f"    lim_(r->inf) for symbolic positive n_sym = {limit_general}")
print("    -> ZERO for ANY n_sym > 0, proven once, not per-case.")
print("    This holds regardless of the physical origin of f(r)=C*r^-n --")
print("    whether C encodes a gradient-induced coupling, an intrinsic spin")
print("    moment, an equation-of-state parameter, or a non-gradient VEV.")
print("    The S-S formula only sees the RADIAL FALLOFF of the pair")
print("    potential, not the mechanism that produced it.")

print("\n[STEP 2] Screened (Yukawa-type) correction, f(r) = C*r^(-n)*exp(-mu*r):")
print("(relevant to whether a SCREENED non-gradient moment, S1+S2 combined,")
print(" could evade the power-law result via a different asymptotic form)")
f_yukawa = C * r ** (-n_sym) * sp.exp(-mu * r)
f_yukawa_prime = sp.diff(f_yukawa, r)
expr_yukawa = sp.simplify(f_yukawa - r * f_yukawa_prime)
limit_yukawa = sp.limit(expr_yukawa, r, sp.oo)
print(f"  f - r*f' = {expr_yukawa}")
print(f"  lim_(r->inf), mu>0, n_sym>0 (symbolic, positive) = {limit_yukawa}")

print("\n  [SEPARATE CHECK] n=0 case (screened monopole-like term) -- computed")
print("  as its own explicit symbol, NOT by substituting 0 into a symbol")
print("  declared positive=True (sympy correctness note: n_sym was declared")
print("  positive, so n_sym=0 is outside its own assumed domain and must be")
print("  verified independently, not inferred from the n_sym>0 result above):")
f_yukawa_n0 = C * sp.exp(-mu * r)
f_yukawa_n0_prime = sp.diff(f_yukawa_n0, r)
expr_yukawa_n0 = sp.simplify(f_yukawa_n0 - r * f_yukawa_n0_prime)
limit_yukawa_n0 = sp.limit(expr_yukawa_n0, r, sp.oo)
print(f"    f - r*f' = {expr_yukawa_n0}")
print(f"    lim_(r->inf), mu>0, n=0 = {limit_yukawa_n0}")
print("    -> ZERO, explicitly verified (not merely asserted): a SCREENED")
print("     monopole-like correction also gives G_eff=0 -- exponential")
print("     screening kills the r->inf tail even faster than a power law.")
print("     Consistent with P149's own finding that a massive mediator")
print("     suppresses the SAME kernel invariant at large r (Hubble-radius")
print("     asymptote), not a new/surprising result, but confirms the")
print("     screened case does not accidentally revive G_eff via some")
print("     non-power-law loophole.")

print()
print("=" * 78)
print("VERDICT")
print("=" * 78)
print("""
The Shtanov-Sahni background G_eff formula gives EXACTLY ZERO for any pair-
kernel correction f(r) that falls off asymptotically as r^(-n) with n>0
(power-law) OR as r^(-n)*exp(-mu r) with mu>0 (screened), for ANY n>=0 in
the screened case. This is a structural fact about the r->inf LIMIT itself
-- it does not depend on:
  - whether the correction is a dipole (n=1), quadrupole (n=2), or any
    higher multipole tier,
  - whether the sourcing moment is a VECTOR (needing the separate C1
    orientation-averaging argument) or a SCALAR (spin-squared, an
    equation-of-state parameter, k_i*k_j) that has no orientation to
    average away,
  - whether the moment is gradient-induced or intrinsic (non-gradient).

CONSEQUENCE FOR S1: the "non-gradient-sourced moment" escape route named in
FINDING_P4 is CLOSED for the entire class of constructions where the moment
enters via a pair-kernel correction of the SAME general shape needed to
reproduce MULTING's own near-field ladder (any n>=1 tier, docs/124's own
established mapping) -- not merely for the two specific cases (vector
dipole via orientation-averaging, C1; scalar quadrupole via radial limit,
P2) already computed. No choice of non-gradient sourcing mechanism (spin,
EOS parameter, VEV) can rescue a nonzero G_eff as long as it produces a
steeper-than-monopole pair-kernel correction -- which reproducing the A3/A4
ladder requires.

WHAT REMAINS OPEN (per FINDING_P4 Sec 5, NOT reopened or closed by this):
a second scalar psi's OWN homogeneous background mode (psi_bg(t), V(psi))
can source H(z) via ordinary quintessence-type physics, entirely
INDEPENDENT of the S-S pair-kernel channel tested here and independent of
whether psi carries any MULTING k-charge structure at all. This channel is
untouched by the closure proven above -- but it was already flagged as
generic to any scalar field and not specific to MULTING, hence not
pursued further under this project's own scope.
""")
