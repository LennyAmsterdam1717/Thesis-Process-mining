# ReTrace: Distilling Tool-Using Agents into Planner-Free Workflows

- **Authors:** Kaiyuan Hou; Yang Ping Kuo; Indranil Bhattacharya; Rohith Nama; Arushi Gupta; Carlos D. Castillo; Prathap Ramachandra; Xiaofan Jiang; Francesco Carbone
- **Year / first version:** 2026 / 2026-11-10
- **Venue / status:** arXiv preprint (Amazon) – preprint
- **Link:** https://doi.org/10.48550/arXiv.2611.14492 ; https://arxiv.org/abs/2611.14492
- **Directions (working numbering):** 2 discovery/behaviour mining, 5 performance, 7 process-aware design
- **Record:** R00071 · relevance high · citation check PASS (2026-11-18)

## What they did
ReTrace turns an SOP plus a few logged agent runs into a planner-free executable workflow by extracting step conditions from the agent's explanations; 79 production procedures, lower cost and latency.

## Key findings
On 79 production SOPs, workflows reach 93.8% completion vs 96.8% for the agent at 24% lower cost; on tau2-bench they run in 1.3 s instead of 170 s.

## Limitations / future work
Relies on the agent's stated reasoning, which may be wrong; conditions not verified before the actions they justify.

## Why it matters for the thesis
Mining logged runs into a workflow = process discovery used for process-aware design (direction 7); a production (Amazon) data point.

_Paraphrased notes written from the full text; not a substitute for reading the paper. Screening pending Frank's verification._
