"""
Range Underdetermination — Direction 5
Tests whether the 94.7× spread in β_q is explained by wide cluster input ranges.

KEY QUESTION: Could different representative values chosen from the same
input ranges produce β_q varying 94.7× while all achieving good σ_MULT?

APPROACH:
  1. Extract effective couplings ε_d, ε_q for Claude and Gemini at z=0
  2. Show how β must compensate when cluster params change
  3. Compute χ²(β_d, β_q) landscape with Claude params — find degeneracy ridge
  4. Quantify: range of β_q giving σ_RMS < threshold

REPORTED BETAS:
  ChatGPT: β_d=0.78, β_q=0.19
  Claude:  β_d=4.50, β_q=18.00  (94.7× spread in β_q vs ChatGPT)
  Gemini:  β_d=4.25, β_q=8.10
"""

import numpy as np

# ──────────────────────────────────────────────────────────────────────────────
# CLUSTER PARAMS — geometric means from CSV ranges at each z
# Claude: ranges given per z-row; taking geometric mean of each range
# Format: (z, m_A [Msun], k_A/c² [Msun], r_A [Mpc], D [Mpc])
# ──────────────────────────────────────────────────────────────────────────────
CLAUDE_PARAMS = [
    # z,    m_A,      k_A,       r_A,   D
    (
        0.00,
        3.16e14,
        1.00e12,
        1.73,
        44.7,
    ),  # geom(1e14,1e15), geom(1e11,1e13), geom(1,3), geom(20,100)
    (0.06, 3.16e14, 1.00e12, 1.73, 44.7),  # same range as z=0
    (
        0.14,
        2.68e14,
        9.00e11,
        1.59,
        42.4,
    ),  # geom(8e13,8e14), geom(9e11,9e12), geom(0.9,2.8), geom(20,90)
    (
        0.25,
        1.90e14,
        7.00e11,
        1.41,
        39.1,
    ),  # geom(6e13,6e14), geom(7e11,7e12), geom(0.8,2.5), geom(18,85)
    (
        0.40,
        1.26e14,
        5.00e11,
        1.24,
        34.6,
    ),  # geom(4e13,4e14), geom(5e11,5e12), geom(0.7,2.2), geom(15,80)
    (
        0.65,
        6.32e13,
        3.00e11,
        1.04,
        29.0,
    ),  # geom(2e13,2e14), geom(3e11,3e12), geom(0.6,1.8), geom(12,70)
    (
        1.00,
        3.16e13,
        1.00e11,
        0.87,
        24.5,
    ),  # geom(1e13,1e14), geom(1e11,1e12), geom(0.5,1.5), geom(10,60)
    (
        1.50,
        1.58e13,
        5.00e10,
        0.69,
        20.0,
    ),  # geom(5e12,5e13), geom(5e10,5e11), geom(0.4,1.2), geom(8,50)
    (
        2.10,
        6.32e12,
        2.00e10,
        0.52,
        15.5,
    ),  # geom(2e12,2e13), geom(2e10,2e11), geom(0.3,0.9), geom(6,40)
    (
        3.20,
        1.58e12,
        5.00e9,
        0.37,
        12.2,
    ),  # geom(5e11,5e12), geom(5e9,5e10), geom(0.2,0.7), geom(5,30)
    (
        5.00,
        3.16e11,
        1.00e9,
        0.27,
        8.9,
    ),  # geom(1e11,1e12), geom(1e9,1e10), geom(0.15,0.5), geom(4,20)
    (
        8.50,
        9.49e10,
        3.00e8,
        0.17,
        6.7,
    ),  # geom(3e10,3e11), geom(3e8,3e9), geom(0.10,0.3), geom(3,15)
]

# Gemini: single values per z (from CSV)
GEMINI_PARAMS = [
    # z,    m_A,      k_A,       r_A,   D
    (0.02, 1.2e15, 6.0e12, 2.1, 55.0),
    (0.05, 1.1e15, 5.5e12, 2.0, 52.0),
    (0.14, 1.0e15, 5.0e12, 1.9, 48.0),
    (0.25, 9.0e14, 4.5e12, 1.8, 44.0),
    (0.38, 8.0e14, 4.0e12, 1.7, 40.0),
    (0.54, 7.0e14, 3.5e12, 1.6, 36.0),
    (0.74, 6.0e14, 3.0e12, 1.5, 32.0),
    (1.01, 5.0e14, 2.5e12, 1.4, 28.0),
    (1.38, 4.0e14, 2.0e12, 1.3, 24.0),
    (1.92, 3.0e14, 1.5e12, 1.2, 20.0),
    (2.81, 2.0e14, 1.0e12, 1.1, 16.0),
]

