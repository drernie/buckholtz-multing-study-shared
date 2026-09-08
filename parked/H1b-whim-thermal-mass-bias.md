# H1b — WHIM filament thermal energy vs cluster mass bias

**Parked:** 2026-09-07
**Verdict:** **STILL PARKED — `BLOCKED-INFRASTRUCTURE` resolved 2026-09-09
(TNG access granted), but a second, more specific data gap took its
place immediately on revival attempt. Not archived on merit — see the
2026-09-09 section below before assuming this is now runnable.**
**Source experiment:** `experiments/20260701-h1b-whim-thermal-mass-bias/`
(`claim.md`, `estimand.md`, both 2026-07-17; `decision.md` added 2026-09-07)
**Status check that produced this:** `docs/159`

---

## Read this first — what parking does and does not mean here

Every other entry in `parked/` was archived on a *scientific* judgement:
valid but deprioritized, method missing, circularity relocated. **This one
is different.** H1b was never run. It is parked for bookkeeping only —
so an experiment folder containing a `claim.md` and no result stops
looking like work in progress.

Per the Substrate Gate's own hard rule, **`BLOCKED-INFRASTRUCTURE` is
never evidence against the claim.** Nothing in this file may be cited as
weighing against H1, in either direction.

## Why it matters more than its parked status suggests

`NR-014`'s own addendum calls H1b *"the sole remaining real test of H1."*

Every H1 arm that was killed — H1a (`NR-010`), H1c (`NR-012`), H1d
(`NR-011`), H1e (`NR-014`) — used the **cluster-interior ICM**
(`T > 10⁷ K`, inside `R_200`). H1b is the only arm using the **WHIM**
(`T = 10⁵–10⁷ K`, `R_200 < r < 3R_200`), which its own `claim.md` calls
*"the actual filament gas TJB refers to."*

So the arm closest to the actual claim is the one that never executed.
Read as a bare list, the H1 programme looks finished; it is not.

## What is already done, and needs no rework on revival

The design is complete and was pre-registered before any data:

- **KILL:** `r < 0.15` **AND** `p > 0.20`
- **PROMOTE:** `r > 0.30` **AND** `p < 0.10`
- **Estimand:** predictive (EstimandOps L0), `E_WHIM` → `delta_M`
- **Confounders named in advance:** cluster dynamical state; mass scaling.
  Discriminator is a partial correlation controlling `M_true` **and**
  dynamical state.
- **Claim entropy** recorded, including the blocker itself as
  `N_unresolved_blockers = 1`.

**Revival cost is execution only.** No redesign, no re-registration.

## The blocker

`IllustrisTNG-300`, snapshot 67 (`z≈0.2`) or 99 (`z=0`), via
`https://www.tng-project.org/api/TNG300-1/`.
Registration submitted **2026-07-01**; still pending at the last verified
check (`docs/145`, 2026-08-26). **68 days** as of parking.

Bypasses checked in July, both dead with recorded reasons:

| option | source | why dead |
|---|---|---|
| B | Barnes et al. 2020, arXiv:2001.11508 (Mock-X) | has `b_HSE` for TNG clusters, **zero** WHIM/IGM data |
| C | Vladutescu-Zopp et al. 2025, arXiv:2506.18459 | 138 TNG clusters with a soft-X-ray WHIM proxy, but states verbatim *"we do not discuss hydrostatic masses"* |

Each has exactly one of the two halves the test needs. Neither has both.

## Revival Condition (measurable — ANY of the three)

1. **TNG-300 API access is granted.** Binary and cheap to check: one login
   by the account holder. On grant, run the pre-registered test unchanged.
2. **A published dataset pairs hydrostatic masses (or `b_HSE`) with
   WHIM/outskirts gas properties for `N > 100` clusters.** This is the
   precise gap Options B and C each half-fill. A single paper carrying
   both columns revives this immediately.
3. **A different simulation suite** with public access supplies both
   quantities at comparable resolution (e.g. any successor or mirror
   providing `M_true`, `M_HE`, and outskirts gas in `R_200–3R_200`).

