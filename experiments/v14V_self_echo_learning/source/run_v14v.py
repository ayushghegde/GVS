import json, math
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
EPS0=8.8541878128e-12
QE=1.602176634e-19


def parse_cap_af(path):
    for line in Path(path).read_text().splitlines():
        if line.startswith('node "TEACH"'):
            return float(line.split()[3])
    raise RuntimeError('TEACH node not found')


def self_tag_screen(n=1_000_000, seed=15001):
    r=np.random.default_rng(seed)
    iw=108.7e-9*np.exp(r.normal(-0.5*0.22**2,0.22,n))
    tw=np.clip(r.normal(8e-9,1.2e-9,n),3e-9,14e-9)
    qw=iw*tw/QE
    il=2.6e-9*np.exp(r.normal(-0.5*0.32**2,0.32,n))
    tl=np.clip(r.normal(8e-9,1.5e-9,n),2e-9,16e-9)
    ql=il*tl/QE
    th=900*np.exp(r.normal(-0.5*0.22**2,0.22,n))
    return {'trials':n,'winner_tag_success':float(np.mean(qw>=th)),'loser_false_tag':float(np.mean(ql>=th)),'winner_charge_e_p0p1':float(np.percentile(qw,0.1)),'loser_charge_e_p99p9':float(np.percentile(ql,99.9)),'threshold_e_p99p9':float(np.percentile(th,99.9)),'threshold_median_e':900.0}


def etg_voltage(rng, n, delay_ns, pulse_ns=30.0, vteach=1.2):
    c=EPS0*25*(12e-9*12e-9)/4e-9
    roff=1e12*np.exp(rng.normal(-0.5*0.28**2,0.28,n))
    gain0=5000*np.exp(rng.normal(-0.5*0.22**2,0.22,n))
    tau=np.clip(rng.normal(180.0,35.0,n),80.0,300.0)
    retained=np.exp(-((delay_ns/tau)**3.2))
    gain=1+(gain0-1)*retained
    rtag=roff/gain
    tp=pulse_ns*1e-9
    tagged=vteach*(1-np.exp(-tp/(rtag*c)))
    untag=vteach*(1-np.exp(-tp/(roff*c)))
    retained_stale=np.exp(-((500.0/tau)**3.2))
    stale_r=roff/(1+(gain0-1)*retained_stale)
    stale=vteach*(1-np.exp(-tp/(stale_r*c)))
    inf=.25*(1-np.exp(-(8e-9)/(roff*c)))
    return tagged,untag,stale,inf,c


def etg_screen(n=1_000_000,seed=15002):
    r=np.random.default_rng(seed)
    tagged,untag,stale,inf,c=etg_voltage(r,n,100.0)
    sweep=[]
    for d in (20,50,80,100,120,160,200,500):
        rr=np.random.default_rng(seed+d)
        t,u,s,i,_=etg_voltage(rr,250_000,float(d))
        sweep.append({'delay_ns':d,'tagged_ge_1V':float(np.mean(t>=1.0)),'tagged_p0p1_V':float(np.percentile(t,.1)),'untagged_p99p9_V':float(np.percentile(u,99.9))})
    return {'trials':n,'hzo_cap_aF':c/1e-18,'delay_ns':100.0,'teach_pulse_ns':30.0,'teach_V':1.2,'roff_median_ohm':1e12,'fresh_gain_median':5000.0,'tagged_ge_1V':float(np.mean(tagged>=1.0)),'untagged_le_0p15V':float(np.mean(untag<=.15)),'stale500_le_0p15V':float(np.mean(stale<=.15)),'inference_only_le_0p30V':float(np.mean(inf<=.30)),'tagged_p0p1_V':float(np.percentile(tagged,.1)),'untagged_p99p9_V':float(np.percentile(untag,99.9)),'stale_p99p9_V':float(np.percentile(stale,99.9)),'delay_sweep':sweep}


