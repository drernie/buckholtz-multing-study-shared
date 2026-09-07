# docs/159 — H1b status: the sole remaining real test of H1 has never run

**Date:** 2026-09-07
**Trigger:** `NR-014`'s own addendum names H1b *"the sole remaining real
test of H1"*; that pointer was recovered while correcting the
`null_results` classification and had never been recorded outside the
addendum.
**Verdict:** **`BLOCKED-INFRASTRUCTURE`** (Substrate Gate). Designed,
pre-registered, **never executed**. Blocked 68 days on external data
access. Per the Gate's own hard rule, this is **not evidence against H1**.

---

## 1. The headline

**The one test that could actually test H1 has never been run.** Everything
killed in the H1 programme used the cluster-interior ICM; H1b is the only
arm that uses the WHIM — which H1b's own `claim.md` calls *"the actual
filament gas TJB refers to."*

| arm | proxy | status |
|---|---|---|
| **H1a** | cluster ICM, `T > 10⁷ K`, inside `R_200` | **KILLED** — `NR-010` |
| **H1c** | morphology as mediator | KILLED — `NR-012` |
| **H1d** | mass-threshold dependence | KILLED — `NR-011` |
| **H1e** | AGN feedback as confound | KILLED — `NR-014` |
| — | `T_X` as shared variable | **UNRESOLVED** — `NR-015`, a *fifth* candidate none of the four controlled for |
| **H1b** | **WHIM, `T = 10⁵–10⁷ K`, `R_200 < r < 3R_200`** | **NEVER RUN** |

Read as a list of kills this looks like H1 is dead. It is not. H1a used a
proxy its own successor file calls less physically motivated, and the arm
matching TJB's actual claim is the one that never executed.

## 2. What exists and what does not

`experiments/20260701-h1b-whim-thermal-mass-bias/` contains exactly two
files, both dated 2026-07-17: `claim.md` and `estimand.md`. There is **no
`decision.md`, no controls, no metrics** — nothing was run.

The design itself is sound and pre-registered before any data:

- **KILL:** `r < 0.15` AND `p > 0.20`
- **PROMOTE:** `r > 0.30` AND `p < 0.10`
- confounders named in advance (dynamical state; mass scaling), with
  partial correlation controlling `M_true` and dynamical state as the
  discriminator
- `claim_entropy` recorded, including *"N_unresolved_blockers = 1 (TNG API
  access not yet set up)"*

## 3. The blocker, and its age

Data path (`claim.md`, verbatim): **IllustrisTNG-300**, snapshot 67
(`z≈0.2`) or 99 (`z=0`), `https://www.tng-project.org/api/TNG300-1/`,
*"registration submitted 2026-07-01, pending approval as of 2026-07-04."*

Two bypasses were checked and are **dead**, with reasons recorded:

- **Option C** — Vladutescu-Zopp et al. 2025 (arXiv:2506.18459), 138 TNG
  clusters with a soft X-ray WHIM proxy: *"we do not discuss hydrostatic
  masses."* No mass-bias data of any kind. (Its radial-annulus design and
  WHIM temperature range were adopted anyway.)
- **Option B** — Barnes et al. 2020 (arXiv:2001.11508), Mock-X: has
  `b_HSE` for TNG clusters but **zero** WHIM/IGM data.

Later status checks, both consistent:

- `progress.md`: *"TNG API technical bypass search — exhausted, all options
  (B/C/D) dead"*, and *"TNG API access — still pending (18+ days silent)"*
- `docs/145` (2026-08-17/26): h1b-whim **"externally blocked"**, waiting on
  TNG-300 access

Last verified block: **2026-08-26**. Elapsed since registration:
**68 days**.

## 4. What could not be checked today, and is therefore not claimed

A literature refresh — has any dataset published since July made a bypass
possible? — **could not be run**. Both search tools failed: arXiv MCP
timed out twice, Semantic Scholar returned a rate-limit error.

Per the Substrate Gate this is recorded as a failure to check, **not** as a
finding that nothing new exists. The July bypass search is 2 months stale
and its conclusion should not be carried forward as current.

## 5. Next actions, in order of cost

1. **Check whether TNG-300 access was granted** and nobody noticed. This
   needs the account holder — it cannot be checked from here, and creating
   or authenticating an account is out of scope. One login answers it.
2. **Re-run the bypass search** when a literature tool is available. Two
   months of new work is a real chance for a dataset pairing hydrostatic
   masses with WHIM/outskirts gas.
3. ~~If access is still refused after 68 days, record H1b in `parked/`~~
   **DONE same day** — `parked/H1b-whim-thermal-mass-bias.md`, with three
   measurable revival conditions, plus the `decision.md` the folder had
   been missing since 2026-07-17.
4. **Added while parking, and it is not bookkeeping:** H1b's thresholds
   were frozen 2026-07-17, before FL Step 4a existed, so they have
   **never been checked against a floor**. `NR-010` in this very dataset
   went from raw `r=0.021` to partial `r=-0.701` on structure alone — so
   whether a WHIM-free null model already clears `PROMOTE: r>0.30` is an
   open question. Step 4a must run BEFORE the test on revival.

## 6. What this does NOT establish

1. **Not that H1 is true or false.** H1b has produced no data.
   `BLOCKED-INFRASTRUCTURE` is never evidence either way.
2. **Not that the other H1 arms were wrongly killed.** `NR-010`/`011`/
   `012`/`014` stand as recorded; `NR-014`'s addendum affirms its own
   verdict is unaffected.
3. **Not that a bypass does not exist** — see §4; the check could not run.
4. **Nothing about MULTING** (`NO_AUTHOR_ERROR`). H1 is this project's own
   reconstruction of a testable consequence, not TJB's own text.
