# FINDING P151 — Q3b: under Reading B only, MICROSCOPE is silent (~22
# orders below sensitivity), but the Cassini safety margin shrinks from
# docs/118's claimed 14 orders to just ~3

**Date:** 2026-08-26
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 math
(external constraint, per `P148`'s corrected internal-consistency →
observable-mapping → external-constraint order)
**Verdict:** `MICROSCOPE-SILENT-CASSINI-MARGIN-SHRUNK`
**Origin:** `P150`'s own explicit finding — Q3b is attemptable *only*
under Reading B (the one of three defensible readings that lets any
laboratory-scale signal exist at all), and *only* with the
solar-system-scale constraint independently re-checked, since `docs/118`'s
own Cassini-safety conclusion does not survive under Reading B.
**Script:** `P151_fifthforce_reading_b_bound_check.py` (positive control +
2 checks against real, WebSearch-verified external bounds, ruff clean,
does not touch the 881-test suite)
**Scope, stated as prominently as `P150` requires:** every number below
is a bound on *this project's own candidate construction*, under *one of
three* disputed readings of an underspecified textual definition — not a
claim about MULTING's own theory (`NO_AUTHOR_ERROR`).

---

## 1. Method — the actual observable, not `κ` plugged into a bound

Per the user's own explicit correction of the skeptic's original
proposal (`P148` §6): the differential-acceleration observable is
derived from this project's own established two-charge force law
(`docs/125`, `two_charge_completion.py`), not assumed:

```
F_d = G β_d (k_A m_P r_A + k_P m_A r_P)/(c² D³)
```

For a test mass `A` near a source `P` (Earth, for MICROSCOPE; the Sun,
for the solar-system check), the term `k_P m_A r_P` — the source's own
charge, sourced with the source's own lever arm — produces the **same**
acceleration on every test mass (it's linear in `m_A`, so it cancels out
of `F/m_A`) and therefore cancels in any *differential* (composition-
dependent) measurement. Only the test mass's *own* charge term,
`k_A m_P r_A`, survives in a differential comparison — this is what
distinguishes the MICROSCOPE check (§2, differential) from the Cassini
check (§3, absolute force ratio, where the source's own term is exactly
the one that matters).

## 2. Check 1 — MICROSCOPE (Ti vs. Pt)

**Real mission parameters, WebSearch-verified, not recalled from memory:**
test masses are Pt:Rh(90:10, inner) and Ti:Al:V(90:6:4, outer) alloy
cylinders, outer radii `39–69` mm (representative `r_test=50` mm used);
sun-synchronous orbit at `~710` km altitude, mean semi-major axis
`7090` km; result `η(Ti,Pt) = [−1.5±2.3(stat)±1.5(syst)]×10⁻¹⁵` (1σ),
Touboul et al. 2022, *Phys. Rev. Lett.* **129**, 121102.

