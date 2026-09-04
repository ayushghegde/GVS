#!/usr/bin/env python3
from __future__ import annotations
import json, math, re, subprocess, importlib.util
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'results'/'results.json'
NG=Path('/mnt/data/ngbuild/install/bin/ngspice')
Qe=1.602176634e-19

# v15D selected architecture
# DCG  = Dendritic Charge Gradient: repeated validated firing leaves signed fast charge on the existing dendrite/HZO collar.
# DTM  = Dual-Time Memory: fast free/ionic charge decays; HZO polarization is the slow consolidated floor in the SAME collar.
# NBR  = Need-Based Replay: unknown/low-margin/mismatch states make the fabric replay candidates; known high-margin routes do not.
# SBR  = Spare Branch Recruitment: two retained repair branches are used before a hardware expansion request is emitted.
# No FITA, no tunnel program path, no per-branch program transistor, no high-voltage branch-address decoder.


def load_coupled_module():
    p=ROOT/'source'/'coupled_charge_hzo.py'
    spec=importlib.util.spec_from_file_location('coupled_charge_hzo',p)
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def choice_mc(n=300000,seed=15052,branches=6):
    rng=np.random.default_rng(seed)
    target=rng.integers(0,4,n); rows=np.arange(n)
    pslow=np.zeros((n,branches))
    pslow[rows,target]=np.clip(rng.normal(0.90,0.09,n),0.55,1.0)
    eff=0.50*pslow + rng.normal(0,0.025,(n,branches))
    gamma=np.clip(rng.normal(28.0,2.0,(n,1)),22,34)
    tau0=np.exp(rng.normal(math.log(18.0),0.10,(n,branches)))
    mean_tau=tau0*np.exp(-gamma*eff)
    lat=rng.exponential(mean_tau)
    winner=np.argmin(lat,axis=1)
    competitor=np.max(np.where(np.arange(branches)[None,:]==target[:,None],-1e9,eff),axis=1)
    margin=eff[rows,target]-competitor
    return {
      'trials':n,'seed':seed,
      'correct_choice_pass':float(np.mean(winner==target)),
      'spare_branch_false_win_rate':float(np.mean(winner>=4)),
      'field_margin_V_q':{k:float(v) for k,v in zip(['p001','p01','median','p99'],np.quantile(margin,[.001,.01,.5,.99]))},
      'winning_latency_ns_q':{k:float(v) for k,v in zip(['p01','median','p99'],np.quantile(lat[rows,winner],[.01,.5,.99]))},
      'note':'Compact stochastic guided-gap nucleation model; no per-branch transistor is implied.'
    }


def run_spice_decks():
    out={}
    for name in ['charge_burst','single_wrong_decay','choice_compact']:
        cir=ROOT/'spice'/f'{name}.cir'; log=ROOT/'spice'/f'{name}.log'
        cp=subprocess.run([str(NG),'-b','-o',str(log),str(cir)],capture_output=True,text=True,timeout=30)
        txt=log.read_text(errors='ignore') if log.exists() else cp.stdout+cp.stderr
        vals={}
        keys={'charge_burst':['v1','v4','v8','v12','v14','v5u','v10u'],
              'single_wrong_decay':['v50n','v5u','v10u'],
              'choice_compact':['vchoice','vax']}[name]
        for key in keys:
            m=re.search(rf'^{key}\s*=\s*([-+0-9.eE]+)',txt,re.I|re.M)
            vals[key]=float(m.group(1)) if m else None
        if name=='choice_compact' and vals.get('vchoice') is not None:
            dv=vals['vax']-vals['vchoice']
            biases=[0.30,0.02,0.0,-0.02]
            currents=[]
            for b in biases:
                r=1e9*math.exp(-20*b); currents.append(dv/r)
            vals['branch_current_A']=currents
            vals['winner_to_runner_current_ratio']=currents[0]/max(currents[1:])
        out[name]={'returncode':cp.returncode,'values':vals,'circuit':cir.name,'log':log.name}
    return out


