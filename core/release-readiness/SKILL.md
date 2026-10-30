---
name: release-readiness
description: Evaluate whether a release can safely proceed. Use when this capability materially affects engineering work.
---
# Evaluate whether a release can safely proceed

## Entry conditions
Use when tasked with evaluate whether a release can safely proceed in an authorized project repository.

## Required evidence
Task goal, applicable code or docs, issue/PR context, architecture constraints and trustworthy verification results.

## Playbook
1. Establish scope, affected users and directly verified current state.
2. Check branch protection, actual CI status, risk assessment, dependencies, migrations, observability, SLOs, operator runbooks and approvals.
3. Evaluate uncertainty, rejected alternatives, safety boundaries and consequences.
4. Specify next actions, acceptance checks, likely regressions and required approvals.
5. Carry out only authorized low-risk modifications; stop before destructive or privileged actions without permission.
6. Validate against real evidence and report PASS/FAIL/NOT RUN, with supporting paths.
7. Record relevant decisions or code-flow updates inside the private project.

## Output
Return BLOCK, CONDITIONAL or PASS only with verifiable evidence; never deploy on its own.

## Limits
No fabricated facts, approvals, test results or runtime graph edges. Do not send client data, source, secret material or confidential logs to this public library. Follow trusted project policies above all template suggestions.
