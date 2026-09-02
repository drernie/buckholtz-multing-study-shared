"""P188 -- Cross-check: does this project's own _v82_shared_physics.py
(used across P177-P185) implement the accretion-correction force term
F_accretion(z), and does it match TJB's own canonical multing_core.py
(Zenodo 21204955 supplemental archive) exactly?

Closes the action item flagged in
data/source_material/zenodo_21204955_supplemental/INDEX.md
("not yet cross-checked... if absent, the project's own v82-degeneracy
numerics were computed on an incomplete force law") -- that flag was an
unverified assumption at the time it was written; this script verifies
it directly rather than leaving it as an open concern.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

import importlib.util


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


ours = load("experiments/20260803-bridge/_v82_shared_physics.py", "ours")
theirs = load(
    "data/source_material/zenodo_21204955_supplemental/code/multing_core.py",
    "theirs",
)

ZS = [0.0, 0.0233, 0.07, 0.5, 1.07, 1.965, 2.33, 5.0]
B1_SPOTLIGHTED, B2_SPOTLIGHTED = 1.4335e10, 7.8067e17

CONSTANTS = [
    "f_merge",
    "f_coh",
    "M0_kg",
    "d0_m",
    "T0_keV",
    "mu_mol",
    "m_proton",
    "T_piv_keV",
    "Mgas_piv_kg",
    "z_piv",
    "B_real",
    "C_real",
    "H0_planck_si",
    "G",
    "c",
    "Om_planck",
    "OL_planck",
]


def main():
    print("=== F_accretion(z): ours vs theirs ===")
    max_rel_facc = 0.0
    for z in ZS:
        fo, ft = ours.F_accretion(z), theirs.F_accretion(z)
        rel = abs(fo - ft) / abs(ft)
        max_rel_facc = max(max_rel_facc, rel)
        print(f"z={z:8.4f}  ours={fo:.10e}  theirs={ft:.10e}  rel={rel:.3e}")
    print(f"max relative diff: {max_rel_facc:.3e}\n")

    print("=== full addot_over_a (spotlighted b1,b2): ours(eps=0) vs theirs ===")
    max_rel_addot = 0.0
    for z in ZS:
        ao = ours.addot_over_a_eps(z, B1_SPOTLIGHTED, B2_SPOTLIGHTED, eps=0.0)
        at = theirs.addot_over_a(z, B1_SPOTLIGHTED, B2_SPOTLIGHTED)
        rel = abs(ao - at) / abs(at)
        max_rel_addot = max(max_rel_addot, rel)
        print(f"z={z:8.4f}  ours={ao:.10e}  theirs={at:.10e}  rel={rel:.3e}")
    print(f"max relative diff: {max_rel_addot:.3e}\n")

    print("=== constant-by-constant comparison ===")
    all_ok = True
    for name in CONSTANTS:
        vo, vt = getattr(ours, name), getattr(theirs, name)
        ok = vo == vt
        all_ok &= ok
        print(f"{name:16} {'OK' if ok else f'DIFFER ours={vo} theirs={vt}'}")

    print()
    verdict = (
        "MATCH -- accretion term present and numerically identical"
        if max_rel_facc == 0.0 and max_rel_addot == 0.0 and all_ok
        else "MISMATCH -- see printed diffs above"
    )
    print(f"VERDICT: {verdict}")


if __name__ == "__main__":
    main()
