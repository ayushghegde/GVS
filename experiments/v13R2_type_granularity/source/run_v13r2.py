#!/usr/bin/env python3
from pathlib import Path
import pandas as pd

BASE=64
ARCH={
 'universal_1type':{'types':1,'module_copies':320},
 'coarse_4type':{'types':4,'module_copies':174},
 'fine_7type':{'types':7,'module_copies':60},
}
rows=[]
for penalty in [0,1,2,4,8,16,24,32,40,48,64]:
    for name,a in ARCH.items():
        cost=BASE+a['module_copies']+penalty*(a['types']-1)
        rows.append(dict(type_penalty_units_per_extra_type=penalty,architecture=name,cell_types=a['types'],optional_module_copies=a['module_copies'],total_abstract_cost_units=cost,reduction_vs_universal_zero_penalty_pct=100*(1-cost/384)))
out=Path(__file__).resolve().parents[1]/'results'; out.mkdir(exist_ok=True)
df=pd.DataFrame(rows); df.to_csv(out/'type_granularity_sweep.csv',index=False)
be=pd.DataFrame([dict(fine_vs_coarse_break_even_penalty_units_per_extra_type=(238-124)/3,
                      fine_vs_universal_break_even_penalty_units_per_extra_type=(384-124)/6,
                      coarse_vs_universal_break_even_penalty_units_per_extra_type=(384-238)/3)])
be.to_csv(out/'break_even.csv',index=False)
print(df[df.type_penalty_units_per_extra_type.isin([0,16,32,40])].to_string(index=False))
print(be.to_string(index=False))
