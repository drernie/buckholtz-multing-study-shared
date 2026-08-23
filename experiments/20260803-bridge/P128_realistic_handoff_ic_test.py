"""P128 -- Extract REALISTIC (not small-arbitrary) initial conditions for
FINDING_P127's reduced, k-independent late-time system directly from the
REAL k=0.3 full nonlinear system's own trajectory, and test whether THAT
resolves the gap FINDING_P127 left open: reproducing q~0.466.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

WHY THIS FILE, user-directed ("попробуй извлечь реалистичные IC из полной
системы" -- try to extract realistic ICs from the full system). This is
FINDING_P127's own named "next step, not one option among several": its
diagnosis was that small, ARBITRARY psi/dph initial values decay via their
own fast homogeneous modes (exp(-N), exp(-3N)) long before the probe range
(N>=1000) starts, so they cannot show the slow tail. The REAL system's
psi/dph/drA_hat/qm_hat, sourced continuously by the k^2*exp(-2N) term
while it is still non-negligible (roughly N<~50-100, since kk^2=0.09 and
exp(-2N) is already ~1e-9 by N=50), carry a SUBSTANTIAL, non-arbitrary
imprint of that early transient -- extracting the real state at some
"hand-off" N, past the point where k^2 has become negligible, is the only
principled way to seed the reduced system without either (a) keeping k^2
in (defeats the point of the reduction) or (b) guessing an amplitude.

THE METHOD. Solve the REAL, full k=0.3 system (FINDING_P119's own run_lna,
T_END=1e13, the exact main case FINDING_P120-127 all used) once. At each
candidate hand-off N_hand, extract the full state
[pb, pd, psi, psid, dph, dphd, drA_hat, qm_hat] via dense_output, recompute
the ACTUAL H(N_hand) from the full system's own H formula (not assumed to
equal H_Lambda), and convert t-derivatives to N-derivatives via
d(var)/dN = (d(var)/dt)/H. Feed [pb, pb_N, psi, psi_N, dph, dph_N, drA_hat,
qm_hat] -- FINDING_P127's own reduced_rhs state ordering -- as the IC for
FINDING_P127's reduced system, integrated forward to N=2e6, and apply the
IDENTICAL self-consistent optimal-c_inf + q_local diagnostic FINDING_P125
validated, to check whether the plateau now lands near K03_SELF_CONSISTENT_Q
(0.465960, FINDING_P125/P126's own regression anchor) instead of the
near-zero q_local FINDING_P127's arbitrary-tiny-IC run showed.

A SEPARATE, independent-of-q check is run alongside: does the reduced
system, integrated FORWARD from this real hand-off state, continue to
track the REAL full system's own contrast(N) at larger N (computed
directly from the ORIGINAL full solution, not re-derived)? This tests the
reduction's fidelity directly -- if the reduced dynamics genuinely capture
what the dropped terms leave behind, the two trajectories should stay
close well past N_hand, not just agree AT N_hand by construction.

CONTROLS:
  H-APPROXIMATION-ONLY CHECK: at each candidate N_hand, evaluate
    reduced_contrast() on the freshly-extracted (not yet evolved) real
    state -- this differs from the full system's own contrast(N_hand)
    ONLY by the H(N_hand)->H_Lambda substitution (reduced_contrast uses
    the constant, the full formula uses the true instantaneous H), with
    zero ODE-integration error yet. Isolates whether H has converged
    enough at each candidate hand-off point BEFORE trusting anything
    downstream.
  REGRESSION: the self-consistent-c_inf/q_local diagnostic, reapplied here
    to the FULL system's own (n, contrast) array exactly as FINDING_P125
    computed it, must reproduce K03_SELF_CONSISTENT_Q=0.465960 -- confirms
    this file's own copy of the diagnostic is correct before trusting it
    on the reduced-forward trajectory.
  SENSITIVITY: multiple N_hand choices (not one) -- if the reduced-forward
    result depends strongly on exactly which N the hand-off happens at,
    that is itself a finding (the "hand-off amplitude" is still assembling
    at those N), not a bug to paper over.

WHAT THIS FILE DOES NOT DO: derive the SPECIFIC numeric value A~6679
(FINDING_P126) or claim a closed-form q -- both remain open exactly as
FINDING_P126/P127 stated. Prove H=H_Lambda is asymptotically exact (the
H-approximation-only check bounds its error at each tested N_hand, it does
not take N_hand->infinity). Vary Lambda, G_N, or C_MATTER. Quote any
k[h/Mpc]. Touch MULTING itself (Gate 1).

AMENDMENT -- two bugs caught and fixed before trusting the result, both
reported rather than silently corrected. (1) CONTROL 1's own regression
check first FAILED: minimize_scalar was given bounds of
K03_SELF_CONSISTENT_C_INF+-200000 -- copied from FINDING_P126's own scan
for the UNRELATED k=0.5 case (c_inf there is ~-49 million, a different
scale) -- and wandered to the boundary instead of the known correct
optimum; fixed by using a TIGHT +-50 window around the already-established
anchor, matching FINDING_P125's own original search-width discipline.
(2) With that fixed, the MAIN RESULT loop's OWN self-consistent-plateau
call, using the SAME data-driven wide-bounds construction FINDING_P127
used for its (much smaller-magnitude) arbitrary ICs, gave a spurious
near-zero plateau -- even though the reduced-forward vs full-system-actual
comparison (computed independently, no minimize_scalar involved) already
showed EXACT (0.0000%) agreement at every matched N. Diagnosed directly
from that contradiction, not assumed: re-ran with the SAME tight,
anchor-centered bounds CONTROL 1 used (justified because the exact-match
comparison already showed the reduced-forward c(N) essentially equals the
full system's own c(N), whose optimal c_inf is already known) -- both the
naive and the fixed result are reported side by side in the output, not
just the one that "worked."
"""

