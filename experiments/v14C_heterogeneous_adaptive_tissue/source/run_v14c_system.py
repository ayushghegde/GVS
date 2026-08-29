#!/usr/bin/env python3
from collections import deque
from pathlib import Path
import numpy as np, pandas as pd
ROLES=['grammar','template','binding','constraint','exact']
BASE=np.array([12,10,8,8,2],dtype=int)
TASKS={'association':[0,1],'relation':[0,2,0],'constraint':[0,2,3,3],'exact':[0,2,4],'mixed':[0,1,2,3,4]}
PHASES=[('balanced',np.array([2.5,2.5,2.0,1.5,1.0])),('relation_heavy',np.array([2.0,5.0,1.0,1.0,1.0])),('template_heavy',np.array([5.0,1.5,1.0,1.0,0.5])),('binding_heavy',np.array([1.0,3.0,3.0,2.0,1.0])),('constraint_heavy',np.array([1.0,1.0,5.0,1.0,1.0])),('exact_heavy',np.array([1.0,1.0,1.0,5.0,1.0])),('mixed',np.array([2.0,2.0,2.0,2.0,2.0]))]
DUR=120; DEADLINE=20

def arrivals(seed):
 rng=np.random.default_rng(seed); seq=[]; tid=0
 for _,rates in PHASES:
  for _ in range(DUR):
   mult=1.2 if rng.random()<.06 else 1.0; items=[]
   for typ,lam in zip(TASKS,rates):
    for _ in range(rng.poisson(lam*mult)): items.append((tid,typ)); tid+=1
   rng.shuffle(items); seq.append(items)
 return seq,tid

def simulate(seed,arch):
 arr,total=arrivals(seed); rng=np.random.default_rng(seed+999); q=[deque() for _ in ROLES]; info={}; completed=[]; transitions=0
 rr=[0,1,2,3]; off=np.zeros(4,int); dwell=np.zeros(4,int); pressure=np.zeros(5); fatigue=np.zeros((4,5)); switches=maxsim=max_backlog=backlog_area=0
 surv=np.array([rng.binomial(int(x),.9) for x in BASE],dtype=int); universal_surv=rng.binomial(44,.9); arrival_end=len(arr)
 for t in range(arrival_end+700):
  if t<arrival_end:
   for tid,typ in arr[t]: info[tid]=[typ,0,t]; q[TASKS[typ][0]].append(tid)
  failed=t>=arrival_end//2
  if arch=='universal':
   cap=universal_surv if failed else 44; served=[]; qlens=np.array([len(x) for x in q],float)
   for _ in range(cap):
    if qlens.max()<=0: break
    r=int(np.argmax(qlens)); tid=q[r].popleft(); qlens[r]-=1; served.append((r,tid))
  else:
   live=surv.copy() if failed else BASE.copy(); add=np.zeros(5,int)
   for i,r in enumerate(rr):
    if off[i]>0: off[i]-=1
    else: add[r]+=1
    dwell[i]+=1
   served=[]
   for r,c in enumerate(live+add):
    for _ in range(min(int(c),len(q[r]))): served.append((r,q[r].popleft()))
  for r,tid in served:
   typ,idx,at=info[tid]; idx+=1
   if idx>=len(TASKS[typ]): completed.append((tid,typ,at,t))
   else: info[tid][1]=idx; q[TASKS[typ][idx]].append(tid); transitions+=1
  nsw=0
  if arch=='adaptive':
   norm=np.array([len(x) for x in q],float)/(BASE+1e-9); pressure=.90*pressure+.10*norm; fatigue*=.96; candidates=[]
   for i in range(4):
    period=2 if i<2 else 4; mind=4 if i<2 else 16; margin=.10 if i<2 else .16
    if (t+1)%period: continue
    cur=rr[i]; score=pressure-.15*fatigue[i]; nr=int(np.argmax(score)); gain=score[nr]-score[cur]
    if nr!=cur and dwell[i]>=mind and gain>margin and pressure[nr]>.10: candidates.append((gain,i,nr))
   if candidates:
    _,i,nr=max(candidates); rr[i]=nr; switches+=1; nsw=1; off[i]=1; dwell[i]=0; fatigue[i,nr]+=1.2 if i<2 else .8
  maxsim=max(maxsim,nsw); backlog=sum(len(x) for x in q); max_backlog=max(max_backlog,backlog)
  if t<arrival_end: backlog_area+=backlog
  if t>=arrival_end and backlog==0: break
 lats=np.array([ct-at+1 for _,_,at,ct in completed]); ontime=int((lats<=DEADLINE).sum()); completed_by_end=sum(1 for _,_,at,ct in completed if ct<arrival_end)
 module_copies=320 if arch=='universal' else 60; support_mim=32 if arch=='adaptive' else 0; support_mos=72 if arch=='adaptive' else 0
 pressure_fJ=switches*0.5*61.88; support_event_fJ=len(completed)*0.156 if arch=='adaptive' else 0.0; comm_fJ=transitions*0.15
 return dict(seed=seed,arch=arch,total=total,completed=len(completed),completed_by_end=completed_by_end,ontime=ontime,ontime_frac=ontime/total,mean_latency=float(lats.mean()),p95_latency=float(np.quantile(lats,.95)),max_backlog=max_backlog,backlog_area=backlog_area,drain_epochs=max(0,t-arrival_end+1),switches=switches,maxsim=maxsim,module_copies=module_copies,support_mim=support_mim,support_mos=support_mos,transitions=transitions,comm_fJ=comm_fJ,pressure_fJ=pressure_fJ,support_event_fJ=support_event_fJ)

rows=[simulate(seed,a) for seed in range(100,200) for a in ('universal','fixed','adaptive')]; df=pd.DataFrame(rows)
summary=df.groupby('arch').agg(total=('total','mean'),completed=('completed','mean'),completed_by_end=('completed_by_end','mean'),ontime_frac=('ontime_frac','mean'),mean_latency=('mean_latency','mean'),p95_latency=('p95_latency','mean'),max_backlog=('max_backlog','mean'),backlog_area=('backlog_area','mean'),drain_epochs=('drain_epochs','mean'),switches=('switches','mean'),module_copies=('module_copies','mean'),support_mim=('support_mim','mean'),support_mos=('support_mos','mean'),comm_fJ=('comm_fJ','mean'),pressure_fJ=('pressure_fJ','mean'),support_event_fJ=('support_event_fJ','mean')).reset_index()
summary['ontime_per_module']=summary.ontime_frac/summary.module_copies
fa=float(summary.loc[summary.arch=='fixed','ontime_frac'].iloc[0]); aa=float(summary.loc[summary.arch=='adaptive','ontime_frac'].iloc[0]); summary['adaptive_break_even_extra_module_equiv']=np.nan; summary.loc[summary.arch=='adaptive','adaptive_break_even_extra_module_equiv']=60*(aa/fa-1)
print(summary.to_string(index=False)); out=Path(__file__).resolve().parents[1]/'results'; out.mkdir(exist_ok=True); df.to_csv(out/'system_runs.csv',index=False); summary.to_csv(out/'system_summary.csv',index=False)
