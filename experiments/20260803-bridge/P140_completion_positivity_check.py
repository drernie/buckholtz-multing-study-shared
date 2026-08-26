"""P140 -- does the linear completion M(phi)=1-g*phi stay physical
(M>0) on the trajectories this campaign has ALREADY computed?

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

WHY THIS FILE. User-directed self-search option for bottleneck 2 (unique
completion), run in parallel with the user's own IC inverse-problem
synthesis for bottleneck 4 (docs/148) -- NOT part of that workstream,
does not touch it. The cheapest self-directed check available: a
theoretical selection criterion between the two candidate completions
that needs no new physics input, only re-inspection of trajectories
this project has already integrated many times over (P74-P139).

THE ARGUMENT. M(phi) multiplies the matter density in this campaign's
own coupling (rho_phys = rho_A * M(phi)) -- a negative M means a
NEGATIVE effective matter density, unphysical. The two candidates:
  linear:      M(phi) = 1 - g*phi        -- negative for phi > 1/g
  exponential: M(phi) = exp(-g*phi)      -- positive for ALL phi, by
                                             construction (exp is never
                                             negative)
So the exponential completion is automatically positivity-safe
everywhere; the linear one is only safe on a bounded range. If the
trajectories this project actually explores stay inside phi<1/g, this
argument is moot (both completions equally physical on the range that
matters). If they exceed it, the linear completion is ALREADY excluded
by this project's own data, without needing any new mechanism, external
fact, or literature search.

PRE-REGISTERED OUTCOMES (before any number is computed):
  LINEAR-EXCLUDED    max(phi_bar) over the trajectories already explored
      this campaign (g_hat=1, k in {1,2,3,10}, lever in {0.1,0.5,1,2},
      both g_hat=1 and g_hat=0 branches) exceeds 1/g_hat=1.0 at some
      point -- the linear completion goes unphysical (M<0) on ground this
      project has already computed, independent of any new test.
  BOTH-SAFE          max(phi_bar) stays below 1/g_hat=1.0 everywhere
      checked -- positivity does not discriminate the two completions on
      the range this campaign actually uses; the argument is moot here,
      though it remains a general theoretical asymmetry (exponential is
      positivity-safe for ALL phi, linear is not, regardless of whether
      THIS project's own trajectories happen to stay inside the safe
      window).

CONTROLS:
  POSITIVE CONTROL: g_hat=0 branch has M=1 identically for BOTH
      completions (no phi-dependence at all) -- max(M)=min(M)=1 exactly,
      confirms the check itself is not spuriously flagging anything.
  REUSE, NOT REDERIVE: run()/mass_law() imported directly from P79's own
      module (itself importing P78's).

WHAT THIS FILE DOES NOT DO: claim positivity violation (if found) PROVES
the linear completion is wrong -- only that it becomes unphysical WITHIN
the specific range this project's own reconstruction explores; a
different normalization/parameter choice elsewhere in parameter space
could avoid it (named, not investigated). Extend the trajectory range
beyond what P74-P139 already integrated. Build a new observable. Vary
Lambda, G_N, or C_MATTER. Quote any k[h/Mpc]. Touch MULTING itself
(Gate 1) -- both completions are this project's own construction.
"""

import importlib.util
import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_sp = importlib.util.spec_from_file_location("p79_ref", os.path.join(_HERE, "P79_low_k_window.py"))
p79 = importlib.util.module_from_spec(_sp)
sys.modules["p79_ref"] = p79
_sp.loader.exec_module(p79)

run, PHIDOT, LAM, GH = p79.run, p79.PHIDOT, p79.LAM, p79.GH
p78 = sys.modules["p78_ref"]
mass_law, T_END = p78.mass_law, p78.T_END

KS = (1.0, 2.0, 3.0, 10.0)
LEVERS = (0.1, 0.5, 1.0, 2.0)
LAWS = ("linear", "exponential")
T_SAMPLE = np.geomspace(1.0, T_END, 2000)


def max_phi_and_M(name, gh, kk, rtol=1e-10, **ic):
    s = run(name, gh, LAM, kk, rtol=rtol, **ic) if ic else run(name, gh, LAM, kk, rtol=rtol)
    M, _, _ = mass_law(name, gh)
    pb_vals = np.array([s.sol(t)[1] for t in T_SAMPLE])
    M_vals = np.array([M(pb) for pb in pb_vals])
    return float(np.max(pb_vals)), float(np.min(M_vals))


