#!/usr/bin/env python3
import random, json
from collections import defaultdict
import numpy as np

SEED=1408
random.seed(SEED)
rng=np.random.default_rng(SEED)

class Fabric:
    def __init__(self):
        self.nodes=[]; self.idx={}; self.out=defaultdict(list); self.goal_rel=defaultdict(dict)
    def node(self,n):
        if n not in self.idx:
            self.idx[n]=len(self.nodes); self.nodes.append(n)
    def edge(self,a,b,w,rel):
        self.node(a); self.node(b); self.out[a].append((b,float(w),rel))
    def goal(self,g,rel,w=1.0):
        self.node(g); self.goal_rel[g][rel]=float(w)

def build():
    fab=Fabric(); q=[]
    goalrels={'G_MEANING':['ctx'],'G_CAUSE':['cause1','cause2'],'G_FIX':['code1','code2'],
              'G_PLAN':['plan1','plan2','plan3'],'G_WHERE':['fact1','fact2','fact3'],
              'G_ANALOGY':['ana1','ana2'],'G_OPERATION':['opselect']}
    for g,rs in goalrels.items():
        for r in rs: fab.goal(g,r)
    for a in range(60):
        amb=f'AMB_{a}'
        for s in range(3):
            sense=f'SENSE_{a}_{s}'; cues=[f'CUE_{a}_{s}_{k}' for k in range(4)]
            fab.edge(amb,sense,.65,'ctx')
            for c in cues: fab.edge(c,sense,.9,'ctx')
            for s2 in range(3):
                if s2!=s:
                    for c in cues[:2]: fab.edge(c,f'SENSE_{a}_{s2}',.18,'ctx')
            for _ in range(4): q.append({'domain':'context','cues':[amb]+random.sample(cues,3),'goal':'G_MEANING','answer':sense,'hops':1})
    for i in range(180):
        mid=i%90; symptom=f'SYM_{i}'; mech=f'MECH_{mid}'; cause=f'CAUSE_{mid%60}'
        fab.edge(symptom,mech,1,'cause1'); fab.edge(mech,cause,1,'cause2')
        for d in rng.choice(90,2,replace=False):
            d=int(d)
            if d!=mid: fab.edge(symptom,f'MECH_{d}',.28,'cause1')
        q.append({'domain':'cause','cues':[symptom],'goal':'G_CAUSE','answer':cause,'hops':2})
    for i in range(150):
        b=i%75; bug=f'BUG_{b}'; fix=f'FIX_{b%50}'; cues=[f'CODECUE_{i}_{k}' for k in range(3)]
        for c in cues: fab.edge(c,bug,.7,'code1')
        fab.edge(bug,fix,1,'code2')
        for c in cues:
            d=int(rng.integers(75))
            if d!=b: fab.edge(c,f'BUG_{d}',.25,'code1')
        q.append({'domain':'code','cues':cues,'goal':'G_FIX','answer':fix,'hops':2})
    for i in range(140):
        p=i%70; a=p%55; e=a%45; st=f'STATE_{i}'; pre=f'PRE_{p}'; act=f'ACT_{a}'; end=f'END_{e}'
        fab.edge(st,pre,1,'plan1'); fab.edge(pre,act,1,'plan2'); fab.edge(act,end,1,'plan3')
        d=int(rng.integers(70))
        if d!=p: fab.edge(st,f'PRE_{d}',.3,'plan1')
        q.append({'domain':'plan','cues':[st],'goal':'G_PLAN','answer':end,'hops':3})
    for i in range(180):
        ci=i%90; co=ci%30; ct=co%6; ent=f'ENT_{i}'; city=f'CITY_{ci}'; country=f'COUNTRY_{co}'; cont=f'CONT_{ct}'
        fab.edge(ent,city,1,'fact1'); fab.edge(city,country,1,'fact2'); fab.edge(country,cont,1,'fact3')
        d=int(rng.integers(90))
        if d!=ci: fab.edge(ent,f'CITY_{d}',.22,'fact1')
        q.append({'domain':'fact','cues':[ent],'goal':'G_WHERE','answer':cont,'hops':3})
    for i in range(160):
        b=i%80; src=f'ASRC_{i}'; rel=f'AREL_{i%20}'; bridge=f'ABRIDGE_{b}'; tgt=f'ATGT_{b}'
        fab.edge(src,bridge,.7,'ana1'); fab.edge(rel,bridge,.7,'ana1'); fab.edge(bridge,tgt,1,'ana2')
        d=int(rng.integers(80))
        if d!=b: fab.edge(src,f'ABRIDGE_{d}',.45,'ana1')
        q.append({'domain':'analogy','cues':[src,rel],'goal':'G_ANALOGY','answer':tgt,'hops':2})
    feats={'ADD':['sum','total','combined'],'COMPARE':['difference','larger','compare'],
           'MULTIPLY':['product','times','area'],'LOOKUP':['define','meaning','what_is'],
           'CAUSE_OP':['why','cause','because'],'PLAN_OP':['how','steps','goal']}
    for op,fs in feats.items():
        node=f'OP_{op}'
        for f in fs: fab.edge(f'OPCUE_{f}',node,.8,'opselect')
        for _ in range(100):
            q.append({'domain':'operation','cues':[f'OPCUE_{x}' for x in random.sample(fs,2)],'goal':'G_OPERATION','answer':node,'hops':1})
    return fab,q

