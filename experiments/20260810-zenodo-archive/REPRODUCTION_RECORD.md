# Reproduction record — Buckholtz (2026) Zenodo supplemental archive

**Date:** 2026-08-10
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION
**Target:** Zenodo 10.5281/zenodo.21204955, "Supplemental material for
*Multi-Tier Newtonian Gravity: A Cosmic-Node-Based Alternative to LCDM for the
Hubble Tension*", posted 2026-08-08, CC-BY-4.0.

---

## Why this is a different kind of target

Every previous attempt in this project to reconstruct the operator carrying the
MULTING force law into H(z) failed, and finding B0 (2026-08-03) established
why: the material available to us did not contain a deterministic, published,
reproducible operator, and Table A1 — the target those attempts aimed at — is
an AI service's response to a prompt, per the author's own caption.

This archive changes that. It ships the operator as code, and it does not use
Table A1.

| | before (v6 preprint) | this archive |
|---|---|---|
| F → H(z) bridge | not present; Appendix A is a prompt | `code/multing_core.py`, deterministic |
| data | Table A1 (AI response) | 31 cosmic chronometers + SH0ES + DESI DR2 Lyα |
| β status | ambiguous | stated outright as the two fitted free parameters |
| AI involvement | present, lightly described | disclosed, with a 20-day dialogue transcript |

B0's `BLOCKED_BY_TARGET_PROVENANCE` verdict is lifted: there is now a target of
the right kind.

**G1 must be split, and only half of it is closed** (correction 2026-08-10, after
an external reading pointed out that a single green mark would mislead a later
reader of this registry):

| | statement | status |
|---|---|---|
| **G1-computational** | `F → H(z)` exists as a deterministic, published, reproducible operator | ✅ **closed** by this archive |
| **G1-physical** | that operator *follows from* the claimed mechanics | 🔴 **open** |

The distinction is load-bearing rather than pedantic. `multing_core.py` computes
`addot_over_a` and its own docstring states the quantity is `-dH/dt`, explicitly
**not** `d̈/d`; for a literal mechanical reading `F = μ d̈` one has the kinematic
identity `d̈/d = Ḣ + H²`. Which of the two the force law licenses is not settled
by the archive, and the planned bridge stress test targets exactly `G1-physical`.
Marking G1 simply green would make that experiment look like a test of a closed
question.

---

## Gate 1 — artifact identity `[VERIFIED]`

| field | value |
|---|---|
| artifact_id | ARTIFACT_ZENODO_2026-08-08_MULTING_SUPPLEMENT |
| DOI | 10.5281/zenodo.21204955 (concept DOI 10.5281/zenodo.21204954) |
| downloaded as | `21204955.zip` — Zenodo's outer "download all" wrapper |
| inner file | `zenodo_archive_v17.zip`, 2 248 164 B |
| MD5 (inner) | `9cc38e1b5a4ac6286b635910acf0f5c2` — **matches published checksum** |
| publication_status | published, CC-BY-4.0 |
| relates_to | supplement to a paper that is **not yet public** (see below) |

The outer wrapper's own MD5 does not match the published one and must not be
compared against it; the published checksum belongs to the inner file. Checking
the wrapper first and stopping there would produce a false "corrupted" verdict.

**The paper itself is not published.** ORCID (0000-0003-4712-2585, 76 works)
lists this archive and nothing newer; no record of the paper appears in ORCID,
Crossref, or public search. The archive is out ahead of the work it supplements.

---

## Code audit before execution `[VERIFIED]`

Third-party code, so it was read before it was run.

- imports across all three scripts: `numpy`, `scipy`, `yaml`, `matplotlib`,
  `sys`, and its own `multing_core`
- no network calls, no `subprocess`, no `eval`/`exec`, no file deletion, no
  writes outside its own `figures/` directory

---

## Results `[VERIFIED-BASH]`

### Numerical results — `generate_all_results.py`

```
94 / 94 checks [OK]
 0     mismatches
 1     item flagged by the script itself, not silently passed
```

The one flagged item is Result 11 (the H₀ ≈ 11 km/s/Mpc circularity finding),
which the script states is reconstructed only approximately (12–19 across three
interpolation choices against a stated ~11) because the exact figure would
require digitising a 1994 figure. It is flagged loudly by the archive's own
code rather than hidden — worth noting as a point of method.

### Figures — `generate_all_figures.py`

Regenerated and compared pixel-by-pixel at 200 dpi against the copies shipped
in the archive:

| figure | pixels | differing |
|---|---|---|
| `multing_data_errorbars_figure` | 1 481 × 1 063 = 1 574 303 | **0** |
| `multing_intro_figure` | 1 481 × 1 063 = 1 574 303 | **0** |

