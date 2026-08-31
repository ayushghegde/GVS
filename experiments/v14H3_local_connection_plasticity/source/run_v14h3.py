#!/usr/bin/env python3
import numpy as np, json
SEED=1433

def trial(reps=1,sigma=.2,stuck=0.0,n_sources=1000,n_targets=500,rounds=10,change_fraction=.05,seed=SEED):
    rr=np.random.default_rng(seed+reps+int(stuck*1000)+int(sigma*100))
    target=rr.integers(0,n_targets,size=n_sources)
    links=[]
    for s,t in enumerate(target):
        d={int(t):np.ones(reps,dtype=np.int8)}
        for x in rr.choice(n_targets,3,replace=False):
            x=int(x)
            if x!=t: d[x]=np.zeros(reps,dtype=np.int8)
        links.append(d)
    def score_src(s):
        vals={}
        for t,bits in links[s].items():
            base=.25+.60*bits.astype(float)
            vals[t]=float(np.maximum(0,base*(1+rr.normal(0,sigma,reps))).sum())
        return max(vals,key=vals.get)
    def accuracy(indices=None):
        if indices is None: indices=range(n_sources)
        idx=list(indices); return sum(score_src(s)==int(target[s]) for s in idx)/len(idx)
    baseline=accuracy(); history=[]; writes=0; changed_total=set()
    for r in range(rounds):
        changed=rr.choice(n_sources,max(1,int(n_sources*change_fraction)),replace=False)
        changed_total.update(map(int,changed))
        for s0 in changed:
            s=int(s0); old=int(target[s]); new=int(rr.integers(n_targets-1))
            if new>=old: new+=1
            if new not in links[s]: links[s][new]=np.zeros(reps,dtype=np.int8)
            for k in range(reps):
                writes+=2
                if rr.random()>=stuck: links[s][old][k]=0
                if rr.random()>=stuck: links[s][new][k]=1
            target[s]=new
        unchanged=[s for s in range(n_sources) if s not in changed_total]
        history.append({'round':r+1,'current_accuracy':accuracy(),
                        'never_changed_retention':accuracy(unchanged) if unchanged else None,
                        'cumulative_changed_sources':len(changed_total),'program_events':writes})
    return {'reps':reps,'sigma':sigma,'stuck_probability_per_write':stuck,'baseline_accuracy':baseline,
            'rounds':history,'final_accuracy':history[-1]['current_accuracy'],
            'final_never_changed_retention':history[-1]['never_changed_retention'],
            'program_events':writes,'events_per_relation_change':2*reps}

def fixed_control(n_sources=1000,n_targets=500,change_fraction=.2,seed=SEED):
    rr=np.random.default_rng(seed); old=rr.integers(0,n_targets,size=n_sources); new=old.copy()
    changed=rr.choice(n_sources,int(n_sources*change_fraction),replace=False)
    for s in changed:
        v=int(rr.integers(n_targets-1)); new[s]=v+(v>=old[s])
    return {'changed_fraction':change_fraction,'overall_after_change_accuracy':float(np.mean(old==new)),
            'changed_relation_accuracy':float(np.mean(old[changed]==new[changed])),'program_events':0}

if __name__=='__main__':
    out={'experiment':'v14H3 local binary connection plasticity','fixed_geometry_control':fixed_control(),
         'plastic_runs':[],'limits':['Abstract binary-link model, not a measured device.',
                                    'Programming energy/area/endurance are not yet physical values.']}
    for stuck in [0,.01,.05,.10]:
        for reps in [1,2,3]: out['plastic_runs'].append(trial(reps=reps,stuck=stuck))
    print(json.dumps(out,indent=2))
