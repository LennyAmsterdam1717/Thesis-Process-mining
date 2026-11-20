# Google Scholar cross-check – 2026-11-20

Query: `"process mining" ("LLM agent" OR "LLM-based agent" OR "agentic AI" OR "multi-agent") ("event log" OR traces)`, years 2026–2026, first 100 results (10 pages).
Purpose: find relevant papers missed by rounds 1–4. Nothing here is added to papers.csv – candidates still need screening + citation check (CLAUDE.md workflow).

## Already covered (in papers.csv)
- Vu et al. – Agent Behavior Mining (BPM 2026) + CEUR version "Generative AI Agent Governance in Business Processes"
- Körner et al. – What Are Your Agents Up To? (seed, other methods)
- Yang et al. – From Event Logs to Governed Action (2609.07984)
- Bala et al. – Using PM to Generate AI Agents from SE Process Records (2607.04948)
- Elyadouni & Li – TraceCompiler (2608.02680)
- Deng – Your Agent Has a Genome (2606.15579)
- Elkoussy & Perez – AgentLTL (2607.02599)
- arXiv 2604.10513: Scholar title "Agent Mentor: Framing Agent Knowledge through Semantic Trajectory Analysis"; papers.csv has it as "Semantic Feature Analysis..." (david2026sfa) – check which title/version is correct

## Missed – high relevance (PM applied to the agents' own traces)
- Xu & Tao (2026) – Inductive Miner for ToolLLaMA: Semantic Process Comparison of Chain-of-Thought and Depth-First Search Traces. IEEE conf. https://ieeexplore.ieee.org/abstract/document/11751192/  ← standard Inductive Miner on ToolBench LLM-agent traces
- Qian, Zhao & Miller (2026) – M2-PALE. arXiv 2604.14687 (Alpha/iDHM/Inductive Miner on agent traces; agents are MCTS-minimax, not LLM – check)
- Hao et al. (2026) – FlowScout. arXiv 2608.10039 (event log built from LLM-agent tool traces)
- Cho et al. (2026) – Automata from agent traces: failure and next-step prediction. arXiv 2608.23670 (PM baselines)
- Rajan (2026) – TraceForge. EMNLP 2026 Demos https://aclanthology.org/2026.emnlp-demos.37/
- Li, Cheng, Nicholls & Kong (2026) – De-Linearizing Agent Traces (BPOP). arXiv 2602.02806 / ICML (compares against PM)
- Talavera (2026) – Early Failure Detection in Web Navigation Agents via Closed Sequential Pattern Mining. Thesis (ProQuest)

## Missed – medium (agent-trace monitoring/mining, PM as related work)
- Malik (2026) – Progressive Crystallization. arXiv 2607.07052
- Brömme (2026) – Intrusion Detection for Agentic Processes. arXiv 2610.00151
- Basak & Shin (2026) – DutyFormer. KDD 2026 agentic-AI eval workshop
- Zhao et al. (2026) – AgentTether. arXiv 2607.06273
- Zhu et al. (2026) – GraphMind. arXiv 2605.17617
- Acharya (2026) – Semantic Consensus. arXiv 2604.16339
- Sokhin (2026) – A Graph-Based Provenance Model for Human-Agent Software Workflows. Aalto thesis

## Missed – background / related work
- Shamieh & Aref (2026) – Bridging OC Process Mining and LLM-Based MAS: an SLR. IEEE JEEIT (overlaps with this review)
- Berti, Kourani & van der Aalst (2026) – Configuring and Diagnosing Conversational Agents for PM Tasks (BPM 2026 forum)
- Margaris et al. (2026) – Agentic AI Meets BPM: SLR and taxonomy. Information 17(11):1143

## Correctly excluded earlier (agents doing PM, not PM of agents)
- Comuzzi et al. – Towards Agentic AI for Event Log Data Quality (TA exclude)
- Antonov et al. – PMAx (TA exclude)

## Abstract check – 2026-11-20 (abstracts read, not full text; single reviewer: Claude)

