import json, math, numpy as np

def branch_mc(n=120000, branches=5, vread=.22, vth0=.25, vth_sigma=.016,
              q_target=5.0, q_other=-1.0, shift_per_q=.012,
              q_sigma=.25, crosstalk=.15, noise_v=.004, seed=123):
    rng=np.random.default_rng(seed)
    q=np.full((n,branches),float(q_other))
    q[:,0]=q_target
    q*=np.clip(1+rng.normal(0,q_sigma,q.shape),.3,1.7)
    mean_other=(q.sum(axis=1,keepdims=True)-q)/(branches-1)
    shift=shift_per_q*(q+crosstalk*mean_other)
    vth=vth0+rng.normal(0,vth_sigma,q.shape)-shift
    margin=vread+rng.normal(0,noise_v,q.shape)-vth
    winner=np.argmax(margin,axis=1)
    return {
      "winner_correct":float(np.mean(winner==0)),
      "target_above_threshold":float(np.mean(margin[:,0]>0)),
      "any_wrong_above_threshold":float(np.mean(np.any(margin[:,1:]>0,axis=1))),
      "clean_target_only":float(np.mean((margin[:,0]>0)&~np.any(margin[:,1:]>0,axis=1)))
    }

def learning_run(rule, seed, n_nodes=128, n_branches=6, warm=12000, adapt=8000):
    rng=np.random.default_rng(seed)
    truth=rng.integers(0,n_branches,n_nodes)
    q=np.zeros((n_nodes,n_branches))
    kv=.012*np.clip(1+rng.normal(0,.2,q.shape),.5,1.5)
    g=np.clip(1+rng.normal(0,.08,q.shape),.6,1.4)
    slope=.035; eta=.55; fail=.05; cross=.08; leak=.99997

    def choose(n):
        others=(q[n].sum()-q[n])/(n_branches-1)
        shift=kv[n]*(q[n]+cross*others)
        score=np.log(g[n])+shift/slope+rng.normal(0,.18,n_branches)
        return int(np.argmax(score))
    def update(n,c,t):
        q[n]*=leak
        if rule=="use_only":
            if rng.random()>fail:q[n,c]+=eta
        elif rule=="confirm_only":
            if rng.random()>fail:q[n,t]+=eta
        elif rule=="reversible":
            if rng.random()>fail:q[n,t]+=eta
            if c!=t and rng.random()>fail:q[n,c]-=eta
        q[n]=np.clip(q[n],-4,8)

    for _ in range(warm):
        n=int(rng.integers(n_nodes)); c=choose(n); update(n,c,int(truth[n]))
    pre=np.mean([choose(n)==truth[n] for n in range(n_nodes) for _ in range(5)])

    rem=rng.choice(n_nodes,int(.25*n_nodes),replace=False)
    old=truth.copy()
    for n in rem:
        opts=[b for b in range(n_branches) if b!=truth[n]]
        truth[n]=rng.choice(opts)

    windows=[500,2000,8000]; snaps={}; wi=0
    for t in range(adapt):
        n=int(rng.choice(rem)) if rng.random()<.6 else int(rng.integers(n_nodes))
        c=choose(n); update(n,c,int(truth[n]))
        if wi<len(windows) and t+1==windows[wi]:
            cur=[]; oldsel=[]
            for n2 in rem:
                for _ in range(5):
                    ch=choose(int(n2)); cur.append(ch==truth[int(n2)]); oldsel.append(ch==old[int(n2)])
            snaps[str(t+1)]={"new_relation_accuracy":float(np.mean(cur)),
                             "old_relation_selection":float(np.mean(oldsel))}
            wi+=1
    return {"pre_accuracy":float(pre),
            "remapped_final_accuracy":float(snaps["8000"]["new_relation_accuracy"]),
            "snapshots":snaps}

def stress():
    rows=[]
    for branches in (4,8,16):
      for sig in (.008,.012,.016,.020):
        x=branch_mc(n=40000,branches=branches,vth_sigma=sig,crosstalk=.30,
                    q_target=5,q_other=-1,q_sigma=.25,seed=1000+branches+int(sig*1000))
        rows.append({"branches":branches,"threshold_sigma_V":sig,**x})
    return rows

if __name__=="__main__":
    learn={}
    for rule in ("use_only","confirm_only","reversible"):
        rr=[learning_run(rule,1400+s) for s in range(6)]
        learn[rule]={
          "pre_accuracy_mean":float(np.mean([x["pre_accuracy"] for x in rr])),
          "remapped_final_accuracy_mean":float(np.mean([x["remapped_final_accuracy"] for x in rr])),
          "adaptation_mean":{
            w:float(np.mean([x["snapshots"][w]["new_relation_accuracy"] for x in rr]))
            for w in ("500","2000","8000")
          },
          "old_path_mean":{
            w:float(np.mean([x["snapshots"][w]["old_relation_selection"] for x in rr]))
            for w in ("500","2000","8000")
          }
        }

    eps0=8.854e-12; e=1.602e-19
    sanity={}
    for er in (10,20,25):
        sanity[str(er)]={}
        for r_nm in (2,5,10):
            sanity[str(er)][str(r_nm)]=e/(4*math.pi*eps0*er*r_nm*1e-9)

    out={
      "schema":"v14P-electrostatic-trail-v1",
      "evidence_boundary":"Engineering electrostatic/learning model; not a fabricated charge-trap junction.",
      "selected_branch_tip":branch_mc(),
      "learning_rules":learn,
      "stress":stress(),
      "coulomb_point_charge_sanity_V":sanity,
      "selected_rule":"reversible confirmation/contradiction trail",
      "decision":"KEEP electrostatic trail as path-bias memory candidate; REJECT ungated use-only deposition."
    }
    print(json.dumps(out,indent=2))
