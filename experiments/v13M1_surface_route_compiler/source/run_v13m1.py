import csv, heapq, itertools, math
from pathlib import Path
OUT=Path(__file__).resolve().parents[1]/'results';OUT.mkdir(parents=True,exist_ok=True)
# 10 x 10 x 2 mm cuboid, sampled on a 2 mm x/y and 1 mm z boundary grid.
XS=[0,2,4,6,8,10]; YS=[0,2,4,6,8,10]; ZS=[0,1,2]
all_nodes=[(x,y,z) for x in XS for y in YS for z in ZS]
def boundary(p):
    x,y,z=p; return x in (0,10) or y in (0,10) or z in (0,2)
N=[p for p in all_nodes if boundary(p)]
S=set(N)
# weighted boundary graph; only axis-adjacent grid segments whose endpoints are on boundary.
G={p:[] for p in N}
for p in N:
    x,y,z=p
    for q in [(x+2,y,z),(x-2,y,z),(x,y+2,z),(x,y-2,z),(x,y,z+1),(x,y,z-1)]:
        if q in S:
            d=abs(q[0]-x)+abs(q[1]-y)+abs(q[2]-z)
            G[p].append((q,d))
def dij(src):
    dist={src:0.0}; h=[(0.0,src)]
    while h:
        d,u=heapq.heappop(h)
        if d!=dist[u]: continue
        for v,w in G[u]:
            nd=d+w
            if nd<dist.get(v,1e99): dist[v]=nd; heapq.heappush(h,(nd,v))
    return dist
D={p:dij(p) for p in N}
def interior_manhattan(a,b): return sum(abs(a[i]-b[i]) for i in range(3))
def faces(p):
    x,y,z=p; f=[]
    if x==0:f.append('x0')
    if x==10:f.append('x10')
    if y==0:f.append('y0')
    if y==10:f.append('y10')
    if z==0:f.append('z0')
    if z==2:f.append('z2')
    return set(f)
def category(a,b):
    fa,fb=faces(a),faces(b)
    if fa&fb:return 'share_face'
    opp={('x0','x10'),('x10','x0'),('y0','y10'),('y10','y0'),('z0','z2'),('z2','z0')}
    if any((x,y) in opp for x in fa for y in fb):return 'opposite_faces'
    return 'different_faces'
rows=[]
for a,b in itertools.combinations(N,2):
    straight=interior_manhattan(a,b)
    if straight==0:continue
    surf=D[a][b]
    ratio=surf/straight
    rows.append({'category':category(a,b),'ax':a[0],'ay':a[1],'az':a[2],'bx':b[0],'by':b[1],'bz':b[2],
                 'interior_mm':straight,'surface_mm':surf,'detour_ratio':ratio,
                 'interior_energy_fj':0.15+3.74*straight,'surface_energy_fj':0.15+3.74*surf})
with (OUT/'pair_detours.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
summ=[]
for cat in ['all','share_face','different_faces','opposite_faces']:
    rr=rows if cat=='all' else [r for r in rows if r['category']==cat]
    ratios=sorted(r['detour_ratio'] for r in rr)
    en_i=sum(r['interior_energy_fj'] for r in rr)/len(rr)
    en_s=sum(r['surface_energy_fj'] for r in rr)/len(rr)
    summ.append({'category':cat,'pairs':len(rr),'mean_detour':sum(ratios)/len(ratios),'median_detour':ratios[len(ratios)//2],
                 'p95_detour':ratios[int(.95*(len(ratios)-1))],'max_detour':max(ratios),
                 'mean_interior_energy_fj':en_i,'mean_surface_energy_fj':en_s,'mean_surface_penalty_pct':100*(en_s-en_i)/en_i})
with (OUT/'detour_summary.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=summ[0].keys());w.writeheader();w.writerows(summ)
print(open(OUT/'detour_summary.csv').read())
for r in sorted(rows,key=lambda x:x['detour_ratio'],reverse=True)[:10]: print(r)
