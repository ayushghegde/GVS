import json, math, numpy as np

# v14P4 — quench-node and sparse-hierarchy closure screen.
# Engineering sensitivity model only.
R_ON=2.3e6
V=0.25
DROP_FRACTION=0.20
EPS0=8.8541878128e-12; QE=1.602176634e-19; ER=20
BASE_FOCUS=1.45; GAP_MEAN=1.30; GAP_SIG=.12; BASE_MIG=23.5; BASE_D=2.0; MIG_EXP=1.5

def M_ring(b,R=8,sep=1.5,obs_gap=2):
    c=QE/(4*math.pi*EPS0*ER); M=np.zeros((b,b))
    for i in range(b):
        a=2*math.pi*i/b; u=np.array([math.cos(a),math.sin(a)])
        pp=R*u; pm=(R-sep)*u
        for j in range(b):
            a2=2*math.pi*j/b; v=np.array([math.cos(a2),math.sin(a2)]); obs=(R+obs_gap)*v
            rp=np.linalg.norm(obs-pp)*1e-9; rm=np.linalg.norm(obs-pm)*1e-9
            M[j,i]=c*(1/rp-1/rm)
    return M

def race(b,trials=150000,qt=10,qo=-3,seed=1):
    r=np.random.default_rng(seed); M=M_ring(b); qs=np.full(b,qo,dtype=float); qs[0]=qt
    q=qs[None,:]*np.clip(1+r.normal(0,.15,(trials,b)),.5,1.5); trail=q@M.T
    lv=np.clip(V+trail,.10,.40); focus=BASE_FOCUS*(lv/V)*np.clip(1+r.normal(0,.04,(trials,b)),.75,1.25)
    gap=np.clip(r.normal(GAP_MEAN,GAP_SIG,(trials,b)),.65,None)
    s=np.sqrt(np.log1p(.15**2)); nuc=r.lognormal(np.log(4/np.sqrt(focus))-.5*s*s,s)
    sm=np.sqrt(np.log1p(.13**2)); mig=BASE_MIG*(gap/BASE_D)**MIG_EXP/focus*r.lognormal(-.5*sm*sm,sm,(trials,b))
    d=nuc+mig; order=np.argsort(d,axis=1); win=order[:,0]; margin=d[np.arange(trials),order[:,1]]-d[np.arange(trials),win]
    return win,margin

rows=[]; pwin={}; pquench={}
for b in (4,5,8,16):
    win,margin=race(b,seed=30000+b); pwin[b]=float(np.mean(win==0))
    for Cff in (.5,.75,1,1.5,2,3):
        t=-math.log(1-DROP_FRACTION)*R_ON*Cff*1e-15*1e9
        pq=float(np.mean((win==0)&(margin>=t)))
        rows.append({'branches':b,'choice_node_fF':Cff,'quench_ns':t,'correct_winner':pwin[b],'correct_and_quenched':pq,
                     'choice_node_energy_fJ':.5*Cff*1e-15*V*V*1e15})
        if Cff==1: pquench[b]=pq

hier=[]
for choices,stages in ((16,2),(64,3),(256,4)):
    hier.append({'logical_choices':choices,'four_way_stages':stages,
                 'hierarchical_winner_probability':pwin[4]**stages,
                 'hierarchical_1fF_quench_probability':pquench[4]**stages,
                 'direct_probability_if_screened':pwin.get(choices)})

out={
 'schema':'v14P4-quench-node-sparse-hierarchy-v1',
 'evidence_boundary':'Engineering timing/electrostatic sensitivity model; no extracted v14P choice-node capacitance yet.',
 'quench_rows':rows,
 'sparse_hierarchy':hier,
 'selected_target':{'ordinary_branch_bundle':'4-5 candidates','choice_node_capacitance_target_fF':'<=1 preferred','reason':'keeps first-bridge quench sub-ns with small energy; wide fanout is handled hierarchically/shared relay tissue rather than 16-way local branching'},
 'decision':'KEEP. Physical v14P closure now requires layout/extraction of the choice node + polarized collar around guided-gap tips, then a calibrated polarization/trap device model.'
}
print(json.dumps(out,indent=2))