def infer(fab,q,sigma,rr,residual=None,residual_scale=0):
    active=defaultdict(float)
    for c in q['cues']: active[c]+=1
    if residual:
        for n,a in residual.items(): active[n]+=residual_scale*a
    gm=fab.goal_rel[q['goal']]; state=dict(active); path=[]
    for _ in range(q['hops']):
        score=defaultdict(float)
        for src,amp in active.items():
            for dst,w,rel in fab.out.get(src,[]):
                if rel not in gm: continue
                nw=max(0,w*(1+rr.normal(0,sigma)))
                score[dst]+=amp*nw*gm[rel]
        if not score: break
        mx=max(score.values()); win=[k for k,v in score.items() if abs(v-mx)<1e-12]
        dst=win[int(rr.integers(len(win)))]; path.append(dst); active=defaultdict(float,{dst:1}); state[dst]=1
    return (path[-1] if path else None),state

def bench(fab,queries,sigma):
    rr=np.random.default_rng(7700+int(sigma*1000)); by=defaultdict(lambda:[0,0])
    qq=queries[:]; random.Random(1234).shuffle(qq)
    for q in qq:
        a,_=infer(fab,q,sigma,rr); by[q['domain']][0]+=int(a==q['answer']); by[q['domain']][1]+=1
    out={d:ok/n for d,(ok,n) in by.items()}; out['ALL']=sum(x[0] for x in by.values())/sum(x[1] for x in by.values()); return out

def residual_screen(fab,queries,sigma=.2):
    qq=queries[:]; random.Random(1234).shuffle(qq); out=[]
    for rscale in [0,.02,.05,.1,.2,.3,.5]:
        rr=np.random.default_rng(99); residual=None; ok=0
        for q in qq:
            a,state=infer(fab,q,sigma,rr,residual,rscale); ok+=int(a==q['answer']); residual=state
        out.append({'retained_previous_activation_fraction':rscale,'accuracy':ok/len(qq)})
    return out

