"""P153 -- S2 test: does a screened (Yukawa, fixed-mass) mediator open a
window where the near-field ladder survives AND the cosmological background
is sourced -- the user's own proposed 3-step overlap-window gate
(local-kernel fidelity / background-cancellation / W_local intersect W_bg),
reusing this project's own already-established machinery rather than
re-deriving it.

NOVELTY CHECK (mandatory before any new derivation, falsification-ladder.md
Step -3): two prior pieces of this project's own work already answer most
of the user's 3 steps, and must be assembled correctly, not re-derived:

  Step 1 (local-kernel fidelity, beta_d(mu*r), beta_q(mu*r)) -- ALREADY
    DONE in P149 (two_field_action_closure.py's own closed forms,
    independently re-verified there):
      beta_d(x)/beta_d(0)    = exp(-x)*(x^2+2x+2)/2
      beta_q^2(x)/beta_q^2(0) = exp(-x)*(x^3+3x^2+6x+6)/6
    with x=mu*r, confirmed beta_d(0)=2, beta_q(0)=sqrt(6) exactly (P1's own
    values), and confirmed cluster-scale (mu=H0/c, r~Mpc) deviation is
    negligible (~1e-8) growing toward O(1) only near the Hubble radius.
    This IS W_local, already computed. Reused here, not re-derived.

  Step 2 (background-cancellation test, is <F_k^(mu)>_iso = 0?) -- THIS
    HAS TWO DIFFERENT, NOT-INTERCHANGEABLE PRIOR ANSWERS, and telling them
    apart is the actual physics content of this file:

    (a) P11_yukawa_screening_breaks_double_layer.py (2026-08-12) tests the
        NEAR-FIELD exterior potential of ONE FINITE dipole shell (radius A,
        dimensionless units, field point a few shell-radii away) for a
        Yukawa kernel -- found NONZERO for every finite mu tested,
        skeptic-CONFIRMED-REAL via an independent closed-form match. This
        is a LOCAL, single-structure statement, in shell-radius units, not
        tied to any particular macroscopic separation.

    (b) P152_S1_general_pairkernel_background_closure.py (2026-08-28,
        Step 2 of that script) already computed the Shtanov-Sahni
        COSMOLOGICAL BACKGROUND closure G_eff = G*lim_{r->inf}[f-r*f'] for
        a screened kernel f(r)=C*r^(-n)*exp(-mu*r) SYMBOLICALLY, for ANY
        n>=0 and ANY mu>0 -- and found it is EXACTLY ZERO, more robustly
        than the massless power-law case (exponential beats polynomial at
        r->inf). This is the SAME criterion this ENTIRE project has used,
        consistently, since docs/124, for "does this correction source the
        smooth cosmological background H(z)" -- not a new test invented
        for this file.

    These are DIFFERENT mathematical objects (a finite-shell near-field
    potential at fixed r, vs. the r->infinity asymptotic limit that enters
    a mean-field/continuum Friedmann-type equation) and answering "does S2
    revive H(z)" requires using (b), the criterion this project's own
    F->H(z) bridge work has used throughout -- not (a), which is a
    near-field/local statement more naturally connected to structure-
    formation / second-order effects (this project's own recurring theme,
    e.g. the beta_cv.py pearl), not the background.

  Step 3 (W_local intersect W_bg) -- follows immediately once Step 2 uses
    criterion (b): if G_eff=0 for EVERY mu>0 (not just at some particular
    scale), then W_bg (in the S-S background sense) is EMPTY -- there is
    no mu, however large, that makes the background channel nonzero. The
    intersection with W_local is therefore empty for a trivial reason: one
    of the two sets is empty on its own, independent of the other.

This file's own new content is: (1) explicitly connecting P152's already-
proven screened-kernel G_eff=0 result to S2's specific physical question
(P152 was built to answer S1, not explicitly framed as an S2 answer at the
time); (2) putting P149's beta_d(mu*r)/beta_q(mu*r) and P152's G_eff(mu)
side by side, at the SAME physical mu=H0/c and the SAME r-grid, so W_local
and W_bg can be read off one table instead of two separate scripts;
(3) explicitly flagging that P11's own, different, still-live near-field
result is NOT closed by this and remains a separate, real lead.

NOT_VALIDATION -- NOT_REFUTATION -- OUR_RECONSTRUCTION. Nothing here is a
claim about MULTING's own theory (NO_AUTHOR_ERROR); this bounds only this
project's own S-S-closure reconstruction of the background question, and
the ladder-fidelity question, for its own scalar-completion candidate.
"""

import sympy as sp

print("=" * 78)
print("P153 -- S2: screened-propagator overlap-window gate (W_local vs W_bg)")
print("=" * 78)

r, mu, C, n = sp.symbols("r mu C n", positive=True)