| Paper | Verdict from abstract | Why |
|---|---|---|
| Xu & Tao – Inductive Miner for ToolLLaMA (SEAI 2026, DOI 10.1109/SEAI70065.2026.11751192) | INCLUDE – strong | ToolBench traces → API-level event logs; Standard Inductive Miner per strategy slice; fitness 1.000; CoT vs DFS comparison |
| Cho et al. – Automata from Agent Traces (arXiv 2608.23670, NeurIPS 2026) | INCLUDE – strong | Agent-trace corpus → one FSM; replay fitness ≥0.997 on 12 datasets; failure prediction + online monitor |
| Li et al. – De-Linearizing Agent Traces / BPOP (arXiv 2602.02806) | INCLUDE | Infers partial-order dependencies from agent traces; beats PM baselines |
| Basak & Shin – DutyFormer (KDD'26 workshop) | INCLUDE | Conformance vector over obligation rules; process logs + tau-bench agent trajectories |
| Hao et al. – FlowScout (arXiv 2608.10039) | INCLUDE – medium | Mines tool-coordination pattern from task records; PM4Py baseline |
| Rajan – TraceForge (EMNLP 2026 Demos) | INCLUDE – medium | OpenTelemetry agent traces → frozen workflow DAG (same family as TraceCompiler) |
| Zhao et al. – AgentTether (arXiv 2607.06273) | INCLUDE – medium | Dependency graph over run steps + normal-behaviour model for failure diagnosis |
| Sokhin – Graph-Based Provenance Model for Human-Agent Software Workflows (Aalto MSc thesis 2026) | GREY LIT – medium | Coding-agent OTel spans → typed PROV graph; diagnosis via subgraph queries |
| Qian, Zhao & Miller – M2-PALE (arXiv 2604.14687) | BORDERLINE | Alpha/iDHM/Inductive Miner on agent traces, but agents are MCTS-minimax in checkers; LLM only explains |
| Berti, Kourani & van der Aalst – Configuring and Diagnosing Conversational Agents for PM Tasks (LNBIP 600, pp.163-178) | BORDERLINE | Agent traces analysed as social networks over roles (SNA), but agents perform PM tasks |
| Malik – Progressive Crystallization (arXiv 2607.07052) | BORDERLINE | Promotes repeated agent behaviour to deterministic workflows; mining method not stated in abstract |
| Shamieh & Aref – OCPM ↔ LLM-MAS SLR (AEECT 2026, DOI 10.1109/AEECT69724.2026.11657849) | BACKGROUND – important | 52-paper review; claims to be first to treat OCPM, LLM-based PM and MAS together – check overlap with this review |
| Brömme – Intrusion Detection for Agentic Processes (arXiv 2610.00151) | EXCLUDE (or background) | Conceptual only; no implementation or evaluation |
| Zhu et al. – GraphMind (arXiv 2605.17617) | EXCLUDE | Mines human incident-resolution traces, not agent traces |
| Acharya – Semantic Consensus (arXiv 2604.16339) | EXCLUDE | Coordination middleware; no trace mining |
| Talavera – Early Failure Detection in Web Navigation Agents (SJSU thesis 2026) | UNCLEAR | Abstract not visible (ProQuest preview only) |

Note on arXiv 2604.10513: arXiv now shows "Semantic Feature Analysis: Improving Agents Without Searching Over Rollouts" (David, Fournier, Limonad, Mulian; v2 2026-09-16). Scholar still lists "Agent Mentor" with first author Ben-Gigi – probably the v1 title. papers.csv matches the current version.

## Full-text reading – 2026-11-20 (papers that bear on RQ-A/B/C)

Read in full: Cho et al. (arXiv 2608.23670v2), DutyFormer (KDD'26 workshop PDF), AgentTether (arXiv 2607.06273v1), Berti/Kourani/van der Aalst (Preprints.org 202606.1316 v1, read via full-text page).
Not accessible: Xu & Tao (IEEE, paywalled, no preprint found), Shamieh & Aref (IEEE, paywalled). Need Utrecht library access.

**Cho et al. – Automata from Agent Traces (NeurIPS 2026)**
- Builds a deterministic directly-follows automaton (prefix tree + merge by last activity; |Q| = |A|+1) from LLM-agent traces; 12 public datasets incl. Who_and_When (184 multi-agent failure traces, 8 activities), SWE-agent, WebArena, tau2-bench.
- Baselines include PM4Py Alpha, Heuristic and Inductive Miner (default params, XES). Table 22: Inductive Miner fitness 1.00 on 8/10 datasets but precision 0.10–0.46 (mean 0.25) – "flower models"; Heuristic 0.95–1.00 fitness, precision 0.20–0.80; Alpha fails (fitness 0.05–0.63). Highest precision on the most constrained workflow (tau2 telecom).
- One FSM from four LLMs' tau2-bench traces replays each at 1.000 fitness; LLMs differ only in transition probabilities -> topology shaped by harness (tools, tasks, prompts), not model. Per-state features predict failure (AUROC up to 0.94).
- => This is itself a 2026 study applying standard PM miners to LLM-agent logs (as baselines).

**Berti, Kourani & van der Aalst – Configuring and Diagnosing Conversational Agents for PM Tasks**
- One LLM, ~7 personas, selector routing, NO tools; 57 PM-LLM-Benchmark questions; 3 models.
- "SNA" = node score (mean judge score per role) + edge score (mean judge score of receiving node per handoff), counts, density. No centrality, no process discovery or conformance on traces, no failure labels, no business process.
- Result: no configuration clearly beats direct answering; pruning 4 weak handoffs helps modestly (same benchmark, no held-out).

**DutyFormer**
- Obligations as DECLARE-style response constraints compiled to Time Petri Nets; labels by replay; Transformer with conformance state injected into attention; predicts omissions from prefixes.
- Data: 4 BPI logs + tau-bench airline/retail trajectories (1,980 episodes). On tau-bench, XGBoost on conformance features is already perfect (OMR 0) – conformance state is highly informative.
- Does NOT compare alignment-based vs declarative checking.

**AgentTether**
- Single-agent repair on tau-bench (261 tasks); dependency graph over "Transition Units", HGT normal-behaviour model + analyst LLM. No process mining (PM only cited as runtime-monitoring related work). Multi-agent coordination named as future work.
- Motivation data: in 83 failed Banking runs, root cause precedes the symptom by median 4 required steps (79% upstream); tau-bench gold action checks give step-level ground truth.
