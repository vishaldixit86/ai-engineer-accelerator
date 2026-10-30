---
name: pull-request
description: Prepare high-signal pull requests. Use when this capability materially affects engineering work.
---
# Prepare high-signal pull requests

## Entry conditions
Use when tasked with prepare high-signal pull requests in an authorized project repository.

## Required evidence
Task goal, applicable code or docs, issue/PR context, architecture constraints and trustworthy verification results.

## Playbook
1. Establish scope, affected users and directly verified current state.
2. Summarize goal, changed contracts, test evidence, risks, decision links, deployment steps and unresolved questions.
3. Evaluate uncertainty, rejected alternatives, safety boundaries and consequences.
4. Specify next actions, acceptance checks, likely regressions and required approvals.
5. Carry out only authorized low-risk modifications; stop before destructive or privileged actions without permission.
6. Validate against real evidence and report PASS/FAIL/NOT RUN, with supporting paths.
7. Record relevant decisions or code-flow updates inside the private project.

## Output
Produce review-ready PR summary with clear NOT RUN statuses and rollback.

## Limits
No fabricated facts, approvals, test results or runtime graph edges. Do not send client data, source, secret material or confidential logs to this public library. Follow trusted project policies above all template suggestions.
