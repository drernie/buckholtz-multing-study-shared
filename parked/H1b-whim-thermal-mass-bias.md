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

## Stage 2 DONE 2026-09-09 — 3 of 4 ingredients now computable at full
## scale (N=71), a real side-finding surfaced, 4th ingredient still
## external

`experiments/20260909-tng-whim-pilot/whim_batch_n71.py` →
`FINDING_stage2_batch_n71.md`. 71 real TNG300-1 clusters, 71/71 controls
pass, 65.3 min wall time. Real, statistically significant (p<0.001)
anticorrelation found between cluster mass and WHIM mass fraction
(`r=-0.429`) — a genuine side-finding, logged in `pearl_registry/
INDEX.md`, independent of H1b itself. Mean WHIM% (33.4%) sits well below
Li+2025's own reported ~70% plateau — a real, now N=71-quantified
discrepancy with 3 named candidate explanations, none yet resolved.

**Still unchanged: the actual H1b test cannot run.** `M_true` and
WHIM-fraction are now computable for any qualifying TNG-300 cluster —
but hydrostatic mass (`M_HE`/`delta_M`) remains external. **Update
2026-09-09, later same day: the data-request letter WAS sent**, to all
4 authors (Ansarifard/Rasia/Cui/Li), real verified addresses, via
browser automation after the Gmail MCP send tool failed systemically —
see `correspondence/draft_three_hundred_data_request_20260909.md`'s own
"Sent" section for the full account. No reply yet. This batch does not
move H1b's own correlation test forward by itself — it removes the "can
we even compute our half" uncertainty and means zero rework is needed
once/if the missing half arrives.

**Update, same day — the dynamical-state confound proxy IS now analyzed,
twice, both null.** The line above ("collected but not yet analyzed")
was live for under an hour. `group_nsubs`
(`experiments/20260909-tng-whim-pilot/check_nsubs_confound.py`, commit
`2244fb4`): collinear with mass (`r(logM,logNsubs)=0.596, p<0.001`), and
the mass-detrended residual has no relation to WHIM%
(`r=0.074, n.s.`) — not usable as an independent confound control.
CM/potential-minimum offset (`check_cm_offset_confound.py`, commit
`449ce63`, a second, independently-motivated standard proxy — Mohr et
al. 1993): same pattern, `r(logM,offset)=-0.543, p<0.001` collinear,
mass-detrended residual `r=-0.083, n.s.`, robust to its one outlier
(`r=-0.057` with halo 38 excluded). DM velocity dispersion within R200
(`velocity_dispersion_confound.py`, third and most tightly-collinear
proxy — `r(logM,log_sigma_v)=0.938, p<0.001`, a clean M-sigma-relation
positive control): mass-detrended residual `r=0.020, n.s.` — also null.
**Three different standard dynamical-state proxies now all come back
null at N=71** — real information (none is a usable confound control at
this sample size with these proxies), not proof dynamical state is
irrelevant. A synthetic-X-ray morphological classifier (Ansarifard+2019-
style) is the one remaining, methodologically different, untested
candidate. Full detail in each script's own commit and
`experiments/20260909-tng-whim-pilot/FINDING_stage2_batch_n71.md`'s three
addenda.

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

## 2026-09-10 — real, useful context found, not a data shortcut

`[VERIFIED-PDF]` de Andres, Cui, Yepes et al. (2024), *"The three hundred
project: mapping the matter distribution in galaxy clusters via deep
learning from multiview simulated observations,"* MNRAS 528, 1517-1530
(`doi:10.1093/mnras/stae071`) — read in full (user-supplied PDF).
**Weiguang Cui is a co-author** — one of the 4 recipients of the
2026-09-09 data-request letter.

**What it is:** a U-Net trained on The Three Hundred's own hydrodynamical
simulations (GADGET-X, GIZMO-SIMBA) to infer projected total-mass-density
maps from simulated SZ/X-ray/stellar-density observations, evaluated
against true simulated mass (bias `~1%`, scatter `~3%` for the best
multiview model).

**Data Availability statement (verbatim):** *"The results shown in this
work use data from The Three Hundred galaxy clusters sample. The data is
freely available upon request following the guidelines of The Three
Hundred collaboration, at https://www.the300-project.org."* — confirms
the request-based route already taken (09-09 letter) is the correct,
only path; no public catalog bypass exists.

