import json, math
import numpy as np
rng=np.random.default_rng(140152)

# v14O final model-level screen. Not a fabricated measurement or calibrated compact model.
NMC=200_000
GAP_MEAN=1.30; GAP_SIG=.12; FIELD_FOCUS=1.45
NUC_FLOOR=4/np.sqrt(FIELD_FOCUS); BASE_MIG=23.5; BASE_D=2.0; MIG_EXP=1.5
V_FIRE=.25; R_BALLAST=2.2e6; R_GAP_ON=.1e6

def lognormal(mean,cv,n):
    s2=np.log1p(cv*cv); return rng.lognormal(np.log(mean)-s2/2,np.sqrt(s2),n)

gap=np.clip(rng.normal(GAP_MEAN,GAP_SIG,NMC),.55,None)
nuc=lognormal(NUC_FLOOR,.15,NMC)
mig=BASE_MIG*(gap/BASE_D)**MIG_EXP/FIELD_FOCUS*lognormal(1,.13,NMC)
delay=nuc+mig
hazard=np.exp((1.20-gap)/.18)

# intrinsic ballast variation screen
rb=lognormal(R_BALLAST,.20,NMC); rg=lognormal(R_GAP_ON,.50,NMC)
I=V_FIRE/(rb+rg)

G={'OFF':.25e-9,'WEAK':2.5e-9,'STRONG':25e-9}
Geff={k:1/(1/v+R_BALLAST) for k,v in G.items()}

# Local differential coincidence programming. One learning coincidence has full differential;
# subthreshold half-select stress is assumed volatile/relaxing between independent teaching events.
# v14K provisional consolidation asks for 3 corroborating coincidences before hardening an uncertain revision.
NPROG=300_000
thr=lognormal(8.0,.15,NPROG)
read_dose=.2**2*20
half_dose=.2**2*100
full_dose=.4**2*100
p_read=float(np.mean(read_dose>=thr)); p_half=float(np.mean(half_dose>=thr)); p_full=float(np.mean(full_dose>=thr))
K=3
p_half_cons=p_half**K
p_full_cons=p_full**K

# Cascade
TRIALS=1200; N=64; LAYERS=8; N_STR=3; N_WEAK=2; ND=3
LINK_FAIL=.01; FIRE_FAIL=.01; VREAD=.2; TPULSE=20e-9
THF=.5; THSIG=.10

def cascade(sig):
    active=np.ones((TRIALS,N),bool); le=np.zeros(TRIALS); fc=np.zeros(TRIALS)
    for _ in range(1,LAYERS):
        q=np.zeros((TRIALS,N))
        for g,c in ((Geff['STRONG'],N_STR),(Geff['WEAK'],N_WEAK)):
            for __ in range(c):
                idx=rng.integers(0,N,(TRIALS,N)); pred=np.take_along_axis(active,idx,1)
                ok=rng.random((TRIALS,N))>LINK_FAIL; var=np.maximum(0,1+rng.normal(0,sig,(TRIALS,N)))
                f=pred&ok; q+=g*VREAD*TPULSE*var*f; le+=f.sum(1)*VREAD*VREAD*g*TPULSE
        for __ in range(ND):
            bg=(rng.random((TRIALS,N))<.2)&(rng.random((TRIALS,N))>LINK_FAIL)
            var=np.maximum(0,1+rng.normal(0,sig,(TRIALS,N)))
            q+=Geff['WEAK']*VREAD*TPULSE*var*bg; le+=bg.sum(1)*VREAD*VREAD*Geff['WEAK']*TPULSE
        qnom=(N_STR*Geff['STRONG']+N_WEAK*Geff['WEAK'])*VREAD*TPULSE
        th=qnom*THF*np.maximum(.65,1+rng.normal(0,THSIG,(TRIALS,N)))
        active=(q>=th)&(rng.random((TRIALS,N))>FIRE_FAIL); fc+=active.sum(1)
    finals=active.mean(1)
    dmean=float(delay.mean()); fireE=V_FIRE*float(I.mean())*dmean*1e-9*1e15
    epf=np.divide(le,fc,out=np.zeros_like(le),where=fc>0)*1e15+fireE+1.5
    return {'sigma':sig,'mean_final':float(finals.mean()),'p05':float(np.quantile(finals,.05)),'min':float(finals.min()),'mean_fJ_per_fire':float(epf.mean())}

casc=[cascade(s) for s in (.1,.2,.3,.4)]

