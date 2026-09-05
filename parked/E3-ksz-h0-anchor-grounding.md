# PARKED — E3: can kSZ ground `H₀,anchor` without the circularity TJB
# diagnosed?

**ID:** E3-ksz
**Date parked:** 2026-09-06
**Verdict:** ARCHIVE (valid question, deliberately deprioritized —
**not** falsified)
**Source:** `experiments/20260906-evidence-authority/FINDING_E3_h0_
anchor_alternative_techniques.md`

## The question

v82's Section IV.M defines `H₀,anchor = ṡ₀/s₀` — a kinematic ratio of
relative velocity to relative separation between two typical
cluster-scale nodes. TJB tried to ground it in real data (cluster-cluster
correlation length + pairwise-velocity statistics), got
`~11 km/s/Mpc` — implausible — and diagnosed why himself: the
peculiar-velocity data is only extractable because surveys already
subtract an assumed Hubble flow. His own conclusion: *"We do not think
this is a fixable methodology choice."*

`FINDING_E3` tested whether that verdict is too strong and found **one**
real, scale-matched structural exception: the **kinematic
Sunyaev-Zel'dovich effect**. Its velocity channel — a Doppler shift of
CMB photons scattered off cluster gas — genuinely does not decompose a
redshift into "assumed Hubble flow + peculiar residual", and current kSZ
pairwise-velocity science operates at `30-230 Mpc` separations
(`[VERIFIED-arXiv:2604.14327]`, ACT collaboration), overlapping the
`~30-60 Mpc` scale `H₀,anchor` needs.

## Why it is parked rather than pursued

A Step 8a skeptic pass established that current kSZ practice **assumes a
fixed fiducial `H₀`/ΛCDM background** to convert redshifts and angles
into the separations it reports, and to calibrate the mass-observable
relations used to interpret the kSZ decrement. The circularity is
**relocated from the velocity side to the separation/calibration side**,
not removed. No kSZ pairwise-velocity paper found derives `H₀`
independently; all condition on an assumed one to test structure growth.

Beyond that: this is squarely TJB's own home domain, it is expensive,
and it is the one axis on which this project is structurally behind —
the opposite of where its comparative advantage lies (`FINDING_E7`,
`boyko-agent` assessment, 2026-09-06).

## Revival Condition (measurable — all are external events, none is
## "we feel like trying again")

**(a)** A published kSZ analysis appears that reports cluster pairwise
velocities **without** conditioning separations or mass-observable
calibration on a fiducial `H₀` — i.e. the relocated circularity is
itself closed upstream by the kSZ community; **OR**

**(b)** TJB's own future work takes up `H₀,anchor` grounding again, in
which case this becomes a contribution to his line rather than an
independent one; **OR**

**(c)** A different technique appears that is scale-matched to
`~30-60 Mpc` cluster separations AND whose full pipeline — not merely
its named signal channel — is free of an assumed expansion rate. The
`E3` lesson applies: check the whole pipeline, not the named step.

## Parked Pearl

The transferable part, already recorded in `pearl_registry/INDEX.md`
(2026-09-06, `FINDING_E3` row): **a technique can genuinely escape the
specific circularity it was designed to escape and re-import the same
class of assumption at a different step.** Verifying only the named
mechanism, and not the rest of the pipeline, is how a false escape gets
recorded as a real one. That lesson is domain-general and does not
depend on this question being revived.

## What is explicitly NOT claimed by parking this

1. Not that TJB's "not fixable" verdict is wrong — `E3`'s corrected
   verdict is that it **stands**, with kSZ named as the one unexamined
   corner.
2. Not that kSZ is unusable — only that no one has shown it closing this
   particular loop, and this project is not the right party to try.
3. `NO_AUTHOR_ERROR`.
