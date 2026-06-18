"""
H-k_A-1: r_P(z) merger-epoch hypothesis

Hypothesis: eps(z) from Table A1 is reproduced by virial k_A + non-standard r_P(z).
The r_P(z) has a minimum near z~0.25-0.40, reflecting the epoch of maximum cluster
proximity during the cosmic cluster-merger peak.

Safety: NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION
"""

import numpy as np
from scipy.special import erfc

# ── Table A1 ground truth ──────────────────────────────────────────────────
Z_A1 = np.array([0.06, 0.14, 0.25, 0.40, 0.65, 1.00, 1.50, 2.10, 3.20, 5.00, 8.50])
EPS_A1 = np.array([0.063, 0.125, 0.215, 0.228, 0.213, 0.186, 0.214, 0.171, 0.106, 0.048, 0.101])

# ── Cosmological background ────────────────────────────────────────────────
H0, OM = 70.0, 0.3  # ΛCDM backdrop (NOT fitting MULTING here, just cluster background)
DELTA_VIR = 200.0
SIGMA_PS = 0.5  # RMS at M_min ~ 1e14 Msun scale
DELTA_C = 1.686


def H_lcdm(z):
    return H0 * np.sqrt(OM * (1 + z) ** 3 + (1 - OM))


def D_growth(z):
    """Carroll-Press-Turner 1992 growth factor, normalised to D(0)=1."""
    a = 1.0 / (1 + z)
    return a * (OM / (OM + (1 - OM) * a**3)) ** 0.55


def Omz(z):
    return OM * (1 + z) ** 3 / (OM * (1 + z) ** 3 + (1 - OM))


# ── PS cluster number density ──────────────────────────────────────────────
_D0 = D_growth(0)


def n_PS(z, sigma=SIGMA_PS):
    """Comoving number density ∝ erfc(ν/√2) where ν=δ_c/σ(z)."""
    sigma_z = sigma * D_growth(z) / _D0
    return erfc(DELTA_C / (sigma_z * np.sqrt(2)))


# ── Physical virial quantities ─────────────────────────────────────────────
def r_vir(z, M_14=1.0):
    """Virial radius [Mpc], M_14 in units of 1e14 M_sun."""
    M_msun = M_14 * 1e14
    rho_crit = 3 * H_lcdm(z) ** 2 / (8 * np.pi * 4.3e-3)  # Msun/Mpc^3
    return (3 * M_msun / (4 * np.pi * DELTA_VIR * rho_crit)) ** (1 / 3)


def k_A_virial(z, M_14=1.0):
    """Virial kinetic energy proxy: G*M/r_vir ∝ H(z)^(4/3) for fixed M."""
    G_Mpc = 4.3e-3  # pc Msun^-1 (km/s)^2 → Mpc
    M_msun = M_14 * 1e14
    return G_Mpc * M_msun / r_vir(z, M_14)  # (km/s)^2


# ── Standard r_P ──────────────────────────────────────────────────────────
def r_P_standard(z):
    """Physical inter-cluster separation: n^(-1/3) / (1+z) [normalised]."""
    n = n_PS(z)
    if n < 1e-15:
        n = 1e-15
    return n ** (-1 / 3) / (1 + z)


# ── Pearson r utility ──────────────────────────────────────────────────────
def pearson_r(x, y):
    xm = x - np.mean(x)
    ym = y - np.mean(y)
    denom = np.sqrt(np.sum(xm**2) * np.sum(ym**2))
    if denom < 1e-30:
        return 0.0
    return float(np.sum(xm * ym) / denom)


# ═══════════════════════════════════════════════════════════════════════════
# TEST 1: k_A virial + r_P_standard  (baseline — should fail, NR-004)
# ═══════════════════════════════════════════════════════════════════════════
k_virial = np.array([k_A_virial(z) for z in Z_A1])
rP_std = np.array([r_P_standard(z) for z in Z_A1])

eps_virial_std = k_virial / rP_std**2
r_baseline = pearson_r(eps_virial_std, EPS_A1)
peak_baseline = Z_A1[np.argmax(eps_virial_std)]

print("=" * 60)
print("TEST 1: k_A virial + r_P standard  (NR-004 replication)")
print("=" * 60)
print(f"  Pearson r = {r_baseline:.3f}  (expected ~-0.46 from NR-004)")
print(f"  Predicted eps peaks at z={peak_baseline:.2f}")
print()

# ═══════════════════════════════════════════════════════════════════════════
# TEST 2: MULTING full structure formula
#   eps ∝ k_A × n^(2/3) × (1+z)^2  (derived from F_oP formula structure)
# ═══════════════════════════════════════════════════════════════════════════
n_arr = np.array([n_PS(z) for z in Z_A1])
eps_full_structure = k_virial * n_arr ** (2 / 3) * (1 + Z_A1) ** 2
r_full = pearson_r(eps_full_structure, EPS_A1)
peak_full = Z_A1[np.argmax(eps_full_structure)]

