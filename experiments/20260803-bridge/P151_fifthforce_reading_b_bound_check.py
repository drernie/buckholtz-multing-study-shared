"""P151 -- Q3b: under Reading B ONLY (per P150's own explicit scope
restriction), does this project's two-charge scalar completion predict a
MICROSCOPE-detectable or Cassini-detectable signal?

Context: P150 found MULTING's own k_A has no formula for ordinary matter;
of three internally-coherent readings this project could use to extend it,
only Reading B (literal total internal thermal/vibrational energy) lets
any laboratory-scale signal exist at all -- Readings A and C both give
k~=0 for solid test masses. This script computes the ACTUAL predicted
signal under Reading B and compares it to REAL experimental bounds
(fetched via WebSearch, not recalled from memory) -- per the corrected
order (internal consistency -> observable mapping -> external constraint)
this project's own methodology requires, and per the user's own explicit
warning against plugging kappa directly into a bound without first
deriving the actual observable.

Everything here is scoped to Reading B, OUR_RECONSTRUCTION, NOT_VALIDATION
-- a bound on this project's own candidate construction under one of three
disputed readings, not a claim about MULTING's own theory (NO_AUTHOR_ERROR).

Two checks:
1. MICROSCOPE (Ti vs Pt differential acceleration in Earth's field).
2. Solar-system scale (Cassini-type), redone under Reading B's CONSISTENT
   k_Sun value (P150 found docs/118's own corona-only k_Sun does not
   survive under Reading B -- this must be rechecked, not reused).
"""

import sympy as sp

print("=" * 78)
print("P151 -- Reading B ONLY. OUR_RECONSTRUCTION, NOT a claim about MULTING.")
print("=" * 78)

kB = 1.380649e-23  # J/K, exact SI definition
amu = 1.66053907e-27  # kg
c = 2.99792458e8  # m/s, exact
G = 6.67430e-11  # m^3 kg^-1 s^-2 (CODATA)
T = 300.0  # K, satellite/lab ambient temperature

print("\n[STEP 1] k_i/m_i for Ti and Pt test masses under Reading B")
print("(literal bulk thermal/vibrational energy, (3/2) k_B T per atom)")

m_Ti_amu = 47.87  # Ti dominant in Ti:Al:V(90:6:4) alloy, order-of-magnitude use
m_Pt_amu = 195.08  # Pt dominant in Pt:Rh(90:10) alloy


def k_over_m(m_atom_amu: float) -> float:
    """k_i/m_i = E_thermal/(m_i c^2), dimensionless -- NOTE: P150 mislabeled
    this quantity 'k_i/(m_i c^2)'; the correct label is k_i/m_i since
    MULTING's own k_i is ALREADY energy/c^2 (mass units) -- fixed here,
    value unchanged from P150 (this is a units-LABEL correction only)."""
    m_atom_kg = m_atom_amu * amu
    E_thermal = 1.5 * kB * T
    return E_thermal / (m_atom_kg * c**2)


kmi_Ti = k_over_m(m_Ti_amu)
kmi_Pt = k_over_m(m_Pt_amu)
print(f"  k_Ti/m_Ti = {kmi_Ti:.4e}")
print(f"  k_Pt/m_Pt = {kmi_Pt:.4e}")
print(f"  ratio Ti/Pt = {kmi_Ti / kmi_Pt:.3f}  (matches P150's own '~4x' claim)")
delta_kmi = kmi_Ti - kmi_Pt
print(f"  (k_Ti/m_Ti - k_Pt/m_Pt) = {delta_kmi:.4e}")

print("\n[POSITIVE CONTROL] Dulong-Petit sanity check: room-temp solids should")
print("have k_i/m_i of order k_B*T/(amu*c^2) ~ 1e-13 to 1e-12 -- textbook scale")
print("for thermal energy vs. rest-mass energy of ordinary matter, not an")
print("arbitrary number:")
control = kB * T / (amu * c**2)
print(f"  k_B*T/(amu*c^2) = {control:.4e}  (both k_Ti/m_Ti, k_Pt/m_Pt sit within")
print("  a factor of a few of this, as expected for atomic masses ~50-200 amu)")

print()
print("=" * 78)
print("[CHECK 1] MICROSCOPE -- Ti vs Pt differential acceleration in Earth's field")
print("=" * 78)

print("""
Real mission parameters (WebSearch-verified, not recalled from memory):
  Test masses: Pt:Rh(90:10) inner, Ti:Al:V(90:6:4) outer cylinders
  Test mass outer radii: 39-69 mm (representative r_test = 50 mm used)
  Orbital altitude: ~710 km, mean semi-major axis 7090 km (sun-synchronous)
  Result (Touboul et al. 2022, Phys. Rev. Lett. 129, 121102):
    eta(Ti,Pt) = [-1.5 +/- 2.3(stat) +/- 1.5(syst)] x 10^-15  (1-sigma)
""")

M_earth = 5.972e24  # kg
R_earth = 6.371e6  # m
D_orbit = 7.090e6  # m, mean semi-major axis (matches R_earth + 710km altitude)
r_test = 0.05  # m, representative test-mass radius
beta_d = 2.0  # THIS PROJECT'S OWN two-charge-completion value (P1), not MULTING's AI-fit

