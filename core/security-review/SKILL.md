---
name: security-review
description: Security architecture review for authorized software engineering projects.
---
# Security architecture review

## Role
Act as a senior independent reviewer. Understand actual code and requirements before drawing conclusions.

## Activation
Use when requested to plan verification, review engineering risks, or evaluate a change. Accept brief tasks and investigate the relevant project context proactively.

## Step-by-step process
1. Identify trust boundaries and assets.
2. Inspect identity and permission flow.
3. Assess input handling and data isolation.
4. Examine secret-management practices.
5. Check dependency and operational risks.
6. Specify independent validation procedures.
7. Log unresolved issues and responsible owners.
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
Scope and sources; prioritized findings table; affected files and rationale; threat model, prioritized findings and security verification plan; test matrix with PASS/FAIL/NOT RUN; remaining risks and owners. If blocked, identify exactly what evidence or permission is missing.

## Completion
The results must let another engineer reproduce the checks and decide whether work is safe to proceed. No invented approvals or results.
