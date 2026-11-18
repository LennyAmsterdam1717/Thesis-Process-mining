# Background reading (outside the review corpus)

Frank's rules (see `docs/decisions.md`, 2026-11-18):

- **E4** papers (an LLM or agent *does* process mining or BPM tasks on ordinary business event logs, and the agents' own behaviour is not analysed) are kept here as background, not discarded.
- **Single-LLM papers** excluded at full text because the LLM neither uses tools nor acts in an environment are also kept here (section 2).

These papers are not used to justify a research question. They have not been citation-checked; run the citation check before citing any of them.

## 1. E4 exclusions at title/abstract (4)

| Record | Title | First authors | Venue / status | Link | Why E4 |
|---|---|---|---|---|---|
| R00004 | Exploring LLM Features in Predictive Process Monitoring for Small-Scale Event-Logs | Padella, de Leoni, Dumas | arXiv preprint (TMIS submission) | https://doi.org/10.48550/arXiv.2601.11468 | LLM used for predictive monitoring of business logs. (In the pilot, Frank coded this one E3, a non-agentic LLM; both AI reviewers coded E4, so it is listed here either way.) |
| R00007 | PMAx: An Agentic Framework for AI-Driven Process Mining | Antonov, Kourani, Berti | arXiv preprint (EMMSAD 2026 demo, under review) | https://doi.org/10.48550/arXiv.2603.15351 | Agents perform process mining on business logs |
| R00014 | Grounding LLM Explanations for Process Mining via Agentic Function Calling | Kalashnikov, Amling, Dormagen | CEUR Workshop Proceedings Vol-4259 | (CEUR page; no DOI) | LLM function calling explains process-mining outputs |
| R00027 | Towards Agentic AI for Event Log Data Quality Assessment | (authors not in record) | Springer chapter | https://doi.org/10.1007/978-3-032-28117-3_23 | Agentic AI assesses event-log quality |

## 2. Full-text exclusions kept as background (1)

| Record | Title | Author | Venue / status | Link | Why |
|---|---|---|---|---|---|
| R00005 | Beyond Pass/Fail: Using Process Mining to Understand How LLMs Resist (and Fail) Red Team Attacks | Topol | arXiv preprint | https://doi.org/10.48550/arXiv.2606.07833 | Single LLM in multi-turn red-teaming; no tools or environment (Frank's single-LLM rule). Methodologically close: it mines DFGs and transition matrices from 8,575 scored attack events, so it is a useful template for process mining of LLM interaction logs. |
