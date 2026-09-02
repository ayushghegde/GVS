import json, math, numpy as np
from pathlib import Path

# Neural Glyph v14R combined closure screen.
# Evidence boundaries:
# - choice-node capacitance is parsed from a real Magic/SKY130 extraction generated in this experiment.
# - guided-gap branch race and learning are engineering sensitivity/Monte Carlo models, not calibrated device physics.
# - HZO collar capacitance/polarization calculations are electrostatic geometry targets, not fabricated GVS measurements.

EPS0=8.8541878128e-12
QE=1.602176634e-19
ER_TRAIL=20.0
R_ON=2.3e6
V_FIRE=.25
DROP=.20
BASE_FOCUS=1.45
GAP_MEAN=1.30
GAP_SIG=.12
BASE_MIG=23.5
BASE_D=2.0
MIG_EXP=1.5

ROOT=Path(__file__).resolve().parents[1]
EXT=ROOT/'physical'/'v14r_choice5_m2.ext'


def parse_choice_cap_af(path: Path):
    # Magic .ext uses attofarad capacitance units for this technology output.
    text=path.read_text()
    own=None; couplings=[]
    for line in text.splitlines():
        if line.startswith('node "CHOICE"'):
            parts=line.split()
            # node "CHOICE" Rscale Cscale x y layer
            own=float(parts[3])
        elif line.startswith('cap ') and '"CHOICE"' in line:
            parts=line.split()
            couplings.append(float(parts[-1]))
    if own is None:
        raise RuntimeError('CHOICE node not found')
    return own, couplings, own+sum(couplings)


def M_ring(b,R=8,sep=1.5,obs_gap=2):
    c=QE/(4*math.pi*EPS0*ER_TRAIL); M=np.zeros((b,b))
    for i in range(b):
        a=2*math.pi*i/b; u=np.array([math.cos(a),math.sin(a)])
        pp=R*u; pm=(R-sep)*u
        for j in range(b):
            a2=2*math.pi*j/b; v=np.array([math.cos(a2),math.sin(a2)]); obs=(R+obs_gap)*v
            rp=np.linalg.norm(obs-pp)*1e-9; rm=np.linalg.norm(obs-pm)*1e-9
            M[j,i]=c*(1/rp-1/rm)
    return M


def race(b=5,trials=80000,qt=10,qo=-3,seed=1):
    r=np.random.default_rng(seed); M=M_ring(b); qs=np.full(b,qo,dtype=float); qs[0]=qt
    q=qs[None,:]*np.clip(1+r.normal(0,.15,(trials,b)),.5,1.5); trail=q@M.T
    lv=np.clip(V_FIRE+trail,.10,.40); focus=BASE_FOCUS*(lv/V_FIRE)*np.clip(1+r.normal(0,.04,(trials,b)),.75,1.25)
    gap=np.clip(r.normal(GAP_MEAN,GAP_SIG,(trials,b)),.65,None)
    s=np.sqrt(np.log1p(.15**2)); nuc=r.lognormal(np.log(4/np.sqrt(focus))-.5*s*s,s)
    sm=np.sqrt(np.log1p(.13**2)); mig=BASE_MIG*(gap/BASE_D)**MIG_EXP/focus*r.lognormal(-.5*sm*sm,sm,(trials,b))
    d=nuc+mig; order=np.argsort(d,axis=1); win=order[:,0]
    first=d[np.arange(trials),win]; second=d[np.arange(trials),order[:,1]]
    return {
        'correct_winner':float(np.mean(win==0)),
        'margins_ns':second-first,
        'winner_delay_mean_ns':float(first.mean()),
        'target_delay_mean_ns':float(d[:,0].mean()),
        'nominal_target_trail_mV':float((M@qs)[0]*1e3),
        'max_wrong_abs_trail_mV':float(np.max(np.abs((M@qs)[1:]))*1e3),
    }


