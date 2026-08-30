#!/usr/bin/env python3
"""Deterministic v14G model battery. No external packages required except numpy for the capacity screen."""
import math, random, csv, json, statistics, os
from collections import defaultdict
try:
    import numpy as np
except Exception:
    np=None
OUT='results'; os.makedirs(OUT,exist_ok=True)

class Fabric:
    def __init__(self):
        self.w=defaultdict(float); self.ctx=defaultdict(lambda:defaultdict(float))
    def edge(self,r,s,d,v=1): self.w[(r,s,d)]+=v
    def context(self,d,c,v=1): self.ctx[d][c]+=v
    def norm(self):
        by=defaultdict(list)
        for k,v in self.w.items():by[k[:2]].append((k,v))
        for arr in by.values():
            m=max(v for _,v in arr) or 1
            for k,v in arr:self.w[k]=v/m
        for x in self.ctx.values():
            m=max(x.values()) if x else 1
            for k in list(x):x[k]/=m
    def step(self,r,s,cues=(),sigma=0,ctxgain=.65,rng=None):
        rng=rng or random;c=[]
        for (rr,ss,d),b in self.w.items():
            if rr!=r or ss!=s:continue
            e=max(0,b*(1+rng.gauss(0,sigma))); a=sum(self.ctx[d].get(q,0) for q in cues)/max(1,len(cues)) if cues else 0
            c.append((e*(1+ctxgain*a),d))
        return max(c)[1] if c else None
    def chain(self,s,rels,cues=(),sigma=0,rng=None):
        for r in rels:
            s=self.step(r,s,cues,sigma,rng=rng)
            if s is None:return None
        return s

def context_screen(rng):
    f=Fabric()
    for _ in range(40):
        f.edge('SENSE','BANK','RIVER_BANK');f.edge('SENSE','BANK','FINANCE_BANK')
        for c in ['RIVER','WATER','SHORE','FLOOD']:f.context('RIVER_BANK',c)
        for c in ['MONEY','LOAN','ACCOUNT','CREDIT']:f.context('FINANCE_BANK',c)
    f.norm();out=[]
    for sig in [0,.05,.1,.2,.3,.4]:
        ok=0;n=4000
        for i in range(n):
            cues,target=(['RIVER','WATER'],'RIVER_BANK') if i%2==0 else (['MONEY','LOAN'],'FINANCE_BANK')
            ok+=f.step('SENSE','BANK',cues,sig,.8,rng)==target
        out.append([sig,ok/n])
    return out

def goal_recognition(rng):
    goals={'SUM':['TOTAL','ADD','TOGETHER','PLUS','SUM'],'VALUE':['VALUE','SOLVE','X','EQUAL','FIND'],'CAUSE':['WHY','CAUSE','REASON','BECAUSE','EXPLAIN'],'LOCATION':['WHERE','LOCATED','PLACE','POSITION','LOCATION'],'FIX_CODE':['ERROR','FIX','BUG','CODE','FAIL'],'WRITE_CODE':['WRITE','IMPLEMENT','FUNCTION','CODE','CREATE'],'COMPARE':['COMPARE','DIFFERENCE','BETTER','VERSUS','WHICH'],'DEFINE':['WHAT','MEAN','DEFINE','DEFINITION','TERM']}
    generic=['WHAT','FIND','CODE','WHICH'];out=[]
    for sig in [0,.05,.1,.2,.3,.4]:
        hit=0;n=5000
        for _ in range(n):
            g=rng.choice(list(goals));sp=[x for x in goals[g] if x not in generic];q=set(rng.sample(sp,min(2,len(sp))))
            if rng.random()<.65:q.add(rng.choice(generic))
            if rng.random()<.5:
                other=[x for h,c in goals.items() if h!=g for x in c if x not in q];q.add(rng.choice(other))
            scores=[]
            for h,cues in goals.items():
                s=sum(max(0,(.65 if cue in generic else 1)*(1+rng.gauss(0,sig))) for cue in q if cue in cues);scores.append((s,h))
            hit+=max(scores)[1]==g
        out.append([sig,hit/n])
    return out

