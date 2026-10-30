# React and responsive interface engineering — specialist engineering pack

**Pack:** `react` · **Status:** original specialist guidance · **Runtime:** uses authorized host tools only.

## Purpose and activation
Select this pack when an AI Engineer works on react and responsive interface engineering. Combine it with the 18 core skills only as relevant. Do not assume the pack installs frameworks, cloud resources or automatically delegates tasks.

## Inputs to collect
Repository structure and approved scope, actual runtime versions and deployment targets, existing design decisions, security classification, data contracts and test commands. If the request is vague, inspect the application before making assumptions.

## Deep investigation procedure
1. **Environment:** Inspect route tree, component hierarchy and design tokens.
2. **Code/data flow:** Trace props, state ownership, async loading and conditional rendering.
3. **Boundaries:** Review responsive layouts at narrow, medium and wide viewports.
4. **Design/implementation:** Check keyboard navigation, focus management, semantic markup and screen-reader hints.
5. **Resilience:** Assess empty/loading/error states and performance of rendering.
6. **Verification:** Validate component and interaction tests using project-approved tools.
7. **Cross-cutting check:** Identify compatibility, failure modes, rollback and user-impacting regressions.


## Specialist quality bar
- Test interactions and keyboard flows; check accessibility with authorized tooling and actual browser when available.
- Preserve existing behavior and code conventions unless the change explicitly requires redesign.
- Test invalid inputs, authorization boundaries, empty datasets and partial failures as applicable.
- Report actual tool/test output; otherwise label the result NOT RUN.
- Identify uncertainties in dynamic behavior; never fabricate runtime traces.

## Required outputs
**Component audit, responsive behavior, interaction defects, patch and verification.** Present (1) verified findings and source paths, (2) assumptions, (3) solution choices and consequences, (4) changed files or implementation proposal, (5) executed test results, (6) unresolved risks and approval requirements.

## Project-specific boundary
All client source code, proprietary design, access-controlled data, retrieved documents, logs and embeddings stay in the authorized private project environment. No centralized upload to the public accelerator. Production writes and privilege elevation require explicit human approval.

## Example task
An engineer says: 'Review my react implementation for correctness, security, reliability and maintainability; identify concrete fixes and verify what can safely be tested.' Respond by inspecting project evidence rather than providing a generic checklist.
