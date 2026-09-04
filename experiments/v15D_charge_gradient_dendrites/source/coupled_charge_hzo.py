#!/usr/bin/env python3
import numpy as np, math, json
Qe=1.602176634e-19
EPS0=8.8541878128e-12

def simulate(n=40000,seed=15101,sign=1,start_pol=0.0,replays=14,spacing_ns=100.0,dt_ns=5.0):
    rng=np.random.default_rng(seed)
    # 4-nm HZO collar; parameters anchored to the same envelope used in v15C.
    C=np.clip(24e-18*np.exp(rng.normal(0,0.08,n)),18e-18,32e-18)
    epsr=np.clip(rng.normal(25,2.0,n),20,31)
    area=C*4e-9/(EPS0*epsr)
    Pr=np.clip(rng.normal(0.125,0.018,n),0.08,0.18) # C/m2
    Qpr=Pr*area
    # Seven domains, signed state in [-1,1].
    z=np.array([-2.326,-1.282,-.524,0,.524,1.282,2.326])[:,None]
    Ea=np.clip(1.60+.35*z,.45,3.2)
    tau0=19*np.exp(rng.normal(0,.18,n))[None,:] # ns
    alpha=np.clip(rng.normal(3,.25,n),2.2,3.8)[None,:]
    beta=np.clip(rng.normal(2,.18,n),1.4,2.6)[None,:]
    p=np.full((7,n),start_pol,dtype=float)
    # Free electrode charge initially screens current polarization.
    Qfree=Qpr*p.mean(0)
    R=np.clip(120e9*np.exp(rng.normal(0,.30,n)),45e9,350e9)
    # Residual charge captured from each guided-gap replay. ~0.3% of inherited event charge.
    inj_e=np.clip(rng.normal(22.5,3.0,(replays,n)),12,34)
    Qinj=sign*inj_e*Qe
    steps=int(round(spacing_ns/dt_ns))
    vmax=np.zeros(n); vmin=np.zeros(n)
    for r in range(replays):
        Qfree += Qinj[r]
        for _ in range(steps):
            Pfrac=p.mean(0)
            V=(Qfree-Qpr*Pfrac)/C
            vmax=np.maximum(vmax,V); vmin=np.minimum(vmin,V)
            # signed domain switching
            E=np.abs(V)[None,:]/4e-7/1e6
            ratio=Ea/np.maximum(E,.05)
            tau=tau0*np.exp(np.minimum(60,ratio**alpha))
            # small-step stretched switching probability
            f=1-np.exp(-((dt_ns/np.maximum(tau,1e-12))**beta))
            pos=V>=0
            p=np.where(pos[None,:], p+(1-p)*f, p+(-1-p)*f)
            # leakage acts on actual electrode voltage, automatically supplying/removing screening charge
            Qfree += -(V/R)*(dt_ns*1e-9)
    P_end=p.mean(0)
    V_end=(Qfree-Qpr*P_end)/C
    # let 10us pass with polarization fixed enough for this leakage screen
    tau_rc=R*C
    V10=V_end*np.exp(-10e-6/tau_rc)
    return {
      'n':n,'sign':sign,'start_pol':start_pol,'replays':replays,
      'final_pol_q':np.quantile(P_end,[.001,.01,.5,.99,.999]).tolist(),
      'pass_pos_ge_0p8':float(np.mean(P_end>=.8)),
      'pass_neg_le_m0p8':float(np.mean(P_end<=-.8)),
      'peak_v_q':np.quantile(vmax,[.001,.01,.5,.99,.999]).tolist(),
      'min_v_q':np.quantile(vmin,[.001,.01,.5,.99,.999]).tolist(),
      'end_v_q':np.quantile(V_end,[.001,.01,.5,.99,.999]).tolist(),
      'v10us_abs_q':np.quantile(np.abs(V10),[.5,.99,.999]).tolist(),
      'inj_e_total_q':np.quantile(np.sum(inj_e,axis=0),[.001,.5,.999]).tolist(),
      'qpr_e_q':np.quantile(Qpr/Qe,[.001,.5,.999]).tolist(),
    }

if __name__=='__main__':
    out={
      'new_positive':simulate(sign=1,start_pol=0.0),
      'new_negative':simulate(sign=-1,start_pol=0.0,seed=15102),
      'overwrite_old_positive_with_negative':simulate(sign=-1,start_pol=.85,seed=15103,replays=18),
      'one_wrong_positive':simulate(sign=1,start_pol=0.0,seed=15104,replays=1),
    }
    print(json.dumps(out,indent=2))
