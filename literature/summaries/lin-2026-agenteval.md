# Mining Workflow Graphs for Black-Box Boundary Testing of Conversational LLM Agents

- **Authors:** Liting Lin; Boxi Yu; Yuzhong Zhang; Lionel Briand; David-Paul Niland; Emir Muñoz
- **Year / first version:** 2026 / 2026-07-08
- **Venue / status:** arXiv preprint – preprint
- **Link:** https://doi.org/10.48550/arXiv.2607.06873 ; https://arxiv.org/abs/2607.06873
- **Directions (working numbering):** 2 discovery/behaviour mining, 3 conformance
- **Record:** R00018 · relevance high · citation check PASS (2026-11-18)

## What they did
AGENTEVAL mines a conversational workflow graph (activities as nodes, user actions as edges) from black-box interaction with an agent and generates boundary tests at each node; evaluated on four tau-bench agents.

## Key findings
AGENTEVAL covers 38.8–46.0 distinct workflow boundaries per agent on tau-bench agents and approaches a white-box auditor.

## Limitations / future work
All metrics depend on an LLM auditor; limited to four benchmark agents; workflow-graph mining is model-specific rather than standard process discovery.

## Why it matters for the thesis
Process-discovery idea (activities from interaction) used for testing; relevant to discovery on conversational agents.

_Paraphrased notes written from the full text; not a substitute for reading the paper. Screening pending Frank's verification._
