"""
Is GroupNsubs (substructure count) a useful, INDEPENDENT dynamical-state
proxy, or is it just collinear with mass -- in which case it adds no
real confound-control information for H1b's own design?

Standard approach: more massive halos trivially host more substructure
just from cosmological abundance (bigger halo = more infalling subhalos
of any given mass, dynamical state aside). The relevant quantity for
confound control is the RESIDUAL of nsubs after removing the mass
trend -- clusters with MORE substructure than their mass alone predicts
are plausible unrelaxed/merging systems; clusters with FEWER are
plausible relaxed systems.
"""

import csv
import math
import statistics as st
import sys

path = sys.argv[1]
rows = list(csv.DictReader(open(path)))

m200 = [float(r["m200_msun"]) for r in rows]
nsubs = [int(r["group_nsubs"]) for r in rows]
whim = [float(r["whim_mass_fraction_pct"]) for r in rows]
log_m = [math.log10(m) for m in m200]
log_nsubs = [math.log10(n) for n in nsubs]

n = len(rows)


def pearson(x, y):
    mx, my = st.mean(x), st.mean(y)
    cov = sum((x[i] - mx) * (y[i] - my) for i in range(n)) / n
    return cov / (st.stdev(x) * st.stdev(y))


def t_and_p_label(r, n):
    df = n - 2
    t = r * math.sqrt(df) / math.sqrt(1 - r**2)
    # rough p-value label via t thresholds for df~69 (two-tailed)
    at = abs(t)
    if at > 3.46:
        p = "<0.001"
    elif at > 2.65:
        p = "<0.01"
    elif at > 1.99:
        p = "<0.05"
    else:
        p = "n.s."
    return t, p


print(f"N = {n}\n")

print("=== Step 1: is nsubs collinear with mass? ===")
r_m_nsubs = pearson(log_m, log_nsubs)
t, p = t_and_p_label(r_m_nsubs, n)
print(f"Pearson r(log M200, log Nsubs) = {r_m_nsubs:.3f}  (t={t:.2f}, p{p})")
print("(expected: strongly positive -- bigger halos trivially host more substructure)\n")

print("=== Step 2: de-trend nsubs (linear fit in log-log space) ===")
# simple OLS: log_nsubs = a + b*log_m
mean_lm, mean_ln = st.mean(log_m), st.mean(log_nsubs)
b = sum((log_m[i] - mean_lm) * (log_nsubs[i] - mean_ln) for i in range(n)) / sum(
    (log_m[i] - mean_lm) ** 2 for i in range(n)
)
a = mean_ln - b * mean_lm
print(f"OLS fit: log10(Nsubs) = {a:.3f} + {b:.3f} * log10(M200)")

residuals = [log_nsubs[i] - (a + b * log_m[i]) for i in range(n)]
print(f"Residual stdev: {st.stdev(residuals):.3f} dex")
print(
    "(residual > 0: MORE substructure than mass alone predicts -- candidate "
    "unrelaxed/merging; residual < 0: fewer -- candidate relaxed)\n"
)

print("=== Step 3: does the mass-independent nsubs residual predict WHIM%? ===")
r_resid_whim = pearson(residuals, whim)
t2, p2 = t_and_p_label(r_resid_whim, n)
print(f"Pearson r(nsubs-residual, WHIM%) = {r_resid_whim:.3f}  (t={t2:.2f}, p{p2})")

print("\n=== Comparison: raw (non-detrended) nsubs vs WHIM% ===")
r_raw_whim = pearson(log_nsubs, whim)
t3, p3 = t_and_p_label(r_raw_whim, n)
print(f"Pearson r(log Nsubs, WHIM%) = {r_raw_whim:.3f}  (t={t3:.2f}, p{p3})")
print("(if this looks similar in size to r(mass,WHIM%)=-0.429, it's likely just")
print(" restating the mass correlation, not new information)")

print("\n=== Verdict ===")
if abs(r_m_nsubs) > 0.5:
    print(f"Nsubs IS substantially collinear with mass (r={r_m_nsubs:.2f}) -- using")
    print("raw Nsubs as a confound-control variable would NOT properly separate")
    print("dynamical state from mass; the de-trended residual (Step 2-3) is the")
    print("statistically correct quantity to use instead.")
if abs(r_resid_whim) < 0.2:
    print(f"\nThe mass-independent residual shows a WEAK relation to WHIM% (r={r_resid_whim:.2f}).")
    print("Nsubs-residual, on this data, is NOT a strong dynamical-state driver of")
    print("WHIM% beyond what mass alone already explains.")
else:
    print(f"\nThe mass-independent residual shows a real relation to WHIM% (r={r_resid_whim:.2f}).")
    print("This IS informative -- substructure count adds real information beyond mass.")
