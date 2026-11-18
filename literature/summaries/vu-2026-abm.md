# Agent Behavior Mining: Generative AI Agent Governance in Business Processes

- **Authors:** Hoang Vu; Maximilian Körner; Adrian Rebmann; Gabriel Kevorkian; Michael Perscheid; Gregor Berg; Timotheus Kampik
- **Year / first version:** 2026 / 2026-06-12
- **Venue / status:** BPM 2026 main track (accepted); arXiv – peer-reviewed (accepted; arXiv version cited)
- **Link:** https://doi.org/10.48550/arXiv.2606.20669 ; https://arxiv.org/abs/2606.20669
- **Directions (working numbering):** 1 event data, 2 discovery/behaviour mining, 3 conformance, 4 multi-agent interaction, 5 performance
- **Record:** R00011 · relevance high · citation check PASS (2026-11-18)

## What they did
Seed paper. Agent Behavior Mining: XES-compatible event data model for GenAI agents (LLM calls, tool calls, hand-offs, tokens, reasoning); applies discovery, conformance, performance and variant analysis to a four-agent order-to-cash system (371 cases); practitioner study (n = 18).

## Key findings
Defines the event types (prompt, agent_start/finish, call_llm, execute_tool, transfer_to_agent) and attributes (tokens, cost, duration, reasoning, errors) that make agent runs XES logs; on the O2C case it finds skipped steps (e.g. calculate_total), insertion violations, token disparities between agents and behavioural variants for similar orders. Practitioners valued variant analysis most (78%).

## Limitations / future work
Perceived usefulness only; single researcher-built scenario with induced failures; one model (gpt-4.1) and sequential ReAct agents; session-level case notion; future work on OCED, other architectures and production data.

## Why it matters for the thesis
The reference data model for the thesis. Its own limitations (one model, ReAct only, synthetic scenario, XES not OCEL, session = case) are direct openings for RQs on comparing architectures (dir. 6) and multi-agent interaction (dir. 4). References were read in full: all pre-2026, so no further 2026 papers from backward chasing.

_Paraphrased notes written from the full text; not a substitute for reading the paper. Screening pending Frank's verification._
