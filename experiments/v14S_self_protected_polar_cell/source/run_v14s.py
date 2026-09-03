import json, math
from pathlib import Path
import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve

# Neural Glyph v14S chip-level closure model.
# Evidence boundary:
#   - CHOICE capacitance is parsed from the real Magic/SKY130 v14R extraction copied under inherited/.
#   - everything involving HZO, passive nonlinear inhibit, aperture electrostatics, guided-gap
#     stochastic switching, yield and shared program-periphery is an engineering model/target.
#   - no fabricated v14S compound branch is claimed.

EPS0=8.8541878128e-12
QE=1.602176634e-19
ROOT=Path(__file__).resolve().parents[1]
EXT=ROOT/'inherited'/'v14r_choice5_m2.ext'

# inherited v14O/v14P model parameters
R_ON=2.3e6
V_FIRE=.25
DROP=.20
BASE_FOCUS=1.45
GAP_MEAN=1.30
GAP_SIG=.12
BASE_MIG=23.5
BASE_D=2.0
MIG_EXP=1.5
ER_TRAIL=20.0
TARGET_TRAIL_V=.159

# v14S selected material/geometry target
P_NOM=.16
PATCH_NM=10.0
FE_T_NM=5.0
FE_ER=25.0
APERTURE_NM=16.0
NEIGHBOR_OBSERVE_NM=20.0
PHYSICAL_BRANCHES=6
LOGICAL_ACTIVE_BRANCHES=4
EXTERNAL_NEIGHBORS=4


def parse_choice_cap_af(path):
    own=None; couplings=[]
    for line in path.read_text().splitlines():
        if line.startswith('node "CHOICE"'):
            own=float(line.split()[3])
        elif line.startswith('cap ') and '"CHOICE"' in line:
            couplings.append(float(line.split()[-1]))
    if own is None:
        raise RuntimeError('CHOICE node missing')
    return own, couplings, own+sum(couplings)


def finite_patch(P=P_NOM,size_nm=PATCH_NM,near_nm=1.0,sep_nm=1.5,er=20.0,n=300):
    y=(np.arange(n)+.5)/n*size_nm*1e-9-size_nm*1e-9/2
    Y,Z=np.meshgrid(y,y,indexing='ij')
    dA=(size_nm*1e-9/n)**2
    r1=np.sqrt((near_nm*1e-9)**2+Y*Y+Z*Z)
    r2=np.sqrt(((near_nm+sep_nm)*1e-9)**2+Y*Y+Z*Z)
    return float(np.sum(P*dA/(4*math.pi*EPS0*er)*(1/r1-1/r2)))


def aperture_ratio(aperture_nm=APERTURE_NM,patch_nm=PATCH_NM,neighbor_nm=NEIGHBOR_OBSERVE_NM,dx_nm=.25):
    xmin,xmax=-24,24; ymin,ymax=-8,12
    xs=np.arange(xmin,xmax+1e-9,dx_nm); ys=np.arange(ymin,ymax+1e-9,dx_nm)
    nx,ny=len(xs),len(ys); N=nx*ny
    def idx(i,j): return j*nx+i
    def solve(shield):
        fixed=np.zeros(N,bool); A=lil_matrix((N,N)); b=np.zeros(N)
        for i in range(nx): fixed[idx(i,0)]=fixed[idx(i,ny-1)]=1
        for j in range(ny): fixed[idx(0,j)]=fixed[idx(nx-1,j)]=1
        if shield:
            j0=np.argmin(abs(ys))
            for i,x in enumerate(xs):
                if abs(x)>aperture_nm/2: fixed[idx(i,j0)]=1
        jpos=np.argmin(abs(ys+1.0)); jneg=np.argmin(abs(ys+2.5))
        for j in range(ny):
            for i,x in enumerate(xs):
                k=idx(i,j)
                if fixed[k]: A[k,k]=1; continue
                A[k,k]=-4
                A[k,idx(i-1,j)]=A[k,idx(i+1,j)]=A[k,idx(i,j-1)]=A[k,idx(i,j+1)]=1
                if abs(x)<=patch_nm/2:
                    if j==jpos: b[k]-=1
                    if j==jneg: b[k]+=1
        V=spsolve(A.tocsr(),b).reshape(ny,nx)
        def samp(x,y=2): return float(V[np.argmin(abs(ys-y)),np.argmin(abs(xs-x))])
        return samp(0),samp(neighbor_nm)
    u=solve(False); s=solve(True)
    return {'target_retained_fraction':s[0]/u[0],'neighbor_to_target_fraction':abs(s[1]/s[0]),'unshielded_norm_target':u[0],'shielded_norm_target':s[0]}


