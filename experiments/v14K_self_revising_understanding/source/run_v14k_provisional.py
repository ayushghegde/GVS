import random, json, statistics
from pathlib import Path
import run_v14k as base
OUT=Path(__file__).resolve().parents[1]/'results'; OUT.mkdir(parents=True,exist_ok=True)
SEED=14041
random.seed(SEED)

def false_chain(case):
    p=case['p']
    return [(case['cue'],p+':false1'),(p+':false1',p+':false2'),(p+':false2',case['wrong'])]

def apply_chain(g,case,chain,effort,program_fail,promote=True):
    gain=(0.18+0.04*effort) if not promote else (0.38+0.10*effort); writes=0
    for a,b in chain:
        if random.random()>=program_fail:g.add(a,b,gain);writes+=1
    return writes

def revise(case,false_evidence,program_fail,read_noise,evidence_count,immediate=False):
    g=case['g'].copy(); effort=base.failed_effort(g,case); writes=0; selftests=0
    correct_chain=case['lesson']; wrong_chain=false_chain(case)
    signs=[random.random()>=false_evidence for _ in range(evidence_count)]
    if immediate:
        choose_correct=signs[0]; writes+=apply_chain(g,case,correct_chain if choose_correct else wrong_chain,effort,program_fail,True)
    else:
        writes+=apply_chain(g,case,correct_chain if signs[0] else wrong_chain,effort,program_fail,False)
        choose_correct=sum(signs)>evidence_count//2
        chosen=correct_chain if choose_correct else wrong_chain; rejected=wrong_chain if choose_correct else correct_chain
        writes+=apply_chain(g,case,chosen,effort,program_fail,True)
        for a,b in rejected:
            if random.random()>=program_fail:g.add(a,b,-0.30);writes+=1
    if choose_correct and random.random()>=program_fail:g.add(case['old'],case['wrong'],-0.72);writes+=1
    elif not choose_correct and random.random()>=program_fail:g.add(case['old'],case['wrong'],+0.08);writes+=1
    for _ in range(3):
        selftests+=1
        if base.predict(g,case,read_noise)=='correct':break
        if choose_correct:
            writes+=apply_chain(g,case,correct_chain,effort,program_fail,False)
            if random.random()>=program_fail:g.add(case['old'],case['wrong'],-0.12);writes+=1
    return g,effort,writes,selftests,choose_correct

def run(false_evidence,evidence_count,immediate=False,program_fail=.05,read_noise=.20):
    rows=[]
    for d in base.DOMAINS:
        for i in range(base.N_PER_DOMAIN):
            c=base.make_case(i,d); g,e,w,st,sign=revise(c,false_evidence,program_fail,read_noise,evidence_count,immediate)
            rows.append((base.predict(g,c,read_noise),base.predict(g,c,read_noise,start=c['n1']),e,w,st,sign))
    n=len(rows)
    return {'policy':'immediate_commit' if immediate else f'provisional_majority_{evidence_count}','false_evidence_probability':false_evidence,'evidence_count':1 if immediate else evidence_count,'program_fail_probability':program_fail,'read_noise_sigma':read_noise,'cases':n,'after_correct':sum(r[0]=='correct' for r in rows)/n,'transfer_correct':sum(r[1]=='correct' for r in rows)/n,'semantic_revision_sign_correct':sum(r[5] for r in rows)/n,'mean_program_events':statistics.mean(r[3] for r in rows),'mean_selftests':statistics.mean(r[4] for r in rows),'mean_effort':statistics.mean(r[2] for r in rows)}

res=[]
for p in [.05,.10,.15,.20,.25]:
    res.append(run(p,1,True)); res.append(run(p,3,False)); res.append(run(p,5,False))
summary={'seed':SEED,'interpretation':'Effort controls plasticity magnitude; corroboration controls semantic sign. Provisional links are not fully consolidated from one uncertain lesson.','results':res,'caution':'If corroborating evidence shares the same systematic error, majority voting does not help; this experiment assumes partially independent evidence.'}
(OUT/'PROVISIONAL_RESULTS.json').write_text(json.dumps(summary,indent=2)); print(json.dumps(summary,indent=2))
