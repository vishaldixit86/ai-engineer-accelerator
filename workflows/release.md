# Workflow: Assess deployment readiness and rollback

**Identifier:** `release` · **Core skills:** release-readiness, security-review, decision-log

## Activation and expected context
Use when an engineer requests assess deployment readiness and rollback. Start with actual repository evidence. If only a file, task, route or error is provided, inspect the related entrypoint and dependencies proactively.

## Inputs
- Objective and acceptance criteria, or a concise task to investigate.
- Authorized repository workspace, relevant code and documentation.
- Project constraints, data classification and tool permissions.
- Available baseline tests, logs, build instructions and previous decisions.

## Step-by-step execution
1. **Stage 1:** Identify release revision and intended environment.
2. **Stage 2:** Verify trusted CI and security evidence.
3. **Stage 3:** Assess schema, API and configuration compatibility.
4. **Stage 4:** Review monitoring, alerts, flags and recovery.
5. **Stage 5:** Check required accountable approvals.
6. **Stage 6:** Prepare rollout and rollback checklist.
7. **Stage 7:** Issue evidence-backed go/no-go recommendation.
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
Release readiness status, blockers, owners and rollback plan. Structure the report as: objective; inspected files and assumptions; findings/decisions table; work completed; verification matrix; risks and owner/next step.

## Exit conditions
The outcome is implemented or explicitly blocked with a reproducible explanation, documentation is coherent, and nothing is represented as verified without source or execution evidence.