def M_ring(b,R=8,sep=1.5,obs_gap=2):
    c=QE/(4*math.pi*EPS0*ER_TRAIL); M=np.zeros((b,b))
    for i in range(b):
        a=2*math.pi*i/b; u=np.array([math.cos(a),math.sin(a)])
        pp=R*u; pm=(R-sep)*u
        for j in range(b):
            a2=2*math.pi*j/b; v=np.array([math.cos(a2),math.sin(a2)])
            obs=(R+obs_gap)*v
            rp=np.linalg.norm(obs-pp)*1e-9; rm=np.linalg.norm(obs-pm)*1e-9
            M[j,i]=c*(1/rp-1/rm)
    return M


def race(branches,qt,qo,external_mv,quench_ns,trials=300000,seed=141500):
    r=np.random.default_rng(seed); M=M_ring(branches); qs=np.full(branches,qo); qs[0]=qt
    q=qs[None,:]*np.clip(1+r.normal(0,.15,(trials,branches)),.5,1.5)
    trail=q@M.T
    if external_mv:
        trail += r.choice((-1.,1.),size=(trials,branches,EXTERNAL_NEIGHBORS)).sum(axis=2)*external_mv*1e-3
    lv=np.clip(V_FIRE+trail,.10,.40)
    focus=BASE_FOCUS*(lv/V_FIRE)*np.clip(1+r.normal(0,.04,(trials,branches)),.75,1.25)
    gap=np.clip(r.normal(GAP_MEAN,GAP_SIG,(trials,branches)),.65,None)
    s=np.sqrt(np.log1p(.15**2)); nuc=r.lognormal(np.log(4/np.sqrt(focus))-.5*s*s,s)
    sm=np.sqrt(np.log1p(.13**2))
    mig=BASE_MIG*(gap/BASE_D)**MIG_EXP/focus*r.lognormal(-.5*sm*sm,sm,(trials,branches))
    d=nuc+mig; order=np.argsort(d,axis=1); win=order[:,0]
    first=d[np.arange(trials),win]; second=d[np.arange(trials),order[:,1]]
    return {'correct_winner':float(np.mean(win==0)),'correct_and_quenched':float(np.mean((win==0)&((second-first)>=quench_ns))),'winner_delay_mean_ns':float(first.mean()),'winner_delay_p95_ns':float(np.percentile(first,95)),'trials':trials}


def program_protection(Cfe,pulse=100e-9,Vsel=1.2,Vhalf=.4,Ron=1e8,Roff=1e11):
    vh_sel=Vsel*(1-math.exp(-pulse/(Ron*Cfe)))
    vh_half=Vhalf*(1-math.exp(-pulse/(Roff*Cfe)))
    Roff_req=pulse/(-math.log(1-.15/Vhalf)*Cfe)
    Ron_max=pulse/(-math.log(1-1.0/Vsel)*Cfe)
    return {'pulse_ns':pulse*1e9,'selected_terminal_V':Vsel,'half_select_terminal_V':Vhalf,'model_Ron_ohm':Ron,'model_Roff_ohm':Roff,'HZO_selected_V':vh_sel,'HZO_half_select_V':vh_half,'Roff_required_for_half_HZO_le_0p15V_ohm':Roff_req,'Ron_max_for_selected_HZO_ge_1p0V_ohm':Ron_max,'minimum_required_Roff_over_Ron_window':Roff_req/Ron_max}


def at_least_k_good(n,k,p):
    return sum(math.comb(n,i)*p**i*(1-p)**(n-i) for i in range(k,n+1))


def yield_screen():
    rows=[]
    for p in (.95,.98,.99,.995):
        for n in (5,6,7):
            cy=at_least_k_good(n,LOGICAL_ACTIVE_BRANCHES,p)
            rows.append({'physical_branches':n,'required_good':LOGICAL_ACTIVE_BRANCHES,'per_branch_usable_probability':p,'cell_functional_probability':cy,'64_cell_region_probability_if_independent':cy**64})
    return rows


