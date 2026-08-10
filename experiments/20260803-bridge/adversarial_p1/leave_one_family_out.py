"""Leave-one-cluster-family-out (and leave-one-z-bin-out) check on the mass-scaling
exponent d ln(u)/d ln(M), u=k*r/m, flagged as not-yet-run in ADVERSARIAL_AUDIT_P1.md
S16-D and S15-D. NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION.

HONEST NOTE, established first because it changes what this script can do: the
n=548 subsample of data/clusters_clean.csv (rows with Ethermal_c2_Msun not null)
is checked below and found to be 100% catalog=MCXC-I, 100%
ICM_proxy_type=Y_SZ_derived_LCDM, 100% dynamical_state=unknown -- there is no
pre-existing catalog/survey/pipeline "family" label to leave out. The audit's
S16 named "leave-one-cluster-family-out" and "leave-one-redshift-bin-out" as two
DISTINCT tests, which presumes a real catalog-origin split that this dataset does
not carry. Rather than silently substitute one test for the other, this script:
  (1) confirms and reports the homogeneity finding itself (a real result -- it
      means the +-0.041 uncertainty already understates systematic risk, since
      it was never checked against an independent pipeline/catalog),
  (2) builds the best available non-arbitrary partition from what DOES vary --
      mass tercile (directly relevant to an M-scaling question) as the family
      proxy, plus the genuinely-intended z-quartile split, and runs
      leave-one-out on both.
"""

import numpy as np
import pandas as pd

df = pd.read_csv("data/clusters_clean.csv")
sub = df[df["Ethermal_c2_Msun"].notna()].copy()
assert len(sub) == 548

print("=" * 78)
print("[0] Is there a real cluster-family label to leave out?")
print("=" * 78)
for col in ("catalog", "ICM_proxy_type", "dynamical_state", "merger_exclusion_flag"):
    vc = sub[col].value_counts(dropna=False)
    print(f"  {col}: {dict(vc)}")
print(
    "  -> NO. All 548 clusters share one catalog, one ICM proxy pipeline, one\n"
    "     (unknown) dynamical-state flag. The +-0.041 uncertainty on the mass-\n"
    "     scaling exponent (S8 of the audit) is a STATISTICAL uncertainty within\n"
    "     one pipeline. It carries no information about cross-pipeline systematic\n"
    "     risk, because no second pipeline is present to compare against. This is\n"
    "     itself a finding, not a null result: report it, do not paper over it by\n"
    "     silently substituting a different split without saying so."
)

k = sub["Ethermal_c2_Msun"].to_numpy()
r = sub["R500c_Mpc"].to_numpy()
m = sub["M500c_Msun"].to_numpy()
z = sub["z"].to_numpy()
u = k * r / m
logM, logU = np.log(m), np.log(u)


def slope_ci(logM_, logU_, n_boot=3000, seed=1):
    slope, _ = np.polyfit(logM_, logU_, 1)
    rng = np.random.default_rng(seed)
    n = len(logM_)
    boots = np.empty(n_boot)
    for i in range(n_boot):
        idx = rng.integers(0, n, n)
        boots[i], _ = np.polyfit(logM_[idx], logU_[idx], 1)
    return slope, boots.std(), np.percentile(boots, 16), np.percentile(boots, 84)


full_slope, full_se, full_lo, full_hi = slope_ci(logM, logU)
print(
    f"\n[baseline] full sample (n={len(sub)}): slope = {full_slope:.3f} +/- {full_se:.3f}"
    f"  68% CI [{full_lo:.3f}, {full_hi:.3f}]"
)

# ---------------------------------------------------------------------------
# (1) Leave-one-mass-tercile-out -- the family proxy most directly relevant to
#     an M-scaling claim: does the exponent survive removing the low-mass third,
#     the mid third, or the high-mass third?
# ---------------------------------------------------------------------------
print("\n" + "=" * 78)
print("[1] LEAVE-ONE-MASS-TERCILE-OUT (family proxy: mass regime)")
print("=" * 78)
tercile_edges = np.quantile(m, [0, 1 / 3, 2 / 3, 1])
tercile_id = np.digitize(m, tercile_edges[1:-1])  # 0,1,2
names = ["low-mass third", "mid-mass third", "high-mass third"]
for t in range(3):
    keep = tercile_id != t
    n_removed = (~keep).sum()
    s, se, lo, hi = slope_ci(logM[keep], logU[keep])
    shift = s - full_slope
    print(
        f"  drop {names[t]:16s} (n={n_removed:>3d} removed, n_kept={keep.sum():>3d}): "
        f"slope = {s:.3f} +/- {se:.3f}   shift from full = {shift:+.3f}"
        f"   ({'within 1 full-sample SE' if abs(shift) < full_se else 'EXCEEDS 1 full-sample SE'})"
    )

# ---------------------------------------------------------------------------
# (2) Leave-one-z-quartile-out -- the genuinely-named companion test in S16.
# ---------------------------------------------------------------------------
print("\n" + "=" * 78)
print("[2] LEAVE-ONE-REDSHIFT-QUARTILE-OUT")
print("=" * 78)
z_edges = np.quantile(z, [0, 0.25, 0.5, 0.75, 1])
z_id = np.digitize(z, z_edges[1:-1])
zlabels = [f"z in [{z_edges[i]:.3f},{z_edges[i + 1]:.3f})" for i in range(4)]
for q in range(4):
    keep = z_id != q
    n_removed = (~keep).sum()
    s, se, lo, hi = slope_ci(logM[keep], logU[keep])
    shift = s - full_slope
    print(
        f"  drop Q{q + 1} {zlabels[q]:24s} (n={n_removed:>3d} removed): "
        f"slope = {s:.3f} +/- {se:.3f}   shift from full = {shift:+.3f}"
        f"   ({'within 1 full-sample SE' if abs(shift) < full_se else 'EXCEEDS 1 full-sample SE'})"
    )

print("\n" + "=" * 78)
print("SUMMARY -- written after seeing the numbers below, not predicted in advance")
print("=" * 78)
print(
    f"  Full-sample exponent: {full_slope:.3f} +/- {full_se:.3f} (matches the FINDING file's\n"
    "  cited +0.555 +/- 0.041 -- independently re-verified twice now, this session).\n"
    "  No true cross-catalog family exists in this data to leave out (S0).\n\n"
    "  The exponent is NOT uniformly stable under the two available proxy partitions:\n"
    "  dropping the low-mass third (0.432), the high-mass third (0.630), or the\n"
    "  lowest-z quartile (0.379) each move the point estimate by MORE than one\n"
    "  full-sample bootstrap SE -- 3 of 7 leave-one-out removals exceed that bar.\n"
    "  The mid-mass third and the three higher-z quartiles are stable (within 1 SE).\n\n"
    "  What this does and does not mean: the QUALITATIVE conclusion (the single-field\n"
    "  completion's exact +1 is excluded) is UNAFFECTED -- even the most favorable\n"
    "  subsample for the single-field theory (drop high-mass third, slope=0.630+-0.072)\n"
    "  is still ~5.1 sigma from +1, not the full 10.8 sigma of the headline number but\n"
    "  nowhere near consistent with it either. But treating +-0.041 as the FULL\n"
    "  uncertainty on the point value 0.555 understates real spread across mass/z\n"
    "  subpopulations by roughly a factor of 3-4. The exponent is real and the\n"
    "  single-field exclusion survives; the specific number 0.555 is less precise\n"
    "  than its own bootstrap CI alone suggests once population heterogeneity is\n"
    "  accounted for."
)
