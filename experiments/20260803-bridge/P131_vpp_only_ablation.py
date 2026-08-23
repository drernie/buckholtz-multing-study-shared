"""P131 -- Vpp-only mechanistic ablation: does dropping kk^2*exp(-2N) from
the PERTURBATION DYNAMICS entirely (while keeping its real, k-dependent
contribution to the N=1 seed via psid0's own constraint) still reproduce
an amplification of order A~6679? A single, tightly-scoped causal
ablation, closed after this file regardless of outcome.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

WHY THIS FILE, user-directed, in detail. FINDING_P130 found the peak-N of
the matter-Lambda resonance is approximately k-independent while its
amplitude is strongly k-dependent (ratio ~4249, same order as
FINDING_P126's A_hat=6679). Term-by-term reconnaissance (this session,
not yet its own FINDING) showed the DOMINANT instantaneous driver of the
resonance is usually Vpp=3*lam*pb^2 (the scalar field's own quartic
self-interaction), NOT kk^2*exp(-2N) -- though kk^2*exp(-2N) is not
uniformly negligible (it exceeds Vpp at some individual N, e.g. N~13). A
first attempt to build a "genuinely independent" prediction via an EXACT
two-stage reformulation (solve pb(N) independently, since it provably
decouples, then solve the linear psi/dph/drA_hat/qm_hat sector driven by
that KNOWN pb(N)) was correctly identified, before building it, as the
SAME circularity the skeptic caught in FINDING_P129: an EXACT
reformulation of the SAME physics reproduces the SAME numbers as a
matter of arithmetic, not a genuinely independent check.

THE FIX, user-specified: stop trying to exactly reproduce the real
system (always tautological). Instead run a genuine ABLATION -- keep the
real background pb(N)/H(N), the real N=1 initial conditions (P105/P119,
INCLUDING their real k-dependence via psid0's own kk^2/a0^2 constraint
term), and the real psi<->dph couplings, but delete ONE specific piece of
physics from the ONGOING dynamics: kk^2*exp(-2N) inside dphdd's own
-(kk^2*exp(-2N)+Vpp)*dph term. This is a genuine intervention, not a
reformulation -- it produces DIFFERENT numbers than the real system,
and whether those different numbers land near 6679 is real information.
(Applied consistently: the OTHER place kk^2 appears in the full system,
drA_hat_d's own kk^2*qm_hat*exp(-2N)/(1-gh*pb) term, is ALSO zeroed for
this ablation -- an honest completion of "drop the k^2/a^2 dynamical
coupling", not a selective, partial cut.)

THREE OUTCOMES, decided in advance, not chosen after seeing results
(user's own framework):
  VPP-DOMINANT-MECHANISM-SUPPORTED: Vpp-only amplitude ratio is the same
    order of magnitude as A_hat=6679 (within a factor of ~3, matching
    FINDING_P130's own precision bar).
  VPP-CORE-K2-CORRECTIONS-LOAD-BEARING: right sign/qualitative shape
    (a real resonance still occurs, k-dependent), but the amplitude is
    substantially smaller than A_hat -- Vpp is a necessary amplifier, but
    the periodic kk^2 episodes materially set the final gain.
  VPP-ONLY-REFUTED: no comparable amplification at all -- the dominant
    INSTANTANEOUS term is not the dominant INTEGRATED mechanism, a real
    and informative negative result in its own right.

MIRROR NEGATIVE CONTROL, user-specified: the reverse ablation (Vpp->0 in
that SAME term, kk^2*exp(-2N) kept) isolates whether kk^2 ALONE, without
Vpp, can drive comparable amplification. If Vpp-only tracks A_hat while
k2-only does not, the mechanistic story is strong; if both fail equally,
neither isolated term explains it and the effect is genuinely coupled/
phase-dependent (the user's own red-team point: an oscillating system's
dominant-magnitude term is not automatically its dominant-INTEGRATED
term -- phase and accumulation matter, which is exactly why this file
runs the actual ablation instead of reasoning from instantaneous
magnitudes alone).

CONTROLS:
  POSITIVE CONTROL: this file's own COPY of FINDING_P119's make_system_lna
    (unmodified, ablation OFF) must reproduce FINDING_P130's own committed
    peak-|psi| values EXACTLY, before trusting either ablated variant --
    confirms the copy/modification introduced no bug.
  REGRESSION: FINDING_P126's own A_hat_mean=6678.998, reused as the
    reference value throughout, not re-measured here.

WHAT THIS FILE DOES NOT DO: derive a closed-form transfer/gain formula
for the Vpp-dominated system, even if VPP-DOMINANT-MECHANISM-SUPPORTED --
per the user's own plan, that is future work, not attempted here. Resolve
ambiguity with further ablations if the result is mixed -- per the user's
own instruction, this line is CLOSED after this file regardless of
outcome, not patched with "10% this, 7% that" after seeing results. Vary
Lambda, G_N, or C_MATTER. Quote any k[h/Mpc]. Touch MULTING itself
(Gate 1).

AMENDMENT -- the first pass's own Vpp-only peak search (window N=9-25)
found its "peak" sitting exactly AT the window's own lower edge (N=9.0)
for both k=0.3 and k=0.5 -- indistinguishable from a genuine interior
peak vs. the search simply not reaching far enough left. Verified
directly, not assumed: widened the search to N=1.5-30 (2851 points) for
BOTH ablated variants. The Vpp-only peak MOVED to a genuine interior
point (N=3.5, not at either new edge) with the SAME amplitude ratio
(1.00, unchanged from the narrower search); the k2-only peak was
UNCHANGED (N=10.71 exactly, already a genuine interior peak in the first
pass). This confirms VPP-ONLY-REFUTED is a robust finding, not a
search-window artifact -- both ablated variants' own tiny amplitude
ratios (~1.0, ~0.9) are stable across window choices.
"""

