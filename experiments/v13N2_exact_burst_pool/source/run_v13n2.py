#!/usr/bin/env python3
from pathlib import Path
import csv, math

N=32
ps=[0.01,0.02,0.05,0.10,0.20,0.25,0.50]
targets=[1e-2,1e-3,1e-4]

def tail(p,k):
    return sum(math.comb(N,i)*p**i*(1-p)**(N-i) for i in range(k+1,N+1))
rows=[]
for p in ps:
    for target in targets:
        k=next(k for k in range(N+1) if tail(p,k)<=target)
        rows.append({
            'fallback_probability_per_octet':p,
            'overflow_target':target,
            'exact_service_slots_required':k,
            'slots_removed_vs_one_per_octet':N-k,
            'slot_reduction_percent':100*(N-k)/N,
            'actual_overflow_probability':tail(p,k),
        })
out=Path(__file__).resolve().parents[1]/'results'/'burst_pool.csv'
with out.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
print(out)
