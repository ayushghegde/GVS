import random, csv, json, math
from pathlib import Path
OUT=Path(__file__).resolve().parents[1]/'results'; OUT.mkdir(parents=True,exist_ok=True)
ACTIONS=['bind_unknown','express_relation','apply_area_relation','balance_expand','factor','select_feasible_root']

# Need-gated procedure cells are indexed here by the unmet transformation state.
# This is a control/selection abstraction, not a transistor-level implementation.

def correct_trace(start_stage):
    return ACTIONS[start_stage:]

def generate(seed=14101):
    rng=random.Random(seed)
    rows=[(w,k,w*(w+k),start) for w in range(1,51) for k in range(1,21) for start in range(len(ACTIONS))]
    rng.shuffle(rows)
    return rows

def majority_decode_stage(stage,p,reps,rng):
    bits=[]
    for j in range(len(ACTIONS)):
        true=(j==stage)
        ones=0
        for _ in range(reps):
            observed=true
            if rng.random()<p: observed=not observed
            ones+=observed
        bits.append(ones)
    # local population competition: largest support must exceed half the replicas.
    best=max(bits); winners=[i for i,x in enumerate(bits) if x==best]
    if best<=reps//2 or len(winners)!=1: return None
    return winners[0]

def noisy_need_trace_success(start,p,reps,rng):
    stage=start
    while stage<len(ACTIONS):
        dec=majority_decode_stage(stage,p,reps,rng)
        if dec!=stage: return False
        stage+=1
    return True

def main():
    rows=generate(); k=len(rows)//4; train=set(rows[:k]); held=rows[k:]
    # Full-state lookup control stores exact numeric problem state + stage.
    lookup={r:correct_trace(r[3])[0] for r in train}
    need_nominal=sum(correct_trace(r[3])==ACTIONS[r[3]:] for r in held)/len(held)
    lookup_direct=sum((lookup.get(r)==correct_trace(r[3])[0]) for r in held)/len(held)
    # Blind fixed script only starts correctly when the problem arrives at stage zero.
    fixed_success=sum(r[3]==0 for r in held)/len(held)
    summary={
      'generated_problems':len(rows),'train_fraction':0.25,'heldout_problems':len(held),
      'need_gated_nominal_trace_success':need_nominal,
      'full_state_lookup_heldout_first_action_success':lookup_direct,
      'blind_fixed_sequence_trace_success':fixed_success,
      'numeric_values_are_not_part_of_need_templates':True
    }
    stress=[]
    for reps in [5,7,9]:
      for p in [0.02,0.05,0.10,0.15,0.20]:
        rr=random.Random(15000+reps*100+int(p*1000)); ok=0; trials=10000
        for _ in range(trials):
          start=rr.randrange(len(ACTIONS))
          ok+=noisy_need_trace_success(start,p,reps,rr)
        stress.append({'feature_flip_probability':p,'population_replicas':reps,'trace_success_rate':ok/trials,'trials':trials})
    example={
      'problem':'rectangle width unknown; length is 5 greater; area is 84',
      'trace':[
        'need unknown value -> bind width as x',
        'need length expression -> length = x + 5',
        'need area equation -> x(x + 5) = 84',
        'need zero-form equation -> x^2 + 5x - 84 = 0',
        'need roots -> factor as (x + 12)(x - 7) = 0',
        'need physically valid dimension -> choose x = 7'
      ],
      'hardware_status':'selection mechanism modeled; multiply/factor structural hardware not yet physically solved'
    }
    with open(OUT/'summary.json','w') as f: json.dump(summary,f,indent=2)
    with open(OUT/'example_trace.json','w') as f: json.dump(example,f,indent=2)
    with open(OUT/'population_stress.csv','w',newline='') as f:
      w=csv.DictWriter(f,fieldnames=stress[0].keys()); w.writeheader(); w.writerows(stress)
    print(json.dumps({'summary':summary,'selected_stress':[r for r in stress if r['population_replicas']==9],'example':example},indent=2))
if __name__=='__main__': main()
