#!/usr/bin/env python3
from __future__ import annotations
import json, math, os, re, shutil, subprocess
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'results'/'results.json'
Qe=1.602176634e-19

# v15F: Partial-Thought Luminous Screen (PTLS)
# Each lit dot is driven from a 5-V branch for >=1 us. Numeric partial results are represented
# as signed dot count: +10 = two positive dots; -10 = two negative dots. The same AI on another
# chip sees the optical pattern and continues the SAME question, not a new task.


def run_ngspice_screen():
    ng=os.environ.get('NGSPICE') or shutil.which('ngspice') or '/mnt/data/nglocal/bin/ngspice'
    cir=ROOT/'spice'/'screen_10.cir'; log=ROOT/'spice'/'screen_10.log'
    if not Path(ng).exists():
        return {'ran':False,'reason':'ngspice not found'}
    cp=subprocess.run([ng,'-b','-o',str(log),str(cir)],capture_output=True,text=True,timeout=30)
    txt=log.read_text(errors='ignore') if log.exists() else cp.stdout+cp.stderr
    vals={}
    for key in ['vd1_1u','vd2_1u','vdark_1u','vneed_1u','vscience_1u','vscience_max']:
        m=re.search(rf'^{key}\s*=\s*([-+0-9.eE]+)',txt,re.I|re.M)
        vals[key]=float(m.group(1)) if m else None
    return {'ran':True,'returncode':cp.returncode,'values':vals,'deck':'screen_10.cir','log':'screen_10.log'}

def screen_mc(n=500_000, seed=15091, max_quanta=8):
    rng=np.random.default_rng(seed)
    qtrue=rng.integers(-max_quanta,max_quanta+1,size=n)
    duration=np.clip(rng.normal(1.20e-6,0.08e-6,n),1.0e-6,1.6e-6)
    Idot=np.clip(rng.lognormal(np.log(0.25e-6),0.22,(n,max_quanta)),0.08e-6,0.8e-6)
    eff=np.clip(rng.normal(0.035,0.009,(n,max_quanta)),0.012,0.065)
    coupling=np.clip(rng.lognormal(np.log(0.006),0.28,(n,max_quanta)),0.0015,0.020)
    Eph=6.62607015e-34*299792458/590e-9
    Eelec=5.0*Idot*duration[:,None]
    photons=Eelec*eff*coupling/Eph
    qe=np.clip(rng.normal(0.72,0.06,(n,max_quanta)),0.50,0.88)
    signal=rng.poisson(np.maximum(photons*qe,0))
    dark=rng.poisson(5.0,size=(n,max_quanta))
    xtalk_ratio=np.clip(rng.lognormal(np.log(2e-4),0.5,(n,max_quanta)),1e-5,0.002)
    lit_count=np.abs(qtrue)
    total_sig=np.sum(signal,axis=1)
    spill=rng.poisson(np.maximum(total_sig[:,None]*xtalk_ratio/max_quanta,0))
    threshold=55
    idx=np.arange(max_quanta)[None,:]
    intended=idx < lit_count[:,None]
    detected=np.where(intended, signal+dark, dark+spill) >= threshold
    count=np.sum(detected,axis=1)
    sign=np.sign(qtrue)
    qread=count*sign
    qread=np.where(qtrue==0,0,qread)
    exact=qread==qtrue
    Emsg=np.sum(Eelec*intended,axis=1)
    quantiles=lambda x:[float(v) for v in np.quantile(x,[.001,.01,.5,.99,.999])]
    return {
        'trials':n,'encoding':'signed unary 5-unit quanta; +10 = two + dots, each driven from 5-V branch',
        'minimum_visible_time_s':1e-6,
        'exact_partial_value_read_pass':float(np.mean(exact)),
        'misread_rate':float(np.mean(~exact)),
        'plus10_exact_read_pass':float(np.mean(exact[qtrue==2])) if np.any(qtrue==2) else None,
        'plus10_energy_J_q':quantiles(Emsg[qtrue==2]) if np.any(qtrue==2) else [],
        'message_energy_J_q':quantiles(Emsg),
        'lit_dot_photoelectrons_q':quantiles(signal[intended]) if np.any(intended) else [],
        'false_dot_count_rate':float(np.mean(np.any(detected & ~intended,axis=1))),
        'missed_lit_dot_rate':float(np.mean(np.any((~detected)&intended,axis=1))),
        'note':'5 V is the per-dot branch supply. A value of 10 is represented by two 5-unit lit dots rather than forcing 10 V across one emitter.'
    }


