# papers.csv verification against the full text

_2026-11-19. Every row of `literature/papers.csv` (51) was compared with the full text (page-marked pypdf text of the arXiv PDF; for the CEUR seed, the CEUR PDF): main contribution (including the method it describes) and limitations/future work. A column `source_checked` was added._

## Result

- `source_checked`: **full text** for all 51 rows. No row was left on abstract-only information after this check.
- **Main contribution / method:** all 51 match the paper; no change was needed. The contributions were originally written from the full-text extraction (abstract, method/evaluation and conclusion), and the numbers they quote appear in the papers.
- **Limitations / future work: 23 rows changed.** Before this check, several rows mixed the authors' stated limitations with my own scope assessment, or had been written from the abstract and the paper's scope without finding its limitations section. Now each row gives the authors' stated limitations first and marks any assessment of mine as "Reviewer note". Where a paper has no limitations section, the row says so.
- Rows whose limitations were previously based on abstract/scope rather than a limitations section (now fixed): R00006, R00024, R00040, R00054, R00063, R00072 (replaced), and R00001, R00035, R00042, R00047, R00060 (no such section exists; marked as reviewer assessment).

## Changes

| Record | Key | What changed | Old text |
|---|---|---|---|
| R00001 | yang2026event2action | limitations: stated-vs-assessed separated | Vision only, no implementation or evaluation; the proposed benchmark (E2A-Bench) and artefacts are future work. Says little about mining the agents' own traces. |
| R00006 | zhu2026taskweave | limitations replaced with stated ones (old text was reviewer assessment) | Simulated IT company only; behavioural comparison relies on framework-specific metrics rather than process models; no explicit process-mining analysis of the traces. |
| R00018 | lin2026agenteval | limitations aligned with Threats to Validity | All metrics depend on an LLM auditor; limited to four benchmark agents; workflow-graph mining is model-specific rather than standard process discovery. |
| R00024 | han2026agbench | limitations replaced with stated ones | Focus on system-level trade-offs, not behavioural or process analysis of traces; specific devices and workloads. |
| R00029 | pitre2026commfailures | stated vs assessed separated | Only failed debate-style trajectories; open-weight models; does not cover tool-using workflow agents. |
| R00032 | wang2026factswithoutrules | limitations aligned with Limitations section | Privacy-specific; testbed and PrivacyLens scenarios; judge-based measurement. |
| R00035 | liu2026mascope | marked as reviewer assessment | Empirical association between topology and failures, not causal; depends on LLM judges; limited set of frameworks. |
| R00037 | nechepurenko2026coordination | added stated threats (prompt sensitivity, sample size) | One domain (prediction markets) and 100 markets; no formal third-party pre-registration; three of five predicted signatures held. |
| R00038 | patel2026sixsigma | added stated limitation (open-ended tasks); assessment marked | Depends on decomposition quality; assumes independent model errors; reliability is the main measure, behaviour is not analysed as process data. |
| R00040 | wang2026dcfa | limitations replaced with stated ones | Attribution benchmarks only; relies on LLM reasoning over long traces; no process-model view. |
| R00042 | ma2026eair | marked source of limitation | Micro-worlds instantiate selected risks only; one run per model and configuration in parts of the evaluation. |
| R00047 | song2026mobilitybench | marked as reviewer assessment | Domain-specific; behaviour assessed through benchmark metrics rather than trace or process analysis. |
| R00049 | li2026defaulttrap | stated vs assessed separated | Two models and selected tau-bench/AgentDojo tasks; decision-window measures, no process view. |
| R00054 | oderinwale2026fingerprints | limitations replaced with stated future work | Coding tasks on SWE-bench only; representation is compressive and may hide semantics. |
| R00055 | ma2026samesignal | added stated future work | Observational, no causal claims; configurations solve different task subsets, so task difficulty confounds effects. |
| R00059 | chen2026schrodinger | assessment marked | Python, open-source repositories only; behaviour analysis is secondary to the memorisation question. |
| R00060 | dumas2026abpms | marked as reviewer assessment | Vision, no evaluation; agents are seen as users of process mining rather than as objects of it. |
| R00063 | ray2026certified | limitations replaced with stated ones | Mainly theoretical; results hold under stated oracle and finite-abstraction assumptions. |
| R00068 | elkoussy2026agentltl | added stated future work | Grounding predicate is vacuous for refusals; fine-tuning on one small base model. |
| R00070 | kang2026policyguide | limitations aligned with Limitations section | tau2-bench domains only; rules partly hand-built by the authors. |
| R00071 | hou2026retrace | added stated future work | Relies on the agent's stated reasoning, which may be wrong; conditions not verified before the actions they justify. |
| R00072 | balaji2026journeybench | limitations replaced with stated ones | Synthetic scenarios generated from graphs; three domains. |
| R00073 | khan2026pakg | added stated future work | Circular evaluation (validator built from the same schema); same author wrote queries and mapping. |

No paper, author, venue, finding or limitation was added that is not in the paper; reviewer assessments are labelled as such.
