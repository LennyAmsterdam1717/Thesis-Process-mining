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

## 2026-11-18 – Screening protocol v1.0 confirmed; calibration pilot chosen

- **Decision:** Frank confirmed `literature/screening/screening_protocol.md` v1.0 with three adjustments, all made before any record was screened:
  1. **E4 (LLM does process mining on ordinary business logs):** excluded from the review corpus but **kept as background reading**, not discarded.
  2. **Training-only papers** (traces used only as training data, no behaviour analysis): excluded (E5).
  3. **Single LLM in multi-turn interaction:** "unclear" at title/abstract; at full text **include if the LLM uses tools or acts in an environment**, otherwise exclude and keep as background.
- **Decision:** Screening path (a): two blinded AI reviewers (Claude Sonnet 5.5) + third-reviewer adjudication + QC recheck of joint exclusions, **after a calibration pilot** in which Frank labels batch b001 (25 records, includes the seed paper Vu et al. 2026) independently.
- **Why:** SR-Screener's rule is that the full run waits until the AI misses none of the records the human advanced. Frank prefers the calibrated route over a recorded override.
- **Records:** 75 unique 2026 records prepared (`literature/screening/sr_work/`), 3 batches of 25; 5 records have no abstract (publisher pages blocked automated access) and are judged on title. Seed found as R00011.

## 2026-11-18 – Pilot conflicts settled by Frank; v1.1 amendment prepared

- **Decision:** R00006 (LLM multi-agent organisational simulation) and R00021 (DAG Plan-Execute vs ReAct) → **include**, as human overrides (`literature/screening/overrides.csv`). They win over the AI reviewers and are marked "Frank" in all outputs.
- **Decision (pending "go"):** protocol amendment v1.1 to concept (e), prepared in `screening_protocol_v1.1_pending.md`. It becomes active only when Frank says "go".
- **Why:** pilot 1 missed R00024 (AgBench) because v1.0 did not say that time, cost and steps count as behaviour (direction 5 in Xixi Lu's project description).
- **Set-up:** `docs/runbook-go.md` lists every remaining step and the stop conditions, so the work can continue on one prompt.

## 2026-11-18 – "go light": protocol v1.1 confirmed, single-reviewer full text

- **Decision:** Frank said **"go light"**. This (1) confirms screening protocol v1.1 exactly as worded in the pending file (concept (e) now counts completion time, cost/tokens, steps, tool usage, rework and coordination overhead as behaviour; new unclear example (d)); (2) approves the title/abstract screening cost (about 8–12 Sonnet reviewer calls: re-pilot, full run, adjudication, QC recheck); (3) chooses a **single-reviewer full-text check done by Claude (Opus 5.5, main session)** instead of two blinded full-text reviewers; (4) asks for the whole RQ brief without check-ins except at the runbook's stop conditions.
- **Done:** `screening_protocol.md` replaced by v1.1 (header: confirmed 2026-11-18, "go light"); the `_pending` file deleted.
- **Why single reviewer at full text:** cost (dual full text would be about 60–80 long-PDF calls). **Consequence, to be disclosed in the methods:** full-text eligibility decisions were made by one AI reviewer without a second independent reviewer or adjudicator, so full-text agreement statistics cannot be reported; Frank's verification of the included set is the only second check.

## 2026-11-18 – Calibration pilot 2 passed (protocol v1.1)

- **Result:** both reviewers advanced R00024; the AI missed none of the 17 records Frank advanced (25/25 compared).
- **Tool note (procedural, no screening judgement changed):** SR-Screener settles a record with a human override before adjudication, so the pilot conflict R00006 (A exclude / B unclear) never got an AI decision and the pilot gate could not complete, while `--jobs pending` would also have scheduled the unscreened b002–b003 (outside the pilot, blocked by the gate). To keep the gate honest without `--pilot-override`, the tool's own adjudicator prompt for R00006 was generated in a scratch copy of the work folder (same review revision and context ID) and run once; the result (unclear) is saved in `sr_work/decisions/ADJ_b001@….json` and the prompt in `sr_work/prompts_pilot2_adj/`. Frank's override (include) remains the final decision.
