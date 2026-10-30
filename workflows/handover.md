# Workflow: Transfer ownership to another engineer

**Identifier:** `handover` · **Core skills:** project-handover, project-discovery, code-flow, documentation

## Activation and expected context
Use when an engineer requests transfer ownership to another engineer. Start with actual repository evidence. If only a file, task, route or error is provided, inspect the related entrypoint and dependencies proactively.

## Inputs
- Objective and acceptance criteria, or a concise task to investigate.
- Authorized repository workspace, relevant code and documentation.
- Project constraints, data classification and tool permissions.
- Available baseline tests, logs, build instructions and previous decisions.

## Step-by-step execution
1. **Stage 1:** Inventory purpose, services and environment.
2. **Stage 2:** Verify build and run commands.
3. **Stage 3:** Trace critical workflows and state boundaries.
4. **Stage 4:** Summarize architectural decisions and known risks.
5. **Stage 5:** Document current work, owners and blockers.
6. **Stage 6:** Explain incident and deployment runbooks.
7. **Stage 7:** Test onboarding narrative for clarity and confidentiality.
8. Check that decisions, code-flow notes and affected documentation match what was actually changed or observed.
9. Provide evidence-backed status and exact next actions if blockers remain.

## Review and escalation rules
- For access-control, customer-data, live-environment, destructive or deployment changes, require accountable human approval before execution.
- Use existing team conventions and minimize unrelated edits.
- Do not claim an agent was delegated to, a tool ran, or tests passed without execution evidence.
- Record unresolved hypotheses and design alternatives rather than silently selecting an irreversible option.
- Do not transmit client source, logs, secrets, knowledge graphs or restricted diagrams into this public repository.

## Verification checklist
- [ ] Project context and relevant files verified.
- [ ] Scope and expected user behavior described.
- [ ] Impacted interfaces, storage, tests and permissions considered.
- [ ] Changes or advice align with actual evidence.
- [ ] Tests recorded PASS, FAIL or NOT RUN with exact commands.
- [ ] Risks, rollback and external dependencies recorded if applicable.
- [ ] Project-local decision and flow guides updated when material.

## Required handoff artifact
Private Project Brain, call flows, decisions, runbook and unresolved work. Structure the report as: objective; inspected files and assumptions; findings/decisions table; work completed; verification matrix; risks and owner/next step.

## Exit conditions
The outcome is implemented or explicitly blocked with a reproducible explanation, documentation is coherent, and nothing is represented as verified without source or execution evidence.
