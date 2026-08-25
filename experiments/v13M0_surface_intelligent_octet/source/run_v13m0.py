import csv, itertools, json
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / 'results'
OUT.mkdir(parents=True, exist_ok=True)

# Preserved GVS energy proxies, fJ.
E_LONG_SELECT = 680.0
E_LEASE = 106.8
E_GRAMMAR = 134.0
E_TEMPLATE = 0.644
E_MYELIN = 0.0132
E_CHECKPOINT = 134.0
E_DIRECT = 0.15
E_SPINE = 0.67
E_ELEC_PER_MM = 3.74
E_ELEC_BASE = 0.15
E_OPT_BASE = 10.862
E_OPT_PER_MM = 0.0094
E_OPT_WRITE = 1000.0

PRIMS = ('G0','G1','T0','T1','M0','M1','C','B')
CORE = {
    'G0': E_GRAMMAR, 'G1': E_GRAMMAR,
    'T0': E_TEMPLATE, 'T1': E_TEMPLATE,
    'M0': E_MYELIN, 'M1': E_MYELIN,
    'C': E_CHECKPOINT, 'B': E_CHECKPOINT,
}

WORKLOADS = {
  'motif_local': {
    ('G0','T0'):4, ('G1','T1'):4,
    ('T0','M0'):3, ('T1','M1'):3,
    ('M0','C'):3, ('M1','C'):3,
    ('C','B'):2, ('G0','C'):1, ('G1','C'):1,
  },
  'fanout_context': {
    ('C','G0'):4, ('C','G1'):4, ('C','T0'):3, ('C','T1'):3,
    ('G0','M0'):2, ('G1','M1'):2, ('M0','B'):2, ('M1','B'):2,
    ('T0','B'):1, ('T1','B'):1,
  },
  'mixed_reasoning': {
    ('G0','T0'):3, ('T0','M0'):2, ('M0','C'):2,
    ('G1','T1'):3, ('T1','M1'):2, ('M1','C'):2,
    ('G0','G1'):1, ('T0','T1'):1, ('C','B'):3,
    ('G0','B'):1, ('G1','B'):1,
  },
  'cross_region_stress': {
    ('G0','M1'):3, ('G1','M0'):3, ('T0','G1'):3, ('T1','G0'):3,
    ('M0','T1'):3, ('M1','T0'):3, ('C','G0'):2, ('C','G1'):2,
    ('B','T0'):2, ('B','T1'):2,
  }
}

FLAT = [(x,y,0) for y in range(2) for x in range(4)]
CUBE = [(x,y,z) for z in range(2) for y in range(2) for x in range(2)]

def manhattan(a,b):
    return sum(abs(x-y) for x,y in zip(a,b))

def adjacent(a,b):
    return manhattan(a,b) == 1

def route_energy(a,b):
    return E_DIRECT if adjacent(a,b) else E_SPINE

def optimize(coords, edges):
    fixed = {PRIMS[0]: coords[0]}
    rest_prims = PRIMS[1:]
    best = None
    for perm in itertools.permutations(coords[1:]):
        placement = dict(fixed)
        placement.update(zip(rest_prims, perm))
        comm = 0.0; direct_events=0; spine_events=0; weighted_hops=0
        for (u,v),w in edges.items():
            a,b=placement[u],placement[v]
            re=route_energy(a,b)
            comm += w*re
            weighted_hops += w*manhattan(a,b)
            if adjacent(a,b): direct_events += w
            else: spine_events += w
        key=(comm, weighted_hops)
        if best is None or key < best[0]:
            best=(key,placement,direct_events,spine_events,weighted_hops)
    return best

def core_episode_energy():
    return sum(CORE.values())

rows=[]
placements={}
for wname,edges in WORKLOADS.items():
    for topo,coords in [('flat_2x4',FLAT),('surface_2x2x2',CUBE)]:
        key,place,direct,spine,hops=optimize(coords,edges)
        comm=key[0]
        local_core=core_episode_energy()
        shared = E_LONG_SELECT + E_LEASE + local_core + comm
        independent = len(PRIMS)*E_LONG_SELECT + local_core + comm
        rows.append({
            'workload':wname,'topology':topo,
            'direct_events':direct,'spine_events':spine,
            'weighted_hops':hops,'comm_fj':comm,
            'core_fj':local_core,'shared_region_fj':shared,
            'independent_select_fj':independent,
            'lease_saving_pct':100*(independent-shared)/independent,
        })
        placements[f'{wname}:{topo}']={k:list(v) for k,v in place.items()}

by={(r['workload'],r['topology']):r for r in rows}
for wname in WORKLOADS:
    f=by[(wname,'flat_2x4')]; h=by[(wname,'surface_2x2x2')]
    h['comm_vs_flat_pct']=100*(f['comm_fj']-h['comm_fj'])/f['comm_fj'] if f['comm_fj'] else 0
    f['comm_vs_flat_pct']=0.0

with (OUT/'placement_energy.csv').open('w',newline='') as fp:
    fields=list(rows[0].keys())
    w=csv.DictWriter(fp,fieldnames=fields);w.writeheader();w.writerows(rows)
(OUT/'placements.json').write_text(json.dumps(placements,indent=2)+'\n')

def eelec(d): return E_ELEC_BASE + E_ELEC_PER_MM*d
def eopt(d,uses): return E_OPT_BASE + E_OPT_PER_MM*d + E_OPT_WRITE/uses
opt_rows=[]
for d in [1,2,5,10,15,20]:
    for uses in [8,16,32,64,128,256]:
        ee=eelec(d); eo=eopt(d,uses)
        opt_rows.append({'distance_mm':d,'uses':uses,'electrical_fj_per_use':ee,'optical_amortized_fj_per_use':eo,'optical_economic':eo<ee,'saving_pct':100*(ee-eo)/ee})
with (OUT/'optical_break_even.csv').open('w',newline='') as fp:
    w=csv.DictWriter(fp,fieldnames=opt_rows[0].keys());w.writeheader();w.writerows(opt_rows)

outer=280.0; total=525.76
cap=[]
for reserve in [0.2,0.3,0.4,0.5]:
    usable=total*(1-reserve)
    cap.append({'service_reserve_pct':100*reserve,'usable_all_surface_mm2':usable,'outer_only_mm2':outer,'capacity_ratio_vs_outer':usable/outer})
with (OUT/'surface_capacity.csv').open('w',newline='') as fp:
    w=csv.DictWriter(fp,fieldnames=cap[0].keys());w.writeheader();w.writerows(cap)

print(json.dumps({'rows':rows,'optical':opt_rows,'capacity':cap},indent=2))
