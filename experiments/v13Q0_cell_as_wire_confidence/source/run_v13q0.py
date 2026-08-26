#!/usr/bin/env python3
import csv, math
import numpy as np
from pathlib import Path

OUT=Path(__file__).resolve().parents[1]/'results'
OUT.mkdir(exist_ok=True)

# Q0A: cell-as-wire 3-D contact geometry. A cube cell has 6 face, 12 edge and
# 8 vertex candidate contacts, but only selected contacts conduct per event.
rng=np.random.default_rng(20260826)
dims=(16,16,4); N=100000
a=np.column_stack([rng.integers(0,d,size=N) for d in dims])
b=np.column_stack([rng.integers(0,d,size=N) for d in dims])
d=np.abs(a-b); man=d.sum(axis=1); mask=man>0; d=d[mask]; man=man[mask]
s=np.sort(d,axis=1); vertex=s[:,0]; edge=s[:,1]-s[:,0]; face=s[:,2]-s[:,1]; cheb=d.max(axis=1)
route=[]
for ef,vf in [(1.25,1.5),(1.5,2.0),(2.0,3.0)]:
    base=man*0.15
    embodied=(face+ef*edge+vf*vertex)*0.15
    route.append({'edge_contact_cost_x_face':ef,'vertex_contact_cost_x_face':vf,
                  'mean_face_only_hops':float(man.mean()),'mean_embodied_hops':float(cheb.mean()),
                  'hop_reduction_percent':float(100*(1-cheb.mean()/man.mean())),
                  'mean_face_only_energy_fj':float(base.mean()),'mean_embodied_energy_fj':float(embodied.mean()),
                  'energy_reduction_percent':float(100*(1-embodied.mean()/base.mean()))})
with (OUT/'routing.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=route[0]); w.writeheader(); w.writerows(route)

# Q0B: neuron-inspired population confidence. Multiple cheap cells encode each
# candidate; recurrent evidence is accumulated until winner-vs-runner-up margin
# crosses a physical confidence threshold. Low margin means keep settling.
rng=np.random.default_rng(314159)
def consensus(mu,sigma=1.0,pop=16,choices=4,trials=20000,threshold=3.0,max_steps=64):
    correct=wrong=unresolved=0; steps=[]
    for _ in range(trials):
        y=int(rng.integers(choices)); acc=np.zeros(choices); decided=False
        for t in range(1,max_steps+1):
            inc=rng.normal(0,sigma/np.sqrt(pop),size=choices); inc[y]+=mu; acc+=inc
            order=np.argsort(acc); margin=acc[order[-1]]-acc[order[-2]]
            if margin>=threshold:
                pred=int(order[-1]); decided=True; steps.append(t)
                if pred==y: correct+=1
                else: wrong+=1
                break
        if not decided: unresolved+=1
    return {'evidence_drift':mu,'correct_fraction':correct/trials,'wrong_robust_fraction':wrong/trials,
            'still_uncertain_fraction':unresolved/trials,'mean_steps_if_decided':float(np.mean(steps))}
cons=[consensus(mu) for mu in [0.08,0.12,0.18,0.25]]
with (OUT/'population_confidence.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=cons[0]); w.writeheader(); w.writerows(cons)

# Q0C: local quorum relay. A cell is itself the relay; it fires only when a
# selected set of neighbouring cell contacts agree strongly enough. No global
# router is involved. Uncertain hops retry locally while the prior state holds.
rng=np.random.default_rng(12345)
def quorum_hop(bit,supporters,p,margin_req,retries):
    for r in range(1,retries+1):
        errs=rng.random(supporters)<p; votes=np.where(errs,1-bit,bit)
        ones=int(votes.sum()); zeros=supporters-ones
        if abs(ones-zeros)>=margin_req:
            return (1 if ones>zeros else 0),r,True
    return bit,retries,False

def chain(supporters,p=.1,margin_req=3,retries=4,trials=20000,hops=16):
    wrong=stalled=total=0
    for _ in range(trials):
        b0=int(rng.integers(2)); b=b0; okall=True
        for _ in range(hops):
            b,r,ok=quorum_hop(b,supporters,p,margin_req,retries); total+=r
            if not ok: stalled+=1; okall=False; break
        if okall and b!=b0: wrong+=1
    return {'supporting_contacts':supporters,'contact_error_probability':p,'confidence_margin_votes':margin_req,
            'wrong_end_to_end_fraction':wrong/trials,'stalled_fraction':stalled/trials,
            'mean_local_attempts_per_planned_hop':total/(trials*hops)}
q=[]
for supporters in [1,3,5,7,9]:
    q.append(chain(supporters,margin_req=(1 if supporters<=3 else 3)))
with (OUT/'quorum_relay.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=q[0]); w.writeheader(); w.writerows(q)
print(OUT)
