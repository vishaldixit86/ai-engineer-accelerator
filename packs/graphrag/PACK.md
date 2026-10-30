# GenAI RAG and GraphRAG engineering — specialist engineering pack

**Pack:** `graphrag` · **Status:** original specialist guidance · **Runtime:** uses authorized host tools only.

## Purpose and activation
Select this pack when an AI Engineer works on genai rag and graphrag engineering. Combine it with the 18 core skills only as relevant. Do not assume the pack installs frameworks, cloud resources or automatically delegates tasks.

## Inputs to collect
Repository structure and approved scope, actual runtime versions and deployment targets, existing design decisions, security classification, data contracts and test commands. If the request is vague, inspect the application before making assumptions.

## Deep investigation procedure
1. **Environment:** Inspect source documents and permitted data classifications.
2. **Code/data flow:** Evaluate OCR extraction, tables and metadata provenance.
3. **Boundaries:** Design chunking with source/page lineage and access metadata.
4. **Design/implementation:** Review embedding, hybrid search and reranking tradeoffs.
5. **Resilience:** Define ontology, entity resolution and selective graph construction.
6. **Verification:** Trace question-to-retrieval-to-tool-to-answer paths.
7. **Reporting:** Evaluate citations, retrieval recall, groundedness, latency, cost and case-level authorization.


## Specialist quality bar
- Never expose restricted documents; test cross-case access and prompt injection in authorized synthetic environments.
- Preserve existing behavior and code conventions unless the change explicitly requires redesign.
- Test invalid inputs, authorization boundaries, empty datasets and partial failures as applicable.
- Report actual tool/test output; otherwise label the result NOT RUN.
- Identify uncertainties in dynamic behavior; never fabricate runtime traces.

## Required outputs
**Ingestion lineage, retrieval architecture, graph model, permission map and evaluation suite.** Present (1) verified findings and source paths, (2) assumptions, (3) solution choices and consequences, (4) changed files or implementation proposal, (5) executed test results, (6) unresolved risks and approval requirements.

## Project-specific boundary
All client source code, proprietary design, access-controlled data, retrieved documents, logs and embeddings stay in the authorized private project environment. No centralized upload to the public accelerator. Production writes and privilege elevation require explicit human approval.

## Example task
An engineer says: 'Review my graphrag implementation for correctness, security, reliability and maintainability; identify concrete fixes and verify what can safely be tested.' Respond by inspecting project evidence rather than providing a generic checklist.
