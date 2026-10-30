# graphrag specialist pack

Status: **design guidance only**. This pack selects task context; it does not automatically install external frameworks, cloud resources or evaluation infrastructure.

## Focus areas
- document extraction and citation provenance
- hybrid retrieval, entity resolution and selective graph construction
- authorization propagation and retrieval/answer evaluation

## Recommended process
1. Inspect the consuming project's stack and actual dependencies.
2. Select applicable core skills; discard irrelevant guidance.
3. Define acceptance criteria, security/privacy obligations and tests for the chosen stack.
4. Require approval for sensitive cloud or data operations; never deploy automatically.
5. Keep client environment data local and preserve evidence in the project repository.

## Example task
Review a proposed graphrag implementation and produce a scoped plan, tradeoffs, security considerations and measured verification criteria.
