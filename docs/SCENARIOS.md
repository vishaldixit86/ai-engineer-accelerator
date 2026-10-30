# Scenario playbooks — AI Engineer Accelerator

Use the [machine-readable catalog](../catalog.json) to discover all 24 scenarios. Choose a scenario, inspect the target project, and select only relevant core capabilities and an optional specialist pack.

## Engineering workflow
1. **Intake:** capture outcome, acceptance criteria, stakeholders and security classification.
2. **Context:** read actual project code, test commands, APIs, dependencies, and design notes.
3. **Route:** identify the needed skills/agents, approval gates and test plan.
4. **Plan:** compare approaches; record assumptions, risks and test evidence requirements.
5. **Execute:** only authorized changes, preferably in feature branches.
6. **Validate:** tests, static checks, threat or access reviews and measurable evaluation.
7. **Handover:** decision log, verified call flow, PR evidence and remaining risks.

## Representative project journeys

### FinCrime / GraphRAG
- Input: SAR/KYC, email, cases, evidence documents (approved synthetic data for shared examples).
- Define provenance and access labels at ingestion and propagate through chunks, indexes, graph nodes, agent tools and citations.
- Create extraction fixtures with scanned tables, multi-column layout and duplications.
- Evaluate text extraction, entity resolution, hybrid retrieval, authorization bypass attempts, grounded answers, cost and latency.
- Keep investigation data and access-controlled graph inside the client project. No central upload.

### Existing banking API
- Inspect current code and contracts, generate a call map, propose change with blast-radius analysis.
- Implement API compatibility and authorization tests; review exceptions, retries and migrations.
- Produce PR, decision and handover notes with actual evidence.

### Production issue
- Reconstruct a chronology from approved logs and deployment events; isolate hypotheses.
- Require human approval for operational actions, test rollback and document remediation.
- Never fabricate root cause or treat missing observability as passed testing.

## Coverage and quality
Every scenario should eventually have: a runnable synthetic sample, expected outcomes, negative tests, approval requirements, supported tools, maintenance owner and review date. The catalog intentionally separates *catalogued* from *implemented* and *verified*.