print("=" * 60)
print("TEST 2: Full MULTING structure  k_A × n^(2/3) × (1+z)^2")
print("=" * 60)
print(f"  Pearson r = {r_full:.3f}")
print(f"  Predicted eps peaks at z={peak_full:.2f}")
print()

# ═══════════════════════════════════════════════════════════════════════════
# TEST 3: Mass-scaling hypothesis
#   k_A uses CHARACTERISTIC mass M_*(z) ∝ D(z)^3 (PS peak mass)
#   eps ∝ D(z)^4 × H(z)^(4/3) × n^(2/3) × (1+z)^2
# ═══════════════════════════════════════════════════════════════════════════
D_arr = np.array([D_growth(z) / _D0 for z in Z_A1])
f_arr = np.array([Omz(z) ** 0.55 for z in Z_A1])

eps_D4 = D_arr**4 * (H_lcdm(Z_A1) / H0) ** (4 / 3) * n_arr ** (2 / 3) * (1 + Z_A1) ** 2
r_D4 = pearson_r(eps_D4, EPS_A1)
peak_D4 = Z_A1[np.argmax(eps_D4)]

print("=" * 60)
print("TEST 3: D^4 × H^(4/3) × n^(2/3) × (1+z)^2  (M* scaling)")
print("=" * 60)
print(f"  Pearson r = {r_D4:.3f}")
print(f"  Predicted eps peaks at z={peak_D4:.2f}")
print()

# ═══════════════════════════════════════════════════════════════════════════
# TEST 4: Merger epoch r_P hypothesis
#   r_P(z) = r_P_standard(z) / (1 + A × xi_merger(z) × tau_diss)^(1/2)
#   xi_merger(z) ∝ (1+z)^2.5 / H(z)  [per-cluster merger rate × H^-1]
# WHY: at peak merger epoch (z~0.3-0.5), clusters approach each other
#      → effective r_P decreases → F_oP increases → eps increases
# ═══════════════════════════════════════════════════════════════════════════
print("=" * 60)
print("TEST 4: Merger-epoch r_P(z) hypothesis  [H-k_A-1]")
print("=" * 60)

xi_merger = (1 + Z_A1) ** 2.5 / (H_lcdm(Z_A1) / H0)  # normalized

best_r4 = -2.0
best_A4 = None

for A_val in np.logspace(-3, 2, 200):
    rP_merger = rP_std / np.sqrt(1 + A_val * xi_merger)
    eps_pred = k_virial / rP_merger**2
    r_val = pearson_r(eps_pred, EPS_A1)
    if r_val > best_r4:
        best_r4 = r_val
        best_A4 = A_val

rP_best4 = rP_std / np.sqrt(1 + best_A4 * xi_merger)
eps_best4 = k_virial / rP_best4**2
peak_best4 = Z_A1[np.argmax(eps_best4)]

print(f"  Best r  = {best_r4:.3f}  (kill threshold: 0.75)")
print(f"  Best A  = {best_A4:.4f}  (merger coupling amplitude)")
print(f"  Peak at z={peak_best4:.2f}")
print()

# ═══════════════════════════════════════════════════════════════════════════
# TEST 5: D(z) × H(z)^(1/3) class — parametric peak-at-0.40 family
# ═══════════════════════════════════════════════════════════════════════════
print("=" * 60)
print("TEST 5: D^n × H^(n/3) family  (all peak at z=0.40)")
print("=" * 60)

for n_val in [1, 2, 3, 4]:
    cand = D_arr**n_val * (H_lcdm(Z_A1) / H0) ** (n_val / 3)
    r_val = pearson_r(cand, EPS_A1)
    peak = Z_A1[np.argmax(cand)]
    print(f"  D^{n_val} × H^({n_val}/3):  r={r_val:.3f}  peak_z={peak:.2f}")

print()

# ═══════════════════════════════════════════════════════════════════════════
# TEST 6: f×sigma8(z) — growth rate (best single non-monotone signal)
# ═══════════════════════════════════════════════════════════════════════════
fsig8 = f_arr * (0.81 * D_arr)
r_fsig8 = pearson_r(fsig8, EPS_A1)
peak_fsig8 = Z_A1[np.argmax(fsig8)]

print("=" * 60)
print("TEST 6: f×sigma8(z)  (RSD-observable, r=0.775 known)")
print("=" * 60)
print(f"  Pearson r = {r_fsig8:.3f}  peak_z={peak_fsig8:.2f}")
print()

# ═══════════════════════════════════════════════════════════════════════════
# TEST 7: COMBINED — D(z) × H^(1/3) × merger correction
# ═══════════════════════════════════════════════════════════════════════════
print("=" * 60)
print("TEST 7: D×H^(1/3) × rP_merger  (combined hypothesis)")
print("=" * 60)

