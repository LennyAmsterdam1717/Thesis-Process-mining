# GRADE: Graph Representation of LLM Agent Dependency and Execution

- **Authors:** Yue Zhao
- **Year / first version:** 2026 / 2026-06-22
- **Venue / status:** arXiv preprint – preprint
- **Link:** https://doi.org/10.48550/arXiv.2606.22741 ; https://arxiv.org/abs/2606.22741
- **Directions (working numbering):** 1 event data, 2 discovery/behaviour mining
- **Record:** R00043 · relevance high · citation check PASS (2026-11-18)

## What they did
GRADE: one graph holding both execution and dependency edges of agent runs, each dependency edge graded as observed, logged or inferred; recovered from six corpora and tested for failure prediction against a run-size baseline.

## Key findings
Dependency edges add failure-prediction signal over run size in some corpora, but a degree-matched counterfeit is not separated within a corpus.

## Limitations / future work
Gains depend on learner and task sampling; recovered structure does not beat a degree-matched counterfeit within corpus; mostly exploratory.

## Why it matters for the thesis
Warns that graph structure from traces can be spurious; methodological caution for any discovery-based RQ.

_Paraphrased notes written from the full text; not a substitute for reading the paper. Screening pending Frank's verification._
