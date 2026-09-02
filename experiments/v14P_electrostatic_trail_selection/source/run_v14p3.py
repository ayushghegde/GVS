import json, math, numpy as np

# v14P3: integrate the polarized trail directly into v14O guided-gap firing.
# Engineering sensitivity model only; not calibrated device physics.
rng=np.random.default_rng(140203)
EPS0=8.8541878128e-12
QE=1.602176634e-19
ER=20.0
V_FIRE=.25
BASE_FOCUS=1.45
GAP_MEAN=1.30
GAP_SIG=.12
BASE_MIG=23.5
BASE_D=2.0
MIG_EXP=1.5


def lognormal(mean,cv,shape):
    s2=np.log1p(cv*cv)
    return rng.lognormal(np.log(mean)-s2/2,np.sqrt(s2),shape)


def dipole_ring_matrix(branches,R_nm=8.0,sep_nm=1.5,gap_obs_nm=2.0):
    # + trap is at the branch collar, compensating - trap sits sep_nm inward.
    const=QE/(4*math.pi*EPS0*ER)
    M=np.zeros((branches,branches))
    for i in range(branches):
        a=2*math.pi*i/branches; u=np.array([math.cos(a),math.sin(a)])
        pp=R_nm*u; pm=(R_nm-sep_nm)*u
        for j in range(branches):
            b=2*math.pi*j/branches; v=np.array([math.cos(b),math.sin(b)])
            obs=(R_nm+gap_obs_nm)*v
            rp=np.linalg.norm(obs-pp)*1e-9; rm=np.linalg.norm(obs-pm)*1e-9
            M[j,i]=const*(1/rp-1/rm)
    return M


def guided_gap_race(branches=5,R_nm=8,q_target=10.0,q_other=-3.0,trials=50000,seed=1):
    local=np.random.default_rng(seed)
    M=dipole_ring_matrix(branches,R_nm)
    qs=np.full(branches,q_other); qs[0]=q_target
    nominal=M@qs
    qtrial=qs[None,:]*np.clip(1+local.normal(0,.15,(trials,branches)),.5,1.5)
    trail=qtrial@M.T
    lv=np.clip(V_FIRE+trail,.10,.40)
    focus=BASE_FOCUS*(lv/V_FIRE)*np.clip(1+local.normal(0,.04,(trials,branches)),.75,1.25)
    gap=np.clip(local.normal(GAP_MEAN,GAP_SIG,(trials,branches)),.65,None)
    s2=np.log1p(.15*.15)
    nuc=local.lognormal(np.log(4/np.sqrt(focus))-s2/2,np.sqrt(s2))
    s2m=np.log1p(.13*.13)
    mig=BASE_MIG*(gap/BASE_D)**MIG_EXP/focus*local.lognormal(-s2m/2,np.sqrt(s2m),(trials,branches))
    d=nuc+mig
    order=np.argsort(d,axis=1); win=order[:,0]
    first=d[np.arange(trials),win]; second=d[np.arange(trials),order[:,1]]
    return {
      'branches':branches,'R_nm':R_nm,'q_target_eff_e':q_target,'q_other_eff_e':q_other,
      'correct_winner':float(np.mean(win==0)),
      'correct_with_1ns_quench_margin':float(np.mean((win==0)&((second-first)>=1))),
      'target_delay_mean_ns':float(d[:,0].mean()),
      'winner_delay_mean_ns':float(first.mean()),
      'median_first_second_margin_ns':float(np.median(second-first)),
      'nominal_target_trail_mV':float(nominal[0]*1e3),
      'max_wrong_abs_trail_mV':float(np.max(np.abs(nominal[1:]))*1e3),
      'local_dipole_mV_per_e':float(M[0,0]*1e3),
      'max_cross_mV_per_e':float(np.max(np.abs(M[0,1:]))*1e3)
    }


def electrostatic_compare():
    out=[]
    for dx in (0,3,5,7,10):
        y=2.0; sep=1.5
        const=QE/(4*math.pi*EPS0*ER)
        r=math.hypot(dx,y)*1e-9
        mono=const/r
        rp=math.hypot(dx,y)*1e-9; rm=math.hypot(dx,y+sep)*1e-9
        dip=const*(1/rp-1/rm)
        out.append({'lateral_nm':dx,'monopole_mV_per_e':mono*1e3,'dipole_mV_per_e':dip*1e3})
    return out


