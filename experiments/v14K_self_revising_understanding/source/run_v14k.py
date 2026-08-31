import random, math, json, statistics
from pathlib import Path
OUT=Path(__file__).resolve().parents[1]/"results"
OUT.mkdir(parents=True,exist_ok=True)
from collections import defaultdict

SEED=14011
random.seed(SEED)
DOMAINS=['biology','math_formula','code_rule','causal','planning','language_context']
N_PER_DOMAIN=350

class Graph:
    def __init__(self): self.w={}
    def set(self,a,b,w): self.w[(a,b)]=max(0.0,min(1.5,w))
    def get(self,a,b): return self.w.get((a,b),0.0)
    def add(self,a,b,d): self.set(a,b,self.get(a,b)+d)
    def copy(self):
        g=Graph(); g.w=dict(self.w); return g
    def propagate(self,start,steps=4,noise=0.0):
        act={start:1.0}; peak=dict(act)
        for _ in range(steps):
            nxt=defaultdict(float)
            for (a,b),w in self.w.items():
                if a in act and w>0:
                    wn=max(0,w*(1+random.gauss(0,noise)))
                    nxt[b]+=act[a]*wn
            if not nxt: break
            m=max(nxt.values())
            if m>0:
                for k in list(nxt): nxt[k]/=m
            act=dict(nxt)
            for k,v in act.items(): peak[k]=max(peak.get(k,0),v)
        return peak

def make_case(i,domain):
    p=f'{domain}:{i}'
    cue=p+':cue'; old=p+':old'; wrong=p+':wrong'; n1=p+':new1'; n2=p+':new2'; correct=p+':correct'
    g=Graph(); g.set(cue,old,0.95); g.set(old,wrong,1.0); g.set(cue,correct,0.03)
    stable=[(p+f':s{k}',p+f':t{k}') for k in range(3)]
    for a,b in stable:g.set(a,b,0.95)
    lesson=[(cue,n1),(n1,n2),(n2,correct)]
    distractor=[(p+':d0',p+':d1'),(p+':d1',p+':d2'),(p+':d2',p+':d3')]
    return dict(domain=domain,p=p,cue=cue,old=old,wrong=wrong,n1=n1,n2=n2,correct=correct,g=g,lesson=lesson,distractor=distractor,stable=stable)

def predict(g,c,noise=0.0,start=None):
    a=g.propagate(start or c['cue'],4,noise); vc=a.get(c['correct'],0); vw=a.get(c['wrong'],0)
    if max(vc,vw)<0.15:return 'unknown'
    return 'correct' if vc>vw*1.05 else ('wrong' if vw>vc*1.05 else 'ambiguous')

def failed_effort(g,c):
    w=g.get(c['old'],c['wrong']); base=1+int(round(2.5*w))
    return max(1,min(4,base+random.choice([-1,0,0,1])))