def episode_recall(rng):
    vocab=list(range(96));eps=[set(rng.sample(vocab,8)) for _ in range(256)];out=[]
    for sig in [.05,.1,.2,.3,.4]:
        hit=0;n=3000
        for _ in range(n):
            i=rng.randrange(256);true=eps[i];q=set(rng.sample(list(true),5));q.update(rng.sample([x for x in vocab if x not in true],2));best=(-1,None)
            for j,ep in enumerate(eps):
                sc=sum(max(0,1+rng.gauss(0,sig)) for x in q if x in ep)
                if sc>best[0]:best=(sc,j)
            hit+=best[1]==i
        out.append([sig,hit/n])
    return out

def goal_echo(rng):
    def one(depth,branch,sig,eg):
        for d in range(depth):
            rem=depth-d-1;c=[]
            for j in range(branch):
                b=1 if j==0 else rng.uniform(.72,.88);eff=max(.01,b*(1+rng.gauss(0,sig)))
                back=.94**rem if j==0 else ((.20+rng.random()*.18)*(.94**rem) if rng.random()<.18 else 0)
                c.append((eff*(1+eg*back),j))
            if max(c)[1]!=0:return False
        return True
    out=[]
    for d in [2,4,6,8,12]:
      for s in [.05,.1,.15,.2,.25]:
       for e in [0,.25,.5,1,1.5]:
        n=5000;out.append([d,s,e,sum(one(d,3,s,e) for _ in range(n))/n])
    return out

def code_screen(rng):
    bc={'NULL':['NONE','ATTRIBUTE','OPTIONAL'],'TYPE':['TYPE','OPERAND','ANNOTATION'],'INDEX':['INDEX','RANGE','BOUND'],'ASYNC':['AWAIT','COROUTINE','EVENTLOOP'],'IMPORT':['MODULE','IMPORT','PATH'],'STATE':['MUTATION','SHARED','STATE']};f=Fabric()
    for b,cues in bc.items():
        for _ in range(30):
            f.edge('DIAG','ERR',b);f.edge('FIX',b,'FIX_'+b)
            for c in cues:f.context(b,c)
    f.norm();out=[]
    for sig in [0,.05,.1,.2,.3,.4]:
        ok=0;n=3000
        for _ in range(n):
            b=rng.choice(list(bc));q=rng.sample(bc[b],2);d=f.step('DIAG','ERR',q,sig,1,rng);fix=f.step('FIX',d,(),sig,0,rng) if d else None;ok+=fix=='FIX_'+b
        out.append([sig,ok/n])
    return out

def arithmetic_limit(rng):
    f=Fabric();MAX=128;ops=[]
    for k in range(1,10):ops += [('ADD'+str(k),lambda x,k=k:x+k),('SUB'+str(k),lambda x,k=k:x-k)]
    for k in [2,3,4]:ops += [('MUL'+str(k),lambda x,k=k:x*k)]
    withheld=[]
    for name,fn in ops:
        for x in range(MAX):
            y=fn(x)
            if not 0<=y<MAX:continue
            if (x*17+sum(map(ord,name)))%11==0:withheld.append((name,x,y))
            else:f.edge(name,'V'+str(x),'V'+str(y))
    f.norm();hit=0
    for name,x,y in withheld:hit+=f.step(name,'V'+str(x),rng=rng)=='V'+str(y)
    return {'withheld':len(withheld),'accuracy':hit/max(1,len(withheld))}

def regen(rng):
    out=[]
    for a in [.98,.96,.94,.92]:
      for sp in [0,4,8,12,16,24,32]:
        oks=[];nr=[]
        for _ in range(4000):
            amp=1;rest=0;ok=True
            for hop in range(1,65):
                amp*=max(0,a*(1+rng.gauss(0,.015)))
                if sp and hop%sp==0:
                    th=.40*(1+rng.gauss(0,.05))
                    if amp>=th:amp=max(.85,min(1.05,.95*(1+rng.gauss(0,.025))));rest+=1
                if amp<.42:ok=False;break
            oks.append(ok);nr.append(rest)
        out.append([a,sp,sum(oks)/len(oks),statistics.mean(nr)])
    return out