## Pre-condition on revival — run Step 4a BEFORE the test, not after

Flagged 2026-09-07 by `hooks/ceiling_gate_guard`. H1b's thresholds were
frozen **2026-07-17**; the Floor-Ceiling Interval (FL Step 4a) entered the
stack at the end of August. **These criteria have never been checked
against a floor.**

That is not hypothetical here. The precedent the hook cites is an H1
criterion that a null model containing no mechanism at all **exceeded
about sevenfold**. And this specific dataset has already shown it: in
`NR-010` the raw correlation was `r=0.021`, yet controlling `M_WL` produced
a partial `r=-0.701` from structure alone. A partial correlation of that
size arising without the tested mechanism is exactly the floor problem.

So `PROMOTE: r > 0.30` may or may not be passable by a construction with no
WHIM physics in it. Nobody has checked.

**On revival, before running the test:**

| end | construction | question |
|---|---|---|
| **floor** | same pipeline, WHIM signal removed — shuffle `E_WHIM` across clusters, or predict `delta_M` from `M_true` and dynamical state alone | how much correlation does the design give for free? |
| **ceiling** | a performer with privileged access to the simulation's own `M_true - M_HE` decomposition | how much is attainable at all? |

Then report `efficiency = (observed - floor) / (ceiling - floor)`.

Stop conditions, resolved **before** any result is generated:

- `PROMOTE` threshold `<=` floor -> **CRITERION_INVALID**, rewrite `claim.md`
- ceiling `<` `PROMOTE` threshold -> **TASK_INFEASIBLE**
- ceiling `~=` floor -> **NO_HEADROOM**

None of the three is evidence against H1 — they say the experiment could
not have been informative as designed.

## Step 4a RESULT — run 2026-09-07, `scripts/p210_h1b_floor_check.py`

The noise half of the floor check has now been done. It does **not** clear
H1b, but it settles one of the two ways the criterion could be invalid,
and it turned up two design defects that are fixable before any data
arrives.

### Noise floor: CLEAN

95th percentile of the null partial correlation vs the PROMOTE threshold,
Monte Carlo (20k trials) agreeing with `1/sqrt(N-k-3)` to under 5 percent:

| N | null SD | 95th pct of null abs(r) | PROMOTE 0.30 sits at | reachable by noise? |
|---|---|---|---|---|
| 100 | 0.1026 | 0.197 | 2.9 sigma | no |
| 138 | 0.0867 | 0.166 | 3.5 sigma | no |
| 200 | 0.0716 | 0.138 | 4.2 sigma | no |
| 300 | 0.0582 | 0.115 | 5.2 sigma | no |

A random predictor does not reach `r > 0.30` at any planned sample size.
The `PROMOTE` bar is not passable by chance — the H1 failure the ceiling
gate warns about (a null model beating the threshold ~7x) does **not**
repeat here on the noise axis.

### Defect 1 — `KILL` has a dead band, and it widens with N

`KILL` requires `r < 0.15` **AND** `p > 0.20`. Those two clauses do not
fire together. The `r` giving exactly `p = 0.20` is:

| N | r at p=0.20 | KILL's r-clause | dead band where KILL cannot fire |
|---|---|---|---|
| 100 | 0.1306 | 0.15 | `0.131 <= r < 0.15` |
| 138 | 0.1106 | 0.15 | `0.111 <= r < 0.15` |
| 200 | 0.0915 | 0.15 | `0.092 <= r < 0.15` |
| 300 | 0.0744 | 0.15 | `0.074 <= r < 0.15` |

A result landing in that band satisfies the r-clause, fails the p-clause,
and is therefore neither killed nor promoted. **The pre-registration does
not say what happens to it**, and the larger the sample, the wider the
band — the opposite of the intended behaviour.

### Defect 2 — the undefined middle

