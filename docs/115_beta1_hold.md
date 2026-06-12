# docs/115 — BETA-1 Hold Pointer

**Date:** 2026-06-13  
**Gate:** BETA-1 — controlled AI β replication  
**Status:** INFRA_READY / AWAITING_RESPONSES / HOLD

```
BETA-1 infrastructure prepared at commit 069ceaa.
Status: AWAITING_RESPONSES / HOLD.
No external LLM replication has been executed.
BETA-0 remains authoritative for β status until Q3 or BETA-1 execution.
```

---

## Why HOLD

BETA-1 is a useful forensic gate, but not the critical path.  
The main blocker remains **Q3**:

> *Are β_d and β_q physical constants, author-selected phenomenological parameters, or AI-fitted coefficients?*

BETA-1 possible verdicts and their limitations:

| Verdict | What it proves | What it does NOT prove |
|---------|---------------|------------------------|
| `CONVERGE` | Controlled prompting produces AI consensus | β are physically motivated |
| `DIVERGE` | Ambiguity persists under controlled conditions | β are AI hallucinations |

Either way, BETA-1 reaches at best `AI_CONSENSUS_CANDIDATE` — not `PHYSICAL_CONSTANT`.  
Q3 (TJB author provenance) is the only path to physical grounding.

---

## Execution Conditions

Do NOT execute (start LLM sessions) until:

1. TJB does not answer Q3 by ~2026-07-12 (consider as supplementary evidence only), OR
2. Explicit user decision to run controlled AI replication

---

## Infrastructure Location

| Artifact | Path | Status |
|----------|------|--------|
| Analysis script | `scripts/beta1_controlled_replication.py` | READY — 44/44 tests |
| Standardized prompt | `data/beta1_responses/prompt_v1.md` | READY |
| Cluster param table | `data/beta1_responses/galaxy_cluster_parameters_v1.csv` | READY |
| Response template | `data/beta1_responses/response_template.csv` | READY (empty — do not fill yet) |
| Baseline report | `reports/beta1_controlled_replication.json` | AWAITING_RESPONSES |

When authorized: fill `{service}_response.csv` for ≥ 3 services → run script → verdict.

---

*BETA-1 · AI_CONVERGENCE_TEST · HOLD · NOT_EXECUTED · OUR_RECONSTRUCTION*  
*docs/115 issued 2026-06-13*
