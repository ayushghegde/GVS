import numpy as np, math, json

# v14S shared-threshold polarized-link cell (STPLC)
# Engineering/model-level screen only. Literature parameters are targets, not a calibrated compact model.
V=0.25
C_NODE=0.20e-15   # v14R extracted 0.152 fF choice node + allowance for one shared threshold element
T_PULSE=20e-9
G_STRONG=7e-9
G_WEAK=0.5e-9
G_LEAK=2e-9
VTH=0.16
TS_I=100e-9
TS_T=12e-9

# One semantic cell: one shared volatile threshold switch; avg five polarized 2-terminal relation links.
# The target receives convergent strong evidence. Distractors receive weak links.
def node_voltage(gsum, t=T_PULSE, c=C_NODE, gleak=G_LEAK):
    gt=gsum+gleak
    vinf=V*gsum/gt
    tau=c/gt
    return vinf*(1-np.exp(-t/tau)), tau

def decision_trial(seed, active_sources=4, targets=5, link_cv=.30, th_sigma=.012, failures=.01, trials=100000):
    r=np.random.default_rng(seed)
    means=np.full((active_sources,targets),G_WEAK); means[:,0]=G_STRONG
    sigma=np.sqrt(np.log1p(link_cv**2))
    mu=np.log(means)-0.5*sigma*sigma
    gs=r.lognormal(mu,sigma,(trials,active_sources,targets))
    dead=r.random(gs.shape)<failures
    gs[dead]=0
    gsum=gs.sum(axis=1)
    gt=gsum+G_LEAK
    vinf=V*gsum/gt
    tau=C_NODE/gt
    vnode=vinf*(1-np.exp(-T_PULSE/tau))
    thresholds=np.clip(r.normal(VTH,th_sigma,(trials,targets)),.10,.24)
    fired=vnode>=thresholds
    score=np.where(fired,vnode,-1)
    winner=np.argmax(score,axis=1)
    success=fired.any(axis=1)&(winner==0)
    false_multi=(fired[:,1:].any(axis=1))
    return {
      'success':float(success.mean()),
      'correct_target_fired':float(fired[:,0].mean()),
      'any_distractor_fired':float(false_multi.mean()),
      'correct_v_mean_V':float(vnode[:,0].mean()),
      'max_distractor_v_mean_V':float(vnode[:,1:].max(axis=1).mean()),
    }

def energy_per_source(active_sources=4, targets=5):
    g_per_source=G_STRONG+(targets-1)*G_WEAK
    link=V*V*g_per_source*T_PULSE
    ts=TS_I*V*TS_T
    node=.5*C_NODE*V*V
    return {'link_fJ_per_source':link*1e15,'link_fJ_4_sources':link*active_sources*1e15,
            'threshold_fJ':ts*1e15,'node_fJ':node*1e15,
            'total_selected_event_fJ':(link*active_sources+ts+node)*1e15}

def robustness_sweep():
    rows=[]
    for cv in (.20,.30,.40,.50):
      for fail in (.0,.01,.03,.05):
        x=decision_trial(14000+int(cv*1000)+int(fail*10000),link_cv=cv,failures=fail,trials=50000)
        x.update({'link_cv':cv,'link_failure':fail}); rows.append(x)
    return rows

def fanin_sweep():
    rows=[]
    for n in (1,2,3,4,5,6):
      x=decision_trial(33000+n,active_sources=n,link_cv=.30,failures=.01,trials=50000)
      v,_=node_voltage(n*G_STRONG)
      rows.append({'active_sources':n,'nominal_correct_node_V':v,**x})
    return rows

def break_even():
    e=energy_per_source()['total_selected_event_fJ']
    rows=[]
    for cff in (5,10,20):
      cmos=cff*1e-15*1.8**2*1e15
      rows.append({'CMOS_effective_switched_C_fF':cff,'CMOS_energy_fJ':cmos,
                   'v14S_event_energy_fJ':e,'energy_ratio_v14S_over_CMOS':e/cmos,
                   'max_v14S_delay_ns_for_equal_EDP':6*cmos/e})
    return rows

def structural():
    degree=5
    return {
      'v14S_per_cell':{'volatile_threshold_devices':1,'polarized_links':degree,'total_two_terminal_devices':1+degree,'MOS_in_semantic_cell':0},
      'lean_MOS_reference_per_cell':{'MOS_threshold_hysteresis':6,'memory_elements':degree,'total_counted_elements':6+degree},
      'v14E_CFN_physical_reference':{'MOS':15,'MIM':2,'note':'different specialized contradiction cell; used as proven transistor-based physical reference, not apples-to-apples semantic cell'},
      'count_reduction_vs_6MOS_plus_5links':1-(1+degree)/(6+degree),
      'chip_4096_cells':{'v14S_two_terminal_devices':4096*(1+degree),'lean_reference_MOS':4096*6,'lean_reference_memory_elements':4096*degree,'MOS_saved_before_shared_periphery':4096*5,'shared_periphery_break_even_MOS_per_cell':5.0,'example_20MOS_driver_per_64_cells_equivalent_MOS_per_cell':20/64},
      'important':'BEOL device footprint, routing, shared program drivers, yield and process masks must be included before area/cost claim.'
    }

def program_window():
    rows=[]
    for mean,sig in ((1.0,.08),(1.0,.12),(1.0,.18)):
      r=np.random.default_rng(88000+int(sig*1000)); vc=np.clip(r.normal(mean,sig,500000),.2,None)
      rows.append({'Vc_mean_V':mean,'Vc_sigma_V':sig,
                   'read_0p25_switch_fraction':float(np.mean(.25>=vc)),
                   'half_0p60_switch_fraction':float(np.mean(.60>=vc)),
                   'selected_1p20_switch_fraction':float(np.mean(1.20>=vc)),
                   'warning':'instantaneous threshold sensitivity only; cumulative half-select fatigue/disturb remains a physical test'})
    return rows

selected=decision_trial(14101,active_sources=4,link_cv=.30,failures=.01,trials=200000)
out={
 'schema':'v14S-shared-threshold-polarized-link-cell-v1',
 'status':'MODEL-LEVEL PARTIAL PASS',
 'central_change':'replace one volatile branch switch per outgoing relation with one shared volatile threshold switch per receiving cell; persistent HZO/FTJ-like two-terminal links carry relation strength.',
 'selected_point':selected,
 'eight_stage_independent_route_success_proxy':selected['success']**8,
 'robustness':robustness_sweep(),
 'fanin':fanin_sweep(),
 'energy':energy_per_source(),
 'break_even':break_even(),
 'structural':structural(),
 'program_window':program_window(),
 'evidence_boundary':'v14R node capacitance is from real SKY130/Magic extraction. v14S link/threshold dynamics and energy are engineering targets; HZO/FTJ and Ag threshold devices are literature-supported classes, not a fabricated combined GVS cell.',
 'decision':'KEEP v14S topology if physical two-terminal link can provide >=10:1 strong/weak read ratio, selected programming without damaging half-selected links, and one shared volatile switch can trigger reliably. DROP per-branch active guided-gap switches from the common cell; retain guided-gap/Ag threshold physics only as the single shared firing junction.'
}
print(json.dumps(out,indent=2))