def noisy_feedback_screen():
    rows=[]
    for err in (0.03,0.10,0.20,0.30):
        for mode in ('raw','corroborated'):
            vals=[]
            for seed in range(30):
                vals.append(uet_trial(97000+seed,with_elig=True,feedback_error=err,corroborate=(mode=='corroborated')))
            rows.append({
                'feedback_error_probability':err,
                'mode':mode,
                'recovery_encounters_mean':float(np.mean([x[0] for x in vals])),
                'final_accuracy_mean':float(np.mean([x[1] for x in vals])),
                'changed_final_accuracy_mean':float(np.mean([x[2] for x in vals])),
                'obsolete_route_selected_mean':float(np.mean([x[3] for x in vals])),
                'evidence_samples_per_feedback':3 if mode=='corroborated' else 1,
            })
    return rows


def finite_dipole_patch_voltage(P=0.16,size_nm=10.0,near_nm=1.0,sep_nm=1.5,er=20.0,n=220):
    # Finite square bound-charge dipole sheet. This includes the compensating opposite sheet,
    # but not explicit metal-electrode screening; it is therefore an electrostatic upper-envelope geometry test.
    y=(np.arange(n)+0.5)/n*size_nm*1e-9-size_nm*1e-9/2
    Y,Z=np.meshgrid(y,y,indexing='ij')
    dA=(size_nm*1e-9/n)**2
    r1=np.sqrt((near_nm*1e-9)**2+Y*Y+Z*Z)
    r2=np.sqrt(((near_nm+sep_nm)*1e-9)**2+Y*Y+Z*Z)
    return float(np.sum(P*dA/(4*math.pi*EPS0*er)*(1/r1-1/r2)))


def fringe_geometry_screen():
    target_v=(M_ring(5)@np.array([10.,-3.,-3.,-3.,-3.]))[0]
    rows=[]
    for P in (0.085,0.16,0.22,0.26):
        for size in (5.0,7.5,10.0):
            for near in (0.5,1.0,1.5,2.0,3.0):
                v=finite_dipole_patch_voltage(P,size,near)
                rows.append({
                    'P_C_m2':P,'patch_size_nm':size,'near_edge_nm':near,
                    'finite_dipole_fringe_V_before_metal_screening':v,
                    'v14P_nominal_target_trail_V':float(target_v),
                    'required_retained_fraction_after_additional_screening':float(target_v/v) if v else None
                })
    return rows


def programming_window_screen():
    # Sensitivity-only threshold window around a literature-scale ~1 V coercive voltage for 5 nm HZO.
    # Real FE switching is pulse-width/domain dependent; this is not a compact FE model.
    rows=[]
    for sigma in (0.08,0.12,0.18):
        r=np.random.default_rng(44000+int(sigma*1000))
        vc=np.clip(r.normal(1.0,sigma,300000),0.2,None)
        rows.append({
          'assumed_Vc_mean_V':1.0,'assumed_Vc_sigma_V':sigma,
          'read_0p25_above_threshold_fraction':float(np.mean(.25>=vc)),
          'half_select_0p60_above_threshold_fraction':float(np.mean(.60>=vc)),
          'selected_1p20_above_threshold_fraction':float(np.mean(1.20>=vc)),
          'warning':'threshold-only sensitivity; ignores pulse width, domain nucleation, cumulative disturb and imprint'
        })
    return rows

def hzo_screen():
    # Literature-informed bracket; values are not GVS device measurements.
    area=(10e-9)**2
    t=5e-9
    k=25.0
    C=EPS0*k*area/t
    rows=[]
    for P in (0.085,0.16,0.22,0.26):
        q=P*area/QE
        rows.append({
            'remanent_polarization_C_m2':P,
            'bound_charge_e_on_10x10nm':q,
            'fraction_needed_for_10e_effective':10/q,
            'unscreened_field_MV_m_for_k25':P/(EPS0*k)/1e6,
            'unscreened_1p3nm_voltage_V':P/(EPS0*k)*1.3e-9,
        })
    return C,rows