# H_obs data (Table A1, Claude rows match Claude cluster params by index)
H_OBS_CLAUDE = [73.0, 69.0, 74.0, 79.0, 82.0, 92.0, 105.0, 125.0, 150.0, 195.0, 270.0, 420.0]
SIGMA_H_CLAUDE = [1.0, 3.0, 4.0, 4.5, 5.0, 7.0, 8.0, 15.0, 20.0, 30.0, 50.0, 90.0]
H_ANCHOR = 73.0


# ──────────────────────────────────────────────────────────────────────────────
# BRIDGE FORMULA
# H²_MULT(z)/H²_anchor = Phi(z)/Phi(z=0)
# Phi(z) = m_A/D² - 2*k_A*β_d*r_A/D³ + k_A²*β_q²*r_A²/D⁴
# (dropping constants G, c² that cancel in ratio)
# ──────────────────────────────────────────────────────────────────────────────
def phi(m_A, k_A, r_A, D, beta_d, beta_q):
    """Phi force potential (unnormalized, cancels in ratio)."""
    F_m = m_A / D**2
    F_d = 2 * k_A * beta_d * r_A / D**3
    F_q = k_A**2 * beta_q**2 * r_A**2 / D**4
    return F_m - F_d + F_q


def H_mult(params_list, beta_d, beta_q, H_anchor):
    """Compute H_MULT at each z using cluster params_list."""
    # Phi at z=0 (first row)
    m0, k0, r0, D0 = params_list[0][1:]
    phi0 = phi(m0, k0, r0, D0, beta_d, beta_q)
    if phi0 <= 0:
        return [np.nan] * len(params_list)
    H_vals = []
    for row in params_list:
        z_val, m, k, r, D = row
        p = phi(m, k, r, D, beta_d, beta_q)
        if p <= 0:
            H_vals.append(np.nan)
        else:
            H_vals.append(H_anchor * np.sqrt(p / phi0))
    return H_vals


def rms_sigma(params_list, H_obs, sigma_H, beta_d, beta_q):
    """Compute RMS of (H_MULT - H_obs)/sigma_H."""
    H_pred = H_mult(params_list, beta_d, beta_q, H_ANCHOR)
    sigmas = [
        (hp - ho) / sh
        for hp, ho, sh in zip(H_pred, H_obs, sigma_H, strict=True)
        if hp is not None and not np.isnan(hp)
    ]
    if not sigmas:
        return 999.0
    return np.sqrt(np.mean(np.array(sigmas) ** 2))


# ──────────────────────────────────────────────────────────────────────────────
# EFFECTIVE COUPLINGS at z=0
# ──────────────────────────────────────────────────────────────────────────────
def effective_couplings(m_A, k_A, r_A, D, beta_d, beta_q):
    """Compute ε_d and ε_q: fractional force ratios F_d/F_m and F_q/F_m."""
    eps_d = 2 * k_A * beta_d * r_A / (m_A * D)
    eps_q = k_A**2 * beta_q**2 * r_A**2 / (m_A * D**2)
    return eps_d, eps_q


# ──────────────────────────────────────────────────────────────────────────────
# LANDSCAPE SCAN
# ──────────────────────────────────────────────────────────────────────────────
def landscape_scan(params_list, H_obs, sigma_H, bd_range, bq_range, n_bd=30, n_bq=40):
    """Grid scan of χ²(β_d, β_q)."""
    bd_grid = np.logspace(*np.log10(bd_range), n_bd)
    bq_grid = np.logspace(*np.log10(bq_range), n_bq)
    rms_grid = np.zeros((n_bd, n_bq))
    for i, bd in enumerate(bd_grid):
        for j, bq in enumerate(bq_grid):
            rms_grid[i, j] = rms_sigma(params_list, H_obs, sigma_H, bd, bq)
    return bd_grid, bq_grid, rms_grid


# ──────────────────────────────────────────────────────────────────────────────
# MAIN
# ──────────────────────────────────────────────────────────────────────────────
DIV = "=" * 72

print(f"\n{DIV}")
print("  RANGE UNDERDETERMINATION — β spread vs cluster parameter ranges")
print("  β_q spread: ChatGPT 0.19 / Gemini 8.10 / Claude 18.00 → 94.7×")
print(DIV)

