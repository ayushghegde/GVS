import numpy as np

# Device-state learning stress for v14M BDJ OFF/WEAK/STRONG links.
rng=np.random.default_rng(140017)
N=3000; OPTIONS=16
G_WEAK=2.5e-9; G_STRONG=25e-9


def trial(copies,program_fail,read_sigma,false_feedback):
    correct=rng.integers(0,OPTIONS,size=N)
    state=np.full((N,OPTIONS,copies),G_WEAK)
    state[np.arange(N),correct,:]=G_STRONG
    changed=rng.choice(N,size=N//5,replace=False)
    new=correct.copy()
    for i in changed:
        choices=np.delete(np.arange(OPTIONS),correct[i])
        new[i]=rng.choice(choices)
        target=new[i] if rng.random()>false_feedback else rng.choice(np.delete(np.arange(OPTIONS),new[i]))
        for k in range(copies):
            if rng.random()>program_fail: state[i,correct[i],k]=G_WEAK
            if rng.random()>program_fail: state[i,target,k]=G_STRONG
    eff=state.sum(axis=2)
    noisy=np.maximum(0,eff*(1+rng.normal(0,read_sigma,size=eff.shape)))
    pred=noisy.argmax(axis=1)
    acc=pred==new
    return acc.mean(),acc[changed].mean()

for copies in (1,2,3):
    vals=np.array([trial(copies,.05,.20,.0) for _ in range(30)])
    print(copies,'copies overall',vals[:,0].mean(),'changed',vals[:,1].mean())

print('Common-mode semantic feedback screen:')
for copies in (1,2,3):
    vals=np.array([trial(copies,.05,.20,.10) for _ in range(30)])
    print(copies,'copies overall',vals[:,0].mean(),'changed',vals[:,1].mean())
