# P7 — the k-definition question, resolved from the primary source (not from TJB) — the "strictly thermal" escape hatch does not survive

**Date:** 2026-08-11 · answers the most decisive, cheapest-of-all open item
named in P6 §3a: whether MULTING's `k` is strictly thermal energy (in which
case a cold neutron star has `u_NS≈0` and the pulsar-timing bound on `β_d`
evaporates) or something broader that a cold compact object still carries.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Method:** direct, careful re-reading of the preprint's own definition of
`k` (Gate 1 discipline — grep the primary source, do not trust a prior
summary of it), cross-checked against a standard nuclear-physics estimate.
**Constraint respected throughout:** TJB asked for a pause in correspondence
until his own preprint publishes (2026-08-03, confirmed). Nothing here asks
him anything or is sent to him — this resolves the question from the text
already in this project's possession, per NO_AUTHOR_ERROR (this evaluates
THIS PROJECT'S OWN derived `β_d=2`, not a claim about what TJB himself
intends or uses).

---

## 1. What the preprint actually says about k — read directly, not from a summary

Three passages, `data/source_material/buckholtz_preprints202511.0598.v6_
pymupdf-clean.md`, quoted verbatim:

**Definition (lines 663-668, 775-780):**
> "we associate the four-word term total internal kinetic energy with a
> property of object-A. The total is across the kinetic energies of the
> moving nonzero-mass sub-objects of object-A." ... "kA denotes the internal
> kinetic energy of object-A. (The internal kinetic energy of object-A is
> the total of the energies of linear motion, relative to the center-of-mass
> of object-A, that associate with movements of nonzero-mass sub-objects
> that associate with object-A.)"

**Explicit exclusion (line 728):**
> "Modeling does not need to consider potential energies that, within
> objects, bind sub-objects into objects or that affect the motions of
> sub-objects."

**The passage that actually settles "thermal-only" (lines 790, 798-802):**
> "Suppose that kA associates only with the rotation of a uniform ring of
> mass. [...] For protoclusters and galaxy clusters, the notion that kA
> associates only with the rotation of a uniform ring of mass does not
> pertain. Typical ratios of total thermal energies of sub-objects to total
> kinetic energies of bulk linear motions of gas and galaxies are generally
> large [80-82]."

## 2. What this settles, directly, no interpretation required

**"k is strictly thermal energy, by definition" has no textual support.**
TJB explicitly discusses ROTATION as a live, physically real candidate
source of `k` ("kA associates only with the rotation of a uniform ring of
mass") — he does not rule this out as a matter of definition, he argues
that for the CLUSTER case specifically, thermal motion of gas dominates
OVER bulk/rotational motion of galaxies, citing three references [80-82] for
that specific astrophysical fact. This is an argument about which physical
source is LARGER for one application (clusters), not a definitional
restriction of `k` to thermal motion only. The definition itself (§1) is
general: kinetic energy of any relative internal motion, explicitly
excluding only potential/binding energy.

**Consequence: rotational kinetic energy of sub-objects unambiguously
counts as `k`, on TJB's own explicit terms.** This is the single least
contestable reading available — it requires no extension, no physics not
already discussed in the text, and no resolution of any harder ambiguity
(see §4).

## 3. The clean bound — using only the uncontestable rotational component

`FINDING_unsuppressed_observable_periastron.md` §4 already computed, from
the double pulsar's OWN measured spin period (`P=22.7` ms, one of the two
J0737-3039 neutron stars — an observed quantity, not an estimate), the
rotational-kinetic-energy-only bound:

```
rotational energy only (P = 22.7 ms):  u_NS = 0.23 m   ->   beta_d < 6.0e-2
```

Against this project's own derived (not fitted) `β_d=2` (`FINDING_two_charge_
completion.md`, zero free parameters after the overall coupling constant):

```
beta_d / bound = 2 / 6.0e-2 = 33.3   ->   ~1.5 orders of magnitude EXCLUDED
```

**This does not require resolving whether degenerate/Fermi motion also
counts (§4).** It uses only the part of `k` that is textually beyond dispute
— TJB's own explicitly-discussed rotational candidate — and an observed,
not estimated, pulsar spin period. `β_d=2` is excluded by this alone.

## 4. What remains genuinely open — and why it does not change the verdict

One real ambiguity survives close reading: TJB defines `k` as the excess of
`EoA` over a "ground-state energy" `E00,oA` (lines 652-661). For a classical
system, "ground state" naturally means "all sub-objects at rest" — under
that reading, a cold, non-thermally-excited, non-rotating neutron star's
`k` would be dominated by degenerate (Pauli-exclusion-forced) neutron motion,
which is NOT negligible. A direct nuclear-physics estimate (relativistic
Fermi kinetic energy per neutron at typical neutron-star core densities):

```
n = n0   (nuclear saturation, 0.16 fm^-3, crust-core boundary): E_kin/mc^2 = 0.060
n = 2 n0 (typical outer core):                                 E_kin/mc^2 = 0.094
n = 4 n0 (typical inner core, ~1.4 Msun NS):                   E_kin/mc^2 = 0.146
n = 7 n0 (dense core, massive NS):                             E_kin/mc^2 = 0.206
```

comparable to or exceeding the `E/Mc²≈0.105` "binding energy" estimate the
periastron finding used for its "broad" reading, giving a bound around
`β_d<1e-5`-`2e-5` — `β_d=2` excluded by ~5 orders of magnitude, not just ~1.5.

**But TJB nowhere discusses quantum degeneracy, Pauli exclusion, or Fermi
statistics anywhere in this text** (checked directly — zero occurrences of
those terms; every example he gives — galaxy/gas motion in clusters — is
classical and non-degenerate). Whether HIS OWN mental model of "ground
state" implicitly means the true quantum-mechanical ground state (filled
Fermi sea, which would already contain this kinetic energy as part of the
baseline, making the degenerate contribution to `k` net to ~zero) or the
classical zero-velocity baseline (which would count it) is **not decided by
anything in the corpus** — this is a genuine interpretive gap, not
something a closer reading can close. Flagged `[UNKNOWN]`, not resolved.

**This ambiguity does not matter for the bottom line.** §3's rotational-only
bound already excludes `β_d=2` by ~1.5 orders of magnitude without touching
this question at all. The degenerate-motion question only affects whether
the exclusion is ~1.5 orders (rotational-only, airtight) or ~5 orders
(rotational + degenerate, if "ground state" means classical rest) — either
way, `β_d=2` does not survive.

## 5. Verdict

```
"k is strictly thermal, by definition"       : NO TEXTUAL SUPPORT.
                                               TJB explicitly discusses
                                               rotation as a candidate
                                               source; thermal dominance is
                                               argued only for the cluster
                                               application specifically.
