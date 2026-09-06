"""E17 ADDENDUM 3 -- close the two caveats `FINDING_E17_ADDENDUM2` left
explicitly open: (a) a sigma(log10 c) sensitivity sweep (Duffy+2008's own
0.15 scatter WIDTH was kept even after its MEDIAN was replaced by
Correa Paper III's cluster-valid relation -- is the divergence headline
robust to that width choice?), and (b) decomposing the exclusion-fraction
change (5.65%->1.02%) from the pure median-swap effect (does differential
truncation of unphysical z_-2<0 draws drive part of the reported shift?).

(a) A real, better-sourced cluster-scale sigma(log10 c) was searched for
(Dutton & Maccio 2014, arXiv:1402.7073, Planck-cosmology NFW/Einasto fits
spanning dwarf galaxies to clusters) -- their own abstract quotes only a
0.2 dex scatter in the Einasto SHAPE parameter, a different quantity, not
a directly usable sigma(log10 c) for NFW concentration. SOURCE_NOT_FOUND
for a superior real replacement value, so this stays a parametric
sensitivity sweep (bracketing Duffy's own 0.15), not a "correct value"
swap.

(b) SELF-CORRECTED while running this file (documented, not silent): the
original design compared "exclude" (drop z_-2<0 draws) against "clip"
(floor z_-2 at the physical boundary 0, keep the draw). This is NOT
numerically viable -- Correa's own alpha formula has a genuine
mathematical singularity as z_-2 -> 0+ (`alpha_beta`'s own
`np.log(1.0 + z_m2)` denominator vanishes, and even clipping to a tiny
positive epsilon leaves alpha finite-but-huge, which overflows in
`mass_history_ratio`'s own `(1+z)**alpha` -- confirmed by rerunning with
both an exact-0 clip [NaN via 0/0] and a 1e-6 clip [NaN via overflow]).
The boundary is not a numerically tractable place to "keep" a draw --
this is a real feature of the source MAH-model parametrization, not a
bug to route around.

Replaced with a numerically sound alternative that answers the same
underlying question: `formation_redshift(c)` is MONOTONIC in c (verified
below, PC3) -- so "exclude z_-2<0" is mechanically equivalent to
"exclude the lowest-c percentile" at each source's own NATURAL rate
(5.60% for Duffy, 1.02% for Correa-III at M0, sigma=0.15). This lets the
two sources be re-compared at a MATCHED exclusion percentile (each run
at the OTHER source's natural rate), isolating whether the reported
divergence shrinkage depends on the DIFFERENTIAL truncation rate itself,
separate from the median-relation choice.

See CLAIM_E17_mass_scatter_for_F0_Faccretion.md, "CLAIM ADDENDUM 3" --
MCID pre-registered before this file was run (part (b)'s MCID restated
below to match the corrected method -- the ORIGINAL exclude-vs-clip MCID
wording is superseded by this in-file correction, not silently dropped).

[Added after Step 8a skeptic WEAKENED-then-fixed, 4 real points, none
dismissed]
1. The sigma sweep's own bottom endpoint (0.05, a factor of 3 below
   Duffy's own 0.15) is not a physically defensible population scatter,
   and the printed "63.0% max shift" headline leaned on it. FIXED: the
   MCID (>20%) already fires at BOTH sigma=0.10 (29.8%) and sigma=0.20
   (21.4%) -- a symmetric +/-0.05 dex bracket around Duffy's own value --
   so the MATERIAL verdict does not depend on the extreme endpoint. The
   printed output below now reports the defensible +/-0.05 dex shifts as
   the primary evidence, with the full-range max kept as a secondary,
   explicitly-labelled number.
2. Part (b)'s "forced to the other source's rate" framing was inaccurate:
   percentile-truncating one source at the OTHER source's natural rate
   does not equalise the two sources' EFFECTIVE exclusion (verified by
   hand: forcing Correa-III to Duffy's 5.60% percentile removes its own
   1.02% physical tail PLUS ~4.58 percentage points of otherwise-valid
   draws; forcing Duffy to Correa-III's 1.02% percentile leaves ~4.63
   percentage points still caught by the physical z_-2<0 cut afterward).
   Neither forced row actually equalises both sides' effective truncation
   -- in each row, one side stays close to its own natural rate. RELABELED
   below to describe what is actually varied (how aggressively the
   lower-c tail is percentile-cut), not "matched exclusion rate". The
   underlying conclusion (divergence is insensitive to this) still holds
   -- it answers the original caveat by a different, still-valid route
   (insensitivity to lower-tail truncation aggressiveness generally, not
   literally "same rate on both sides").
3. No seed-variance check existed for part (b)'s tiny (0.0%/0.1%)
   reported shifts -- indistinguishable from Monte Carlo noise without
   one. FIXED: reruns across 5 independent seeds, reporting the
   min/median/max shift.
4. Only z=2.33 was checked, not z=2.00 (Addendum 2's own MCID checked
   both). FIXED: z=2.00 added to part (a)'s sweep table.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

from __future__ import annotations

import numpy as np
from E17_addendum2_cluster_calibrated_concentration import (
    draw_c_cluster_calibrated,
)
from E17_mass_scatter_for_F0_Faccretion import (
    N_MC,
    SIGMA_LOG10_C200_DUFFY08,
    formation_redshift,
    mass_history_ratio,
)
from E17_mass_scatter_for_F0_Faccretion import draw_c as draw_c_duffy
from P176_v82_real_chi2_hessian_degeneracy import M0_kg
from P176_v82_real_chi2_hessian_degeneracy import M_of as v82_M_ref

FOCUS_Z = 2.33  # the headline point in both prior findings
SECOND_Z = 2.00  # Addendum 2's own OTHER MCID point -- added per Step 8a skeptic point 4
FOCUS_POWER = 2.0  # F0's own power
SIGMA_SWEEP = (0.05, 0.10, 0.15, 0.20, 0.25, 0.30)
SEEDS_FOR_VARIANCE_CHECK = (20260906, 1, 2, 3, 4)  # Step 8a skeptic point 3


def divergence(offset_z, jensen_z):
    """1/(offset*jensen) -- same construction Addendum 2 used for its own
    headline number, per the skeptic-corrected formula (not offset alone)."""
    return (offset_z * jensen_z) ** -1


def _decompose(c_draws, zs, powers):
    """Core: exclude unphysical z_-2<0 draws (the ONLY treatment used
    anywhere in this file, per the self-correction above), then compute
    offset/jensen/combined exactly as E17's and Addendum 2's own
    decompose_* functions do."""
    zm2_draws = formation_redshift(c_draws)
    valid = zm2_draws >= 0.0
    excluded_frac = 1.0 - float(np.mean(valid))
    c_draws, zm2_draws = c_draws[valid], zm2_draws[valid]
    offset, jensen, combined = {}, {p: {} for p in powers}, {p: {} for p in powers}
    for z in zs:
        m_ratio = mass_history_ratio(c_draws, zm2_draws, z)
        ref_ratio = float(v82_M_ref(z) / M0_kg)
        mean_m = float(np.mean(m_ratio))
        offset[z] = mean_m / ref_ratio
        for p in powers:
            e_mp = float(np.mean(m_ratio**p))
            jensen[p][z] = e_mp / mean_m**p
            combined[p][z] = e_mp / ref_ratio**p
    return offset, jensen, combined, excluded_frac


def _decompose_percentile_matched(c_draws, target_excl_frac, zs, powers):
    """Part (b), corrected method: instead of the physical z_-2<0 cut,
    drop the lowest `target_excl_frac` of draws BY c-PERCENTILE. Because
    z_-2(c) is monotonic (PC3), this reduces to the natural cut exactly
    when target_excl_frac equals a source's own natural rate (verified by
    PC2's continuity below), and lets a DIFFERENT source be evaluated at
    a rate it would not naturally produce -- e.g. Duffy forced to
    Correa-III's 1.02%, or Correa-III forced to Duffy's 5.60%."""
    if target_excl_frac > 0:
        cutoff = np.quantile(c_draws, target_excl_frac)
        c_draws = c_draws[c_draws > cutoff]
    return _decompose(c_draws, zs, powers)


def sigma_sweep(sigma_values=SIGMA_SWEEP, zs=(FOCUS_Z, SECOND_Z), n=N_MC, seed=20260906):
    """Part (a). Cluster-calibrated (Correa Paper III) median, current
    concentration source of record after Addendum 2, sigma varied.
    Tracks BOTH z=2.33 and z=2.00 (Step 8a skeptic point 4)."""
    results = {}
    for sigma in sigma_values:
        rng = np.random.default_rng(seed)
        c_draws, c_med = draw_c_cluster_calibrated(sigma, n, rng)
        offset, jensen, _combined, excl = _decompose(c_draws, zs, (FOCUS_POWER,))
        results[sigma] = (offset, jensen, excl, c_med)
    return results


def exclusion_rate_matched_comparison(
    sigma_log10_c=SIGMA_LOG10_C200_DUFFY08, n=N_MC, seed=20260906
):
    """Part (b), corrected method. For each source: (i) its own NATURAL
    exclusion result (the z_-2<0 cut, matches Addendum 2's own numbers
    exactly, PC2), and (ii) the result forced to the OTHER source's
    natural exclusion rate via percentile truncation. Both treatments run
    on the SAME random c draws per source -- only the truncation rate
    differs, not the sample."""
    out = {}
    natural_excl = {}
    c_draws_by_source = {}
    for label, draw_fn in (("duffy", draw_c_duffy), ("correa3", draw_c_cluster_calibrated)):
        rng = np.random.default_rng(seed)
        c_draws, c_med = draw_fn(sigma_log10_c, n, rng)
        c_draws_by_source[label] = c_draws
        natural = _decompose(c_draws.copy(), (FOCUS_Z,), (FOCUS_POWER,))
        natural_excl[label] = natural[3]
        out[label] = {"c_med": c_med, "natural": natural}
    other = {"duffy": "correa3", "correa3": "duffy"}
    for label in ("duffy", "correa3"):
        forced_rate = natural_excl[other[label]]
        out[label]["forced"] = _decompose_percentile_matched(
            c_draws_by_source[label].copy(), forced_rate, (FOCUS_Z,), (FOCUS_POWER,)
        )
        out[label]["forced_rate"] = forced_rate
    return out


def test_positive_control_percentile_matches_natural_cut():
    """PC3: the DEFINING check for the corrected method. Truncating at a
    source's own natural exclusion fraction via PERCENTILE must reproduce
    the same offset/jensen as the direct z_-2<0 physical cut -- confirms
    z_-2(c) is monotonic in c (so percentile truncation and physical
    truncation select the SAME draws) and that _decompose_percentile_
    matched is not a different, silently-diverging computation."""
    rng = np.random.default_rng(20260906)
    c_draws, _ = draw_c_cluster_calibrated(SIGMA_LOG10_C200_DUFFY08, N_MC, rng)
    natural = _decompose(c_draws.copy(), (FOCUS_Z,), (FOCUS_POWER,))
    matched = _decompose_percentile_matched(c_draws.copy(), natural[3], (FOCUS_Z,), (FOCUS_POWER,))
    assert abs(natural[0][FOCUS_Z] - matched[0][FOCUS_Z]) / natural[0][FOCUS_Z] < 0.01
    assert (
        abs(natural[1][FOCUS_POWER][FOCUS_Z] - matched[1][FOCUS_POWER][FOCUS_Z])
        / natural[1][FOCUS_POWER][FOCUS_Z]
        < 0.01
    )


def test_positive_control_sweep_reproduces_addendum2_at_sigma_015():
    """The sigma=0.15 sweep point must reproduce Addendum 2's own reported
    c_med (4.711) and excluded fraction (1.02%) for the Correa-III source
    -- confirms this file's refactored core matches the original, not a
    silent re-derivation."""
    results = sigma_sweep((0.15,), n=N_MC, seed=20260906)
    _offset, _jensen, excl, c_med = results[0.15]
    assert abs(c_med - 4.711) < 0.001, c_med
    assert abs(excl - 0.0102) < 0.002, excl


def exclusion_rate_matched_comparison_seed_variance(seeds=SEEDS_FOR_VARIANCE_CHECK, n=N_MC):
    """Step 8a skeptic point 3: rerun the part-(b) comparison across
    several independent seeds so the reported 0.0%/0.1% shifts can be
    checked against Monte Carlo noise, not just a single realisation."""
    shifts_correa_rate = []
    shifts_duffy_rate = []
    for seed in seeds:
        cmp = exclusion_rate_matched_comparison(seed=seed)
        div_dn = divergence(
            cmp["duffy"]["natural"][0][FOCUS_Z], cmp["duffy"]["natural"][1][FOCUS_POWER][FOCUS_Z]
        )
        div_cn = divergence(
            cmp["correa3"]["natural"][0][FOCUS_Z],
            cmp["correa3"]["natural"][1][FOCUS_POWER][FOCUS_Z],
        )
        div_df = divergence(
            cmp["duffy"]["forced"][0][FOCUS_Z], cmp["duffy"]["forced"][1][FOCUS_POWER][FOCUS_Z]
        )
        div_cf = divergence(
            cmp["correa3"]["forced"][0][FOCUS_Z], cmp["correa3"]["forced"][1][FOCUS_POWER][FOCUS_Z]
        )
        shift_natural = div_dn / div_cn
        shifts_correa_rate.append(abs((div_df / div_cn) / shift_natural - 1.0))
        shifts_duffy_rate.append(abs((div_dn / div_cf) / shift_natural - 1.0))
    return shifts_correa_rate, shifts_duffy_rate


if __name__ == "__main__":
    test_positive_control_sweep_reproduces_addendum2_at_sigma_015()
    print("PC1 sigma=0.15 sweep point reproduces Addendum 2's own c_med=4.711, excl=1.02%: PASS")

    test_positive_control_percentile_matches_natural_cut()
    print("PC2 percentile truncation at a source's own natural rate matches its physical")
    print(
        "    z_-2<0 cut to <1% (confirms z_-2(c) monotonicity, the corrected method's basis): PASS\n"
    )

    print("=" * 100)
    print("PART (a) -- sigma(log10 c) sensitivity sweep, Correa-III median, z=2.33 AND z=2.00")
    print("SOURCE_NOT_FOUND for a superior real sigma(log10 c) value (Dutton & Maccio 2014's own")
    print("abstract quotes only a 0.2 dex EINASTO SHAPE scatter, a different quantity) -- this is")
    print("a parametric sweep, not a literature-sourced replacement.")
    print("=" * 100)
    sweep = sigma_sweep()
    base_div_233 = divergence(sweep[0.15][0][FOCUS_Z], sweep[0.15][1][FOCUS_POWER][FOCUS_Z])
    base_div_200 = divergence(sweep[0.15][0][SECOND_Z], sweep[0.15][1][FOCUS_POWER][SECOND_Z])
    print(
        f"{'sigma':>7} {'div(z=2.33)':>12} {'shift@2.33':>11} {'div(z=2.00)':>12} {'shift@2.00':>11}"
    )
    max_shift_233, max_shift_200 = 0.0, 0.0
    bracket_shift_233, bracket_shift_200 = 0.0, 0.0  # +/-0.05 dex around Duffy's 0.15 only
    for sigma in SIGMA_SWEEP:
        off, jen, _excl, _c = sweep[sigma]
        div_233 = divergence(off[FOCUS_Z], jen[FOCUS_POWER][FOCUS_Z])
        div_200 = divergence(off[SECOND_Z], jen[FOCUS_POWER][SECOND_Z])
        shift_233 = abs(div_233 / base_div_233 - 1.0)
        shift_200 = abs(div_200 / base_div_200 - 1.0)
        max_shift_233 = max(max_shift_233, shift_233)
        max_shift_200 = max(max_shift_200, shift_200)
        if sigma in (0.10, 0.20):
            bracket_shift_233 = max(bracket_shift_233, shift_233)
            bracket_shift_200 = max(bracket_shift_200, shift_200)
        print(
            f"{sigma:7.2f} {div_233:12.3f} {100 * shift_233:10.1f}% {div_200:12.3f} {100 * shift_200:10.1f}%"
        )
    print(
        "\n  [Step 8a skeptic point 1, fixed] Defensible +/-0.05 dex bracket (sigma in {0.10,0.20}) "
        "around Duffy's 0.15:"
    )
    print(f"    z=2.33: {100 * bracket_shift_233:.1f}%   z=2.00: {100 * bracket_shift_200:.1f}%")
    print("  Full-range max (sigma 0.05-0.30, secondary/ancillary number, not the headline):")
    print(f"    z=2.33: {100 * max_shift_233:.1f}%   z=2.00: {100 * max_shift_200:.1f}%")
    a_material = bracket_shift_233 > 0.20 or bracket_shift_200 > 0.20
    print(
        f"\n  MCID (>20%, evaluated on the DEFENSIBLE bracket, not the extreme endpoint): "
        f"{'MATERIAL' if a_material else 'not material -- (a) resolved'}"
    )

    print("\n" + "=" * 100)
    print("PART (b), CORRECTED METHOD -- lower-c-tail percentile-cut sensitivity (RELABELED per")
    print(
        "Step 8a skeptic point 2: 'forced to the other source's rate' overclaimed what percentile"
    )
    print("truncation at a different rate actually equalises -- see module docstring)")
    print("=" * 100)
    cmp = exclusion_rate_matched_comparison()
    div_natural = {}
    div_forced = {}
    for label in ("duffy", "correa3"):
        d = cmp[label]
        off_n, jen_n, _c_n, excl_n = d["natural"]
        off_f, jen_f, _c_f, excl_f = d["forced"]
        div_n = divergence(off_n[FOCUS_Z], jen_n[FOCUS_POWER][FOCUS_Z])
        div_f = divergence(off_f[FOCUS_Z], jen_f[FOCUS_POWER][FOCUS_Z])
        div_natural[label] = div_n
        div_forced[label] = div_f
        print(
            f"  {label:8s} c_med={d['c_med']:.3f}  natural cut (physical excl={100 * excl_n:.2f}%): div={div_n:.3f}"
            f"   percentile-cut at {100 * d['forced_rate']:.2f}% (residual physical excl={100 * excl_f:.2f}%): div={div_f:.3f}"
        )
    shift_natural = div_natural["duffy"] / div_natural["correa3"]
    shift_matched_at_correa_rate = div_forced["duffy"] / div_natural["correa3"]
    shift_matched_at_duffy_rate = div_natural["duffy"] / div_forced["correa3"]
    b_diff_correa_rate = abs(shift_matched_at_correa_rate / shift_natural - 1.0)
    b_diff_duffy_rate = abs(shift_matched_at_duffy_rate / shift_natural - 1.0)
    max_b_diff = max(b_diff_correa_rate, b_diff_duffy_rate)
    print(
        f"\n  Duffy->Correa-III divergence shrinkage at each source's own natural cut: {shift_natural:.3f}x"
    )
    print(
        f"  shrinkage with Duffy's tail percentile-cut to Correa-III's 1.02% level:  {shift_matched_at_correa_rate:.3f}x  (shift {100 * b_diff_correa_rate:.1f}%)"
    )
    print(
        f"  shrinkage with Correa-III's tail percentile-cut to Duffy's 5.60% level:  {shift_matched_at_duffy_rate:.3f}x  (shift {100 * b_diff_duffy_rate:.1f}%)"
    )
    print(
        "\n  NOTE (Step 8a skeptic point 2): neither percentile-cut row equalises BOTH sides' effective"
    )
    print(
        "  truncation -- in each row one side stays close to its own natural rate. What this DOES show:"
    )
    print(
        "  divergence at z=2.33 is insensitive to how aggressively the lower-c tail is percentile-cut,"
    )
    print(
        "  which still answers the original caveat (not a truncation-RATE artefact), by this route."
    )

    print("\n  [Step 8a skeptic point 3, fixed] Seed-variance check (5 independent seeds):")
    shifts_cr, shifts_dr = exclusion_rate_matched_comparison_seed_variance()
    print(
        f"    percentile-cut-to-Correa-rate shift: min={100 * min(shifts_cr):.2f}%  "
        f"median={100 * float(np.median(shifts_cr)):.2f}%  max={100 * max(shifts_cr):.2f}%"
    )
    print(
        f"    percentile-cut-to-Duffy-rate shift:  min={100 * min(shifts_dr):.2f}%  "
        f"median={100 * float(np.median(shifts_dr)):.2f}%  max={100 * max(shifts_dr):.2f}%"
    )
    max_seed_shift = max(max(shifts_cr), max(shifts_dr))
    print(
        f"\n  MCID (>20% change, checked against seed-to-seed noise above): "
        f"{'MATERIAL -- truncation aggressiveness IS a real confound' if max_b_diff > 0.20 else 'not material -- (b) resolved'}"
        f" (seed noise ceiling: {100 * max_seed_shift:.2f}%)"
    )
