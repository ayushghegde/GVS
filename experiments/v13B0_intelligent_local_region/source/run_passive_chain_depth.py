#!/usr/bin/env python3
"""v13B0 passive-Myelin chain-depth screen.

This generates the TT chain benches used in v13B0. It preserves the old v12R
source Grammar pair and only varies passive-Myelin MIM size / target node C.
Use the supplied SKY130 ngspice model deck. The experiment report records the
exact simulator/tool limitation and does not treat this TT screen as new PVT
signoff.
"""
from pathlib import Path
import subprocess, re, csv, argparse

CASES=[(2,3),(2,2),(3,2),(4,2),(5,2)]

def make_netlist(lib,w,target):
    nodes=' '.join([f'v(e{i})=.44 v(p{i})=.44' for i in range(1,9)])
    L=[f'.lib "{lib}" tt','.temp 25',
       'VB3P b3p 0 PULSE(0 .2 1u 1n 1n .2u 10u)','VB3N b3n 0 0',
       'VB2P b2p 0 0','VB2N b2n 0 PULSE(0 .2 1u 1n 1n .2u 10u)',
       'VB1P b1p 0 PULSE(0 .2 1u 1n 1n .2u 10u)','VB1N b1n 0 0',
       'VB0P b0p 0 0','VB0N b0n 0 PULSE(0 .2 1u 1n 1n .2u 10u)',
       'CG0 g0 0 40f','CG1 g1 0 40f',f'.ic v(g0)=.44 v(g1)=.44 {nodes}',
       'X00 g0 b3p sky130_fd_pr__cap_mim_m3_1 w=2 l=2',
       'X01 g0 b2n sky130_fd_pr__cap_mim_m3_1 w=2 l=2',
       'X02 g0 b1p sky130_fd_pr__cap_mim_m3_1 w=2 l=2',
       'X03 g0 b0n sky130_fd_pr__cap_mim_m3_1 w=2 l=2',
       'X10 g1 b3p sky130_fd_pr__cap_mim_m3_1 w=2 l=2',
       'X11 g1 b2n sky130_fd_pr__cap_mim_m3_1 w=2 l=2',
       'X12 g1 b1n sky130_fd_pr__cap_mim_m3_1 w=2 l=2',
       'X13 g1 b0p sky130_fd_pr__cap_mim_m3_1 w=2 l=2']
    a,b='g0','g1'
    for i in range(1,9):
        L += [f'XME{i} {a} e{i} sky130_fd_pr__cap_mim_m3_1 w={w} l={w}',
              f'XMP{i} {b} p{i} sky130_fd_pr__cap_mim_m3_1 w={w} l={w}',
              f'CE{i} e{i} 0 {target}f',f'CP{i} p{i} 0 {target}f']
        a,b=f'e{i}',f'p{i}'
    L += ['.tran 1n 1.15u uic','.meas tran G0 find v(g0) at=1.1u','.meas tran G1 find v(g1) at=1.1u']
    for i in range(1,9):
        L += [f'.meas tran E{i} find v(e{i}) at=1.1u',f'.meas tran P{i} find v(p{i}) at=1.1u']
    L += [".meas tran ESRC INTEG par('v(b3p)*(-i(VB3P))+v(b2n)*(-i(VB2N))+v(b1p)*(-i(VB1P))+v(b0n)*(-i(VB0N))') from=.9u to=1.15u",'.end']
    return '\n'.join(L)+'\n'

def parse(log):
    vals={}
    for k in ['g0','g1']+[z for i in range(1,9) for z in (f'e{i}',f'p{i}')]+['esrc']:
        m=re.search(rf'^\s*{k}\s*=\s*([+-]?[0-9.eE+-]+)',log,re.M)
        if not m: raise RuntimeError(f'missing {k}')
        vals[k]=float(m.group(1))
    return vals

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--ngspice',required=True)
    ap.add_argument('--lib',required=True)
    ap.add_argument('--out',default='v13B0_chain_runs')
    a=ap.parse_args(); out=Path(a.out); out.mkdir(exist_ok=True)
    rows=[]
    for w,target in CASES:
        stem=f'tt_w{w}_c{target}'
        cir=out/(stem+'.cir'); log=out/(stem+'.log')
        cir.write_text(make_netlist(a.lib,w,target))
        subprocess.run([a.ngspice,'-b',str(cir),'-o',str(log)],check=True)
        v=parse(log.read_text(errors='ignore'))
        seps=[(v['g0']-v['g1'])*1e3]+[(v[f'e{i}']-v[f'p{i}'])*1e3 for i in range(1,9)]
        r={'case':f'{w}x{w}_target{target}','mim_w_um':w,'target_fF':target,'mim_area_um2_per_edge':w*w,'source_energy_fJ':v['esrc']*1e15}
        for i,s in enumerate(seps):
            r[f'stage{i}_exact_partial_sep_mV']=s
            r[f'stage{i}_best_symmetric_margin_mV']=s/2
        for th in (18,11):
            n=0
            for i in range(1,9):
                if seps[i]/2 >= th: n=i
                else: break
            r[f'max_hops_margin_ge_{th}mV']=n
        rows.append(r)
    with open(out/'passive_chain_depth.csv','w',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=list(rows[0])); wr.writeheader(); wr.writerows(rows)

if __name__=='__main__': main()