def threshold_screen(rng):
    out=[]
    for sig in [.05,.1,.15,.2]:
      for th in [.45,.5,.55,.6,.65]:
        tp=fp=0;n=20000
        for _ in range(n):
            cor=max(0,rng.gauss(.72,.06)*(1+rng.gauss(0,sig)));wrong=max(0,rng.gauss(.36,.07)*(1+rng.gauss(0,sig)));vth=th*(1+rng.gauss(0,.04));tp+=cor>=vth;fp+=wrong>=vth
        out.append([sig,th,tp/n,fp/n])
    return out

def capacity(rng):
    if np is None:return []
    nr=np.random.default_rng(1407005);out=[]
    for cells in [128,256,512,1024]:
      vocab=max(96,cells//2)
      for episodes in [64,128,256,512,1024,2048]:
        if episodes>cells*4:continue
        M=np.zeros((episodes,vocab),dtype=np.uint8);sets=[]
        for i in range(episodes):s=rng.sample(range(vocab),8);M[i,s]=1;sets.append(s)
        for sig in [.1,.2,.3]:
            hit=0;n=1500
            for _ in range(n):
                i=rng.randrange(episodes);true=sets[i];q=rng.sample(true,5)+rng.sample([x for x in range(vocab) if x not in true],2);ov=M[:,q].sum(1).astype(float);sc=ov+nr.normal(0,sig*np.sqrt(np.maximum(ov,1e-9)),episodes);hit+=int(np.argmax(sc)==i)
            sparse=episodes*8;dense=vocab*episodes;out.append([cells,vocab,episodes,sig,hit/n,sparse,dense,sparse/dense])
    return out

def hardware():
    out=[]
    for N in [64,256,1024,4096]:
      e=N*6//2
      for sp in [4,8,16]:
        r=math.ceil(N/sp);td=e+r;m=N;cmos=6*e+6*N;out.append([N,6,sp,e,r,td,m,cmos,cmos/td])
    return out

def main():
    r=random.Random(1407001)
    data={'context':context_screen(r),'goal_recognition':goal_recognition(r),'episode_recall':episode_recall(r),'goal_echo':goal_echo(r),'code':code_screen(r),'arithmetic_unseen':arithmetic_limit(r),'regeneration':regen(r),'threshold':threshold_screen(r),'capacity':capacity(r),'hardware':hardware()}
    with open(OUT+'/summary.json','w') as f:json.dump(data,f,indent=2)
    def find(arr,cond):
        for x in arr:
            if cond(x):return x
    keys=[
      ['context_accuracy','sigma=.2',find(data['context'],lambda x:x[0]==.2)[1]],
      ['goal_recognition','sigma=.2',find(data['goal_recognition'],lambda x:x[0]==.2)[1]],
      ['episode_recall','sigma=.2',find(data['episode_recall'],lambda x:x[0]==.2)[1]],
      ['goal_echo_8hop','sigma=.2;echo=0',find(data['goal_echo'],lambda x:x[:3]==[8,.2,0])[3]],
      ['goal_echo_8hop','sigma=.2;echo=1',find(data['goal_echo'],lambda x:x[:3]==[8,.2,1])[3]],
      ['goal_echo_12hop','sigma=.2;echo=1',find(data['goal_echo'],lambda x:x[:3]==[12,.2,1])[3]],
      ['code_repair','sigma=.2',find(data['code'],lambda x:x[0]==.2)[1]],
      ['unseen_arithmetic','withheld='+str(data['arithmetic_unseen']['withheld']),data['arithmetic_unseen']['accuracy']],
      ['64hop_success','loss=.06;spacing=8',find(data['regeneration'],lambda x:x[0]==.94 and x[1]==8)[2]],
      ['64hop_success','loss=.08;spacing=8',find(data['regeneration'],lambda x:x[0]==.92 and x[1]==8)[2]],
    ]
    with open(OUT+'/key_results.csv','w',newline='') as f:
        w=csv.writer(f);w.writerow(['metric','condition','value']);w.writerows(keys)
    print(json.dumps(keys,indent=2))
if __name__=='__main__':main()
