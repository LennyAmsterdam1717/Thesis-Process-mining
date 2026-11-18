# What Are Your Agents Up To? Agent Behavior Mining in Action

- **Authors:** Maximilian Körner; Hoang Vu; Adrian Rebmann; Gabriel Kevorkian; Tobias Wuttke; Michael Perscheid; Gregor Berg; Timotheus Kampik
- **Year / first version:** 2026 / 2026-09-28
- **Venue / status:** BPM 2026 Demonstration & Resources Forum, CEUR-WS Vol-4274, paper 39 – peer-reviewed (demo track)
- **Link:** https://ceur-ws.org/Vol-4274/paper-39.pdf (no DOI, no arXiv version)
- **Directions (working numbering):** 1 event data, 2 discovery/behaviour mining, 3 conformance, 5 performance
- **Record:** seed (other methods) · relevance high · citation check PASS (2026-11-18)

## What they did
Seed paper. Demonstrates agent behavior mining in SAP Signavio Process Intelligence: OpenTelemetry agent traces converted to ABM logs, then dashboards, DFG discovery, BPMN alignment and declarative process-atom checks on a three-agent procurement system (200 traces).

## Key findings
Walkthrough on 200 procurement traces: the last agent in the pipeline uses about twice the tokens of the others (it receives the full history); one tool has a 30% error rate; DFG shows a skipped calculator in 48 cases, duplicate tool calls and missing approvals; only ~28% of ordering cases conform to the BPMN model; three process atoms (declarative rules) give 85%, 76% and 25% satisfaction.

## Limitations / future work
Demo paper; one synthetic procurement case; support for external agent runtimes and closing the loop to steer agents are future work.

## Why it matters for the thesis
Shows that off-the-shelf process mining (discovery, alignments, declarative atoms) works on agent logs. Also a template for an Accenture demo: OTLP traces → ABM log → standard tooling. References: all 2025 or earlier apart from the BPM 2026 companion paper.

_Paraphrased notes written from the full text; not a substitute for reading the paper. Screening pending Frank's verification._
