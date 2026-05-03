from dataclasses import dataclass

from .models import Executor, Planner, Synthesizer
from .state import StepStatus, WorkflowState


@dataclass(frozen=True)
class PlanExecuteResult:
    answer: str
    state: WorkflowState


class PlanExecuteAgent:
    def __init__(
        self,
        planner: Planner,
        executor: Executor,
        synthesizer: Synthesizer,
    ) -> None:
        self.planner = planner
        self.executor = executor
        self.synthesizer = synthesizer

    def run(self, goal: str) -> PlanExecuteResult:
        state = WorkflowState(goal=goal, steps=self.planner.create_plan(goal))
        for step in state.steps:
            step.status = StepStatus.RUNNING
            try:
                step.observation = self.executor.execute(step, state.completed_observations())
                step.status = StepStatus.COMPLETED
            except Exception as exc:
                step.status = StepStatus.FAILED
                step.observation = f"failed: {exc}"
                raise

        answer = self.synthesizer.synthesize(goal, state.completed_observations())
        return PlanExecuteResult(answer=answer, state=state)

