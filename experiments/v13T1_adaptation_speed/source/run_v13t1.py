#!/usr/bin/env python3
from pathlib import Path
import numpy as np, pandas as pd
BASE=np.array([12.,10.,8.,8.,2.])
PH=[np.array([.78,.78,.78,.78,.75]),np.array([1.28,.65,.65,.72,.70]),np.array([.68,1.30,.66,.72,.72]),np.array([.70,.70,1.34,.74,.72]),np.array([.68,.68,.68,1.32,.78]),np.array([.72,.70,.70,.74,2.15]),np.array([.85,.82,.80,.88,1.20])]

def run(seed,policy,dur):
    rng=np.random.default_rng(seed); dem=[]
    for mult in PH*3:
        for _ in range(dur): dem.append(rng.poisson(BASE*mult*(1+.2*(rng.random()<.06))))
    dem=np.asarray(dem,float); T=len(dem); rf=np.random.default_rng(seed+999); surv=np.array([rf.binomial(int(x),.9) for x in BASE],float)
    rr=[0,1,2,3]; off=np.zeros(4,int); dwell=np.zeros(4,int); pressure=np.zeros(5); fatigue=np.zeros((4,5)); q=np.zeros(5)
    backlog=maxq=completed=switches=0.
    for t,d in enumerate(dem):
        live=BASE if t<T//2 else surv; add=np.zeros(5)
        for i,r in enumerate(rr):
            if off[i]>0: off[i]-=1
            else:add[r]+=1
            dwell[i]+=1
        q+=d; done=np.minimum(q,live+add); q-=done; completed+=done.sum(); backlog+=q.sum(); maxq=max(maxq,q.sum())
        if policy=='instant':
            tmp=q/(BASE+1e-9); new=[]
            for _ in range(4): nr=int(np.argmax(tmp)); new.append(nr); tmp[nr]*=.65
            for i,nr in enumerate(new):
                if nr!=rr[i]: rr[i]=nr; switches+=1; off[i]=1; dwell[i]=0
        elif policy=='single':
            pressure=.94*pressure+.06*(q/(BASE+1e-9)); fatigue*=.97
            if t%4==3:
                for i in range(4):
                    cur=rr[i]; score=pressure-.12*fatigue[i]; nr=int(np.argmax(score))
                    if nr!=cur and dwell[i]>=12 and score[nr]-score[cur]>.14 and pressure[nr]>.12:
                        rr[i]=nr; switches+=1; off[i]=1; dwell[i]=0; fatigue[i,nr]+=1
        elif policy=='dual':
            pressure=.90*pressure+.10*(q/(BASE+1e-9)); fatigue*=.96
            for i in range(4):
                period=2 if i<2 else 4; mind=4 if i<2 else 16; margin=.10 if i<2 else .16
                if (t+1)%period: continue
                cur=rr[i]; score=pressure-.15*fatigue[i]; nr=int(np.argmax(score))
                if nr!=cur and dwell[i]>=mind and score[nr]-score[cur]>margin and pressure[nr]>.10:
                    rr[i]=nr; switches+=1; off[i]=1; dwell[i]=0; fatigue[i,nr]+=1.2 if i<2 else .8
    return backlog,maxq,switches,completed
rows=[]
for dur in (4,8,16,32,64,120):
    for seed in range(50,100):
        for p in ('instant','single','dual'):
            b,m,s,c=run(seed,p,dur); rows.append((dur,p,b,m,s,c))
df=pd.DataFrame(rows,columns=['phase_duration','policy','backlog','max_queue','switches','completed']); out=Path(__file__).resolve().parents[1]/'results'; out.mkdir(exist_ok=True)
s=df.groupby(['phase_duration','policy']).agg(mean_backlog=('backlog','mean'),mean_max_queue=('max_queue','mean'),mean_switches=('switches','mean'),mean_completed=('completed','mean')).reset_index(); s.to_csv(out/'speed_sweep.csv',index=False); print(s.to_string(index=False))
