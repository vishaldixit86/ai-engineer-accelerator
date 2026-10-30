# AWS solution delivery — specialist engineering pack

**Pack:** `aws` · **Status:** original specialist guidance · **Runtime:** uses authorized host tools only.

## Purpose and activation
Select this pack when an AI Engineer works on aws solution delivery. Combine it with the 18 core skills only as relevant. Do not assume the pack installs frameworks, cloud resources or automatically delegates tasks.

## Inputs to collect
Repository structure and approved scope, actual runtime versions and deployment targets, existing design decisions, security classification, data contracts and test commands. If the request is vague, inspect the application before making assumptions.

## Deep investigation procedure
1. **Environment:** Identify account boundaries, regions and workloads.
2. **Code/data flow:** Map IAM principals and service permissions.
3. **Boundaries:** Inspect network isolation, encryption and secret handling.
4. **Design/implementation:** Review infrastructure as code and drift risks.
5. **Resilience:** Evaluate quotas, error handling, disaster recovery and cost controls.
6. **Verification:** Verify observability, deployment and rollback paths.
7. **Cross-cutting check:** Identify compatibility, failure modes, rollback and user-impacting regressions.


## Specialist quality bar
- Use read-only assessment by default; deployment requires permission and cloud-specific credentials.
- Preserve existing behavior and code conventions unless the change explicitly requires redesign.
- Test invalid inputs, authorization boundaries, empty datasets and partial failures as applicable.
- Report actual tool/test output; otherwise label the result NOT RUN.
- Identify uncertainties in dynamic behavior; never fabricate runtime traces.

## Required outputs
**Deployment architecture, IAM review, risk and cost notes, operational checklist.** Present (1) verified findings and source paths, (2) assumptions, (3) solution choices and consequences, (4) changed files or implementation proposal, (5) executed test results, (6) unresolved risks and approval requirements.

## Project-specific boundary
All client source code, proprietary design, access-controlled data, retrieved documents, logs and embeddings stay in the authorized private project environment. No centralized upload to the public accelerator. Production writes and privilege elevation require explicit human approval.

## Example task
An engineer says: 'Review my aws implementation for correctness, security, reliability and maintainability; identify concrete fixes and verify what can safely be tested.' Respond by inspecting project evidence rather than providing a generic checklist.
