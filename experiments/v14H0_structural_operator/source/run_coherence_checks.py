import math, random, csv
from collections import Counter
from pathlib import Path
OUT=Path(__file__).resolve().parents[1]/'results'; OUT.mkdir(parents=True,exist_ok=True)
N=420; CORE=(3,4,5,7); CRT={(x%3,x%4,x%5,x%7):x for x in range(N)}

def maj(a,b,m,v,rng,reps,static):
    sd=v/math.sqrt(2)
    votes=[int(round((a%m)+(b%m)+static[i]+rng.gauss(0,sd)))%m for i in range(reps)]
    return Counter(votes).most_common(1)[0]

def run(checks,check_reps=3,v=0.25,chains=5000,L=8,seed=1):
    rng=random.Random(seed); ss=v/math.sqrt(2)
    wrong=flagged=flagged_wrong=0; total=chains*L; exact_chain=0
    for _ in range(chains):
        core_static={m:[rng.gauss(0,ss) for _ in range(5)] for m in CORE}
        chk_static={m:[rng.gauss(0,ss) for _ in range(check_reps)] for m in checks}
        st=truth=rng.randrange(N); ce=True
        for _ in range(L):
            b=rng.randrange(N); truth=(truth+b)%N
            residues=[maj(st,b,m,v,rng,5,core_static[m])[0] for m in CORE]
            out=CRT[tuple(residues)]
            mismatch=False
            for m in checks:
                rr,_=maj(st,b,m,v,rng,check_reps,chk_static[m])
                mismatch |= (out%m)!=rr
            w=out!=truth
            wrong+=w; flagged+=mismatch; flagged_wrong+=(w and mismatch); ce &= not w; st=out
        exact_chain+=ce
    return {
      'check_moduli':'+'.join(map(str,checks)) if checks else 'none',
      'check_replicas_each':check_reps if checks else 0,
      'added_check_state_sites':sum(checks)*check_reps,
      'variation_sigma_fraction_state_pitch':v,
      'exact_chain_rate':exact_chain/chains,
      'per_operation_error_rate':wrong/total,
      'check_flag_rate':flagged/total,
      'wrong_error_flag_recall':flagged_wrong/wrong if wrong else 1.0,
      'chains':chains,'chain_length':L
    }

rows=[]
for i,checks in enumerate([(),(6,),(10,),(6,10),(140,),(210,)]):
    rows.append(run(checks,3,0.25,5000,8,700+i))
with open(OUT/'coherence_check_screen.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
for r in rows: print(r)
