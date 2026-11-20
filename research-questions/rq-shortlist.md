# RQ shortlist (top 3)

_Draft; screening pending Frank's verification. Full versions in `rq-candidates.md`._

| Rank | RQ | Direction | Main gap | Data dependency | Feasibility |
|---|---|---|---|---|---|
| 1 | **RQ-A** – Comparing agent architectures as processes | 6 | G2 | Rebuilt case + public; Accenture optional | high |
| 2 | **RQ-B** – Organisational mining of multi-agent interaction | 4 | G1 | Public (day 1) + rebuilt case; Accenture optional | medium–high |
| 3 | **RQ-C** – Alignment-based vs declarative conformance for agents | 3 | G4 | Rebuilt case + public | high |
| new (rank to decide) | **RQ-F** – Comparing multi-agent orchestration patterns with process mining | 4, 6 | G1 + G2 | Public (day 1) + rebuilt case; Accenture optional | medium–high |

## Rationale

1. **RQ-A first.** It matches direction 6, which Frank prefers, and fills the clearest gap. Several 2026 papers compare architectures (Borman et al. 2607.14456, Dhanyamraju et al. 2606.20058, Ma et al. 2605.18332), but none does it with process mining, and the seed paper names "ReAct only, one model" as its own limitation (Vu et al. 2606.20669). It is an experimental design, which Xixi is open to. It does not depend on Accenture data, which lowers the risk if internal agent logs turn out to be unavailable. For Accenture the result is direct: which architecture to use for which kind of client process.
2. **RQ-B second.** It matches direction 4, which Frank prefers. The gap is sharp: six 2026 multi-agent failure studies exist, none uses organisational mining, and search round 2 found nothing. Public labelled traces (Liu et al. 2610.10126; Nechepurenko & Shuvalov 2605.03310) allow a start before any Accenture data arrives. It is slightly riskier (trace conversion, label mapping), and it is the best use of internal Accenture multi-agent logs if they exist.
3. **RQ-C third.** It is a safe, well-scoped fallback with clear ground truth (fault injection), and it fits Xixi's conformance expertise. It is less novel because the SAP seeds already show both techniques.

4. **RQ-F (added 2026-11-20, not yet ranked).** Matches Frank's main interest, multi-agent orchestration, and directions 4 and 6. It compares orchestration patterns (supervisor/hierarchical, sequential pipeline, selector-based group chat) on the same business process, using process mining as the measuring tool: conformance against the intended BPMN model (with precision), variants and loops, and organisational mining of hand-offs (handover-of-work networks, bottleneck agents, ping-pong). The gap is clear: Vu et al. 2606.20669 mine only sequential ReAct agents and name other architectures as future work, while Nechepurenko & Shuvalov 2605.03310, Liu et al. 2610.10126, Dhanyamraju et al. 2606.20058 and Zhu et al. 2606.01199 compare coordination set-ups without process mining. Released multi-agent traces (Nechepurenko & Shuvalov; MAScope-Bench; Who&When) allow a start before any own system is built. It overlaps with RQ-A (multi-agent arm) and RQ-B (organisational mining) and could replace both as one merged question. Full version in `rq-candidates.md`.

**Possible combination:** RQ-A and RQ-B share the same infrastructure (ABM logging of a rebuilt multi-agent case). A thesis could take RQ-A as the main question and B2 as a sub-question if the multi-agent architecture is one of the compared designs.

**Not shortlisted:** RQ-D (case notion, OCEL) is valuable but more methodological and harder to motivate for Accenture; it could become a chapter inside RQ-A or RQ-B. RQ-E (closing the loop) depends on many design choices and would fit better as future work.

## Open points before sending

- Confirm with Accenture (Nino Hulsthoff) whether internal, non-client agent logs exist and in which format (OpenTelemetry? LangSmith?). This decides "Accenture internal" vs "rebuilt case" for all three RQs.
- Confirm the numbering of directions 1–7 against Xixi's project description.
