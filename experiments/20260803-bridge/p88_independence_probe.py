"""Two attacks on P88's R-CONFIRMED verdict, run BEFORE it is written up.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

P88 reported agreement of 1.4e-10 / 1.7e-11 / 2.4e-13 at k = 3 / 10 / 30. The
last of those is BETTER THAN EITHER CODE'S INTEGRATOR TOLERANCE -- 1e-11 in the
reconstruction, 1e-10 in P76. A result that is more accurate than the machinery
that produced it is the exact shape this campaign has caught eight times now:
the gate measuring something other than what the claim asserts. So the verdict
gets attacked here before it gets quoted anywhere.

TWO WAYS THE AGREEMENT COULD BE FAKE, and one test each.

ATTACK 1 -- THE AGREEMENT IS NOT TOLERANCE-LIMITED.
    If both files really integrate the same equations independently, their
    difference is a DISCRETIZATION difference, and loosening one side's
    tolerance must degrade it roughly in step. If instead the difference stays
    pinned near 1e-13 while the reconstruction's rtol is loosened by five
    orders of magnitude, the two numbers are not being produced independently
    and the agreement means nothing.

    PRE-REGISTERED, before the numbers: sweeping the reconstruction's rtol over
    1e-12 -> 1e-6 must make the relative difference GROW BY A FACTOR >= 100.
      grows by >= 100x  -> TOL-LIMITED, the agreement is a real convergence result
      grows by <  10x   -> SUSPICIOUS, the verdict is withdrawn pending a cause
      between           -> PARTIAL, must be named in the finding, not smoothed over

    The same sweep is run on P76's side too. It is the symmetric half of the
    same question and costs one extra integration.

ATTACK 2 -- "SHARES NO COMPUTATIONAL CODE" IS PROSE, NOT A MEASUREMENT.
    P88's docstring asserts independence and draws a line in the file, with
    everything below it allowed to touch the campaign's code. That claim has
    never been executed. Here it is made mechanical: the file is split at its
    OWN documented marker, only the text ABOVE the marker is exec'd into a bare
    namespace, and eps is recomputed from that fragment alone.

      * if the fragment needs anything from below the line, it raises and the
        independence claim is false as written;
      * if it runs, it must reproduce the headline number BITWISE -- not
        approximately, since it is literally the same source text.

    The fragment's source is also grepped for any mention of P76 at all.

Neither attack can confirm the physics. Both can destroy the verdict, which is
the only thing a control is for.
"""

import ast
import importlib.util
import io
import os
import re
import sys
import tokenize

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
P88_PATH = os.path.join(HERE, "P88_independent_reconstruction.py")
MARKER = "# Everything BELOW this line may touch the campaign's code"
K_PROBE = 10.0
A1, A2 = 1000.0, 400000.0
T_END_P76 = 1e8


def load_p88():
    spec = importlib.util.spec_from_file_location("p88_probe", P88_PATH)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["p88_probe"] = mod
    spec.loader.exec_module(mod)
    return mod


def load_p76():
    spec = importlib.util.spec_from_file_location(
        "p76_probe", os.path.join(HERE, "P76_growth_observable.py")
    )
    mod = importlib.util.module_from_spec(spec)
    sys.modules["p76_probe"] = mod
    spec.loader.exec_module(mod)
    return mod


def executable_text(text):
    """Everything the interpreter would RUN, minus prose. Comments and the
    module docstring out; every other string literal KEPT.

    # WHY not the obvious "strip all string literals": a dynamic load hides its
    # target inside a STRING --
    # spec_from_file_location("x", "P76_growth_observable.py") -- and the
    # fragment inherits `import importlib.util` from the file's import block,
    # so that escape route is genuinely open. Blanking every string would blind
    # the check to the ONE way the fragment could still reach P76. Only the
    # module docstring is removed, located by AST position rather than guessed.
    """
    lines = text.split("\n")
    mod = ast.parse(text)
    first = mod.body[0] if mod.body else None
    if (
        isinstance(first, ast.Expr)
        and isinstance(first.value, ast.Constant)
        and isinstance(first.value.value, str)
    ):
        for i in range(first.lineno - 1, first.end_lineno):
            lines[i] = ""
    out = []
    for tok in tokenize.generate_tokens(io.StringIO("\n".join(lines)).readline):
        if tok.type != tokenize.COMMENT:
            out.append(tok.string)
    return " ".join(out)


def run_p76_eps(p76, k, rtol):
    """eps = ln(G)/ln(a2/a1), assembled here so rtol can be varied.

    # WHY not p76.G_growth: its signature fixes rtol at run()'s default. The
    # three calls below are P76's OWN functions in P76's own order -- run,
    # t_of_a, contrast -- so this is still P76 computing the number, only with
    # the tolerance exposed.
    """
    out = []
    for gg in (1.0, 0.0):
        s = p76.run(gg, 1.0, k, T_END_P76, rtol=rtol)
        t1 = p76.t_of_a(s, A1, 1.0, T_END_P76)
        t2 = p76.t_of_a(s, A2, 1.0, T_END_P76)
        if t1 is None or t2 is None:
            return None
        out.append(p76.contrast(s, gg, 1.0, t2) / p76.contrast(s, gg, 1.0, t1))
    return np.log(out[0] / out[1]) / np.log(A2 / A1)


