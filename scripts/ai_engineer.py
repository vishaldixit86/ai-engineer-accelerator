#!/usr/bin/env python3
"""Self-contained local CLI for finding and installing original AI Engineer resources."""
import argparse
import hashlib
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def catalog():
    return json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))

def discover(term):
    rows = catalog()["scenarios"]
    return [r for r in rows if term.lower() in json.dumps(r).lower()]

def install(project, pack=None, dry_run=False):
    dest = Path(project).expanduser().resolve()
    if not dest.is_dir():
        raise ValueError("Target project must exist")
    if dest == ROOT:
        raise ValueError("Install into a separate project, not the accelerator itself")
    choices = catalog()
    if pack and pack not in choices["packs"]:
        raise ValueError("Unknown technology pack")
    mappings = []
    for path in sorted((ROOT / "core").glob("*/SKILL.md")) if (ROOT / "core").exists() else []:
        mappings.append((path, dest / ".github" / "skills" / path.parent.name / "SKILL.md"))
    for path in sorted((ROOT / ".github" / "skills").glob("*/SKILL.md")):
        mappings.append((path, dest / ".github" / "skills" / path.parent.name / "SKILL.md"))
    for path in sorted((ROOT / ".github" / "agents").glob("*.agent.md")):
        mappings.append((path, dest / ".github" / "agents" / path.name))
    for name in ("decision.md", "flow.md", "quizyouon-changes.md"):
        path = ROOT / "skills" / name
        if path.is_file():
            mappings.append((path, dest / "docs" / "ai-engineer" / name))
    if pack:
        path = ROOT / "packs" / pack / "PACK.md"
        if path.is_file():
            mappings.append((path, dest / "docs" / "ai-engineer" / ("pack-" + pack + ".md")))
    # Duplicate destination only allowed if source content is identical.
    desired = {}
    for source, target in mappings:
        if target in desired and source.read_bytes() != desired[target].read_bytes():
            raise ValueError("Conflicting source packages targeting " + str(target))
        desired[target] = source
    conflicts = [str(p) for p, s in desired.items() if p.exists() and p.read_bytes() != s.read_bytes()]
    if conflicts:
        raise ValueError("Refusing to overwrite modified project files: " + ", ".join(conflicts))
    additions = [p for p in desired if not p.exists()]
    if not dry_run:
        record = dest / ".ai-engineer-install.json"
        if record.exists():
            raise ValueError("Install record already exists; review before modifying")
        for p in additions:
            p.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(desired[p], p)
        hashes = {str(p.relative_to(dest)).replace("\\","/"): hashlib.sha256(p.read_bytes()).hexdigest() for p in desired}
        record.write_text(json.dumps({"pack":pack,"files":hashes},indent=2)+"\n", encoding="utf-8")
    return {"pack":pack or "core","planned_additions":len(additions),"managed_files":len(desired),"dry_run":dry_run}

def main():
    ap=argparse.ArgumentParser(description="AI Engineer Accelerator local CLI")
    sub=ap.add_subparsers(dest="command",required=True)
    search=sub.add_parser("search");search.add_argument("query")
    sub.add_parser("list")
    setup=sub.add_parser("install");setup.add_argument("--project",required=True);setup.add_argument("--pack");setup.add_argument("--dry-run",action="store_true")
    args=ap.parse_args()
    if args.command=="search": result=discover(args.query)
    elif args.command=="list": result=catalog()["scenarios"]
    else: result=install(args.project,args.pack,args.dry_run)
    print(json.dumps(result,indent=2))
if __name__=="__main__":
    main()
