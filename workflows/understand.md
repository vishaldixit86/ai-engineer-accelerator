# Workflow: Understand an unfamiliar repository

**Identifier:** `understand` · **Core skills:** project-discovery, code-flow, knowledge-index

## Activation and expected context
Use when an engineer requests understand an unfamiliar repository. Start with actual repository evidence. If only a file, task, route or error is provided, inspect the related entrypoint and dependencies proactively.

## Inputs
- Objective and acceptance criteria, or a concise task to investigate.
- Authorized repository workspace, relevant code and documentation.
- Project constraints, data classification and tool permissions.
- Available baseline tests, logs, build instructions and previous decisions.

## Step-by-step execution
1. **Stage 1:** Locate modules, entrypoints, runtime and test commands.
2. **Stage 2:** Trace key API or event lifecycle across files.
3. **Stage 3:** Identify data dependencies and external integrations.
4. **Stage 4:** Mark unresolved dynamic and runtime paths.
5. **Stage 5:** Document configuration, operational assumptions and owners.
6. **Stage 6:** Check onboarding instructions against actual code.
7. **Stage 7:** Create project-local verified Project Brain.
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
Repository map, architecture snapshot, call-flow references and onboarding checklist. Structure the report as: objective; inspected files and assumptions; findings/decisions table; work completed; verification matrix; risks and owner/next step.

## Exit conditions
The outcome is implemented or explicitly blocked with a reproducible explanation, documentation is coherent, and nothing is represented as verified without source or execution evidence.
