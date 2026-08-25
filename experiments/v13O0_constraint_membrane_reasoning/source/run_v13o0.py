#!/usr/bin/env python3
"""v13O0 deterministic constraint-membrane model; physics-inspired, not PEX."""
import csv,math,random,statistics
from pathlib import Path
OUT=Path(__file__).resolve().parents[1]/'results';OUT.mkdir(exist_ok=True)
P={'beta':1.8009053123296777,'gain':.9959574018207161,'inertia':.7448191377983095,'noise':.005,'q_alpha':.9786454299642544,'q_decay':.9171019129262584,'qmax':4.,'f_alpha':.15556278530157508,'f_decay':.9338898773126618,'fmax':2.3664774631145984}
def gen(n,seed):
 r=random.Random(seed);pl=[r.choice((-1,1)) for _ in range(n)];C=[]
 while len(C)<round(4.2*n):
  v=r.sample(range(n),3);s=[r.choice((-1,1)) for _ in range(3)]
  if not any(s[k]*pl[v[k]]>0 for k in range(3)):
   j=r.randrange(3);s[j]=pl[v[j]]
  C.append((v[0],s[0],v[1],s[1],v[2],s[2]))
 return C
def sat(st,C):return all(a*st[i]>0 or b*st[j]>0 or c*st[k]>0 for i,a,j,b,k,c in C)
def g(r,s):
 u=max(r.random(),1e-15);return s*math.sqrt(-2*math.log(u))*math.cos(2*math.pi*r.random())
def relax(n,C,seed,adaptive=True,pulse=False,steps=100):
 r=random.Random(seed);m=[r.uniform(-.4,.4) for _ in range(n)];q=[1.]*len(C);fat=[0.]*n;deg=[0]*n
 for i,_,j,_,k,_ in C:deg[i]+=1;deg[j]+=1;deg[k]+=1
 pressure=0.;kicks=0
 for t in range(steps):
  f=[P['inertia']*x for x in m];vu=[0.]*n;cache=[]
  for z,(i,a,j,b,k,c) in enumerate(C):
   u0=(1-a*m[i])/2;u1=(1-b*m[j])/2;u2=(1-c*m[k])/2;x=u0*u1*u2
   if adaptive:q[z]=min(P['qmax'],max(.5,P['q_decay']*q[z]+P['q_alpha']*x));vu[i]+=x;vu[j]+=x;vu[k]+=x
   cache.append((u0,u1,u2))
  if adaptive:
   for i in range(n):
    x=vu[i]/deg[i] if deg[i] else 0;fat[i]=min(P['fmax'],max(0,P['f_decay']*fat[i]+P['f_alpha']*x*abs(m[i])));f[i]-=fat[i]*m[i]
  for z,(i,a,j,b,k,c) in enumerate(C):
   u0,u1,u2=cache[z];x=P['gain']*(q[z] if adaptive else 1)/2;f[i]+=x*a*u1*u2;f[j]+=x*b*u0*u2;f[k]+=x*c*u0*u1
  m=[min(.999,max(-.999,math.tanh(P['beta']*x)+g(r,P['noise']))) for x in f];st=[1 if x>=0 else -1 for x in m]
  if sat(st,C):return True,t+1,kicks
  if pulse:
   pressure=.97*pressure+sum(vu)/(3*len(C))
   if pressure>=.25:
    kicks+=1;m=[min(.8,max(-.8,.2*x+g(r,.3))) for x in m];fat=[x*.5 for x in fat];pressure=0.
 return False,steps,kicks
def wr(name,rows):
 with (OUT/name).open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def main():
 rows=[]
 for n in (16,24,32,48,64):
  Cs=[gen(n,200+s) for s in range(50)]
  for mode in ('plain','adaptive'):
   rr=[relax(n,C,900000+n*1000+s*37,mode=='adaptive') for s,C in enumerate(Cs)];ss=[x[1] for x in rr if x[0]]
   rows.append({'variables':n,'clauses':round(4.2*n),'mode':mode,'instances':50,'success_fraction':sum(x[0] for x in rr)/50,'mean_settle_steps_success':statistics.mean(ss) if ss else '','median_settle_steps_success':statistics.median(ss) if ss else ''})
 wr('single_fabric_summary.csv',rows)
 n=64;Cs=[gen(n,200+s) for s in range(50)];runs=[[relax(n,C,9100000+s*149+r*977,True) for r in range(16)] for s,C in enumerate(Cs)];reps=[]
 for R in (1,2,4,8,16):
  best=[]
  for rr in runs:
   x=[q[1] for q in rr[:R] if q[0]]
   if x:best.append(min(x))
  reps.append({'variables':64,'clauses':269,'replicas':R,'instances':50,'success_fraction':len(best)/50,'mean_first_solution_steps':statistics.mean(best) if best else '','median_first_solution_steps':statistics.median(best) if best else '','max_first_solution_steps':max(best) if best else ''})
 wr('replica_tradeoff.csv',reps)
 pr=[relax(64,C,9300000+s*173,True,True,200) for s,C in enumerate(Cs)];good=[(x[1],x[2]) for x in pr if x[0]]
 wr('pressure_pulse.csv',[{'variables':64,'clauses':269,'instances':50,'success_fraction':len(good)/50,'mean_steps_success':statistics.mean(x for x,k in good),'median_steps_success':statistics.median(x for x,k in good),'mean_pressure_kicks_success':statistics.mean(k for x,k in good)}])
 e=round((64*(2*.5*72e-15*.2**2)+269*(.5*9.52e-15*.2**2))*1e15,4)
 wr('capacitive_proxy.csv',[{'replicas':x['replicas'],'variable_plus_constraint_cap_switch_fj_per_sweep_per_replica':e,'median_first_solution_steps':float(x['median_first_solution_steps']),'capacitive_switch_proxy_fj_to_first_solution_if_all_replicas_active':round(e*x['replicas']*float(x['median_first_solution_steps']),4)} for x in reps])
if __name__=='__main__':main()
