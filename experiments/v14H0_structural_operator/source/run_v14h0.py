import math, random, csv, json
from collections import Counter
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / 'results'
OUT.mkdir(parents=True, exist_ok=True)
N=420
MODS=(3,4,5,7)
CRT={(x%3,x%4,x%5,x%7):x for x in range(N)}


def ring_op(a,b,v,rng,reps=5,static=None):
    s_static=v/math.sqrt(2); s_dynamic=v/math.sqrt(2)
    if static is None:
        static={(m,r):rng.gauss(0,s_static) for m in MODS for r in range(reps)}
    residues=[]; counts=[]
    for m in MODS:
        votes=[]
        for r in range(reps):
            noisy=(a%m)+(b%m)+static[(m,r)]+rng.gauss(0,s_dynamic)
            votes.append(int(round(noisy))%m)
        c=Counter(votes); residue,count=c.most_common(1)[0]
        residues.append(residue); counts.append(count)
    return CRT[tuple(residues)], counts


def wave_op(a,b,v,rng,reps=3,static=None):
    s_static=v/math.sqrt(2); s_dynamic=v/math.sqrt(2)
    if static is None: static=[rng.gauss(0,s_static) for _ in range(reps)]
    votes=[int(round((a+b+static[r]+rng.gauss(0,s_dynamic))%N))%N for r in range(reps)]
    c=Counter(votes); out,count=c.most_common(1)[0]
    return out, count


def nearest_lookup_prediction(a,b,train,table):
    # Efficient local search for the nearest memorized operand pair.
    for d in range(1, N):
        for da in range(-d,d+1):
            db=d-abs(da)
            for sign in (-1,1) if db else (1,):
                q=(a+da,b+sign*db)
                if 0<=q[0]<N and 0<=q[1]<N and q in train:
                    return table[q]
    return None


def nominal_unseen(seed=14080):
    rng=random.Random(seed)
    pairs=[(a,b) for a in range(N) for b in range(N)]
    rng.shuffle(pairs); k=len(pairs)//4
    train=set(pairs[:k]); held=pairs[k:]
    table={p:(p[0]+p[1])%N for p in train}
    ring_ok=sum(CRT[((a+b)%3,(a+b)%4,(a+b)%5,(a+b)%7)]==((a+b)%N) for a,b in held)
    wave_ok=len(held)
    lookup_ok=sum(table.get((a,b))==((a+b)%N) for a,b in held)
    sample=held[:1000]; near_ok=0
    for a,b in sample:
        near_lookup=nearest_lookup_prediction(a,b,train,table)
        near_ok += near_lookup==((a+b)%N)
    return {
        'domain':'Z_420 modular addition',
        'total_pairs':N*N,
        'stored_lookup_pairs':k,
        'heldout_pairs':len(held),
        'ring5_heldout_exact_rate_nominal':ring_ok/len(held),
        'wave3_heldout_exact_rate_nominal':wave_ok/len(held),
        'lookup25_heldout_exact_rate_direct':lookup_ok/len(held),
        'lookup25_nearest_interpolation_exact_rate':near_ok/len(sample),
        'nearest_interpolation_trials':len(sample)
    }


def stress(v, chains=5000, steps=8, seed=1):
    rows=[]
    for name,reps in [('ring5',5),('wave3',3)]:
        rng=random.Random(seed+int(v*10000)+(0 if name=='ring5' else 999))
        exact_chains=wrong_ops=flagged_ops=flagged_wrong=0; total=chains*steps
        for _ in range(chains):
            ss=v/math.sqrt(2)
            static=({(m,r):rng.gauss(0,ss) for m in MODS for r in range(reps)} if name=='ring5' else [rng.gauss(0,ss) for _ in range(reps)])
            st=truth=rng.randrange(N); ce=True
            for _ in range(steps):
                b=rng.randrange(N); truth=(truth+b)%N
                if name=='ring5':
                    st,counts=ring_op(st,b,v,rng,reps,static); flagged=any(c<reps for c in counts)
                else:
                    st,count=wave_op(st,b,v,rng,reps,static); flagged=count<reps
                wrong=st!=truth
                wrong_ops+=wrong; flagged_ops+=flagged; flagged_wrong+=(wrong and flagged); ce &= not wrong
            exact_chains+=ce
        rows.append({
            'variation_sigma_fraction_state_pitch':v,'operator':name,'chains':chains,'chain_length':steps,
            'exact_chain_rate':exact_chains/chains,'per_operation_error_rate':wrong_ops/total,
            'confidence_flag_rate':flagged_ops/total,
            'wrong_error_flag_recall':(flagged_wrong/wrong_ops if wrong_ops else 1.0)
        })
    return rows


def chain_length_screen(v=0.20, lengths=(8,16,32), chains=5000):
    rows=[]
    for L in lengths: rows += stress(v,chains=chains,steps=L,seed=500+L)
    return rows

unseen=nominal_unseen(); variation=[]
for v in [0.05,0.10,0.15,0.20,0.25,0.30]: variation += stress(v)
lengths=chain_length_screen()
hardware=[
    {'operator':'ring5','state_sites':sum(MODS)*5,'programmable_pair_links':0,'local_replicas':len(MODS)*5,'notes':'five copies of each 3/4/5/7 residue ring; local majority restoration'},
    {'operator':'wave3','state_sites':N*3,'programmable_pair_links':0,'local_replicas':3,'notes':'three 420-site displacement tracks with local voting'},
    {'operator':'lookup25','state_sites':0,'programmable_pair_links':N*N//4,'local_replicas':0,'notes':'stores 25% of operand pairs; direct held-out coverage is zero'},
    {'operator':'lookup_full','state_sites':0,'programmable_pair_links':N*N,'local_replicas':0,'notes':'full value-to-value memorization control'}
]
with open(OUT/'unseen_generalization.json','w') as f: json.dump(unseen,f,indent=2)
for fn,rows in [('variation_chain.csv',variation),('chain_length.csv',lengths),('hardware_proxy.csv',hardware)]:
    with open(OUT/fn,'w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
print(json.dumps({'unseen':unseen,'variation_at_0p20':[r for r in variation if r['variation_sigma_fraction_state_pitch']==0.20],'chain_length':lengths,'hardware':hardware},indent=2))
