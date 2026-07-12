# Specification Ablation Ladder — Pilot Results (n=1, single model: Codex/GPT-5.5)

**Status:** PILOT / CANDIDATE — not the full design (4 models x 4 levels x 5 reps = 80 runs).
This is the cheapest possible first slice: 1 model x 2 levels x 1 run = 2 data points,
run via `codex exec` from a neutral working directory (no project context, no web access)
to keep the trial genuinely blind. Full transcripts: `s1_prompt.txt` was run inline
(output captured in session transcript, not auto-saved to a file — key numbers below are
verbatim from that run); `s2_prompt.txt` output is `s2_codex_transcript.txt` (full, auto-saved).

## Why this exists

Extension of R007 (BRAI: ChatGPT/Claude/Gemini gave beta_d/beta_q spread of up to 95x on
the same task). Original BRAI prompt never disentangled two competing explanations:
H2 (models are unreliable) vs H3 (the task itself was under-specified, so different models
legitimately solved different problems). This pilot tests H3 directly, within one model,
by holding the model fixed and only varying how much of the computation is pre-specified.

## S1 — data fixed, F->H(z) mapping left open (`s1_prompt.txt`)

Real MCXC cluster data (6 clusters) + real Moresco+2022 H(z) points given; formula given;
D0, normalization constant, and the cluster<->H(z) comparison procedure NOT specified.

- **beta_d = 1.185e5, beta_q = 0.0054** (Codex chose D0=1 on its own)
- Model explicitly self-flagged **7 additional assumptions** it had to make:
  D0 value, multiplicative normalization constant, interpolation method for matching
  cluster z to target z, endpoint extrapolation rule, weighting scheme, positivity
  constraint on phi, and the beta_q sign-degeneracy note.

## S2 — everything fixed except beta_d, beta_q (`s2_prompt.txt`)

Same data, same formula, PLUS: D0=100 Mpc, H_anchor=H(z=0.09)=69.0 km/s/Mpc explicit,
nearest-neighbor cluster-to-target pairing rule explicit, weighted-least-squares fit
objective explicit.

- **beta_d = 1.368e8, beta_q = 8.254**, weighted sum of squared residuals = 0.818
- Only **4 near-trivial clarifying notes** remained (how to evaluate phi(anchor) per
  cluster, sign convention, reality constraint, which endpoint the H_anchor instruction
  overrides) — none are real remaining degrees of freedom, unlike S1's list.

## Findings

1. **H3 confirmed within-model**: specification collapses the assumption list from 7
   substantive choices (S1) to 4 trivial ones (S2). Under-specification, not (only)
   model unreliability, drove at least part of the original BRAI divergence.
2. **Unexpected, unconfirmed pearl**: S2's beta_q=8.254 sits within ~2% of Gemini's
   original reported beta_q=8.10 (`src/beta_provenance.py` / R007), despite this Codex
   session having zero shared context with the original BRAI run. beta_d does not
   converge similarly (differs by orders of magnitude from Gemini's 4.25 — most likely
   a different D0/unit convention on Gemini's side, not verified). See pearl_registry
   entry 2026-07-12 for the falsifiable follow-up test.

## What this does NOT show

- Not a multi-model result — only Codex was run blind. Claude (this session) was
  explicitly excluded as a subject because it already knows the reported answer and
  the R011 finding (contamination), and Ollama was unavailable locally (infra blocker,
  not a design choice).
- n=1 per condition — no variance estimate, no CV, no bootstrap CI. The full design's
  metrics (Conditional Wrong Agreement, Majority Gain, UAR, FDR) cannot be computed yet.
- The S2 nearest-neighbor pairing collapsed 6 clusters onto only 4 unique H(z) target
  points — a real coarseness in this pilot's own spec, not fixed before running. A
  follow-up should either use interpolation or a larger/denser H(z) table.
- Does not by itself say anything about whether MULTING is physically correct — this
  result is about AI-assisted-science reproducibility methodology, independent of
  MULTING's own status (per R011: monopole already beats the full formula on this task).

## Next step (not yet done)

Run the identical `s2_prompt.txt` through fresh ChatGPT and Gemini sessions (no shared
context) to see whether beta_q dispersion collapses across genuinely different providers,
not just within Codex. This is the cheapest differentiating test for H2 vs H3 at the
multi-model level.
