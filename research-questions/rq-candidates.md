# Research-question candidates

_Status: draft for discussion with Dr. Xixi Lu. Based on 51 citation-checked 2026 papers (`literature/papers.csv`); screening pending Frank's verification. Gaps G1–G7: `gap-analysis.md`. Thesis window: 8 months from 4 Jan 2027 (if the 2-month extension is approved)._

Data-dependency labels: **Accenture internal** (logs of Accenture's own, non-client agents) · **Rebuilt case** (an agent system rebuilt from an Accenture/client scenario, run by the student) · **Public** (released traces or benchmarks).

---

## RQ-A (direction 6) – Comparing agent architectures as processes

**RQ:** To what extent do process-mining measures distinguish LLM-agent architectures (single-agent ReAct, Plan & Execute, multi-agent orchestration) running the same business process, beyond task success, latency and cost?

- **A1.** Which process-mining measures (fitness/precision against the intended BPMN model, model complexity, variant count and entropy, rework and retry loops, tool-error recovery paths) differ significantly between architectures?
- **A2.** Are these differences stable when the underlying LLM is swapped (architecture effect vs model effect)?
- **A3.** Do the process-level differences predict outcome quality and cost better than aggregate metrics alone?

- **Gap:** G2 (and G5).
- **2026 evidence:** Vu et al. [2606.20669](https://arxiv.org/abs/2606.20669) (ABM; limitation: ReAct only, one model) · Borman et al. [2607.14456](https://arxiv.org/abs/2607.14456) (specialist vs generalist, metric-only) · Dhanyamraju et al. [2606.20058](https://arxiv.org/abs/2606.20058) (DAG Plan&Execute vs ReAct, metric-only) · Ma et al. [2605.18332](https://arxiv.org/abs/2605.18332) (framework vs LLM effects with feature statistics).
- **Method:** controlled experiment. Implement 2–3 architectures over one business process (e.g. order-to-cash or procurement, as in the seeds) with the same tools and prompts, 2–3 LLMs, ~200–400 runs per cell; log with the ABM data model (OpenTelemetry → XES); analyse with PM4Py (inductive miner, alignments, variant analysis); statistical comparison (mixed models or permutation tests).
- **Data:** Rebuilt case (main) + Public (tau-bench-style tasks for replication); Accenture internal logs optional for external validity.
- **Feasibility (8 months):** high. M1–2 set-up and pilot, M3–5 experiments, M6 analysis, M7–8 writing. Risks: LLM API budget (mitigate with smaller or open models for part of the grid); non-determinism needs enough runs; "intended process" must be defined in advance for conformance.
- **Why Accenture:** gives evidence for choosing an agent architecture for a client process and a reusable way (ABM logs + standard process-mining tooling) to benchmark agent designs before deployment.

---

## RQ-B (direction 4) – Organisational mining of multi-agent interaction

**RQ:** Can organisational process-mining techniques (handover-of-work, social-network and role analysis) applied to multi-agent LLM event logs reveal coordination patterns associated with failure and cost, and how do they compare with trace-level LLM-judge diagnosis?

- **B1.** How must the event data model represent agents, hand-offs and shared context (ABM `transfer_to_agent` plus an agent entity, or an object-centric log) to support organisational mining?
- **B2.** Which interaction patterns (delegation loops, bottleneck agents, context growth along hand-off chains, lost constraints) are associated with failed or costly cases?
- **B3.** On labelled failure traces, how does process-mining-based diagnosis compare with taxonomy- or LLM-judge-based diagnosis in accuracy and cost?

- **Gap:** G1 (and G3).
- **2026 evidence:** Vu et al. [2606.20669](https://arxiv.org/abs/2606.20669) and Körner et al. [CEUR 4274/39](https://ceur-ws.org/Vol-4274/paper-39.pdf) (hand-off events, per-agent token disparity) · Pitre et al. [2610.32060](https://arxiv.org/abs/2610.32060) (communication-failure taxonomy) · Liu et al. [2610.10126](https://arxiv.org/abs/2610.10126) (topology recovery from traces) · Sun et al. [2608.24569](https://arxiv.org/abs/2608.24569) (constraint erosion in hand-offs) · Ma et al. [2610.14800](https://arxiv.org/abs/2610.14800) (enterprise interaction risks).
- **Method:** mixed. (1) Data-model design; (2) analysis of public labelled multi-agent traces released with 2026 papers (e.g. MAScope-Bench, Liu et al.; coordination traces, Nechepurenko & Shuvalov [2605.03310](https://arxiv.org/abs/2605.03310)); (3) controlled experiment with injected coordination faults in a rebuilt multi-agent case; comparison against an LLM-judge baseline.
- **Data:** Public (main, available from day 1) + Rebuilt case; Accenture internal multi-agent logs if available.
- **Feasibility (8 months):** medium–high. Risks: public trace formats differ (conversion effort); labels may not map to organisational patterns; multi-agent runs are costly. Mitigation: start with one public corpus, keep the experiment small.
- **Why Accenture:** multi-agent systems are where agent behaviour is hardest to see; a mining-based diagnostic for hand-offs supports governance and debugging of client multi-agent deployments.

---

## RQ-F (directions 4, 6) – Comparing multi-agent orchestration patterns with process mining

_Added 2026-11-20. Combines RQ-A's comparative design with RQ-B's organisational-mining measures, but stays entirely within multi-agent systems._

**RQ:** How do multi-agent orchestration patterns (supervisor/hierarchical, sequential pipeline, selector-based group chat) differ as processes – in control flow, hand-off structure and conformance to the intended business process – when running the same business process, and do these differences explain failures and cost beyond task success and token use?

- **F1. Control flow.** Which control-flow measures (fitness and precision against the intended BPMN model, variant count and entropy, rework and delegation loops) differ between orchestration patterns?
- **F2. Hand-off structure.** What do organisational-mining measures (handover-of-work and working-together networks, centralisation, bottleneck agents, ping-pong hand-offs, hand-off waiting time) show about how each pattern actually coordinates, compared with its designed topology?
- **F3. Failures and cost.** Which mined patterns (e.g. long hand-off chains, loops between two agents, a dominant coordinator) are associated with known multi-agent failure modes – constraints lost at hand-offs, skipped mandatory steps – and with cost, and do they stay stable when the underlying LLM is swapped?

- **Gap:** G1 + G2. 2026 work compares coordination set-ups with outcome metrics, failure taxonomies or LLM judges, never with process mining; the process-mining work on agents (ABM) covers one sequential architecture only.
- **2026 evidence (in `papers.csv`):**
  - Motivation: Vu et al. [2606.20669](https://arxiv.org/abs/2606.20669) (ABM on a four-agent order-to-cash system; limitation: sequential ReAct agents only, future work on other architectures) · Körner et al. [CEUR 4274/39](https://ceur-ws.org/Vol-4274/paper-39.pdf) (hand-off events in ABM).
  - Orchestration comparisons without process mining: Nechepurenko & Shuvalov [2605.03310](https://arxiv.org/abs/2605.03310) (five coordination configurations, same LLM/tools/prompts, failure signatures, traces released) · Liu et al. [2610.10126](https://arxiv.org/abs/2610.10126) (MAScope: topology recovered from traces is associated with failure patterns; LLM judges; MAScope-Bench) · Dhanyamraju et al. [2606.20058](https://arxiv.org/abs/2606.20058) (DAG Plan&Execute vs ReAct orchestration, metric-only) · Zhu et al. [2606.01199](https://arxiv.org/abs/2606.01199) (hierarchical framework vs AutoGen, MetaGPT etc., metric-only).
  - Hand-off failure modes to look for: Sun et al. [2608.24569](https://arxiv.org/abs/2608.24569) (workflow constraints erode at hand-offs) · Wang et al. [2608.29028](https://arxiv.org/abs/2608.29028) (boundary metadata lost in summarised hand-offs) · Pitre et al. [2610.32060](https://arxiv.org/abs/2610.32060) (communication-failure taxonomy) · Ma et al. [2610.14800](https://arxiv.org/abs/2610.14800) (enterprise interaction risks).
  - Intended model and representation: Fillies et al. [2611.13196](https://arxiv.org/abs/2611.13196) (BPMN → LangGraph workflows) · Xavier et al. [2603.20356](https://arxiv.org/abs/2603.20356) (workflow graphs extracted from LangGraph/CrewAI/AutoGen, temporal checks over traces) · Cha et al. [2606.14805](https://arxiv.org/abs/2606.14805) (multi-agent traces as event knowledge graphs).
- **Not yet in `papers.csv` (Scholar check 2026-11-20; screen + citation-check first):** Berti, Kourani & van der Aalst, BPM 2026 Forum, LNBIP 600 (selector-routed persona agents; hand-offs analysed as a social network over roles, without tools or process mining) · Cho et al. [2608.23670](https://arxiv.org/abs/2608.23670) (standard miners give low-precision "flower models" on agent traces incl. the Who&When multi-agent set; topology shaped by harness, not LLM) · Shamieh & Aref, AEECT 2026 (SLR on object-centric PM and LLM multi-agent systems).
- **Method foundation (classic process mining, not 2026; citation-check before use):** handover-of-work and social-network mining (van der Aalst, Reijers & Song 2005, *Discovering Social Networks from Event Logs*, CSCW) · organisational mining (Song & van der Aalst 2008, *Towards Comprehensive Support for Organizational Mining*, Decision Support Systems) · object-centric event logs (OCEL 2.0) for agents as objects.
- **Method:** controlled experiment. Implement 3 orchestration patterns in one framework (e.g. LangGraph) over one business process with the same agents, tools and prompts; 2 LLMs; ~200 runs per cell; inject a small set of known faults (e.g. a constraint that must survive a hand-off). Log with the ABM data model (agent = resource; hand-offs as events), export to XES/OCEL. Analyse with PM4Py: discovery + alignments against the intended BPMN (report precision, not only fitness – Cho et al.), variant analysis, handover-of-work and working-together networks; compare patterns with mixed models or permutation tests. Replicate F2/F3 on public traces (Nechepurenko & Shuvalov; MAScope-Bench; Who&When).
- **Data:** Rebuilt case (main) + Public (released multi-agent traces, usable from day 1); Accenture internal multi-agent logs if available.
- **Feasibility (8 months):** medium–high. M1–2 build the three patterns and logging, pilot; M3–5 experiments; M6 analysis + public-trace replication; M7–8 writing. Risks: multi-agent runs are costly (mitigate with a smaller open model for part of the grid); framework-specific patterns are hard to hold "everything else equal"; flower models if only discovery is used (mitigate with conformance against the intended model and organisational measures).
- **Relation to other RQs:** replaces the multi-agent arm of RQ-A and turns RQ-B's organisational mining into the measurement method; RQ-A and RQ-B could be merged into this question.
- **Why Accenture:** clients increasingly ask which orchestration pattern to use; this gives evidence per pattern on process adherence, hand-off risks and cost, plus a reusable ABM + process-mining benchmark for multi-agent designs.

---

## RQ-C (direction 3) – Conformance checking of agents against business processes

**RQ:** How do alignment-based (BPMN) and declarative (Declare/LTL) conformance checking compare in detecting deviations of LLM agents from a business process, and which log attributes must agent observability record for them to work?

- **C1.** Which deviation types (skipped mandatory steps, wrong order, unauthorised tool use, duplicate actions) does each technique detect on the same agent logs, and with what false-alarm rate?
- **C2.** How do missing attributes (timestamps, approvals, data provenance, reasoning) change detection quality?
- **C3.** Can conformance results be turned into actionable agent fixes (instructions, tool permissions)?

- **Gap:** G4 (and G6).
- **2026 evidence:** Körner et al. [CEUR 4274/39](https://ceur-ws.org/Vol-4274/paper-39.pdf) (alignments + process atoms) · Elkoussy & Perez [2607.02599](https://arxiv.org/abs/2607.02599) (FO-LTL over agent traces) · Kekatos et al. [2610.09793](https://arxiv.org/abs/2610.09793) (MFOTL; logs lack timestamps/approvals) · Xavier et al. [2603.20356](https://arxiv.org/abs/2603.20356) (DFA policies on event traces).
- **Method:** experiment with fault injection (seeded deviations with ground truth) in a rebuilt business-process agent; detection precision/recall per technique; ablation over logged attributes.
- **Data:** Rebuilt case + Public (AgentDojo-style recorded trajectories); Accenture internal logs for a realism check.
- **Feasibility (8 months):** high; well-defined ground truth. Risk: less novel than RQ-A/B because the SAP seeds already demonstrate both techniques; the novelty lies in the head-to-head comparison and the logging requirements.
- **Why Accenture:** compliance evidence for agents in regulated client processes, and concrete logging requirements for agent platforms.

---

## RQ-D (directions 1, 2) – Case notion and event abstraction for agent logs

**RQ:** Which case notion and activity abstraction for LLM-agent event logs yield stable and interpretable process models, and what does an object-centric representation add for multi-agent systems?

- **D1.** How do conversation-, task- and business-object-based case notions change the discovered models and their stability across runs?
- **D2.** Do taxonomy-based activity labels (e.g. Act-ONOMY) give simpler and more stable models than raw tool or LLM-call names?
- **D3.** What insights does an OCEL 2.0 view (agents, tasks, business objects) reveal that the XES-based ABM view hides?

- **Gap:** G3.
- **2026 evidence:** Vu et al. [2606.20669](https://arxiv.org/abs/2606.20669) (session case notion and OCED as stated limitations) · El Yadouni & Li [2608.02680](https://arxiv.org/abs/2608.02680) (directly-follows misses dependencies) · Zhao [2606.22741](https://arxiv.org/abs/2606.22741) (execution vs dependency edges) · Gao et al. [2605.13625](https://arxiv.org/abs/2605.13625) (behaviour taxonomy).
- **Method:** design science + experiment: define transformations, apply them to the same logs, compare model quality (fitness, precision, simplicity) and stability (bootstrap over runs).
- **Data:** Public + Rebuilt case; Accenture internal logs if available.
- **Feasibility (8 months):** medium. Risk: more methodological and harder to sell as an Accenture business case; OCEL tooling for agents must be built.
- **Why Accenture:** a reusable logging and transformation standard for agent platforms, so that agent logs from different frameworks can be analysed with the same tools.

---

## RQ-E (direction 7) – Closing the loop from mined deviations to agent improvement

**RQ:** Do agent changes derived from process-mining results (deviations, costly variants) improve conformance and cost of LLM agents over successive iterations without reducing task success?

- **E1.** Which kinds of intervention (instruction changes, tool-permission changes, process atoms as memory) follow from which mined findings?
- **E2.** How much do conformance, cost and success change per iteration, compared with a non-mining baseline (e.g. failure-driven prompt tweaks)?

- **Gap:** G7.
- **2026 evidence:** Körner et al. [CEUR 4274/39](https://ceur-ws.org/Vol-4274/paper-39.pdf) (closing the loop as future work) · Kirchdorfer et al. [2607.03228](https://arxiv.org/abs/2607.03228) (organisational memory of process atoms) · Hou et al. [2611.14492](https://arxiv.org/abs/2611.14492) (logged runs → workflows) · David et al. [2604.10513](https://arxiv.org/abs/2604.10513) (trace-based prompt repair).
- **Method:** iterative experiment (3–4 rounds) on a rebuilt agent; pre-registered metrics.
- **Data:** Rebuilt case (main).
- **Feasibility (8 months):** medium. Risks: many design choices in what counts as a "derived" intervention; results may depend on the case.
- **Why Accenture:** turns agent monitoring into continuous improvement of deployed agents.
