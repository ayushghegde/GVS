#!/usr/bin/env python3
from pathlib import Path
import numpy as np, pandas as pd, math

SEED=130; N_CELLS=256; T=2000; BATTERY_RATE_FACTOR=1.15
TAUS=[0,1,2,4,8,16]
rng=np.random.default_rng(SEED)

def gen_counts(kind):
    if kind=='uniform': return rng.binomial(N_CELLS,0.02,size=T)
    if kind=='bursty':
        counts=rng.binomial(N_CELLS,0.01,size=T)
        b=rng.choice(T,size=40,replace=False)
        counts[b]+=rng.binomial(N_CELLS,0.18,size=40)
        return counts
    if kind=='aligned':
        counts=rng.binomial(N_CELLS,0.005,size=T)
        for t in range(50,T,100): counts[t]+=128
        return counts
    raise ValueError(kind)

def simulate(counts,tau,tail=400):
    if tau==0: inflow=np.pad(counts.astype(float),(0,tail))
    else:
        L=max(10,int(math.ceil(12*tau)))
        k=np.exp(-np.arange(L)/tau); k=k/k.sum()
        inflow=np.convolve(counts,k,mode='full')
        if len(inflow)<T+tail: inflow=np.pad(inflow,(0,T+tail-len(inflow)))
        inflow=inflow[:T+tail]
    rate=counts.mean()*BATTERY_RATE_FACTOR
    reservoir=peak=battery=0.0
    for x in inflow:
        reservoir+=x
        y=min(reservoir,rate); reservoir-=y; battery+=y; peak=max(peak,reservoir)
    total=float(counts.sum())
    return dict(peak_inflow=float(inflow.max()),peak_reservoir_charge_units=peak,
                transferred_fraction=battery/total if total else 1.0,
                battery_rate_units_per_interval=rate)

rows=[]
for scenario in ('uniform','bursty','aligned'):
    counts=gen_counts(scenario); base=simulate(counts,0)
    for tau in TAUS:
        r=simulate(counts,tau)
        r.update(scenario=scenario,tau_event_intervals=tau,
                 peak_inflow_reduction_pct=100*(1-r['peak_inflow']/base['peak_inflow']),
                 peak_reservoir_reduction_pct=100*(1-r['peak_reservoir_charge_units']/base['peak_reservoir_charge_units']))
        rows.append(r)
out=Path(__file__).resolve().parents[1]/'results'; out.mkdir(exist_ok=True)
df=pd.DataFrame(rows); df.to_csv(out/'charge_egress_sweep.csv',index=False)
df[df.tau_event_intervals==8].to_csv(out/'selected_tau8_summary.csv',index=False)
print(df[df.tau_event_intervals==8][['scenario','peak_inflow_reduction_pct','peak_reservoir_reduction_pct','transferred_fraction']].to_string(index=False))
