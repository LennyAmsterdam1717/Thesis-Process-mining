# Literature search log

One entry per search round. PRISMA 2020 counts come from `sr-screener`.

**Review form:** integrative review (ARS `lit-review` mode) with a scoping purpose. See `docs/decisions.md` (2026-11-18) for eligibility criteria and the search plan.

**Search tools available in this run:** web search (general web index, which covers arXiv, ACL Anthology, CEUR, Springer, ACM, IEEE and OpenReview pages) plus direct reads of arXiv abstract pages. Bibliographic databases such as Scopus or Web of Science were not queried directly; counts below are records returned by web search, not database hits.

<!-- Copy this template for each round:

## Round N – YYYY-MM-DD

- **Question / focus:**
- **Sources searched:** (e.g. Scopus, Web of Science, ACM DL, Google Scholar)
- **Search string:**
- **Date range / filters:**

| PRISMA step | Count |
|---|---|
| Records identified | |
| Duplicates removed | |
| Records screened (title/abstract) | |
| Records excluded (title/abstract) | |
| Reports sought for retrieval | |
| Reports not retrieved | |
| Reports assessed (full text) | |
| Reports excluded (full text, with reasons) | |
| Studies included | |

- **Full-text exclusion reasons:**
- **Notes:**
-->

## Round 1 – 2026-11-18 – Broad: process mining of AI-agent behaviour

- **Question / focus:** Which 2026 papers treat LLM / GenAI agent execution as event data or apply process mining to agentic systems?
- **Sources searched:** web search (extended mode), results from arXiv, CEUR-WS, Springer, ScienceDirect, MSR 2026 site, ResearchGate.
- **Date range / filters:** none in the query engine; the 2026 filter is applied at screening.

| ID | Search string |
|---|---|
| Q1.1 | `process mining LLM agents event logs arXiv 2026` |
| Q1.2 | `"agent behavior mining" OR "agentic process mining" 2026` |
| Q1.3 | `process mining generative AI agent traces conformance checking 2026 paper` |
| Q1.4 | `event log LLM agent trajectories process discovery directly-follows graph tool calls 2026` |
| Q1.5 | `object-centric event data AI agents multi-agent system 2026 arXiv` |
| Q1.6 | `"agent system mining" OR "agent system event data" LLM 2026` |

- Scholarly records returned: **44** (35 new, 9 duplicates within the round). Vendor pages, blogs and news items were not counted as records.
- **Notes:** Q1.5 (object-centric) returned nothing that combines OCEL with LLM agents; this is itself a finding (see gap analysis).

## Round 2 – 2026-11-18 – Multi-agent interaction analysis (direction 4)

| ID | Search string |
|---|---|
| Q2.1 | `multi-agent LLM system interaction patterns handoffs communication traces analysis 2026 arXiv` |
| Q2.2 | `multi-agent system failure taxonomy traces coordination LLM agents 2026` |
| Q2.3 | `process mining multi-agent LLM collaboration social network handover of work 2026` |
| Q2.4 | `LLM multi-agent interaction graph topology analysis execution logs dependency structure empirical 2026` |

- Scholarly records returned: **28** (26 new to this round, 2 duplicates).
- **Notes:** Q2.3 (process-mining-style handover / social-network analysis of LLM multi-agent systems) returned no 2026 paper that combines these; the hits are pre-2026 or non-LLM.

## Round 3 – 2026-11-18 – Comparing agentic approaches (direction 6)

| ID | Search string |
|---|---|
| Q3.1 | `comparing agent architectures ReAct plan-and-execute behaviour trajectories analysis tool usage efficiency 2026 arXiv` |
| Q3.2 | `single-agent vs multi-agent LLM comparison trajectories cost coordination overhead empirical study 2026` |
| Q3.3 | `process mining compare LLM models agent behaviour variants prompting strategies event log 2026` |
| Q3.4 | `behavioral fingerprint agent trajectories across LLMs action sequence analysis SWE-bench 2026 arXiv` |
| Q3.5 | `BPM 2026 OR ICPM 2026 OR CAiSE 2026 LLM agents process mining paper` |

- Scholarly records returned: **28** (20 new, 8 duplicates). Q3.2 returned almost only blogs; one arXiv record.
- **Notes:** Q3.3 found no 2026 paper that uses process mining to compare models or prompting strategies on agent logs. Trajectory comparison work exists, but it uses n-grams, Markov chains or custom metrics, not process mining.

## Round 4 – 2026-11-18 – Other directions + citation chasing from seeds

| ID | Search string |
|---|---|
| Q4.1 | `"Agent Behavior Mining" Vu Kampik cited 2026 agents process mining runtime monitoring declarative constraints` |
| Q4.2 | `declarative process constraints LTLf runtime monitoring LLM agents guardrails 2026 arXiv` |
| Q4.3 | `OpenTelemetry agent traces XES OCEL conversion process mining LLM agent observability 2026` |
| Q4.4 | `LLM agent SOP workflow adherence compliance checking traces business process model 2026 arXiv` |
| Q4.5 | `process-aware LLM agents BPMN guided agent execution process mining feedback 2026` |

- Scholarly records returned: **33** (25 new, 8 duplicates).
- **Citation chasing:** the seed papers' reference lists were read in full (see `literature/summaries/`). All their references are from 2025 or earlier except the seeds themselves, so backward chasing gave no new 2026 papers. Forward chasing (papers citing the seeds) is not possible with web search alone; no citing paper was found.

## Identification totals (all rounds)

| PRISMA step | Count |
|---|---|
| Records identified (all rounds, incl. cross-round duplicates) | 133 |
| Duplicates removed | 27 |
| Unique records | 106 |
| Records removed before screening: not 2026 (year rule) | 31 |
| Records screened (title/abstract) | 75 |

Screening counts follow in the screening section below.