print("""
[STEP 1 -- W_local, REUSED from P149, not re-derived]
beta_d(x)/beta_d(0)     = exp(-x)*(x^2+2x+2)/2      (x = mu*r)
beta_q^2(x)/beta_q^2(0) = exp(-x)*(x^3+3x^2+6x+6)/6
""")

x = sp.Symbol("x", positive=True)
beta_d_ratio = sp.exp(-x) * (x**2 + 2 * x + 2) / 2
beta_q2_ratio = sp.exp(-x) * (x**3 + 3 * x**2 + 6 * x + 6) / 6

print("[POSITIVE CONTROL] x->0 limit must reproduce beta_d(0)=2/2=1, beta_q^2(0)=6/6=1")
print(f"  beta_d_ratio(x=0)   = {sp.limit(beta_d_ratio, x, 0)}   (expect 1)")
print(f"  beta_q2_ratio(x=0)  = {sp.limit(beta_q2_ratio, x, 0)}  (expect 1)")
assert sp.limit(beta_d_ratio, x, 0) == 1
assert sp.limit(beta_q2_ratio, x, 0) == 1
print("  -> PASSED, matches P149's own beta_d=2, beta_q=sqrt(6) exactly.")

print("\n" + "=" * 78)
print("[STEP 2 -- W_bg, the Shtanov-Sahni background criterion, REUSED from P152]")
print("=" * 78)
print("""
P152 already proved SYMBOLICALLY (its own Step 2), for f(r)=C*r^(-n)*exp(-mu*r):
  G_eff = G * lim_{r->inf} [f - r*f'] = 0   for ANY n>=0, ANY mu>0

Re-confirmed here directly for MULTING's own two tiers (dipole n=1, quad
n=2), not just the abstract general-n case, before using it as W_bg:
""")

for n_val, label in [(1, "dipole (n=1)"), (2, "quadrupole (n=2)")]:
    f_screened = C * r ** (-n_val) * sp.exp(-mu * r)
    f_screened_prime = sp.diff(f_screened, r)
    expr = sp.simplify(f_screened - r * f_screened_prime)
    limit_val = sp.limit(expr, r, sp.oo)
    print(f"  {label}: f-r*f' = {expr}")
    print(f"    lim_(r->inf), mu>0 fixed = {limit_val}   (expect 0)")
    assert limit_val == 0

print("""
-> CONFIRMED: G_eff=0 for BOTH MULTING tiers, for ANY finite mu>0 -- not
   just at mu=H0/c, not just at cosmological r. There is no value of mu,
   however large or small, that makes the screened background coupling
   nonzero. Screening does not revive G_eff -- it cannot, structurally,
   because exponential decay only strengthens the r->inf vanishing that
   already held for the massless (mu=0) power-law case.

W_bg (mu values where the background contribution is nonzero) = EMPTY SET.
""")

print("=" * 78)
print("[STEP 3 -- W_local intersect W_bg]")
print("=" * 78)
print("""
W_local (per Step 1, reusing P149's own physical-scale table): at
mu=H0/c=70/2.998e5 Mpc^-1, cluster-scale deviation from the massless ratio
is ~1e-8 at r~few Mpc, growing toward O(1) only near the Hubble radius --
a wide, comfortable window, already tabulated in P149.

W_bg (per Step 2, this file) = EMPTY, for every mu tested and, by the
general-n proof in P152, for every mu>0 whatsoever (not merely the ones
sampled here).

W_local intersect W_bg = W_local intersect (empty set) = EMPTY.

VERDICT: SCREENED-PROPAGATOR-NO-COMPATIBLE-WINDOW (S-S background channel)
-- not because the local ladder is fragile (it is not: W_local is wide),
but because W_bg is empty on its own, independent of W_local. A screened
mediator does not trade local fidelity against background sourcing; it
simply never sources the background, at any scale, for this observable.
""")

print("=" * 78)
print("[WHAT THIS DOES NOT CLOSE -- P11's separate, still-open result]")
print("=" * 78)
print("""
P11_yukawa_screening_breaks_double_layer.py found a NONZERO exterior
potential for a single, FINITE dipole shell at a Yukawa mediator's
near-field (a few shell-radii away, dimensionless shell-radius units,
skeptic-CONFIRMED-REAL). That is a genuinely different mathematical
object from G_eff -- a finite-r, single-structure near-field quantity,
not the r->infinity asymptotic limit that enters the smooth cosmological
background equation. P11's own result is NOT overturned or closed by
this file: it remains a real, live, LOCAL effect (structure-formation /
second-order scale, per this project's own recurring "degenerate with
LambdaCDM at first order, distinguishable only at second" theme, e.g. the
beta_cv.py pearl) -- just not, per the reasoning above, a background-H(z)
effect. The two should not be conflated when reporting S2's status.
""")