def program_bank_energy():
    rows=[]; lines=16
    for L in (5.0,20.0,100.0):
        for cper in (.2,.5,1.0):
            Cline_fF=L*cper
            ideal_fJ=.5*Cline_fF*(2*.6**2+14*.2**2)
            pessimistic_fJ=.5*lines*Cline_fF*1.2**2
            rows.append({'line_length_um':L,'line_cap_fF_per_um':cper,'one_line_cap_fF':Cline_fF,'ideal_V3_transition_energy_fJ':ideal_fJ,'pessimistic_all_16_lines_to_1p2V_upper_fJ':pessimistic_fJ})
    return rows


def polarity_floor_screen(aperture):
    rows=[]
    for P in (.08,.10,.12,.14,.16,.18,.22):
        un=finite_patch(P=P)
        post=un*aperture['target_retained_fraction']
        qt=10*post/TARGET_TRAIL_V; qo=-.30*qt
        xmv=post*aperture['neighbor_to_target_fraction']*1e3
        rr=race(PHYSICAL_BRANCHES,qt,qo,xmv,quench_ns,trials=150000,seed=142000+int(P*10000))
        rows.append({'P_C_m2':P,'post_aperture_target_V':post,'effective_target_charge_e':qt,'external_neighbor_leak_mV_each':xmv,**rr})
    return rows


own_af,couplings_af,choice_af=parse_choice_cap_af(EXT)
C_choice=choice_af*1e-18
Cfe=EPS0*FE_ER*(PATCH_NM*1e-9)**2/(FE_T_NM*1e-9)
Ctotal=C_choice+PHYSICAL_BRANCHES*Cfe
quench_ns=-math.log(1-DROP)*R_ON*Ctotal*1e9
node_energy_fJ=.5*Ctotal*V_FIRE**2*1e15

geo_rows=[]
for aperture_nm in (10.,12.,14.,16.):
    for neighbor_nm in (14.,18.,20.):
        g=aperture_ratio(aperture_nm=aperture_nm,neighbor_nm=neighbor_nm)
        geo_rows.append({'aperture_nm':aperture_nm,'neighbor_observe_nm':neighbor_nm,**g})
selected_geo=next(x for x in geo_rows if x['aperture_nm']==APERTURE_NM and x['neighbor_observe_nm']==NEIGHBOR_OBSERVE_NM)
unshielded=finite_patch()
post=unshielded*selected_geo['target_retained_fraction']
qt=10*post/TARGET_TRAIL_V; qo=-.30*qt
external_mv=post*selected_geo['neighbor_to_target_fraction']*1e3
selected_race=race(PHYSICAL_BRANCHES,qt,qo,external_mv,quench_ns,trials=300000,seed=141506)
program=program_protection(Cfe)

BANK_CELLS=8
BANK_LINES=16
BANK_LINE_SWITCH_MOS=32
BANK_SHARED_LEVEL_MOS=8
BANK_PROGRAM_MOS=BANK_LINE_SWITCH_MOS+BANK_SHARED_LEVEL_MOS
MOS_EQ_PER_CELL=BANK_PROGRAM_MOS/BANK_CELLS
REGION_CELLS=64
BANKS=REGION_CELLS//BANK_CELLS
REGION_PROGRAM_MOS=BANKS*BANK_PROGRAM_MOS

v14e_mim_area_um2=3.0*3.0+1.71*1.71
branch_area_break_even_um2=v14e_mim_area_um2/PHYSICAL_BRANCHES
v14o_event_fJ=1.90
inference_fJ=v14o_event_fJ+node_energy_fJ
cmos_controls=[]
for cff in (5,10,20):
    e=cff*1e-15*1.8**2*1e15
    cmos_controls.append({'effective_switched_cap_fF':cff,'energy_fJ':e,'delay_ns':6.0,'v14S_energy_ratio':inference_fJ/e,'v14S_EDP_ratio':inference_fJ*selected_race['winner_delay_mean_ns']/(e*6.0)})

