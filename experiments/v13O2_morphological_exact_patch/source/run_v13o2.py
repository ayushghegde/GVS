#!/usr/bin/env python3
"""v13O2: NAND-only spatial exact patch."""
import csv
from pathlib import Path
OUT=Path(__file__).resolve().parents[1]/'results'; OUT.mkdir(parents=True,exist_ok=True)
def nand(a,b): return 0 if (a and b) else 1
def full_adder(a,b,cin):
    n1=nand(a,b); n2=nand(a,n1); n3=nand(b,n1); x=nand(n2,n3); n4=nand(x,cin); n5=nand(x,n4); n6=nand(cin,n4)
    return nand(n5,n6),nand(n1,n4)
def add8(a,b):
    carry=0; out=0
    for bit in range(8):
        s,carry=full_adder((a>>bit)&1,(b>>bit)&1,carry); out|=s<<bit
    return out,carry
def depth8():
    carry=0; sums=[]
    for _ in range(8):
        a=b=0; n1=max(a,b)+1; n2=max(a,n1)+1; n3=max(b,n1)+1; x=max(n2,n3)+1; n4=max(x,carry)+1; n5=max(x,n4)+1; n6=max(carry,n4)+1; s=max(n5,n6)+1; carry=max(n1,n4)+1; sums.append(s)
    return max(sums+[carry]),carry
def main():
    wrong=0
    for a in range(256):
        for b in range(256):
            s,c=add8(a,b); wrong += (s+(c<<8) != a+b)
    depth,carry_depth=depth8(); rows=[{'operation':'8-bit unsigned addition','input_pairs_tested':65536,'wrong_results':wrong,'correct_fraction':1-wrong/65536,'nand_cells':72,'max_gate_depth':depth,'final_carry_depth':carry_depth,'runtime_instruction_fetches':0,'runtime_program_counter_steps':0}]
    p=OUT/'exact_patch_summary.csv'
    with p.open('w',newline='') as f: w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    print(p)
if __name__=='__main__': main()