def behavior(relations=256,episodes=650,seed=15053):
    rng=np.random.default_rng(seed); b=6
    truth=rng.integers(0,4,relations)
    slow=np.zeros((relations,b)); committed=np.full(relations,-1,dtype=int)
    known=rng.random(relations)<0.70
    slow[np.arange(relations)[known],truth[known]]=np.clip(rng.normal(.88,.06,np.sum(known)),.70,1)
    committed[known]=truth[known]
    evidence=np.zeros((relations,b)); provisional=np.zeros((relations,b))
    wrong=[set() for _ in range(relations)]
    change_ids=rng.choice(relations,size=int(.20*relations),replace=False)
    novel_ids=rng.choice([i for i in range(relations) if i not in set(change_ids)],size=3,replace=False)
    durable_events=0; pos_replays=0; neg_replays=0; need_events=0; blocked=0; hw_requests=set(); spare_recruits=0
    for ep in range(episodes):
        if ep==240:
            for i in change_ids:
                old=truth[i]; truth[i]=rng.choice([x for x in range(4) if x!=old])
        for i in novel_ids:
            if ep>=350: truth[i]=6
        for i in rng.permutation(relations):
            if truth[i]>=6:
                if ep>470: hw_requests.add(int(i))
                continue
            context=rng.normal(0,.055,b); context[truth[i]]+=.16
            score=context+.50*slow[i]+.10*provisional[i]
            order=np.argsort(score)[::-1]; top,second=order[:2]
            margin=score[top]-score[second]
            need=(committed[i]<0) or (top!=truth[i]) or (margin<.18)
            if need: need_events+=1
            candidates=order[:4] if need else order[:1]
            found=None
            for cand in candidates:
                if cand==truth[i]: found=int(cand); break
                wrong[i].add(int(cand)); provisional[i,cand]=max(-1.0,provisional[i,cand]-.20)
            trusted=rng.random()<.16
            if not trusted: blocked+=1
            if found is not None:
                provisional[i,found]=min(1.0,provisional[i,found]+(.22 if trusted else .035))
                if trusted:
                    evidence[i]*=.95; evidence[i,found]+=1
            eo=np.argsort(evidence[i]); best,second_e=eo[-1],eo[-2]
            emargin=evidence[i,best]-evidence[i,second_e]
            if trusted and evidence[i,best]>=3 and emargin>=2 and provisional[i,best]>=.55 and committed[i]!=best:
                old=committed[i]
                if old>=0 and old!=best:
                    slow[i,old]=max(-.25,slow[i,old]-.70); neg_replays+=26; wrong[i].add(int(old))
                slow[i,best]=max(slow[i,best],.88); committed[i]=best
                durable_events+=1; pos_replays+=24; provisional[i,best]*=.20
            if ep>300 and committed[i]<0 and np.sum(evidence[i])>10 and emargin<.6:
                spare=[x for x in (4,5) if slow[i,x]<.1]
                if spare:
                    slow[i,spare[0]]=.15; spare_recruits+=1
            if committed[i]==truth[i] and evidence[i,truth[i]]>=6 and emargin>=4: wrong[i].clear()
        provisional*=.82
    answerable=np.array([truth[i]<6 for i in range(relations)])
    pred=np.argmax(.50*slow+.10*provisional,axis=1)
    answered=answerable & (committed>=0)
    return {
      'relations':relations,'episodes':episodes,
      'accuracy_on_committed_answerable':float(np.mean(pred[answered]==truth[answered])),
      'unresolved_answerable':int(np.sum(answerable & (committed<0))),
      'changed_definition_accuracy':float(np.mean(pred[change_ids]==truth[change_ids])),
      'deliberate_novel_relations':len(novel_ids),
      'hardware_change_requests':len(hw_requests),
      'durable_consolidation_events':durable_events,
      'positive_internal_replays_for_consolidation':pos_replays,
      'negative_internal_replays_for_redefinition':neg_replays,
      'need_based_events':need_events,
      'untrusted_teach_attempts_blocked':blocked,
      'spare_branch_recruitments':spare_recruits,
      'remaining_wrong_path_traces':int(sum(len(x) for x in wrong)),
      'note':'Behavioral rule of the same fabric. The hardware-request interpretation in this historical run is corrected by v15E: unknown knowledge alone is not a hardware fault.'
    }


