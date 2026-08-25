#!/usr/bin/env python3
from pathlib import Path
import csv

LOCAL_OCTET_FJ=1324.1144
ROUTE_FJ=17.765
fallbacks=[0.01,0.05,0.10,0.25,0.50,0.75]
exact_pj=[0.5,1,2,5,10,50,100]
rows=[]
for e_pj in exact_pj:
    exact=e_pj*1000
    exact_every=exact+ROUTE_FJ
    for f in fallbacks:
        local_first=LOCAL_OCTET_FJ+f*exact_every
        rows.append({
            'exact_compute_pj':e_pj,
            'fallback_fraction':f,
            'exact_every_episode_pj':exact_every/1000,
            'local_first_pj':local_first/1000,
            'saving_percent':100*(1-local_first/exact_every),
        })

out=Path(__file__).resolve().parents[1]/'results'/'energy_frontier.csv'
with out.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)

be=[]
for f in fallbacks:
    threshold_fj=LOCAL_OCTET_FJ/(1-f)-ROUTE_FJ
    be.append({'fallback_fraction':f,'local_resolution_fraction':1-f,'break_even_exact_compute_pj':threshold_fj/1000})
out2=Path(__file__).resolve().parents[1]/'results'/'break_even.csv'
with out2.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=be[0].keys()); w.writeheader(); w.writerows(be)
print(out); print(out2)
