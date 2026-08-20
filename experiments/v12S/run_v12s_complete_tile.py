#!/usr/bin/env python3
import argparse, pathlib, subprocess, re, tempfile, sys

temps={"tt":25,"ff":-20,"ss":85,"tt_mm":25,"ff_mm":-20,"ss_mm":85}
ap=argparse.ArgumentParser()
ap.add_argument("--corner",choices=list(temps),default="tt")
ap.add_argument("--ngspice",default="/mnt/data/ngspice_runtime/ngspice-runtime/bin/ngspice")
ap.add_argument("--pdk",default="/mnt/data/sky130_pdk_v12s/sky130A/libs.tech/combined/sky130.lib.spice")
ap.add_argument("--template",default=str(pathlib.Path(__file__).with_name("v12s_complete_autonomous_tile_template.cir")))
args=ap.parse_args()

ng=pathlib.Path(args.ngspice); pdk=pathlib.Path(args.pdk); tpl=pathlib.Path(args.template)
for p,n in [(ng,"ngspice"),(pdk,"PDK library"),(tpl,"netlist template")]:
    if not p.exists(): raise SystemExit(f"Missing {n}: {p}")

text=tpl.read_text().replace("__PDK_LIB__",str(pdk)).replace("__CORNER__",args.corner).replace("__TEMP__",str(temps[args.corner]))
with tempfile.TemporaryDirectory() as td:
    cir=pathlib.Path(td)/"tile.cir"; log=pathlib.Path(td)/"tile.log"
    cir.write_text(text)
    with log.open("w") as f:
        r=subprocess.run([str(ng),"-b",str(cir)],stdout=f,stderr=subprocess.STDOUT)
    out=log.read_text()
    print(out)
    if r.returncode: sys.exit(r.returncode)