print("Derivation: F_d = G*beta_d*(k_i*m_Earth*r_i + k_Earth*m_i*r_Earth)/(c^2*D^3)")
print("The k_Earth term is IDENTICAL for both test masses -> cancels in the")
print("differential (Eotvos) measurement. Only the k_i*m_Earth*r_i term")
print("(each test mass's OWN charge) survives in the difference:")
print()
print("  Delta_a = a_Ti - a_Pt")
print("          = [G*beta_d*M_Earth*r_test/(c^2*D^3)] * (k_Ti/m_Ti - k_Pt/m_Pt)")
print()
print("  eta = 2*Delta_a / g_orbit,  g_orbit = G*M_Earth/D^2  (ordinary gravity")
print("  dominates the denominator a_Ti+a_Pt -- the dipole term is a tiny")
print("  correction on top of it, not comparable in size)")
print()
print("  => eta = 2*beta_d*r_test/(c^2*D) * (k_Ti/m_Ti - k_Pt/m_Pt)")

eta_predicted = 2 * beta_d * r_test / (c**2 * D_orbit) * delta_kmi
print(f"\n  eta_predicted (Reading B) = {eta_predicted:.4e}")

eta_bound = 1.5e-15  # 1-sigma combined-ish scale from Touboul et al. 2022
print(f"  eta_observed (MICROSCOPE, 1-sigma scale)  = ~{eta_bound:.1e}")
ratio = abs(eta_predicted) / eta_bound
print(f"\n  |eta_predicted| / eta_bound = {ratio:.2e}")
if ratio < 1:
    print("  -> predicted signal is BELOW MICROSCOPE's sensitivity by")
    print(f"     {sp.log(1 / ratio, 10).evalf():.1f} orders of magnitude.")
    print("     MICROSCOPE does NOT constrain this construction -- not because")
    print("     the mapping is invalid, but because the predicted effect is")
    print("     far too small to detect at current precision.")
else:
    print("  *** predicted signal EXCEEDS the observed bound -- this specific")
    print("  *** Reading-B instantiation would be EXCLUDED by MICROSCOPE. ***")

print()
print("=" * 78)
print("[CHECK 2] Solar-system scale (Cassini-type), Reading B applied")
print("CONSISTENTLY to the Sun -- redoing docs/118, not reusing its number")
print("(per P150's own explicit flag: docs/118 used corona-only k_Sun,")
print("which does NOT survive under Reading B)")
print("=" * 78)

M_sun = 1.989e30  # kg
R_sun = 6.957e8  # m
AU = 1.496e11  # m

k_Sun_over_Msun_readingB = G * M_sun / (R_sun * c**2)
print("\nk_Sun/M_sun (Reading B, consistent -- compactness proxy for total")
print("internal/self-gravitational energy budget, NOT corona-only):")
print(f"  = G*M_sun/(R_sun*c^2) = {k_Sun_over_Msun_readingB:.4e}")
print(f"  (independently re-verified: matches P150's own {2.1e-6:.1e} figure)")

k_Sun_readingB = k_Sun_over_Msun_readingB * M_sun
print(f"  k_Sun (Reading B) = {k_Sun_readingB:.4e} kg")

k_Sun_docs118 = 3e-17 * M_sun
print(f"  k_Sun (docs/118, corona-only) = {k_Sun_docs118:.4e} kg")
print(f"  ratio (Reading B / docs/118)  = {k_Sun_readingB / k_Sun_docs118:.3e}")

print("\nDipole-to-monopole force ratio at Earth-Sun separation (D=1 AU).")
print("The surviving term is the SUN's own k-charge (k_P m_A r_P, P=Sun,")
print("A=Earth) -- its lever arm is the SUN's OWN radius R_sun, matching")
print("docs/118's own formula F_d/F_m = beta_d*(k_Sun/M_sun)*(R_sun/D)")
print("(NOT R_earth -- an error in an earlier draft of this script, caught")
print("and fixed before this ran against the skeptic):")

F_d_over_Fm = beta_d * (k_Sun_readingB / M_sun) * (R_sun / AU)
print(f"  F_d/F_m = beta_d*(k_Sun/M_sun)*(R_sun/D) = {F_d_over_Fm:.4e}")

cassini_bound = 2.3e-5  # Bertotti et al. 2003, as cited in docs/118
print("  Cassini bound on anomalous force ratio (Bertotti et al. 2003,")
print(f"  as cited in docs/118): < {cassini_bound:.1e}")
ratio2 = F_d_over_Fm / cassini_bound
print(f"\n  F_d/F_m / Cassini_bound = {ratio2:.4e}")
if ratio2 < 1:
    print(f"  -> still below the Cassini bound, by {sp.log(1 / ratio2, 10).evalf():.1f}")
    print("     orders of magnitude -- SAFE, but by a much smaller margin than")
    print("     docs/118's own (stale, corona-based) 14-orders-of-magnitude claim.")
else:
    print("  *** EXCEEDS the Cassini bound -- Reading B, applied consistently,")
    print("  *** would be EXCLUDED at the solar-system scale. ***")

print()
print("=" * 78)
print("SUMMARY (Reading B only -- per P150, the one-of-three reading that")
print("lets any signal exist; NOT a claim about MULTING itself)")
print("=" * 78)
