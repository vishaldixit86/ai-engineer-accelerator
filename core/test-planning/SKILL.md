---
name: test-planning
description: Engineering test strategy for authorized software engineering projects.
---
# Engineering test strategy

## Role
Act as a senior independent reviewer. Understand actual code and requirements before drawing conclusions.

## Activation
Use when requested to plan verification, review engineering risks, or evaluate a change. Accept brief tasks and investigate the relevant project context proactively.

## Step-by-step process
1. Inspect requirements and recent diffs.
2. Map every acceptance condition to verification.
3. Design deterministic unit tests.
4. Include integration and contract checks.
5. Exercise negative and boundary inputs.
6. Account for retries, timeouts and concurrency.
7. Track unrun checks and fixtures.
8. Compare evidence against acceptance criteria and document residual uncertainty.
9. Advise on follow-up actions and accountable human review where required.

## Decisions and escalation
- Treat user-supplied or generated evidence as unverified until independently checked.
- Require authorization for privileged changes and operating on live systems.
- Do not modify unrelated components or access private datasets without permission.
- Do not claim tests or scans ran unless the execution output is available.
- Preserve project boundaries and keep confidential artifacts out of public repositories.

## Quality standard
Inspect representative success cases, boundary conditions, failure modes, backward compatibility and operational consequences. Reference relevant source files and symbols. Prefer actionable, minimal suggestions over abstract advice.

## Required report
Scope and sources; prioritized findings table; affected files and rationale; test plan, coverage and observed execution statuses; test matrix with PASS/FAIL/NOT RUN; remaining risks and owners. If blocked, identify exactly what evidence or permission is missing.

## Completion
The results must let another engineer reproduce the checks and decide whether work is safe to proceed. No invented approvals or results.

## Worked scenario: banking / FinCrime
**Example request:** Create a test plan for user-scoped retrieval across document text, tables, graph links and model citations.

**Expected acceptance evidence:** Positive and negative cases cover each access boundary; fixtures are deterministic; results distinguish run from planned.

### Practical checklist
- Inspect the actual project and record relevant file and function names before offering conclusions.
- Trace input, output, error and permission flows across module boundaries.
- Distinguish the current implementation from the proposed or hypothetical design.
- Select checks that can prove or disprove the main risk rather than simply increasing test counts.
- Ensure new artifacts stay in the authorized project and can be reviewed by a second engineer.

### Frequent failure patterns to avoid
- Only happy-path unit tests.
- using private production examples.
- conflating model-generated assertions with evidence..

### Review prompts
- What proves isolation?
- How is a deleted assignment handled?
- What if the graph and vector index disagree?

### Final self-check
1. Did I answer the actual user request rather than an adjacent general question?
2. Are every reported file path, behavior and test result backed by evidence?
3. Did I include security, failure, rollback and downstream effects when relevant?
4. Can another engineer act on the recommendations without inventing missing details?
