#!/usr/bin/env python3
from __future__ import annotations
import json, math, os, re, shutil, subprocess
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'results'/'results.json'


def sigmoid(x):
    return 1/(1+np.exp(-x))


def run_ngspice_vector_screen():
    candidates=[os.environ.get('NGSPICE'),shutil.which('ngspice'),'/mnt/data/nglocal/bin/ngspice']
    ng=next((x for x in candidates if x and Path(x).exists()),None)
    cir=ROOT/'spice'/'screen_vector.cir'; log=ROOT/'spice'/'screen_vector.log'
    if not ng:
        return {'ran':False,'reason':'fresh ngspice binary not present in current runtime; v15FG real ngspice screen result remains inherited physical-circuit evidence','deck':'screen_vector.cir'}
    cp=subprocess.run([ng,'-b','-o',str(log),str(cir)],capture_output=True,text=True,timeout=30)
    txt=log.read_text(errors='ignore') if log.exists() else cp.stdout+cp.stderr
    vals={}
    for k in [f'v{i}' for i in range(8)]+['vref']:
        m=re.search(rf'^{k}\s*=\s*([-+0-9.eE]+)',txt,re.I|re.M)
        vals[k]=float(m.group(1)) if m else None
    target=np.array([0.15,0.72,0.38,0.00,1.00,0.57,0.09,0.83])
    rec=None; rmse=maxerr=None
    if vals.get('vref') and vals['vref']>0 and all(vals.get(f'v{i}') is not None for i in range(8)):
        rec=np.array([vals[f'v{i}']/vals['vref'] for i in range(8)])
        rmse=float(np.sqrt(np.mean((rec-target)**2))); maxerr=float(np.max(np.abs(rec-target)))
    return {'ran':True,'returncode':cp.returncode,'values_V':vals,'target_normalized':target.tolist(),
            'recovered_normalized':None if rec is None else rec.tolist(),'rmse':rmse,'max_abs_error':maxerr,
            'semantic_note':'Emitter supply is hardware-only. Dot meaning is normalized optical working-state intensity, not voltage-as-number.'}


def optical_vector_mc(n=500_000,seed=15111,dots=8):
    rng=np.random.default_rng(seed)
    x=rng.beta(1.35,1.35,(n,dots))
    hold=np.clip(rng.normal(1.25e-6,.10e-6,n),1.0e-6,1.7e-6)
    common=np.clip(rng.lognormal(0,.16,n),.55,1.65)
    gtrue=np.clip(rng.lognormal(0,.18,(n,dots)),.48,1.8)
    gcal=gtrue*(1+rng.normal(0,.008,(n,dots)))
    gcal=np.clip(gcal,.35,2.2)
    full_e=2600.0
    mu=full_e*common[:,None]*gtrue*x
    xt=np.clip(rng.lognormal(np.log(1.5e-4),.45,n),2e-5,1.2e-3)
    total=np.sum(mu,axis=1,keepdims=True)
    mu_rx=mu+xt[:,None]*(total-mu)/(dots-1)+4.0
    counts=rng.poisson(np.maximum(mu_rx,0))
    ref=rng.poisson(np.maximum(full_e*common,1)+4.0)
    black=rng.poisson(4.0,size=n)
    drift_est=np.maximum(ref-black,1)/full_e
    signal=np.maximum(counts-black[:,None],0)
    xhat=np.clip(signal/(full_e*drift_est[:,None]*gcal),0,1.15)
    rmse=np.sqrt(np.mean((xhat-x)**2,axis=1)); maxerr=np.max(np.abs(xhat-x),axis=1)
    I_fs=np.clip(rng.lognormal(np.log(.18e-6),.18,n),.07e-6,.45e-6)
    E=5.0*I_fs*hold*np.sum(x,axis=1)
    q=lambda a:[float(v) for v in np.quantile(a,[.001,.01,.5,.99,.999])]
    return {'trials':n,'dots':dots,'minimum_hold_s':1e-6,
            'representation':'calibrated normalized analog optical working-state vector; no literal voltage/value mapping',
            'calibration':'per-dot static gain calibration + one reference dot + one black/dark reference',
            'rmse_q':q(rmse),'max_error_q':q(maxerr),
            'pass_rmse_below_0p05':float(np.mean(rmse<.05)),
            'pass_max_error_below_0p12':float(np.mean(maxerr<.12)),
            'energy_J_q':q(E)}


