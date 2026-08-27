#!/usr/bin/env python3
from pathlib import Path
import numpy as np, pandas as pd
BASE=np.array([12.,10.,8.,8.,2.])
PH=[np.array([.78,.78,.78,.78,.75]),np.array([1.28,.65,.65,.72,.70]),np.array([.68,1.30,.66,.72,.72]),np.array([.70,.70,1.34,.74,.72]),np.array([.68,.68,.68,1.32,.78]),np.array([.72,.70,.70,.74,2.15]),np.array([.85,.82,.80,.88,1.20])]
DUR=120

def run(seed,staggered):
    rng=np.random.default_rng(seed); dem=[]
    for mult in PH:
        for _ in range(DUR): dem.append(rng.poisson(BASE*mult*(1+.2*(rng.random()<.06))))
    dem=np.asarray(dem,float); T=len(dem); rf=np.random.default_rng(seed+999); surv=np.array([rf.binomial(int(x),.9) for x in BASE],float)
    rr=[0,1,2,3]; off=np.zeros(4,int); dwell=np.zeros(4,int); pressure=np.zeros(5); fatigue=np.zeros((4,5)); q=np.zeros(5)
    backlog=maxq=completed=switches=0.; maxsim=0
    for t,d in enumerate(dem):
        live=BASE if t<T//2 else surv; add=np.zeros(5)
        for i,r in enumerate(rr):
            if off[i]>0: off[i]-=1
            else:add[r]+=1
            dwell[i]+=1
        q+=d; done=np.minimum(q,live+add); q-=done; completed+=done.sum(); backlog+=q.sum(); maxq=max(maxq,q.sum())
        pressure=.90*pressure+.10*(q/(BASE+1e-9)); fatigue*=.96; candidates=[]
        for i in range(4):
            period=2 if i<2 else 4; mind=4 if i<2 else 16; margin=.10 if i<2 else .16
            if (t+1)%period: continue
            cur=rr[i]; score=pressure-.15*fatigue[i]; nr=int(np.argmax(score))
            if nr!=cur and dwell[i]>=mind and score[nr]-score[cur]>margin and pressure[nr]>.10: candidates.append((score[nr]-score[cur],i,nr))
        if staggered: candidates=sorted(candidates,reverse=True)[:1]
        n=0
        for _,i,nr in candidates:
            rr[i]=nr; switches+=1; n+=1; off[i]=1; dwell[i]=0; fatigue[i,nr]+=1.2 if i<2 else .8
        maxsim=max(maxsim,n)
    return backlog,maxq,switches,completed,maxsim
rows=[]
for seed in range(100,200):
    for stag in (False,True):
        b,m,s,c,ms=run(seed,stag); rows.append((seed,'break_before_make_wave' if stag else 'dual_unstaggered',b,m,s,c,ms))
df=pd.DataFrame(rows,columns=['seed','policy','backlog','max_queue','switches','completed','max_simultaneous_switches']); out=Path(__file__).resolve().parents[1]/'results'; out.mkdir(exist_ok=True)
s=df.groupby('policy').agg(mean_backlog=('backlog','mean'),mean_max_queue=('max_queue','mean'),mean_switches=('switches','mean'),mean_completed=('completed','mean'),mean_max_simultaneous_switches=('max_simultaneous_switches','mean')).reset_index(); s.to_csv(out/'handoff_summary.csv',index=False); print(s.to_string(index=False))
