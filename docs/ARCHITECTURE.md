# Architecture Decision Record: Plan and Execute Agent Pattern

## Context

Long-running AI work fails when a model tries to solve everything in one turn. Research briefs, data analysis, report generation, migration assessments, and operational runbooks need decomposition, progress visibility, and controlled execution. Plan and Execute separates deciding what should happen from doing each unit of work.

## Decision

This repo implements the pattern with three roles:

1. `Planner` converts a goal into ordered `PlanStep` objects.
2. `Executor` performs one step at a time using prior observations.
3. `Synthesizer` produces the final answer from completed observations.

The orchestrator owns state transitions. This prevents the executor from rewriting the plan invisibly and allows each step to be observed, retried, skipped, or escalated.

## When To Use

Use this pattern for structured multi-step work:

- Deep research.
- Report generation.
- Data analysis.
- Migration planning.
- Workflow automation where each step has a clear objective.

Avoid it for simple Q&A or immediate tool lookup, where ReAct is faster.

## Runtime Flow

```text
Goal
  -> planner creates ordered plan
  -> executor runs step 1
  -> observation saved
  -> executor runs next step
  -> synthesizer creates final answer
```

## State Model

`WorkflowState` stores the goal, steps, statuses, observations, and workflow id. Production systems should persist state after every transition so work can resume after process failure.

Recommended persistent fields:

- Workflow id and tenant id.
- Plan version and planner model metadata.
- Step id, objective, status, retry count, and observation.
- Tool calls and artifacts per step.
- Final synthesis and evaluation score.

## Guardrails

- The executor receives one step, not the whole authority to invent hidden work.
- Each step has an explicit status.
- Observations are separated from final synthesis.
- Failed steps surface through state instead of being buried in a final answer.

Recommended production additions:

- Approval gates before expensive or irreversible steps.
- Checkpointing after each step.
- Per-step budgets for time, cost, and tool calls.
- Re-planning policy when observations invalidate the original plan.
- Artifact storage for generated files and data outputs.

## Failure Modes

- Bad plan: the planner decomposes the task poorly. Mitigation: plan review and re-planning checkpoints.
- Step drift: executor solves a different problem than the step objective. Mitigation: step-level acceptance criteria.
- Partial failure: one step fails after previous work succeeds. Mitigation: resumable state and idempotent execution.
- Over-planning: too many low-value steps. Mitigation: plan length caps and cost-aware planning.

## Scaling Strategy

Run simple workflows in process. For production workloads, store `WorkflowState` in a durable database and execute steps through a queue. The same model maps cleanly to Temporal, durable functions, LangGraph state graphs, Airflow, or a custom orchestrator.

## Success Metrics

- Plan acceptance rate.
- Step completion rate.
- Re-plan frequency.
- Average workflow duration.
- Cost per completed workflow.
- Human intervention rate.
- Final answer acceptance rate.

