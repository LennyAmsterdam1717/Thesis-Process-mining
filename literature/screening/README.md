# Screening (SR-Screener)

| File | What it is |
|---|---|
| `screening_protocol.md` | Confirmed eligibility rules (v1.1, 2026-11-18), sent verbatim to the AI reviewers |
| `ft_protocol.md` | Full-text protocol (v1.1 + full-text rules) |
| `screening_config.json` | Exclusion codes and order, core criteria, reviewer personas, QC settings, models |
| `inputs/records_2026.csv` | The 75 unique 2026 records from search rounds 1–4 (metadata from the arXiv API) |
| `sr_work/` | SR-Screener work folder: records, batches, identification counts, generated prompts |
| `pilot_batch_to_read.md` | **Calibration batch b001** – the 25 titles/abstracts to read |
| `pilot_labels.csv` | **Fill this in**: one row per pilot record (`d`, `code`, `why`) |

## Status (2026-11-18, after "go light")

1. ✅ Protocol v1.1 confirmed (`screening_protocol.md`); full-text rules in `ft_protocol.md`
2. ✅ Calibration pilot 2 passed (AI missed 0 of Frank's 17 advances)
3. ✅ Title/abstract screening: 75 → 62 advanced, 13 excluded (`Screening_TA/`)
4. ✅ Full text (single AI reviewer): 58 assessed → 50 included, 8 excluded, 4 not retrieved (`Screening_FT/`)
5. ✅ Citation check 51/51 (incl. seed via other methods) → `../papers.csv`
6. ⏳ **Frank verifies the included set** (and the rows flagged "borderline") – counts are provisional until then

PDFs are in `fulltext/` (git-ignored, named by record ID).

## How to fill in `pilot_labels.csv`

Open it in Excel or any text editor. For each row write:

- `d`: `include`, `unclear` or `exclude`
- `code`: `INC`, `UNC`, or for an exclusion the **first** failing code: `E1` year · `E2` publication type · `E3` not LLM agents · `E4` wrong direction (kept as background) · `E5` no process/trace angle · `E9` other
- `why`: the deciding fact in ≤ 15 words

Every row must be filled in (the comparison script rejects empty or mismatched rows). Save as CSV, keep the column names, then tell Claude "pilot labels done".
