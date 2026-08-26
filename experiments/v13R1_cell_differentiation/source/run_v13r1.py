#!/usr/bin/env python3
from pathlib import Path
import numpy as np, pandas as pd, math

MODULES=['grammar','template','binding','constraint','exact']
SPEC={'grammar':12,'template':10,'binding':8,'constraint':8,'exact':2}
COORDS=[(x,y,z) for x in range(4) for y in range(4) for z in range(4)]
PROBS=np.array([.28,.20,.18,.28,.06])

def cheb(a,b): return max(abs(a[i]-b[i]) for i in range(3))

def make_assign(general):
    relay=64-sum(SPEC.values())-general
    roles=['relay']*relay
    for r,n in SPEC.items(): roles += [r]*n
    roles += ['general']*general
    rr=np.random.default_rng(1000+general); rr.shuffle(roles)
    perm=sorted(COORDS,key=lambda c:((c[0]*17+c[1]*31+c[2]*43)%67,c))
    return dict(zip(perm,roles)),relay

def avg_route(assign,nseq=5000):
    capable={m:[c for c,r in assign.items() if r==m or r=='general'] for m in MODULES}
    rr=np.random.default_rng(2000+sum(r=='general' for r in assign.values()))
    hops=[]
    for _ in range(nseq):
        seq=list(rr.choice(MODULES,size=int(rr.integers(2,6)),p=PROBS)); cur=COORDS[int(rr.integers(64))]; h=0
        for m in seq:
            nxt=min(capable[m],key=lambda c:(cheb(cur,c),c)); h+=cheb(cur,nxt); cur=nxt
        hops.append(h)
    return float(np.mean(hops)),float(np.quantile(hops,.95))

def availability(assign,pfail=.10,trials=10000):
    rr=np.random.default_rng(3000+sum(r=='general' for r in assign.values())); cells=list(assign); ok=0
    for _ in range(trials):
        live=[assign[c] for c in cells if rr.random()>pfail]
        ok += all((m in live) or ('general' in live) for m in MODULES)
    return ok/trials

rows=[]
for g in [0,2,4,8,12,16,20,24]:
    a,relay=make_assign(g); avg,p95=avg_route(a); avail=availability(a)
    copies=sum(SPEC[m]+g for m in MODULES)
    rows.append(dict(general_cells=g,relay_cells=relay,optional_module_copy_reduction_pct=100*(1-copies/(64*5)),
                     avg_extra_cell_hops_per_mixed_episode=avg,p95_extra_hops=p95,
                     all_module_classes_available_after_10pct_random_cell_failures=avail,
                     avg_extra_route_energy_fJ_at_0p15fJ_per_hop=avg*0.15))
out=Path(__file__).resolve().parents[1]/'results'; out.mkdir(exist_ok=True)
df=pd.DataFrame(rows); df.to_csv(out/'differentiation_sweep.csv',index=False)
print(df[df.general_cells==4].to_string(index=False))
