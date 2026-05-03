# Local Development Guide

## Current Runtime Behavior

This repo runs locally without LLM or database credentials. The default scripted components are:

- `ScriptedPlanner`
- `ScriptedExecutor`
- `ScriptedSynthesizer`

They demonstrate the production control flow: plan creation, step execution, observation capture, and final synthesis.

## 1. Setup

```bash
cd /Users/lakshmipraveenabodempudi/plan-execute-agent-pattern
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## 2. Run Locally

```bash
python -m plan_execute_agent_pattern
```

No-key smoke run:

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -m plan_execute_agent_pattern
```

Expected behavior:

- Planner creates three ordered steps.
- Executor completes each step.
- Observations are stored in workflow state.
- Synthesizer returns a final report.

## 3. Run Tests

```bash
pytest
```

## 4. Environment Variables

Create a local `.env`:

```bash
cp .env.example .env
```

Important variables:

| Variable | Purpose |
| --- | --- |
| `PLANNER_MODEL` | Model used to decompose the task |
| `EXECUTOR_MODEL` | Model used to execute each step |
| `SYNTHESIZER_MODEL` | Model used for final response |
| `DATABASE_URL` | Durable workflow state |
| `REDIS_URL` | Locks, queues, cache, or short-lived state |
| `ARTIFACT_STORE_URL` | Reports, generated files, datasets |
| `MAX_PLAN_STEPS` | Planning budget |
| `MAX_STEP_RETRIES` | Retry budget per step |
| `ENABLE_STEP_APPROVAL` | Human gate for risky steps |

## 5. Where To Add Real LLM Support

Add provider-backed implementations in:

```text
src/plan_execute_agent_pattern/models.py
```

Implement:

- `Planner`
- `Executor`
- `Synthesizer`

The planner should return structured `PlanStep` objects. Do not allow free-form plans that cannot be resumed or audited.

## 6. Where To Add Database Support

The in-memory state lives in:

```text
src/plan_execute_agent_pattern/state.py
```

Production state should be durable. Recommended tables:

- `workflows`
- `workflow_steps`
- `step_observations`
- `step_artifacts`
- `workflow_events`
- `approval_requests`

Persist after every status transition so a workflow can resume after process failure.

## 7. Production Readiness Checks

- Plan is inspectable before execution.
- Steps have stable IDs.
- Step status transitions are persisted.
- Failed steps are retryable or escalated.
- Re-planning is policy-controlled.
- Cost and latency are tracked per step.