import importlib.util
import os
import sys

import numpy as np
from scipy.integrate import solve_ivp

HERE = os.path.dirname(os.path.abspath(__file__))


def _load(stem, alias):
    spec = importlib.util.spec_from_file_location(alias, os.path.join(HERE, stem))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[alias] = mod
    spec.loader.exec_module(mod)
    return mod


p130 = _load("P130_matter_lambda_resonance_characterization.py", "p130_for_p131")
p119 = p130.p119
p105 = p130.p128.p127.p126.p125.p120.p119.p105
LAMBDA_FIXED = p130.LAMBDA_FIXED
PHIDOT_INIT = p130.PHIDOT_INIT
G_N = p130.p128.G_N
C_MATTER = p130.C_MATTER
A_HAT_MEAN_REGRESSION = 6678.998  # FINDING_P126's own committed regression anchor

# FINDING_P130's own committed peak values -- the positive-control target.
P130_PEAK_N03 = 13.4550
P130_PEAK_ABS_PSI03 = 2.643627e00
P130_PEAK_N05 = 13.6200
P130_PEAK_ABS_PSI05 = 1.123195e04


def make_system_ablated(gh, lam, kk, lam_cc, drop_k2, drop_vpp):
    """A COPY of FINDING_P119's own make_system_lna, with two independent
    toggles: drop_k2 zeroes BOTH places kk^2*exp(-2N) appears (dphdd's own
    term, and drA_hat_d's own term); drop_vpp zeroes Vpp ONLY inside
    dphdd's own -(kk^2*exp(-2N)+Vpp)*dph term (Vp elsewhere, e.g. in
    dp_phi, in 2*psi*(gh*rho_A-Vp), and in pb's own pdd, is UNTOUCHED --
    this ablation is surgical, not a broader simplification)."""

    def rhs(_t, y):
        lna, pb, pd, psi, psid, dph, dphd, drA_hat, qm_hat = y
        with np.errstate(all="ignore"):
            rho_A = C_MATTER * np.exp(-3.0 * lna)
            rho_phys = rho_A * (1.0 - gh * pb)
            V = lam * pb**4 / 4.0 + lam_cc
            H = np.sqrt(max((8.0 * np.pi * G_N / 3.0) * (rho_phys + pd**2 / 2.0 + V), 0.0))
            Vp = lam * pb**3
            Vpp = 0.0 if drop_vpp else 3.0 * lam * pb**2
            Hdot = -4.0 * np.pi * G_N * (rho_phys + pd**2)

            pdd = gh * rho_A - 3.0 * H * pd - Vp
            dp_phi = pd * dphd - psi * pd**2 - Vp * dph
            psidd = 4 * np.pi * G_N * dp_phi - 4 * H * psid - (2 * Hdot + 3 * H**2) * psi

            drA_for_dphdd = drA_hat * np.exp(-3.0 * lna)
            k2_dphdd = 0.0 if drop_k2 else kk**2 * np.exp(-2.0 * lna)
            dphdd = (
                gh * drA_for_dphdd
                + 2 * psi * (gh * rho_A - Vp)
                + 4 * psid * pd
                - 3 * H * dphd
                - (k2_dphdd + Vpp) * dph
            )

            k2_drA = 0.0 if drop_k2 else kk**2
            drA_hat_d = 3 * psid * C_MATTER + k2_drA * qm_hat * np.exp(-2.0 * lna) / (1 - gh * pb)
            qm_hat_d = C_MATTER * (gh * dph - (1 - gh * pb) * psi)

        return [H, pd, pdd, psid, psidd, dphd, dphdd, drA_hat_d, qm_hat_d]

    return rhs


