from dataclasses import dataclass, field
from enum import StrEnum
from uuid import uuid4


class StepStatus(StrEnum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass
class PlanStep:
    id: str
    objective: str
    status: StepStatus = StepStatus.PENDING
    observation: str | None = None


@dataclass
class WorkflowState:
    goal: str
    steps: list[PlanStep]
    workflow_id: str = field(default_factory=lambda: str(uuid4()))

    def completed_observations(self) -> list[str]:
        return [step.observation for step in self.steps if step.observation]

