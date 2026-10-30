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

# Content depth checks: reject placeholder-length or structurally thin operating guides.
for skill in (ROOT / "core").glob("*/SKILL.md"):
    body = skill.read_text(encoding="utf-8")
    assert len(body) >= 2800, f"Core skill is insufficiently detailed: {skill}"
    assert body.count("## ") >= 7, f"Core skill missing operational sections: {skill}"
    assert "NOT RUN" in body, f"Core skill missing verification honesty: {skill}"
for pack in (ROOT / "packs").glob("*/PACK.md"):
    body = pack.read_text(encoding="utf-8")
    assert len(body) >= 1200, f"Specialist pack needs more detail: {pack}"
    assert "## " in body, f"Specialist pack missing sections: {pack}"
for agent in (ROOT / ".github" / "agents").glob("*.agent.md"):
    body = agent.read_text(encoding="utf-8")
    assert len(body) >= 1800, f"Agent needs senior-level operating detail: {agent}"
    assert "## " in body, f"Agent missing workflow sections: {agent}"
print("Depth checks passed for present core, pack and agent files")
