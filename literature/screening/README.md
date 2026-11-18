# Screening (SR-Screener)

| File | What it is |
|---|---|
| `screening_protocol.md` | Confirmed eligibility rules (v1.0, 2026-11-18), sent verbatim to the AI reviewers |
| `screening_config.json` | Exclusion codes and order, core criteria, reviewer personas, QC settings, models |
| `inputs/records_2026.csv` | The 75 unique 2026 records from search rounds 1–4 (metadata from the arXiv API) |
| `sr_work/` | SR-Screener work folder: records, batches, identification counts, generated prompts |
| `pilot_batch_to_read.md` | **Calibration batch b001** – the 25 titles/abstracts to read |
| `pilot_labels.csv` | **Fill this in**: one row per pilot record (`d`, `code`, `why`) |

## Status (2026-11-18)

1. ✅ Protocol confirmed
2. ✅ Records prepared (75 records, 3 batches of 25, seed R00011 found)
3. ⏳ **Frank labels the calibration batch** (`pilot_labels.csv`) – independently, before seeing any AI decision
4. ⏳ AI pilot on b001 (Reviewers A + B), then comparison with Frank's labels
5. ⏳ Full title/abstract run on b002–b003, adjudication, QC recheck of joint exclusions
6. ⏳ Full-text check, citation check, then `papers.csv`

## How to fill in `pilot_labels.csv`

Open it in Excel or any text editor. For each row write:

- `d`: `include`, `unclear` or `exclude`
- `code`: `INC`, `UNC`, or for an exclusion the **first** failing code: `E1` year · `E2` publication type · `E3` not LLM agents · `E4` wrong direction (kept as background) · `E5` no process/trace angle · `E9` other
- `why`: the deciding fact in ≤ 15 words

Every row must be filled in (the comparison script rejects empty or mismatched rows). Save as CSV, keep the column names, then tell Claude "pilot labels done".