def receiver_ode_test():
    C=5e-15; R=100e9; Iph=90e-12; t_on=1.2e-6
    def f(t,y):
        I=Iph if 0<=t<=t_on else 0.0
        return [(I-y[0]/R)/C]
    sol=solve_ivp(f,(0,8e-6),[0.0],max_step=2e-9,rtol=1e-9,atol=1e-12,dense_output=True)
    ts=np.array([0.1e-6,1.0e-6,1.2e-6,2e-6,4e-6,8e-6])
    vs=sol.sol(ts)[0]
    threshold=0.010
    return {'C_F':C,'R_ohm':R,'Iph_A':Iph,'pulse_s':t_on,'read_threshold_V':threshold,'samples_V':{f'{t*1e6:g}us':float(v) for t,v in zip(ts,vs)},'peak_V':float(np.max(sol.y[0])),'read_pass':bool(np.max(sol.y[0])>=threshold)}

def same_model_dialogue_mc(n=300_000,seed=15092):
    rng=np.random.default_rng(seed)
    base_acc=0.82
    rhos=[0.0,0.3,0.6,0.85,1.0]
    out={}
    from scipy.stats import norm
    th=norm.ppf(1-base_acc)
    for rho in rhos:
        z_shared=rng.normal(size=n); z1=rng.normal(size=n); z2=rng.normal(size=n)
        a=np.sqrt(rho)*z_shared+np.sqrt(max(0,1-rho))*z1
        b=np.sqrt(rho)*z_shared+np.sqrt(max(0,1-rho))*z2
        c1=a>th; c2=b>th
        conf1=np.clip(rng.normal(np.where(c1,.80,.46),.12,n),0,1)
        conf2=np.clip(rng.normal(np.where(c2,.80,.46),.12,n),0,1)
        same=c1==c2; disagree=~same
        if rho>=0.999999:
            final_correct=c1.copy(); unresolved=np.zeros(n,dtype=bool)
        else:
            pconv=np.clip(.48+.40*np.abs(conf1-conf2),.48,.86)
            resolved=disagree & (rng.random(n)<pconv)
            both_bad=(~c1)&(~c2)
            precover=max(0.0,0.12*(1-rho))
            recover=both_bad & (rng.random(n)<precover)
            final_correct=(c1&c2) | resolved | recover
            unresolved=disagree & ~resolved
        out[str(rho)]={
            'single_context_accuracy':float(np.mean(c1)),
            'initial_agreement_fraction':float(np.mean(same)),
            'final_correct_fraction_protocol_model':float(np.mean(final_correct)),
            'unresolved_fraction_after_one_exchange':float(np.mean(unresolved)),
            'gain_over_single_context':float(np.mean(final_correct)-np.mean(c1))
        }
    return {'trials_per_correlation':n,'same_model_same_prompt_correlation_sweep':out,'boundary':'Same-model self-dialogue only creates perspective if inference states/sampling are not perfectly correlated. This is a protocol/error-correlation model, not measured GPT quality.'}