**Real, usable context (not a data source):**
1. Cui's group is actively building ML tooling for exactly this class of
   question (observable-proxy-inferred mass vs true mass) — strengthens
   confidence he is a well-matched, currently-engaged contact for the
   pending request, not a passive co-author.
2. Their own bias quantity (ML-predicted total mass map vs true mass,
   `b_ρ = (M̂_ρ-M_ρ)/M_ρ`) is conceptually adjacent to but NOT the same
   as H1b's target `B_hydro = 1-M_HE/M_true` (classical hydrostatic-
   equilibrium mass, not an ML image-to-mass inference) — not a plug-in
   replacement.
3. Does not touch WHIM/filament gas at all — all apertures are `R200`/
   `R500` (cluster interior), not the `2-3×R200` region H1b's other half
   needs.

**Net effect on H1b's own blocked status: unchanged.** No new data
channel opened; real, useful context for interpreting a future reply.

## 2026-09-10 (second entry) — three more real papers, still no data
## shortcut; one genuinely new baseline number, one reusable methodology

User supplied 3 PDFs plus one pasted-text paper (verified via
`mcp__arxiv__get_abstract`). All four are real, on The Three Hundred,
and all confirm rather than change the blocked status.

**`[VERIFIED-PDF]` Gianfagna, Rasia, Cui, De Petris, Yepes,
Contreras-Santos & Knebe (2021), MNRAS 502, 5115** (`arXiv:2211.08372`)
+ its `EPJ Web Conf. 257, 00020` proceedings summary (same authors,
same content, no new information) — full hydrostatic-bias study on
~300 Three Hundred clusters, 9 redshifts (`z=0.07-1.32`). **Genuinely
new information not previously in this file:** real, published baseline
numbers for H1b's own outcome variable in this exact cluster sample —
median `b_X`/`b_SZ` ≈ 0.10-0.20 at R500, **no significant dependence on
mass or redshift**, disturbed clusters carry nearly all the scatter, and
bias goes **negative** (mass *over*-estimated) for ~1 dynamical time
right after a major-merger peak before recovering. Useful as a prior for
interpreting any future per-cluster result: since our own TNG-300 WHIM
finding (`r=-0.429` in `FINDING_stage2_batch_n71.md`) is mass-dependent,
a WHIM-driven bias mechanism would have to act mainly through the
disturbed/merger-scatter channel, not a smooth mass trend — this paper's
own null mass/z result on the bias side makes that distinction sharper
than before. **Data Availability (verbatim):** *"shared on request to
The Three Hundred Collaboration, at https://www.the300-project.org"* —
same portal already confirmed dead in the 2026-09-09 section above.
Tables 5-7 report only binned top/bottom-50 statistics (by concentration,
mass growth, `χ_DS`), not per-cluster IDs — no bypass here either.

**`[VERIFIED-arXiv]` Rost, Nuza, Stasyszyn, Kuchner, Hoeft, Welker,
Pearce, Gray, Knebe, Cui & Yepes (2023), `arXiv:2310.12245`** — confirmed
real via `mcp__arxiv__get_abstract` (title/authors/abstract match the
user-pasted text exactly). Filament thermodynamics/WHIM on The Three
Hundred's own 324 clusters (not TNG) — density/temperature/entropy/Mach
profiles via DisPerSe filament-finding + `2×R200` halo excision,
`WHIM ≡ 10⁵<T<10⁷K, n_H<10⁻⁴h²cm⁻³`. **Real, reusable methodological
template** if/when the data request succeeds: this collaboration already
has an established, published WHIM-extraction pipeline on their own
simulation, so a future H1b-equivalent run on Three Hundred (rather than
TNG-300) would not need to invent one from scratch — align with theirs
for direct comparability. Confirms filaments genuinely isolate cooler,
lower-entropy WHIM gas near the spine (`θ≈0` WHIM fraction → 1) and that
this WHIM is efficiently dragged toward the cluster, both independent of
and consistent in spirit with our own TNG-300 mass-anticorrelation
finding. **Data Availability (verbatim):** *"shared on reasonable
request to the corresponding author"* — again request-only, no bypass.
No hydrostatic-mass comparison anywhere in this paper — does not touch
H1b's other half.

