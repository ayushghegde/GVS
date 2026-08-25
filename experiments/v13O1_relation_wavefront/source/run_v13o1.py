#!/usr/bin/env python3
"""v13O1: typed relation-wavefront model for multi-hop reasoning.

A query injects an event into one entity membrane and relation-specific local
connections propagate only the requested relation sequence. This is a graph/
event model, not PEX or a natural-language benchmark.
"""
from __future__ import annotations
import csv, random, statistics
from pathlib import Path
OUT=Path(__file__).resolve().parents[1]/'results'; OUT.mkdir(parents=True,exist_ok=True)
SPINE_EVENT_FJ=0.67

def make_graph(n,degree,relations,seed):
    rng=random.Random(seed); adj=[[] for _ in range(n)]; edges=[]
    for u in range(n):
        candidates=list(range(n)); candidates.remove(u)
        for v in rng.sample(candidates,degree):
            r=rng.randrange(relations); adj[u].append((r,v)); edges.append((u,r,v))
    return adj,edges

def grounded_query(adj,length,rng):
    start=rng.randrange(len(adj)); cur=start; rel=[]
    for _ in range(length):
        r,v=rng.choice(adj[cur]); rel.append(r); cur=v
    return start,rel,cur

def wave(adj,start,relations):
    frontier={start}; traversals=0
    for wanted in relations:
        nxt=set()
        for u in frontier:
            for r,v in adj[u]:
                if r==wanted: traversals+=1; nxt.add(v)
        frontier=nxt
        if not frontier: break
    return frontier,traversals

def main():
    rows=[]
    for n,deg,nrel in [(128,4,8),(256,4,8),(512,4,16),(512,8,16)]:
        adj,edges=make_graph(n,deg,nrel,7000+n+31*deg+nrel); rng=random.Random(17000+n)
        for hops in (2,4,8):
            ok=0; travers=[]; answer_sizes=[]
            for _ in range(500):
                start,rels,target=grounded_query(adj,hops,rng); ans,tr=wave(adj,start,rels)
                ok += target in ans; travers.append(tr); answer_sizes.append(len(ans))
            fullscan=len(edges)*hops; mean_tr=statistics.mean(travers)
            rows.append({'nodes':n,'average_degree':deg,'relation_types':nrel,'hops':hops,'queries':500,'grounded_target_recall':ok/500,'mean_relation_edge_events':mean_tr,'median_relation_edge_events':statistics.median(travers),'mean_answer_set_size':statistics.mean(answer_sizes),'active_edge_events_vs_full_scan_percent':100*mean_tr/fullscan,'conservative_spine_event_energy_proxy_fj':mean_tr*SPINE_EVENT_FJ})
    p=OUT/'wavefront_summary.csv'
    with p.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    print(p)
if __name__=='__main__': main()