def initial_data_lna_ablated(gh, lam, kk, lam_cc, **ic):
    """IDENTICAL to FINDING_P119's own initial_data_lna -- the REAL,
    k-dependent seed (via psid0's own kk^2/a0^2 constraint term) is kept
    for every variant tested here; only the ONGOING dynamics is ablated."""
    y0 = p105.initial_data(gh, lam, kk, lam_cc, **ic)
    a0, pb0, pd0, psi0, psid0, dph0, dphd0, drA0, qm0 = y0
    return [np.log(a0), pb0, pd0, psi0, psid0, dph0, dphd0, drA0 * a0**3, qm0 * a0**3]


def run_ablated(gh, lam, kk, t_end, lam_cc, drop_k2, drop_vpp, rtol=1e-10, **ic):
    with np.errstate(all="ignore"):
        sol = solve_ivp(
            make_system_ablated(gh, lam, kk, lam_cc, drop_k2, drop_vpp),
            (1.0, t_end),
            initial_data_lna_ablated(gh, lam, kk, lam_cc, **ic),
            rtol=rtol,
            atol=1e-20,
            dense_output=True,
        )
    return sol if sol.success else None


def find_peak_abs_psi(sol, t_end, n_lo, n_hi, n_points):
    ns = np.linspace(n_lo, n_hi, n_points)
    best_n, best_abs = None, -1.0
    for n in ns:
        t = p119.t_of_lna(sol, float(n), 1.0, t_end)
        if t is None:
            continue
        state = sol.sol(t)
        psi = state[3]
        if abs(psi) > best_abs:
            best_abs, best_n = abs(psi), float(n)
    return best_n, best_abs