def learn(case,mode,false_feedback=0.0,program_fail=0.0,noise=0.10):
    g=case['g'].copy(); effort=failed_effort(g,case); touched=set(); new_edges=0; weakened=0; selftests=0
    feedback_correct=random.random()>=false_feedback
    if mode=='static': pass
    elif mode=='strengthen_only':
        for a,b in case['lesson']:
            if random.random()>=program_fail:
                if g.get(a,b)==0:new_edges+=1
                g.add(a,b,0.66); touched.add((a,b))
        for a,b in case['distractor']:
            if random.random()<0.35 and random.random()>=program_fail:g.add(a,b,0.45); touched.add((a,b))
    elif mode=='v14j_existing_only':
        if feedback_correct and random.random()>=program_fail:g.add(case['old'],case['wrong'],-0.78); touched.add((case['old'],case['wrong'])); weakened+=1
        if random.random()>=program_fail:g.add(case['cue'],case['correct'],0.22); touched.add((case['cue'],case['correct']))
    elif mode in ('v14k_no_effort','v14k_effort'):
        gain=0.55 if mode=='v14k_no_effort' else 0.38+0.10*effort
        for a,b in case['lesson']:
            if random.random()>=program_fail:
                if g.get(a,b)==0:new_edges+=1
                g.add(a,b,gain); touched.add((a,b))
        if random.random()>=program_fail:
            delta=-0.72 if feedback_correct else +0.15
            g.add(case['old'],case['wrong'],delta); touched.add((case['old'],case['wrong']))
            if feedback_correct: weakened+=1
        p_irrel=0.18 if mode=='v14k_no_effort' else max(0.01,0.12-0.025*effort)
        for a,b in case['distractor']:
            if random.random()<p_irrel and random.random()>=program_fail:g.add(a,b,0.35); touched.add((a,b))
        for _ in range(3):
            selftests+=1
            if predict(g,case,noise=noise)=='correct':break
            for a,b in case['lesson']:
                if random.random()>=program_fail:g.add(a,b,0.18); touched.add((a,b))
            if feedback_correct and random.random()>=program_fail:g.add(case['old'],case['wrong'],-0.16); touched.add((case['old'],case['wrong']))
    return g,effort,len(touched),new_edges,weakened,selftests

def run_condition(mode,false_feedback=0,program_fail=0,read_noise=.1):
    rows=[]
    for d in DOMAINS:
        for i in range(N_PER_DOMAIN):
            c=make_case(i,d); before=predict(c['g'],c,read_noise)
            g,e,t,new,wk,st=learn(c,mode,false_feedback,program_fail,read_noise)
            after=predict(g,c,read_noise); transfer=predict(g,c,read_noise,start=c['n1'])
            stable_ok=sum(1 for a,b in c['stable'] if g.get(a,b)>=0.8)/len(c['stable'])
            rows.append((d,before,after,transfer,e,t,new,wk,st,stable_ok))
    def rate(idx,val='correct'):return sum(r[idx]==val for r in rows)/len(rows)
    return {'mode':mode,'false_feedback':false_feedback,'program_fail':program_fail,'read_noise':read_noise,'cases':len(rows),'before_correct':rate(1),'after_correct':rate(2),'transfer_correct':rate(3),'after_unknown':rate(2,'unknown'),'after_wrong':rate(2,'wrong'),'mean_effort':statistics.mean(r[4] for r in rows),'mean_touched_links':statistics.mean(r[5] for r in rows),'mean_new_links':statistics.mean(r[6] for r in rows),'mean_weakened_links':statistics.mean(r[7] for r in rows),'mean_selftests':statistics.mean(r[8] for r in rows),'unrelated_retention':statistics.mean(r[9] for r in rows)}

results=[]
for mode in ['static','strengthen_only','v14j_existing_only','v14k_no_effort','v14k_effort']: results.append(run_condition(mode,0,0,.10))
for ff in [0.02,0.05,0.10,0.15]:
    for pf in [0.02,0.05,0.10]: results.append(run_condition('v14k_effort',ff,pf,.20))
formula=[]
for effort in [1,2,3,4]:
    ok=0; transfer=0; trials=5000
    for j in range(trials):
        c=make_case(j,'formula'); g=c['g'].copy(); gain=0.38+.10*effort
        for a,b in c['lesson']:g.add(a,b,gain*(1+random.gauss(0,.15)))
        g.add(c['old'],c['wrong'],-.72*(1+random.gauss(0,.10)))
        if predict(g,c,.15)=='correct':ok+=1
        if predict(g,c,.15,start=c['n1'])=='correct':transfer+=1
    formula.append({'failed_attempts_before_teaching':effort,'one_shot_retest_success':ok/trials,'transfer_success':transfer/trials})
out={'seed':SEED,'domains':DOMAINS,'cases_per_domain':N_PER_DOMAIN,'conditions':results,'effort_formula_screen':formula}
(OUT/'RESULTS.json').write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
