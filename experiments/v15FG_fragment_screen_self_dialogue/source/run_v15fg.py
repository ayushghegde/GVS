#!/usr/bin/env python3
import json, math, hashlib
import numpy as np
from pathlib import Path

OUT=Path(__file__).resolve().parents[1]/'results'/'results.json'
rng=np.random.default_rng(15067)

# ---------------- F: fragment scratch screen ----------------
# 8 data dots + 4 Hamming parity dots. Each dot uses a fixed 5 V emitter domain.
# The mathematical value is NOT represented as a high logic voltage.
VPIX=5.0
HOLD_US=1.0
N=300_000
values=rng.integers(0,256,N,dtype=np.uint16)

def encode_hamming_12_8(vals):
    bits=np.zeros((len(vals),13),dtype=np.uint8)
    data_pos=[3,5,6,7,9,10,11,12]
    for j,p in enumerate(data_pos): bits[:,p]=(vals>>j)&1
    for p in [1,2,4,8]:
        idx=[i for i in range(1,13) if i&p and i!=p]
        bits[:,p]=np.bitwise_xor.reduce(bits[:,idx],axis=1)
    return bits[:,1:]

def decode_hamming(arr):
    b=np.zeros((len(arr),13),dtype=np.uint8); b[:,1:]=arr
    syndrome=np.zeros(len(arr),dtype=np.int16)
    for p in [1,2,4,8]:
        idx=[i for i in range(1,13) if i&p]
        bad=np.bitwise_xor.reduce(b[:,idx],axis=1)
        syndrome += bad.astype(np.int16)*p
    fix=(syndrome>=1)&(syndrome<=12)
    rows=np.nonzero(fix)[0]
    b[rows,syndrome[rows]] ^= 1
    data_pos=[3,5,6,7,9,10,11,12]
    out=np.zeros(len(arr),dtype=np.uint16)
    for j,p in enumerate(data_pos): out |= (b[:,p].astype(np.uint16)<<j)
    return out, syndrome

code=encode_hamming_12_8(values)
photo_mean_on=np.exp(rng.normal(np.log(110),0.38,N))
dark_mean=np.exp(rng.normal(np.log(0.9),0.45,N))
xtalk=np.clip(rng.lognormal(np.log(4e-3),0.8,N),0,0.06)
counts=np.empty_like(code,dtype=np.int32)
for j in range(12):
    neigh=(code[:,(j-1)%12]+code[:,(j+1)%12])
    mu=dark_mean + code[:,j]*photo_mean_on + neigh*photo_mean_on*xtalk
    counts[:,j]=rng.poisson(mu)
thr=np.maximum(10,0.24*photo_mean_on)[:,None]
read=(counts>thr).astype(np.uint8)
decoded,syndrome=decode_hamming(read)
screen_ok=decoded==values
raw_bit_errors=np.sum(read!=code)

Cdrive=2e-15
analog_vals=values.astype(float)
E_direct=0.5*Cdrive*analog_vals**2
I_nom=0.1e-6
lit=code.sum(axis=1)
E_screen=lit*VPIX*I_nom*(HOLD_US*1e-6)
I_sweep=np.array([0.05e-6,0.1e-6,0.2e-6,0.5e-6,1.0e-6])
E_screen_sweep={str(float(i*1e6)):float(np.median(lit*VPIX*i*(HOLD_US*1e-6))*1e12) for i in I_sweep}

hold=np.clip(rng.normal(1.25,0.12,N),1.0,None)
observe=rng.uniform(0,1.0,N)
persistence_ok=observe<=hold

dist_mm=np.array([2.,5.,10.,20.])
Cline=0.2e-15*(dist_mm*1000)
E_elec=12*0.5*0.5*Cline*(0.8**2)

# ---------------- G: same-AI self-dialogue option ----------------
M=500_000
difficulty=rng.beta(2.2,4.5,M)
p_single=0.985-0.23*difficulty**1.35
shared_bad=rng.random(M) < (0.35*(1-p_single))
ind1=rng.random(M)<p_single
ind2=rng.random(M)<p_single
ok1=ind1 & ~shared_bad
ok2=ind2 & ~shared_bad
single_acc=ok1.mean()
pair_no_talk=np.where(ok1==ok2,ok1,rng.random(M)<0.5)
disagree=ok1!=ok2
both_wrong=~ok1 & ~ok2
resolved=np.zeros(M,dtype=bool)
resolved[ok1&ok2]=True
p_resolve=np.clip(0.93-0.25*difficulty,0.55,0.95)
resolved[disagree]=rng.random(disagree.sum())<p_resolve[disagree]
p_reroute=np.clip(0.24-0.12*difficulty,0.04,0.24)
resolved[both_wrong]=rng.random(both_wrong.sum())<p_reroute[both_wrong]
dialogue_acc=resolved.mean()

