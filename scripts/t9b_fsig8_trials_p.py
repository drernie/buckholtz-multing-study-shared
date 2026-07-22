"""T9b — a real trials-corrected p for R004 (fsigma8 bell-shape correlation).

R004 (facts.json): r(eps(z), f*sigma8(z)) = 0.851, raw two-tailed p = 0.0018,
n = 10 points. T9 flagged that this p carries NO proxy-trials factor: fsigma8
was one of several observables tried against eps(z). This script quantifies the
correction two honest ways.

  ROUTE (a) — PROXY-COUNT (Bonferroni-style).
    Enumerate, from the project's OWN history, the distinct observables/proxies
    that were actually correlated against eps(z). K of them were available to
    report; fsigma8 was the one that hit. p_corr = min(1, K * p_raw). K is
    archaeology, not arithmetic, so a [K_min, K_max] range is given with an
    explicit evidence level.

  ROUTE (b) — PERMUTATION null.
    With n=10, permute the fsigma8 y-values 10,000 times, recompute |r|, and
    count |r_perm| >= 0.851 -> empirical p with its own 1/N_perm resolution floor.
    CAVEAT (stated, not buried): both curves are SMOOTH in z. A plain permutation
    destroys that smoothness, so the permuted nulls are LESS structured than a
    realistic null -> the empirical p is OPTIMISTIC (significance INFLATED). An
    AR(1)/phase-randomised surrogate that preserves autocorrelation is the honest
    upper bound on p; a block/circular-shift null is added as a cheap partial fix.

We consume R004's stored r/p/n as inputs; we do not re-derive the correlation.
Route (b) necessarily recomputes r on permuted data — that is the null, not R004.

Run:  python scripts/t9b_fsig8_trials_p.py
Reproducible (seeded). Prints only. NOT_VALIDATION.
"""

from __future__ import annotations

import numpy as np

# ── R004 stored result (facts.json; consumed, not recomputed) ──
R_OBS = 0.851
P_RAW = 0.0018
N_PTS = 10

# ── Table A1 arrays (identical to scripts/fsig8_robustness.py) ──
Z_A1 = np.array([0.06, 0.14, 0.25, 0.40, 0.65, 1.00, 1.50, 2.10, 3.20, 5.00, 8.50])
EPS_A1 = np.array([0.063, 0.125, 0.215, 0.228, 0.213, 0.186, 0.214, 0.171, 0.106, 0.048, 0.101])
MASK10 = Z_A1 <= 5.01
Z_10 = Z_A1[MASK10]
EPS_10 = EPS_A1[MASK10]


def pearson_r(x, y):
    xm, ym = x - x.mean(), y - y.mean()
    denom = np.sqrt((xm**2).sum() * (ym**2).sum())
    return float((xm * ym).sum() / denom) if denom > 1e-30 else 0.0


def fsig8_model(z_arr, Om=0.30, sig8=0.81):
    """LambdaCDM f*sigma8(z) (Carroll-Press-Turner growth) — same as fsig8_robustness.py."""
    a = 1.0 / (1 + z_arr)
    D = a * (Om / (Om + (1 - Om) * a**3)) ** 0.55
    D0 = 1.0 * (Om / (Om + (1 - Om))) ** 0.55
    D_norm = D / D0
    H2 = Om * (1 + z_arr) ** 3 + (1 - Om)
    Om_z = Om * (1 + z_arr) ** 3 / H2
    f = Om_z**0.55
    return f * sig8 * D_norm