def main():
    m=load_coupled_module()
    pos=m.simulate(n=50000,seed=15201,sign=1,start_pol=0.0,replays=24)
    wrong=m.simulate(n=50000,seed=15202,sign=1,start_pol=0.0,replays=1)
    erase=m.simulate(n=50000,seed=15203,sign=-1,start_pol=.70,replays=26)
    neg=m.simulate(n=50000,seed=15204,sign=-1,start_pol=0.0,replays=24)
    ch=choice_mc(); sp=run_spice_decks(); beh=behavior()
    capture_fJ=22.5*Qe*.5*1e15
    out={
      'experiment':'v15D_charge_gradient_dendrites',
      'status':'PARTIAL PHYSICS PASS — FITA REJECTED; CHARGE-GRADIENT DUAL-TIME MEMORY SELECTED FOR CUSTOM-DEVICE COUPON',
      'architecture':{
        'DCG':'Dendritic Charge Gradient: validated firing leaves signed charge residue on the existing dendrite/HZO collar; repeated use accumulates it and disuse leaks it away.',
        'DTM':'Dual-Time Memory in one collar: free electrode/ionic charge is fast and leaky; HZO polarization is the slow durable floor. No extra memory device.',
        'NBR':'Need-Based Replay: unknown, close-margin, or mismatch states cause candidate replay; known high-margin routes do not.',
        'SBR':'Two repair branches are retained and may be reassigned before a hardware/topology-change request is emitted.',
        'FITA_tunnel_anchor':'REJECTED from selected path after v15D improvement; no tunnel selector is required.',
        'ordinary_semantic_cell_MOS':0,
        'polarity_memory':'4-nm HZO collar retained as slow state',
        'inference':'guided volatile gap + ballast/quench retained',
        'hollow_charge_return_infrastructure':'retained for shared supply/decoupling, but high-voltage TEACH distribution is no longer required by v15D learning',
      },
      'coupled_free_charge_hzo':{'positive_24_replays':pos,'single_wrong_event':wrong,'erase_old_p0p70_with_26_negative_replays':erase,'negative_24_replays':neg},
      'choice_mc':ch,
      'ngspice':sp,
      'need_based_learning':beh,
      'energy':{
        'captured_residual_charge_energy_fJ_per_replay_proxy':capture_fJ,
        'inherited_inference_energy_fJ_per_replay_proxy':1.9056,
        '24_replay_learning_burst_inference_energy_fJ_proxy':24*1.9056,
        '26_replay_redefinition_negative_burst_fJ_proxy':26*1.9056,
        'note':'Local capture energy is tiny relative to replay inference energy. High-voltage regional HZO program pulse from v15C is removed.'
      },
      'initial_failed_variant_preserved':{
        'selected_hzo_spice_V':0.8740383,'choice_correct':0.706348,'eight_replay_reaches_0p45V':0.0448133,
        'reason':'Initial v15D assumed too-small charge accumulation and independent weak branch races. It was rejected, not overwritten.'
      },
      'evidence_boundary':{
        'actual_software_this_run':'compiled ngspice transient charge/decay and compact branch-choice circuits; Python/NumPy coupled free-charge/HZO-domain and system behavior models.',
        'inherited_physical':'v15C fresh Magic/SKY130 TEACH mesh DRC=0, 263.385 fF; v15D no longer requires that mesh for high-voltage programming.',
        'still_not_physical_proof':'fraction of guided-gap event charge that remains as signed dendrite residue, exact fast-charge leakage time, charge-to-guided-gap field coupling, partial-HZO analog retention, and intrinsic Ag deep-trap lifetime.'
      },
      'next_problem':'Fabricate/model-calibrate one dendrite/HZO/guided-gap coupon to measure signed residual charge per event and analog HZO consolidation/decay. v15E later replaces the fixed 15–25e target with event-derived Q=C·V; do not add branch MOS merely to save it.'
    }
    OUT.parent.mkdir(exist_ok=True); OUT.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({
      'status':out['status'],
      'pos24_pol_q':pos['final_pol_q'],
      'wrong1_pol_q':wrong['final_pol_q'],
      'erase26_pol_q':erase['final_pol_q'],
      'choice_correct':ch['correct_choice_pass'],
      'behavior':beh,
      'spice':{k:v['values'] for k,v in sp.items()}
    },indent=2))

if __name__=='__main__': main()