**`arXiv:1911.07878` (Ansarifard et al. 2019/2020) re-confirmed, not
new.** This is the arXiv preprint of the paper already definitively
closed in the "Primary-source confirmation" section above (2026-09-09,
using the published `aa36742-19.pdf`). Read the preprint's own Appendix
A/B/C directly this time: identical structure — Fig. A.1 individual
scatter points with no ID labels, Tables B.1/B.2/C.1 class-level only,
no data-availability statement anywhere in the visible pages. Same dead
end, now confirmed from a second copy of the same paper — no new
information, standing closure unchanged.

**Net synthesis:** all 4 documents (5 counting the proceedings twin) are
real, all confirm the request-based route (letter sent 2026-09-09) is
the only channel and none leak a bypass, and — as with `stae071` the day
before — 3 of the 4 papers here (Gianfagna, Rost, and the already-closed
Ansarifard) carry **Weiguang Cui and/or Gustavo Yepes** as co-authors,
reinforcing again that the request went to people actively, currently
working on precisely this intersection (hydrostatic bias AND filament
WHIM, both on the same 324-cluster sample). No change to H1b's blocked
status. Two genuinely new, real, citable pieces of context worth keeping:
the Gianfagna baseline-bias numbers (for interpreting a future result)
and the Rost et al. WHIM-extraction methodology (for executing on Three
Hundred data without redesign, if/when it arrives).

## CORRECTION, same day — my own TIP (Mach-number comparison, previous
## entry above) rested on a pasted external "report" that misstates its
## own sources; direct verification finds a real disagreement, not the
## clean confirmation implied

Immediately after the entry above, I suggested comparing stacked
Mach-number distributions around filaments in The Three Hundred (Rost)
vs. TNG-300 as an unblocked, literature-only check. The user brought
back a pasted "research report" claiming this was already doable and
citing 3 sources. Per this session's standing discipline (verify every
external/pasted claim directly, never trust a pasted "AI report" at face
value — already exercised repeatedly this session), checked all three
via `mcp__arxiv__get_abstract`, `mcp__scholarly-lookup__find_by_doi`, and
`mcp__arxiv__search_papers`. Two of the three claims do not hold up.

**`[VERIFIED-arXiv]` Pastén, Gouin, Aghanim & Sorce (2026),
`arXiv:2604.24852`** — real, N=415 TNG-300 clusters, `z=0`, exactly the
filament-accretion topic needed. **But the pasted text's characterization
is backwards.** Its own abstract, verbatim: *"While virial shocks tend to
be observed near the cluster boundary, especially at the
filament-cluster interface. **We do not find strong evidence of
accretion shocks around filaments**, suggesting slow thermalization of
filament gas..."* — the pasted claim ("прямо фиксирует... более сильные
аккреционные удары M~100... воспроизводя картину Molnar/Baxter") states
the opposite of this paper's own headline finding for the filament
region specifically.

**This is a real tension worth keeping, not a wasted lead.** Rost et al.
(already read in full above) reports a genuine **shocked envelope
wrapping filaments** at intermediate angles (`10°≲θ≲30°`), distinct from
both the (unshocked) spine and the far void — their own Fig. 6/7 and
§4.2.1 text. Pastén et al. 2026, a different simulation and a different,
larger (N=415) cluster sample, explicitly does **not** find that
envelope. Two recent, real papers, looking at conceptually the same
question, disagree. That is a more interesting and more honest starting
point for the comparison than confirmed agreement would have been — but
it means any future write-up must say "these two pictures disagree,"
not "these two pictures match."

**`[VERIFIED-arXiv]` Łokas (2023), `arXiv:2304.13585`, "Merging galaxy
clusters in IllustrisTNG," A&A** (confirmed real via
`find_by_doi` on `10.1051/0004-6361/202345984`, then the arXiv full
abstract). The "median Mach ≈2" figure in the pasted text traces to a
real sentence here (*"the median Mach numbers of these gas cells are
around two"* — the pasted ".03" decimal is not in the source, false
precision). **But this paper is about something else entirely**: 10
examples of Bullet-Cluster-style **cluster-cluster merger bow shocks**
in the 200 most massive TNG-300 haloes — not filament accretion shocks,
not WHIM, no radial/angular profile around filaments at all. Citing it
as the "TNG-side" filament-Mach comparison point is a category error —
real paper, wrong phenomenon.