# ═══════════════════════════════════════════════════════════════════════════
# ROUTE (a) — proxy-count Bonferroni
# ═══════════════════════════════════════════════════════════════════════════
def route_a() -> None:
    print("=" * 70)
    print("ROUTE (a) — PROXY-COUNT correction (Bonferroni-style)")
    print("=" * 70)
    # Distinct observables/proxies actually correlated against eps(z) in this
    # repo (archaeology from scripts/; each is a 'which curve to report' choice).
    # Evidence level per entry: [CODE] = a pearson_r(., eps) call exists on disk.
    proxies = [
        (
            "f*sigma8(z) growth  [R004, THE reported hit]",
            "fsig8_robustness.py / test_rP_merger TEST6",
            "CODE",
        ),
        (
            "Virial k_A ~ H(z)^(4/3) (monotone baseline)",
            "loo_epsilon_analysis Proxy0 / test_rP TEST1",
            "CODE",
        ),
        ("dN/dz cluster survey rate (M8-C, r=0.723)", "loo_epsilon_analysis Proxy2", "CODE"),
        ("cluster merger-epoch r_P hypothesis", "test_rP_merger_hypothesis TEST4", "CODE"),
        ("D(z) mass-scaling (D^4 family)", "test_rP_merger_hypothesis TEST3", "CODE"),
        ("D(z) x H(z)^(1/3) parametric peak family", "test_rP_merger_hypothesis TEST5", "CODE"),
    ]
    # Broader pool: fitted/derived forms + cluster-audit sub-candidates that also
    # got an r-vs-eps evaluation (arguably not independent 'observable choices',
    # so they inflate K_max, not K_min).
    extra = [
        ("Gaussian bell fit (z_peak=0.40 hypothesis)", "loo Proxy1", "CODE"),
        ("LogNormal parametric fit", "loo Proxy3", "CODE"),
        ("hdmavp1 cluster candidate A (richness-like)", "hdmavp1 r_a", "CODE"),
        ("hdmavp1 cluster candidate B", "hdmavp1 r_b", "CODE"),
        ("hdmavp1 cluster candidate C", "hdmavp1 r_c", "CODE"),
        ("hdmavp1 cluster candidate D (LambdaCDM transition)", "hdmavp1 r_d", "CODE"),
        ("hdmavp1 selection-function f_sel", "hdmavp1 r_fsel", "CODE"),
    ]

    print("\n  Distinct EXTERNAL observables (K_min pool — genuine 'which physical")
    print("  curve do we report' choices):")
    for name, src, ev in proxies:
        print(f"    - {name:<48} [{ev}] {src}")
    k_min = len(proxies)

    print("\n  + fitted forms & cluster-audit sub-candidates (K_max pool — these are")
    print("    variants/fits, weaker claim to being independent observable choices):")
    for name, src, ev in extra:
        print(f"    - {name:<48} [{ev}] {src}")
    k_max = len(proxies) + len(extra)

    print(f"\n  K_min = {k_min}   K_max = {k_max}   [evidence: WEAK — archaeology of")
    print("  the repo's own scripts; the true intended 'trials' set is not logged]")
    p_min = min(1.0, k_min * P_RAW)  # conservative-favorable (fewest trials)
    p_max = min(1.0, k_max * P_RAW)  # least-favorable (most trials)
    print(f"\n  p_raw                     = {P_RAW:.4f}")
    print(f"  p_corr (K_min={k_min:>2})          = {k_min} x {P_RAW} = {p_min:.4f}")
    print(f"  p_corr (K_max={k_max:>2})          = {k_max} x {P_RAW} = {p_max:.4f}")
    print(f"\n  => trials-corrected p in [{p_min:.4f}, {p_max:.4f}]")
    verdict = (
        "SURVIVES 0.05 across the whole K range"
        if p_max < 0.05
        else "MARGINAL — survives at K_min, wash-out risk at K_max"
        if p_min < 0.05 <= p_max
        else "WASHED OUT at 0.05"
    )
    print(f"  => at alpha=0.05: {verdict}")
    print()
    return p_min, p_max