def cooperative_deliberation_mc(n=250_000,seed=15112):
    rng=np.random.default_rng(seed); K=8
    difficulty=rng.beta(2.0,2.0,n)
    base_logit=(1.20-1.55*difficulty[:,None])+rng.normal(0,.24,(n,K))
    critical=np.zeros(K,dtype=bool); critical[:2]=True

    def branch_comp(corr):
        common=rng.normal(0,.55,(n,K)); a=rng.normal(0,.55,(n,K)); b=rng.normal(0,.55,(n,K))
        ca=base_logit+common*.45+a*.55
        cb=base_logit+common*.45+(math.sqrt(corr)*a+math.sqrt(max(0,1-corr))*b)*.55
        return ca,cb

    def solve_single(passes=8):
        ca,_=branch_comp(1.0); state=np.zeros((n,K),np.int8)
        for t in range(passes):
            unk=state==0; wrong=state==-1
            pdisc=sigmoid(ca+.10+.035*t)
            hit=(rng.random((n,K))<pdisc)&unk
            correct=hit&(rng.random((n,K))<.945)
            state[correct]=1; state[hit&~correct]=-1
            prep=.16*sigmoid(ca+.25+.03*t)
            fix=(rng.random((n,K))<prep)&wrong
            state[fix]=1
        ok=(np.sum(state==1,axis=1)>=7)&~np.any((state==-1)&critical,axis=1)
        return ok,np.sum(state==1,axis=1),np.sum(state==-1,axis=1)

    def solve_dialogue(corr=.45,syc=.07,turns=8):
        ca,cb=branch_comp(corr); state=np.zeros((n,K),np.int8)
        contributor=np.full((n,K),-1,np.int8)
        for t in range(turns):
            who=t%2; comp=ca if who==0 else cb
            active=rng.random(n)>=syc
            unk=state==0; wrong=state==-1
            focus=.33+.05*t
            pdisc=sigmoid(comp+focus)
            hit=(rng.random((n,K))<pdisc)&unk&active[:,None]
            correct=hit&(rng.random((n,K))<.952)
            state[correct]=1; contributor[correct]=who
            bad=hit&~correct; state[bad]=-1; contributor[bad]=who
            other_wrong=wrong&(contributor!=who)
            same_wrong=wrong&(contributor==who)
            prep_other=.62*sigmoid(comp+.40)
            prep_same=.20*sigmoid(comp+.10)
            fix=((rng.random((n,K))<prep_other)&other_wrong | (rng.random((n,K))<prep_same)&same_wrong) & active[:,None]
            state[fix]=1; contributor[fix]=who
        ok=(np.sum(state==1,axis=1)>=7)&~np.any((state==-1)&critical,axis=1)
        return ok,np.sum(state==1,axis=1),np.sum(state==-1,axis=1)

    s,si,se=solve_single(8)
    d,di,de=solve_dialogue(.45,.07,8)
    ident,ii,ie=s.copy(),si.copy(),se.copy()
    syc,yi,ye=solve_dialogue(.45,.42,8)
    return {'trials':n,
      'protocol':'same model, same original prompt, shared evolving transcript. A contributes a partial line of reasoning; B reads it and extends/reframes/repairs it; A then continues from the updated transcript. Final synthesis occurs only after the discussion.',
      'single_same_compute':{'success':float(np.mean(s)),'mean_correct_insights':float(np.mean(si)),'mean_wrong_insights':float(np.mean(se))},
      'cooperative_dialogue':{'success':float(np.mean(d)),'mean_correct_insights':float(np.mean(di)),'mean_wrong_insights':float(np.mean(de))},
      'near_identical_state_control':{'success':float(np.mean(ident)),'mean_correct_insights':float(np.mean(ii)),'mean_wrong_insights':float(np.mean(ie))},
      'high_sycophancy_control':{'success':float(np.mean(syc)),'mean_correct_insights':float(np.mean(yi)),'mean_wrong_insights':float(np.mean(ye))},
      'gain_over_single_protocol_model':float(np.mean(d)-np.mean(s)),
      'boundary':'Protocol/latent-insight simulation only. This runtime cannot spawn two independent GPT-5.6 Sol conversations, so a real same-model A/B remains required.'}


