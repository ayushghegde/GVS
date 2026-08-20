#!/usr/bin/env python3
"""
Reproduce the v12S hierarchical-rebuild comparison from the v12Q execution trace.
Requires agin_v12q_complete_query_log.csv in the same directory.
"""
from pathlib import Path
import pandas as pd, numpy as np, math
root=Path(__file__).resolve().parent
q=pd.read_csv(root/"agin_v12q_complete_query_log.csv").sort_values("time_ms")
mods=["GrammarCell","CapTemplate","Interneuron","Lease","PhysicalEventEdge","RuleEngine","ExactALU","SRAM_Table","StaticSelector"]
regions=[]
for (qt,plan),g in q.groupby(["question_type","plan"]):
    regions.append((qt,plan,tuple(int(g[m].mean()>=.5) for m in mods),len(g)))
print(f"plans/regions={len(regions)} structural_archetypes={len(set(r[2] for r in regions))}")
print("Use agin_v12s_hierarchical_rebuild_summary.csv for the deterministic stress configuration and exact recorded result.")
