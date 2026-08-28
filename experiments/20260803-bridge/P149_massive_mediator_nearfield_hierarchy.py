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

print("\n[POSITIVE CONTROL 2] small-(mu*s) expansion, checked to O((mu*s)^4)")
print("  CORRECTED (per independent skeptic review): P1/P11's own quoted")
print("  expansion 'Lambda = 3/2 - (3/4)(mu*s)^2 + O((mu*s)^4)' is INCOMPLETE")
print("  -- it silently drops a real +(mu*s)^3 term (P1's own script truncated")
print("  the series before that order, hiding it; propagated uncorrected into")
print("  the first draft of this file too). The correct expansion is:")
print("    Lambda = 3/2 - (3/4)x^2 + x^3 - (5/8)x^4 + O(x^5),  x = mu*s")
print("  Checked here to O(x^4), all four nonzero coefficients required exact.")
mus = sp.Symbol("x", positive=True)  # x = mu*s
Lambda_of_x = Lambda.subs(mu, mus / s)
series_check = sp.expand(sp.series(Lambda_of_x, mus, 0, 5).removeO())
print(f"  series in (mu*s) = {series_check}")
expected_coeffs = {
    0: sp.Rational(3, 2),
    2: -sp.Rational(3, 4),
    3: sp.Integer(1),
    4: -sp.Rational(5, 8),
}
all_ok = True
for power, expected in expected_coeffs.items():
    diff = sp.simplify(series_check.coeff(mus, power) - expected)
    print(f"  coeff(mu*s, {power}) - {expected} = {diff}  (must be 0)")
    all_ok = all_ok and (diff == 0)
if not all_ok:
    print("  *** FAILED. STOP. ***")
    raise SystemExit(1)
print("  -> PASSED (corrected expansion, all 4 coefficients exact).")

print("\n[ITEM-4 CHECK, per skeptic review] does the ratio Lambda hide drift")
print("that the INDIVIDUAL tier coefficients don't show (or vice versa)?")
print("Compare each tier's own Yukawa/massless ratio, small-x expansion:")
beta_d_ratio = sp.series(sp.exp(-mus) * (mus**2 + 2 * mus + 2) / 2, mus, 0, 6).removeO()
beta_q2_ratio = sp.series(
    sp.exp(-mus) * (mus**3 + 3 * mus**2 + 6 * mus + 6) / 6, mus, 0, 6
).removeO()
print(f"  beta_d(mu)/beta_d(0)   = {sp.expand(beta_d_ratio)}   (leading drift O(x^3))")
print(f"  beta_q^2(mu)/beta_q^2(0) = {sp.expand(beta_q2_ratio)}   (leading drift O(x^4))")
print("  Lambda(mu)/Lambda(0) leading drift is O(x^2) -- STRICTER than either")
print("  individual tier (O(x^3), O(x^4)). The ratio-only check is therefore")
print("  the MOST sensitive of the three at leading order, not a looser one")
print("  that could hide drift -- confirmed here, not just asserted.")

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
VERDICT CRITERION (per P148/Q4, wording corrected per skeptic review):
what is actually tested is the convention-independent RATIO-invariant
Lambda(s), per P1's own finding that only the ratio beta_q/beta_d is
physical -- NOT that the individual power-law tiers F_km~1/r^3, F_kk~1/r^4
survive unmodified (they do not, for any mu>0: each picks up its own
exp(-mu*r)*polynomial(mu*r) deformation, confirmed above to be smaller
than Lambda's own deviation at leading order, but still a real deformation
of the pure power-law form).

If Lambda's deviation from 3/2 stays negligible at cluster scale
(r ~ 0.5-10 Mpc, where beta_d=2, beta_q=sqrt(6) was derived and measured)
and only grows toward O(1) near the Hubble radius, this is
MASSIVE-MEDIATOR-NEAR-FIELD-RATIO-INVARIANT-COMPATIBLE -- P11's mu~H0/c
candidate does not break the one convention-independent quantity this
construction's physical content actually reduces to. If the deviation is
already non-negligible at cluster scale, this is
MASS-SCALE-ESCAPE-LOAD-BEARING/INCOMPATIBLE.
""")
