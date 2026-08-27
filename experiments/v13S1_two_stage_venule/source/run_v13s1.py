#!/usr/bin/env python3
from pathlib import Path
import math, numpy as np, pandas as pd

N=256; T=2000; TAIL=400; BATTERY_RATE_FACTOR=1.15
SCENARIOS=['uniform','bursty','aligned']
GROUPS=[2,4,8,16,32]
CELL_TAUS=[1,2,3,4,6]
VENULE_TAUS=[4,6,8,12]

def kernel(tau):
    L=max(10,int(math.ceil(12*tau)))
    k=np.exp(-np.arange(L)/tau); return k/k.sum()

def matrix(kind,seed):
    rr=np.random.default_rng(seed)
    if kind=='uniform': return rr.binomial(1,.02,size=(T,N))
    if kind=='bursty':
        m=rr.binomial(1,.01,size=(T,N)); burst=rr.choice(T,size=40,replace=False)
        for t in burst: m[t]=np.maximum(m[t],rr.binomial(1,.18,size=N))
        return m
    if kind=='aligned':
        m=rr.binomial(1,.005,size=(T,N))
        for t in range(50,T,100): m[t,:128]=1
        return m
    raise ValueError(kind)

def direct(counts,tau=8):
    c=np.convolve(counts,kernel(tau),mode='full')
    if len(c)<T+TAIL: c=np.pad(c,(0,T+TAIL-len(c)))
    return c[:T+TAIL]

def grouped(m,g,tcell,tven):
    ng=N//g; counts=m.reshape(T,ng,g).sum(axis=2); k=kernel(tcell)
    inflow=np.zeros((T+TAIL,ng))
    for j in range(ng):
        z=np.convolve(counts[:,j],k,mode='full'); inflow[:min(len(z),T+TAIL),j]=z[:T+TAIL]
    a=1-math.exp(-1/tven); v=np.zeros(ng); artery=np.zeros(T+TAIL); peak_v=0.; peak_group_out=0.
    for t in range(T+TAIL):
        v+=inflow[t]; y=a*v; v-=y; artery[t]=y.sum()
        peak_v=max(peak_v,float(v.max())); peak_group_out=max(peak_group_out,float(y.max()))
    return artery,peak_v,peak_group_out

def reservoir(counts,inflow):
    rate=counts.mean()*BATTERY_RATE_FACTOR; q=peak=battery=0.
    for x in inflow:
        q+=x; y=min(q,rate); q-=y; battery+=y; peak=max(peak,q)
    return dict(peak_artery_inflow=float(inflow.max()),peak_reservoir_units=float(peak),transferred_fraction=float(battery/counts.sum()),battery_rate=float(rate))

rows=[]
for si,s in enumerate(SCENARIOS):
    m=matrix(s,130+si); counts=m.sum(axis=1); b=reservoir(counts,direct(counts,8))
    for tc in CELL_TAUS:
      for tv in VENULE_TAUS:
       for g in GROUPS:
        inflow,pv,pgo=grouped(m,g,tc,tv); r=reservoir(counts,inflow)
        rows.append(dict(scenario=s,group_cells=g,cell_to_venule_tau=tc,venule_to_artery_tau=tv,
          slow_venule_outlets=N//g,slow_outlet_copy_reduction_pct=100*(1-(N//g)/N),
          cell_charge_remaining_after_8_intervals_pct=100*math.exp(-8/tc),
          peak_local_venule_charge_units=pv,peak_one_group_artery_output=pgo,
          peak_artery_inflow=r['peak_artery_inflow'],peak_reservoir_units=r['peak_reservoir_units'],
          transferred_fraction=r['transferred_fraction'],
          artery_peak_reduction_vs_direct_tau8_pct=100*(1-r['peak_artery_inflow']/b['peak_artery_inflow']),
          reservoir_peak_reduction_vs_direct_tau8_pct=100*(1-r['peak_reservoir_units']/b['peak_reservoir_units'])))

out=Path(__file__).resolve().parents[1]/'results'; out.mkdir(exist_ok=True)
df=pd.DataFrame(rows); df.to_csv(out/'venule_sweep.csv',index=False)
sel=df[(df.group_cells==8)&(df.cell_to_venule_tau==2)&(df.venule_to_artery_tau==8)].copy()
sel.to_csv(out/'selected_group8_tau2_tau8.csv',index=False)
burden=df[(df.cell_to_venule_tau==2)&(df.venule_to_artery_tau==8)][['scenario','group_cells','slow_outlet_copy_reduction_pct','peak_local_venule_charge_units']]
burden.to_csv(out/'group_size_burden.csv',index=False)
print(sel[['scenario','artery_peak_reduction_vs_direct_tau8_pct','reservoir_peak_reduction_vs_direct_tau8_pct','cell_charge_remaining_after_8_intervals_pct','slow_outlet_copy_reduction_pct','peak_local_venule_charge_units','transferred_fraction']].to_string(index=False))
