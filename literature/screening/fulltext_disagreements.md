# Full-text disagreements – first vs second reviewer (for Frank to decide)

_2026-11-19. First reviewer: Claude Opus 5.5 (single-reviewer full text, "go light"). Second reviewer: Claude Sonnet 5.5, SR-Screener `screening-reviewer-agent`, persona B (methodologist), blinded to the first decisions, reading the pypdf-extracted text of each report with page markers. **No decision has been changed.** Write your decision in the last column; until then the first decision stands in `papers.csv` and the PRISMA counts._

## Set and agreement

- Checked: 24 reports = all 8 full-text exclusions + all 7 "low relevance" includes + a random 20% sample (9 of 44) of the other includes (Python `random.Random(20261118).sample`, from the sorted list of the 43 other FT includes plus the CEUR seed).
- Sample drawn: R00002, R00003, R00008, R00024, R00029, R00037, R00040, R00048, R00074.
- Agreement (include vs exclude): **16 / 24 = 66.7 %**, Cohen's kappa **0.08**, PABAK 0.33. By group: exclusions 1/8 agree; low-relevance includes 6/7; random includes 9/9.
- Kappa is low partly by design: the set is weighted towards the borderline records (all exclusions and weakest includes), so it does not estimate agreement on the whole corpus. The random includes agree 9/9.
- **Pattern:** in 7 of 8 disagreements the second reviewer would *include* what the first excluded. Most turn on concept (e): the second reviewer accepted efficiency or cost tables (tokens, latency, steps) as a "stated analysis", where the first reviewer applied the stricter full-text rule (comparison must be part of the stated analysis, not a side metric). Two are surveys/position papers (R00028, R00045) that the second reviewer accepted under concept (a).
- **Reading coverage caveat:** the second reviewer was told to read the whole file in 400-line parts, but its tool counts suggest it often read only the first part of long reports (estimated coverage below, = reads × 400 lines ÷ file lines; an estimate, not a measurement). Low-coverage decisions (e.g. R00045 ~20 %, R00028 ~41 %) rest mainly on abstract, introduction and early sections.

## Disagreements