**Scope of that check.** This verifies that the shipped copies were generated
by the shipped code. It does *not* verify the archive's stronger claim that the
code reproduces *the paper's own* figures — those files are explicitly not in
the archive ("kept alongside the .lyx source"), so that claim is not testable
from the archive alone. The archive's README reports 72 differing pixels for
the intro figure against the paper's file; our 0 is against the archive copy,
a different comparison. The two numbers are not in conflict.

---

## Defect found: figure generation breaks on a long install path

`generate_all_figures.py` writes via the relative path
`../figures/<name>.pdf`. On Windows, Python transparently applies the `\\?\`
long-path prefix to **absolute** paths but cannot to relative ones, so a
relative write is still bound by MAX_PATH = 260.

Extracted under a deep directory (resolved path 255 characters), the first
figure saved and the second — whose filename is 10 characters longer — failed
with `FileNotFoundError: '../figures/multing_data_errorbars_figure_archive_verification_copy.pdf'`,
naming a directory that plainly exists. Re-extracting to a short path fixed it
with no other change.

Two reasons this is worth passing on:

1. It is silent and misdirecting — the error names a path, so a reader will
   look for a missing directory rather than a length limit.
2. It is one line to fix: resolve against `pathlib.Path(__file__).parent`
   instead of the process working directory.

Diagnostic note: a direct write test to the same file *succeeded*, because that
test used an absolute path and Python repaired it. The failure only reproduces
in the exact call form the script uses.

---

## What the reproduction settles for this project

| project blocker | before | after |
|---|---|---|
| **G1-computational** — no deterministic H(z) from the force law | 🔴 primary blocker | ✅ **closed** |
| **G1-physical** — that operator follows from the claimed mechanics | (not separated before) | 🔴 **open** — target of the bridge stress test |
| **B0** — target of the wrong provenance | 🔴 | ✅ **lifted** — Table A1 unused |
| **BETA-1 HOLD** — β not derivable | 🔴 | ⚠️ **confirmed**: stated as fitted |
| **G3** — no Lagrangian | 🔴 | 🔴 unchanged |
| **G4** — symmetry fixing the isomer count | 🔴 | 🔴 out of this paper's scope |

### Convergences with this project's earlier findings

Stated as observed agreement. No claim is made about cause; the author may have
reached these independently.

| our earlier finding | this archive |
|---|---|
| β_d = 4.5 gives ε ~ 10⁻⁶; an observable signature needs β_d ≳ 2.9 × 10⁵ | β₁ = 1.43 × 10¹⁰ |
| β are not derived from first principles | "the ONLY two free parameters fit in each row" |
| MULTING vs ΛCDM on H(z): ΔAIC = 0.74, indistinguishable | χ² 15.78 vs 16.60 apples-to-apples |
| test against the cosmic-chronometer compilation, not Table A1 | CC-31 + SH0ES + DESI |

### Model comparison, as the archive itself reports it

| model | free parameters | χ²₃₃ |
|---|---|---|
| MULTING, SH0ES-anchored | 2 | 15.78 |
| ΛCDM, apples-to-apples | 1 | 16.60 |
| ΛCDM, freely optimised | 2 | 16.31 |
| ΛCDM, fixed Planck | 0 | 36.95 |

At comparable freedom the difference is under one χ² unit on 33 points. The
headline contrast (15.75 vs 36.95) is against a ΛCDM allowed no free parameter;
the archive supplies the apples-to-apples row itself.

---

## Open questions a referee is likely to raise

Recorded as questions about the calculation. Items 4 and 7 are raised by the
archive itself.

| # | question | first raised by |
|---|---|---|
| 1 | Sensitivity to the F₁/F₂ near-cancellation | us — **now measured**, see `FINDING_beta_degeneracy.md` |
| 2 | F₀ contributes ≤ 1 % of the net; in what sense is the result Newtonian | us |
| 3 | `Efun(z)` uses Planck ΛCDM inside MULTING's own scaling laws | us |
| 4 | T₀ recalibration implies T ≈ 3.3–3.6 keV vs ≈ 7 keV from weak-lensing M–T | **the archive**, called unresolved |
| 5 | Headline comparison is against a zero-free-parameter ΛCDM | us |
| 6 | Cosmic-chronometer covariance; χ² uses diagonal errors on 31 correlated points | us, raised in the July correspondence |
| 7 | d₀ = 45 Mpc is self-referential; M₀ "not independently data-grounded" | **the archive** |

---

## Status

TJB asked for a pause until his preprint is published. That condition is **not
met** — the supplement is out, the paper is not. Nothing here is to be sent.

This work is on material published under CC-BY for the express purpose of
replication, and is therefore not an approach to the author.
