# Contributing original AI Engineer capabilities

Every proposed skill must have an independent purpose, an author, a trigger, required inputs, methodology, output contract, safety boundaries and example evaluation cases.

## Required files
- `skills/<domain>/<skill-name>/SKILL.md` or `core/<skill-name>/SKILL.md`.
- `provenance.json` including origin, license, version, reviewer and tests.
- A synthetic example that uses no proprietary project context.
- Evidence that the intended host supports the chosen skill format.

## Review criteria
Check near-duplicates, language clarity, instructions that grant unsafe permissions, prompt injection surfaces, external dependencies, secret handling, licence provenance and maintainability. Prefer precise capabilities over dozens of overlapping generic skills.

## Quality gates
Run catalog validation, unit tests, security checks and a scenario-specific evaluation. Human review required before public release. Never strip notices from licensed third-party content; if in doubt, independently rewrite or exclude.
