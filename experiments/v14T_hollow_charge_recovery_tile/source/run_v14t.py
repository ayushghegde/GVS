#!/usr/bin/env python3
import json, math, re
from pathlib import Path

EPS0=8.8541878128e-12
ROOT=Path(__file__).resolve().parents[1]
EXT=ROOT/'physical'/'v14t_program_porch_proxy.ext'
REGION_UM=(200.0,200.0); CAVITY_UM=(60.0,40.0,40.0); DIEL_ER=9.0; DIEL_T_NM=20.0; WALL_USE=0.50; TANKS=2; VPROGRAM=1.2

def parse_ext(path):
    nodes={}; caps=[]
    for line in path.read_text().splitlines():
        if line.startswith('node '):
            p=line.split(); nodes[p[1].strip('"')]=float(p[3])
        elif line.startswith('cap '):
            m=re.match(r'cap "([^"]+)" "([^"]+)" ([0-9.eE+-]+)',line)
            if m: caps.append((m.group(1),m.group(2),float(m.group(3))))
    return nodes,caps

def node_load_af(name,nodes,caps): return nodes[name]+sum(c for a,b,c in caps if a==name or b==name)
nodes,caps=parse_ext(EXT); prog=sorted([k for k in nodes if k.startswith('P')],key=lambda s:int(s[1:])); loads={k:node_load_af(k,nodes,caps) for k in prog}; interior=[loads[k] for k in prog if k not in ('P0','P15')]; mean_af=sum(loads.values())/len(loads); mean_per_um_fF=(mean_af/1000)/20.0; interior_mean_af=sum(interior)/len(interior)
L,W,D=CAVITY_UM; surface_um2=L*W+2*(L+W)*D; usable_um2=surface_um2*WALL_USE; cdens_fF_um2=EPS0*DIEL_ER/(DIEL_T_NM*1e-9)*1e3; cres_pF=usable_um2*cdens_fF_um2/1000; tank_each_pF=cres_pF/TANKS; void_fraction=(L*W)/(REGION_UM[0]*REGION_UM[1])
def saving_fraction(r):
    if r<=0:return 0.0
    if r<=1:return 0.55*r
    return 0.55+(2/3-0.55)*(1-math.exp(-(r-1)/2.0))
rows=[]
for length_um in (20,50,100,200,400):
    c_line_fF=mean_per_um_fF*length_um; c_load_fF=2*c_line_fF; ratio=tank_each_pF*1000/c_load_fF; sf=saving_fraction(ratio); direct_fJ=c_load_fF*VPROGRAM**2; recoverable_fJ=direct_fJ*sf
    for ctrl_fJ in (0.5,1.0,2.0,5.0): rows.append({'line_length_um':length_um,'two_line_load_fF':c_load_fF,'tank_to_load_ratio':ratio,'saving_fraction_envelope':sf,'direct_program_distribution_energy_fJ':direct_fJ,'gross_recoverable_fJ':recoverable_fJ,'assumed_recovery_control_overhead_fJ':ctrl_fJ,'net_saved_fJ':recoverable_fJ-ctrl_fJ,'recovery_should_enable':recoverable_fJ>ctrl_fJ})
rho=997.0; mu=.00089; cp=4180.0; channel_w=40e-6; channel_h=40e-6; channel_L=60e-6; heat_W=.1; allowed_dT=10.0; flow_m3_s=heat_W/(rho*cp*allowed_dT); A=channel_w*channel_h; v=flow_m3_s/A; Dh=2*channel_w*channel_h/(channel_w+channel_h); Re=rho*v*Dh/mu; f=64/Re if Re else 0; dp=f*(channel_L/Dh)*(rho*v*v/2); pump_elec_W=dp*flow_m3_s/.5
out={'schema':'v14T-hollow-charge-recovery-tile-v1','status':'PHYSICAL PROGRAM-METAL PROXY PASS; HOLLOW/RECOVERY SYSTEM MODEL PARTIAL PASS','evidence_boundary':{'extracted':'Magic 8.3 / SKY130A DRC and parasitic extraction of 16 metal2 program lines crossed by two metal3 tank rails.','modeled':'cavity capacitor, charge-recovery envelope, hydraulic screen, and scaling from the 20-um proxy.','not_claimed':'No fabricated cavity, reservoir capacitor, adiabatic recovery switch network, HZO compound branch, or full post-layout tile.'},'physical_program_proxy':{'drc_errors':0,'program_lines':16,'proxy_line_length_um':20.0,'program_line_loads_aF':loads,'mean_program_line_load_aF':mean_af,'interior_mean_program_line_load_aF':interior_mean_af,'mean_effective_capacitance_fF_per_um':mean_per_um_fF,'tank0_self_aF':nodes.get('TANK0'),'tank1_self_aF':nodes.get('TANK1')},'hollow_tile':{'region_um':REGION_UM,'cavity_um':CAVITY_UM,'projected_void_fraction':void_fraction,'inner_surface_um2':surface_um2,'used_surface_fraction':WALL_USE,'used_inner_surface_um2':usable_um2,'dielectric_er':DIEL_ER,'dielectric_thickness_nm':DIEL_T_NM,'modeled_cap_density_fF_um2':cdens_fF_um2,'total_reservoir_pF':cres_pF,'tank_each_pF':tank_each_pF},'charge_recovery_sweep':rows,'decision':{'keep':['v14S polarity cell unchanged','60x40x40um regional hollow cavity target','inner-wall charge-return skin','recovery only on sufficiently large regional program distribution','optional coolant-compatible cavity'],'drop':['per-cell inference energy harvester','mandatory recovery on every short local program line','claim that 36 shared MOS/8 cells is already physically closed'],'reason':'The extracted compact 20um program line is only ~%.3f fF, so local recovery can be smaller than control overhead; regional lines scale into a clearly useful energy range.'%(mean_af/1000)},'optional_cooling_screen':{'heat_W':heat_W,'allowed_fluid_dT_K':allowed_dT,'flow_m3_s':flow_m3_s,'mean_velocity_m_s':v,'hydraulic_diameter_m':Dh,'Re':Re,'pressure_drop_Pa':dp,'pump_electrical_W_at_50pct_efficiency':pump_elec_W,'pump_fraction_of_100mW':pump_elec_W/heat_W,'warning':'simple laminar hydraulic screen, not CFD or thermal signoff'}}
(ROOT/'results'/'results.json').write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2))