# background-only logical false-fire screen; spontaneous atomic bridging remains uncalibrated.
S=400_000; q=np.zeros(S)
for _ in range(ND):
    bg=rng.random(S)<.2; var=np.maximum(0,1+rng.normal(0,.3,S)); q+=Geff['WEAK']*VREAD*TPULSE*var*bg
qnom=(N_STR*Geff['STRONG']+N_WEAK*Geff['WEAK'])*VREAD*TPULSE
th=qnom*THF*np.maximum(.65,1+rng.normal(0,THSIG,S))
false_logic=int(np.count_nonzero(q>=th))

# 64-hop sparse transport
H=64; T0=.06; ALPHA=.018; PE=.035; TTR=2500
fire_event_fJ=V_FIRE*float(I.mean())*float(delay.mean())*1e-9*1e15+1.5
best=None
for sp in range(8,30):
    nodes=math.ceil(H/sp); lengths=[sp]*(nodes-1)+[H-sp*(nodes-1)]
    ds=[]; good=0
    for _ in range(TTR):
        d=0; ok=True
        for L in lengths:
            if math.exp(-ALPHA*L)*rng.normal(1,.05)<.5: ok=False; break
            d+=T0*L*L+float(lognormal(float(delay.mean()),.15,1)[0])
        if ok: good+=1; ds.append(d)
    succ=good/TTR
    if succ>=.999:
        row={'spacing':sp,'nodes':nodes,'success':succ,'mean_ns':float(np.mean(ds)),'p95_ns':float(np.quantile(ds,.95)),
             'energy_fJ':H*PE+nodes*fire_event_fJ}
        if best is None or (row['mean_ns'],row['energy_fJ'])<(best['mean_ns'],best['energy_fJ']): best=row

# conservative rewrite correctness under independent 5% physical program failure after coincidence qualification.
def rewrite(copies):
    changed=10000; fail=.05; correct=0
    for _ in range(changed):
        old=sum(rng.random(copies)>(fail+(1-p_full_cons)))
        new=sum(rng.random(copies)>(fail+(1-p_full_cons)))
        need=copies//2+1
        corrupt=np.any(rng.random(4*copies)<p_half_cons)
        correct += old>=need and new>=need and not corrupt
    return correct/changed

out={
 'schema':'v14O-guided-gap-self-limited-junction-v2',
 'evidence_boundary':'Engineering sensitivity model, not compact-model or fabricated-device evidence.',
 'selected_geometry':{'total_oxide_nm':4.0,'dynamic_gap_mean_nm':GAP_MEAN,'gap_sigma_nm':GAP_SIG,'field_focus_factor':FIELD_FOCUS,
                      'intrinsic_ballast_Mohm':R_BALLAST/1e6,'concept':'inert nano-spine + sharp field-focus tip + short Ag dynamic gap + passive ballast neck'},
 'delay':{'mean_ns':float(delay.mean()),'p95_ns':float(np.quantile(delay,.95)),'p99_ns':float(np.quantile(delay,.99)),
          'prob_le_15ns':float(np.mean(delay<=15)),'prob_le_38p5ns':float(np.mean(delay<=38.5))},
 'ballast_current':{'mean_nA':float(I.mean()*1e9),'p01_nA':float(np.quantile(I,.01)*1e9),'p99_nA':float(np.quantile(I,.99)*1e9)},
 'link_ballast_effective_nS':{k:v*1e9 for k,v in Geff.items()},
 'strong_link_penalty_fraction':1-Geff['STRONG']/G['STRONG'],
 'gap_hazard_proxy':{'mean_relative_to_1p2nm':float(hazard.mean()),'p99':float(np.quantile(hazard,.99)),
                     'warning':'relative comparison only; spontaneous-bridge probability is not calibrated'},
 'coincidence_programming':{'single_full_program_probability':p_full,'single_half_select_disturb_probability':p_half,
                            'read_disturb_probability':p_read,'provisional_confirmations':K,
                            'three_confirmation_program_probability':p_full_cons,'three_confirmation_half_select_proxy':p_half_cons},
 'cascade':casc,'background_only_logical_false_fires':false_logic,
 'sparse_transport':best,'cmos_transport_control':{'delay_ns':111.36,'energy_fJ':261.44},
 'relation_rewrite_correctness_with_5pct_physical_write_fail':{str(c):rewrite(c) for c in (1,2,3)},
 'decision':'KEEP model-level. v14O fixes v14N delay by guiding the final bridge rather than shrinking the whole oxide; passive ballast addresses current compliance; local differential coincidence programming attacks selector/write-driver overhead. Physical closure remains required.'
}
print(json.dumps(out,indent=2))