def uet_trial(seed,elig_gain=1.2,elig_inference_leak=0.0,with_elig=True,feedback_error=.03,corroborate=False):
    # Continual remap model. One encounter means one opportunity per relation.
    # UET changes learning sensitivity only unless inference_leak > 0.
    r=np.random.default_rng(seed); n=256; b=5
    truth=r.integers(0,b,n)
    state=np.full((n,b),-.35); state[np.arange(n),truth]=.85
    elig=np.zeros((n,b))
    feedback_p=.12; alpha=.12; decay=.92; noise=.18
    rem=r.choice(n,int(.25*n),replace=False)
    old=truth[rem].copy()
    truth[rem]=(truth[rem]+r.integers(1,b,len(rem)))%b
    recovery=None
    rows=np.arange(n)
    for encounter in range(1,301):
        elig*=decay
        scores=state + elig_inference_leak*(elig/(1+elig)) + r.normal(0,noise,state.shape)
        chosen=np.argmax(scores,axis=1)
        elig[rows,chosen]+=1.0
        fb=r.random(n)<feedback_p
        idx=np.flatnonzero(fb)
        if len(idx):
            target=truth[idx].copy()
            # Teaching/confirmation exposes the intended branch during the update event.
            elig[idx,target]+=0.5
            if corroborate:
                # Three independent noisy labels; majority is the v14K-style provisional/corroboration proxy.
                labels=np.tile(target[:,None],(1,3))
                for j in range(3):
                    wrong=r.random(len(idx))<feedback_error
                    labels[wrong,j]=(labels[wrong,j]+r.integers(1,b,wrong.sum()))%b
                target=np.array([np.bincount(row,minlength=b).argmax() for row in labels])
            else:
                wrong=r.random(len(idx))<feedback_error
                if wrong.any():
                    target[wrong]=(target[wrong]+r.integers(1,b,wrong.sum()))%b
            chosen_fb=chosen[idx]
            prog=r.random(len(idx))>.05
            ip=idx[prog]; tp=target[prog]
            if len(ip):
                gain=(1+elig_gain*elig[ip,tp]/(1+elig[ip,tp])) if with_elig else np.ones(len(ip))
                state[ip,tp]=np.clip(state[ip,tp]+alpha*gain,-1,1)
            depress=(chosen_fb!=target)&(r.random(len(idx))>.05)
            im=idx[depress]; cm=chosen_fb[depress]
            if len(im):
                gain=(1+elig_gain*elig[im,cm]/(1+elig[im,cm])) if with_elig else np.ones(len(im))
                state[im,cm]=np.clip(state[im,cm]-alpha*gain,-1,1)
        if encounter%5==0:
            pred=np.argmax(state+r.normal(0,noise,state.shape),axis=1)
            changed_acc=float(np.mean(pred[rem]==truth[rem]))
            if recovery is None and changed_acc>=.90:
                recovery=encounter
    pred=np.argmax(state+r.normal(0,noise,state.shape),axis=1)
    return recovery or 301, float(np.mean(pred==truth)), float(np.mean(pred[rem]==truth[rem])), float(np.mean(pred[rem]==old))


def uet_screen():
    rows=[]
    for leak in (0.0,0.02,0.05,0.10,0.20,0.40):
        base=[]; uet=[]
        for seed in range(40):
            base.append(uet_trial(91000+seed,with_elig=False,elig_inference_leak=0.0))
            uet.append(uet_trial(91000+seed,with_elig=True,elig_inference_leak=leak))
        br=np.array([x[0] for x in base]); ur=np.array([x[0] for x in uet])
        rows.append({
            'uet_inference_leak':leak,
            'baseline_recovery_encounters_mean':float(br.mean()),
            'uet_recovery_encounters_mean':float(ur.mean()),
            'recovery_improvement_fraction':float((br.mean()-ur.mean())/br.mean()),
            'baseline_final_accuracy_mean':float(np.mean([x[1] for x in base])),
            'uet_final_accuracy_mean':float(np.mean([x[1] for x in uet])),
            'uet_changed_final_accuracy_mean':float(np.mean([x[2] for x in uet])),
            'uet_obsolete_route_selected_mean':float(np.mean([x[3] for x in uet])),
        })
    return rows


