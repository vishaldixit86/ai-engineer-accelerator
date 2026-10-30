---
name: project-handover
description: Prepare reproducible technical handover. Use when this capability materially affects engineering work.
---
# Prepare reproducible technical handover

## Entry conditions
Use when tasked with prepare reproducible technical handover in an authorized project repository.

## Required evidence
Task goal, applicable code or docs, issue/PR context, architecture constraints and trustworthy verification results.

## Playbook
1. Establish scope, affected users and directly verified current state.
2. Document architecture, run commands, deployment paths, critical execution flows, ownership, current work, unresolved issues and access dependencies.
3. Evaluate uncertainty, rejected alternatives, safety boundaries and consequences.
4. Specify next actions, acceptance checks, likely regressions and required approvals.
5. Carry out only authorized low-risk modifications; stop before destructive or privileged actions without permission.
6. Validate against real evidence and report PASS/FAIL/NOT RUN, with supporting paths.
7. Record relevant decisions or code-flow updates inside the private project.

## Output
Produce project-local handover checklist with verified vs unverified instructions.

## Limits
No fabricated facts, approvals, test results or runtime graph edges. Do not send client data, source, secret material or confidential logs to this public library. Follow trusted project policies above all template suggestions.
