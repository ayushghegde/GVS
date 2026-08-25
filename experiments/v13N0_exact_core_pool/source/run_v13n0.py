#!/usr/bin/env python3
from itertools import combinations
from pathlib import Path
import csv

ROUTE_FJ_PER_MM = 3.74
XS = [1.25, 3.75, 6.25, 8.75]
YS = XS
ZS = [0.5, 1.5]
OCTETS = [(x,y,z) for x in XS for y in YS for z in ZS]
CANDIDATES = [(x,y,1.0) for x in XS for y in YS]

def md(a,b):
    return sum(abs(a[i]-b[i]) for i in range(3))

def best_for_k(k):
    if k == 1:
        centers=[(5.0,5.0,1.0)]
        ds=[md(o,centers[0]) for o in OCTETS]
        return sum(ds)/len(ds), max(ds), centers
    if k == 32:
        return 0.0, 0.0, OCTETS
    best=None
    for comb in combinations(CANDIDATES,k):
        ds=[min(md(o,c) for c in comb) for o in OCTETS]
        score=(sum(ds)/len(ds), max(ds))
        if best is None or score < best[:2]:
            best=(score[0],score[1],comb)
    return best

rows=[]
for k in [1,2,4,8,16,32]:
    avg,mx,locs=best_for_k(k)
    rows.append({
        'exact_core_copies':k,
        'copies_removed_vs_per_octet':32-k,
        'copy_reduction_percent':100*(32-k)/32,
        'avg_one_way_mm':avg,
        'max_one_way_mm':mx,
        'avg_round_trip_route_fj':2*avg*ROUTE_FJ_PER_MM,
        'locations':'|'.join(','.join(str(v) for v in p) for p in locs),
    })
out=Path(__file__).resolve().parents[1]/'results'/'exact_core_pool.csv'
with out.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
print(out)
