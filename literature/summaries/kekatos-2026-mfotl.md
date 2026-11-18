# Formal Runtime Verification for Tool-Using LLM Agents: An Offline Same-Benchmark Study on AgentDojo and STAC

- **Authors:** Nikolaos Kekatos; Stylianos Basagiannis; Marinelio Chintri; Alexios Lekidis; Tom Nianios; Ioannis Seitoglou; Anastasios Temperekidis; Panagiotis Katsaros
- **Year / first version:** 2026 / 2026-10-07
- **Venue / status:** CPSIoTSec 2026 workshop at ACM CCS (accepted); arXiv – peer-reviewed (accepted workshop paper; ACM DOI)
- **Link:** https://doi.org/10.1145/3847353.3847499 ; https://arxiv.org/abs/2610.09793
- **Directions (working numbering):** 3 conformance
- **Record:** R00064 · relevance high · citation check PASS (2026-11-18)

## What they did
Replays recorded AgentDojo, STAC and R-Judge trajectories through the MonPoly MFOTL monitor: generic temporal obligations flag most attacks but also fire on many benign runs; provenance-aware policies help.

## Key findings
Five generic MFOTL obligations flag ~70% of attack chains but also ~29% of benign runs because corpora lack timestamps and approvals; provenance-bound policies fix a simple evasion.

## Limitations / future work
Offline only (no live blocking); corpora lack timestamps and approvals; keyword-based action typing.

## Why it matters for the thesis
Shows that conformance on agent traces is limited by what the logs record: data-quality requirement for any Accenture log.

_Paraphrased notes written from the full text; not a substitute for reading the paper. Screening pending Frank's verification._
