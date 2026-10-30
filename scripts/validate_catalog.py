#!/usr/bin/env python3
"""Validate machine-readable catalog, skill frontmatter and file provenance coverage."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/"catalog.json").read_text(encoding="utf-8"))
assert data["schemaVersion"]=="1.0"
assert len(data["scenarios"])==len({r["id"] for r in data["scenarios"]})
core=set(data["defaultCore"])
packs=set(data["packs"])
for row in data["scenarios"]:
    assert row["id"] and row["title"]
    assert set(row["skills"]).issubset(core),row["id"]
    assert row["pack"]=="core" or row["pack"] in packs,row["id"]
    assert row["clientDataPolicy"]=="project-local"
for f in (ROOT/"core").glob("*/SKILL.md") if (ROOT/"core").exists() else []:
    content=f.read_text(encoding="utf-8")
    assert content.startswith("---\n"),f
    assert "name:" in content.split("---",2)[1],f
    assert "description:" in content.split("---",2)[1],f
    assert (f.parent/"provenance.json").is_file(),f
for f in (ROOT/".github"/"skills").glob("*/SKILL.md"):
    assert f.read_text(encoding="utf-8").startswith("---\n"),f
print("Catalog and available skill packages validated")
