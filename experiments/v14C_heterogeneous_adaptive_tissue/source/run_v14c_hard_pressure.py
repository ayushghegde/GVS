#!/usr/bin/env python3
from collections import deque
from pathlib import Path
import numpy as np,pandas as pd
P={'96':.5,'128':1/6};T=120;DEAD=20

def run(seed,threshold):
 rng=np.random.default_rng(seed);q=deque();info={};done=[];tid=0;attempts=0;failcap=rng.binomial(8,.9)+1
 for t in range(T+350):
  if t<T:
   n=rng.poisson(6*(1.4 if rng.random()<.08 else 1))
   for _ in range(n):
    d='128' if rng.random()<.35 else '96';info[tid]=[d,t,0];q.append(tid);tid+=1
  base=9 if t<T//2 else failcap;phase=t%(T//2);cap=base+(0 if phase<4 else (2 if phase<16 else 5));backlog=len(q);batch=[q.popleft() for _ in range(min(cap,len(q)))]
  for x in batch:
   d,at,k=info[x];k+=1;attempts+=1
   if rng.random()<P[d]:done.append((x,d,at,t,k));continue
   maxdeep=6 if d=='96' else 16;allowed=4 if backlog>=threshold else maxdeep
   if k<allowed and t-at<100:info[x][2]=k;q.append(x)
  if t>=T and not q:break
 l=np.array([ct-at+1 for _,_,at,ct,_ in done]);return dict(seed=seed,threshold=threshold,total=tid,resolved=len(done)/tid,ontime=(l<=DEAD).sum()/tid,p95=np.quantile(l,.95),meanlat=l.mean(),attempts=attempts/tid)

rows=[run(seed,th) for th in (0,15,20,25,30) for seed in range(1300,1400)];df=pd.DataFrame(rows);s=df.groupby('threshold').agg(resolved=('resolved','mean'),ontime=('ontime','mean'),p95=('p95','mean'),meanlat=('meanlat','mean'),attempts=('attempts','mean')).reset_index();s['ontime_per_module']=s.ontime/64;print(s.to_string(index=False));out=Path(__file__).resolve().parents[1]/'results';out.mkdir(exist_ok=True);s.to_csv(out/'hard_pressure.csv',index=False)