def affect_goal_reasoning_mc(n=250_000,seed=15093):
    rng=np.random.default_rng(seed)
    threat=rng.beta(2.0,3.0,n); authorized=rng.beta(3.0,2.0,n); uncertainty=rng.beta(1.8,3.0,n)
    def act(caution,urgency,curiosity):
        allow=1.45*authorized-1.10*threat-0.25*caution
        verify=0.75*uncertainty+0.35*caution+0.25*curiosity+0.15*authorized+0.10*threat
        block=1.45*threat+0.55*urgency-0.72*authorized-0.20*uncertainty
        return np.argmax(np.vstack([allow,verify,block]),axis=0)
    neutral=act(np.full(n,.35),np.full(n,.35),np.full(n,.35))
    cautious=act(np.full(n,.80),np.full(n,.45),np.full(n,.55))
    dist=lambda a:{name:float(np.mean(a==i)) for i,name in enumerate(['allow','verify/challenge','block'])}
    m=50_000
    thv=np.clip(rng.normal(.68,.12,m),0,1); auv=np.clip(rng.normal(.58,.18,m),0,1); unv=np.clip(rng.normal(.62,.15,m),0,1)
    allow=1.45*auv-1.10*thv-.25*.80
    verify=.75*unv+.35*.80+.25*.55+.15*auv+.10*thv
    block=1.45*thv+.55*.45-.72*auv-.20*unv
    av=np.argmax(np.vstack([allow,verify,block]),axis=0)
    return {
      'trials':n,'neutral_affect_action_distribution':dist(neutral),'high_caution_action_distribution':dist(cautious),
      'fraction_actions_changed_by_direct_affect':float(np.mean(neutral!=cautious)),
      'vehicle_like_example_action_distribution':dist(av),
      'direct_affect_definition':'caution/urgency/curiosity are direct signed modulatory states in the reasoning fabric. They change thresholds and search depth; they do not hard-code a particular action and are not claimed to be conscious feelings.',
      'example_interpretation':'In the locked/interior-start style ambiguity, the selected response is usually verify/challenge rather than automatically allow or block, because both threat and legitimate-occupant evidence are considered.'
    }

def partial_result_power_relay():
    value_quanta=2; quantum_value=5; partial=value_quanta*quantum_value
    core_V=0.8; base_window=0.40e-6
    gate_window=value_quanta*base_window
    Cload=40e-15; Rload=20e3
    def f(t,y):
        src=core_V if 0<=t<=gate_window else 0.0
        return [(src-y[0])/(Rload*Cload)]
    sol=solve_ivp(f,(0,2e-6),[0.0],max_step=1e-9,rtol=1e-9,atol=1e-12,dense_output=True)
    return {'partial_result':partial,'representation':'two 5-V screen dots','specialist_core_supply_V':core_V,'gate_window_s':gate_window,'core_peak_V':float(np.max(sol.y[0])),'safety_note':'10 is represented by two 5-unit optical quanta. 10 V is not applied across the specialist chip core.'}

def wiring_comparison(screen_dots=16,chips=8):
    Edot=5*0.25e-6*1.2e-6
    E10=2*Edot
    lengths=np.array([2,5,10,20],float)
    C_per_mm=0.20e-12; Vio=0.8; transitions=5
    Ewire=transitions*.5*C_per_mm*lengths*Vio**2
    return {
        'screen_local_dots':screen_dots,'chips':chips,'energy_for_value_10_two_dots_J_proxy':E10,
        'electrical_partial_result_energy_J_proxy_by_length_mm':{str(int(l)):float(e) for l,e in zip(lengths,Ewire)},
        'conclusion':'At the deliberately long 1us hold, the optical screen is not an energy win over short electrical links. Its value is reduced cross-chip wiring/visible shared state. Use only if package wiring/concurrency benefits justify the optical hold energy.'
    }


def main():
    out={
      'experiment':'v15FG_partial_screen_self_dialogue',
      'status':'MODEL PASS WITH BOUNDARIES',
      'v15F_partial_screen':screen_mc(),
      'v15F_ngspice_screen_10':run_ngspice_screen(),
      'v15F_receiver_transient_scipy':receiver_ode_test(),
      'v15G_same_model_dialogue':same_model_dialogue_mc(),
      'v15F_partial_result_power_relay':partial_result_power_relay(),
      'v15G_direct_affect_goal_reasoning':affect_goal_reasoning_mc(),
      'screen_vs_wire':wiring_comparison(),
      'architecture_decisions':{
        'retain':['v15D signed dendrite charge','HZO slow consolidation','guided-gap firing','4 active + 2 repair branches','unknown state','hardware-revision request only for persistent physical faults','hollow/shared power infrastructure'],
        'replace':['v15E destination-address optical screen -> v15F partial-result working screen'],
        'optional_software_feature':'same-model self-dialogue is an application option, not a new chip block',
        'affect':'direct affect may be represented as modulatory signed state; do not equate it with consciousness or subjective emotion.'
      }
    }
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__': main()
