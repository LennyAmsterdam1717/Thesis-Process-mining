# Your Agent Has a Genome: Sequence-Level Behavioral Analysis and Runtime Governance of LLM-Powered Autonomous Agents

- **Authors:** Sidi Deng
- **Year / first version:** 2026 / 2026-04-05
- **Venue / status:** arXiv preprint – preprint
- **Link:** https://doi.org/10.48550/arXiv.2606.15579 ; https://arxiv.org/abs/2606.15579
- **Directions (working numbering):** 2 discovery/behaviour mining
- **Record:** R00053 · relevance high · citation check PASS (2026-11-18)

## What they did
Base Sequence Analysis encodes ReAct agent behaviour as Explore/Execute/Plan/Verify sequences and mines 347 production traces with n-grams and Markov transitions; derives a runtime Governor from the patterns.

## Key findings
P-X-P trigram is the only significant risk pattern (-10.4% success); Execute→Verify transition only 2.1% (verification deficit); a data-derived Governor intervenes at runtime.

## Limitations / future work
Single system, eight days of data; non-randomised before/after comparison; patterns may not transfer across models or systems.

## Why it matters for the thesis
Production traces analysed with sequence mining (not process mining) → clear gap: same data with DFGs/conformance.

_Paraphrased notes written from the full text; not a substitute for reading the paper. Screening pending Frank's verification._