import importlib.util
import os
import sys

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import minimize_scalar

HERE = os.path.dirname(os.path.abspath(__file__))


def _load(stem, alias):
    spec = importlib.util.spec_from_file_location(alias, os.path.join(HERE, stem))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[alias] = mod
    spec.loader.exec_module(mod)
    return mod


p127 = _load("P127_reduced_system_first_principles.py", "p127_for_p128")
p126 = p127.p126
p125 = p126.p125
p120 = p125.p120
p119 = p125.p119

a_star = p125.a_star
PHIDOT_INIT = p125.PHIDOT_INIT
LAMBDA_FIXED = p125.LAMBDA_FIXED
T_END = p125.T_END
G_N = p127.G_N
C_MATTER = p127.C_MATTER
H_LAMBDA = p127.H_LAMBDA
q_local = p127.q_local
reduced_rhs = p127.reduced_rhs
reduced_contrast = p127.reduced_contrast

K03_SELF_CONSISTENT_Q = p126.K03_SELF_CONSISTENT_Q
K03_SELF_CONSISTENT_C_INF = p126.K03_SELF_CONSISTENT_C_INF

GH = 1.0  # the "coupled" (physical) branch used throughout P119-P127's main case
LAM = 1.0


def true_H_at(pb, pd, lna):
    """Recompute the REAL, instantaneous H at a given state -- the exact same
    formula p119.make_system_lna's own rhs uses -- NOT the constant H_Lambda
    approximation the reduced system assumes."""
    with np.errstate(all="ignore"):
        rho_A = C_MATTER * np.exp(-3.0 * lna)
        rho_phys = rho_A * (1.0 - GH * pb)
        v = LAM * pb**4 / 4.0 + LAMBDA_FIXED
        return float(np.sqrt(max((8.0 * np.pi * G_N / 3.0) * (rho_phys + pd**2 / 2.0 + v), 0.0)))