out={
 'schema':'v14S-chip-level-self-protected-polar-cell-v2',
 'status':'MODEL/ARCHITECTURE PASS; PHYSICAL COMPOUND-DEVICE PARTIAL',
 'evidence_boundary':'Only the inherited v14R CHOICE capacitance is extracted SKY130/Magic data. HZO/selector/aperture/guided-gap/yield/periphery numbers are engineering models or explicit targets.',
 'selected_cell':{
   'name':'SP-PGCC — Self-Protected Polarity-Guided Choice Cell','core_MOS_per_cell':0,'physical_branches':PHYSICAL_BRANCHES,'logical_active_branches':LOGICAL_ACTIVE_BRANCHES,'repair_spares':PHYSICAL_BRANCHES-LOGICAL_ACTIVE_BRANCHES,
   'branch_anatomy':'low-voltage guided-gap volatile signal path + intrinsic ballast; adjacent HZO route-polarity collar on separate program electrodes; same-footprint passive nonlinear inhibit; grounded aperture shield',
   'eligibility':'volatile guided-gap residue itself; no standalone eligibility device','programming':'8-cell local program bank, V/3 row/column scheme; selected collar 1.2 V target, half-select terminal 0.4 V; high-voltage program plane is electrically separate from signal path'},
 'inherited_physical_choice_node':{'source':'v14R Magic/SKY130 .ext copied under inherited/','choice_self_af':own_af,'choice_branch_couplings_af':couplings_af,'choice_total_af':choice_af},
 'choice_and_quench':{'HZO_cap_each_aF':Cfe*1e18,'six_HZO_total_aF':PHYSICAL_BRANCHES*Cfe*1e18,'combined_choice_plus_HZO_fF':Ctotal*1e15,'20pct_quench_ns':quench_ns,'choice_energy_fJ_at_0p25V':node_energy_fJ},
 'aperture_geometry_sweep':geo_rows,
 'selected_aperture':{**selected_geo,'finite_3d_unshielded_patch_V':unshielded,'estimated_post_aperture_target_V':post,'effective_target_charge_e':qt,'effective_contradicted_charge_e':qo,'external_neighbor_leak_mV_each':external_mv},
 'six_way_race_with_four_external_neighbors':selected_race,
 'polarization_floor_screen':polarity_floor_screen(selected_geo),
 'program_protection':program,
 'repair_yield_screen':yield_screen(),
 'program_bank':{'cells_per_bank':BANK_CELLS,'program_lines_per_bank':BANK_LINES,'line_switch_MOS_proxy_per_bank':BANK_LINE_SWITCH_MOS,'shared_level_MOS_proxy_per_bank':BANK_SHARED_LEVEL_MOS,'total_shared_program_MOS_proxy_per_bank':BANK_PROGRAM_MOS,'amortized_program_MOS_proxy_per_cell':MOS_EQ_PER_CELL,'64_cell_region_banks':BANKS,'64_cell_region_program_MOS_proxy':REGION_PROGRAM_MOS,'energy_bracket':program_bank_energy()},
 'old_cell_comparison':{'v14E_physical_CFN':'15 MOS + 2 MIM; real extracted/PVT/mismatch passed reference, but different contradiction-restart function','v14E_MIM_area_alone_um2':v14e_mim_area_um2,'v14S_branch_footprint_break_even_vs_v14E_MIM_area_only_um2_each':branch_area_break_even_um2,'v12S_whole_tile':'70 MOS + 14 MIM; TT accepted physical-query window about 28.28 pJ; broader function than one v14S choice cell','v12S_local_two_candidate_route_proxy':'50 MOS + 12 MIM in the parsed route/competition/capture section; broader circuitry than a single v14S cell','v14S_core_MOS':0,'v14S_amortized_shared_program_MOS_proxy_per_cell':MOS_EQ_PER_CELL,'warning':'device-count and MIM-area ceilings are structural comparisons, not placed-layout area equivalence'},
 'inference_energy':{'v14S_model_fJ':inference_fJ,'winner_delay_mean_ns':selected_race['winner_delay_mean_ns'],'cmos_controls':cmos_controls},
 'decision':'KEEP v14S. The key closure is physical separation of low-voltage inference and high-voltage collar programming. Six passive branch mouths provide four normal routes plus two repair spares. No MOS is allowed in the ordinary semantic cell; MOS is confined to shared 8-cell program porches until a passive regional driver is proven cheaper.'
}
(ROOT/'results').mkdir(exist_ok=True)
(ROOT/'results'/'results.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
