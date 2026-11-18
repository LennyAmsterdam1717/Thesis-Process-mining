# Runbook: what happens when Frank says "go"

_Prepared 2026-11-18. Claude follows this top to bottom when Frank prompts "go" (or "go light")._

## What "go" means

By saying **"go"**, Frank:
1. **confirms screening protocol v1.1** exactly as worded in `literature/screening/screening_protocol_v1.1_pending.md` (amendment to concept (e): time, cost, steps, tool usage, rework and coordination overhead count as behaviour);
2. **approves the screening cost**: about 8–12 Sonnet reviewer calls for title/abstract (re-pilot, full run, adjudication, QC recheck) **plus** full-text dual review, two calls per advanced paper (expected about 30–40 papers → roughly 60–80 calls on long PDFs);
3. asks Claude to continue the whole RQ brief (screening → citation check → papers.csv → summaries → gap analysis → RQs → shortlist → email draft) without further check-ins, except at the stop conditions below.

**"go light"** means the same, except the full-text stage is a **single-reviewer** check by Claude (much cheaper, disclosed as single-reviewer in the methods and the decisions log).

## Steps (commit and push after each one)

1. **Activate v1.1.** Replace `screening_protocol.md` with the pending file, set the header to "Version 1.1, confirmed by Frank (Lenny) Pam on <date> ("go")", delete the `_pending` file, log in `docs/decisions.md`.
2. **Re-pilot b001 under v1.1.** `build_workflow.py ta --jobs pilot --batches b001 --emit-prompts sr_work/prompts_pilot2` → Reviewer A and B (`academic-research-skills:screening-reviewer-agent`, sonnet) → save returns in `sr_work/decisions/` with the full label from `index.json` → `merge_decisions.py --from sr_work/decisions --overrides overrides.csv --pilot-labels pilot_labels.csv`. Adjudicate conflicts with `--jobs pending` (within the pilot).
   - **STOP** if the AI still excludes any record Frank advanced: report it and propose wording; do not override the gate.
3. **Full title/abstract run.** `--jobs all` (b002, b003) → A + B → merge → `--jobs pending` until no conflicts or missing decisions remain.
4. **QC recheck.** `--jobs recheck` (all joint exclusions, since there are fewer than 100, plus near-miss records) → merge until it prints "complete".
5. **TA outputs.** `build_outputs.py --work sr_work --out Screening_TA --config screening_config.json`; copy the PRISMA counts into `literature/search-log.md`; list every E4 exclusion in `literature/background.md` (Frank's rule: kept as background).
6. **Full text.** Download the arXiv PDFs of advanced records into `literature/screening/fulltext/` (PDFs are git-ignored), named by record ID; `prepare_fulltext.py`; write `ft_protocol.md` (copy of v1.1 with the full-text rules, including Frank's single-LLM rule: include if the LLM uses tools or acts in an environment, otherwise exclude → background). Dual review (go) or single review (go light). Merge, `build_outputs.py --stage ft`, FT PRISMA counts into the search log.
7. **Citation check.** Run the `academic-paper` citation-check on every included paper (title, authors, year, venue, DOI/arXiv link against the arXiv API or DOI resolver). Only papers that pass go into `literature/papers.csv`, with all columns filled (peer-reviewed vs preprint label, directions 1–7, contribution, limitations/future work).
8. **Summaries.** One note per key paper in `literature/summaries/<first-author-year-keyword>.md` (paraphrased; includes the two seed papers).
9. **Research questions.** `research-questions/gap-analysis.md` (themes + 5–8 gaps tied to papers), `rq-candidates.md` (3–5 RQs in the brief's format), `rq-shortlist.md` (top 2–3 + rationale), `email-xixi-draft.md` (≤ 250 words).
10. **Wrap-up.** Update `docs/decisions.md`, `docs/timeline.md`, `README.md`; final commit and push; short summary for Frank: number of papers, top RQs, open questions.

## Stop conditions (Claude stops and asks)

- The re-pilot still misses a record Frank advanced.
- Fewer than 15 papers survive full text and citation check (say so plainly; do not widen beyond 2026).
- A paper fails the citation check in a way that changes an RQ's evidence base.
- Any step would push PDFs, Word files or other git-ignored material.

## Frank still has to do (not blocked by "go")

- **Verify the final included set** (every advanced record and a sample of exclusions). SR-Screener requires a human sign-off before the counts are final; the RQ drafts will say "screening pending Frank's verification".