own,couplings,total_af=parse_choice_cap_af(EXT)
C_hzo,hzo=hzo_screen()
C_choice=total_af*1e-18
C_total=C_choice+5*C_hzo
quench_ns=-math.log(1-DROP)*R_ON*C_total*1e9
node_energy_fj=.5*C_total*V_FIRE*V_FIRE*1e15

# Polarity/race screen: translate a nominal 0.16 C/m2 HZO patch into an effective-charge fraction.
Pnom=.16; qbound=Pnom*(10e-9)**2/QE
race_rows=[]
for frac in (.03,.05,.075,.10,.125,.15,.20):
    qt=qbound*frac
    qo=-.30*qt
    rr=race(5,qt=qt,qo=qo,seed=15000+int(frac*1000))
    pq=float(np.mean((rr['margins_ns']>=quench_ns)))
    # correct+quench requires correct winner and sufficient margin; rerun same arrays unavailable, approximate separately is wrong.
    # To avoid inventing, rerun exact race internals with helper below.
    r=np.random.default_rng(25000+int(frac*1000)); b=5; M=M_ring(b); qs=np.full(b,qo); qs[0]=qt
    q=qs[None,:]*np.clip(1+r.normal(0,.15,(80000,b)),.5,1.5); trail=q@M.T
    lv=np.clip(V_FIRE+trail,.10,.40); focus=BASE_FOCUS*(lv/V_FIRE)*np.clip(1+r.normal(0,.04,(80000,b)),.75,1.25)
    gap=np.clip(r.normal(GAP_MEAN,GAP_SIG,(80000,b)),.65,None)
    s=np.sqrt(np.log1p(.15**2)); nuc=r.lognormal(np.log(4/np.sqrt(focus))-.5*s*s,s)
    sm=np.sqrt(np.log1p(.13**2)); mig=BASE_MIG*(gap/BASE_D)**MIG_EXP/focus*r.lognormal(-.5*sm*sm,sm,(80000,b))
    d=nuc+mig; order=np.argsort(d,axis=1); win=order[:,0]; first=d[np.arange(80000),win]; second=d[np.arange(80000),order[:,1]]
    exact=float(np.mean((win==0)&((second-first)>=quench_ns)))
    race_rows.append({
        'fringe_fraction_of_bound_charge':frac,
        'effective_target_charge_e':qt,
        'effective_contradicted_charge_e':qo,
        'correct_winner':float(np.mean(win==0)),
        'correct_and_quenched':exact,
        'quench_ns':quench_ns,
    })

uet=uet_screen()
noisy=noisy_feedback_screen()
fringe=fringe_geometry_screen()
program_window=programming_window_screen()