def one_learning(seed, feedback_error=.03, method='self', epochs=120, nrel=256,b=6):
    r=np.random.default_rng(seed)
    truth=r.integers(0,b,nrel)
    w=np.full((nrel,b),-.25)
    w[np.arange(nrel),truth]=.82
    rem=r.choice(nrel,nrel//4,replace=False)
    old=truth[rem].copy()
    truth[rem]=(truth[rem]+r.integers(1,b,len(rem)))%b
    recovery=None
    alpha=.18
    noise=.14
    for ep in range(1,epochs+1):
        order=r.permutation(nrel)
        for i in order:
            chosen=int(np.argmax(w[i]+r.normal(0,noise,b)))
            if r.random()>.12: continue
            label=int(truth[i])
            if r.random()<feedback_error:
                label=(label+int(r.integers(1,b)))%b
            if method=='explicit':
                w[i,label]=min(1.0,w[i,label]+alpha)
                if chosen!=label: w[i,chosen]=max(-1.0,w[i,chosen]-alpha)
            elif method=='self':
                if chosen==label: w[i,chosen]=min(1.0,w[i,chosen]+alpha)
                else: w[i,chosen]=max(-1.0,w[i,chosen]-alpha)
            elif method=='corroborated':
                votes=[]
                for _ in range(3):
                    lab=int(truth[i])
                    if r.random()<feedback_error: lab=(lab+int(r.integers(1,b)))%b
                    votes.append(lab)
                maj=int(np.bincount(votes,minlength=b).argmax())
                if chosen==maj: w[i,chosen]=min(1.0,w[i,chosen]+alpha)
                else: w[i,chosen]=max(-1.0,w[i,chosen]-alpha)
        pred=np.argmax(w+r.normal(0,noise,w.shape),axis=1)
        ch=float(np.mean(pred[rem]==truth[rem]))
        if recovery is None and ch>=.90: recovery=ep
    pred=np.argmax(w+r.normal(0,noise,w.shape),axis=1)
    return recovery or epochs+1,float(np.mean(pred==truth)),float(np.mean(pred[rem]==truth[rem])),float(np.mean(pred[rem]==old))


def learning_screen():
    rows=[]
    for err in (.03,.10,.20,.30):
      methods=['explicit','self','corroborated'] if err==.03 else ['self','corroborated']
      for method in methods:
        vals=[one_learning(16000+s,err,method) for s in range(20)]
        rows.append({'feedback_error':err,'method':method,'recovery_epochs_mean':float(np.mean([v[0] for v in vals])),'final_accuracy_mean':float(np.mean([v[1] for v in vals])),'changed_final_accuracy_mean':float(np.mean([v[2] for v in vals])),'obsolete_route_selected_mean':float(np.mean([v[3] for v in vals]))})
    return rows

cap64=parse_cap_af(ROOT/'physical/v14v_teach_mesh_8x8.ext')
cap256=parse_cap_af(ROOT/'physical/v14v_teach_mesh_16x16.ext')
Ccoll=EPS0*25*(12e-9*12e-9)/4e-9
energy=[]
for cells,metal in ((64,cap64),(256,cap256)):
    coll=cells*6*Ccoll
    ctot=metal*1e-18+coll
    direct=ctot*1.2**2*1e15
    energy.append({'cells':cells,'extracted_teach_metal_fF':metal/1000,'estimated_collar_fF':coll/1e-15,'combined_fF':ctot/1e-15,'direct_cycle_fJ':direct,'after_2over3_recovery_fJ':direct/3,'plus_20fJ_launcher_fJ':direct/3+20})

out={'schema':'v14V-self-addressed-polarity-fabric-rerun-v2','status':'PARTIAL PASS','evidence_boundary':{'extracted':'Magic/SKY130A metal2 TEACH meshes only; both rerun meshes DRC=0.','modeled':'self-tag charge, ETG volatile conductance, HZO internal voltage, learning and energy beyond extracted metal.','not_claimed':'No fabricated ETG/FIC/HZO/guided-gap compound device and no pulse-launcher PEX.'},'physical_teach_mesh':{'64_cells':{'drc_errors':0,'cap_fF':cap64/1000,'geometry':'8-run 100um serpentine metal2 proxy'},'256_cells':{'drc_errors':0,'cap_fF':cap256/1000,'geometry':'16-run 200um serpentine metal2 proxy'},'note':'Fresh rerun geometry. It intentionally replaces no historical physical measurement and is lighter than the earlier interrupted proxy.'},'self_tag':self_tag_screen(),'etg':etg_screen(),'learning':learning_screen(),'energy':energy,'decision':{'keep':'activity-as-address remains viable as a model/metal-routing direction','problem':'ETG must physically provide a large but temporary fresh/stale conductance ratio without rewriting HZO','next':'move slow human/teacher interpretation out of the ETG timing window; regenerate physical tags by replay at the thinking layer'}}
(ROOT/'results/results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
