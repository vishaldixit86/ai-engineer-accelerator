# Workflow: Build a feature

## Trigger
Use when asked to implement a feature in an authorized project.

## Preparation
Inspect requirements, current source, build commands, active interfaces, dependencies and tests. Identify acceptance criteria and potential impact on users or other components.

## Execution sequence
1. Find the relevant code paths and current tests.
2. Write a narrowly scoped implementation plan.
3. Check compatibility and security boundaries.
4. Obtain approval before sensitive or irreversible changes.
5. Implement the minimal coherent change.
6. Add focused success and failure tests.
7. Run project-supported checks and capture real outcomes.
8. Update code-flow and decision records where appropriate.
9. Draft review-ready change summary and handoff.

## Decision rules
Do not expand scope silently. Preserve existing behavior unless requirements explicitly change it. If project tools are unavailable, provide a precise implementation plan and mark checks NOT RUN rather than claiming success.

## Completion report
Objective; inspected source and contracts; changes made or blocked; tests with PASS/FAIL/NOT RUN; remaining issues; rollback and next actions.