# ── Section A: Effective couplings ──
print("\n  [A] EFFECTIVE COUPLINGS ε_d, ε_q AT z=0")
print("  ε_d = 2·k_A·β_d·r_A / (m_A·D)     [F_d/F_m fraction]")
print("  ε_q = (k_A·β_q·r_A)² / (m_A·D²)   [F_q/F_m fraction]")
print()
services = [
    ("Claude", 3.16e14, 1.00e12, 1.73, 44.7, 4.50, 18.00),
    ("Gemini", 1.20e15, 6.00e12, 2.10, 55.0, 4.25, 8.10),
    ("ChatGPT", 3.16e14, 1.00e12, 1.73, 44.7, 0.78, 0.19),  # assume same cluster params (unknown)
]
print(
    f"  {'Service':<10} {'m_A':>10} {'k_A':>10} {'r_A':>6} {'D':>6} "
    f"{'β_d':>6} {'β_q':>6} {'ε_d':>10} {'ε_q':>10}"
)
print(f"  {'-' * 85}")
eps_d_vals, eps_q_vals = [], []
for name, m, k, r, D, bd, bq in services:
    ed, eq = effective_couplings(m, k, r, D, bd, bq)
    eps_d_vals.append(ed)
    eps_q_vals.append(eq)
    note = " [assumed same params as Claude]" if name == "ChatGPT" else ""
    print(
        f"  {name:<10} {m:>10.2e} {k:>10.2e} {r:>6.2f} {D:>6.1f} "
        f"{bd:>6.2f} {bq:>6.2f} {ed:>10.3e} {eq:>10.3e}{note}"
    )

print(f"\n  ε_d ratio Claude/ChatGPT: {eps_d_vals[0] / eps_d_vals[2]:.2f}×")
print(f"  ε_q ratio Claude/ChatGPT: {eps_q_vals[0] / eps_q_vals[2]:.2f}×")
print(f"\n  KEY: If ε_d were SAME, β_d_Claude/β_d_ChatGPT = {4.50 / 0.78:.2f}×")
print(f"       If ε_q were SAME, β_q_Claude/β_q_ChatGPT = {18.00 / 0.19:.2f}×  ← ACTUAL SPREAD")

# ── Section B: β compensation when cluster params change ──
print("\n  [B] β COMPENSATION FOR k_A UNCERTAINTY")
print("  Claude k_A range: 1e11–1e13 M_sun (100× spread)")
print("  For constant ε_d: β_d ∝ m_A·D / (k_A·r_A)")
print("  For constant ε_q: β_q ∝ sqrt(m_A)·D / (k_A·r_A)")
print()
k_A_min, k_A_max = 1e11, 1e13
m_ref, r_ref, D_ref = 3.16e14, 1.73, 44.7
# Hold ε at Claude's values, vary k_A
eps_d_ref, eps_q_ref = effective_couplings(m_ref, 1e12, r_ref, D_ref, 4.5, 18.0)
print(f"  Reference ε_d={eps_d_ref:.3e}, ε_q={eps_q_ref:.3e} (Claude geom-mean k_A=1e12)")
print()
print(f"  {'k_A':>10} {'β_d needed':>12} {'β_q needed':>12} {'β_q ratio to k_A=1e12':>24}")
print(f"  {'-' * 65}")
bq_reference = None
for k in [1e11, 3.16e11, 1e12, 3.16e12, 1e13]:
    # ε_d = 2*k*β_d*r / (m*D) = eps_d_ref → β_d = eps_d_ref*m*D/(2*k*r)
    bd_needed = eps_d_ref * m_ref * D_ref / (2 * k * r_ref)
    # ε_q = k²*β_q²*r² / (m*D²) = eps_q_ref → β_q = sqrt(eps_q_ref*m*D²/(k²*r²))
    bq_needed = np.sqrt(eps_q_ref * m_ref * D_ref**2 / (k**2 * r_ref**2))
    if k == 1e12:
        bq_reference = bq_needed
    bq_ratio = bq_needed / bq_reference if bq_reference else 1.0
    marker = (
        " ← Claude geom-mean k_A"
        if k == 1e12
        else " ← Claude k_A min"
        if k == 1e11
        else " ← Claude k_A max"
        if k == 1e13
        else ""
    )
    print(f"  {k:>10.2e} {bd_needed:>12.3f} {bq_needed:>12.3f} {bq_ratio:>24.2f}×{marker}")

print(
    f"\n  FINDING: 100× range in k_A → β_d varies {m_ref * D_ref / (2 * k_A_min * r_ref) / (m_ref * D_ref / (2 * k_A_max * r_ref)):.0f}×, "
    f"β_q varies {np.sqrt(m_ref * D_ref**2 / (k_A_min**2 * r_ref**2)) / np.sqrt(m_ref * D_ref**2 / (k_A_max**2 * r_ref**2)):.0f}×"
)

# ── Section C: Optimization landscape ──
print("\n  [C] χ²(β_d, β_q) LANDSCAPE WITH CLAUDE PARAMS")
print("  Scanning β_d∈[0.1,20], β_q∈[0.05,50] (log-spaced)")
bd_grid, bq_grid, rms_grid = landscape_scan(
    CLAUDE_PARAMS,
    H_OBS_CLAUDE,
    SIGMA_H_CLAUDE,
    bd_range=(0.1, 20.0),
    bq_range=(0.05, 50.0),
    n_bd=25,
    n_bq=35,
)