# ---------------- Direct emotion-like modulation ----------------
K=250_000
risk=rng.beta(2,4,K)
uncert=rng.beta(2.5,2.5,K)
urgency=rng.beta(2,3,K)
novelty=rng.beta(2,3,K)
verify_true=1.3*risk*uncert + 0.45*risk - 0.30*urgency
act_true=0.95*urgency + 0.35*(1-uncert) - 0.75*risk*uncert
explore_true=0.95*novelty*uncert - 0.28*urgency
truth=np.argmax(np.stack([verify_true,act_true,explore_true],1),axis=1)
noise=rng.normal(0,0.13,(K,3))
static=np.stack([0.95*risk,0.78*urgency,0.65*novelty],1)+noise
static_choice=np.argmax(static,1)
caution=np.clip(risk*uncert,0,1)
urg_mod=urgency
curiosity=np.clip(novelty*uncert,0,1)
mod=np.stack([
    0.95*risk + 0.62*caution - 0.18*urg_mod,
    0.78*urgency + 0.20*(1-uncert) - 0.42*caution,
    0.65*novelty + 0.55*curiosity - 0.15*urg_mod
],1)+noise
mod_choice=np.argmax(mod,1)

# ---------------- hardware-fault revision requests ----------------
R=100_000
fault=rng.random(R)<0.055
base=rng.normal(0,1,(R,4,8))
base[fault,:, :] += rng.normal(1.65,0.25,(fault.sum(),4,1))
window_bad=(base>1.25).sum(axis=1)>=2
doubt=window_bad.sum(axis=1)
request=doubt>=5

results={
 'experiment':'v15FG_fragment_screen_self_dialogue',
 'status':'PARTIAL PASS',
 'selected_architecture':{
   'screen':'FSS Fragment Scratch Screen: fixed-voltage optical dots hold only intermediate fragments >=1 us; not destination routing',
   'dialogue':'optional same-model mirror dialogue mode for high-compute users; same prompt to same model replicas then exchange/aggregate',
   'learning':'inherit v15D charge-gradient dendrites; no FITA/tunnel; no extra learning capacitor',
   'modulation':'direct functional global charge biases (caution/urgency/curiosity), not literal emotions or consciousness',
   'hardware_request':'persistent physical-fault evidence may request maker revision; knowledge unknown does not'
 },
 'screen':{
   'trials':N,'hold_min_us':HOLD_US,'coding':'Hamming(12,8), fixed 5-V emitter domain',
   'decode_success':float(screen_ok.mean()),'raw_bit_error_rate':float(raw_bit_errors/code.size),
   'persistence_observed_success':float(persistence_ok.mean()),
   'mean_lit_dots':float(lit.mean()),
   'energy_nominal_pj':{'p50':float(np.percentile(E_screen,50)*1e12),'p99':float(np.percentile(E_screen,99)*1e12)},
   'energy_p50_pj_vs_emitter_current_uA':E_screen_sweep,
   'direct_numeric_voltage_rejected':{'max_value_v':255.0,'median_energy_pj':float(np.median(E_direct)*1e12),'reason':'numerical value should not equal device voltage; energy/stress scales with value squared'},
   'electrical_12bit_bus_energy_pj_by_distance':{str(int(d)):float(e*1e12) for d,e in zip(dist_mm,E_elec)}
 },
 'same_ai_dialogue':{
   'trials':M,'single_accuracy':float(single_acc),'two_copy_no_talk_accuracy':float(pair_no_talk.mean()),
   'one_exchange_dialogue_accuracy':float(dialogue_acc),'fixed_dialogue_compute_multiplier_proxy':2.45,
   'initial_disagreement_rate':float(disagree.mean()),
   'adaptive_dialogue_compute_multiplier_proxy':float(2.0+0.45*disagree.mean()),
   'evidence_boundary':'correlated-error model, not an actual LLM benchmark in this runtime'
 },
 'direct_modulation':{
   'trials':K,'static_accuracy_vs_generic_optimum':float((static_choice==truth).mean()),
   'modulated_accuracy_vs_generic_optimum':float((mod_choice==truth).mean()),
   'note':'functional emotion-like modulation only; does not imply subjective emotion'
 },
 'hardware_revision_request':{
   'trials':R,'fault_prevalence':float(fault.mean()),'fault_detection':float(request[fault].mean()),
   'false_request_rate':float(request[~fault].mean())
 },
 'accepted_from_prior':['HZO polarity','guided-gap firing','positive/negative charge-gradient dendrites','natural decay','four active + two repair branches','hollow shared infrastructure','hardware revision requests for physical faults','zero-MOS ordinary semantic cells'],
 'rejected_or_corrected':['v15E destination-address optical plane','literal numeric voltage encoding','FITA tunnel','SEEP delayed tag','extra learning capacitor'],
}
OUT.write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
print('sha256',hashlib.sha256(OUT.read_bytes()).hexdigest())