**`[VERIFIED-OUP]` Schaal, Springel, Pakmor et al. (2016), MNRAS 461,
4441** (fetched directly, quotes confirmed) — real, and its numbers are
close to but measurably inflated in the pasted text: paper says typical
accretion-shock Mach `≈2` (pasted text said "`~10`"), extreme cases
"several hundred" (pasted text said "up to `~1000`"). Detection threshold
`M≈1.3` **is** accurate as quoted.

**Consequence for the unblocked Mach-comparison sub-task named in the
entry above:** still genuinely unblocked (no data-portal dependency,
both real profiles are already published) — but the honest framing is
"Rost (Three Hundred) reports a filament-wrapping shock envelope; Pastén
2026 (TNG-300, N=415) explicitly does not find one — a real,
unreconciled disagreement between two 2023/2026 papers" — not a
confirmation exercise. Worth a `pearl_registry` row if pursued further;
not pursued in this session beyond verification. Łokas 2023 is not a
usable comparison point for this specific sub-task.

### Follow-up, same day — checked whether Rost and Pastén use the same
### shock-detection threshold. They don't; they use different KINDS of
### method entirely, which may itself explain part of the disagreement

`[VERIFIED-arXiv]` Downloaded and read `2604.24852` directly (not just
its abstract) — `mcp__arxiv__list_paper_latex_sections` +
`mcp__arxiv__get_paper_latex_section` + `search_paper_text`.

**Rost et al., §2.3** (already quoted in full above): a formal,
per-particle, **multi-criterion** shock finder following Nuza et al.
2012/2017 — convergent flow (negative velocity divergence) **and**
density increase **and** entropy increase downstream, all three
required; Mach number is computed via Rankine-Hugoniot only *after* a
particle already qualifies, taking the minimum of 3 derived values as a
conservative estimate. **No numeric Mach threshold appears anywhere in
this criterion** — detection is qualitative (3 physical conditions),
not a cutoff.

**Pastén et al., checked directly:** §3.1 ("Methodology") does not
mention Mach number or shocks at all — it only defines the isotropic/
anisotropic radial-profile machinery for `T`/`S`/`P`/`ρ`. The paper has
**no dedicated shock-finding section**. The Mach-number discussion
appears only in §6.2 ("Shock signatures..."), where a shock front is
identified **visually**, by inspecting a Mach-number map and reporting
where an elevated region sits ("we clearly observe a shock front near
`R_200` with `M∼2` in most of the clusters") — no stated detection
algorithm or threshold at all, and (`search_paper_text` for "shock
finder"/"sound speed": 0 hits both) apparently no formal one exists in
this paper.

**Neither paper uses Schaal et al. 2016's `M≈1.3` jump criterion** —
that comparison point (suggested as a next check in the entry above)
turned out not to apply to either source; dropped.

**Refines, does not overturn, the disagreement noted above.** Reading
Pastén's full text (not just its abstract) sharpens where the
disagreement actually sits: they **do** confirm a virial shock
(`M∼2` near `R_200`, "in most of the clusters") — roughly the same
radius as part of Rost's own "shocked envelope." They do **not** confirm
the stronger, further-out accretion shocks (`M∼100`, Molnar 2009/Baxter
2021) at `2-4R_200`. Rost's own filament-wrapping shocked-envelope
finding is specifically reported at `3-4R_200` (§4.2.1: "a large shocked
region centred at approximately 60°" in that same range) — so the real
disagreement is localized to the far zone, not the whole profile; the
earlier entry's blanket framing ("Rost finds one, Pastén finds none")
was itself slightly too coarse, now corrected. The pasted text's
original error stands as diagnosed: it merged the confirmed virial-shock
result with the unconfirmed far accretion-shock result into one blanket
"reproduces Molnar/Baxter" claim.

**Practical upshot:** a future quantitative comparison between these two
papers' Mach profiles would need to control for this methodological gap
(formal multi-criterion particle detector vs. visual Mach-map reading)
before treating any numeric disagreement as physical — the two papers
may not be measuring the same operational definition of "shocked" at
all. Not pursued further this session.
