"""RQ-B feasibility pilot on MAScope-Bench LG-Ctrl (converted by convert_mascope.py).

1) Process discovery: Inductive Miner per topology; token-based replay fitness and precision.
2) Handover-of-work (pm4py.discover_handover_of_work_network) per topology.
3) Descriptive comparison of simple handover features between traces with and without injected anomalies.
usage: python analyse_pilot.py <events.csv> <results_dir>
"""
import json, sys, os, collections
import pandas as pd, pm4py
src, out = sys.argv[1], sys.argv[2]; os.makedirs(out, exist_ok=True)
df = pd.read_csv(src); df['time:timestamp'] = pd.to_datetime(df['time:timestamp'])
log = pm4py.format_dataframe(df, case_id='case:concept:name', activity_key='concept:name', timestamp_key='time:timestamp')
res = {'n_cases': int(df['case:concept:name'].nunique()), 'n_events': int(len(df)), 'per_topology': {}}
for topo, g in log.groupby('case:topology'):
    net, im, fm = pm4py.discover_petri_net_inductive(g, noise_threshold=0.2)
    fit = pm4py.fitness_token_based_replay(g, net, im, fm)
    prec = pm4py.precision_token_based_replay(g, net, im, fm)
    var = pm4py.get_variants(g)
    how = pm4py.discover_handover_of_work_network(g)
    edges = {f'{a}->{b}': round(float(w), 4) for (a, b), w in how.connections.items()} if hasattr(how, 'connections') else {}
    pm4py.write_pnml(net, im, fm, os.path.join(out, f'im_{topo.replace(" ", "_")}.pnml'))
    try:
        pm4py.save_vis_petri_net(net, im, fm, os.path.join(out, f'im_{topo.replace(" ", "_")}.png'))
        pm4py.save_vis_sna(how, os.path.join(out, f'handover_{topo.replace(" ", "_")}.png'), variant_str='pyvis') if False else None
    except Exception as e:
        print('vis skipped:', e)
    res['per_topology'][topo] = {'cases': int(g['case:concept:name'].nunique()), 'variants': len(var),
        'im_places': len(net.places), 'im_transitions': len(net.transitions),
        'fitness_log': round(fit['log_fitness'], 3), 'precision': round(prec, 3), 'handover_edges': edges}
# per-case handover features
feat = []
for cid, g in df.sort_values(['case:concept:name', 'position']).groupby('case:concept:name'):
    seq = list(g['org:resource']); ag = [s for s in seq if s != 'system']
    hand = [(a, b) for a, b in zip(ag, ag[1:]) if a != b]
    pingpong = sum(1 for x, y, z in zip(ag, ag[1:], ag[2:]) if x == z and x != y)
    feat.append({'case': cid, 'topology': g['case:topology'].iat[0], 'injected': g['case:anomaly_injected'].iat[0],
                 'anomaly_type': g['case:anomaly_type'].iat[0], 'events': len(seq), 'agent_turns': len(ag),
                 'system_msgs': seq.count('system'), 'handovers': len(hand), 'distinct_pairs': len(set(hand)),
                 'pingpong': pingpong, 'self_repeat': sum(1 for a, b in zip(ag, ag[1:]) if a == b)})
F = pd.DataFrame(feat); F.to_csv(os.path.join(out, 'case_handover_features.csv'), index=False)
cols = ['events', 'agent_turns', 'system_msgs', 'handovers', 'distinct_pairs', 'pingpong', 'self_repeat']
by_inj = F.groupby(['topology', 'injected'])[cols].mean().round(2)
by_type = F.groupby('anomaly_type')[cols].mean().round(2)
by_inj.to_csv(os.path.join(out, 'features_by_topology_injected.csv')); by_type.to_csv(os.path.join(out, 'features_by_anomaly_type.csv'))
json.dump(res, open(os.path.join(out, 'discovery_handover_summary.json'), 'w'), indent=1)
print(json.dumps({t: {k: v for k, v in d.items() if k != 'handover_edges'} for t, d in res['per_topology'].items()}, indent=1))
for t, d in res['per_topology'].items(): print(t, sorted(d['handover_edges'].items(), key=lambda x: -x[1])[:6])
print(by_inj.to_string()); print(by_type.to_string())
