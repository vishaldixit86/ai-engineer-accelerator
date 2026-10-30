# Azure application and infrastructure design — specialist engineering pack

**Pack:** `azure` · **Status:** original specialist guidance · **Runtime:** uses authorized host tools only.

## Purpose and activation
Select this pack when an AI Engineer works on azure application and infrastructure design. Combine it with the 18 core skills only as relevant. Do not assume the pack installs frameworks, cloud resources or automatically delegates tasks.

## Inputs to collect
Repository structure and approved scope, actual runtime versions and deployment targets, existing design decisions, security classification, data contracts and test commands. If the request is vague, inspect the application before making assumptions.

## Deep investigation procedure
1. **Environment:** Map subscriptions, resource groups, regions and policies.
2. **Code/data flow:** Trace managed identities and Azure RBAC.
3. **Boundaries:** Review network endpoints, key vault integration and configuration.
4. **Design/implementation:** Assess logging, alerts, diagnostics and retention.
5. **Resilience:** Inspect IaC, deployment stages and disaster recovery.
6. **Verification:** Review scalability, quotas and cost visibility.
7. **Cross-cutting check:** Identify compatibility, failure modes, rollback and user-impacting regressions.


## Specialist quality bar
- Prefer project-approved tools; do not assume permission to modify resources.
- Preserve existing behavior and code conventions unless the change explicitly requires redesign.
- Test invalid inputs, authorization boundaries, empty datasets and partial failures as applicable.
- Report actual tool/test output; otherwise label the result NOT RUN.
- Identify uncertainties in dynamic behavior; never fabricate runtime traces.

## Required outputs
**Resource boundary map, identity assessment, deployment checklist, verification.** Present (1) verified findings and source paths, (2) assumptions, (3) solution choices and consequences, (4) changed files or implementation proposal, (5) executed test results, (6) unresolved risks and approval requirements.

## Project-specific boundary
All client source code, proprietary design, access-controlled data, retrieved documents, logs and embeddings stay in the authorized private project environment. No centralized upload to the public accelerator. Production writes and privilege elevation require explicit human approval.

## Example task
An engineer says: 'Review my azure implementation for correctness, security, reliability and maintainability; identify concrete fixes and verify what can safely be tested.' Respond by inspecting project evidence rather than providing a generic checklist.
