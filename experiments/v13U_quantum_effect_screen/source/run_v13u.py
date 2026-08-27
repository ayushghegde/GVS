#!/usr/bin/env python3
from __future__ import annotations
import json, math
from pathlib import Path
import numpy as np

OUT=Path(__file__).resolve().parents[1]/'results'; OUT.mkdir(exist_ok=True)

technology_screen=[
 {'candidate':'MIM/MOS volatile state','fast_state':'KEEP','adaptive_role':'KEEP','persistent_morphology':'NO_RETENTION','current_gvs_process':True},
 {'candidate':'SKY130 SONOS flash','fast_state':'REJECT','adaptive_role':'REJECT','persistent_morphology':'KEEP_CONDITIONAL','current_gvs_process':'SPECIAL_TECH_OPTION'},
 {'candidate':'STT/SOT MRAM','fast_state':'FUTURE','adaptive_role':'FUTURE','persistent_morphology':'FUTURE','current_gvs_process':False},
 {'candidate':'coherent qubit memory','fast_state':'REJECT','adaptive_role':'REJECT','persistent_morphology':'REJECT','current_gvs_process':False},
 {'candidate':'single-electron/quantum-dot memory','fast_state':'REJECT_CURRENT','adaptive_role':'REJECT_CURRENT','persistent_morphology':'RESEARCH','current_gvs_process':False},
]

SEED=1310; EPOCHS=200000; NCELLS=4; NROLES=5; ENDURANCE=100000
V13T_CHANGES=121.5; V13T_EPOCHS=840
v13t_rate=V13T_CHANGES/(V13T_EPOCHS*NCELLS)
rng=np.random.default_rng(SEED)
lengths=np.array([4,8,16,32,64,120]); probs=np.array([.15,.20,.25,.20,.15,.05]); probs/=probs.sum()
roles=np.zeros((EPOCHS,NCELLS),dtype=np.int8); t=0; prev=rng.integers(NROLES,size=NCELLS)
while t<EPOCHS:
    L=int(rng.choice(lengths,p=probs)); cur=prev.copy()
    for j in rng.choice(NCELLS,size=int(rng.integers(2,5)),replace=False):
        opts=[r for r in range(NROLES) if r!=cur[j]]; cur[j]=int(rng.choice(opts))
    roles[t:min(EPOCHS,t+L)]=cur; prev=cur; t+=L
for i,j in zip(*np.where(rng.random((EPOCHS,NCELLS))<0.0005)):
    roles[i,j]=(roles[i,j]+1+int(rng.integers(NROLES-1)))%NROLES
raw_changes=int(np.sum(roles[1:]!=roles[:-1])); raw_rate=raw_changes/(EPOCHS*NCELLS)
def consolidate(window):
    nvm=np.full(NCELLS,-1,dtype=np.int8); cand=roles[0].copy(); stable=np.ones(NCELLS,dtype=int); writes=0; tr=np.empty_like(roles)
    for i in range(EPOCHS):
        if i:
            same=roles[i]==cand; stable[same]+=1; ch=~same; cand[ch]=roles[i,ch]; stable[ch]=1
        ready=(stable>=window)&(nvm!=cand); writes+=int(ready.sum()); nvm[ready]=cand[ready]; tr[i]=nvm
    valid=tr>=0; match=(tr==roles)&valid; wr=writes/(EPOCHS*NCELLS)
    return {'window_epochs':window,'writes':writes,'writes_per_cell_epoch':wr,'endurance_equiv_epochs':ENDURANCE/wr if wr else None,'live_role_match_fraction':float(match.sum()/valid.sum())},tr
consolidation=[]; traces={}
for w in [1,4,8,16,32,64,128,256]:
    r,tr=consolidate(w); consolidation.append(r); traces[w]=tr
base=consolidation[0]['writes']
for r in consolidation: r['write_reduction_pct']=100*(1-r['writes']/base)
cutrng=np.random.default_rng(SEED+1); cuts=cutrng.integers(1000,EPOCHS,size=20000)
powercut=[]
for w in [8,16,32,64,128,256]:
    tr=traces[w]; valid=tr[cuts]>=0; match=(tr[cuts]==roles[cuts])&valid
    powercut.append({'window_epochs':w,'restore_match_fraction':float(match.sum()/valid.sum()),'stale_fraction':float(1-match.sum()/valid.sum())})

