"""Rank-based AUC (Mann-Whitney) of each per-case handover feature for injected vs not-injected traces,
overall and per topology. usage: python feature_auc.py results/case_handover_features.csv results/feature_auc.csv"""
import sys, pandas as pd
F = pd.read_csv(sys.argv[1]); F['y'] = F['injected'].astype(str).eq('True').astype(int)
cols = ['events', 'agent_turns', 'system_msgs', 'handovers', 'distinct_pairs', 'pingpong', 'self_repeat']
def auc(x, y):
    r = x.rank(); n1 = y.sum(); n0 = len(y) - n1
    return (r[y == 1].sum() - n1 * (n1 + 1) / 2) / (n1 * n0) if n1 and n0 else float('nan')
rows = [{'scope': 'all', **{c: round(auc(F[c], F['y']), 3) for c in cols}}]
for t, g in F.groupby('topology'): rows.append({'scope': t, **{c: round(auc(g[c], g['y']), 3) for c in cols}})
R = pd.DataFrame(rows); R.to_csv(sys.argv[2], index=False); print(R.to_string(index=False))
print('cases', len(F), 'injected', int(F['y'].sum()))