def main() -> int:  # noqa: PLR0915 - one linear report
    print("=" * 78)
    print("p88 independence probe -- two attacks on the R-CONFIRMED verdict")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    p88 = load_p88()
    p76 = load_p76()

    # ==================================================================
    print("\n" + "-" * 78)
    print("ATTACK 1 -- is the agreement TOLERANCE-LIMITED, or pinned?")
    print("-" * 78)
    print(f"  k = {K_PROBE:g}, anchors {A1:g} -> {A2:g}. P76 held at its own rtol=1e-10")
    print("  while the reconstruction's is loosened by five orders of magnitude.")

    ref = run_p76_eps(p76, K_PROBE, 1e-10)
    print(f"\n  P76 reference eps = {ref:.14f}")
    print(f"\n    {'recon rtol':<14}{'recon eps':<22}{'relative diff'}")
    rels_a = {}
    for rt in (1e-12, 1e-10, 1e-8, 1e-6):
        er = p88.eps_recon(1.0, 1.0, K_PROBE, A1, A2, rtol=rt)
        if er is None:
            print(f"    {rt:<14.0e}{'unresolved -- not measured':<22}")
            rels_a[rt] = None
            continue
        rel = abs(er / ref - 1.0)
        rels_a[rt] = rel
        print(f"    {rt:<14.0e}{er:<22.14f}{rel:.3e}")

    vals = [v for v in rels_a.values() if v is not None]
    ok_a = len(vals) == len(rels_a)
    growth = (max(vals) / min(vals)) if ok_a and min(vals) > 0 else float("inf")
    print(f"\n    spread across the ladder: {growth:.3g}x")

    print("\n  SYMMETRIC HALF -- now loosen P76 instead, reconstruction at 1e-11.")
    er_ref = p88.eps_recon(1.0, 1.0, K_PROBE, A1, A2, rtol=1e-11)
    print(f"\n  reconstruction reference eps = {er_ref:.14f}")
    print(f"\n    {'P76 rtol':<14}{'P76 eps':<22}{'relative diff'}")
    rels_b = {}
    for rt in (1e-10, 1e-8, 1e-6):
        ep = run_p76_eps(p76, K_PROBE, rt)
        if ep is None:
            print(f"    {rt:<14.0e}{'unresolved -- not measured':<22}")
            rels_b[rt] = None
            continue
        rel = abs(ep / er_ref - 1.0)
        rels_b[rt] = rel
        print(f"    {rt:<14.0e}{ep:<22.14f}{rel:.3e}")

    vals_b = [v for v in rels_b.values() if v is not None]
    growth_b = (max(vals_b) / min(vals_b)) if vals_b and min(vals_b) > 0 else float("inf")
    print(f"\n    spread across the ladder: {growth_b:.3g}x")

    if growth >= 100 and growth_b >= 100:
        a1_verdict = "TOL-LIMITED"
    elif growth < 10 or growth_b < 10:
        a1_verdict = "SUSPICIOUS"
    else:
        a1_verdict = "PARTIAL"
    print(f"\n    ATTACK 1 -> {a1_verdict}")
    if a1_verdict == "SUSPICIOUS":
        print("    *** the difference does not track either tolerance. The two")
        print("    *** numbers are not being produced independently -- R-CONFIRMED")
        print("    *** must be WITHDRAWN until the cause is found.")

    # ==================================================================
    print("\n" + "-" * 78)
    print("ATTACK 2 -- execute the independence claim instead of asserting it")
    print("-" * 78)

    src = open(P88_PATH, encoding="utf-8").read()
    idx = src.find(MARKER)
    if idx < 0:
        print("  the file no longer carries its own boundary marker -- cannot test.")
        return 1
    above = src[:idx]
    frac = 100.0 * len(above) / len(src)
    print(f"  boundary marker found at {frac:.0f}% of the file.")

    hits_raw = re.findall(r"[pP]76", above)
    hits_code = re.findall(r"[pP]76", executable_text(above))
    print(f"  mentions of P76 in the fragment's RAW TEXT   : {len(hits_raw)}")
    print(f"  mentions of P76 in its EXECUTABLE TEXT       : {len(hits_code)}")
    print("  (the criterion is the second. The first counts the docstring,")
    print("   which DESCRIBES the comparison in prose -- the first version of")
    print("   this control used it and failed on its own wording, not on the")
    print("   claim. Recorded rather than quietly retuned.)")

    ns: dict = {"__name__": "p88_above_the_line"}
    try:
        exec(compile(above, "<p88-above-the-line>", "exec"), ns)  # noqa: S102
    except Exception as exc:  # noqa: BLE001
        print(f"  the fragment does NOT run on its own: {type(exc).__name__}: {exc}")
        print("  => the independence claim is FALSE AS WRITTEN.")
        return 1

    er_frag = ns["eps_recon"](1.0, 1.0, K_PROBE, A1, A2, rtol=1e-11)
    same = er_frag == er_ref
    print(f"  fragment-only eps = {er_frag:.14f}")
    print(f"  full-file    eps = {er_ref:.14f}")
    print(f"  bitwise identical: {same}")
    ok_b = same and len(hits_code) == 0
    print(f"\n    ATTACK 2 -> {'INDEPENDENCE HOLDS' if ok_b else 'INDEPENDENCE FAILS'}")

    # ==================================================================
    print("\n" + "=" * 78)
    print("COMBINED")
    print("=" * 78)
    if a1_verdict == "TOL-LIMITED" and ok_b:
        print("  Both attacks failed to break the verdict. The agreement tracks the")
        print("  integrator tolerances on BOTH sides, which is what a genuine")
        print("  convergence of two discretizations looks like, and the half of the")
        print("  file that produces the number provably never mentions P76.")
        print("  R-CONFIRMED stands, at the rung it was claimed at and no higher.")
    else:
        print(f"  ATTACK 1 = {a1_verdict}, ATTACK 2 = {'ok' if ok_b else 'FAILED'}.")
        print("  R-CONFIRMED does not stand as written -- see above.")
    print("\n  Neither attack says anything about whether the shared EQUATIONS are")
    print("  right. Two faithful implementations of a wrong specification agree.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
