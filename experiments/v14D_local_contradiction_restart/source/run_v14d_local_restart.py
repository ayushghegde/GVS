#!/usr/bin/env python3
from __future__ import annotations
from collections import deque
from dataclasses import dataclass
from pathlib import Path
import itertools
import numpy as np
import pandas as pd

SEEDS=range(1300,1400); T=120; DEAD=20; MODULE_COPIES=64

@dataclass(frozen=True)
class Config:
    policy:str
    pressure_threshold:int=15
    restart_after:int=2
    hard_retrap:float=0.04
    easy_retrap:float=0.015
    hard_max_rounds:int=8
    easy_max_rounds:int=6

def run(seed:int,cfg:Config):
    rng=np.random.default_rng(seed); q=deque(); info={}; done=[]; tid=0
    attempts=local_restarts=whole_restarts=0; disturbed=0.0
    failcap=rng.binomial(8,.9)+1
    for t in range(T+400):
        if t<T:
            arrivals=rng.poisson(6*(1.4 if rng.random()<.08 else 1.0))
            for _ in range(arrivals):
                hard=rng.random()<.35; ncl=int(rng.integers(3,6) if hard else rng.integers(2,4)); trap=.08 if hard else .032
                info[tid]={'at':t,'hard':hard,'ncl':ncl,'trapped':rng.random(ncl)<trap,'progress':np.zeros(ncl,bool),'tries':np.zeros(ncl,int),'psolve':.52 if hard else .68,'rounds':0,'whole_restarts':0}
                q.append(tid); tid+=1
        base=9 if t<T//2 else failcap; phase=t%(T//2); cap=base+(0 if phase<4 else (2 if phase<16 else 5)); backlog=len(q)
        for x in [q.popleft() for _ in range(min(cap,len(q)))]:
            z=info[x]; z['rounds']+=1
            for j in np.where(~z['progress'])[0]:
                z['tries'][j]+=1; attempts+=1
                if not z['trapped'][j] and rng.random()<z['psolve']: z['progress'][j]=True
            if z['progress'].all(): done.append((x,z['at'],t)); continue
            if cfg.policy=='fixed4': allowed=4
            elif cfg.policy=='pressure': allowed=4 if backlog>=cfg.pressure_threshold else (cfg.hard_max_rounds if z['hard'] else cfg.easy_max_rounds)
            elif cfg.policy=='whole_restart':
                if z['rounds'] in (cfg.restart_after+1,2*cfg.restart_after+3) and z['whole_restarts']<2:
                    whole_restarts+=1; disturbed+=z['ncl']; z['progress'][:]=False; z['trapped']=rng.random(z['ncl'])<(.08 if z['hard'] else .032); z['tries'][:]=0; z['whole_restarts']+=1
                allowed=10
            elif cfg.policy=='local_restart':
                for j in np.where(~z['progress'])[0]:
                    if z['tries'][j]>=cfg.restart_after:
                        local_restarts+=1; disturbed+=1.0; z['trapped'][j]=rng.random()<(cfg.hard_retrap if z['hard'] else cfg.easy_retrap); z['tries'][j]=0
                allowed=4 if backlog>=cfg.pressure_threshold else (cfg.hard_max_rounds if z['hard'] else cfg.easy_max_rounds)
            else: raise ValueError(cfg.policy)
            if z['rounds']<allowed and t-z['at']<100: q.append(x)
        if t>=T and not q: break
    lat=np.array([ct-at+1 for _,at,ct in done],float)
    return dict(seed=seed,policy=cfg.policy,pressure_threshold=cfg.pressure_threshold,restart_after=cfg.restart_after,hard_retrap=cfg.hard_retrap,easy_retrap=cfg.easy_retrap,hard_max_rounds=cfg.hard_max_rounds,easy_max_rounds=cfg.easy_max_rounds,total=tid,resolved=len(done)/tid,ontime=(lat<=DEAD).sum()/tid,p95=np.quantile(lat,.95),meanlat=lat.mean(),attempts=attempts/tid,local_restarts=local_restarts/tid,whole_restarts=whole_restarts/tid,disturbed_state=disturbed/tid,ontime_per_module=((lat<=DEAD).sum()/tid)/MODULE_COPIES)

def summarize(df):
    keys=['policy','pressure_threshold','restart_after','hard_retrap','easy_retrap','hard_max_rounds','easy_max_rounds']
    return df.groupby(keys).agg(resolved=('resolved','mean'),ontime=('ontime','mean'),p95=('p95','mean'),meanlat=('meanlat','mean'),attempts=('attempts','mean'),local_restarts=('local_restarts','mean'),whole_restarts=('whole_restarts','mean'),disturbed_state=('disturbed_state','mean'),ontime_per_module=('ontime_per_module','mean')).reset_index()

configs=[Config('fixed4'),Config('pressure',pressure_threshold=15),Config('whole_restart',restart_after=2)]
for trigger,threshold,retrap_h in itertools.product([2,3],[10,15,20],[.02,.04,.06,.08]):
    configs.append(Config('local_restart',pressure_threshold=threshold,restart_after=trigger,hard_retrap=retrap_h,easy_retrap=max(.005,retrap_h*.375)))
rows=[run(seed,cfg) for cfg in configs for seed in SEEDS]
raw=pd.DataFrame(rows); summary=summarize(raw)
whole=summary.loc[summary.policy.eq('whole_restart'),'resolved'].iloc[0]; lcr=summary[summary.policy.eq('local_restart')].copy(); eligible=lcr[(lcr.resolved>=whole-.03)&(lcr.disturbed_state<=1.0)]
selected=(eligible if len(eligible) else lcr).sort_values(['ontime','resolved'],ascending=False).iloc[0]
summary['selected']=False
mask=np.ones(len(summary),bool)
for col in ['policy','pressure_threshold','restart_after','hard_retrap','easy_retrap','hard_max_rounds','easy_max_rounds']: mask &= summary[col].eq(selected[col])
summary.loc[mask,'selected']=True
out=Path(__file__).resolve().parents[1]/'results'; out.mkdir(exist_ok=True)
summary.to_csv(out/'local_restart_sweep.csv',index=False)
cmp=pd.concat([summary[summary.policy.isin(['fixed4','pressure','whole_restart'])],summary[summary.selected]],ignore_index=True); cmp.to_csv(out/'selected_comparison.csv',index=False)
print(cmp[['policy','resolved','ontime','p95','meanlat','attempts','disturbed_state','selected']].to_string(index=False))
