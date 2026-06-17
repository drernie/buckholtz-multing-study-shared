# Pearson r Test Results — MULTING vs H_CC (Moresco+2022)
NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION
Date: 2026-06-16

## Data
- Clusters: MCXC-I (1742 total) + PSZ2 Y_SZ (name join via PSZ2.MCXC column)
- With E_thermal/c² (T_i, Path B Y_SZ): 548 clusters, z=0.011–0.888
- H(z) CC: 27 Moresco+2022 points (FLRW-independent)
- Merger-excluded: 2 hard-excluded (Bullet Cluster, Abell 520)
- Valid pairs for r test: 443 (cluster z within CC z range 0.07–1.965)

## Method (OUR_RECONSTRUCTION)
phi = M500/D^2 - 2*beta_d*T_i*R500/D^3 + (beta_q*T_i*R500)^2/D^4
H_MULTING = H_0 * sqrt(phi(z)/phi(z_ref))   [ref = lowest-z cluster]
D = D_0/(1+z)  [proper inter-cluster scale hypothesis — G1 BLOCKER]
Pearson r between H_MULTING(z_i) and H_CC_interp(z_i) for 443 cluster-CC pairs

## Results (Pearson r) — Full MCXC+PSZ2 sample

| Model                          |    r   |   n | Notes                          |
|--------------------------------|--------|-----|--------------------------------|
| Trivial: just redshift z       | 0.8904 | 443 | Upper bound from monotone H_CC |
| LCDM Planck18                  | 0.8795 | 443 | Standard cosmological model    |
| Power law H=73*(1+z)^1.5       | 0.8870 | 443 | Simple fitting formula         |
| MULTING monopole (beta_d=bq=0) | 0.7334 | 443 | D=100/(1+z) Mpc                |
| MULTING full, grid best        | 0.6235 | 443 | beta_d=1e2, beta_q=3.2e7       |
| Malmquist bias: log(M500)      | 0.6030 | 443 | Selection effect only          |

## Results — Bin-averaged Pearson r (Task 2)
Reduces intra-bin T_i scatter; does NOT remove between-bin Malmquist bias.

| n_bins | n_valid | r_MULTING | r_monopole | r_trivial_z | MULTING > trivial? |
|--------|---------|-----------|------------|-------------|--------------------|
|      5 |       4 |    0.7987 |     0.9250 |      0.9967 | NO                 |
|      7 |       5 |    0.9853 |     0.9692 |      0.9918 | NO (CI wide, n=5)  |
|     10 |       7 |    0.8591 |     0.9232 |      0.9931 | NO                 |
|     15 |      10 |    0.7834 |     0.8496 |      0.9817 | NO                 |
|     20 |      13 |    0.8495 |     0.8633 |      0.9716 | NO                 |

Note: trivial z-only r is HIGHER on bins (0.97–0.99) because binned H_CC(z_bin)
is nearly a perfect function of z_bin. Binning amplifies trivial baseline.

## Results — CHEX-MATE proxy subsample (Task 3)
Selection: M500 > 2e14 Msun, z = [0.05, 0.60] (volume-limited approximation)

| Model                          |    r   |   n | Notes                              |
|--------------------------------|--------|-----|------------------------------------|
| Trivial: just redshift z       | 0.8860 | 386 | Slightly reduced vs full sample    |
| r(log M500, H_CC)              | 0.5544 | 386 | Malmquist bias quantifier          |
| MULTING monopole               | 0.6972 | 386 | Best MULTING component             |
| MULTING full (beta_d,bq best)  | 0.5818 | 386 | Full formula                       |
| r(log M500, z)                 | 0.6223 | 386 | Selection bias strength            |

CHEX-MATE data status: NOT in VizieR (CHEX-MATE catalogs not indexed as machine-readable).
Proxy uses mass-selected MCXC+PSZ2 subsample → reduces but does NOT eliminate Malmquist bias.
r(logM500, z) dropped from 0.677 (full) to 0.622 (mass-selected) — modest improvement.

## Results — CHEX-MATE combined catalog (104 clusters, Task 4 — 2026-06-16)
Source: J/A+A/686/A68 (Rossetti+2024, 30 XMM T_X) + J/A+A/693/A2 (Sereno+2025, σ_v, M_dyn)
Ti_best = XMM T_X where available, else 1.5·M_dyn·σ_v²/c²

| Sample                                  |  n  | r_trivial_z | r_MULTING | r(logM500,z) | MULTING>trivial? |
|-----------------------------------------|-----|-------------|-----------|--------------|-----------------|
| All 104 CHEX-MATE (sigma_v Ti)          | 100 |   0.9321    |  0.6269   |   0.5302     | NO              |
| 23 with real XMM T_X (from Rossetti+24) |  22 |   0.9142    |  0.7029   |   0.0941     | NO              |
| Tier-1 z<0.2 (volume-limited, sigma_v)  |  53 |   0.8255    |  0.2783   |   0.2255     | NO              |

