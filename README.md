# AI Engineer Accelerator

An independent, public engineering toolkit for teams working across multiple technology stacks and client projects.

**Start here:** [20-minute onboarding](docs/START-HERE.md) · [24 scenario catalog](docs/SCENARIOS.md) · [platform blueprint](docs/PLATFORM-ARCHITECTURE.md) · [research benchmark](docs/RESEARCH-BENCHMARK.md).

## Try it locally

```powershell
git clone https://github.com/vishaldixit86/ai-engineer-accelerator.git
cd ai-engineer-accelerator
python scripts/ai_engineer.py search fincrime
python scripts/ai_engineer.py install --project C:\Projects\my-app --pack graphrag --dry-run
python scripts/ai_engineer.py install --project C:\Projects\my-app --pack graphrag
python scripts/validate_catalog.py
python -m unittest discover -s tests -v
```

The project folder must already exist. The installer refuses to overwrite differing files and records the installed files for future reconciliation. It is a local file installer, **not** an autonomous coding runtime.

## Capabilities

- **18 original core skills** in `core/`, each with a provenance manifest
- **7 optional specialist packs** in `packs/`
- **24 scenario mappings** in `catalog.json`
- **AI Engineer agents and governance guides** in `agents/`, `.github/agents/`, and `skills/`
- **Catalog search, installation, metadata checks, and unit tests** in `scripts/` and `tests/`

**Privacy:** Only reusable source assets belong in this public library. Client code, private architecture, customer documents, indexes and project evaluations remain in approved project repositories.

## Maturity

Core skill content is in draft review status. CI validates catalog and basic installer behavior, but security enforcement, autonomous task delegation, production knowledge graphs and assessed delivery improvements are **not implemented**.

---

## Independent framework layout

- `agents/`: orchestrator, architecture, implementation, code-review, testing, security, project-knowledge
- `skills/`: requirements, architecture, development, testing, security, genai, data-engineering, governance
- `workflows/`: understand, design, build, fix, review, test, release, handover
- `platform/`: orchestration, policies, knowledge-graph, evaluation
- `packs/`: opt-in technology packs
- `templates/`, `scripts/`: project adoption and documentation resources
- `third-party/notices/`: license and attribution tracking
- `.github/agents/`, `.github/skills/`, `.github/workflows/`: GitHub/Copilot integrations

### Existing original work preserved
`skills/decision.md`, `skills/flow.md` and `skills/quizyouon-changes.md` are retained. An original Design Coach and `solution-design-coaching` skill have been added. Other agent-domain directories currently document intended responsibilities, not completed agents. The independent agent runtime, enterprise policy enforcement and persistent private knowledge graph remain development milestones.

This public project contains no HVE Core source, and it must not collect client confidential context.
