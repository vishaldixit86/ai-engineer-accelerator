# AI Engineer Accelerator platform blueprint

## Three layers
1. **Core:** 18 portable engineering capabilities and governance.
2. **Optional specialist packs:** Python, React, AWS, Azure, GraphRAG, data engineering, cybersecurity.
3. **Private project context:** files, architecture, source indexes, approval records and outcomes.

## Six platform services
- **Discovery service:** scenario/skill catalog, search and provenance.
- **Installer/distribution:** project-local installation, collisions, pinned source revisions; upgrade PRs are planned.
- **Orchestrator:** task router → specialist plan → approval → execution → verification; runtime adapter is not implemented.
- **Policy service:** independent status checks, human reviews and authorization; document templates alone are not enforcement.
- **Project knowledge:** code AST and call references, ADRs, symbols, provenance, private search. Persistent knowledge graph is planned.
- **Evaluation:** deterministic route checks, synthetic fixtures, agent-tool traces and regression gates; model-based execution is planned.

## Scalability for 100+ engineers
Publish immutable tags and release notes; each project adopts an approved version. Pilot technology packs on representative projects. Provide a compatibility matrix and central catalog but never centralize client source. Use GitHub-protected branches and required checks for code merge policy.

## Security
No default access to write tools or secrets. Explicit boundaries per project. No copy of private context to public systems. Sensitive authorization and production actions require approvals via trusted identity/CI systems, not self-reported JSON.

## Lifecycle
Draft → static validation → fixture evaluation → reviewed release → pilot adoption → monitored rollout → deprecated/replaced.

## Scope today
The catalog, CLI, installer, basic validation/tests and existing Markdown agents are present. This is not yet an autonomous multi-agent system or production enforcement gateway.
