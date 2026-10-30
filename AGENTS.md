# AI Engineer Accelerator — repository instructions

This is an **independent public framework** for use by multiple AI Engineers on separate, authorized projects.

## Operating rules
- Keep private client code, data, generated project knowledge graphs, logs, secrets and identifiers in the client-approved environment; never copy these into this repository.
- Do not import HVE Core files or other third-party agent/skill source without explicit review and applicable licenses.
- Preserve existing `skills/decision.md`, `skills/flow.md`, `skills/quizyouon-changes.md` and document decisions when changes affect compatibility, security, architecture or behavior.
- Any new `SKILL.md` must have meaningful name and description frontmatter, expected outputs, test cases and a provenance record.
- Never claim autonomous multi-agent execution, policy enforcement, or evaluation results without a matching tested integration.
- Do not run destructive operations or touch production data without explicit authorization.
- Validate with `python scripts/validate_catalog.py` and `python -m unittest discover -s tests` before proposing changes.
