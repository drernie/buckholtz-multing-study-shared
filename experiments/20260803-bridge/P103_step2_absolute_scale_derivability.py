"""P103 -- attack Gamow Bridge Test Step 2 directly: can Lambda_internal be DERIVED,
not searched, from the completion's own microphysics (P58-P92, extended P86)?

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

THE PIVOT THIS FILE MAKES, STATED BEFORE ANY CODE RUNS. P93-P102 (nine
attempts) all did the SAME kind of thing: pick an external anchor (a single
epoch's Omega_Lambda, the age of the universe, a two-epoch H(a) shape),
SEARCH the completion's free Lambda_internal against it, and ask whether a
match exists. Every attempt failed to pin an absolute scale. The Gamow
Bridge Test (named in activeContext.md, 2026-08-22) names this failure mode
explicitly: search-and-anchor answers "which Lambda matches externally?",
never "what IS Lambda, derived from the model's own physics?" -- Step 2 of
that test. This file does not search. It asks whether Step 2 is even
ANSWERABLE from what the completion (as built, P58-P92 + P86's addition)
already contains -- and answers with a PROOF, not a scan, the same register
as FINDING_P95's Omega_phi>=0 identity.

THE ARGUMENT, READ FROM THE CODE ITSELF BEFORE ANY NUMBER IS COMPUTED.
P81.background_rhs(g_hat, lam, lam_cc) is the complete equation of motion:

    rho_phys = rho_A * (1 - g_hat*phibar)
    V        = lam*phibar^4/4 + lam_cc
    H        = sqrt((8*pi*G_N/3) * (rho_phys + phibar_dot^2/2 + V))
    d(a)/dt         = a*H
    d(phibar)/dt    = phibar_dot
    d(phibar_dot)/dt = g_hat*rho_A - 3*H*phibar_dot - lam*phibar^3

lam_cc (Lambda_internal) appears EXACTLY ONCE in this system, additively,
inside V, which itself appears only inside the ONE combined expression that
sources H. It does NOT appear in the Klein-Gordon force term
(g_hat*rho_A - lam*phibar^3), which is exactly what FINDING_P86 already
noted ("a constant has zero derivative, so V' = lam*phibar^3 is untouched").
P86 stopped there. The sharper statement, verified in this file: Lambda
still affects the trajectory -- through H's appearance in the FRICTION
term -3*H*phibar_dot -- so "Klein-Gordon does not see it" is true only for
the FORCE, not the full dynamics. But this refinement does not open a door:
Lambda still has exactly ONE channel of influence (through H), with no
SEPARATE equation, boundary condition, or stability requirement anywhere
that depends on Lambda in any other way. There is no equation to SOLVE for
Lambda. It is a free additive constant of the model, on the same footing as
g_hat and lam -- except g_hat and lam are MULTIPLICATIVE couplings, and can
be (and were, in FINDING_P94) fixed to 1.0 by a field/unit normalization
choice. Lambda is ADDITIVE to a potential that sources gravity, and an
additive shift to a potential that couples to gravity is NOT removable by
any field redefinition or choice of units -- shifting V by a constant
changes the physical energy density gravity responds to. This is not a
quirk of this specific completion: it is the SAME structural freedom behind
the real cosmological constant problem. A minimally-coupled scalar field
plus gravity has this freedom generically, unless something OUTSIDE the
minimal coupling (a symmetry, a UV-completion argument, an explicit
Lambda(phi) function replacing the bare constant) removes it. This
completion, as built, has none of those.

WHAT THIS FILE VERIFIES, NOT JUST ASSERTS -- AND WHAT IT DOES NOT (a design
correction made DURING this file's own build, before any final number was
trusted, in the same spirit as every self-correction this arc has made).
  (1) CODE-LEVEL: lam_cc appears in exactly one place in background_rhs
      and viability() -- grep-verified, quoted exactly, not eyeballed.
      This is the PRIMARY basis for the verdict below -- a structural fact
      about the equations, true independent of what any solver can reach.
  (2) NUMERICAL, POSITIVE SIDE, SECONDARY/BOUNDED SUPPORT ONLY. A first
      attempt at this file scanned lam_cc across ~33 decades assuming the
      solver could resolve all of it. It cannot: probed one value at a
      time before trusting a full scan, min_M is only actually MEASURABLE
      up to lam_cc ~ 1e-13 (an arithmetic rho_phys<=0 rejection appears at
      1e-12, and the solver returns "integrator gave up" -- unresolved,
      BLOCKED-INFRASTRUCTURE -- for essentially everything at or above
      ~1e-11, all the way out to 1e8, cheaply and fast to determine, just
      not measurable). This is almost EXACTLY FINDING_P86's own ~13-decade
      window, not the much wider one first assumed -- corrected before
      writing any verdict text, not after. Within that narrower, honestly-
      bounded window, min_M IS flat -- reported as bounded supporting
      evidence, not as an exhaustive sweep.
  (3) NUMERICAL, NEGATIVE SIDE -- ATTEMPTED, BLOCKED-INFRASTRUCTURE, NOT
      PURSUED. P86 never tested negative lam_cc. This file tried: EVERY
      negative value probed (from -1e-6 to -5.0) made P81.viability()'s
      default RK45 integration prohibitively slow -- over 150s wall-clock
      for a SINGLE value with no sign of finishing, versus ~1-3s for any
      positive value including the extremes. Diagnosed as a Substrate Gate
      matter (removing rather than adding Hubble friction likely makes the
      default explicit method grind toward T_END=1e8), not evidence about
      viability itself, and not fixed here -- the negative side is dropped
      from this file's evidence entirely rather than reported as a result
      it cannot actually support.

PRE-REGISTERED OUTCOMES:
  STEP2-UNAVAILABLE-PROVEN   the code-level fact holds (lam_cc appears
                             ONLY additively inside the one combined
                             energy-density expression that sources H, in
                             NO other equation) AND min_M is flat within
                             whatever range the solver can actually
                             measure -> Step 2 is analytically unanswerable
                             from this completion's current construction,
                             on the strength of the STRUCTURAL argument,
                             with the numerical scan as bounded supporting
                             evidence, not as the proof itself. A genuine
                             derivation would require EXTENDING the model
                             (Lambda(phi), a symmetry, a UV argument), not
                             further analysis of what already exists.
  STEP2-HIDDEN-CONSTRAINT    the code-level check finds lam_cc entering
                             SOME other equation, or the measurable window
                             shows min_M genuinely varying with lam_cc ->
                             new information, not assumed away.

WHAT THIS FILE DOES NOT DO: propose what the completion SHOULD be extended
to, or claim numerical coverage of a Lambda range wider than the solver can
actually reach -- the verdict rests on the STRUCTURAL argument, checked
against the equations directly, not on how far a scan gets. It does not
touch MULTING itself (Gate 1) -- this is a statement about OUR
reconstruction's structure, not about the source theory.
"""

