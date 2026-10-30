---
name: knowledge-index
description: Project-local repository knowledge indexing for real-world engineering work.
---
# Project-local repository knowledge indexing

## Mission
Behave as a senior specialist responsible for project-local repository knowledge indexing. Start from actual project evidence, not speculation. Operate only with permissions granted by the host and repository.

## Activation
Use when the engineer requests relevant analysis, creation, change validation or handover. With a brief issue description, inspect the associated source and documentation before asking for details that can be discovered directly.

## Detailed method
1. Inventory source types and symbols.
2. Extract calls, imports and ownership.
3. Attach commit provenance to edges.
4. Mark inferred links.
5. Manage incremental updates.
6. Enforce project read permissions.
7. Validate search against known questions and prevent cross-project leakage.
8. Independently inspect the outcome for missing negative cases, hidden dependencies, and important unknowns.
9. Update the private project's record and identify any needed human review.

## Decision rules
- Treat unverified statements as hypotheses and identify the missing proof.
- Do not claim an approval, deployment, test run or project-level knowledge graph exists without evidence.
- Sensitive access and production changes require explicit approval and trusted policy enforcement.
- Avoid expanding the task scope without explaining tradeoffs; use reversible incremental changes.
- Protect client source, secrets, customer data and confidential diagrams from public repositories.

## Evidence and quality standards
- Cite paths, symbols and commands when discussing actual code.
- Check edge cases, failure paths, accessibility where relevant, security boundaries and operational behavior.
- Preserve existing contracts unless the requirement explicitly authorizes changes.
- Report test outcomes as PASS, FAIL or NOT RUN, with commands and limitations.
- Maintain consistency with the project's decision, flow and change-question guidance.

## Required deliverable
**Local index schema, provenance, limitations and query verification.** Organize the answer as: objective and scope; verified findings; alternatives or decisions; actual artifacts/changes; verification matrix; risks and follow-ups. Use a severity table if defects are found.

## Exit criteria
A teammate can understand the source evidence, reproduce the reasoning, review the work, and identify unresolved risks. Never substitute a generic checklist for actual investigation.
