# Gap analysis – process mining for agentic AI (2026 literature)

_Basis: the 51 papers in `literature/papers.csv` (all 2026, all citation-checked). Screening is pending Frank's verification. Directions use the working numbering in `docs/decisions.md` (1 event data · 2 discovery/behaviour mining · 3 conformance · 4 multi-agent interaction · 5 performance · 6 comparing approaches · 7 process-aware design). Links: arXiv abstract pages unless stated._

## Themes in the 2026 corpus

| Theme | What 2026 work does | Representative papers |
|---|---|---|
| T1 Agent event data | Data models and trace formats that make agent runs analysable: XES-based ABM, event-sourced runtimes, trace compilers, dependency graphs, behaviour taxonomies | Vu et al. [2606.20669](https://arxiv.org/abs/2606.20669); Körner et al. [CEUR 4274/39](https://ceur-ws.org/Vol-4274/paper-39.pdf); Zhang & Agrawala [2603.29678](https://arxiv.org/abs/2603.29678); Nakajima [2605.21997](https://arxiv.org/abs/2605.21997); Zhao [2606.22741](https://arxiv.org/abs/2606.22741); Gao et al. [2605.13625](https://arxiv.org/abs/2605.13625) |
| T2 Behaviour mining across runs | Sequence/n-gram/Markov mining, fingerprints, consistency metrics, cross-framework behaviour studies; workflow graphs mined from interaction | Deng [2606.15579](https://arxiv.org/abs/2606.15579); Oderinwale [2606.16988](https://arxiv.org/abs/2606.16988); Ma et al. [2605.18332](https://arxiv.org/abs/2605.18332); Banerjee & Raichura [2608.13598](https://arxiv.org/abs/2608.13598); El Yadouni & Li [2608.02680](https://arxiv.org/abs/2608.02680); Lin et al. [2607.06873](https://arxiv.org/abs/2607.06873) |
| T3 Conformance / compliance | Temporal-logic monitors (LTL, MFOTL, DFA), workflow-graph controllers and policy benchmarks; BPMN alignments only in the SAP seed papers | Elkoussy & Perez [2607.02599](https://arxiv.org/abs/2607.02599); Kekatos et al. [2610.09793](https://arxiv.org/abs/2610.09793); Xavier et al. [2603.20356](https://arxiv.org/abs/2603.20356); Wang et al. [2607.25400](https://arxiv.org/abs/2607.25400); Kang et al. [2608.19861](https://arxiv.org/abs/2608.19861); Balaji et al. [2601.00596](https://arxiv.org/abs/2601.00596) |
| T4 Multi-agent interaction | Failure taxonomies, topology recovery, failure attribution, hand-off erosion, enterprise interaction risks — almost all with LLM judges or custom graphs | Pitre et al. [2610.32060](https://arxiv.org/abs/2610.32060); Liu et al. [2610.10126](https://arxiv.org/abs/2610.10126); Wang et al. [2609.04749](https://arxiv.org/abs/2609.04749); Sun et al. [2608.24569](https://arxiv.org/abs/2608.24569); Wang et al. [2608.29028](https://arxiv.org/abs/2608.29028); Ma et al. [2610.14800](https://arxiv.org/abs/2610.14800) |
| T5 Comparing agentic approaches | Architectures, frameworks, deployments and coordination set-ups compared on success, latency, tokens, tool errors, failure signatures | Borman et al. [2607.14456](https://arxiv.org/abs/2607.14456); Dhanyamraju et al. [2606.20058](https://arxiv.org/abs/2606.20058); Nechepurenko & Shuvalov [2605.03310](https://arxiv.org/abs/2605.03310); Liparulo & Pierri [2608.26199](https://arxiv.org/abs/2608.26199); Han et al. [2609.38652](https://arxiv.org/abs/2609.38652) |
| T6 Process-aware agent design | Process models, SOPs and mined knowledge used to build, guide or constrain agents | Kirchdorfer et al. [2607.03228](https://arxiv.org/abs/2607.03228); Bala et al. [2607.04948](https://arxiv.org/abs/2607.04948); Dumas et al. [2601.18833](https://arxiv.org/abs/2601.18833); Hou et al. [2611.14492](https://arxiv.org/abs/2611.14492); Fournier & Limonad [2606.27188](https://arxiv.org/abs/2606.27188); Fillies et al. [2611.13196](https://arxiv.org/abs/2611.13196) |

**Overall picture:** only the two SAP seed papers apply standard process-mining techniques (discovery, alignments, variants, declarative atoms) to LLM-agent logs. The rest of the field analyses agent traces with its own tools (sequence statistics, graph learning, LLM judges, temporal logic). The BPM community mainly uses process mining *to build or steer* agents (T6), not to analyse them.

## Gaps

### G1 – No process mining of multi-agent interaction (direction 4)
- **Evidence:** six 2026 studies analyse multi-agent coordination from traces (Pitre et al. 2610.32060; Liu et al. 2610.10126; Wang et al. 2609.04749; Sun et al. 2608.24569; Wang et al. 2608.29028; Ma et al. 2610.14800), but all use LLM judges, taxonomies or custom graphs. ABM logs `transfer_to_agent` events (Vu et al. 2606.20669) and Körner et al. show per-agent token disparities, but neither applies organisational mining (handover-of-work, social networks, role discovery). Search round 2 (Q2.3) found no 2026 paper doing so.
- **Open question:** do established organisational-mining techniques expose coordination problems (bottleneck agents, delegation loops, context bloat along hand-offs) that the LLM-judge approaches find or miss?

### G2 – Agent designs are compared on metrics, not on process behaviour (direction 6)
- **Evidence:** Borman et al. (2607.14456), Dhanyamraju et al. (2606.20058), Nechepurenko & Shuvalov (2605.03310), Liparulo & Pierri (2608.26199) compare designs on success, latency, tokens or failure signatures; Ma et al. (2605.18332) and Oderinwale (2606.16988) compare behaviour with feature or sequence statistics. None compares architectures through discovered process models, conformance or variant structure. Vu et al. name "only sequential ReAct agents, one model" as a limitation. Round 3 (Q3.3) found no process-mining comparison.
- **Open question:** do process-mining measures (model complexity, fitness to an intended process, variant entropy, rework loops, recovery paths) separate architectures such as ReAct, Plan & Execute and multi-agent orchestration beyond success and cost, and are these differences stable when the LLM changes?

### G3 – Case notion and event abstraction for agent logs are unsettled (directions 1, 2)
- **Evidence:** ABM assumes one conversation = one case and treats each LLM call as atomic (Vu et al.); El Yadouni & Li (2608.02680) show directly-follows ordering misses real producer–consumer dependencies between tool calls; Zhao (2606.22741) separates execution and dependency edges; Gao et al. (2605.13625) offer a behaviour taxonomy usable as activity labels. No 2026 paper uses object-centric event logs (OCEL) for agents; search round 1 (Q1.5) found none, and Vu et al. list OCED as future work.
- **Open question:** which case notion and activity abstraction (conversation vs task vs business object; raw tool names vs taxonomy labels) give stable, interpretable models of agent behaviour, and what does an object-centric view add for multi-agent systems?

### G4 – Conformance checking for agents is built outside BPM (direction 3)
- **Evidence:** compliance work uses LTL/MFOTL/DFA monitors (Elkoussy & Perez 2607.02599; Kekatos et al. 2610.09793; Xavier et al. 2603.20356) or workflow-graph controllers (Wang et al. 2607.25400; Kang et al. 2608.19861). BPMN alignments and declarative process atoms appear only in the SAP seeds. Kekatos et al. show that missing timestamps and approvals in agent logs make history-based rules collapse.
- **Open question:** how do alignment-based and declarative (Declare/LTL) conformance compare on the same agent logs, and which log attributes must agent observability record for conformance to work?

### G5 – No account of acceptable behavioural variability (directions 2, 6)
- **Evidence:** Vu et al. argue variability is intrinsic and call for "normative theories of acceptable variance"; Banerjee & Raichura (2608.13598) show consistency is distinct from success; Ma et al. (2605.18332) find behaviour–outcome rules do not transfer across frameworks; Deng (2606.15579) finds single risky patterns.
- **Open question:** which behavioural variants matter for outcomes, cost or compliance, and can variant analysis separate legitimate adaptation from drift?

### G6 – Little real or production agent data (all directions)
- **Evidence:** most studies use benchmarks, micro-worlds or researcher-built scenarios (Vu et al.; Körner et al.; Ma et al. 2610.14800; Dhanyamraju et al. 2606.20058). Exceptions are single systems or proprietary data: Deng (one production system, 8 days), Hou et al. (Amazon procedures, aggregate results only), Min et al. (deployment sessions, 2609.33295).
- **Open question:** do findings from synthetic logs hold on enterprise agent logs? This is where internal Accenture agent data would add value.

### G7 – The loop from mined insight to agent improvement is rarely closed or evaluated (direction 7)
- **Evidence:** Körner et al. name closing the loop as the next step; Hou et al. (2611.14492), David et al. (2604.10513) and Deng (2606.15579) feed traces back into workflows, prompts or governors, but none measures whether process-mining-derived interventions improve conformance over successive iterations.
- **Open question:** do interventions derived from discovered deviations (prompt or tool-access changes) measurably increase conformance and reduce cost without lowering success?