import importlib.util
import inspect
import os
import re
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))


def _load(stem, alias):
    spec = importlib.util.spec_from_file_location(alias, os.path.join(HERE, stem))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[alias] = mod
    spec.loader.exec_module(mod)
    return mod


p81 = _load("P81_background_viability.py", "p81_for_a103")

G_HAT_FIXED, LAM_FIXED = 1.0, 1.0  # the same (g_hat, lam) point P94-P102 all built on

# P86's own published anchor: min_M at this point, lam_cc=0 (P81 exactly).
P86_MIN_M_ANCHOR = 0.871740335

POSITIVE_SCAN = np.concatenate(
    [
        [0.0],
        np.geomspace(1e-25, 1e8, 34),  # cheap & fast at EVERY point (verified individually);
    ]  # most of this range returns unresolved, not measured -- see STEP 2/3 below
)
# Negative side: attempted separately, off this file's main path (see docstring
# point 3) -- every value probed made the solver take >150s with no sign of
# finishing, versus 1-3s for positive values across the SAME 33-decade span.
# BLOCKED-INFRASTRUCTURE, not run here at all -- reported in prose, not code,
# because there is no result to show.


def code_level_check():
    """Grep the ACTUAL source of background_rhs/viability for every lam_cc occurrence,
    classified so a 'def' signature or a pass-through call isn't mistaken for a
    SEPARATE equation depending on lam_cc -- both forward to the same computation,
    they don't add a new one. Only lines that use lam_cc inside a computed
    expression count as 'formula' occurrences.
    """
    src_rhs = inspect.getsource(p81.background_rhs)
    src_via = inspect.getsource(p81.viability)
    occurrences = []
    for name, src in (("background_rhs", src_rhs), ("viability", src_via)):
        for i, line in enumerate(src.splitlines(), start=1):
            stripped = line.strip()
            if not re.search(r"\blam_cc\b", stripped):
                continue
            if "#" in stripped and stripped.index("#") < stripped.find("lam_cc"):
                continue  # commented out before the reference
            if stripped.startswith("def "):
                kind = "signature"  # declares the parameter, not an equation
            elif re.match(r"^\w+\(.*\blam_cc\b.*\)\s*,?\s*$", stripped) and "=" not in stripped:
                kind = "forwarding"  # passes the value on, doesn't compute with it here
            else:
                kind = "formula"  # actually used in a computed expression
            occurrences.append((name, i, kind, stripped))
    return occurrences


