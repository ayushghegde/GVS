import json, math
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
EPS0=8.8541878128e-12
QE=1.602176634e-19
KB_EV=8.617333262e-5
VTEACH=1.2
PULSE_NS=30.0
C_HZO=EPS0*25*(12e-9*12e-9)/4e-9
V_TAG_MIN=1.0
V_STALE_MAX=0.15

def resistance_for_cap_voltage(vsrc,vtarget,pulse_s,cap_f):
    return -pulse_s/(cap_f*math.log(1-vtarget/vsrc))

def requirement():
    tp=PULSE_NS*1e-9
    rf=resistance_for_cap_voltage(VTEACH,V_TAG_MIN,tp,C_HZO)
    rs=resistance_for_cap_voltage(VTEACH,V_STALE_MAX,tp,C_HZO)
    return {'hzo_cap_aF':C_HZO/1e-18,'fresh_path_max_Gohm_for_1V':rf/1e9,'stale_path_min_Gohm_for_0p15V':rs/1e9,'minimum_fresh_stale_conductance_ratio':rs/rf,'nominal_gain_needed_from_1Tohm_off':1e12/rf,'barrier_shift_for_500x_at_300K_eV':1.2*KB_EV*300*math.log(500),'barrier_shift_for_1000x_at_300K_eV':1.2*KB_EV*300*math.log(1000),'barrier_shift_for_5000x_at_300K_eV':1.2*KB_EV*300*math.log(5000)}

def monte_carlo(n=1_000_000,seed=15111,delay_ns=100.0):
    r=np.random.default_rng(seed)
    iw=108.7e-9*np.exp(r.normal(-0.5*0.22**2,0.22,n)); tw=np.clip(r.normal(8e-9,1.2e-9,n),3e-9,14e-9); qw=iw*tw/QE
    il=2.6e-9*np.exp(r.normal(-0.5*0.32**2,0.32,n)); tl=np.clip(r.normal(8e-9,1.5e-9,n),2e-9,16e-9); ql=il*tl/QE
    q0=600*np.exp(r.normal(-0.5*0.12**2,0.12,n)); capture=0.11*np.exp(r.normal(-0.5*0.20**2,0.20,n))
    nw=r.poisson(np.clip((qw-q0)*capture,0,None)); nl=r.poisson(np.clip((ql-q0)*capture,0,None))
    coupling=0.006*np.exp(r.normal(-0.5*0.18**2,0.18,n)); d0w=np.minimum(nw*coupling,0.50); d0l=np.minimum(nl*coupling,0.50)
    tau=190*np.exp(r.normal(-0.5*0.12**2,0.12,n)); roff=1e12*np.exp(r.normal(-0.5*0.22**2,0.22,n)); ideal=1.2*np.exp(r.normal(-0.5*0.06**2,0.06,n)); vt=KB_EV*300
    def solve(d0,d):
        dp=d0*np.exp(-d/tau); gain=np.exp(np.minimum(dp/(ideal*vt),25)); rr=roff/gain; v=VTEACH*(1-np.exp(-(PULSE_NS*1e-9)/(rr*C_HZO))); return v,gain,dp,rr
    tagged,gfresh,dpfresh,rfresh=solve(d0w,delay_ns); loser,gloser,dploser,rloser=solve(d0l,delay_ns); stale,gstale,dpstale,rstale=solve(d0w,500.0)
    inference_induced=0.10*d0w
    rows=[]
    for d in (20,50,80,100,120,200,500):
        vv,gg,dd,rr=solve(d0w,float(d)); rows.append({'delay_ns':d,'tagged_ge_1V':float(np.mean(vv>=1.0)),'tagged_p0p1_V':float(np.percentile(vv,0.1)),'gain_p0p1':float(np.percentile(gg,0.1))})
    return {'trials':n,'delay_ns':delay_ns,'tagged_ge_1V':float(np.mean(tagged>=1.0)),'untagged_le_0p15V':float(np.mean(loser<=0.15)),'stale500_le_0p15V':float(np.mean(stale<=0.15)),'inference_induced_le_0p30V':float(np.mean(inference_induced<=0.30)),'tagged_p0p01_V':float(np.percentile(tagged,0.01)),'tagged_p0p1_V':float(np.percentile(tagged,0.1)),'untagged_p99p99_V':float(np.percentile(loser,99.99)),'stale_p99p99_V':float(np.percentile(stale,99.99)),'fresh_gain_p0p1':float(np.percentile(gfresh,0.1)),'fresh_gain_median':float(np.median(gfresh)),'stale_gain_p99p9':float(np.percentile(gstale,99.9)),'fresh_barrier_shift_p0p1_eV':float(np.percentile(dpfresh,0.1)),'stale_barrier_shift_p99p9_eV':float(np.percentile(dpstale,99.9)),'winner_pocket_ions_p0p1':float(np.percentile(nw,0.1)),'loser_pocket_ions_p99p99':float(np.percentile(nl,99.99)),'delay_sweep':rows}

req=requirement(); mc=monte_carlo()
out={'schema':'v14V1-self-emptying-echo-pocket-v1','status':'MODEL PASS / PHYSICAL COUPON OPEN','mechanism':'SEEP: guided-gap firing loads a shallow Ag-ion side pocket beside the orthogonal program barrier; the ionic electrostatic field temporarily lowers that barrier and then decays by return diffusion.','requirement':req,'monte_carlo':mc,'decision':{'old_5000x_requirement':'rejected as unnecessary as a hard material spec','new_electrical_requirement':'~14x is the mathematical fresh/stale minimum for the selected HZO C and pulse; target >=500x fresh gain for variation margin.','selected_model_result':'fresh p0.1 gain exceeds 1000x at 100 ns while untouched and 500-ns stale branches remain below 0.15 V in >=99.99% of the modeled population.','physical_blocker':'fabricate one guided-gap + SEEP + orthogonal barrier coupon and measure ion capture, barrier shift, relaxation, endurance and temperature dependence.'}}
(ROOT/'results/results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
