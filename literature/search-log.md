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

## Screening – calibration pilot 1 (batch b001, 25 records) – 2026-11-18

- Two blinded AI reviewers (Claude Sonnet 5.5, SR-Screener `screening-reviewer-agent`) vs Frank's independent labels.
- AI agreement A vs B (advance vs exclude): n = 25, observed 0.92, kappa 0.834, PABAK 0.84; 2 conflicts (R00006, R00021) awaiting adjudication.
- Against Frank: 23 compared, Frank advanced 15, AI advanced 14, **AI missed 1** (R00024 AgBench: Frank unclear, both AI reviewers excluded E5), AI advanced 0 that Frank excluded.
- Result: **pilot gate not passed** → protocol wording to be amended and the pilot re-run before the full run.

## Screening – calibration pilot 2 (batch b001, protocol v1.1) – 2026-11-18

- Same set-up as pilot 1 (two blinded Sonnet 5.5 reviewers), protocol v1.1.
- AI agreement A vs B: n = 25, observed 0.96, kappa 0.911, PABAK 0.92; 1 conflict (R00006, A exclude E5 / B unclear) → adjudicator: unclear (advance). Frank's override (include) is the final decision.
- Against Frank: **25 compared, Frank advanced 17, AI advanced 17, AI missed 0**, AI advanced 0 that Frank excluded (agreement 1.0, kappa 1.0). R00024 (AgBench) is now advanced by both reviewers.
- Result: **pilot gate passed** → full title/abstract run on b002–b003.

## Screening – full title/abstract run (all 75 records, protocol v1.1) – 2026-11-18

- Two blinded AI reviewers (Claude Sonnet 5.5, SR-Screener 1.0.0 `screening-reviewer-agent`) on b001 (pilot 2) and b002–b003; third-reviewer adjudication of 4 advance/exclude conflicts (all → unclear, i.e. advanced; R00006 then set to include by Frank's override); required QC recheck of all 14 joint exclusions by a senior AI reviewer (1 advanced: R00045). 11 reviewer calls in total.
- Agreement A vs B (advance vs exclude): n = 75, observed 0.947, kappa 0.842, PABAK 0.893.
- Decided by: A+B 69, adjudicator 3, QC 1, Frank (override) 2.
- Full log, RIS files and methods draft: `literature/screening/Screening_TA/`.

| PRISMA step (title/abstract) | Count |
|---|---|
| Records identified (all rounds) | 133 |
| Duplicates removed | 27 |
| Removed before screening: not 2026 | 31 |
| Records screened (title/abstract) | 75 |
| Records excluded (title/abstract) | 13 (E3: 3, E4: 4, E5: 6) |
| Reports sought for retrieval | 62 (43 include, 19 unclear) |

- E4 exclusions (4) are listed in `literature/background.md` (Frank's rule).
- **Counts are provisional until Frank verifies** every advanced record and a sample of exclusions (SR-Screener requires human sign-off).