I_ERASE_MIN=20e-6; I_ERASE_MAX=72e-6; I_PROG_MAX=2e-9; I_PROG_NOM=0.003e-9
ratio=I_ERASE_MIN/I_PROG_MAX; threshold=math.sqrt(I_ERASE_MIN*I_PROG_MAX)
rng2=np.random.default_rng(1311); N=1_000_000
prog=np.exp(rng2.uniform(np.log(max(I_PROG_NOM,1e-15)),np.log(I_PROG_MAX),N)); erase=np.exp(rng2.uniform(np.log(I_ERASE_MIN),np.log(I_ERASE_MAX),N))
sigma=np.log(10)/3
prog_m=prog*np.exp(rng2.normal(0,sigma,N)); erase_m=erase*np.exp(rng2.normal(0,sigma,N))
sonos_margin={'conservative_current_ratio':ratio,'threshold_A':threshold,'margin_above_programmed_max_x':threshold/I_PROG_MAX,'margin_below_erased_min_x':I_ERASE_MIN/threshold,'MC_samples':N,'MC_wrong_programmed_fraction':float(np.mean(prog_m>threshold)),'MC_wrong_erased_fraction':float(np.mean(erase_m<threshold))}

master=np.random.default_rng(1312)
def make_planted(n,ratio=4.2):
    sol=master.integers(0,2,n,dtype=np.int8); m=round(n*ratio); V=np.empty((m,3),dtype=np.int16); S=np.empty((m,3),dtype=np.int8)
    for i in range(m):
        v=master.choice(n,3,replace=False); s=master.integers(0,2,3,dtype=np.int8)
        if not np.any(np.where(s==1,sol[v],1-sol[v])): s[0]^=1
        V[i]=v; S[i]=s
    return V,S
def satvec(x,V,S): return np.any(np.where(S==1,x[V],1-x[V]),axis=1)
def solve(V,S,n,noise,rr,max_steps=700):
    x=rr.integers(0,2,n,dtype=np.int8)
    for step in range(max_steps):
        sv=satvec(x,V,S); uns=np.flatnonzero(~sv)
        if not len(uns): return True,step
        cand=V[int(rr.choice(uns))]
        if rr.random()<noise: j=int(rr.choice(cand))
        else:
            base=int(sv.sum()); scores=[]
            for jj in cand:
                j0=int(jj); x[j0]^=1; scores.append(int(satvec(x,V,S).sum())-base); x[j0]^=1
            mx=max(scores); j=int(rr.choice(cand[np.array(scores)==mx]))
        x[j]^=1
    return False,max_steps
stochastic=[]
for n in [64,96,128]:
    probs3=[make_planted(n) for _ in range(12)]
    for noise in [0,0.02,0.05,0.10,0.20]:
        okc=0; ss=0
        for pidx,(V,S) in enumerate(probs3):
            ok,st=solve(V,S,n,noise,np.random.default_rng(1312+n*1000+pidx*31+int(noise*1000))); okc+=ok; ss+=st
        stochastic.append({'variables':n,'noise_probability':noise,'success_fraction':okc/len(probs3),'mean_steps':ss/len(probs3)})

summary={
 'schema':'gvs-v13u-results-v1',
 'technology_screen':technology_screen,
 'v13t_measured_fast_persistence':{'role_changes':V13T_CHANGES,'epochs':V13T_EPOCHS,'reserve_cells':NCELLS,'writes_per_cell_epoch_if_persist_every_change':v13t_rate,'sonos_100k_endurance_equiv_epochs':ENDURANCE/v13t_rate},
 'synthetic_role_trace':{'epochs':EPOCHS,'raw_role_changes':raw_changes,'raw_change_rate_per_cell_epoch':raw_rate},
 'consolidation_sweep':consolidation,
 'powercut_screen':powercut,
 'sonos_read_margin':sonos_margin,
 'stochastic_search':stochastic,
}
(OUT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
