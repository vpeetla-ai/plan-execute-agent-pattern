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

The default demo uses deterministic planner, executor, and synthesizer stubs, so it runs without external API keys.

For local setup, environment variables, LLM API keys, database configuration, and production adapter guidance, see [docs/LOCAL_DEVELOPMENT.md](docs/LOCAL_DEVELOPMENT.md).

Create your local secret file from:

```bash
cp .env.example .env
```
