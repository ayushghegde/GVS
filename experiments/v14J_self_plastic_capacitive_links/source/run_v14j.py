#!/usr/bin/env python3
import numpy as np, json
SEED=1410
C_MIN=0.25; C_MAX=0.85; V_READ=0.20; V_PROG=3.0; V_THRESH=1.5
ETA_P=.46; ETA_D=.55

def cap(x): return C_MIN+(C_MAX-C_MIN)*x
class Link:
    def __init__(self,x=0): self.x=float(x)
    def c(self): return cap(self.x)
    def pulse(self,sign,rr,fail=.0,hebb=False):
        if rr.random()<fail: return
        if sign>0: self.x += ETA_P*(1-self.x)
        elif sign<0 and not hebb: self.x -= ETA_D*self.x
        self.x=float(np.clip(self.x,0,1))

class Fabric:
    def __init__(self,reps=1,seed=SEED,n=1000,targets=500,distractors=4):
        self.rr=np.random.default_rng(seed); self.reps=reps; self.n=n; self.targets=targets
        self.target=self.rr.integers(0,targets,size=n); self.links=[]
        for s in range(n):
            t=int(self.target[s]); d={t:[Link(1) for _ in range(reps)]}
            while len(d)<distractors+1:
                x=int(self.rr.integers(targets))
                if x not in d: d[x]=[Link(0) for _ in range(reps)]
            self.links.append(d)
    def ensure(self,s,t):
        if t not in self.links[s]: self.links[s][t]=[Link(0) for _ in range(self.reps)]
    def score(self,s,t,sigma=.2):
        return sum(max(0,l.c()*(1+self.rr.normal(0,sigma))) for l in self.links[s][t])
    def predict(self,s,sigma=.2): return max(self.links[s],key=lambda t:self.score(s,t,sigma))
    def accuracy(self,idx=None,sigma=.2):
        idx=list(range(self.n) if idx is None else idx)
        return float(np.mean([self.predict(s,sigma)==int(self.target[s]) for s in idx]))
    def change(self,s,new,false_feedback=.0,fail=.05,hebb=False,events=3):
        old=int(self.target[s]); self.ensure(s,new)
        for _ in range(events):
            for k in range(self.reps):
                wrong=self.rr.random()<false_feedback
                self.links[s][new][k].pulse(-1 if wrong else +1,self.rr,fail,hebb)
                self.links[s][old][k].pulse(+1 if wrong else -1,self.rr,fail,hebb)
        self.target[s]=new

def continual(reps=1,false_feedback=0,hebb=False,seed=SEED):
    f=Fabric(reps,seed); changed=set(); hist=[]
    for r in range(12):
        chosen=f.rr.choice(f.n,int(.05*f.n),replace=False)
        for s0 in chosen:
            s=int(s0); old=int(f.target[s]); new=int(f.rr.integers(f.targets-1)); new += new>=old
            f.change(s,new,false_feedback,fail=.05,hebb=hebb); changed.add(s)
        unchanged=[s for s in range(f.n) if s not in changed]
        hist.append({'round':r+1,'accuracy':f.accuracy(),'never_changed_retention':f.accuracy(unchanged) if unchanged else None})
    desired=[]; other=[]
    for s in range(f.n):
        t=int(f.target[s]); desired += [l.c() for l in f.links[s][t]]
        for u,ls in f.links[s].items():
            if u!=t: other += [l.c() for l in ls]
    return {'reps':reps,'false_feedback':false_feedback,'hebbian_only':hebb,'final_accuracy':hist[-1]['accuracy'],
            'never_changed_retention':hist[-1]['never_changed_retention'],
            'mean_desired_cap_fF':float(np.mean(desired)),'mean_nonselected_cap_fF':float(np.mean(other))}

def chain(reps=1,false_feedback=0,seed=SEED+70):
    rr=np.random.default_rng(seed); chains=180; hops=6; sigma=.2; F=[]
    for _ in range(chains):
        c=[]
        for _ in range(hops):
            good=int(rr.integers(10000)); opts={good:[Link(1) for _ in range(reps)]}
            while len(opts)<4:
                x=int(rr.integers(10000))
                if x not in opts: opts[x]=[Link(0) for _ in range(reps)]
            c.append([good,opts])
        F.append(c)
    def pick(opts): return max(opts,key=lambda t:sum(max(0,l.c()*(1+rr.normal(0,sigma))) for l in opts[t]))
    def acc(): return sum(all(pick(opts)==good for good,opts in c) for c in F)/chains
    before=acc()
    for ci0 in rr.choice(chains,int(.25*chains),replace=False):
        ci=int(ci0); h=int(rr.integers(hops)); old,opts=F[ci][h]; new=int(rr.integers(10000))
        while new in opts: new=int(rr.integers(10000))
        opts[new]=[Link(0) for _ in range(reps)]
        for _ in range(3):
            for k in range(reps):
                wrong=rr.random()<false_feedback
                opts[new][k].pulse(-1 if wrong else +1,rr,.05)
                opts[old][k].pulse(+1 if wrong else -1,rr,.05)
        F[ci][h][0]=new
    return {'reps':reps,'false_feedback':false_feedback,'before':before,'after_local_relearning':acc()}

def threshold_screen(n=200000):
    rr=np.random.default_rng(SEED+9); th=np.maximum(.2,rr.normal(V_THRESH,.2*V_THRESH,n))
    return {'samples':n,'read_disturb_probability':float(np.mean(V_READ>=th)),
            'program_above_threshold_probability':float(np.mean(V_PROG>=th))}

if __name__=='__main__':
    out={'experiment':'v14J self-polarizing capacitive-link learning','continual':[],'six_hop':[],'threshold_screen':threshold_screen(),
         'limits':['abstract memcapacitor model','no fabricated programmable GVS link','learning requires local correctness/contradiction echo']}
    for hebb in [False,True]:
        for reps in [1,2,3]:
            for fb in [0,.01,.05,.10]: out['continual'].append(continual(reps,fb,hebb,SEED+reps+int(fb*1000)))
    for reps in [1,2,3]:
        for fb in [0,.05,.10]: out['six_hop'].append(chain(reps,fb,SEED+100*reps+int(fb*1000)))
    print(json.dumps(out,indent=2))
