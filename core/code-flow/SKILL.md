---
name: code-flow
description: Trace verified cross-file execution. Use when this capability materially affects engineering work.
---
# Trace verified cross-file execution

## Entry conditions
Use when tasked with trace verified cross-file execution in an authorized project repository.

## Required evidence
Task goal, applicable code or docs, issue/PR context, architecture constraints and trustworthy verification results.

## Playbook
1. Establish scope, affected users and directly verified current state.
2. Start from a concrete event or route, follow function calls, branches, awaits, exceptions, storage and external services.
3. Evaluate uncertainty, rejected alternatives, safety boundaries and consequences.
4. Specify next actions, acceptance checks, likely regressions and required approvals.
5. Carry out only authorized low-risk modifications; stop before destructive or privileged actions without permission.
6. Validate against real evidence and report PASS/FAIL/NOT RUN, with supporting paths.
7. Record relevant decisions or code-flow updates inside the private project.

## Output
Document ordered file::symbol sequence and label dynamic/unknown edges.

## Limits
No fabricated facts, approvals, test results or runtime graph edges. Do not send client data, source, secret material or confidential logs to this public library. Follow trusted project policies above all template suggestions.
