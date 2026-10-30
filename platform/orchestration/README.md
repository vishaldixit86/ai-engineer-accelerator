# Orchestration

Pipeline: task intake → classify → select agents/skills → plan → approval gate → authorized execution → verification → decision/flow updates. The runtime must have explicit tool permissions, idempotent retries, trace IDs, concurrency limits, budgets, and a kill switch. Initial runtime can use deterministic routing; no live delegated execution is implied.