def capacitor_context(sigma,n=5000):
    rr=np.random.default_rng(42); vin=.2; cl=5.0; wins=0; margins=[]
    def vt(cs):
        s=float(np.sum(cs)); return vin*s/(cl+s)
    for _ in range(n):
        correct=np.maximum(0,np.array([.65,.9,.9,.9])*(1+rr.normal(0,sigma,4)))
        wrong=np.maximum(0,np.array([.65,.18,.18])*(1+rr.normal(0,sigma,3)))
        vc,vw=vt(correct),vt(wrong); wins+=vc>vw; margins.append(vc-vw)
    return {'variation_sigma':sigma,'trials':n,'correct_target_higher_voltage_rate':wins/n,
            'mean_voltage_margin_V':float(np.mean(margins)),'p01_voltage_margin_V':float(np.percentile(margins,1))}

def quantized_bench(fab,queries,sigma,levels):
    def qweight(w): return min(levels,key=lambda x:abs(x-w))
    rr=np.random.default_rng(8800+int(sigma*1000)+len(levels)); qq=queries[:]; random.Random(1234).shuffle(qq); by=defaultdict(lambda:[0,0])
    for q in qq:
        active=defaultdict(float)
        for c in q['cues']: active[c]+=1
        gm=fab.goal_rel[q['goal']]; ans=None
        for _ in range(q['hops']):
            score=defaultdict(float)
            for src,amp in active.items():
                for dst,w,rel in fab.out.get(src,[]):
                    if rel not in gm: continue
                    w=qweight(w); w=max(0,w*(1+rr.normal(0,sigma))); score[dst]+=amp*w*gm[rel]
            if not score: break
            mx=max(score.values()); wins=[d for d,v in score.items() if abs(v-mx)<1e-12]; ans=wins[int(rr.integers(len(wins)))]; active=defaultdict(float,{ans:1})
        by[q['domain']][0]+=int(ans==q['answer']); by[q['domain']][1]+=1
    out={d:ok/n for d,(ok,n) in by.items()}; out['ALL']=sum(v[0] for v in by.values())/sum(v[1] for v in by.values()); return out

def chain_bundle_screen(sigma,reps,n=2000,hops=12,strong=.85,weak=.25,distractors=3):
    rr=np.random.default_rng(700+int(100*sigma)+reps); ok=0
    for _ in range(n):
        good=True
        for _ in range(hops):
            wc=np.maximum(0,strong*(1+rr.normal(0,sigma,reps))).sum()
            wd=max(np.maximum(0,weak*(1+rr.normal(0,sigma,reps))).sum() for _ in range(distractors))
            if wc<=wd: good=False; break
        ok+=good
    return ok/n

if __name__=='__main__':
    fab,queries=build(); n=len(fab.nodes); e=sum(len(x) for x in fab.out.values())
    result={'experiment':'v14H2 connection-imprinted excitation fabric','persistent_node_memory_sites':0,
      'cells':n,'learned_sparse_connections':e,'directed_connection_density':e/(n*(n-1)),'queries':len(queries),
      'domains':['context','cause','code','plan','fact','analogy','operation'],
      'connection_variation':{str(s):bench(fab,queries,s) for s in [0,.1,.2,.3]},
      'retained_node_charge_control':residual_screen(fab,queries,.2),
      'capacitive_cofiring_screen':[capacitor_context(s) for s in [.05,.1,.2,.3,.4]],
      'weight_quantization':{
        '2_level_weak_strong':{str(s):quantized_bench(fab,queries,s,[.25,.85]) for s in [0,.1,.2,.3,.4]},
        '4_level':{str(s):quantized_bench(fab,queries,s,[.2,.4,.7,1.0]) for s in [0,.1,.2,.3,.4]}},
      'twelve_hop_connection_bundle':{str(s):{str(r):chain_bundle_screen(s,r) for r in [1,2,3,5]} for s in [.2,.3,.4]},
      'limits':['Synthetic relational benchmark, not a foundation-model benchmark.',
                'Operation selection is tested, but structural multiplication/factorization remains open.',
                'Persistent memory is assumed to reside in connection strength; a cheap trainable physical coupler is not yet closed.',
                'Threshold/restoration physics for long cascades remains a hardware problem.']}
    print(json.dumps(result,indent=2))
