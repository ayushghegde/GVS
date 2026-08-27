#!/usr/bin/env python3
from pathlib import Path
import numpy as np, pandas as pd

ROLES=['grammar','template','binding','constraint','exact']
BASE=np.array([12,10,8,8,2],dtype=int)
N_GENERAL=4
PHASES=[
 ('mixed',np.array([10.5,8.5,6.8,6.8,1.8])),
 ('grammar_heavy',np.array([16.0,7.5,6.0,6.5,1.8])),
 ('template_heavy',np.array([8.5,15.0,6.2,6.5,1.8])),
 ('binding_heavy',np.array([9.0,7.5,13.0,6.5,1.8])),
 ('constraint_heavy',np.array([9.0,7.0,6.0,14.5,1.8])),
 ('exact_burst',np.array([8.0,6.5,5.5,6.0,6.5])),
 ('mixed_return',np.array([10.5,8.5,6.8,6.8,1.8])),
]
PHASE_LEN=120
T=PHASE_LEN*len(PHASES)
SEED=1300
rng=np.random.default_rng(SEED)
ARR=np.vstack([rng.poisson(lam,size=(PHASE_LEN,len(ROLES))) for _,lam in PHASES])
PHASE_NAME=sum([[name]*PHASE_LEN for name,_ in PHASES],[])

def simulate(policy, failures=None, fail_epoch=None, switch_cost=2, hysteresis=.8, alpha=.2):
    q=np.zeros(len(ROLES),float)
    base=BASE.astype(float).copy()
    assign=np.array([0,1,2,3],dtype=int)
    cooldown=np.zeros(N_GENERAL,dtype=int)
    ema=np.zeros(len(ROLES),float)
    total_backlog=0.; maxq=0.; served=0.; switches=0; pressure_pulses=0
    rows=[]
    for t in range(T):
        if fail_epoch is not None and t==fail_epoch:
            base-=np.asarray(failures,dtype=float)
        q+=ARR[t]
        pressure=q/(base+1)
        if policy=='role_pressure': pressure_pulses += int(np.sum(pressure>1.0))
        ema=(1-alpha)*ema + alpha*pressure
        if policy=='oracle':
            temp=np.maximum(q-base,0); new=[]
            for _ in range(N_GENERAL):
                i=int(np.argmax(temp)); new.append(i); temp[i]=max(0,temp[i]-1)
            assign=np.array(new,dtype=int)
        elif policy=='role_pressure':
            for j in range(N_GENERAL):
                if cooldown[j]>0:
                    cooldown[j]-=1; continue
                cur=assign[j]; best=int(np.argmax(ema))
                if best!=cur and ema[best] > ema[cur]+hysteresis:
                    assign[j]=best; cooldown[j]=switch_cost; switches+=1
        elif policy!='fixed': raise ValueError(policy)
        cap=base.copy()
        for j,a in enumerate(assign):
            if policy=='role_pressure' and cooldown[j]>0: continue
            cap[a]+=1
        done=np.minimum(q,cap); q-=done; served+=done.sum()
        total_backlog+=q.sum(); maxq=max(maxq,q.sum())
        rows.append(dict(epoch=t,phase=PHASE_NAME[t],policy=policy,total_queue=float(q.sum()),reserve_roles=';'.join(ROLES[i] for i in assign)))
    return dict(policy=policy,total_backlog_area=float(total_backlog),max_total_queue=float(maxq),ending_queue=float(q.sum()),served=float(served),reserve_role_changes=int(switches),role_pressure_pulses=int(pressure_pulses)),pd.DataFrame(rows)

summary=[]; traces=[]
for policy in ['fixed','role_pressure','oracle']:
    s,tr=simulate(policy); summary.append(s); traces.append(tr)
rr=np.random.default_rng(99)
cell_roles=np.repeat(np.arange(len(ROLES)),BASE)
failed_idx=rr.choice(len(cell_roles),size=round(len(cell_roles)*.10),replace=False)
failures=np.zeros(len(ROLES),dtype=int)
for i in failed_idx: failures[cell_roles[i]]+=1
failure_rows=[]
for policy in ['fixed','role_pressure','oracle']:
    s,_=simulate(policy,failures=failures,fail_epoch=T//2)
    s.update({f'failed_{r}_cells':int(failures[i]) for i,r in enumerate(ROLES)})
    failure_rows.append(s)
out=Path(__file__).resolve().parents[1]/'results'; out.mkdir(exist_ok=True)
pd.DataFrame(summary).to_csv(out/'adaptation_summary.csv',index=False)
pd.DataFrame(failure_rows).to_csv(out/'failure_adaptation.csv',index=False)
trace=pd.concat(traces,ignore_index=True)
trace.groupby(['policy','phase'],sort=False)['total_queue'].agg(['mean','max']).reset_index().to_csv(out/'phase_queue_summary.csv',index=False)
sdf=pd.DataFrame(summary).set_index('policy'); rpf=sdf.loc['role_pressure']; fixed=sdf.loc['fixed']; oracle=sdf.loc['oracle']
print('role-pressure backlog reduction vs fixed %',100*(1-rpf.total_backlog_area/fixed.total_backlog_area))
print('role-pressure max-queue reduction vs fixed %',100*(1-rpf.max_total_queue/fixed.max_total_queue))
print('role-pressure backlog above oracle %',100*(rpf.total_backlog_area/oracle.total_backlog_area-1))
print('role changes',int(rpf.reserve_role_changes),'over',T,'epochs')
support_fj=float(rpf.role_pressure_pulses)*N_GENERAL*0.67
pd.DataFrame([dict(role_pressure_pulses=int(rpf.role_pressure_pulses),fanout_taps_per_pulse=N_GENERAL,event_proxy_fJ_per_tap=0.67,total_support_proxy_fJ=support_fj,support_proxy_fJ_per_completed_operation=support_fj/float(rpf.served))]).to_csv(out/'role_pressure_support_proxy.csv',index=False)
print('RPF support proxy fJ/completed operation',support_fj/float(rpf.served))
fdf=pd.DataFrame(failure_rows).set_index('policy')
print('failure-case backlog reduction vs fixed %',100*(1-fdf.loc['role_pressure'].total_backlog_area/fdf.loc['fixed'].total_backlog_area))
print('failure vector',dict(zip(ROLES,failures.tolist())))
