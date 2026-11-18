"""Convert MAScope-Bench LG-Ctrl traces (raw text) into an event log.

Each "[speaker]" block in a trajectory becomes one event:
  case:concept:name = trace_id, concept:name = speaker (e.g. agent_A, system),
  org:resource = speaker, time:timestamp = synthetic (case start + 1 s per position;
  the dataset has no timestamps, so only the ORDER is real).
Case attributes: topology, anomaly_injected, anomaly_type, llm, task_type, complexity,
and the 14 MAST labels (as case:mast_<code>).
Message text is NOT copied into the log (only its length), to keep the log small.

usage: python convert_mascope.py <LG-Ctrl.jsonl> <out_dir> [sample_per_topology]
"""
import ast, json, random, re, sys, os
from datetime import datetime, timedelta
import pandas as pd
import pm4py

src, out = sys.argv[1], sys.argv[2]
k = int(sys.argv[3]) if len(sys.argv) > 3 else 5
os.makedirs(out, exist_ok=True)
# Only these speaker headers start an event; other bracketed lines (e.g. '[Insert Logo Here]') are message text.
# Lower-case agent_a/agent_b (used in some templates) are normalised to agent_A/agent_B.
SPK = re.compile(r'^\[(system|agent_[A-Ea-e]|verifier|reviewer)\]\s*$', re.M)
rows, base = [], datetime(2026, 1, 1)
recs = [json.loads(l) for l in open(src)]
for ci, r in enumerate(recs):
    t = r['trajectory']; ms = list(SPK.finditer(t))
    ann = r['mast_annotation']; ann = ast.literal_eval(ann) if isinstance(ann, str) else ann
    start = base + timedelta(hours=ci)
    for i, m in enumerate(ms):
        end = ms[i + 1].start() if i + 1 < len(ms) else len(t)
        spk = m.group(1).strip()
        if spk.startswith('agent_'): spk = 'agent_' + spk[-1].upper()
        rows.append({'case:concept:name': r['trace_id'], 'concept:name': spk, 'org:resource': spk,
                     'time:timestamp': start + timedelta(seconds=i), 'position': i,
                     'msg_chars': len(t[m.end():end].strip()),
                     'case:topology': r['guo_topology'], 'case:anomaly_injected': str(r['anomaly_injected']),
                     'case:anomaly_type': r.get('anomaly_type') or 'none', 'case:llm': r['llm_name'],
                     'case:task_type': r.get('task_type'), 'case:complexity': r.get('complexity'),
                     **{f'case:mast_{a}': int(v) for a, v in ann.items()}})
df = pd.DataFrame(rows)
df.to_csv(os.path.join(out, 'lgctrl_events.csv'), index=False)
log = pm4py.format_dataframe(df, case_id='case:concept:name', activity_key='concept:name', timestamp_key='time:timestamp')
pm4py.write_xes(log, os.path.join(out, 'lgctrl_full.xes'))
# small stratified sample (k traces per topology, fixed seed) for the repository
rng = random.Random(2026); keep = []
for topo, g in df.groupby('case:topology'):
    ids = sorted(g['case:concept:name'].unique()); keep += rng.sample(ids, k)
samp = df[df['case:concept:name'].isin(keep)]
pm4py.write_xes(pm4py.format_dataframe(samp, case_id='case:concept:name', activity_key='concept:name', timestamp_key='time:timestamp'),
                os.path.join(out, 'lgctrl_sample.xes'))
print(f'cases {df["case:concept:name"].nunique()}  events {len(df)}  sample cases {len(keep)}  sample events {len(samp)}')
print(df.groupby('case:topology')['concept:name'].agg(lambda s: sorted(s.unique())).to_string())