`k_i/m_i` computed under Reading B (`(3/2)k_BT/(m_{atom,i}c²)`,
`T=300`K): `k_Ti/m_Ti≈8.70×10⁻¹³`, `k_Pt/m_Pt≈2.13×10⁻¹³`, ratio `4.08`
(matches `P150`'s own "~4×" claim). **Positive control:** both values
sit within a factor of a few of the textbook thermal-to-rest-mass-energy
scale `k_BT/(m_{amu}c²)≈2.8×10⁻¹¹` for atomic masses `~50–200` amu — not
an arbitrary number.

```
η_predicted = 2β_d r_test/(c²D) × (k_Ti/m_Ti − k_Pt/m_Pt)
            = 2.06×10⁻³⁷
```

against the observed `η≈1.5×10⁻¹⁵`: **`|η_predicted|/η_bound ≈ 1.4×10⁻²²`
— ~22 orders of magnitude below MICROSCOPE's sensitivity.**

**MICROSCOPE does not constrain this construction — not because the
mapping is invalid (that's `P150`'s separate, already-flagged concern),
but because the predicted effect, even under the one reading that allows
any signal at all, is astronomically smaller than what MICROSCOPE can
detect.**

## 3. Check 2 — solar-system scale (Cassini-type), redone under Reading B

**Corrected in place before this reached the skeptic (own catch, not
the skeptic's):** an early draft of the script used Earth's radius as
the lever arm for this check. The physically correct lever arm is the
**Sun's own radius** — the surviving term is the Sun's own charge
(`k_P m_A r_P`, `P`=Sun, `A`=Earth), matching `docs/118`'s own formula
`F_d/F_m = β_d(k_Sun/M_☉)(R_☉/D)`. Fixed before running against the
skeptic, not after.

`k_Sun/M_☉` under Reading B, applied **consistently** (compactness
proxy `GM_☉/(R_☉c²)`, not `docs/118`'s corona-only sub-component):

```
k_Sun/M_☉ (Reading B) = 2.12×10⁻⁶
k_Sun/M_☉ (docs/118, corona-only) = 3×10⁻¹⁷
ratio = 7.08×10¹⁰   — confirms P150's own flagged ~10-order gap
```

```
F_d/F_m = β_d(k_Sun/M_☉)(R_☉/D) = 1.97×10⁻⁸   (D = 1 AU)
```

Compared against the Cassini bound **`γ−1=(2.1±2.3)×10⁻⁵`** (Bertotti,
Iess & Tortora 2003, *Nature* **425**, 374 — independently WebSearch-
verified, not recalled from memory): `docs/118`'s own framing treats
this `2.3×10⁻⁵` figure as a generic "anomalous force ratio" bound;
**this mapping (a PPN light-bending/Shapiro-delay parameter constraining
a `1/r³` dipole *force* ratio) is itself unverified and inherited
uncritically from `docs/118`, not independently derived here** — flagged
explicitly, not silently reused.

Taking the number at face value regardless: `F_d/F_m / bound ≈ 8.6×10⁻⁴`
— **still below the bound, by ~3.1 orders of magnitude, not the ~5
orders an intermediate (Earth-radius) draft gave, and nowhere near
`docs/118`'s original 14-orders-of-magnitude margin.**

## 4. Verdict

**`MICROSCOPE-SILENT-CASSINI-MARGIN-SHRUNK`** — under Reading B, the one
of three defensible readings this construction can even be tested under:

- MICROSCOPE gives **no constraint at all** on this construction — the
  predicted composition-dependent signal is ~22 orders of magnitude
  below current experimental sensitivity.
- The solar-system-scale margin is real but **far thinner than `docs/118`
  reported** — `~3` orders of magnitude, not `14` — because `docs/118`
  used an internally-inconsistent, ad hoc sub-component (corona energy)
  instead of Reading B's own consistent total-energy prescription. This
  confirms `P150`'s own flagged concern was not merely theoretical.
- The Cassini-bound *mapping itself* (force ratio vs. PPN `γ`) is a
  further layer of unverified construct validity, inherited from
  `docs/118`, not resolved here.

## What this file does NOT establish

1. **Not a claim about MULTING's own viability or falsification** (Gate
   1) — this bounds only this project's own Reading-B reconstruction,
   one of three disputed readings `P150` found, itself only
   `LEANING`-favored over the other two, not established.
2. **Does not validate Reading B** by virtue of surviving these two
   checks — surviving a bound is necessary, not sufficient, for a
   reading's own construct validity, which remains `P150`'s separate,
   unresolved question.
3. **The Cassini γ-vs-force-ratio mapping is unverified** — inherited
   from `docs/118` at face value, explicitly flagged, not independently
   derived (§3). A proper PPN-level derivation of what a `1/r³` dipole
   force actually implies for γ was not attempted.
4. **`r_test`, Ti/Pt atomic-mass-only approximation, and `T=300`K are all
   order-of-magnitude inputs** (per `P150`'s own §5 flag) — real heat
   capacities, exact test-mass geometry, and the alloys' minority
   constituents (Al, V, Rh) were not used.
5. Nothing about MULTING itself (Gate 1) — entirely this project's own
   reconstruction, evaluated under its own disputed extension choice.
