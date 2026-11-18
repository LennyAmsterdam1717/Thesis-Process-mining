# Thesis – Process Mining for Agentic AI

Working repository for a potential MSc Artificial Intelligence thesis (Utrecht University) on applying process mining to the behaviour of generative AI agents, carried out alongside a thesis internship at Accenture (Technology Strategy & Transformation).

## Topic in one paragraph

The thesis builds on *Agent Behavior Mining: Generative AI Agent Governance in Business Processes* (Vu et al., SAP) and on Dr. Xixi Lu's master project description *"Process Mining for Agentic AI"*. The idea is to treat AI-agent execution traces as event logs and use process-mining techniques to understand, compare and govern how agents behave inside business processes.

Directions of most interest:

- **Multi-agent interaction analysis** – how agents hand off work, communicate and coordinate
- **Comparing agentic AI approaches** – mining and contrasting the behaviour of different agent designs
- **Process-aware agent design** – using mined process knowledge to shape how agents are built
- (Earlier also considered: conformance checking and deviation detection)

## People

| Role | Person |
|---|---|
| Student | Frank (Lenny) |
| Potential university supervisor (process mining) | Dr. Xixi Lu, Utrecht University (ICS) |
| Company supervisor | Nino Hulsthoff, Accenture |
| Contact for thesis-duration extension | Max |

## Key facts

- Internship contract signed 9 Nov 2026; start date **4 January 2027**.
- The university prefers an **8-month** thesis; Accenture internships are capped at 6 months, so a 2-month extension has been requested.
- Data: aim to use **internal Accenture AI-agent data** (not client data).
- GenAI may be used during the thesis, as long as the student can explain the work it generated.

## Repository contents

- [`docs/timeline.md`](docs/timeline.md) – timeline up to the 17 Nov 2026 meeting
- [`docs/meetings/2026-11-17-xixi-lu.md`](docs/meetings/2026-11-17-xixi-lu.md) – notes from the meeting with Dr. Xixi Lu
- [`docs/next-steps.md`](docs/next-steps.md) – open action items
- [`literature/search-log.md`](literature/search-log.md) – search rounds and PRISMA counts
- [`literature/papers.csv`](literature/papers.csv) – papers that passed the citation check
- [`literature/screening/`](literature/screening/) – screening protocol, records and calibration batch (SR-Screener)
- [`docs/decisions.md`](docs/decisions.md) – log of choices made and why
- [`literature/summaries/`](literature/summaries/) – notes on 22 key papers (incl. both seeds)
- [`literature/background.md`](literature/background.md) – background reading outside the review corpus (E4 and single-LLM papers)
- [`literature/methods-draft.md`](literature/methods-draft.md) – methods text for the literature selection (discloses the single-reviewer full text)
- [`research-questions/`](research-questions/) – gap analysis, RQ candidates, shortlist and email draft to Xixi Lu

## Status (18 Nov 2026)

- Literature review done: 75 records screened → 62 full texts sought → **51 papers from 2026** in `papers.csv` (all citation-checked; 7 peer-reviewed or accepted, 44 preprints). **Provisional until Frank verifies the included set.**
- Shortlisted RQs: **RQ-A** comparing agent architectures with process mining (direction 6), **RQ-B** organisational mining of multi-agent interaction (direction 4), **RQ-C** alignment-based vs declarative conformance (direction 3).
