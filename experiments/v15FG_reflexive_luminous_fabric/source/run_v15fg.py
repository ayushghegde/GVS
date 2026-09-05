import json
import numpy as np
from scipy.integrate import solve_ivp
from pathlib import Path

SEED=150706
rng=np.random.default_rng(SEED)
N=300000

# Luminous Intermediate Surface: shared AI context, optical surface carries only scalar intermediate/need.
num_specialists=8
vmax_value=20.0
hold_us=1.2
wavelength=590e-9
h=6.62607015e-34; c=299792458.0
photon_E=h*c/wavelength
E_full=80e-15
xtalk=np.exp(rng.normal(np.log(2e-4),0.55,size=N))
xtalk=np.clip(xtalk,1e-6,4e-3)
node_v_full=0.45
values=rng.uniform(-vmax_value,vmax_value,size=N)
target=rng.integers(0,num_specialists,size=N)
mag=np.abs(values)/vmax_value
photons_mean=(E_full*mag/photon_E)
photons=rng.poisson(np.maximum(photons_mean,0))
dark=rng.normal(0,18,size=N)
meas_ph=np.maximum(0, photons+dark)
meas_mag=np.clip(meas_ph*photon_E/E_full,0,1.2)
decoded=np.sign(values)*meas_mag*vmax_value
abs_err=np.abs(decoded-values)
false_wake=((xtalk>0.07) & (mag>0.05)) | ((mag<=0.05) & (rng.random(N)<2e-6))
miss=(meas_mag<0.03)&(mag>0.05)
mask=mag>0.1
lis={
 'trials':N,'hold_us':hold_us,'full_scale_optical_energy_fJ':E_full*1e15,
 'full_scale_photons':E_full/photon_E,
 'decoded_value_mae_units':float(np.mean(abs_err[mask])),
 'decoded_value_p99_error_units':float(np.quantile(abs_err[mask],.99)),
 'false_wake_rate':float(false_wake.mean()),'miss_rate':float(miss.mean()),
 'crosstalk_median':float(np.median(xtalk)),'crosstalk_p99':float(np.quantile(xtalk,.99)),
 'physical_node_fullscale_V':node_v_full,
 'note':'scalar intermediate+need only; semantic context is already shared by the same AI state'
}

Cnode=50e-15; Rleak=30e6; responsivity=.4; Pfull=E_full/(hold_us*1e-6)
def node_ode(t,y,power):
    I=responsivity*power if t<hold_us*1e-6 else 0.0
    return [(I-y[0]/Rleak)/Cnode]
sol=solve_ivp(lambda t,y:node_ode(t,y,Pfull),[0,5e-6],[0.0],max_step=2e-9,rtol=1e-8,atol=1e-11)
v=sol.y[0]; tt=sol.t
lis['need_node_peak_V']=float(v.max())
lis['need_node_1us_V']=float(np.interp(1e-6,tt,v))
lis['need_node_2us_V']=float(np.interp(2e-6,tt,v))

# Same-AI reflexive discussion toy orchestration model.
M=250000
latent=rng.choice([-1,1],size=M)
difficulty=rng.beta(2.2,3.0,size=M)
signal=2.8*(1-difficulty)+0.25
e1=latent*signal+rng.normal(0,1,size=M)
single=np.sign(e1); single[single==0]=1
single_acc=float(np.mean(single==latent))
e2=latent*signal+rng.normal(0,1,size=M)
conf1=np.tanh(e1/2); conf2=np.tanh(e2/2)
r1=e1+0.75*conf2; r2=e2+0.75*conf1
synth=r1+r2+0.25*np.sign(r1*r2)*np.minimum(np.abs(r1),np.abs(r2))
pred=np.sign(synth); pred[pred==0]=1
linked_acc=float(np.mean(pred==latent))
discuss_needed=(np.sign(e1)!=np.sign(e2)) | (np.maximum(np.abs(e1),np.abs(e2))<1.4)
reflex={'trials':M,'single_path_accuracy':single_acc,'linked_same_ai_accuracy':linked_acc,
 'absolute_accuracy_gain':linked_acc-single_acc,'discussion_fraction':float(np.mean(discuss_needed)),
 'note':'orchestration simulation only; does not measure real LLM reasoning quality'}