Nothing at all is specified for `0.15 <= r <= 0.30`. At these sample sizes
that is roughly 1.5 to 3 sigma wide: precisely where a real but modest
effect would land. Combined with defect 1, the criterion is only decisive
at the two extremes.

(Minor, harmless: `PROMOTE`'s `p < 0.10` clause is redundant — any
`r > 0.30` already has `p` far below it at every planned N. It reads like
a second safeguard and is not one.)

### Still NOT cleared: the structural floor

This check used random predictors. It says nothing about a **WHIM-free but
structurally correlated** predictor — which is exactly what bit before:
`NR-010` went from raw `r = 0.021` to partial `r = -0.701` once `M_WL` was
controlled, purely from covariance structure. That floor needs the data
(shuffle `E_WHIM` preserving its marginal, or predict `delta_M` from
`M_true` and dynamical state alone) and remains open.

### Consequence for revival

Fix the bands **before** running, not after seeing a result — otherwise
the fix is unfalsifiable. Concretely: make `KILL` a single clause
(`p > 0.20` alone, or `r` below the N-dependent value above), and state
explicitly what an outcome in `0.15-0.30` means. Then run the structural
floor as the first thing the data touches.

## Bands REPAIRED 2026-09-07 — `claim.md` AMENDMENT 1

The two defects P210 found are fixed, additively and before any data
exists (`scripts/p211_h1b_criterion_repair.py`). The original criteria are
NOT rewritten; `claim.md` carries a dated AMENDMENT 1 that supersedes them
for execution.

**New rule** — one-sided 95% bounds, Fisher-z, `k = 2` controls, both
original numbers kept:

```
KILL          upper bound on r  <  0.15
PROMOTE       lower bound on r  >  0.30
INCONCLUSIVE  otherwise
```

Verified complete and disjoint over 3801 values of `r` at
`N = 100/138/200/300/500`. Dead band gone, middle defined, behaviour now
monotone in `N`.

**New binding requirement: `N >= 124`.** The repair exposed that `KILL` is
unattainable below that even for a perfectly null `r = 0` — at `N = 100`
the best achievable upper bound is `0.1672 > 0.15`. The design's own
`"N > 100"` cannot deliver a `KILL`, and a test that can only return
`PROMOTE` or `INCONCLUSIVE` is not a test of the claim.

**Deliberately left open:** how large the `KILL` bar should be is a
scientific judgement, not a statistical one. Its cost is tabulated in the
amendment (bar 0.20 -> `N >= 71`; bar 0.10 -> `N >= 274`). Not changed
unilaterally.

**Unaffected:** the structural floor. Still needs the data, still must run
first.

## AMENDMENT 2 — 2026-09-07 — bar relaxed, sign subtype, null models frozen

`scripts/p212_h1b_amendment2.py`. Additive again; nothing rewritten.

- **`KILL` bar 0.15 -> 0.20** (user decision — a judgement about the
  smallest meaningful effect, not a statistical one). **Minimum `N` for a
  reachable `KILL` drops 124 -> 71**, so the design's own "N > 100" is now
  sufficient where under AMENDMENT 1 it was not.
- **New subtype `KILL — opposite-sign signal`**, trigger `U₉₅(r) < −0.30`
  — the mirror of `PROMOTE`. A strongly negative result is no longer
  filed indistinguishably from "no effect". The weaker trigger `L₉₅ < 0`
  was rejected: at `N=138` even `r = −0.01` would have fired it.
- **Structural-floor ALGORITHM frozen** (not its value): `M0-1` permutes
  `E_WHIM` within `(M_true, z, dynamical state)` strata, 10 000 draws,
  with the stratification fixed **deterministically by `N` alone** (finest
  scheme keeping >= 5 units/stratum: 2x2x2 / 3x3x2 / 3x3x3 / 4x4x3);
  `M0-2` predicts `δM` from controls with no WHIM term. **Binding order:
  compute `p(r | M0)` FIRST, unblind the real pairing after.** This
  removes the freedom to pick a permutation scheme after seeing structure.

