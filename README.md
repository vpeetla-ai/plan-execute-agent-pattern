# Plan and Execute Agent Pattern

Production-grade reference implementation of the Plan and Execute pattern for research, reporting, data analysis, and controlled multi-step workflows.

## Highlights

- Planner produces explicit executable steps.
- Executor handles one step at a time.
- Observations are fed back into state.
- Workflow status is inspectable and resumable.

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
python -m plan_execute_agent_pattern
pytest
```

