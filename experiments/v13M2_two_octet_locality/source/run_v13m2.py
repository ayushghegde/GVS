import csv
from pathlib import Path
OUT=Path(__file__).resolve().parents[1]/'results'; OUT.mkdir(parents=True,exist_ok=True)
E_SEL=680.0
E_LEASE=106.8
E_OCTET_CORE=537.3144
E_REMOTE_HALF=E_OCTET_CORE/2
E_SPINE=0.67

def elec(d): return 0.15+3.74*d
def optical(d,uses): return 10.862+0.0094*d+1000.0/uses
ROUTES={
    'near_spine': E_SPINE,
    'opposite_surface_chord_2mm': elec(2),
    'bad_surface_detour_10mm': elec(10),
    'hot_optical_10mm_64use': optical(10,64),
}
rows=[]
for p in [0.0,0.1,0.25,0.5,0.75,1.0]:
    for route_name,eroute in ROUTES.items():
        indep=(8*E_SEL+E_OCTET_CORE) + p*(4*E_SEL+E_REMOTE_HALF+eroute)
        v13m=(E_SEL+E_LEASE+E_OCTET_CORE) + p*(eroute+E_SEL+E_LEASE+E_REMOTE_HALF)
        rows.append({
            'cross_fraction':p,'route':route_name,'route_fj':eroute,
            'independent_fj_per_episode':indep,
            'v13m_fj_per_episode':v13m,
            'saving_pct':100*(indep-v13m)/indep,
            'long_selections_independent':8+4*p,
            'long_selections_v13m':1+p,
        })
with (OUT/'locality_sweep.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
route_cmp=[]
for p in [0.1,0.25,0.5,0.75,1.0]:
    base=[r for r in rows if r['cross_fraction']==p and r['route']=='bad_surface_detour_10mm'][0]
    for name in ['opposite_surface_chord_2mm','hot_optical_10mm_64use']:
        r=[x for x in rows if x['cross_fraction']==p and x['route']==name][0]
        route_cmp.append({'cross_fraction':p,'replacement':name,'v13m_fj':r['v13m_fj_per_episode'],
                          'vs_surface_detour_fj_saved':base['v13m_fj_per_episode']-r['v13m_fj_per_episode'],
                          'vs_surface_detour_pct':100*(base['v13m_fj_per_episode']-r['v13m_fj_per_episode'])/base['v13m_fj_per_episode']})
with (OUT/'route_choice.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=route_cmp[0].keys());w.writeheader();w.writerows(route_cmp)
print(open(OUT/'locality_sweep.csv').read())
print(open(OUT/'route_choice.csv').read())