DH13 = D_arr * (H_lcdm(Z_A1) / H0) ** (1 / 3)  # peaks at z=0.40

best_r7 = -2.0
best_A7 = None

for A_val in np.logspace(-3, 2, 300):
    rP_comb = rP_std / np.sqrt(1 + A_val * xi_merger)
    eps_comb = DH13 * (H_lcdm(Z_A1) / H0) ** (4 / 3) / rP_comb**2
    r_val = pearson_r(eps_comb, EPS_A1)
    if r_val > best_r7:
        best_r7 = r_val
        best_A7 = A_val

eps_best7 = DH13 * (H_lcdm(Z_A1) / H0) ** (4 / 3) / (rP_std / np.sqrt(1 + best_A7 * xi_merger)) ** 2
peak_best7 = Z_A1[np.argmax(eps_best7)]
print(f"  Best r  = {best_r7:.3f}")
print(f"  Best A  = {best_A7:.4f}")
print(f"  Peak at z={peak_best7:.2f}")
print()

# ═══════════════════════════════════════════════════════════════════════════
# TEST 8: Unconstrained 2-param scan k_A ~ D^a × H^b
# ═══════════════════════════════════════════════════════════════════════════
print("=" * 60)
print("TEST 8: Unconstrained D^a × H^b scan  (upper bound on r)")
print("=" * 60)

best_r8 = -2.0
best_params8 = None
for a in np.arange(0, 7, 0.5):
    for b in np.arange(-1, 3, 0.25):
        cand = D_arr**a * (H_lcdm(Z_A1) / H0) ** b
        r_val = pearson_r(cand, EPS_A1)
        if r_val > best_r8:
            best_r8 = r_val
            best_params8 = (a, b)
            best_peak8 = Z_A1[np.argmax(cand)]

a8, b8 = best_params8
print(f"  Best: D^{a8:.1f} × H^{b8:.2f}  r={best_r8:.3f}  peak_z={best_peak8:.2f}")
print()

# ═══════════════════════════════════════════════════════════════════════════
# SUMMARY
# ═══════════════════════════════════════════════════════════════════════════
print("=" * 60)
print("SUMMARY — all candidates vs Table A1 eps(z)")
print("=" * 60)
print(f"{'Candidate':<40} {'r':>7}  {'peak_z':>7}  {'Verdict'}")
print("-" * 70)
rows = [
    ("k_A virial + r_P standard (NR-004)", r_baseline, peak_baseline),
    ("k_A × n^(2/3) × (1+z)^2", r_full, peak_full),
    ("D^4 × H^(4/3) × n^(2/3) × (1+z)^2", r_D4, peak_D4),
    ("k_A virial + r_P merger-epoch (H-k_A-1)", best_r4, peak_best4),
    ("D×H^(1/3) (D^n×H^(n/3) family base)", pearson_r(DH13, EPS_A1), Z_A1[np.argmax(DH13)]),
    ("f×sigma8", r_fsig8, peak_fsig8),
    ("D×H^(1/3) + r_P merger combined", best_r7, peak_best7),
    (f"Unconstrained D^{a8:.1f}×H^{b8:.2f}", best_r8, best_peak8),
]
for name, r_val, peak in rows:
    if r_val > 0.85:
        verdict = ">>> KILL-TEST PASS <<"
    elif r_val > 0.75:
        verdict = "NEAR-THRESHOLD"
    elif r_val > 0.60:
        verdict = "PARTIAL"
    elif r_val > 0.0:
        verdict = "weak"
    else:
        verdict = "NEGATIVE"
    print(f"  {name:<40} {r_val:>6.3f}  {peak:>6.2f}  {verdict}")

print()

# ── Kill-test verdict ──────────────────────────────────────────────────────
print("=" * 60)
print("KILL-TEST VERDICT  (threshold: r > 0.85)")
print("=" * 60)
if best_r4 > 0.85:
    print(f"  H-k_A-1 CONFIRMED: r={best_r4:.3f} > 0.85")
    print("  → r_P(z) merger epoch is the missing ingredient")
    print("  → virial k_A works when r_P has correct shape")
elif best_r4 > 0.75:
    print(f"  H-k_A-1 NEAR-THRESHOLD: r={best_r4:.3f} (need > 0.85)")
    print("  → partial support; need better merger rate model")
else:
    print(f"  H-k_A-1 FALSIFIED: r={best_r4:.3f} < 0.75")
    print("  → merger-epoch r_P is insufficient")
    print("  → BETA-1 HOLD remains; await TJB Q2 response")

print()
unconstrained_gap = best_r8 - best_r4
print(f"  Unconstrained ceiling: r={best_r8:.3f}")
print(f"  H-k_A-1 vs ceiling gap: {unconstrained_gap:.3f}")
print(f"  Physical-mechanistic gap to close: {0.85 - best_r4:.3f}")