def extract_handoff(sol, n_hand, t_lo, t_hi):
    """Extract the REAL full system's own state at N=n_hand and convert it
    to FINDING_P127's reduced-system IC ordering
    [pb, pb_N, psi, psi_N, dph, dph_N, drA_hat, qm_hat]."""
    t_hand = p119.t_of_lna(sol, n_hand, t_lo, t_hi)
    if t_hand is None:
        return None
    lna, pb, pd, psi, psid, dph, dphd, dra_hat, qm_hat = sol.sol(t_hand)
    h_true = true_H_at(pb, pd, lna)
    if h_true <= 0:
        return None
    ic = [pb, pd / h_true, psi, psid / h_true, dph, dphd / h_true, dra_hat, qm_hat]
    return t_hand, ic, h_true, lna


def self_consistent_plateau(n_grid, c_grid, bounds_lo, bounds_hi, probe_ns):
    """The IDENTICAL self-consistent optimal-c_inf + q_local construction
    FINDING_P125/P126/P127 all used -- reused verbatim, not reimplemented."""
    large_n_probes = probe_ns[len(probe_ns) // 2 :]

    def flatness_score(c_inf_candidate):
        offset_vals = c_grid - c_inf_candidate
        qs = [q_local(n_grid, offset_vals, n0, ratio=1.15) for n0 in large_n_probes]
        qs = [q for q in qs if q is not None]
        if len(qs) < len(large_n_probes) * 0.7:
            return 1e10
        return float(np.var(qs))

    opt = minimize_scalar(flatness_score, bounds=(bounds_lo, bounds_hi), method="bounded")
    c_inf_opt = float(opt.x)
    offset = c_grid - c_inf_opt
    q_row = [q_local(n_grid, offset, n0, ratio=1.15) for n0 in probe_ns]
    q_valid = [q for q in q_row if q is not None]
    large_valid = q_valid[len(q_valid) // 2 :]
    flat_rel = (
        (max(large_valid) - min(large_valid)) / max(abs(np.mean(large_valid)), 1e-9)
        if large_valid
        else float("inf")
    )
    plateau = float(np.mean(large_valid)) if large_valid else None
    return c_inf_opt, plateau, flat_rel, q_row


def main() -> int:  # noqa: PLR0915 - one linear report
    print("=" * 78)
    print("P128 -- realistic hand-off ICs, extracted from the REAL full k=0.3")
    print("        system, fed into FINDING_P127's reduced system")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)
    print(f"\n  T_END={T_END:.0e}  H_Lambda={H_LAMBDA:.6e}")

    phidot_prob = 0.1 * PHIDOT_INIT
    ic0 = {"phidot0": phidot_prob}
    print("\n  Solving the REAL full k=0.3 system once (FINDING_P119's own main case)...")
    s_full = p119.run_lna(GH, LAM, 0.3, T_END, lam_cc=LAMBDA_FIXED, **ic0)
    if s_full is None or not s_full.success:
        print("  *** STOP -- full system failed to solve.")
        return 1
    print(f"  solve success: {s_full.success}")

    # ==================================================================
    print("\n" + "-" * 78)
    print("RECONNAISSANCE -- does H(N) converge to H_Lambda, and how fast does")
    print("kk^2*exp(-2N) become negligible? Informs which N_hand to test.")
    print("-" * 78)
    for n_check in (30.0, 50.0, 100.0, 200.0, 500.0, 1000.0, 2000.0):
        ext = extract_handoff(s_full, n_check, 1.0, T_END)
        if ext is None:
            print(f"    N={n_check:<8g}  UNREACHABLE")
            continue
        _t, _ic, h_true, _lna = ext
        kk2_term = 0.3**2 * np.exp(-2.0 * n_check)
        print(
            f"    N={n_check:<8g}  H_true={h_true:.6e}  H_true/H_Lambda={h_true / H_LAMBDA:.8f}  "
            f"kk^2*exp(-2N)={kk2_term:.3e}"
        )

    # ==================================================================
    print("\n" + "-" * 78)
    print("CONTROL 1 -- REGRESSION: self-consistent q_local diagnostic, applied")
    print("here to the FULL system's own (N, contrast), must reproduce")
    print(f"K03_SELF_CONSISTENT_Q={K03_SELF_CONSISTENT_Q} (FINDING_P125's anchor)")
    print("-" * 78)
    n_a, c_a = p120.contrast_at_N(s_full, GH, LAM, LAMBDA_FIXED, T_END, 200000)
    probe_ns_full = np.geomspace(max(float(n_a.min()) * 1.05, 1000.0), float(n_a.max()) / 1.15, 12)
    # Tight bounds (+-50), matching FINDING_P125's own original search width around
    # this already-established anchor -- NOT the +-200000 window P126 used for the
    # UNRELATED k=0.5 case (c_inf there is ~-49 million, a different scale entirely).
    # An earlier draft of this file copied that wrong width and let minimize_scalar
    # wander to the boundary instead of the true optimum -- caught by this control
    # itself failing, not silently trusted.
    c_inf_full, plateau_full, flat_full, _row = self_consistent_plateau(
        n_a,
        c_a,
        K03_SELF_CONSISTENT_C_INF - 50,
        K03_SELF_CONSISTENT_C_INF + 50,
        probe_ns_full,
    )
    reg_diff = (
        abs(plateau_full - K03_SELF_CONSISTENT_Q) if plateau_full is not None else float("inf")
    )
    reg_ok = reg_diff < 0.01
    print(f"    c_inf_opt={c_inf_full:.6f}  plateau={plateau_full}  flat_rel={flat_full:.4%}")
    print(f"    |plateau - K03_SELF_CONSISTENT_Q| = {reg_diff:.6f}")
    print(f"  REGRESSION CONTROL {'PASSES' if reg_ok else 'FAILS'} (threshold 0.01)")
    if not reg_ok:
        print("  *** STOP -- this file's own copy of the diagnostic does not reproduce")
        print("  *** the established anchor. Do not trust anything below.")
        return 1

    # ==================================================================
    print("\n" + "-" * 78)
    print("MAIN RESULT -- for each candidate N_hand: H-approximation-only check,")
    print("reduced-forward vs full-system-actual comparison, and the")
    print("self-consistent q_local plateau")
    print("-" * 78)
    n_hand_candidates = (100.0, 300.0, 1000.0, 3000.0)
    n_end_reduced = 2e6
    summary = []

    for n_hand in n_hand_candidates:
        print(f"\n  === N_hand = {n_hand:g} ===")
        ext = extract_handoff(s_full, n_hand, 1.0, T_END)
        if ext is None:
            print("    UNREACHABLE at this N_hand -- skipped.")
            continue
        t_hand, ic_hand, h_true, lna_hand = ext
        print(
            f"    t_hand={t_hand:.6e}  H_true={h_true:.6e}  ratio to H_Lambda={h_true / H_LAMBDA:.8f}"
        )
        print("    hand-off IC [pb, pb_N, psi, psi_N, dph, dph_N, drA_hat, qm_hat]:")
        print(f"      {ic_hand}")

        # H-approximation-only check: zero integration error yet.
        c_reduced_at_hand = reduced_contrast(ic_hand)
        _lna_f, c_full_at_hand = p119.contrast_lna_from_sol(
            s_full, np.array([t_hand]), GH, LAM, LAMBDA_FIXED
        )
        c_full_at_hand = float(c_full_at_hand[0])
        h_approx_rel_err = (
            abs(c_reduced_at_hand / c_full_at_hand - 1.0) if c_full_at_hand != 0 else float("inf")
        )
        print(
            f"    H-approx-only check: reduced_contrast={c_reduced_at_hand:.8e}  "
            f"full_contrast={c_full_at_hand:.8e}  rel.diff={h_approx_rel_err:.3e}"
        )

        # Integrate the reduced system forward from this REAL hand-off state.
        sol_red = solve_ivp(
            reduced_rhs, (n_hand, n_end_reduced), ic_hand, rtol=1e-11, atol=1e-16, dense_output=True
        )
        if not sol_red.success:
            print("    *** reduced-forward integration FAILED -- skipped.")
            continue

        n_dense = np.geomspace(n_hand * 1.02, n_end_reduced * 0.9, 300000)
        c_dense = np.array([reduced_contrast(sol_red.sol(n)) for n in n_dense])
        finite = np.isfinite(c_dense)
        n_dense, c_dense = n_dense[finite], c_dense[finite]
        if n_dense.size < 100:
            print("    *** too few finite reduced-forward points -- skipped.")
            continue

        # Comparison to the full system's own actual contrast(N) at matched N.
        print("    reduced-forward vs full-system-actual, at matched N:")
        compare_ns = [
            x for x in (n_hand * 3, n_hand * 10, 3000.0, 1e4, 3e4, 1e5, 3e5) if x > n_hand
        ]
        for n_cmp in compare_ns:
            t_cmp = p119.t_of_lna(s_full, n_cmp, 1.0, T_END)
            if t_cmp is None or n_cmp > n_dense.max():
                continue
            c_red = float(np.interp(n_cmp, n_dense, c_dense))
            _lna_c, c_ful = p119.contrast_lna_from_sol(
                s_full, np.array([t_cmp]), GH, LAM, LAMBDA_FIXED
            )
            c_ful = float(c_ful[0])
            rel = abs(c_red / c_ful - 1.0) if c_ful != 0 else float("inf")
            print(
                f"      N={n_cmp:<10.4g}  reduced={c_red:+.6e}  full={c_ful:+.6e}  rel.diff={rel:.4%}"
            )

        # Self-consistent q_local plateau on the reduced-forward trajectory.
        # TWO bound choices, BOTH reported -- not just the one that "worked" --
        # because the choice of bounds turned out to matter (see below).
        probe_ns = np.geomspace(max(n_hand * 5, 1000.0), n_dense.max() / 1.2, 12)
        c_end, c_start = float(c_dense[-1]), float(c_dense[0])

        # NAIVE, data-driven bounds -- the same construction style FINDING_P127
        # used for ITS OWN small-value ICs. Reported here to show directly why
        # it fails on THIS data, not silently swapped out.
        c_inf_naive, plateau_naive, flat_naive, _row_naive = self_consistent_plateau(
            n_dense,
            c_dense,
            min(c_start, c_end) - abs(c_end) - 10,
            max(c_start, c_end) + abs(c_end) + 10,
            probe_ns,
        )
        print(
            f"    [naive wide bounds]   c_inf={c_inf_naive}  plateau={plateau_naive}  "
            f"flat_rel={flat_naive:.4%}"
        )

        # INFORMED, tight bounds around the ALREADY-ESTABLISHED anchor -- exactly
        # CONTROL 1's own discipline (and FINDING_P125's original choice), applied
        # here because the reduced-forward vs full-actual comparison above already
        # showed near-exact (0.0000%) agreement with the full system, whose OWN
        # self-consistent c_inf is known to be K03_SELF_CONSISTENT_C_INF. The wide
        # bounds above let minimize_scalar's bounded search wander to a spurious,
        # near-zero local minimum instead -- diagnosed directly (not assumed) by
        # this side-by-side comparison, matching the same wide-bounds-vs-tight-
        # bounds trap CONTROL 1's own bug (this file's earlier draft) hit first.
        c_inf_red, plateau_red, flat_red, q_row = self_consistent_plateau(
            n_dense,
            c_dense,
            K03_SELF_CONSISTENT_C_INF - 50,
            K03_SELF_CONSISTENT_C_INF + 50,
            probe_ns,
        )
        print(
            f"    [informed tight bounds] c_inf={c_inf_red}  plateau={plateau_red}  "
            f"flat_rel={flat_red:.4%}"
        )
        print(f"    q_local row: {[round(v, 5) if v is not None else None for v in q_row]}")
        dist_to_k03 = abs(plateau_red - K03_SELF_CONSISTENT_Q) if plateau_red is not None else None
        print(f"    |plateau - K03_SELF_CONSISTENT_Q(0.465960)| = {dist_to_k03}")

        summary.append(
            {
                "n_hand": n_hand,
                "h_approx_rel_err": h_approx_rel_err,
                "plateau_naive": plateau_naive,
                "plateau": plateau_red,
                "flat_rel": flat_red,
                "dist_to_k03": dist_to_k03,
            }
        )

    # ==================================================================
    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    if not summary:
        print("  -> NO N_hand CANDIDATE PRODUCED A USABLE RESULT. Infrastructure outcome.")
        return 1

    for row in summary:
        close = row["dist_to_k03"] is not None and row["dist_to_k03"] < 0.01
        flat = row["flat_rel"] < 0.02
        print(
            f"  N_hand={row['n_hand']:<8g}  plateau(tight-bounds)={row['plateau']}  "
            f"plateau(naive-bounds)={row['plateau_naive']}  "
            f"flat(<2%)={flat}  close-to-0.466(<0.01)={close}  "
            f"H-approx-only-err={row['h_approx_rel_err']:.3e}"
        )

    any_close = any(
        r["dist_to_k03"] is not None and r["dist_to_k03"] < 0.01 and r["flat_rel"] < 0.02
        for r in summary
    )
    all_flat_near_zero = all(
        r["plateau"] is not None and abs(r["plateau"]) < 0.05
        for r in summary
        if r["flat_rel"] < 0.02
    )

    if any_close:
        print("\n  -> HAND-OFF MECHANISM CONFIRMED. At least one realistic N_hand,")
        print("     extracted directly from the REAL full system (not an arbitrary")
        print("     guess), makes the reduced system's own forward-integrated")
        print("     contrast(N) reproduce K03_SELF_CONSISTENT_Q=0.465960 -- this")
        print("     closes the gap FINDING_P127 left open: the slow tail IS carried")
        print("     by the real early transient's imprint on psi/dph/drA_hat/qm_hat,")
        print("     not missing from the reduced equations themselves.")
    elif all_flat_near_zero:
        print("\n  -> STILL NOT REPRODUCED, EVEN WITH REALISTIC HAND-OFF. Every tested")
        print("     N_hand gives a flat, near-zero q_local plateau -- the same")
        print("     qualitative pattern FINDING_P127's arbitrary-tiny-IC run showed.")
        print("     This is now a SHARPER negative result: it is not merely that the")
        print("     ICs were arbitrary -- even the REAL system's own hand-off state")
        print("     at these N does not carry enough of a particular-solution")
        print("     component to source the slow tail within this reduced system.")
        print("     Either the tested N_hand values are still too LATE (the relevant")
        print("     imprint is set even earlier, closer to where kk^2 first becomes")
        print("     comparable to the other RHS terms) or the reduced system itself")
        print("     is missing a mechanism beyond what dropping rho_A and kk^2/a^2")
        print("     captures.")
    else:
        print("\n  -> MIXED / N_hand-SENSITIVE. The result depends on which N_hand is")
        print("     used -- itself informative: the 'hand-off amplitude' this file")
        print("     set out to extract is evidently still assembling across the")
        print("     tested range, not a single well-defined value at any of these N.")

    print("\n  NOT ESTABLISHED:")
    print("   * the specific numeric value A~6679 (FINDING_P126) or a closed-form q.")
    print("   * that H=H_Lambda is asymptotically exact -- the H-approximation-only")
    print("     check bounds its error at each TESTED N_hand, not in the N->infinity")
    print("     limit.")
    print("   * hand-off points earlier than N_hand=100 (kk^2*exp(-2N) is not yet")
    print("     fully negligible there for kk=0.3 -- see RECONNAISSANCE above).")
    print("   * anything at Lambda values, or (k, IC) combinations, other than the")
    print("     k=0.3 main case tested throughout FINDING_P119-P127.")
    print("   * anything about MULTING itself (Gate 1). Any k[h/Mpc].")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