# ═══════════════════════════════════════════════════════════════════════════
# ROUTE (b) — permutation / surrogate nulls
# ═══════════════════════════════════════════════════════════════════════════
def route_b() -> None:
    print("=" * 70)
    print("ROUTE (b) — PERMUTATION & surrogate nulls (n=10)")
    print("=" * 70)
    rng = np.random.default_rng(20260722)
    fsig = fsig8_model(Z_10)
    r_check = abs(pearson_r(fsig, EPS_10))
    print(f"\n  |r| on the actual model vs eps (10 pts) = {r_check:.3f}  (R004 stored 0.851)")
    n_perm = 10_000

    # (b1) plain permutation of fsigma8 y-values
    cnt_perm = 0
    for _ in range(n_perm):
        perm = rng.permutation(fsig)
        if abs(pearson_r(perm, EPS_10)) >= R_OBS:
            cnt_perm += 1
    p_perm = cnt_perm / n_perm

    # (b2) circular-shift null (preserves the ordered SHAPE/autocorrelation of
    #      fsigma8, only offsets its phase vs eps) — a cheap partial fix that
    #      does NOT destroy smoothness the way (b1) does.
    cnt_shift = 0
    n_shift = len(fsig)
    shifts = 0
    for k in range(1, n_shift):  # exclude 0-shift (identity)
        rolled = np.roll(fsig, k)
        shifts += 1
        if abs(pearson_r(rolled, EPS_10)) >= R_OBS:
            cnt_shift += 1
    p_shift = cnt_shift / shifts

    # (b3) AR(1)-surrogate null: fit lag-1 autocorr of fsigma8, generate AR(1)
    #      surrogates with matched rho+variance, correlate vs eps. Preserves
    #      smoothness -> honest (higher) p. Chance |r|>=0.851 becomes RARE.
    dev = fsig - fsig.mean()
    rho = float(np.corrcoef(dev[:-1], dev[1:])[0, 1])
    rho = max(min(rho, 0.99), -0.99)
    sd = dev.std()
    cnt_ar = 0
    for _ in range(n_perm):
        s = np.empty(n_shift)
        s[0] = rng.normal(0, sd)
        for i in range(1, n_shift):
            s[i] = rho * s[i - 1] + rng.normal(0, sd * np.sqrt(1 - rho**2))
        if abs(pearson_r(s, EPS_10)) >= R_OBS:
            cnt_ar += 1
    p_ar = cnt_ar / n_perm

    print(
        f"\n  (b1) plain permutation   : p = {cnt_perm}/{n_perm} = {p_perm:.4f}"
        f"  (floor 1/{n_perm}={1 / n_perm:.0e})"
    )
    print("       [OPTIMISTIC: destroys smoothness of both curves -> inflates signif.]")
    print(
        f"  (b2) circular-shift null : p = {cnt_shift}/{shifts} = {p_shift:.4f}"
        f"  (only {shifts} distinct shifts -> coarse)"
    )
    print(f"       [preserves fsig8 shape; rho_lag1(fsig8) = {rho:.3f}]")
    print(
        f"  (b3) AR(1) surrogate     : p = {cnt_ar}/{n_perm} = {p_ar:.4f}"
        "   [HONEST: keeps smoothness]"
    )
    print("       [this is the realistic upper bound on p for a smooth-null world]")
    print()
    return p_perm, p_shift, p_ar


def main() -> None:
    print("T9b — trials-corrected p for R004 (r=0.851, p_raw=0.0018, n=10)\n")
    p_min, p_max = route_a()
    p_perm, p_shift, p_ar = route_b()
    print("=" * 70)
    print("SYNTHESIS")
    print("=" * 70)
    print(f"  proxy-count Bonferroni : p in [{p_min:.4f}, {p_max:.4f}]  (K=6..13, [WEAK])")
    print(f"  permutation (optimistic): p = {p_perm:.4f}")
    print(f"  AR(1) surrogate (honest): p = {p_ar:.4f}")
    print("\n  Least-favorable DEFENSIBLE number is the driver: whichever of the")
    print("  proxy-count upper edge or the smooth-null p is larger governs the verdict.")
    print("  Report that one, not the permutation floor.")


if __name__ == "__main__":
    main()
