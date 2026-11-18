# TraceCompiler: Skill-Guided Mining and Compilation of LLM Agent Traces into Mostly Deterministic Workflows

- **Authors:** Salma El Yadouni; Guanyi Li
- **Year / first version:** 2026 / 2026-08-03
- **Venue / status:** arXiv preprint – preprint
- **Link:** https://doi.org/10.48550/arXiv.2608.02680 ; https://arxiv.org/abs/2608.02680
- **Directions (working numbering):** 2 discovery/behaviour mining, 5 performance
- **Record:** R00008 · relevance high · citation check PASS (2026-11-18)

## What they did
TraceCompiler mines clusters of noisy tool-agent traces, recovers producer-consumer dependencies between tool calls with auditable evidence, and compiles them into mostly deterministic workflows; beats adjacency and directly-follows baselines on dependency recovery.

## Key findings
Rule-based dependency recovery reaches 0.93/0.94 precision/recall on 15,775 def-use edges versus ~0.71 F1 for adjacency and directly-follows baselines; compiled workflows cut API calls (34 → 11 in one intent).

## Limitations / future work
Offline compilation cost not measured (no break-even point); no semantics-preservation guarantee; evaluated on two compiled AppWorld intents plus T1.

## Why it matters for the thesis
Directly challenges the directly-follows abstraction for agent logs: data-flow between tool calls matters. Useful for an RQ on event abstraction / case notion for agent traces.

_Paraphrased notes written from the full text; not a substitute for reading the paper. Screening pending Frank's verification._