**Still not settled:** the structural floor's *value*. Only the procedure
is fixed.

## TNG access PROBED 2026-09-07 — question is UNANSWERABLE anonymously

Checked, with a control. Result: **the probe cannot settle it, and that is
itself the finding.**

| endpoint | HTTP |
|---|---|
| `https://www.tng-project.org/` (control) | **200** |
| `https://www.tng-project.org/data/` (control) | **200** |
| `https://www.tng-project.org/api/` | **403** |
| `https://www.tng-project.org/api/TNG100-1/` | **403** |
| `https://www.tng-project.org/api/TNG300-1/` (H1b's target) | **403** |

The controls matter: the site answers 200 while the API answers 403, so
this is an **authentication requirement, not a block on us**. Had the site
also 403'd, the API result would have carried no information.

**Consequence: `403` is returned to an anonymous caller whether the
registration was approved or not.** "Access granted but no key configured"
and "still pending" are indistinguishable from outside. Only a request
carrying the key separates them — and obtaining or using credentials is
out of scope here.

So the earlier next-action stands, now backed by evidence rather than
assumption: **one login by the account holder settles it, and nothing
short of that does.**

No API key exists anywhere in this repository (checked: no `.env`, no
config carrying a TNG token, no key-shaped variable in any tracked file).

### Side finding, corrected in place

`scripts/illustris_tng_k_a.py` claimed in two places that the API needs no
key for top-level info — *"public, no API key needed for summary"* and
*"does not require API key for top-level info"*. **Both are false**: the
root itself 403s. So `try_fetch_tng_api()` has always taken its HTTPError
branch and that script has always used its analytical fallback.

Provenance checked before reporting: `main()` computes from
`kinetic_energy_proxy_tng` / `merger_rate_proxy`, never from the API
response, and **no `.md` in the repo cites that script**. So nothing
downstream ever claimed TNG data from it. A documentation defect, not a
contaminated result. Corrected in the file, with the old claim quoted
rather than deleted.

## Standing caveat on the July bypass search

The Option B/C survey is dated **July 2026** and is now two months stale.
A refresh was attempted on 2026-09-07 and **could not run** — arXiv MCP
timed out twice, Semantic Scholar returned a rate limit. That is a failure
to check, not a finding that nothing new exists. **Do not carry the July
conclusion forward as current** when evaluating revival condition 2.

## What this does NOT establish

1. **Nothing about whether H1 is true or false.** No data was produced.
2. **Not that the other H1 arms were wrongly killed.** `NR-010`/`011`/
   `012`/`014` stand as recorded.
3. **Not that no bypass exists** — see the standing caveat above.
4. **Nothing about MULTING** (`NO_AUTHOR_ERROR`). H1 is this project's own
   reconstruction of a testable consequence, not TJB's own text.

---

## TNG ACCESS GRANTED 2026-09-09 — revival attempted, blocked on a
## DIFFERENT, more specific reason than before

**Status change on Revival Condition 1**, from *pending* to *granted and
verified*. Approval email (`[third-party email redacted]`, 2026-09-08 19:25
UTC) followed same session; account active, real API key obtained,
stored at `~/.secrets/tng_api_key.env` (outside repo, never in chat/
tracked files per this file's own standing instruction).

**Live API checks, `[VERIFIED-BASH]` against the real TNG-300 group
catalog (snapshot 99, halo 0 as a control):**
- `Group_M_Crit200` **is** directly available (`104034.4 * 1e10/h M_sun`
  for the box's most massive halo) — this covers `M_true` in the
  estimand.
- **No hydrostatic-mass field exists anywhere in the raw group
  catalog** (`GroupBHMass`, `GroupMass`, `GroupMassType`,
  `Group_M_Crit200/500`, `Group_M_Mean200`, `Group_M_TopHat200` — full
  field dump checked, no `M_HE`-equivalent). Confirms, by direct
  inspection rather than inference, what the July bypass note already
  suspected: TNG's own catalog does not carry an observationally-styled
  hydrostatic mass.

**New idea tried, and killed with a specific reason:** compute `E_WHIM`
directly from real TNG-300 gas-particle cutouts (the API supports this —
confirmed via the official docs' cutout example), and cross-match against
Barnes et al. (2020)'s own published `b_HSE` **per cluster**, rather than
treating Option B as fully dead. This would have filled both halves of
H1b's estimand using two independent, real sources.

**Killed by direct full-text check of `arXiv:2001.11508`, not
inference:** three separate searches for a per-object data release —
`"data availability"`, `"public"`/`"github"`, `"individual cluster"` —
**zero hits, all three.** Every quantitative result in the paper (Figs.
3, 5, 6, 7) is reported as a **median trend and scatter band binned by
mass** (*"median ratio... where the number of clusters in a bin of width
Δlog₁₀(M)=0.1 is less than 10"*) — population-level statistics, not a
per-halo table with TNG IDs. There is nothing to cross-match against.

**Consequence:** Revival Condition 1 (TNG access) is now satisfied, but
this does not revive H1b as pre-registered. The blocker has moved from
"no data access" to "the specific missing ingredient — a real,
per-cluster hydrostatic mass estimate — still does not exist anywhere
public," exactly as the original bypass survey (Options B/C) found in
July, now confirmed with live access rather than assumed from an
abstract. Building `M_HE` from scratch means implementing a genuine
synthetic-X-ray/HSE pipeline (Mock-X's own actual method, not just its
headline number) — the "materially larger, more specialized undertaking"
this file has named twice now. **Not attempted here** — out of scope for
a single session, and not authorized as its own separate undertaking.

**Revival Condition 2, updated:** still open. A future paper or data
release pairing per-cluster `M_HE` (or `b_HSE`) with per-cluster outskirts
gas properties, for `N≥71` TNG-300 clusters, would revive this
immediately with no redesign — same standing condition as before, now
narrowed by knowing exactly what Barnes+2020 does NOT provide.

## Revival Condition 3 — a PROMISING, UNCONFIRMED lead found 2026-09-09,
## logged honestly at the state it was left in, not chased further

Widened the search past TNG-specific papers. Two real papers from the
**same collaboration**, on the **same fixed sample of 324 clusters**
("The Three Hundred Project," Cui et al. 2018, `arXiv:1811.11810`):

- `arXiv:1911.07878` (Ansarifard et al. 2019) — per-cluster hydrostatic
  mass bias, correlated against per-cluster X-ray diagnostics (azimuthal
  scatter, gas ellipticity) for **>300 individual simulated clusters** —
  this reads as genuinely per-object, not binned-median-only (contrast
  with Barnes+2020 above).
- `arXiv:2503.05011` (Li et al. 2025) — WHIM gas properties
  (`10⁵<T<10⁷K`) around the **same 324-cluster sample**, two physics runs
  (GIZMO-SIMBA, Gadget-X).

If both papers' underlying data are keyed to the same standard 324
cluster IDs (very plausible — same collaboration, same fixed sample,
routine practice for this group), this fills H1b's own estimand for a
**different simulation suite** than the one originally registered —
exactly the shape Revival Condition 3 (above) already anticipated
("a different simulation suite... supplies both quantities").

**Not confirmed, and stopped here deliberately:**
1. The collaboration's own data portal, `the300-project.org` (cited
   inside `arXiv:1911.07878` itself), does not resolve from this
   session's network (`getaddrinfo ENOTFOUND`) — could be a stale URL,
   a real outage, or a sandbox network restriction; not established
   which.
2. Neither paper's per-cluster table has actually been opened and
   checked for a shared ID column — the "per-object, not binned"
   reading above is from abstract-level and section-level text only
   (`search_paper_text`, not a downloaded table).
3. Using a different simulation suite than TNG-300 is a real
   re-scoping of H1b's own pre-registered `claim.md`/`estimand.md`
   (`experiments/20260701-h1b-whim-thermal-mass-bias/`) — this needs
   its own dated AMENDMENT (same discipline as AMENDMENT 1/2 for the
   criteria), not a silent substitution, before any test runs.

**Consequence:** H1b stays parked. This is a real, specific,
better-than-before lead — worth a `pearl_registry` row with a
`next_check` — not yet a revival.

### Portal search, 2026-09-09 — six channels tried, bounded, all failed for stated reasons

| channel | result |
|---|---|
| `the300-project.org` (root) | DNS `getaddrinfo ENOTFOUND` |
| `www.the300-project.org` | DNS `getaddrinfo ENOTFOUND` |
| `weiguangcui.github.io/the300/` (co-author's own page) | reachable, no data page, itself points to `the300-project.org` |
| `nottingham.ac.uk/astronomy/The300/` | reachable, no data page, same pointer, plus a PBworks wiki link explicitly requiring permission |
| `web.archive.org` | tool-level block — cannot fetch this host at all from this environment |
| VizieR (`vizier.cds.unistra.fr`) | blocked the request itself, anti-bot protection ("Anubis") |

Two independent, authoritative sources (a paper co-author's own page, a
university astronomy department page) both confirm `the300-project.org`
IS the correct canonical address — this is not a wrong-URL problem.

**[UPDATED 2026-09-09] Confirmed via the user's own Chrome, real
network — not a sandbox artifact.** `the300-project.org` (https and
http both) returns a genuine browser error page from a real, unrestricted
browser too. **Control test, same browser, same network:**
`weiguangcui.github.io/the300/` (a co-author's mirror page) loads fine
immediately after. This isolates the failure to the domain itself —
the canonical portal appears to be genuinely down at this point in time
(2026-09-09), not blocked by this session's sandbox.

**Working substitute found**, read in full: `https://weiguangcui.github.io/
the300/` — confirms 324 clusters, the intro paper (Cui et al. 2018) and 3
follow-up papers, restates "all simulations and derived data products are
publicly available" **without a direct download link**, and points to two
workshop pages not yet checked: `popia.ft.uam.es/CrystalClearClusters/`
and `popia.ft.uam.es/GlenfiddlingGalaxyClusters/`.

**[UPDATED 2026-09-09] Both workshop pages checked — also dead.** Both
`popia.ft.uam.es/CrystalClearClusters/Home.html` and `.../
GlenfiddlingGalaxyClusters/Home.html` fail identically, by two
independent methods: `WebFetch` gets `ECONNREFUSED` on the host itself
(not a missing page — the host refuses the connection), and a real,
unrestricted Chrome browser shows a generic connection error on both
URLs. Same host, two paths, two tools, same result — the university
server behind this 2018-era workshop domain (`popia.ft.uam.es`) appears
to no longer be running at all, not just this one page moved.

**Consequence:** every web lead from the co-author's own mirror page has
now been checked and is dead. Three of three "The Three Hundred"-hosted
addresses (main portal, workshop 1, workshop 2) are down; only the
co-author's static GitHub Pages mirror survives, and it carries no data
link. **Genuinely blocked on this specific search path** — not from lack
of trying, from the collaboration's own infrastructure being
unreachable, control-tested across two tools and (for the main portal)
two independent networks.

### Round 2, 2026-09-09 — 3 more channels tried, all closed

- **Published journal version** (A&A 634, A113, `doi:10.1051/0004-6361/
  201936742` — the paper is A&A, not MNRAS as this file's own AMENDMENT 2
  section header once assumed; corrected here) — read in full via a real
  browser (WebFetch itself hit a `403` on this host, matching the
  VizieR block pattern above). Full-text grep for `data availability`,
  `CDS`, `VizieR`, `cdsarc`, `zenodo`, `available at http` —
  **zero matches, all patterns.** The published version carries no data
  deposit statement either.
- **`github.com/weiguangcui/pymsz`** — a real, live repository (unlike
  the dead web portals), but confirmed pure analysis/mock-observation
  code (SZ-map generation), no data catalog, no mention of The Three
  Hundred's own cluster properties.
- **ADS** (`mcp__astroquery__ads_*`, checks for a paper's own "data
  links" tab, which sometimes surfaces linked datasets a web search
  misses) — `BLOCKED-INFRASTRUCTURE`: no ADS API token configured in
  this environment (`API_DEV_KEY` unset). Not a null result — the
  channel itself could not be tried.

**Consequence:** every channel triable without a human step (a
collaboration website, a GitHub org, a journal's own supplementary
material, VizieR, ADS) is now either dead, empty, or blocked by missing
credentials. **The remaining paths all require a human**: contact the
authors directly (Ansarifard, Cui, or Li — institutional emails are in
the papers themselves), configure an ADS API token
(`https://ui.adsabs.harvard.edu/user/settings/token`) and retry that one
channel, or retry the three dead URLs weeks/months later.

Do not re-attempt any of the now-9 checked channels (3 web portals + A&A
+ VizieR + pymsz + TNG catalog + Barnes+2020 full-text + ADS) again
without a stated, specific reason to expect a different result this
time.

### Primary-source confirmation, same day — user supplied the actual PDF

The user provided `aa36742-19.pdf` (the published article) directly.
Read Appendices A/B/C and both reference-list pages in full, not via
search. **Confirms the null result first-hand, not by inference:**

- Tables B.1, B.2, C.1 are all class-level summaries (median/σ/skewness,
  Spearman-ρ per morphology class) — no per-cluster rows.
- **Fig. A.1** ("Hydrostatic mass bias vs. cluster mass at R500") plots
  individual clusters as scatter points ("each point refers to a single
  cluster") — so per-object values exist and were used internally — but
  **the points carry no ID label and are not tabulated.** Even
  digitizing this figure (a real, available technique — see
  `~/.claude/rules/artifact-provenance-gates.md` Gate 3) would not help:
  a digitized (mass, bias) pair still cannot be matched to a specific
  cluster's WHIM properties in Li+2025 without an ID, which the plot
  does not carry.
- No data-availability/CDS/Zenodo language anywhere in the
  Acknowledgements or References — matches the earlier full-text search
  exactly, now confirmed by reading the actual published pages.

**This closes the search for this specific paper definitively** — not
"not found by search," but "read the primary source directly, the
per-cluster key does not exist in it, structurally (unlabeled scatter
points), not just administratively (no stated data release)."

---

## TNG ACCESS — REQUESTED 2026-09-07, awaiting admin approval

**Status change on Revival Condition 1**, from *not attempted* to
*submitted, pending*.

Sergey submitted an account request at `tng-project.org`. The site's own
reply: the request needs administrator approval ("a few minutes, though
outside US-Eastern business hours it may take several hours"), after
which a confirmation email with an activation link is sent.

**Re-probed the same day, before the request:**

| endpoint | status |
|---|---|
| `https://www.tng-project.org/` | **200** — site up, network fine |
| `https://www.tng-project.org/api/` | **403** |
| `https://www.tng-project.org/api/TNG300-1/` (H1b's target) | **403** |
| `https://www.tng-project.org/api/TNG100-1/` | **403** |

`200` on the root against `403` on the API is a precise diagnosis: not a
network or outage problem, an authorisation refusal. Also checked and
absent: any `TNG*`/`ILLUSTRIS*` environment variable, `~/.tng`,
`~/.tng_api_key`, `~/.config/tng`, and any key-shaped variable in the
repo.

**Do not re-submit a second request** — one is already in the queue.

**When the activation email arrives**, the key goes into an environment
variable (`TNG_API_KEY`) or a file outside the repository — never into a
chat message and never into a tracked file. Verifying it then costs one
command: `403 → 200` on `/api/TNG300-1/`.

**Unchanged by this:** Revival Condition 1 is satisfied only when access
is actually *granted*, not when it is requested. And the pre-condition
above stands regardless — **Step 4a (floor–ceiling) runs BEFORE the test,
not after.**
