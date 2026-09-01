import math, json, numpy as np

# v14M deterministic model-level screen. This is not a compact device model.
rng=np.random.default_rng(140016)
G_WEAK=2.5e-9; G_STRONG=25e-9
VREAD=.20; TPULSE=20e-9
N=64; LAYERS=8; TRIALS=1000
N_STRONG=3; N_WEAK=2; N_DISTRACTOR=3
LINK_FAIL=.01; FIRE_FAIL=.01; THRESH_SIGMA=.10; THRESH_FACTOR=.50


def cascade(sig):
    active=np.ones((TRIALS,N),dtype=bool)
    link_E=np.zeros(TRIALS); fire_count=np.zeros(TRIALS)
    for _ in range(1,LAYERS):
        q=np.zeros((TRIALS,N))
        for g,c in ((G_STRONG,N_STRONG),(G_WEAK,N_WEAK)):
            for __ in range(c):
                idx=rng.integers(0,N,size=(TRIALS,N))
                pred=np.take_along_axis(active,idx,axis=1)
                ok=rng.random((TRIALS,N))>LINK_FAIL
                var=np.maximum(0,1+rng.normal(0,sig,size=(TRIALS,N)))
                f=pred&ok
                q += g*VREAD*TPULSE*var*f
                link_E += f.sum(axis=1)*VREAD*VREAD*g*TPULSE
        for __ in range(N_DISTRACTOR):
            bg=(rng.random((TRIALS,N))<.20)&(rng.random((TRIALS,N))>LINK_FAIL)
            var=np.maximum(0,1+rng.normal(0,sig,size=(TRIALS,N)))
            q += G_WEAK*VREAD*TPULSE*var*bg
            link_E += bg.sum(axis=1)*VREAD*VREAD*G_WEAK*TPULSE
        qnom=(N_STRONG*G_STRONG+N_WEAK*G_WEAK)*VREAD*TPULSE
        th=qnom*THRESH_FACTOR*np.maximum(.65,1+rng.normal(0,THRESH_SIGMA,size=(TRIALS,N)))
        active=(q>=th)&(rng.random((TRIALS,N))>FIRE_FAIL)
        fire_count += active.sum(axis=1)
    finals=active.mean(axis=1)
    epf=np.divide(link_E,fire_count,out=np.zeros_like(link_E),where=fire_count>0)*1e15
    return dict(read_sigma=sig,mean_final_active=float(finals.mean()),p05=float(np.quantile(finals,.05)),minimum=float(finals.min()),mean_link_read_fJ_per_fire=float(epf.mean()))

rows=[cascade(s) for s in (.10,.20,.30,.40)]

# Background-only false-fire screen.
SAMPLES=1_000_000
q=np.zeros(SAMPLES)
for _ in range(N_DISTRACTOR):
    bg=rng.random(SAMPLES)<.20
    var=np.maximum(0,1+rng.normal(0,.30,size=SAMPLES))
    q += G_WEAK*VREAD*TPULSE*var*bg
qnom=(N_STRONG*G_STRONG+N_WEAK*G_WEAK)*VREAD*TPULSE
th=qnom*THRESH_FACTOR*np.maximum(.65,1+rng.normal(0,THRESH_SIGMA,size=SAMPLES))
false_fires=int(np.count_nonzero(q>=th))

# Energy-delay sensitivity.
VTH=.25; ICOMP=100e-9; OVERHEAD_FJ=1.5; CMOS_VDD=1.8; CMOS_DELAY_NS=6.0
linkE=[r['mean_link_read_fJ_per_fire'] for r in rows if r['read_sigma']==.20][0]
per_ns=VTH*ICOMP*1e-9*1e15
fixed=OVERHEAD_FJ+linkE
sweep=[]
for delay_ns in (10,20,30,40,50,55,62,75,100,250,1000,10000):
    total=per_ns*delay_ns+fixed
    r=dict(delay_ns=delay_ns,total_fJ=total)
    for cff in (5,10,20):
        ecmos=cff*CMOS_VDD**2
        r[f'energy_ratio_vs_{cff}fF']=total/ecmos
        r[f'edp_ratio_vs_{cff}fF']=total*delay_ns/(ecmos*CMOS_DELAY_NS)
    sweep.append(r)

break_even={}
for cff in (5,10,20):
    rhs=(cff*CMOS_VDD**2)*CMOS_DELAY_NS
    t=(-fixed+math.sqrt(fixed*fixed+4*per_ns*rhs))/(2*per_ns)
    break_even[str(cff)]=t

out={'cascade':rows,'background_false_fires':false_fires,'energy_delay_sweep':sweep,'edp_break_even_delay_ns':break_even}
print(json.dumps(out,indent=2))
