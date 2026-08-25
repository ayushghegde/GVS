#!/usr/bin/env python3
"""Canonical entry point for reproducible GVS simulation/model experiments.

Use this instead of copying constants from chat history. Historical evidence,
current model work, candidate architectures and trace tooling remain explicitly separated.
"""
from __future__ import annotations
import json, subprocess, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CFG=ROOT/'MASTER_GVS'/'SIMULATION_BASELINE.json'

def load():
    return json.loads(CFG.read_text())

def status():
    print(json.dumps(load(),indent=2))

def run_script(rel,args=None):
    p=ROOT/rel
    if not p.exists():
        raise SystemExit(f'missing canonical script: {p}')
    cmd=[sys.executable,str(p)] + (args or [])
    subprocess.run(cmd,check=True,cwd=p.parent)

def verify_files():
    c=load(); missing=[]
    paths=[c['architecture_source']]
    if c.get('candidate_architecture_source'):
        paths.append(c['candidate_architecture_source'])
    paths += list(c['historical_physical_baseline'].values())
    paths += list(c['current_reproducible_work'].values())
    paths += list(c.get('support_tools',{}).values())
    for rel in paths:
        if not (ROOT/rel).exists(): missing.append(rel)
    if missing:
        print('MISSING:')
        for x in missing: print(' -',x)
        return 1
    print('canonical GVS baseline paths present')
    return 0

def run_key(key):
    c=load(); work=c['current_reproducible_work']
    if key not in work:
        raise SystemExit(f'unknown registered experiment: {key}')
    run_script(work[key])

def run_family(family):
    c=load(); work=c['current_reproducible_work']
    keys=[k for k in work if k.lower().startswith(family.lower())]
    if not keys:
        raise SystemExit(f'no registered experiments for family {family}')
    for key in sorted(keys):
        print(f'== {key} ==')
        run_script(work[key])

def run_trace(args):
    c=load(); analyzer=c.get('support_tools',{}).get('trace_analyzer')
    if not analyzer:
        raise SystemExit('trace analyzer is not registered')
    run_script(analyzer,args)

def usage():
    print('usage:')
    print('  python3 scripts/gvs_sim.py status')
    print('  python3 scripts/gvs_sim.py verify')
    print('  python3 scripts/gvs_sim.py current')
    print('  python3 scripts/gvs_sim.py run <registered-key>')
    print('  python3 scripts/gvs_sim.py family <v13M|v13N|...>')
    print('  python3 scripts/gvs_sim.py trace <trace.csv> [--slots N] [--out summary.json]')

def main():
    if len(sys.argv)<2:
        usage(); return 2
    cmd=sys.argv[1].lower()
    c=load()
    if cmd=='status': status(); return 0
    if cmd=='verify': return verify_files()
    if cmd=='current': run_family(c['current_experiment_family']); return 0
    if cmd=='run' and len(sys.argv)==3: run_key(sys.argv[2]); return 0
    if cmd=='family' and len(sys.argv)==3: run_family(sys.argv[2]); return 0
    if cmd=='trace' and len(sys.argv)>=3: run_trace(sys.argv[2:]); return 0
    raw=sys.argv[1]
    if raw in c['current_reproducible_work']:
        run_key(raw); return 0
    if any(k.lower().startswith(raw.lower()) for k in c['current_reproducible_work']):
        run_family(raw); return 0
    usage(); return 2

if __name__=='__main__': raise SystemExit(main())
