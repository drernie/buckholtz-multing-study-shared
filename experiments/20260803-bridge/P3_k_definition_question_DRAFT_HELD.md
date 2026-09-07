> **[SUPERSEDED 2026-09-07 — `FINDING_P214`] THE QUESTION AS POSED IS
> ANSWERED BY v82 ITSELF.** Line 207 of v82's own symbol table:
> *"`k_A` is the thermal energy that associates with the ICM of node-A."*
> The ambiguity this draft was written to resolve came from reading v6's
> broader phrasing alongside v82's code. **Do not send this as written.**
> If any question survives, it is much narrower — whether `k` extends to
> objects with no ICM at all — and v82 already says MULTING *"does not
> (yet) adequately discuss"* such cases. Draft kept below unedited.

# P3 — the k-definition question for TJB

**Status: DRAFT, HELD.** Not sent. TJB asked for a pause until his preprint
publishes (2026-08-03); nothing about this changes that. Kept here so the
question is formulated while the reasoning is fresh, per the project's own
"share results, don't ask questions" protocol — this is written as something
to eventually *tell* him we found, not to *ask* him.

---

## Why this is the one load-bearing question

Two independent routes converged on the same undefined term.

1. **Pulsar bound** (`FINDING_unsuppressed_observable_periastron.md`): the
   double pulsar J0737-3039 constrains `β_d < 1.2×10⁻⁵` if `k` includes bulk
   internal energy (binding, rotational, degeneracy) — five orders below
   Table A1's fitted `4.5`. If `k` is strictly thermal, cold neutron stars have
   `u_NS ≈ 0` and the bound evaporates entirely.
2. **Charge-space identifiability** (this session, cluster data): the
   pipeline's own `k = (3/2)(M_gas/μm_p)k_BT` is thermal by construction, and a
   positional cross-match against CHEX-MATE's independent X-ray temperatures
   found a residual correlation `ρ = +0.36` (n=25) between two independent
   `k`-estimators after removing the mass trend — consistent with `k` carrying
   real information beyond `M` alone, in the thermal reading specifically.

Both routes point at the same fork: **is `k` thermal kinetic energy
specifically, or "kinetic energy of sub-objects" more broadly?** The preprint's
own text supports the broader reading in places and the narrower one in the
cluster analysis. The theory's viability for compact objects hangs entirely on
which.

## What we would tell him, in prose, once the pause lifts

> We found that if the "kinetic energy" charge k in the dipole/quadrupole
> terms is read as internal energy generally — as it would need to be for a
> neutron star's binding or rotational energy — the double pulsar
> J0737-3039's periastron precession, measured to 1 part in 400,000, bounds
> β_d about five orders of magnitude below the fitted cluster value. If k is
> specifically thermal kinetic energy, the way it's used in the cluster
> analysis, cold neutron stars carry almost none of it and the bound doesn't
> apply. This turns out to be the same distinction our cluster-data check
> needed: whether k varies independently of mass, or is just mass wearing a
> different unit. We think this is worth pinning down explicitly in the next
> draft, because right now the theory's compact-object reach depends on it
> entirely.

## What is NOT in this draft

No question marks aimed at him to answer on demand, no audit language, no
implication anything is broken — per `feedback_tjb_no_questions_share_results.md`
and `feedback_no_evaluative_authority_words.md`. When this is eventually sent
(after the pause, after TJB's own preprint is out, and only with explicit
approval), it should read as a finding shared, not a gap flagged for him to
close.