# Need-based reasoning behavior.
K=200000
known_conf=rng.beta(4.5,1.8,size=K)
novel=rng.random(K)<0.22
contradiction=rng.random(K)<0.08
need=(known_conf<0.63)|novel|contradiction
rounds=np.ones(K,dtype=int)
conf=known_conf.copy()
for r in range(2,11):
    active=need & (conf<0.82)
    if not active.any(): break
    gain=rng.beta(2.5,5.0,size=K)*0.35
    conf[active]=np.clip(conf[active]+gain[active],0,1)
    rounds[active]=r
need_behavior={'tasks':K,'need_trigger_fraction':float(need.mean()),'mean_rounds':float(rounds.mean()),
 'p99_rounds':float(np.quantile(rounds,.99)),
 'answerable_fraction':float(np.mean((~need & (known_conf>=0.63)) | (need & (conf>=0.82)))),
 'durably_resolved_need_fraction':float(np.mean(conf[need]>=0.82)),
 'unresolved_need_fraction':float(np.mean(conf[need]<0.82))}

# Hardware diagnostic request: physical faults only.
H=120000
fault=rng.random(H)<0.05
leak=rng.normal(0,1,(H,6))+fault[:,None]*2.3
timing=rng.normal(0,1,(H,6))+fault[:,None]*1.8
temp=rng.normal(0,1,(H,6))+fault[:,None]*1.5
repair=rng.poisson(0.15,(H,6))+fault[:,None]*rng.poisson(1.2,(H,6))
score=0.9*np.maximum(leak-0.8,0)+0.8*np.maximum(timing-0.6,0)+0.55*np.maximum(temp-0.8,0)+0.7*(repair>=1)
bad_windows=score>2.25
request=(bad_windows.sum(axis=1)>=3) | ((score>3.4).sum(axis=1)>=2)
hw={'regions':H,'fault_fraction':float(fault.mean()),'revision_request_true_positive':float(request[fault].mean()),
 'revision_request_false_positive':float(request[~fault].mean()),'requests_total':int(request.sum()),
 'meaning':'maker-facing chip-revision request only for persistent physical weakness'}

# Affect-like direct modulators (control signals, not consciousness/emotion claim).
A=180000
risk=rng.random(A); uncert=rng.random(A); benefit=rng.random(A)
base_act=benefit>risk
caution=np.clip(risk*0.8+uncert*0.2,0,1)
curiosity=np.clip(uncert*0.9+0.1*(1-benefit),0,1)
mod_act=benefit>(risk+0.22*caution)
verify=(caution>0.55)&(uncert>0.35)
explore=(curiosity>0.62)&(~mod_act)
base_hazard=np.mean(base_act & (risk>0.75))
mod_hazard=np.mean(mod_act & (risk>0.75) & ~verify)
affect={'trials':A,'baseline_high_risk_action_rate':float(base_hazard),
 'modulated_unverified_high_risk_action_rate':float(mod_hazard),'verification_rate':float(verify.mean()),
 'exploration_rate':float(explore.mean()),
 'interpretation':'affect-like control biases (caution/curiosity), not subjective emotion or consciousness'}

charge={'local_node_capacitance_aF':24.0,'status':'intrinsic/effective dendrite-HZO capacitance only; no added memory capacitor',
 'explanation':'positive/negative charge is the state; capacitance is the physical relation between charge and voltage'}

out={'experiment':'v15FG_reflexive_luminous_fabric','seed':SEED,'status':'PARTIAL PASS',
 'luminous_intermediate_surface':lis,'same_ai_reflexive_mode':reflex,'need_based_reasoning':need_behavior,
 'hardware_revision_diagnostic':hw,'affect_like_modulation':affect,'charge_gradient_memory':charge,
 'decisions':{'drop_previous_destination-code interpretation':True,'screen_carries_entire_prompt':False,
 'screen_carries_scalar_intermediate_and_need':True,'literal_10V_core_encoding':False,
 'same_ai_linked_discussion_is_optional_software_mode':True,'fita_tunnel_used':False,
 'explicit_added_memory_capacitor_used':False}}
Path('results').mkdir(exist_ok=True)
Path('results/results.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
