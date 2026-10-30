# Reliable data pipelines and knowledge models — specialist engineering pack

**Pack:** `data-engineering` · **Status:** original specialist guidance · **Runtime:** uses authorized host tools only.

## Purpose and activation
Select this pack when an AI Engineer works on reliable data pipelines and knowledge models. Combine it with the 18 core skills only as relevant. Do not assume the pack installs frameworks, cloud resources or automatically delegates tasks.

## Inputs to collect
Repository structure and approved scope, actual runtime versions and deployment targets, existing design decisions, security classification, data contracts and test commands. If the request is vague, inspect the application before making assumptions.

## Deep investigation procedure
1. **Environment:** Profile source schemas and data contracts.
2. **Code/data flow:** Design deterministic ingestion with idempotency keys.
3. **Boundaries:** Review incremental loads, CDC, late events and replay logic.
4. **Design/implementation:** Specify data-quality assertions and reject/dead-letter handling.
5. **Resilience:** Trace lineage and schema changes across consumers.
6. **Verification:** Test failure/restart paths, reconciliation and privacy boundaries.
7. **Cross-cutting check:** Identify compatibility, failure modes, rollback and user-impacting regressions.


## Specialist quality bar
- Never process live private rows in public fixtures; anonymize only with approved policy.
- Preserve existing behavior and code conventions unless the change explicitly requires redesign.
- Test invalid inputs, authorization boundaries, empty datasets and partial failures as applicable.
- Report actual tool/test output; otherwise label the result NOT RUN.
- Identify uncertainties in dynamic behavior; never fabricate runtime traces.

## Required outputs
**Lineage map, schema contract, runbook, quality tests and recovery plan.** Present (1) verified findings and source paths, (2) assumptions, (3) solution choices and consequences, (4) changed files or implementation proposal, (5) executed test results, (6) unresolved risks and approval requirements.

## Project-specific boundary
All client source code, proprietary design, access-controlled data, retrieved documents, logs and embeddings stay in the authorized private project environment. No centralized upload to the public accelerator. Production writes and privilege elevation require explicit human approval.

## Example task
An engineer says: 'Review my data-engineering implementation for correctness, security, reliability and maintainability; identify concrete fixes and verify what can safely be tested.' Respond by inspecting project evidence rather than providing a generic checklist.