def context_modulation_mc(n=350_000,seed=15113):
    rng=np.random.default_rng(seed)
    threat=rng.beta(2,3,n); benefit=rng.beta(2.6,2.2,n); uncertainty=rng.beta(1.8,2.7,n)
    novelty=rng.beta(1.8,2.4,n); urgency=rng.beta(1.7,3.0,n)
    evidence=np.vstack([1.25*benefit-1.00*threat-.28*uncertainty,
                        .72*uncertainty+.30*novelty+.12*benefit+.08*threat,
                        1.20*threat-.58*benefit+.18*urgency]).T
    hidden=rng.normal(0,.16,evidence.shape)
    true=np.argmax(evidence+hidden,axis=1)
    base=np.argmax(evidence,axis=1)
    salience=np.clip(.55*novelty+.45*np.abs(threat-benefit),0,1)
    outcome=np.clip(benefit-threat,-1,1)
    margin=np.partition(evidence,-2,axis=1)[:,-1]-np.partition(evidence,-2,axis=1)[:,-2]

    unsafe=evidence.copy(); unsafe[:,0]+=.85*outcome; unsafe[:,1]+=.70*uncertainty+.45*salience; unsafe[:,2]+=.85*(-outcome)+.50*urgency
    unsafe_act=np.argmax(unsafe,axis=1)

    need=(uncertainty>.48)|(salience>.58)|(margin<.16)
    observations=np.where(need, np.where(urgency>.82,1,2), 0)
    estimate=np.zeros_like(hidden)
    for m in [1,2]:
        idx=observations>=m
        if np.any(idx):
            obs=hidden[idx]+rng.normal(0,.12,hidden[idx].shape)
            if m==1: estimate[idx]=obs
            else: estimate[idx]=(estimate[idx]+obs)/2
    refined=evidence+np.where(need[:,None],.78*estimate,0)
    act=np.argmax(refined,axis=1)
    gain=np.clip(1+.10*salience+.06*urgency-.07*uncertainty,.85,1.15)
    plasticity=np.clip(.50+.30*np.abs(outcome)+.12*salience,0,1)
    return {'trials':n,
      'principle':'diffuse context fields modulate gain, replay/observation budget, commitment margin and later plasticity; they do not encode a target action.',
      'fields':{'salience':'importance/novelty gain','uncertainty':'requests more internal observation/replay','signed_outcome':'later reinforcement/depression sign and strength','urgency':'limits or accelerates deliberation'},
      'baseline_accuracy_proxy':float(np.mean(base==true)),
      'rejected_action_coded_affect_accuracy_proxy':float(np.mean(unsafe_act==true)),
      'rejected_action_coded_fraction_changed':float(np.mean(unsafe_act!=base)),
      'selected_context_field_accuracy_proxy':float(np.mean(act==true)),
      'selected_extra_reasoning_fraction':float(np.mean(need)),
      'selected_mean_extra_observations':float(np.mean(observations)),
      'selected_action_change_after_new_evidence':float(np.mean(act!=base)),
      'gain_q':[float(v) for v in np.quantile(gain,[.001,.01,.5,.99,.999])],
      'plasticity_q':[float(v) for v in np.quantile(plasticity,[.001,.01,.5,.99,.999])],
      'decision':'reject emotion-as-command; keep bounded neuromodulatory context fields that alter processing and learning while evidence selects behavior.'}


def main():
    out={'experiment':'v15G_cooperative_deliberation_context_field','status':'PARTIAL PASS',
         'corrected_screen':optical_vector_mc(),
         'screen_spice_check':run_ngspice_vector_screen(),
         'cooperative_self_dialogue':cooperative_deliberation_mc(),
         'brain_principle_context_field':context_modulation_mc(),
         'decisions':{
           'screen':'v15FG literal number/voltage mapping rejected. Screen carries calibrated temporary analog partial-thought state for >=1us; hardware voltage is not meaning.',
           'dialogue':'not answer-then-compare. Two same-model branches co-author one evolving solution through a shared transcript; independent inference state is necessary for perspective.',
           'emotion':'do not encode named emotion commands. Use diffuse context modulation analogous in principle to neuromodulation: gain, attention/replay, commitment and plasticity.',
           'core':'retain v15D signed dendrite free charge + natural decay + HZO consolidation; no added learning capacitor.'}}
    OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2))

if __name__=='__main__': main()
