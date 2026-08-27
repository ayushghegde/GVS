#!/usr/bin/env python3
from pathlib import Path
import numpy as np, pandas as pd, math

MODULES=['grammar','template','binding','constraint','exact']
SPEC={'grammar':12,'template':10,'binding':8,'constraint':8,'exact':2}
GENERAL=4
N_CELLS=64
N_TRIALS=20000
SEED=132

rng=np.random.default_rng(SEED)
rows=[]
headroom=[]
for _ in range(N_TRIALS):
    weights={m:10**rng.uniform(math.log10(0.25),math.log10(8.0)) for m in MODULES}
    universal=N_CELLS + sum(N_CELLS*weights[m] for m in MODULES)
    installed={m:SPEC[m]+GENERAL for m in MODULES}
    patch=N_CELLS + sum(installed[m]*weights[m] for m in MODULES)
    rows.append(100*(1-patch/universal))
    headroom.append((universal-patch)/sum(installed.values()))

q=np.quantile(rows,[.05,.5,.95])
hq=np.quantile(headroom,[.05,.5,.95])
out=Path(__file__).resolve().parents[1]/'results'
out.mkdir(exist_ok=True)
pd.DataFrame([{
    'optional_module_copies_universal':N_CELLS*len(MODULES),
    'optional_module_copies_patch':sum(SPEC.values())+GENERAL*len(MODULES),
    'optional_module_copy_reduction_pct':100*(1-(sum(SPEC.values())+GENERAL*len(MODULES))/(N_CELLS*len(MODULES))),
    'mean_total_hardware_reduction_pct':float(np.mean(rows)),
    'p05_total_hardware_reduction_pct':float(q[0]),
    'median_total_hardware_reduction_pct':float(q[1]),
    'p95_total_hardware_reduction_pct':float(q[2]),
    'p05_interface_headroom_base_units_per_installed_patch':float(hq[0]),
    'median_interface_headroom_base_units_per_installed_patch':float(hq[1]),
}]).to_csv(out/'patch_cost_summary.csv',index=False)
print(pd.read_csv(out/'patch_cost_summary.csv').to_string(index=False))
