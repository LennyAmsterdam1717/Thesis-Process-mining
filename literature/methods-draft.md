# Methods draft – literature selection (for the thesis / RQ proposal)

_Draft. Numbers are provisional until Frank (Lenny) Pam has verified the included set. Full logs: `literature/search-log.md`, `literature/screening/Screening_TA/`, `literature/screening/Screening_FT/`._

**Design.** Integrative review with a scoping purpose (Academic Research Skills `lit-review` mode). Eligibility: LLM-based agentic systems whose behaviour is treated as process or trace data or linked to process models; published (first version) in 2026; peer-reviewed papers or arXiv preprints.

**Search.** Four rounds of web search (18 Nov 2026) covering arXiv, CEUR-WS, Springer, ACM, IEEE and OpenReview pages; 133 records, 27 duplicates, 31 not from 2026, so 75 records were screened. One seed paper not returned by the search (Körner et al., 2026) was added through "other methods".

**Title/abstract screening.** Protocol v1.0 was confirmed before screening and amended once (v1.1, concept (e): time, cost, steps and tool use count as behaviour) after a calibration pilot on 25 records that Frank had labelled independently. Under v1.1 the AI reviewers missed none of Frank's 17 advances. Two blinded AI reviewers (Claude Sonnet 5.5) with different personas screened every record (agreement 94.7%, Cohen's kappa 0.842, PABAK 0.893). A third AI reviewer adjudicated 4 conflicts, and a senior AI reviewer rechecked all 14 joint exclusions (1 advanced). Frank overrode 2 records (include). Result: 62 advanced, 13 excluded. Tool: SR-Screener 1.0.0 (Academic Research Skills), Claude Code.

**Full-text assessment.** 58 of 62 reports were retrieved (4 publisher-only reports could not be retrieved). **Full-text eligibility was assessed by a single AI reviewer (Claude Opus 5.5) without a second independent reviewer or adjudicator.** The student chose this design to limit cost ("go light"), so no agreement statistics exist for this stage. Full-text rules were fixed before assessment (`ft_protocol.md`). 50 reports were included and 8 excluded.

**Citation check.** Every included paper was verified against the arXiv API (title, authors, first-version date) and the DOI resolver, or for the CEUR paper against the CEUR volume index; 51/51 passed.

**Human verification.** [TO COMPLETE: Frank verifies every included paper and a sample of exclusions, especially the records flagged "borderline"; record outcome and final numbers.]

**Use of AI.** Search, screening, full-text assessment, citation checking and drafting of summaries and research questions were carried out with Claude models in Claude Code. The student reviewed the outputs and is responsible for the final selection and text.