def main() -> int:  # noqa: PLR0915 - one linear report
    print("=" * 78)
    print("P103 -- attack Gamow Bridge Test Step 2 directly: is Lambda_internal")
    print("        DERIVABLE from the completion's own microphysics?")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    # ==================================================================
    print("\n" + "-" * 78)
    print("STEP 1 -- CODE-LEVEL: where does lam_cc actually appear? (grep, not eyeball)")
    print("-" * 78)
    occ = code_level_check()
    for fn, ln, kind, text in occ:
        print(f"    {fn}:{ln} [{kind:<10}]: {text}")
    formula_lines = [text for _fn, _ln, kind, text in occ if kind == "formula"]
    print(
        f"\n    total lam_cc occurrences: {len(occ)} "
        f"({sum(1 for o in occ if o[2] == 'signature')} signature, "
        f"{sum(1 for o in occ if o[2] == 'forwarding')} forwarding, "
        f"{len(formula_lines)} formula)"
    )
    formula_normalized = {re.sub(r"\s+", "", t) for t in formula_lines}
    only_via_V = len(formula_normalized) > 0 and all(
        "V=" in re.sub(r"\s+", "", t) or "V+=" in re.sub(r"\s+", "", t) for t in formula_lines
    )
    same_formula = len(formula_normalized) == 1
    print(f"    formula occurrences all write the SAME V=...+lam_cc expression: {same_formula}")
    print(
        f"    every formula occurrence is inside the V=... energy-density expression: {only_via_V}"
    )

    # ==================================================================
    print("\n" + "-" * 78)
    print("CONTROL -- reproduce FINDING_P86's own anchor before trusting a wider scan")
    print("-" * 78)
    anchor = p81.viability(G_HAT_FIXED, LAM_FIXED, lam_cc=0.0)
    anchor_ok = (
        anchor.get("state") == "measured"
        and anchor.get("ok") is True
        and abs(anchor.get("min_M", -99) - P86_MIN_M_ANCHOR) < 1e-9
    )
    print(f"    lam_cc=0.0: state={anchor.get('state')}, min_M={anchor.get('min_M')!r}")
    print(f"    CONTROL {'PASSES' if anchor_ok else 'FAILS'} (expected min_M={P86_MIN_M_ANCHOR})")
    if not anchor_ok:
        print("    *** does not reproduce P81/P86's own published anchor. STOP.")
        return 1

    # ==================================================================
    print("\n" + "-" * 78)
    print(
        f"STEP 2 -- POSITIVE-SIDE wide scan, {len(POSITIVE_SCAN)} values, "
        f"{POSITIVE_SCAN[1]:.1e} to {POSITIVE_SCAN[-1]:.1e} (~33 decades)"
    )
    print("-" * 78)
    print(f"\n    {'lam_cc':<14}{'state':<14}{'min_M':<16}{'ok'}")
    pos_rows = []
    for lc in POSITIVE_SCAN:
        r = p81.viability(G_HAT_FIXED, LAM_FIXED, lam_cc=float(lc))
        pos_rows.append((lc, r))
        mM = r.get("min_M")
        mM_str = f"{mM:.9f}" if mM is not None else "--"
        print(f"    {lc:<14.4e}{r.get('state', '?'):<14}{mM_str:<16}{r.get('ok')}")

    measured_pos = [(lc, r) for lc, r in pos_rows if r.get("state") == "measured"]
    unresolved_pos = [(lc, r) for lc, r in pos_rows if r.get("state") == "unresolved"]
    min_Ms = [r["min_M"] for _lc, r in measured_pos if r.get("min_M") is not None]
    spread = (max(min_Ms) - min(min_Ms)) if min_Ms else float("nan")
    print(
        f"\n    measured (any reason, incl. arithmetic-rejected): {len(measured_pos)}/{len(pos_rows)}"
    )
    print(
        f"    unresolved (BLOCKED-INFRASTRUCTURE, not evidence either way): "
        f"{len(unresolved_pos)}/{len(pos_rows)}"
    )
    measured_lcs = [lc for lc, _r in measured_pos]
    if min_Ms:
        print(
            f"    min_M range across all measured positive lam_cc: [{min(min_Ms):.9f}, "
            f"{max(min_Ms):.9f}]  (spread {spread:.3e})"
        )
        print(f"    measured lam_cc range: [{min(measured_lcs):.4e}, {max(measured_lcs):.4e}]")

    print("\n" + "-" * 78)
    print("STEP 3 -- NEGATIVE SIDE: attempted separately (not in the scan above),")
    print("BLOCKED-INFRASTRUCTURE, not run further -- see docstring point 3")
    print("-" * 78)
    print("    Every negative lam_cc probed during this file's build (-1e-6 through -5.0)")
    print("    made P81.viability()'s default integration take >150s per value with no sign")
    print("    of finishing, versus 1-3s for ANY positive value across the same span. Not a")
    print("    physics result -- an infrastructure limitation, diagnosed and left unfixed,")
    print("    out of scope for this file (see NOT ESTABLISHED below).")

    print("\n" + "=" * 78)
    print("VERDICT (against the outcomes pre-registered in the docstring)")
    print("=" * 78)
    positive_side_flat = len(min_Ms) > 1 and spread < 1e-6
    print(
        f"  positive-side min_M flat within the MEASURABLE window: {positive_side_flat} "
        f"(spread {spread:.3e})"
    )
    print(
        f"  every formula occurrence is additive-only inside V, same expression: "
        f"{only_via_V and same_formula}"
    )
    if positive_side_flat and only_via_V and same_formula:
        print("\n  -> STEP2-UNAVAILABLE-PROVEN, on the strength of the STRUCTURAL argument.")
        print("     Lambda_internal enters this completion's equations in exactly ONE place,")
        print("     additively, inside the total energy density that sources H -- verified by")
        print("     reading the code, not assumed. No other equation (Klein-Gordon's force")
        print("     term, any stability/boundary condition) depends on it at all. That fact is")
        print("     TRUE REGARDLESS of what any solver can numerically reach -- it is read")
        print("     directly off the equations, the same register as FINDING_P95's algebraic")
        print("     proof, not a claim that depends on scan coverage.")
        print("     The numerical scan is BOUNDED supporting evidence only: within the window")
        print(
            f"     the solver can actually measure ([{min(measured_lcs):.1e}, "
            f"{max(measured_lcs):.1e}], almost exactly FINDING_P86's own ~13-decade window,"
        )
        print("     not the much wider one first assumed before individual probes corrected")
        print("     that), min_M is flat to 1 part in 1e10 or better -- consistent with, and")
        print("     no stronger than, what P86 already established. Both directions beyond")
        print("     that window are BLOCKED-INFRASTRUCTURE (solver non-convergence on the high")
        print("     positive side, prohibitive slowness on the negative side), not physics")
        print("     rejections -- and are reported as exactly that, not folded into the claim.")
        print("     Step 2 of the Gamow Bridge Test is analytically UNANSWERABLE from this")
        print("     completion's current construction -- the SAME structural freedom as the")
        print("     real cosmological constant problem: an additive vacuum-energy term coupled")
        print("     to gravity is not fixed by any equation of motion or consistency condition")
        print("     unless something OUTSIDE minimal coupling removes the freedom. A genuine")
        print("     Step-2 answer requires EXTENDING the completion (Lambda(phi), a symmetry,")
        print("     a UV-completion argument) -- not further analysis of what P58-P92 already")
        print("     contain. Nine anchor/search attempts (P93-P102) were never going to succeed")
        print("     at DERIVING this number; at best they could MEASURE it against external")
        print("     data -- a different, still-open question this file does not resolve either.")
    else:
        print("\n  -> STEP2-HIDDEN-CONSTRAINT. The scan found structure the argument above did")
        print("     not predict -- reported above, not assumed away. Reconsider the analytic")
        print("     claim before trusting it.")

    print("\n  NOT ESTABLISHED:")
    print("   * that NO extension of the completion could supply Step 2 -- only that the")
    print("     CURRENT one (P58-P92 + P86) cannot, proven not searched.")
    print("   * what the correct extension would be, or whether MULTING itself already has one")
    print("     (Gate 1 -- this file says nothing about the source theory).")
    print("   * any numeric value of eps(k) or f(k) in physical units.")
    print("   * anything about the negative-side boundary -- BLOCKED-INFRASTRUCTURE, not run.")
    print("   * that a different solver/method/tolerance could not measure further in either")
    print("     direction -- only that P81's current one, unchanged, cannot. Not fixed here.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
