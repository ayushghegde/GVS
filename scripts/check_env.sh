#!/usr/bin/env bash
set -euo pipefail

printf 'GVS environment check\n'
printf '%-18s' 'ngspice:'
if command -v ngspice >/dev/null 2>&1; then
  ngspice --version | head -n 1
else
  echo 'MISSING'
fi

printf '%-18s' 'PDK_ROOT:'
if [[ -n "${PDK_ROOT:-}" && -d "${PDK_ROOT}" ]]; then
  echo "${PDK_ROOT}"
else
  echo 'NOT SET / NOT FOUND'
fi

printf '%-18s' 'baseline netlist:'
if find experiments/baseline -type f \( -name '*.sp' -o -name '*.cir' -o -name '*.spice' \) -print -quit 2>/dev/null | grep -q .; then
  echo 'FOUND'
else
  echo 'NOT RECOVERED YET'
fi