| Record | Title | First reviewer (Opus) | Second reviewer (Sonnet) | 2nd coverage | Frank's decision |
|---|---|---|---|---|---|
| R00025 | A Vocabulary for Multi-Agent Automated Research Systems | **exclude E5**: Conceptual vocabulary for research-agent design; no trace data model or behavioural analysis (Sec. 4, 6) | **include INC**: 2026 arXiv position/vocabulary paper for LLM multi-agent systems; formal per-step trajectory data model, cost accounting, and comparison of agent designs. (p7-8 Sec. 4 Trajectory (Eq. 5-7); p1 Abstract; p9-15 Sec. 6 Case studies) — note: Reviewer note: borderline, low-relevance include; conceptual, no process mining or empirical trace study; meets (a) via formal trajectory record and (e) via design-comparison framework; included under the sensitive principle. | ~100 % | |
| R00028 | Reinforcement Learning for LLM-based Multi-Agent Systems through Orchestration Traces | **exclude E5**: RL training survey: orchestration traces used as reward/credit units, no behaviour analysis (Abstract, Limitations) | **include INC**: 2026 arXiv survey of LLM multi-agent systems; orchestration traces as event graphs with a replayable JSON trace schema (concept a). (p1 Abstract; p34-35 Sec. 8.1 Orchestration trace; p67 App. C.7 Trace schema) | ~41 % | |
| R00036 | Silent Failure in LLM Agent Systems: The Entropy Principle and the Inevitable Disorder of Autonomous Agents | **exclude E5**: Entropy principle from output consistency over trials; no trace or process analysis (Abstract, Sec. 3) | **include INC**: arXiv Jun 2026; LLM multi-agent hand-off fidelity measured across hops/rounds/runs; bare vs guarded configs compared; rule-check deviation monitor (borderline, low relevance) (p1 Abstract; p2-4 Sec. 2 taxonomy; p7-9 Sec. 6 Experimental Verification; p9 Sec. 7.2 PIG Engine) | ~100 % | |
| R00044 | Inference-Time Graph Engineering for Multi-Agent LLM Workflows | **exclude E5**: New multi-agent graph framework evaluated on accuracy; no trace or behavioural analysis (Abstract, Sec. 5) | **include INC**: Multi-agent LLM system (2026 arXiv); compares designs on time, tokens and cost, and analyses communication graph patterns across rounds. (p1 Abstract; p6 Sec. 4.2 Efficiency, Tables 2-3; p7-8 Sec. 4.3 GAIA graph analysis) | ~93 % | |
| R00045 | Graph Engineering in the Era of LLM Agents: From Individual Intelligence to System Intelligence | **exclude E5**: Survey of graph engineering for agent systems; trace analysis only named as future need (Abstract, Sec. Evaluation) | **include INC**: 2026 survey of LLM multi-agent systems; covers execution-state recording, trace-based fault localization, workflow graphs, agent communication and coordination structures. (p1 Abstract; p19-22 Sec. 4.4 Runtime State Management (4.4.1-4.4.2); p15-19 Secs. 4.2-4.3; p29 Sec. 7) | ~20 % | |
| R00046 | AgentConductor: Topology Evolution for Multi-Agent Competition-Level Code Generation | **exclude E5**: RL-trained topology generator; token cost as side metric, no behavioural trace analysis (Abstract, Sec. 3) | **include INC**: LLM multi-agent system; compares agent topologies on token cost and interaction density against baselines as a stated result (abstract, Table 3). (p1 Abstract; p6 Sec. 3.2.2 and Table 3 (cost and density comparison); p7 Fig. 5) | ~95 % | |
| R00052 | Robust and Efficient Tool Orchestration via Layered Execution Structures with Reflective Correction | **exclude E5**: New tool-orchestration method evaluated on pass and win rates; no trace analysis (Abstract, Sec. Evaluation Metrics) | **include INC**: LLM tool-using agents; execution designs compared on tokens and steps as a stated analysis, meeting concept (e); layered structure guides agents. (p1 Abstract; p2 Contributions; p7-8 Sec. 4.2.5 Efficiency Analysis, Table 2) | ~59 % | |
| R00062 | guardscope: Measuring Which Actions Runtime Controls Check in LLM Agent Systems | **include INC**: Agent actions reconciled with kernel-level ground truth to measure runtime-control coverage (Abstract, Sec. 5) | **exclude E5**: Agent security: measures runtime-control coverage of fixed replayed actions against kernel truth; no analysis of agent behaviour as process data (p1 Abstract; p6-7 Sec. 4.3 Empirical Measurement (no LLM in loop, deterministic replay of 15 actions)) — note: Reviewer note: read lines 1-800 of 1163 (skipped evaluation results, limitations, references). Borderline E5: framework logs dispatch records reconciled with kernel traces (resembles concept a), but the object of analysis is control coverage, not agent behaviour across runs. | ~69 % | |

## What changes if you side with the second reviewer

- Each of the 7 exclusions you overturn adds one paper to `papers.csv` (after its citation check and a full-text-based row) and changes the full-text PRISMA counts (excluded 8 → fewer, included 50 → more).
- If you exclude R00062, `papers.csv` loses one low-relevance paper; it supports no RQ directly.
- None of the disputed papers is cited as evidence for a shortlisted RQ (RQ-A, RQ-B, RQ-C), so no RQ evidence base changes either way. R00044 (ReActNet) and R00046 (AgentConductor) would add topology/cost comparisons relevant to RQ-A/RQ-B background.

## Agreements (for completeness)

| Record | Group | Both |
|---|---|---|
| R00002 | random include | include |
| R00003 | random include | include |
| R00005 | exclusion | exclude |
| R00008 | random include | include |
| R00024 | random include | include |
| R00029 | random include | include |
| R00037 | random include | include |
| R00038 | low-relevance include | include |
| R00040 | random include | include |
| R00047 | low-relevance include | include |
| R00048 | random include | include |
| R00049 | low-relevance include | include |
| R00051 | low-relevance include | include |
| R00059 | low-relevance include | include |
| R00063 | low-relevance include | include |
| R00074 | random include | include |
