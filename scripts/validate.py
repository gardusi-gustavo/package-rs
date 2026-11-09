#!/usr/bin/env python3
from __future__ import annotations
import argparse, sys, tomllib
from pathlib import Path

def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument("--root", default=".")
    root = Path(ap.parse_args().root)
    cargo = root / "Cargo.toml"
    if not cargo.is_file():
        print("missing Cargo.toml", file=sys.stderr); return 1
    data = tomllib.loads(cargo.read_text(encoding="utf-8"))
    if data.get("package", {}).get("name") != "gardusi-gustavo-rs":
        print("unexpected crate name", file=sys.stderr); return 1
    for name in ("src/lib.rs", "tests/contract.rs", "examples/cli.rs"):
        if not (root / name).is_file():
            print(f"missing {name}", file=sys.stderr); return 1
    for p in list((root / "src").rglob("*.rs")) + list((root / "tests").rglob("*.rs")) + list((root / "examples").rglob("*.rs")):
        text = p.read_text(encoding="utf-8")
        if text.count("{") != text.count("}"):
            print(f"{p}: unbalanced braces", file=sys.stderr); return 1
    print("rust validation ok")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
