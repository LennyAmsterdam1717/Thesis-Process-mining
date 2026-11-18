# RQ-B feasibility pilot – process discovery and handover-of-work on MAScope-Bench (LG-Ctrl)

_2026-11-19. Goal: check that public labelled multi-agent traces can be turned into an event log and analysed with standard process-mining tools. This is a feasibility check, not a result for the thesis._

## Data
- **MAScope-Bench, corpus LG-Ctrl** (Liu et al. 2026, arXiv:2610.10126), https://huggingface.co/datasets/mascope/mascope-bench, **CC-BY-4.0**.
- 408 LangGraph traces, 102 per communication topology (Layered, Centralized, Decentralized, Shared Message Pool); 328 with an injected anomaly (goal_hijack, over_constraint, information_loss, loop_failure, silent_pass, deadlock), 80 without; LLM: gemini-3 (per record).
- Raw data stays local in `data/` (git-ignored). The committed `sample/lgctrl_sample.xes` holds 20 traces (5 per topology, seed 2026) **without message text** (speaker, position and labels only); attribution in `sample/ATTRIBUTION.md`.

## Method
1. `scripts/convert_mascope.py`: each `[speaker]` block → one event (case = trace, activity = resource = speaker: `system`, `agent_A`–`agent_E`, `verifier`, `reviewer`). Other bracketed lines count as message text; lower-case `agent_a/b` are normalised. **Timestamps are synthetic** (1 s per position) because the data has none; only the order is real. Result: 408 cases, 5,921 events (XES + CSV).
2. `scripts/analyse_pilot.py` (pm4py 2.7.23 in a venv): Inductive Miner (noise threshold 0.2) per topology with token-based replay fitness and precision; `discover_handover_of_work_network` per topology; per-case handover features (agent hand-offs, distinct pairs, A→B→A "ping-pong", self-repeats, system messages).
3. `scripts/feature_auc.py`: rank-based AUC of each feature for injected vs not-injected traces.

## Results (`results/`)

| Topology | Variants | IM places / transitions | Fitness | Precision | Strongest handover edges (share of handovers) |
|---|---|---|---|---|---|
| Centralized | 24 | 25 / 34 | 0.985 | 0.288 | system→agent_A 0.16, agent_B→agent_A 0.09, agent_A→system 0.08 |
| Decentralized | 6 | 15 / 20 | 0.998 | 0.347 | agent_C→agent_D 0.14, agent_B→agent_C 0.12, system→agent_B 0.11 |
| Layered | 6 | 20 / 26 | 0.979 | 0.405 | system→agent_A 0.12, agent_A→agent_B 0.06, agent_B→agent_C 0.05 |
| Shared Message Pool | 11 | 24 / 31 | 1.000 | 0.247 | agent_C→agent_D 0.13, agent_A→agent_B 0.11, agent_B→agent_C 0.11 |

- **Handover structure matches the topology labels:** in Centralized traces work flows through agent_A as a hub (in and out); in Layered traces it runs as a chain A→B→C→D→E; in Decentralized traces it runs peer-to-peer (B→C→D), and in Shared Message Pool traces it cycles (A→B→C→D→A). This suggests organisational mining can recover topology without an LLM judge, which is a testable RQ-B claim.
- **Injected vs normal traces (AUC, all 408):** events 0.78, agent turns 0.68, handovers 0.66, distinct pairs 0.63, self-repeat 0.61, ping-pong 0.54 (per topology up to 1.0 for `events`). By anomaly type, *information_loss* traces have far more self-repeats (7.1 vs 0.2) and ping-pong (3.6 vs 0.6) than normal traces; *goal_hijack* and *over_constraint* show mainly extra system messages (≈9.7 vs 1.0).

## Limits – read before using any number
- **Synthetic artefacts dominate:** normal LG-Ctrl traces follow fixed templates (constant length per topology), and two anomaly types are injected as extra `system` messages. Length and system-message features therefore separate classes almost by construction; the AUCs say little about real coordination failures.
- **No timestamps, no tool calls:** only conversational turns are logged, so performance analysis and ABM-style `call_llm` / `execute_tool` events are impossible.
- **Activity = resource:** with only speaker labels, the discovered models are agent-order models; richer activity labels (message intent, e.g. via a behaviour taxonomy such as Act·ONOMY) would be needed.
- **Low precision (0.25–0.41)** of the Inductive Miner models: the logs allow many interleavings; a better case notion or activity abstraction is needed (links to RQ-D).
- One framework (LangGraph) and one LLM; no comparison with an LLM-judge baseline yet (RQ-B sub-question B3).
- pm4py is **AGPL-3.0**. Fine for a thesis, but check with Accenture before using it in any internal tool.

## Verdict
**The pipeline works:** public labelled traces → XES → discovery + handover-of-work, with interpretable topology-specific handover patterns. RQ-B is feasible on public data for control-flow and organisational analysis. For valid failure-related findings it needs (a) the non-synthetic MAST-clean / MAD traces (natural failures, several frameworks; parsers per framework) and (b) properly logged traces (timestamps, tool calls) from a rebuilt or Accenture case.

## Reproduce
```bash
python3 -m venv venv && venv/bin/pip install pm4py
curl -L -o data/mascope_LG-Ctrl.jsonl https://huggingface.co/datasets/mascope/mascope-bench/resolve/main/LG-Ctrl.jsonl
venv/bin/python -I scripts/convert_mascope.py data/mascope_LG-Ctrl.jsonl data/out 5
venv/bin/python -I scripts/analyse_pilot.py data/out/lgctrl_events.csv results
venv/bin/python -I scripts/feature_auc.py results/case_handover_features.csv results/feature_auc.csv
```
Petri-net images were not rendered (Graphviz is not installed); models are saved as PNML in `results/`.
