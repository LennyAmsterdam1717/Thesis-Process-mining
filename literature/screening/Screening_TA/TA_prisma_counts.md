# PRISMA 2020 counts - title/abstract stage

```mermaid
flowchart TD
  I["Records identified from databases (n = 75)<br/>Web search (arXiv API metadata) n = 75"]
  R["Records removed before screening:<br/>duplicate records (n = 0)"]
  S["Records screened (n = 75)"]
  X["Records excluded (n = 13)<br/>E3 System studied is not an LLM-based / generative AI agentic system: 3<br/>E4 LLMs/agents used to perform process mining on ordinary logs; agents' own behaviour not analysed: 4<br/>E5 No treatment of agent behaviour as process/trace data and no link to process models: 6"]
  F["Reports sought for retrieval (n = 62)"]
  I --> R
  I --> S
  S --> X
  S --> F
```

```json
{
 "stage": "ta",
 "tool": "sr-screener 1.0.0",
 "complete": true,
 "pending_records": 0,
 "state_problems": [],
 "identified_by_database": {
  "Web search (arXiv API metadata)": 75
 },
 "identified_total": 75,
 "duplicates_removed": 0,
 "records_screened": 75,
 "records_to_screen": 75,
 "records_excluded": 13,
 "excluded_by_code": {
  "E3": 3,
  "E4": 4,
  "E5": 6
 },
 "reports_sought_for_retrieval": 62,
 "advanced_include": 43,
 "advanced_unclear": 19,
 "advanced_outside_allowed_languages": 0,
 "agreement": {
  "n": 75,
  "both_advance": 57,
  "both_exclude": 14,
  "a_only_advance": 0,
  "b_only_advance": 4,
  "observed_agreement": 0.9467,
  "kappa": 0.842,
  "pabak": 0.893,
  "conflicts": 4,
  "resolved_by": {
   "A+B": 69,
   "Frank": 2,
   "ADJ": 3,
   "QC": 1
  }
 },
 "decided_by": {
  "A+B": 69,
  "Frank": 2,
  "ADJ": 3,
  "QC": 1
 }
}
```
