#! /usr/bin/env python3

import os
import argparse
import subprocess
import shlex
from pathlib import Path

HERE = Path(__file__).resolve().parent
PY_SRC = HERE / 'httpx'
DOC_ROOT = HERE / 'sphinx-doc'

def setup_paths(doc_root=DOC_ROOT, py_src=PY_SRC):
    assert py_src.exists()
    doc_root.mkdir(exist_ok=True)
    apidoc_path = doc_root / 'source' / 'apidoc'
    apidoc_path.mkdir(exist_ok=True)
    for p in apidoc_path.glob('*.rst'):
        print(f'removing "{p}"')
        p.unlink()

def build_apidoc(doc_root=DOC_ROOT, py_src=PY_SRC):
    apidoc_path = doc_root / 'source' / 'apidoc'
    cmd_str = f'sphinx-apidoc --private --separate -o {apidoc_path} {py_src}'
    print(cmd_str)
    proc = subprocess.run(shlex.split(cmd_str), check=True)

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--doc-root', dest='doc_root', default=str(DOC_ROOT))
    p.add_argument('--py-src', dest='py_src', default=str(PY_SRC))
    args = p.parse_args()
    args.doc_root = Path(args.doc_root)
    args.py_src = Path(args.py_src)
    setup_paths(args.doc_root, args.py_src)
    build_apidoc(args.doc_root, args.py_src)