# Architecture comparison uses recorded v14 evidence, not a new physical measurement.
comparison=[
 {'family':'v14J SPCL','cell_parts':'temporary semantic node + programmable capacitive links','strength':'clean two-terminal reversible weight concept; real fixed-MIM floor','blocker':'trainable memcapacitor/program-voltage/periphery not closed','v14R_use':'retain reversible polarity learning rule, not large link capacitance'},
 {'family':'v14L QVC/VRS','cell_parts':'membrane capacitor + leak + volatile release switch + plastic links','strength':'explicit integration/regeneration','blocker':'more parts; VRS energy/device still unknown','v14R_use':'reject dedicated membrane/VRS in common choice cell'},
 {'family':'v14M BDJ','cell_parts':'volatile BDJ instance + nonvolatile BDJ link instances','strength':'simple two-terminal device family, low modeled event energy','blocker':'same stack not closed across volatile/nonvolatile regimes; separate instances','v14R_use':'retain two-terminal diffusive firing principle'},
 {'family':'v14N SN-BDJ','cell_parts':'seeded diffusive junctions + sparse regeneration','strength':'field-focused nucleation and sparse transport','blocker':'speed target remained model envelope','v14R_use':'retain pre-guided/field-focused bridge idea'},
 {'family':'v14O GG-SLDJ','cell_parts':'guided gap + inert spine + passive ballast','strength':'~11.85ns modeled firing, intrinsic compliance, ~1.90fJ proxy','blocker':'no fabricated/calibrated compact model','v14R_use':'KEEP as firing core'},
 {'family':'v14P PTC','cell_parts':'v14O branch + local reversible polarization collar + tiny shared choice node','strength':'physics selects branch; reversible route memory separated from volatile bridge','blocker':'collar device not physically closed; choice C previously unextracted','v14R_use':'KEEP; choice C is now extracted and closes strongly'},
 {'family':'v14Q UET','cell_parts':'temporary usage-eligibility state beside PTC','strength':'faster correction/relearning in model','blocker':'bad if it adds a device or leaks strongly into inference','v14R_use':'KEEP only as shallow state in same collar and learning-only bias'},
]

out={
 'schema':'v14R-polarity-guided-choice-cell-v1',
 'evidence_boundary':{
   'extracted':'Magic/SKY130 five-way metal2 branch-mouth DRC/extraction only.',
   'modeled':'guided-gap race, HZO electrostatic conversion, UET learning, and energy/timing beyond metal parasitics are engineering models.',
   'not_claimed':'No fabricated HZO collar or GG-SLDJ; no calibrated compact model; no full post-layout v14R device.'
 },
 'physical_choice_node':{
   'choice_self_cap_aF':own,
   'choice_branch_couplings_aF':couplings,
   'choice_total_extracted_aF':total_af,
   'choice_total_extracted_fF':total_af/1000,
   'drc_errors':0,
 },
 'hzo_polarity_collar':{
   'geometry_nm':'10x10 area, 5 nm thickness, k=25 engineering target',
   'estimated_capacitance_aF_each':C_hzo/1e-18,
   'five_collar_added_cap_aF':5*C_hzo/1e-18,
   'polarization_bracket':hzo,
   'nominal_0p16C_m2_bound_charge_e':qbound,
   'finite_patch_fringe_screen':fringe,
   'programming_window_sensitivity':program_window,
   'proposed_learning_drive':'rare differential coincidence: +0.6 V at one terminal and -0.6 V at the other -> 1.2 V selected; <=0.6 V half-select; ~0.25 V inference'
 },
 'combined_choice_node':{
   'extracted_metal_plus_estimated_five_collar_fF':C_total/1e-15,
   '20pct_quench_ns_at_2p3Mohm':quench_ns,
   'stored_energy_fJ_at_0p25V':node_energy_fj,
 },
 'polarity_branch_race':race_rows,
 'usage_eligibility_screen':uet,
 'uet_noisy_feedback_screen':noisy,
 'architecture_comparison':comparison,
 'decision':{
   'cell':'v14R Polarity-Guided Choice Cell (PGCC)',
   'keep':['v14O guided-gap volatile bridge','v14O passive self-ballast','v14P local reversible electric-polarity collar','five-way sub-fF shared Choice Node','v14K confirmation/contradiction + provisional self-test','v14Q UET only if co-located as a shallow collar state and kept out of inference selection'],
   'drop':['literal magnetic attraction/electromagnet learning','dedicated membrane capacitor in the ordinary choice cell','separate VRS release device','forcing one filament to be both fast volatile firing and long-retention memory','per-branch MOS selector/compliance','standalone UET device'],
 }
}
(ROOT/'results'/'results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