def main() -> int:
    print("=" * 78)
    print("P140 -- does the linear completion stay physical (M>0) on this")
    print("campaign's own already-explored trajectories?")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    # ------------------------------------------------------------ control
    print("\n" + "-" * 78)
    print("POSITIVE CONTROL -- g_hat=0 branch: M=1 identically for BOTH laws")
    print("-" * 78)
    control_ok = True
    for name in LAWS:
        max_pb, min_M = max_phi_and_M(name, 0.0, 1.0)
        ok = abs(min_M - 1.0) < 1e-12 and abs(max_pb) >= 0
        control_ok &= ok
        print(
            f"    {name:<12} g_hat=0: max(phi)={max_pb:.6e}  min(M)={min_M:.12f}  "
            f"{'OK' if ok else 'FAIL'}"
        )
    if not control_ok:
        print("\n  *** control failed -- the check itself is not trustworthy. STOP.")
        return 1
    print("\n    control PASSES -- proceeding to the g_hat=1 branch.")

    # -------------------------------------------------------------- main
    print("\n" + "-" * 78)
    print("MAIN SCAN -- g_hat=1, all (k, lever) combinations already used P78-P139")
    print("-" * 78)
    print(f"\n    {'law':<12}{'k':<6}{'lever':<8}{'max(phi_bar)':<16}{'min(M)':<14}{'M<0?'}")
    worst = {"linear": (-1e9, None), "exponential": (-1e9, None)}
    any_negative = {"linear": False, "exponential": False}
    for name in LAWS:
        for kk in KS:
            for f in LEVERS:
                max_pb, min_M = max_phi_and_M(name, GH, kk, phidot0=f * PHIDOT)
                neg = min_M < 0
                any_negative[name] |= neg
                if max_pb > worst[name][0]:
                    worst[name] = (max_pb, (kk, f, min_M))
                print(
                    f"    {name:<12}{kk:<6}{f:<8}{max_pb:<16.6e}{min_M:<14.6e}"
                    f"{'YES' if neg else 'no'}"
                )

    # ------------------------------------------------------------ verdict
    print("\n" + "=" * 78)
    print("VERDICT (against the outcomes pre-registered in the docstring)")
    print("=" * 78)
    print(
        f"\n    linear:      worst max(phi_bar) = {worst['linear'][0]:.6e}  "
        f"(at k,lever,min(M) = {worst['linear'][1]}); any M<0? {any_negative['linear']}"
    )
    print(
        f"    exponential: worst max(phi_bar) = {worst['exponential'][0]:.6e}  "
        f"(at k,lever,min(M) = {worst['exponential'][1]}); any M<0? {any_negative['exponential']}"
    )
    print(f"\n    threshold for linear unphysicality: phi_bar > 1/g_hat = {1.0 / GH:.6e}")

    if any_negative["linear"]:
        print("\n  -> LINEAR-EXCLUDED. The linear completion M=1-g*phi goes negative")
        print("     (unphysical: implies a negative effective matter density) on")
        print("     trajectories this campaign has already computed -- excluded on")
        print("     this project's own existing ground, no new mechanism or")
        print("     external fact needed. The exponential completion has NO such")
        print("     violation anywhere (positive by construction, confirmed above).")
    else:
        print("\n  -> BOTH-SAFE. max(phi_bar) stays below 1/g_hat everywhere checked --")
        print("     positivity does not discriminate the two completions on the")
        print("     range this campaign actually explores. The general theoretical")
        print("     asymmetry (exponential positivity-safe for ALL phi; linear only")
        print("     on a bounded range) still stands, but is moot for this project's")
        print("     own trajectories as currently computed.")

    print("\n  NOT ESTABLISHED regardless of outcome:")
    print("   * that a positivity violation (if found) proves the linear completion")
    print("     is wrong in general -- only unphysical on the specific range this")
    print("     project's own reconstruction explores.")
    print("   * anything about a wider trajectory range than P74-P139 already used.")
    print("   * anything observational -- internal units, NO_BRIDGE_FITTING in force")
    print("   * anything about MULTING itself (Gate 1): both completions are OURS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
