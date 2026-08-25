#!/usr/bin/env python3
"""Canonical entry point for reproducible GVS simulation/model experiments.

Use this instead of copying constants from chat history. The script deliberately
keeps historical evidence separate from new model experiments.
"""
from __future__ import annotations
import argparse, json, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
CFG=ROOT/'MASTER_GVS'/'SIMULATION_BASELINE.json'

def load():
    return json.loads(CFG.read_text())

def status():
    c=load(); print(json.dumps(c,indent=2))

def run_script(rel):
    p=ROOT/rel
    if not p.exists():
        raise SystemExit(f'missing canonical experiment script: {p}')
    subprocess.run([sys.executable,str(p)],check=True,cwd=p.parent)

def verify_files():
    c=load(); missing=[]
    for rel in [c['architecture_source'], *c['historical_physical_baseline'].values(), *c['current_reproducible_work'].values()]:
        if not (ROOT/rel).exists(): missing.append(rel)
    if missing:
        print('MISSING:')
        for x in missing: print(' -',x)
        return 1
    print('canonical GVS baseline paths present')
    return 0

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('command',choices=['status','verify','v13m0','v13m1','v13m2','v13m'])
    a=ap.parse_args()
    if a.command=='status': status(); return 0
    if a.command=='verify': return verify_files()
    c=load()
    if a.command in ('v13m0','v13m'):
        run_script(c['current_reproducible_work']['v13M0'])
    if a.command in ('v13m1','v13m'):
        run_script(c['current_reproducible_work']['v13M1'])
    if a.command in ('v13m2','v13m'):
        run_script(c['current_reproducible_work']['v13M2'])
    return 0
if __name__=='__main__': raise SystemExit(main())
