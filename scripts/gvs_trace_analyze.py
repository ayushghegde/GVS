#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,json,math,statistics
from pathlib import Path

def fbool(v):
    return str(v).strip().lower() in {'1','true','yes','y'}

def quantile_nearest(xs,q):
    if not xs:return 0
    s=sorted(xs)
    idx=max(0,min(len(s)-1,math.ceil(q*len(s))-1))
    return s[idx]

def slots_for_overflow(counts,target):
    if not counts:return 0
    for k in range(max(counts)+1):
        if sum(c>k for c in counts)/len(counts) <= target:
            return k
    return max(counts)

def analyze(path,slots=None):
    rows=list(csv.DictReader(Path(path).open()))
    if not rows:raise SystemExit('trace is empty')
    required={'epoch','octet','workload','local_result','exact_request','cross_handoffs','memory_units','wrong_accept'}
    missing=required-set(rows[0])
    if missing:raise SystemExit('missing required trace columns: '+','.join(sorted(missing)))
    episodes=len(rows)
    exact=sum(fbool(r['exact_request']) for r in rows)
    wrong=sum(int(float(r['wrong_accept'] or 0)) for r in rows)
    cross=sum(float(r['cross_handoffs'] or 0) for r in rows)
    mem=sum(float(r['memory_units'] or 0) for r in rows)
    local_accept=sum(r['local_result'].strip().lower()=='accept' and not fbool(r['exact_request']) for r in rows)
    local_ops=sum(float(r.get('local_ops') or 0) for r in rows)
    leases=sum(float(r.get('lease_count') or 0) for r in rows)
    by_epoch={}
    for r in rows:
        e=r['epoch']; by_epoch.setdefault(e,0)
        by_epoch[e]+=int(fbool(r['exact_request']))
    counts=list(by_epoch.values())
    mean=statistics.mean(counts)
    var=statistics.pvariance(counts) if len(counts)>1 else 0.0
    summary={
        'episodes':episodes,
        'epochs':len(counts),
        'local_resolution_fraction':local_accept/episodes,
        'ambiguity_budget':exact/episodes,
        'wrong_robust_accepts':wrong,
        'cross_handoffs_per_episode':cross/episodes,
        'memory_units_per_episode':mem/episodes,
        'local_ops_per_lease':(local_ops/leases if leases else None),
        'exact_requests_per_epoch':{
            'mean':mean,
            'p95':quantile_nearest(counts,0.95),
            'p99':quantile_nearest(counts,0.99),
            'p999':quantile_nearest(counts,0.999),
            'max':max(counts),
            'variance':var,
            'fano_factor':(var/mean if mean else 0.0),
        },
        'empirical_exact_slots':{
            'overflow_le_1pct':slots_for_overflow(counts,0.01),
            'overflow_le_0p1pct':slots_for_overflow(counts,0.001),
            'overflow_le_0p01pct':slots_for_overflow(counts,0.0001),
        },
    }
    if slots is not None:
        backlog=0; max_backlog=0; total_backlog=0
        for demand in counts:
            backlog=max(0,backlog+demand-slots)
            max_backlog=max(max_backlog,backlog); total_backlog+=backlog
        summary['queue_if_slots']={'slots':slots,'max_backlog_requests':max_backlog,'mean_end_epoch_backlog':total_backlog/len(counts),'final_backlog':backlog}
    workloads={}
    for w in sorted(set(r['workload'] for r in rows)):
        wr=[r for r in rows if r['workload']==w]
        workloads[w]={
            'episodes':len(wr),
            'ambiguity_budget':sum(fbool(r['exact_request']) for r in wr)/len(wr),
            'wrong_robust_accepts':sum(int(float(r['wrong_accept'] or 0)) for r in wr),
        }
    summary['by_workload']=workloads
    return summary

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('trace')
    ap.add_argument('--slots',type=int)
    ap.add_argument('--out')
    a=ap.parse_args()
    s=analyze(a.trace,a.slots)
    text=json.dumps(s,indent=2,sort_keys=True)
    if a.out:Path(a.out).write_text(text+'\n')
    print(text)
if __name__=='__main__':main()
