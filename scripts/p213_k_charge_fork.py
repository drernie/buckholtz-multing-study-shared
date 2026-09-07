"""Fork the k-charge revival lead by MODEL_SPEC_AUDIT §5's two readings.

Berge et al. 2018 (arXiv:1712.00483, PRL 120,141101), Eq. (5)-(6):

    alpha_ij = alpha * (q/mu)_i * (q/mu)_j
    eta      = alpha * [ (q/mu)_Pt - (q/mu)_Ti ] * (q/mu)_E * (1+r/L) e^{-r/L}

P208's reduction of MULTING's own Eotvos expression:

    eta_E = 2 * eta_MULT * |Delta_psi| / r,   psi_i = K_i r_i / (M_i c^2)

Same shape. Their alpha <-> our eta = kappa/g; their Delta(q/mu) <-> our
Delta_psi. But MODEL_SPEC_AUDIT §5 says `k` has TWO readings, and they land
in completely different places on this map.

Numbers below are textbook nuclear/thermodynamic values entered explicitly
so they can be audited; each is marked. The ORDER OF MAGNITUDE is the
robust output, not the last digit.
"""

# --- Nuclear masses in u, [MEMORY] -- verify against AME2020 before quoting
# a precise figure. Order of magnitude is what this script is for.
ISOTOPES = {
    "Ti": [
        (46, 45.95263, 0.0825),
        (47, 46.95176, 0.0744),
        (48, 47.94794, 0.7372),
        (49, 48.94787, 0.0541),
        (50, 49.94479, 0.0518),
    ],
    "Pt": [
        (190, 189.95995, 0.00012),
        (192, 191.96104, 0.00782),
        (194, 193.96268, 0.3286),
        (195, 194.96479, 0.3378),
        (196, 195.96495, 0.2521),
        (198, 197.96789, 0.0736),
    ],
}

MICROSCOPE_PRODUCT_BOUND_M = 2.48e-8  # eta * |Delta_psi| <= this, from P209
TEST_MASS_RADIUS_M = 0.03  # MICROSCOPE test cylinders, order of magnitude


def baryon_per_mass(el: str) -> float:
    """<A> / <m> for a natural element -- the EP community's q/mu with q = B."""
    a = sum(f * A for A, _, f in ISOTOPES[el])
    m = sum(f * mm for _, mm, f in ISOTOPES[el])
    return a / m


print("=" * 72)
print("BRANCH 1 -- BROAD reading: k = all internal energy (binding, degeneracy)")
print("=" * 72)
print("\nBerge et al: 'taking into account the electromagnetic and nuclear")
print("binding energies, the charge are usually reduced to the material's")
print("baryon and/or lepton numbers'. So the broad reading maps k -> B.\n")
bt, bp = baryon_per_mass("Ti"), baryon_per_mass("Pt")
d = abs(bp - bt)
print(f"  (B/mu)_Ti = {bt:.6f}")
print(f"  (B/mu)_Pt = {bp:.6f}")
print(f"  |Delta(B/mu)| = {d:.3e}     <- the standard EP composition contrast")

psi_broad = d * TEST_MASS_RADIUS_M
print(f"\n  If psi ~ (B/mu) * r_body with r_body ~ {TEST_MASS_RADIUS_M} m:")
print(f"    |Delta_psi| ~ {psi_broad:.2e} m")
print(f"    => eta = kappa/g <= {MICROSCOPE_PRODUCT_BOUND_M / psi_broad:.2e}")
print("\n  MICROSCOPE BITES HARD on this branch.")
print("  BUT MODEL_SPEC_AUDIT §5: this broad reading is already disfavoured")
print("  by a periastron bound beta_d < 1.2e-5, FIVE ORDERS below Table A1.")

print("\n" + "=" * 72)
print("BRANCH 2 -- NARROW reading: k = THERMAL kinetic energy specifically")
print("=" * 72)
print("\n  §5 calls this the reading 'consistent with the cluster analysis'.")
# Thermal energy fraction of rest mass for a solid at room temperature.
# Dulong-Petit: ~3k_B T per atom. [MEMORY] textbook.
K_B_T_EV = 0.02585  # k_B * 300 K, in eV
U_MEV = 931.494  # atomic mass unit in MeV
for el, mu in (("Ti", 47.867), ("Pt", 195.084)):
    e_th_ev = 3.0 * K_B_T_EV  # per atom
    frac = (e_th_ev * 1e-6) / (mu * U_MEV)
    print(f"  {el}: E_thermal/atom ~ {e_th_ev:.4f} eV  ->  E_th/(M c^2) ~ {frac:.2e}")

f_ti = (3 * K_B_T_EV * 1e-6) / (47.867 * U_MEV)
f_pt = (3 * K_B_T_EV * 1e-6) / (195.084 * U_MEV)
d_th = abs(f_pt - f_ti)
psi_narrow = d_th * TEST_MASS_RADIUS_M
print(f"\n  |Delta(E_th/Mc^2)| ~ {d_th:.2e}   (driven by 1/mu, not by nuclear structure)")
print(f"  |Delta_psi| ~ {psi_narrow:.2e} m")
print(f"    => eta = kappa/g <= {MICROSCOPE_PRODUCT_BOUND_M / psi_narrow:.2e}")
print("\n  MICROSCOPE DOES NOT BITE on this branch -- the bound on eta is")
print("  astronomically weak. This is exactly P25's own 'K/M universality'")
print("  escape route, now quantified.")

print("\n" + "=" * 72)
print("THE FORK")
print("=" * 72)
ratio = psi_broad / psi_narrow
print(f"\n  The two readings differ in |Delta_psi| by a factor ~{ratio:.1e}.")
print("  The revival lead WORKS only under the reading MODEL_SPEC_AUDIT §5")
print("  already disfavours, and FAILS under the reading §5 calls consistent.")
print("\n  So the question 'what fixes Delta_psi' was never a literature gap.")
print("  It is the SAME single open question §5 already named: what is k?")
print("=" * 72)
