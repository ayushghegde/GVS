#!/usr/bin/env python3
from collections import deque
from pathlib import Path
import numpy as np, pandas as pd
ROLES=['grammar','template','binding','constraint','exact']; BASE=np.array([12,10,8,8,2],dtype=int)
TASKS={'association':[0,1],'relation':[0,2,0],'constraint':[0,2,3,3],'exact':[0,2,4],'mixed':[0,1,2,3,4]}
PHASES=[('balanced',np.array([2.5,2.5,2.0,1.5,1.0])),('relation_heavy',np.array([2.0,5.0,1.0,1.0,1.0])),('template_heavy',np.array([5.0,1.5,1.0,1.0,0.5])),('binding_heavy',np.array([1.0,3.0,3.0,2.0,1.0])),('constraint_heavy',np.array([1.0,1.0,5.0,1.0,1.0])),('exact_heavy',np.array([1.0,1.0,1.0,5.0,1.0])),('mixed',np.array([2.0,2.0,2.0,2.0,2.0]))]
DUR=120; DEADLINE=20; END=len(PHASES)*DUR

def arrivals(seed):
 rng=np.random.default_rng(seed);seq=[];tid=0
 for _,rates in PHASES:
  for _ in range(DUR):
   mult=1.2 if rng.random()<.06 else 1.0;items=[]
   for typ,lam in zip(TASKS,rates):
    for _ in range(rng.poisson(lam*mult)):items.append((tid,typ));tid+=1
   rng.shuffle(items);seq.append(items)
 return seq,tid

def sim(seed,surv=.9,lean=(3,4)):
 arr,total=arrivals(seed);rng=np.random.default_rng(seed+999);q=[deque() for _ in ROLES];info={};comp=[];allowed=[tuple(range(5))]*4+[tuple(lean)]*2
 rr=[0,1,2,3,lean[0],lean[-1]];off=np.zeros(6,int);dwell=np.zeros(6,int);pressure=np.zeros(5);fatigue=np.zeros((6,5));switches=0;backlog_area=0
 livefail=np.array([rng.binomial(int(x),surv) for x in BASE],int)
 for t in range(END+700):
  if t<END:
   for tid,typ in arr[t]:info[tid]=[typ,0,t];q[TASKS[typ][0]].append(tid)
  live=livefail.copy() if t>=END//2 else BASE.copy();add=np.zeros(5,int)
  for i,r in enumerate(rr):
   if off[i]>0:off[i]-=1
   else:add[r]+=1
   dwell[i]+=1
  served=[]
  for r,c in enumerate(live+add):
   for _ in range(min(int(c),len(q[r]))):served.append((r,q[r].popleft()))
  for _,tid in served:
   typ,idx,at=info[tid];idx+=1
   if idx>=len(TASKS[typ]):comp.append((tid,at,t))
   else:info[tid][1]=idx;q[TASKS[typ][idx]].append(tid)
  norm=np.array([len(x) for x in q],float)/(BASE+1e-9);pressure=.90*pressure+.10*norm;fatigue*=.96;cand=[]
  for i in range(6):
   fast=i<3;period=2 if fast else 4;mind=4 if fast else 16;margin=.10 if fast else .16
   if (t+1)%period:continue
   cur=rr[i];score=pressure-.15*fatigue[i];nr=max(allowed[i],key=lambda j:score[j]);gain=score[nr]-score[cur]
   if nr!=cur and dwell[i]>=mind and gain>margin and pressure[nr]>.10:cand.append((gain,i,nr,fast))
  if cand:
   _,i,nr,fast=max(cand);rr[i]=nr;switches+=1;off[i]=1;dwell[i]=0;fatigue[i,nr]+=1.2 if fast else .8
  b=sum(len(x) for x in q)
  if t<END:backlog_area+=b
  if t>=END and b==0:break
 l=np.array([ct-at+1 for _,at,ct in comp]);modules=40+20+2*len(lean)
 return dict(seed=seed,survival=surv,lean='-'.join(map(str,lean)),complete=len(comp)/total,ontime=(l<=DEADLINE).sum()/total,p95=np.quantile(l,.95),meanlat=l.mean(),backlog=backlog_area,drain=max(0,t-END+1),switches=switches,modules=modules,eff=((l<=DEADLINE).sum()/total)/modules)

rows=[]
for surv in (1.0,.9,.8,.7):
 for lean in ((4,),(3,4),(2,3,4),(1,3,4)):
  for seed in range(700,750):rows.append(sim(seed,surv,lean))
df=pd.DataFrame(rows);s=df.groupby(['survival','lean']).agg(complete=('complete','mean'),ontime=('ontime','mean'),p95=('p95','mean'),meanlat=('meanlat','mean'),backlog=('backlog','mean'),drain=('drain','mean'),switches=('switches','mean'),modules=('modules','mean'),eff=('eff','mean')).reset_index();print(s.to_string(index=False));out=Path(__file__).resolve().parents[1]/'results';out.mkdir(exist_ok=True);s.to_csv(out/'reserve_diff.csv',index=False)