Rotational kinetic energy counts as k         : YES, unambiguous on TJB's
                                               own explicit terms.
beta_d=2 (this project's own derived value)
  vs pulsar bound, rotational-only            : EXCLUDED by ~1.5 orders of
                                               magnitude (beta_d<6.0e-2),
                                               using only an OBSERVED pulsar
                                               spin period, no disputed
                                               physics estimate needed.
beta_d=2 vs pulsar bound, if "ground state"
  = classical rest (degenerate motion counts) : EXCLUDED by ~5 orders of
                                               magnitude -- consistent with
                                               the periastron finding's
                                               original "broad/binding"
                                               estimate (0.105), now backed
                                               by an independent nuclear-
                                               physics calculation (0.06-0.21
                                               across realistic NS densities)
                                               rather than an ad hoc number.
Remaining open question                       : whether TJB's "ground state"
                                               baseline is classical or
                                               quantum-mechanical -- genuinely
                                               undecided by the corpus, and
                                               does not change the verdict
                                               either way (S4).
```

**Resolution: the "k is strictly thermal, escape hatch, u_NS≈0" reading that
`FINDING_unsuppressed_observable_periastron.md` §4 left open does not
survive close reading of the primary source.** This project's own derived
`β_d=2` (P1, two-charge completion) is excluded by the double-pulsar bound,
by at least ~1.5 orders of magnitude on the most conservative, textually
uncontroversial reading, and by ~5 orders of magnitude on the reading this
finding's own nuclear-physics estimate favors as more likely.

## What this does NOT establish

1. **Does not say TJB's own theory is wrong**, per NO_AUTHOR_ERROR. This
   evaluates this project's own reconstruction (`β_d=2`, derived in P1 from
   a specific point-charge construction), against this project's own
   best-effort reading of his published definition of `k`. TJB's own
   fitted/intended values (Table A1's `4.5`, or any value in his own
   unpublished work) are a separate matter this finding does not speak to.
2. **Does not resolve the classical-vs-quantum "ground state" question**
   (§4) — flagged `[UNKNOWN]`, not closed. The bottom-line verdict does not
   depend on resolving it, but a fuller understanding of the theory's
   intended scope for compact objects would benefit from it.
3. **Does not ask TJB anything, and is not sent to him.** The correspondence
   pause stands untouched. `P3_k_definition_question_DRAFT_HELD.md` (the
   earlier, still-held draft of a question for him) is a different artifact
   — that draft assumed the question needed TJB's input to resolve; this
   finding shows the corpus itself already resolves the operative part of
   it (whether the escape hatch survives) without needing to ask.
4. **This is a scaling/order-of-magnitude argument for §4's degenerate-motion
   branch**, not a full stellar-structure calculation — realistic neutron
   star density profiles, general-relativistic corrections, and composition
   (protons, electrons, possible exotic matter) would shift the exact
   number by a factor of order unity, not by orders of magnitude (matches
   the periastron finding's own caveat #4 about uniform-density estimates).

## Reproduction

```python
import math

# Section 3 -- the clean, uncontroversial bound
beta_d = 2  # FINDING_two_charge_completion.md, derived not fitted
bound_rotational = 6.0e-2  # FINDING_unsuppressed_observable_periastron.md S4, from P=22.7ms
print(beta_d / bound_rotational)  # -> 33.3, ~1.5 orders of magnitude excluded

# Section 4 -- degenerate Fermi kinetic energy estimate, for context only
hbarc = 197.327  # MeV*fm
mn_c2 = 939.565  # MeV
n0 = 0.16        # fm^-3, nuclear saturation density

def fermi_kinetic_fraction(n_fm3):
    pF_c = hbarc * (3 * math.pi**2 * n_fm3) ** (1/3)
    Ekin = math.sqrt(pF_c**2 + mn_c2**2) - mn_c2
    return Ekin / mn_c2

for factor in (1, 2, 4, 7):
    print(factor, "* n0:", fermi_kinetic_fraction(factor * n0))
```