def relearn_cycles(seed=1,evidence_per_update=3,updates=3,cycles=12):
    local=np.random.default_rng(seed); n=512; b=5
    truth=local.integers(0,b,n); state=np.full((n,b),-.25); state[np.arange(n),truth]=1.0
    ever=np.zeros(n,bool); rows=[]
    for cyc in range(cycles):
        rem=local.choice(n,int(.2*n),replace=False); ever[rem]=True; old=truth[rem].copy()
        for x in rem: truth[x]=local.choice([k for k in range(b) if k!=truth[x]])
        for _ in range(updates):
            for x in rem:
                votes=[]
                for __ in range(evidence_per_update):
                    ft=truth[x]
                    if local.random()<.03: ft=local.choice([k for k in range(b) if k!=truth[x]])
                    votes.append(ft)
                ft=int(np.argmax(np.bincount(votes,minlength=b)))
                c=int(np.argmax(state[x]+local.normal(0,.20,b)))
                if local.random()>.05: state[x,ft]=np.clip(state[x,ft]+.65,-1,1)
                if c!=ft and local.random()>.05: state[x,c]=np.clip(state[x,c]-.65,-1,1)
        pred=np.argmax(state+local.normal(0,.20,state.shape),axis=1)
        never=~ever
        rows.append({'cycle':cyc+1,'overall':float(np.mean(pred==truth)),
                     'changed_now':float(np.mean(pred[rem]==truth[rem])),
                     'old_selected_now':float(np.mean(pred[rem]==old)),
                     'never_changed':float(np.mean(pred[never]==truth[never])) if np.any(never) else None})
    return rows


def retention_refresh():
    scales=np.linspace(0,1,11); probs=[]
    for i,s in enumerate(scales):
        r=guided_gap_race(branches=5,R_nm=8,q_target=10*s,q_other=-3*s,trials=12000,seed=8100+i)
        probs.append(r['correct_winner'])
    rows=[]
    for tau in (1,2,5,20):
        for days in (7,30,180,365,730):
            local=np.random.default_rng(int(10000+tau*100+days)); amp=np.ones(5000); dt=days/365.25
            acc=[]; steps=max(1,int(10*365.25/days)); decay=math.exp(-dt/tau)
            for _ in range(steps):
                amp*=decay
                p=np.interp(np.clip(amp,0,1),scales,probs)
                ok=local.random(amp.size)<p; acc.append(float(ok.mean()))
                amp[ok]=1.0
            rows.append({'tau_years':tau,'query_interval_days':days,
                         'mean_query_accuracy':float(np.mean(acc)),
                         'last_query_accuracy':float(acc[-1]),'mean_final_trail':float(amp.mean())})
    return {'scale_curve':[{'remaining_trail':float(s),'winner':float(p)} for s,p in zip(scales,probs)],'rows':rows}

fan=[]
for b in (4,5,8,12,16): fan.append(guided_gap_race(branches=b,R_nm=8,trials=50000,seed=7000+b))

C_floor=EPS0*ER*(10e-9*10e-9)/(5e-9)
collar_floor={'parallel_plate_floor_F':C_floor,'one_volt_stored_energy_J':.5*C_floor,
              'one_volt_charge_electrons':C_floor/QE,
              'warning':'geometric electrostatic floor only; excludes trap injection, losses, drivers, selectors and material switching energy'}

rel=[]
for seed in range(20): rel.append(relearn_cycles(seed=9000+seed))
rel_agg=[]
for c in range(12):
    rel_agg.append({'cycle':c+1,
                    'overall_mean':float(np.mean([x[c]['overall'] for x in rel])),
                    'changed_now_mean':float(np.mean([x[c]['changed_now'] for x in rel])),
                    'old_selected_mean':float(np.mean([x[c]['old_selected_now'] for x in rel])),
                    'never_changed_mean':float(np.mean([x[c]['never_changed'] for x in rel if x[c]['never_changed'] is not None]))})

out={
 'schema':'v14P3-polarized-trail-guided-gap-integration-v1',
 'evidence_boundary':'Engineering electrostatic + guided-gap sensitivity model only; no calibrated trap/ferroelectric compact model or fabricated v14P device.',
 'physical_interpretation':'polarized trail collar around each v14O guided-gap branch tip; local polarization biases transient bridge formation. The first bridge discharges/quench-biases the source node.',
 'electrostatic_compare':electrostatic_compare(),
 'guided_gap_fanout':fan,
 'relearning_12_cycles':rel_agg,
 'retention_with_confirmation_refresh':retention_refresh(),
 'collar_electrostatic_floor':collar_floor,
 'decision':'KEEP polarized trail collar integrated with v14O guided-gap firing. Use traffic only as eligibility; consolidation/reversal must be confirmation/contradiction gated. Prefer ~4-5 ordinary candidate branches; wider fanout needs hierarchy or additional competition.'
}
print(json.dumps(out,indent=2))