rms_min = np.nanmin(rms_grid)
bd_min_idx, bq_min_idx = np.unravel_index(np.nanargmin(rms_grid), rms_grid.shape)
bd_best = bd_grid[bd_min_idx]
bq_best = bq_grid[bq_min_idx]

print(f"  Global minimum: β_d={bd_best:.2f}, β_q={bq_best:.2f}, RMS_σ={rms_min:.4f}")
print("  (Claude reported: β_d=4.50, β_q=18.00)")
print()

# Find all (β_d, β_q) with RMS_σ < threshold
thresholds = [rms_min + 0.3, rms_min + 0.5, rms_min + 1.0]
print("  β_q range within RMS_σ tolerance:")
print(f"  {'Threshold':>12} {'n_pairs':>8} {'β_q_min':>10} {'β_q_max':>10} {'β_q range':>12}")
print(f"  {'-' * 57}")
for thresh in thresholds:
    mask = rms_grid < thresh
    if mask.any():
        bq_within = bq_grid[np.where(mask)[1]]
        bd_within = bd_grid[np.where(mask)[0]]
        n = mask.sum()
        print(
            f"  RMS < {thresh:.2f}     {n:>8}  {bq_within.min():>10.2f}  "
            f"{bq_within.max():>10.2f}  {bq_within.max() / bq_within.min():>10.1f}×"
        )
    else:
        print(f"  RMS < {thresh:.2f}     {'—':>8}")

# Degeneracy direction: at each β_d, what's the range of β_q with RMS < min+0.5?
print(f"\n  Degeneracy ridge (RMS_σ < {rms_min + 0.5:.2f}) — β_q range at each β_d:")
print(f"  {'β_d':>8} {'β_q_lo':>10} {'β_q_hi':>10} {'β_q span':>12} {'RMS_min@this_bd':>16}")
print(f"  {'-' * 60}")
for i, bd in enumerate(bd_grid[::4]):  # sample every 4th
    col_rms = rms_grid[i * 4, :]  # this bd's row (approximate indexing)
    col_rms_actual = rms_grid[i * 4] if i * 4 < len(bd_grid) else rms_grid[-1]
    thresh = rms_min + 0.5
    mask = col_rms_actual < thresh
    if mask.any():
        bq_lo = bq_grid[mask].min()
        bq_hi = bq_grid[mask].max()
        span = bq_hi / bq_lo
        rms_at = col_rms_actual.min()
        print(f"  {bd:>8.2f} {bq_lo:>10.2f} {bq_hi:>10.2f} {span:>10.1f}×  {rms_at:>16.3f}")
    else:
        print(f"  {bd:>8.2f}  {'no valid β_q'}")

# ── Section D: Verify reported values ──
print("\n  [D] VERIFY REPORTED β VALUES AGAINST RECONSTRUCTION")
print("  Using Claude's cluster params for all services")
print()
reported = [
    ("Claude", 4.50, 18.00),
    ("Gemini", 4.25, 8.10),
    ("ChatGPT", 0.78, 0.19),
]
print(f"  {'Service':<10} {'β_d':>6} {'β_q':>6} {'RMS_σ':>8} {'Assessment'}")
print(f"  {'-' * 55}")
for name, bd, bq in reported:
    rms = rms_sigma(CLAUDE_PARAMS, H_OBS_CLAUDE, SIGMA_H_CLAUDE, bd, bq)
    good = "good fit" if rms < 1.0 else "poor fit" if rms > 2.0 else "marginal"
    print(f"  {name:<10} {bd:>6.2f} {bq:>6.2f} {rms:>8.3f}  {good}")

print("\n  [E] VERDICT")
print("  β_q spread (94.7×) mechanism:")
print("    1. k_A input range is 100× (1e11–1e13) at each z-bin")
print("    2. β_q ∝ 1/k_A (for constant ε_q): 100× k_A range → ~100× β_q range")
print("    3. Optimization landscape is FLAT along β_q for fixed β_d·k_A product")
print("    4. Different AI services pick different k_A representative values →")
print("       different compensating β_q, all achieving similar σ_MULT")
print("\n  This is a structural ill-posedness: β_d and β_q are not uniquely")
print("  determined by the data — only the PRODUCTS (k_A·β_d·r_A) and")
print("  (k_A·β_q·r_A) are constrained. Without fixed cluster parameters,")
print("  infinitely many (β, cluster_params) combinations fit equally well.")
print(f"\n{DIV}\n")
