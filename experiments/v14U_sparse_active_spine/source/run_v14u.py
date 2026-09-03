import json, math, numpy as np
from pathlib import Path

# v14U reproducible engineering screen.
# No fabricated HZO/rectifier result is claimed.
RNG=np.random.default_rng(14021)
N=400_000
VSEL=1.2
VHALF=0.75
C_HZO=8.8541878128e-12*25*(12e-9*12e-9)/(4e-9)

def rc_v(v,r,c,t):
    return v*(1-np.exp(-t/(r*c)))

rows=[]
for t_ns in (10,20,30,40,60,80,100):
    r_on=np.exp(RNG.normal(np.log(1e8),0.28,N))
    r_off=np.exp(RNG.normal(np.log(1e11),0.55,N))
    c=C_HZO*np.clip(RNG.normal(1,0.10,N),0.65,1.35)
    vs=rc_v(VSEL,r_on,c,t_ns*1e-9)
    vh=rc_v(VHALF,r_off,c,t_ns*1e-9)
    ok=(vs>=0.6)&(vh<=0.2)
    rows.append({'pulse_ns':t_ns,'joint_pass':float(ok.mean()),'selected_fail':float((vs<0.6).mean()),'half_fail':float((vh>0.2).mean()),'half_p999_V':float(np.quantile(vh,.999)),'selected_p001_V':float(np.quantile(vs,.001))})

r=np.random.default_rng(14022); M=500_000
span=np.clip(r.normal(19e-6,1e-6,M),15e-6,23e-6)
t=np.clip(r.normal(5e-6,.5e-6,M),3e-6,7e-6)
E=np.clip(r.normal(160e9,8e9,M),130e9,190e9)
p=np.clip(r.normal(101325,15000,M),50_000,160_000)
nu=.22
D=E*t**3/(12*(1-nu**2))
w=0.00406*p*span**4/D
stress=.308*p*span**2/t**2
mech={'trials':M,'pass_fraction':float(np.mean((w<50e-9)&(stress<100e6))),'deflection_p99_nm':float(np.quantile(w,.99)*1e9),'deflection_max_nm':float(w.max()*1e9),'stress_p99_MPa':float(np.quantile(stress,.99)/1e6),'stress_max_MPa':float(stress.max()/1e6)}

physical={'8x8':{'drc_errors':0,'row_R_ohm_mean':179.0,'col_R_ohm_mean':31.0,'row_load_fF_mean':15.964,'col_load_fF_mean':17.458,'row_RC_ps':2.86,'col_RC_ps':0.54},'16x16':{'drc_errors':0,'row_load_fF_mean':16.346,'col_load_fF_mean':17.771,'row_RC_ps':2.93,'col_RC_ps':0.55}}
cr=physical['16x16']
Csum=(16*cr['row_load_fF_mean']+16*cr['col_load_fF_mean'])*1e-15
Edirect=.5*Csum*(.8**2)*1e15
recovery=2/3
out={'schema':'v14U-sparse-active-spine-v1','evidence_boundary':{'physical':'SKY130 metal-grid extraction values are preserved measurements from the v14U run; HZO/FIC/rectifier/mechanical/energy are engineering models.','not_claimed':'No fabricated 4-nm HZO FIC, no fabricated edge rectifier, no extracted <=52-MOS active-spine PEX.'},'physical_program_grids':physical,'pulse_sweep':rows,'mechanical_HRM':mech,'dynamic_precharge_decode':{'evaluate_ns':88.85,'write_ns':30.0,'service_ns':118.85,'distribution_energy_fJ_proxy':Edirect,'gross_recovery_fJ_proxy':Edirect*recovery,'net_with_100fJ_control_fJ_proxy':Edirect*(1-recovery)+100},'structural_accounting':{'semantic_cell_MOS':0,'v14S_shared_MOS_equiv_per_cell':5.0,'v14U_64cell_proxy':0.75,'v14U_256cell_target':52/256},'decision':{'keep':['electric-polarity route memory','field-isolated HZO collar','guided volatile gap','dry ribbed hollow reservoir','dynamic precharge decode','charge return','sparse regional active gain only'],'reject':['per-cell MOS selector','100ns write pulse','wet electrical cavity','HZO direct chemical contact with Ag gap']}}
root=Path(__file__).resolve().parents[1]
(root/'results').mkdir(exist_ok=True)
(root/'results'/'results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
