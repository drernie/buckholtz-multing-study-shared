# Specification Ablation Ladder — S1/S2 task packs (real data, ready to run)

Built 2026-07-12 for the "Consensus Is Not Verification" pilot (BRAI extension).
Grounded in real MCXC cluster data + real Moresco+2022 cosmic-chronometer H(z) data,
same formula as R011 (src/pearson_fit.py). NOT run against a genuine blind model yet — see blockers below.

## S1 — data fixed, F->H(z) mapping left open

```
You are given a modified gravity model and real astrophysical data. Your task: propose
values for two free parameters, beta_d and beta_q, that make the model's predicted H(z)
curve match the observed H(z) data as closely as possible. State your reasoning, your
final beta_d and beta_q values, AND explicitly list any additional assumptions or choices
you had to make that were NOT specified in this prompt (if any).

MODEL:
phi(z) = M500/D^2 - 2*beta_d*k_A*R500/D^3 + (beta_q*k_A*R500)^2/D^4
D = D0/(1+z)
H_MULT(z) is proportional to sqrt(phi(z))

CLUSTER DATA (real, from MCXC X-ray catalog):
cluster_id | z | M500 [Msun] | R500 [Mpc] | k_A=Ethermal/c^2 [Msun]
J0001.9+1204 | 0.2033 | 2.6927e14 | 0.9178 | 4.5931e8
J0003.1-0605 | 0.232 | 5.2188e14 | 1.1326 | 1.5167e9
J0003.8+0203 | 0.0924 | 1.7342e14 | 0.8233 | 7.7698e7
J0006.0-3443 | 0.1147 | 2.7122e14 | 0.9486 | 6.2777e8
J0006.3+1052 | 0.1698 | 2.9941e14 | 0.9621 | 5.3277e8
J0008.9+4110 | 0.1537 | 2.8963e14 | 0.9569 | 4.6438e8

TARGET H(z) DATA (real cosmic chronometers, Moresco et al. 2022):
z | H(z) [km/s/Mpc] | sigma
0.07 | 69.0 | 19.6
0.09 | 69.0 | 12.0
0.12 | 68.6 | 26.2
0.17 | 83.0 | 8.0
0.179 | 75.0 | 4.0
0.199 | 75.0 | 5.0
0.2 | 72.9 | 29.6
0.27 | 77.0 | 14.0

Give your final answer as: beta_d = ..., beta_q = ..., then list ADDITIONAL_ASSUMPTIONS: [...]
```

## S2 — everything fixed except beta_d, beta_q (adds the missing pieces from S1)

Same as S1, plus this block inserted before "Give your final answer":

```
FIXED COMPUTATIONAL PROTOCOL (do not deviate):
- D0 = 100 Mpc (anchor distance scale)
- H_anchor = H(z=0.09) observed = 69.0 km/s/Mpc (lowest-z data point, used as normalization)
- H_MULT(z) = H_anchor * sqrt(phi(z) / phi(z=0.09))
- To compare model to N cluster-CC pairs: for each cluster, pair it with the single
  closest-z target H(z) point from the table above (nearest-neighbor in z).
- Fit beta_d, beta_q by minimizing sum of squared residuals (H_MULT(z_i) - H_obs(z_i))^2
  over the 6 cluster-CC pairs, weighted by 1/sigma_i^2.
- Report the best-fit values and the resulting sum of squared residuals.
```

## Status (honest, not run cleanly yet)

- **TEST_DESIGNED: PASS** — both packs built from real project data, ready to send to fresh model sessions.
- **TESTED: BLOCKED today**, two independent reasons, both logged rather than papered over:
  1. **Infra**: Ollama (the intended open-weight / provider-diversity leg, MCP tool
     `mcp__ollama__ollama_general_task`) is not running locally (`Cannot connect to
     Ollama... localhost:11434`, confirmed via `tasklist` — no ollama process).
  2. **Blinding failure**: Claude (this session) cannot serve as a valid S1/S2 subject
     itself — it already knows the reported answer (beta_d=4.5, beta_q=18.0) and the
     R011 finding (monopole beats full formula) from the surrounding session context.
     Running S1/S2 "on itself" here would not be a blind trial; the experimental design
     explicitly requires "no knowledge of expected beta, no access to prior results."

## To actually run this

Needs genuinely separate, blind sessions: paste S1 into a fresh ChatGPT/Gemini/Claude
chat (new conversation, no project context) and separately into a running Ollama
instance, once for S1 and once for S2, n=1 each as a first pilot (the full design calls
for n=5 x 4 models x 4 levels = 80; this is the cheapest possible first slice: 2 models x
2 levels x 1 run = 4 data points, enough to see if the S1->S2 specification gain is even
in the right direction before investing in the full grid).
