"""P149 -- Q4: does the near-field ratio beta_q/beta_d = sqrt(6)/2 survive a
nonzero mediator mass mu ~ H0/c at cluster scale?

Context: P148's retrospective promotion of the 2026-08-10..12 scalar
completion cluster to PROMOTE-WITH-QUALIFIERS named this as the cheapest
remaining internal-consistency check (Q4), to run BEFORE any fifth-force
experimental mapping (P150/Q3a), per the user's own explicit ordering:
internal consistency -> observable mapping -> external constraint.

Method: two_field_action_closure.py (P1) already established, for a
general exchange kernel K(s), that beta_q/beta_d is fixed by the pure
kernel invariant Lambda(r) = K'''(r)K'(r)/K''(r)^2 -- and that ONLY this
RATIO is physical (individual beta_d, beta_q depend on the lever-arm
convention d=r_A, which is a modelling choice, not physics -- P1's own
"[THE RATIO INVARIANT]" section). For the massless kernel K=1/s,
Lambda=3/2 exactly at every r. For Yukawa K=exp(-mu*s)/s, P1's own script
already derived Lambda(r) in closed form; this file evaluates THAT
closed-form expression (re-derived here independently, then checked
against P1's small-mu*r expansion Lambda=3/2-(3/4)(mu*r)^2 as a positive
control) at realistic H0/c * r for cluster and cosmological separations r.

This directly answers Q4 using the SAME already-established, already
skeptic-checked machinery (P1's kernel invariant, P11's small-mu*r
expansion), rather than re-deriving the full lever-arm ladder from
scratch (which the first draft of this script attempted and which
introduced an unrelated separation-vs-lever-arm variable-naming bug --
discarded in favour of this simpler, more directly verifiable route).
"""

import sympy as sp

s, mu = sp.symbols("s mu", positive=True)

print("=" * 78)
print("P149 -- kernel invariant Lambda(r) for a Yukawa mediator, vs. H0/c")
print("=" * 78)

K = sp.exp(-mu * s) / s
Kp = sp.diff(K, s)
Kpp = sp.diff(K, s, 2)
Kppp = sp.diff(K, s, 3)
Lambda = sp.simplify(Kppp * Kp / Kpp**2)
print(f"\nLambda(s) = K'''K'/(K'')^2 = {Lambda}")

print("\n[POSITIVE CONTROL 1] massless limit mu->0 must give exactly 3/2")
lam0 = sp.limit(Lambda, mu, 0)
print(f"  Lambda(mu=0) = {lam0}  (must be 3/2)")
if sp.simplify(lam0 - sp.Rational(3, 2)) != 0:
    print("  *** FAILED. STOP. ***")
    raise SystemExit(1)
print("  -> PASSED.")

print("\n[POSITIVE CONTROL 2] small-(mu*s) expansion must match P1/P11's own")
print("  Lambda = 3/2 - (3/4)(mu*s)^2 + O((mu*s)^4)")
mus = sp.Symbol("x", positive=True)  # x = mu*s
Lambda_of_x = Lambda.subs(mu, mus / s)
series_check = sp.expand(sp.series(Lambda_of_x, mus, 0, 5).removeO())
print(f"  series in (mu*s) = {series_check}")
coeff0 = sp.simplify(series_check.coeff(mus, 0) - sp.Rational(3, 2))
coeff2 = sp.simplify(series_check.coeff(mus, 2) - (-sp.Rational(3, 4)))
print(f"  coeff(mu*s, 0) - 3/2    = {coeff0}  (must be 0)")
print(f"  coeff(mu*s, 2) - (-3/4) = {coeff2}  (must be 0)")
if coeff0 != 0 or coeff2 != 0:
    print("  *** FAILED. STOP. ***")
    raise SystemExit(1)
print("  -> PASSED, matches P1/P11's own hand-derived expansion.")

print("\n" + "=" * 78)
print("[THE DECISIVE TEST] Lambda(mu*r) at realistic separations, mu=H0/c")
print("=" * 78)

H0_over_c_per_mpc = 70 / 2.998e5  # H0=70 km/s/Mpc, c=2.998e5 km/s -> Mpc^-1
print(f"\nmu = H0/c = {H0_over_c_per_mpc:.4e} Mpc^-1  (H0=70 km/s/Mpc)")
print(f"Hubble radius c/H0 = {1 / H0_over_c_per_mpc:.1f} Mpc")

print(f"\n{'r [Mpc]':>12} {'mu*r':>14} {'Lambda(mu*r)':>16} {'dev from 3/2':>16}")
target = 1.5
for r_mpc in [0.5, 1.0, 3.0, 10.0, 100.0, 1000.0, 4283.0, 8566.0, 42830.0]:
    mu_r = H0_over_c_per_mpc * r_mpc
    lam_val = float(Lambda.subs({mu: H0_over_c_per_mpc, s: r_mpc}))
    dev_pct = 100 * abs(lam_val - target) / target
    print(f"{r_mpc:>12.1f} {mu_r:>14.3e} {lam_val:>16.10f} {dev_pct:>14.6e}%")

print("""
VERDICT CRITERION (per P148/Q4): if the deviation of Lambda from 3/2 (and
hence of beta_q/beta_d from sqrt(6)/2) stays negligible at cluster scale
(r ~ 0.5-10 Mpc, where this project's own beta_d=2, beta_q=sqrt(6) result
was derived and where it would need to be measured) and only grows toward
O(1) near the Hubble radius (r ~ 1/H0), this is
MASSIVE-MEDIATOR-NEAR-FIELD-COMPATIBLE -- P11's mu~H0/c candidate does not
break the near-field ladder it needs to preserve. If the deviation is
already non-negligible at cluster scale, this is
MASS-SCALE-ESCAPE-LOAD-BEARING/INCOMPATIBLE.
""")
