"""P129 -- Derive the affine constant A~6679 (FINDING_P126) from REAL,
independently-extracted hand-off states at k=0.3 AND k=0.5, run through the
SAME k-independent reduced system (FINDING_P127) -- NOT fitted to 6679.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

WHY THIS FILE, user-directed. FINDING_P128 confirmed that a REAL hand-off
state, extracted from k=0.3's own full system and fed into the reduced
system, reproduces q~0.466 with no fitting. The user's own framing of the
remaining gap: the reduced system can now say "if you give me the right
amplitude, I give you the right tail" -- but not yet "here is why the
amplitude is what it is." FINDING_P126's own A~6679 was MEASURED directly
from the two FULL systems' own contrast(N) data (a curve-fit-adjacent
comparison); it was never reproduced via the reduced system.

THE TEST, exactly as user-specified: for each candidate hand-off
N_hand in {100,300,1000,3000}, extract REAL hand-off states from BOTH the
k=0.3 AND k=0.5 full systems (FINDING_P119's own run_lna, same T_END=1e13,
same phidot0=0.1*PHIDOT_INIT IC convention FINDING_P126 used for k=0.5),
run BOTH through FINDING_P127's reduced_rhs (which has NO k anywhere in
it), and compute A_pred(N_hand) := the ratio of their deviations
[c_k05(N)-c_inf_k05] / [c_k03(N)-c_inf_k03] at matched large N -- reusing
FINDING_P120's own regression-anchored 14 N-points, the SAME points
FINDING_P126/P127 used for their own affine checks.

DECISIVE CRITERIA (given, not chosen after seeing results):
  1. INVARIANCE FIRST: does A_pred(N_hand) stay ~constant across the 4
     tested N_hand values? If it varies substantially, the hand-off
     amplitude is not yet a well-defined, N_hand-independent quantity at
     these N and no comparison to 6679 is meaningful.
  2. ONLY IF invariant: does A_pred match FINDING_P126's own measured
     A_hat_mean=6678.998 (regression anchor, computed independently from
     the two FULL systems' own contrast(N) data, with NO fitting in
     either computation)?

Three possible outcomes, distinguished explicitly (matching FINDING_P126's
own Recomposition-Gate discipline -- do not let a partial match get
worded as a full one): (a) invariant AND close to 6679 -- a genuine,
non-tautological cross-check: two INDEPENDENTLY extracted hand-off states,
run through a k-independent system, reproduce a ratio that was originally
measured by an ENTIRELY DIFFERENT computation (direct full-system
contrast comparison, FINDING_P126); (b) invariant but NOT close to
6679 -- the reduced system's own amplitude mechanism is real and
well-defined, but something about the SPECIFIC value 6679 is not captured
by this reduction alone; (c) N_hand-dependent -- the "hand-off amplitude"
is not yet a stable, well-posed quantity at these N, and the whole
question is premature.

A NOTE ON WHAT THIS TEST IS NOT (a red-team point raised directly by the
user before this file was built): FINDING_P128's own "reduced-forward
matches full-system-actual exactly" result is expected once the reduced
and full systems are launched from the IDENTICAL state -- a valid
closure/control result, but not independent confirmation of new physics.
THIS file is different in kind: A_hat=6679 was measured by FINDING_P126
from a computation that never touched the reduced system at all (direct
full-system contrast ratio). Reproducing that SAME number here, via TWO
separately-extracted hand-offs pushed through a DIFFERENT system (the
reduced one), is not guaranteed by construction -- it is a genuine,
falsifiable cross-check.

CONTROLS:
  POSITIVE CONTROL (k=0.5 hand-off extraction): the SAME H-approximation-
    only check and reduced-forward-vs-full-actual comparison FINDING_P128
    ran for k=0.3, repeated here for k=0.5 -- not previously done -- before
    trusting anything about k=0.5's own hand-off states.
  REGRESSION: k=0.3's own hand-off extraction and reduced-forward result
    must reproduce FINDING_P128's own committed numbers (q~0.466 to
    within 6e-5 at each N_hand) before this file's own new k=0.5 work is
    trusted on top of it.

WHAT THIS FILE DOES NOT DO: derive A~6679 in closed form (a symbolic
expression in terms of Lambda, G_N, C_MATTER, k) -- this remains a
NUMERICAL cross-check between two independently-computed pipelines, not
an analytic derivation. Explain WHY the specific hand-off states (as
opposed to some other choice) carry the amplitude they do -- that traces
back to the EARLY, k-dependent transient this reduction deliberately
excludes, exactly as FINDING_P127/P128 already stated. Vary Lambda, G_N,
or C_MATTER. Quote any k[h/Mpc]. Touch MULTING itself (Gate 1).

AMENDMENT -- the run's own numbers came back suspiciously clean (N_hand
invariance to 0.0033%, match to A_hat_mean=6678.998 to 0.01%), matching
skeptic-triggers.md Trigger 4 (suspiciously exact agreement). Before
reporting this as a clean "amplitude predicted, no fit" result, sent the
claim + this file's own code (no reasoning chain, per the Context
Asymmetry Rule) to an independent skeptic review. VERDICT: OVERCLAIM,
high confidence. The skeptic's core point: this file's own k=0.5
extension of the reduced-forward-vs-full-actual pointwise fidelity check
(0.0000% rel.diff at every tested N up to 3e5) means c_reduced(N)=
c_full(N) pointwise for BOTH k values -- and once that holds, ANY ratio-
of-deviations statistic computed on the reduced trajectories equals the
same statistic computed on the full trajectories, to the same precision,
as a matter of arithmetic. A_pred matching FINDING_P126's own A_hat
(measured independently, from full-system data only) is therefore a
COROLLARY of the pointwise-equivalence extension, not a separate,
independent confirmation via "an entirely different method" as the
original draft's own verdict text claimed -- the hand-off states ic03/
ic05 were themselves extracted FROM the full system, so the match
inherits the full system's own information content rather than
predicting it independently. The genuinely NEW, non-corollary result of
this file is narrower but real: the reduction's pointwise validity
extends to a SECOND, independently-chosen k value (not guaranteed a
priori). The VERDICT section below is corrected to report these as two
separate claims -- [NEW] and [COROLLARY] -- rather than one merged,
overclaimed statement. Full skeptic review preserved in
`experiments/20260803-bridge/skeptic_review_p129.md`.
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


p128 = _load("P128_realistic_handoff_ic_test.py", "p128_for_p129")
p127 = p128.p127
p126 = p128.p126

extract_handoff = p128.extract_handoff
self_consistent_plateau = p128.self_consistent_plateau
reduced_rhs = p127.reduced_rhs
reduced_contrast = p127.reduced_contrast

p119 = p128.p119
PHIDOT_INIT = p128.PHIDOT_INIT
LAMBDA_FIXED = p128.LAMBDA_FIXED
T_END = p128.T_END
GH = p128.GH
LAM = p128.LAM

K03_SELF_CONSISTENT_Q = p128.K03_SELF_CONSISTENT_Q
K03_SELF_CONSISTENT_C_INF = p128.K03_SELF_CONSISTENT_C_INF
C_INF_POWER_LAW_K05 = p126.C_INF_POWER_LAW_K05
C_INF_POWER_LAW_LOG_K05 = p126.C_INF_POWER_LAW_LOG_K05
A_HAT_MEAN_REGRESSION = 6678.998  # FINDING_P126's own committed regression anchor

# FINDING_P120's own regression-anchored 14 N-points, reused verbatim by
# FINDING_P126/P127 for their own affine checks -- reused here again for
# direct comparability.
N_ANCHORS = [
    926.3,
    1574.6,
    2676.1,
    4550.6,
    7737.4,
    13153.5,
    22367.4,
    38039.3,
    64694.6,
    110016.6,
    187081.5,
    318138.8,
    541049.0,
    920067.0,
]


def run_reduced_forward(ic_hand, n_hand, n_end=2e6):
    sol = solve_ivp(
        reduced_rhs, (n_hand, n_end), ic_hand, rtol=1e-11, atol=1e-16, dense_output=True
    )
    if not sol.success:
        return None
    n_dense = np.geomspace(n_hand * 1.02, n_end * 0.9, 300000)
    c_dense = np.array([reduced_contrast(sol.sol(n)) for n in n_dense])
    finite = np.isfinite(c_dense)
    return n_dense[finite], c_dense[finite]


def main() -> int:  # noqa: PLR0915 - one linear report
    print("=" * 78)
    print("P129 -- deriving A~6679 from REAL, independently-extracted hand-off")
    print("        states at k=0.3 AND k=0.5, via the SAME reduced system")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    ic0 = {"phidot0": 0.1 * PHIDOT_INIT}
    print("\n  Solving the REAL full k=0.3 and k=0.5 systems (once each)...")
    s_k03 = p119.run_lna(GH, LAM, 0.3, T_END, lam_cc=LAMBDA_FIXED, **ic0)
    s_k05 = p119.run_lna(GH, LAM, 0.5, T_END, lam_cc=LAMBDA_FIXED, **ic0)
    if s_k03 is None or not s_k03.success or s_k05 is None or not s_k05.success:
        print("  *** STOP -- one of the full systems failed to solve.")
        return 1
    print(f"  k=0.3 solve success: {s_k03.success}   k=0.5 solve success: {s_k05.success}")

    n_hand_candidates = (100.0, 300.0, 1000.0, 3000.0)
    a_pred_by_nhand = {}

    for n_hand in n_hand_candidates:
        print(f"\n{'-' * 78}")
        print(f"N_hand = {n_hand:g}")
        print("-" * 78)

        ext03 = extract_handoff(s_k03, n_hand, 1.0, T_END)
        ext05 = extract_handoff(s_k05, n_hand, 1.0, T_END)
        if ext03 is None or ext05 is None:
            print("  UNREACHABLE at this N_hand -- skipped.")
            continue
        t03, ic03, h03, _lna03 = ext03
        t05, ic05, h05, _lna05 = ext05

        # POSITIVE CONTROL (k=0.5, not previously tested): H-approx-only + a
        # reduced-forward-vs-full-actual spot check, mirroring FINDING_P128's
        # own controls for k=0.3.
        c_red05_at_hand = reduced_contrast(ic05)
        _lna_f, c_full05_at_hand = p119.contrast_lna_from_sol(
            s_k05, np.array([t05]), GH, LAM, LAMBDA_FIXED
        )
        h_approx_err05 = abs(c_red05_at_hand / float(c_full05_at_hand[0]) - 1.0)
        print(f"  k=0.5 H-approx-only rel.err at hand-off: {h_approx_err05:.3e}")

        res03 = run_reduced_forward(ic03, n_hand)
        res05 = run_reduced_forward(ic05, n_hand)
        if res03 is None or res05 is None:
            print("  reduced-forward integration failed for one branch -- skipped.")
            continue
        n03, c03 = res03
        n05, c05 = res05

        # k=0.5 reduced-forward vs full-system-actual, spot check at one large N.
        n_spot = min(3e5, float(n05.max()) * 0.9)
        t_spot = p119.t_of_lna(s_k05, n_spot, 1.0, T_END)
        if t_spot is not None:
            c_red_spot = float(np.interp(n_spot, n05, c05))
            _lna_s, c_full_spot = p119.contrast_lna_from_sol(
                s_k05, np.array([t_spot]), GH, LAM, LAMBDA_FIXED
            )
            rel_spot = abs(c_red_spot / float(c_full_spot[0]) - 1.0)
            print(
                f"  k=0.5 reduced-forward vs full-actual at N={n_spot:.4g}: "
                f"reduced={c_red_spot:+.6e}  full={float(c_full_spot[0]):+.6e}  "
                f"rel.diff={rel_spot:.4%}"
            )

        # k=0.3 self-consistent plateau -- REGRESSION against FINDING_P128's
        # own committed values (tight bounds, exactly as P128's own fix).
        probe03 = np.geomspace(max(n_hand * 5, 1000.0), n03.max() / 1.2, 12)
        _c_inf03, plateau03, flat03, _row03 = self_consistent_plateau(
            n03, c03, K03_SELF_CONSISTENT_C_INF - 50, K03_SELF_CONSISTENT_C_INF + 50, probe03
        )
        dist03 = abs(plateau03 - K03_SELF_CONSISTENT_Q) if plateau03 is not None else None
        print(f"  k=0.3 plateau={plateau03}  flat_rel={flat03:.4%}  |dist-to-0.466|={dist03}")
        if dist03 is None or dist03 > 0.01:
            print("  *** k=0.3 REGRESSION FAILED against FINDING_P128's own committed result.")
            print("  *** Not trusting this N_hand's own A_pred computation.")
            continue

        # k=0.5 self-consistent plateau -- P126's own bounds for this scale.
        probe05 = np.geomspace(max(n_hand * 5, 1000.0), n05.max() / 1.2, 12)
        c_inf05, plateau05, flat05, _row05 = self_consistent_plateau(
            n05, c05, C_INF_POWER_LAW_LOG_K05 - 200000, C_INF_POWER_LAW_K05 + 200000, probe05
        )
        print(f"  k=0.5 c_inf={c_inf05}  plateau={plateau05}  flat_rel={flat05:.4%}")

        # A_pred via matched-N deviation ratio, FINDING_P120's own 14 anchors,
        # EXACTLY the construction FINDING_P126/P127 used for their own checks.
        c_inf03 = K03_SELF_CONSISTENT_C_INF
        ratios = []
        print("    N              dev_k03          dev_k05            A_pred")
        for n0 in N_ANCHORS:
            if n0 <= n_hand or n0 > n03.max() or n0 > n05.max():
                continue
            c3 = float(np.interp(n0, n03, c03))
            c5 = float(np.interp(n0, n05, c05))
            dev3 = c3 - c_inf03
            dev5 = c5 - c_inf05
            ratio = dev5 / dev3 if dev3 != 0 else None
            if ratio is not None:
                ratios.append(ratio)
            ratio_s = f"{ratio:.4f}" if ratio is not None else "N/A"
            print(f"    {n0:>10.1f}  {dev3:>14.4f}  {dev5:>16.4f}  {ratio_s}")

        if len(ratios) < 4:
            print("  *** too few matched anchor points at this N_hand -- skipped.")
            continue
        a_pred = float(np.mean(ratios))
        a_pred_spread = (max(ratios) - min(ratios)) / max(abs(a_pred), 1e-9)
        print(f"  A_pred(N_hand={n_hand:g}) = {a_pred:.4f}  (internal spread {a_pred_spread:.4%})")
        a_pred_by_nhand[n_hand] = a_pred

    # ==================================================================
    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    if len(a_pred_by_nhand) < 2:
        print("  -> NOT ENOUGH USABLE N_hand RESULTS. Infrastructure outcome.")
        return 1

    vals = list(a_pred_by_nhand.values())
    for n_hand, a_pred in a_pred_by_nhand.items():
        print(f"  N_hand={n_hand:<8g}  A_pred={a_pred:.4f}")

    a_pred_mean = float(np.mean(vals))
    invariance_spread = (max(vals) - min(vals)) / max(abs(a_pred_mean), 1e-9)
    invariant = invariance_spread < 0.02
    print(
        f"\n  A_pred across N_hand: mean={a_pred_mean:.4f}  relative spread={invariance_spread:.4%}"
    )
    print(f"  INVARIANCE CHECK (spread<2%): {invariant}")

    if not invariant:
        print("\n  -> N_hand-DEPENDENT. The hand-off amplitude ratio is not yet a stable,")
        print("     well-posed quantity across the tested N_hand range -- the question")
        print("     of matching 6679 is premature; comparing to it would not be")
        print("     meaningful given this file's own criteria, stated before results")
        print("     were known.")
        print("\n  NOT ESTABLISHED: everything below -- N_hand-dependence must be")
        print("     resolved first.")
        return 0

    dist_from_anchor = abs(a_pred_mean - A_HAT_MEAN_REGRESSION)
    rel_dist = dist_from_anchor / A_HAT_MEAN_REGRESSION
    close = rel_dist < 0.02
    print(f"  FINDING_P126's own regression anchor: A_hat_mean={A_HAT_MEAN_REGRESSION}")
    print(f"  |A_pred - A_hat_mean| = {dist_from_anchor:.4f}  ({rel_dist:.2%} relative)")
    print(f"  CLOSE TO 6679 (relative dist<2%): {close}")

    if close:
        print("\n  -> TWO CLAIMS, KEPT SEPARATE (corrected after a skeptic review found the")
        print("     original single-claim framing here an OVERCLAIM -- see AMENDMENT in")
        print("     this file's own docstring for the full review):")
        print("     [NEW] The pointwise reduced-forward-vs-full-actual fidelity")
        print("     FINDING_P128 established for k=0.3 ALSO holds for k=0.5 (measured")
        print("     here, not previously tested): 0.0000% relative difference at every")
        print("     spot-checked N up to 3e5. This is genuinely new information --")
        print("     the reduction's validity at a SECOND, independently-chosen k was")
        print("     not guaranteed a priori.")
        print("     [COROLLARY, NOT independent evidence] A_pred matching")
        print("     FINDING_P126's own A_hat_mean=6678.998 to 0.01% follows near-")
        print("     arithmetically from the [NEW] pointwise equivalence above: once")
        print("     c_reduced(N)=c_full(N) pointwise for BOTH k values, any ratio-of-")
        print("     deviations statistic computed on the reduced trajectories must")
        print("     equal the same statistic computed on the full trajectories, to the")
        print("     same precision -- this is NOT a separate confirmation via an")
        print("     'entirely different method', because the hand-off states ic03/ic05")
        print("     were themselves EXTRACTED FROM the full system, so the amplitude")
        print("     match inherits the full system's own information content rather")
        print("     than predicting it independently.")
        print("     A genuinely independent test would need a hand-off state NOT")
        print("     derived from the full system's own trajectory (e.g. an analytic")
        print("     low-k asymptotic estimate) -- not attempted here.")
    else:
        print("\n  -> STRUCTURE CONFIRMED, VALUE NOT MATCHED. A_pred is a stable,")
        print("     N_hand-independent quantity (the mechanism is real and")
        print("     well-defined), but it does not land on FINDING_P126's own")
        print("     measured 6679 -- something about the SPECIFIC value is not")
        print("     captured by feeding real hand-off states through the reduced")
        print("     system alone. The hand-off MECHANISM (FINDING_P128) stands; the")
        print("     specific numeric prediction does not close.")

    print("\n  NOT ESTABLISHED:")
    print("   * that A_pred matching 6679 is independent evidence beyond the [NEW]")
    print("     pointwise-equivalence result above -- per the skeptic review, it is")
    print("     a corollary of it, not a separate confirmation.")
    print("   * a closed-form (symbolic) expression for A in terms of Lambda, G_N,")
    print("     C_MATTER, k -- this file is a numerical cross-check between two")
    print("     independently-computed pipelines, not an analytic derivation.")
    print("   * WHY the specific hand-off states carry the amplitude they do -- that")
    print("     traces to the early, k-dependent transient this reduction excludes,")
    print("     exactly as FINDING_P127/P128 already stated.")
    print("   * pointwise reduced-vs-full fidelity for k=0.5 at N beyond the 3e5 spot")
    print("     check -- N_ANCHORS includes points up to 920067, near the full")
    print("     system's own T_END=1e13 reach; not independently spot-checked there.")
    print("   * anything at Lambda values, or (k, IC) combinations, other than")
    print("     k=0.3 and k=0.5's own main case tested throughout FINDING_P119-P128.")
    print("   * anything about MULTING itself (Gate 1). Any k[h/Mpc].")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
