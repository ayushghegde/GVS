#!/usr/bin/env python3
from pathlib import Path
import csv
LOCAL_FJ=1324.1144
routes={1:41.14,2:29.4525,4:17.765,8:13.09,16:3.74}
fallbacks=[0.01,0.05,0.10,0.25,0.50]
rows=[]
for k,rt in routes.items():
    for f in fallbacks:
        avg=f*rt
        rows.append({
            'exact_core_copies':k,
            'fallback_fraction':f,
            'avg_exact_transport_fj_per_episode':avg,
            'transport_tax_percent_of_local_octet':100*avg/LOCAL_FJ,
        })
out=Path(__file__).resolve().parents[1]/'results'/'shared_service_tax.csv'
with out.open('w',newline='') as fp:
    w=csv.DictWriter(fp,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
print(out)
