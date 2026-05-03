from plan_execute_agent_pattern import (
    PlanExecuteAgent,
    ScriptedExecutor,
    ScriptedPlanner,
    ScriptedSynthesizer,
)
from plan_execute_agent_pattern.state import StepStatus


def test_plan_execute_completes_ordered_steps() -> None:
    result = PlanExecuteAgent(
        ScriptedPlanner(),
        ScriptedExecutor(),
        ScriptedSynthesizer(),
    ).run("Write a research brief")

    assert len(result.state.steps) == 3
    assert all(step.status == StepStatus.COMPLETED for step in result.state.steps)
    assert "3 observations" in result.answer

