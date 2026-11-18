# Decisions log

Append new entries at the bottom; do not overwrite earlier ones.

## 2026-11-18 – Review form and protocol for the RQ literature search

- **Decision:** Integrative review in ARS `lit-review` mode, used for a scoping purpose: map 2026 work on process mining for agentic AI and find gaps for research questions.
- **Why:** The goal this week is 2–3 research questions for Dr. Xixi Lu, not a publishable systematic review. An integrative review allows a documented search and screening while mixing study types (data models, demos, experiments, position papers).
- **Note:** ARS has no separate scoping-review mode, so a formal scoping-review protocol and the PRISMA-ScR checklist are not followed. PRISMA 2020 counts are still logged per round in `literature/search-log.md`, as required by `CLAUDE.md`.
- **Eligibility (set by Frank):**
  - Published in **2026** only (by publication or first arXiv version date). Year range is not widened without Frank's approval.
  - Peer-reviewed venues or arXiv preprints; each paper labelled as one or the other.
  - Must treat LLM / generative-AI agent behaviour (actions, tool calls, messages, decisions, interactions) as process or trace data, or apply process-mining-style analysis to agentic systems.
  - Every included paper needs a working DOI or arXiv link and must pass the citation check.
- **Search plan:** Round 1 broad (process mining × AI agents); Round 2 multi-agent interaction analysis; Round 3 comparing agentic approaches; Round 4 other directions (discovery, conformance, performance, process-aware design) and citation chasing from the two seed papers.
- **Seed papers:** Vu et al. (2026) *Agent Behavior Mining* (arXiv:2606.20669, BPM 2026) and Körner et al. (2026) *What Are Your Agents Up To?* (BPM 2026 Demos, CEUR).

## 2026-11-18 – Screening protocol drafted (awaiting confirmation)

- **Decision:** Draft SR-Screener protocol and config in `literature/screening/` (PCC framing; exclusion codes E1 year → E2 publication type → E3 not LLM agents → E4 wrong direction → E5 no process/trace angle → E9 other).
- **Why:** SR-Screener requires a confirmed protocol before any record is screened. Rules marked `[proposed]` operationalise Frank's scope and need his confirmation, especially E4 (LLMs doing process mining on ordinary logs are out unless the agents' own behaviour is analysed).