def main() -> int:  # noqa: PLR0915 - one linear report
    print("=" * 78)
    print("P131 -- Vpp-only mechanistic ablation (+ k2-only negative control)")
    print("        LAST file in this specific mechanistic-ablation line")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    ic0 = {"phidot0": 0.1 * PHIDOT_INIT}
    t_end = 1e10

    # ==================================================================
    print("\n" + "-" * 78)
    print("POSITIVE CONTROL -- this file's own COPY of make_system_lna,")
    print("ablation OFF, must reproduce FINDING_P130's own committed peaks")
    print("-" * 78)
    s03_off = run_ablated(1.0, 1.0, 0.3, t_end, LAMBDA_FIXED, False, False, **ic0)
    s05_off = run_ablated(1.0, 1.0, 0.5, t_end, LAMBDA_FIXED, False, False, **ic0)
    if s03_off is None or s05_off is None:
        print("  *** STOP -- unablated copy failed to solve.")
        return 1
    n03_off, abs03_off = find_peak_abs_psi(s03_off, t_end, 13.0, 14.5, 301)
    n05_off, abs05_off = find_peak_abs_psi(s05_off, t_end, 13.0, 14.5, 301)
    print(f"    k=0.3 (ablation OFF): peak |psi|={abs03_off:.6e} at N={n03_off:.4f}")
    print(f"    k=0.5 (ablation OFF): peak |psi|={abs05_off:.6e} at N={n05_off:.4f}")
    pc_ok = (
        abs(n03_off - P130_PEAK_N03) < 1e-3
        and abs(n05_off - P130_PEAK_N05) < 1e-3
        and abs(abs03_off / P130_PEAK_ABS_PSI03 - 1.0) < 1e-3
        and abs(abs05_off / P130_PEAK_ABS_PSI05 - 1.0) < 1e-3
    )
    print(f"  POSITIVE CONTROL {'PASSES' if pc_ok else 'FAILS'} (matches FINDING_P130 to 0.1%)")
    if not pc_ok:
        print("  *** STOP -- this file's own copy of the system does not match the")
        print("  *** already-committed real-system result. Do not trust ablations below.")
        return 1

    # ==================================================================
    print("\n" + "-" * 78)
    print("MAIN TEST -- Vpp-only ablation: kk^2*exp(-2N) DROPPED from the")
    print("dynamics (both places it appears), real k-dependent seed KEPT")
    print("-" * 78)
    s03_vpp = run_ablated(1.0, 1.0, 0.3, t_end, LAMBDA_FIXED, True, False, **ic0)
    s05_vpp = run_ablated(1.0, 1.0, 0.5, t_end, LAMBDA_FIXED, True, False, **ic0)
    if s03_vpp is None or s05_vpp is None:
        print("  *** STOP -- Vpp-only ablation failed to solve.")
        return 1
    # WHY a wide 1.5-30 search, not the 9-25 window FINDING_P130 used for the
    # real system: the first pass here found the Vpp-only "peak" sitting
    # exactly AT the search window's own lower edge (N=9.0) -- indistinguishable
    # from a genuine interior peak vs. the search simply not reaching far enough
    # left. Widened before trusting a REFUTED verdict on what could have been a
    # search-boundary artifact, not real physics.
    n03_vpp, abs03_vpp = find_peak_abs_psi(s03_vpp, t_end, 1.5, 30.0, 2851)
    n05_vpp, abs05_vpp = find_peak_abs_psi(s05_vpp, t_end, 1.5, 30.0, 2851)
    print(f"    k=0.3 (Vpp-only): peak |psi|={abs03_vpp:.6e} at N={n03_vpp:.4f}")
    print(f"    k=0.5 (Vpp-only): peak |psi|={abs05_vpp:.6e} at N={n05_vpp:.4f}")
    at_lower_edge_vpp = n03_vpp <= 1.55 or n05_vpp <= 1.55  # flag, don't silently trust
    if at_lower_edge_vpp:
        print("    *** peak sits at/near the search window's own lower edge -- widen")
        print("    *** further before trusting this as a genuine interior peak.")
    a_vpp_only = abs05_vpp / abs03_vpp if abs03_vpp else float("nan")
    print(f"    A_vpp_only = peak|psi|(k=0.5)/peak|psi|(k=0.3) = {a_vpp_only:.2f}")

    # ==================================================================
    print("\n" + "-" * 78)
    print("NEGATIVE CONTROL -- mirror ablation: Vpp DROPPED from that same")
    print("term, kk^2*exp(-2N) KEPT (isolates kk^2 alone, no Vpp)")
    print("-" * 78)
    s03_k2 = run_ablated(1.0, 1.0, 0.3, t_end, LAMBDA_FIXED, False, True, **ic0)
    s05_k2 = run_ablated(1.0, 1.0, 0.5, t_end, LAMBDA_FIXED, False, True, **ic0)
    if s03_k2 is None or s05_k2 is None:
        print("  *** STOP -- k2-only ablation failed to solve.")
        return 1
    n03_k2, abs03_k2 = find_peak_abs_psi(s03_k2, t_end, 1.5, 30.0, 2851)
    n05_k2, abs05_k2 = find_peak_abs_psi(s05_k2, t_end, 1.5, 30.0, 2851)
    print(f"    k=0.3 (k2-only): peak |psi|={abs03_k2:.6e} at N={n03_k2:.4f}")
    print(f"    k=0.5 (k2-only): peak |psi|={abs05_k2:.6e} at N={n05_k2:.4f}")
    at_lower_edge_k2 = n03_k2 <= 1.55 or n05_k2 <= 1.55
    if at_lower_edge_k2:
        print("    *** peak sits at/near the search window's own lower edge -- widen")
        print("    *** further before trusting this as a genuine interior peak.")
    a_k2_only = abs05_k2 / abs03_k2 if abs03_k2 else float("nan")
    print(f"    A_k2_only = peak|psi|(k=0.5)/peak|psi|(k=0.3) = {a_k2_only:.2f}")

    # ==================================================================
    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    log10_diff_vpp = abs(np.log10(a_vpp_only) - np.log10(A_HAT_MEAN_REGRESSION))
    log10_diff_k2 = abs(np.log10(a_k2_only) - np.log10(A_HAT_MEAN_REGRESSION))
    vpp_same_order = log10_diff_vpp < 0.5  # within a factor of ~3, FINDING_P130's own bar
    k2_same_order = log10_diff_k2 < 0.5
    print(f"  A_hat (FINDING_P126, real full system) = {A_HAT_MEAN_REGRESSION:.1f}")
    print(
        f"  A_vpp_only = {a_vpp_only:.1f}  |log10 diff|={log10_diff_vpp:.4f}  same order: {vpp_same_order}"
    )
    print(
        f"  A_k2_only  = {a_k2_only:.1f}  |log10 diff|={log10_diff_k2:.4f}  same order: {k2_same_order}"
    )

    if vpp_same_order and not k2_same_order:
        print("\n  -> VPP-DOMINANT-MECHANISM-SUPPORTED, K2-ONLY MIRROR FAILS TO MATCH.")
        print("     Dropping kk^2*exp(-2N) from the dynamics ENTIRELY (keeping only the")
        print("     real k-dependent N=1 seed and the Vpp self-interaction) still gives")
        print("     an amplitude ratio the same order of magnitude as A_hat=6679. The")
        print("     mirror ablation (kk^2 kept, Vpp dropped) does NOT reproduce a")
        print("     comparable ratio -- together these support Vpp as the LOAD-BEARING")
        print("     amplification mechanism, with kk^2 mattering mainly through the tiny")
        print("     N=1 seed it sets (FINDING_P125-P130's own affine-in-kk^2 result),")
        print("     not through its ongoing dynamical role.")
    elif vpp_same_order and k2_same_order:
        print("\n  -> BOTH ABLATIONS REPRODUCE THE ORDER OF MAGNITUDE -- the amplification")
        print("     is not cleanly attributable to either term alone. Either mechanism,")
        print("     given the real seed, is roughly SUFFICIENT on its own -- a real,")
        print("     if less clean, result: the amplitude is robust to which specific")
        print("     driving term is present, suggesting the coupled psi<->dph structure")
        print("     itself (not one specific term) is what matters.")
    elif abs03_vpp > 0.05:  # a real, k-dependent resonance still occurs, just weaker
        print("\n  -> VPP-CORE, K2-CORRECTIONS LOAD-BEARING. A real resonance still")
        print("     occurs under Vpp-only (peak |psi| well above the tiny N=1 seed), but")
        print(f"     the amplitude ratio ({a_vpp_only:.1f}) is substantially different from")
        print("     A_hat=6679 -- Vpp is a necessary amplifier, but the periodic kk^2")
        print("     episodes this ablation removed materially set the final gain. The")
        print("     'dominant instantaneous term' finding does NOT, by itself, identify")
        print("     the dominant INTEGRATED mechanism -- exactly the user's own")
        print("     red-team point about phase/accumulation in an oscillating system.")
    else:
        print("\n  -> VPP-ONLY-REFUTED. No comparable amplification occurs when kk^2 is")
        print("     removed from the dynamics -- the dominant INSTANTANEOUS term (Vpp,")
        print("     found via term-by-term reconnaissance) is NOT the dominant")
        print("     INTEGRATED mechanism. A real, informative negative result: the")
        print("     amplification genuinely requires the coupled kk^2-and-Vpp dynamics,")
        print("     not either piece in isolation.")

    print("\n  THIS MECHANISTIC-ABLATION LINE IS CLOSED HERE, per the user's own")
    print("  explicit instruction, regardless of which outcome above obtained --")
    print("  no further ablation variants are attempted in response to this result.")

    print("\n  NOT ESTABLISHED:")
    print("   * a closed-form transfer/gain formula for the Vpp-dominated system, even")
    print("     under VPP-DOMINANT-MECHANISM-SUPPORTED -- named as future work, not")
    print("     attempted here, per the user's own plan.")
    print("   * anything at Lambda values, or (k, IC) combinations, other than")
    print("     k=0.3 and k=0.5's own main case tested throughout FINDING_P119-P130.")
    print("   * anything about MULTING itself (Gate 1). Any k[h/Mpc].")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
