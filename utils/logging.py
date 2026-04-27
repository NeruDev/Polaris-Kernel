# yaml_frontmatter:
#   id: 'logging'
#   title: 'Utilidades de log estandarizadas'
#   tags: ['utils', 'logging']

import sys

def log_info(msg: str):
    print(f"[INFO] {msg}")

def log_warn(msg: str):
    print(f"[WARN] {msg}", file=sys.stderr)

def log_error(msg: str):
    print(f"[ERROR] {msg}", file=sys.stderr)