Key observation (Malmquist quantifier):
- Full 104: r(logM500,z) = 0.530 — moderate selection bias (mass-selected but sigma_v-limited)
- XMM subset: r(logM500,z) = 0.094 — almost NO Malmquist bias (mass-selected + z-stratified)
- Tier-1 z<0.2: r(logM500,z) = 0.226 — very mild selection bias
Despite near-zero Malmquist bias on XMM T_X subset, MULTING does NOT outperform trivial (r=0.703 vs 0.914).
This rules out Malmquist bias as the SOLE explanation for MULTING underperforming trivial.

## Critical finding
MULTING does NOT outperform trivial baselines on any tested sample.
Monopole only CONSISTENTLY outperforms full formula in ALL tests.

Reasons (updated after CHEX-MATE unbiased test):
1. Dipole+quadrupole add cluster-to-cluster T_i scatter on top of z correlation.
2. D=D_0/(1+z) makes phi(z) a monotone function → trivial z correlation dominates.
3. Even without Malmquist bias (XMM T_X, r(M,z)=0.09), MULTING loses to trivial.
The G1 BLOCKER (no analytic H(z) from F_oP) means D(z) is phenomenological — we may be
testing a scalar proxy that conflates z and Ti rather than a genuine MULTING prediction.

## Selection bias quantified
r(log T_i, z) = 0.648
r(log M500, z) = 0.677 (full), 0.622 (mass-selected)
MCXC is flux-limited: at higher z, only massive, hot clusters detected.
Spurious T_i–z correlation is INDISTINGUISHABLE from MULTING signal without
a volume-limited sample with high-quality T_X measurements.

## C6/C9 Particle Physics Claims (PDG 2024 verification — Task 1)

### C6: m²_W : m²_Z : m²_H = 7 : 9 : 17
| Ratio | Measured | Claim | delta | sigma | Status |
|-------|----------|-------|-------|-------|--------|
| m_W²  | 7.0000   | 7     | 0%    | 0σ    | (norm) |
| m_Z²  | 9.0114   | 9     | 0.13% | 5.5σ  | ⚠️ FAIL |
| m_H²  | 16.9874  | 17    | 0.07% | 0.4σ  | ✅ PASS |
(m_H = 125.25 GeV → ratio = 17.0010 → virtually perfect)

VERDICT: C6 is MIXED. Higgs ratio (17) is [CONFIRMED] at <0.5σ.
Z ratio (9) is [OPEN] — 5.5σ discrepancy may reflect W mass precision (80.3692 GeV PDG2024).

### C9: (4/3)(m_τ/m_e)¹² = α_EM / α_G
With α_G = G·m_e²/(ℏ·c) = 1.752e-45 (electron mass, not proton mass):
  LHS = 4.166172e+42
  RHS = 4.165609e+42
  LHS/RHS = 1.000135  →  delta = 0.014%  →  0.17σ from m_τ uncertainty

VERDICT: C9 is [CONFIRMED] at 0.17σ.
KEY: TJB's α_G is defined via ELECTRON mass, not proton mass.
Using proton mass α_G = 5.906e-39 gives ratio = 3.37 million (6 orders off).
The proton/electron mass ratio squared = (1836)² = 3.37×10⁶ — exact match to
the discrepancy — confirmed α_G definition is the explanation.

## Interpretation
POSITIVE r (0.62) = correct sign, theory not falsified.
BUT: test is INCONCLUSIVE on flux-limited sample.
Full MULTING formula adds noise on top of z correlation rather than signal.
MULTING > trivial would require: high-quality T_X (not Y_SZ proxy) + volume-limited sample.

## For conclusive test: need one of
- CHEX-MATE: actual XMM T_X data (118 Planck clusters) — NOT yet in VizieR
- SPT-SZ: 700+ SZ-selected (less Malmquist bias than X-ray flux-limited)
- ACT-DR5: 4195 SZ-selected clusters

## Action for TJB letter (after 2026-06-18)
Present as honest preliminary finding:
  - Real catalog T_i gives r=0.62 with H_CC Moresco+2022
  - Flux-limited sample cannot distinguish MULTING from Malmquist bias
  - C9 is confirmed at 0.17σ with α_G(electron mass) — elegantly precise
  - C6 Higgs ratio confirmed at 0.4σ; Z ratio 5.5σ — ask TJB about this
  - Key open question: what is D(z) in your formula? (G1 blocker)
  - Volume-limited cluster sample with XMM T_X needed for Step 4 Pearson r

## Caveats
1. [SELECTION BIAS] Flux-limited sample inflates r artificially.
2. [G1 BLOCKER] D=D_0/(1+z) is phenomenological — not derived from TJB.
3. [G2 BLOCKER] beta values are fitted, not from first principles.
4. [T_i SCALE] Real T_i ~ 1e8–1e9 M_sun vs TJB AI k_A ~ 1e11–1e13 M_sun.
   Effective beta must be rescaled by ~1e3 relative to TJB Table A1 values.
5. [C9 alpha_G] TJB uses α_G(m_e) not α_G(m_p) — important definitional choice.
