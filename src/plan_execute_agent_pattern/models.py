from typing import Protocol

from .state import PlanStep


class Planner(Protocol):
    def create_plan(self, goal: str) -> list[PlanStep]:
        """Break a goal into ordered executable steps."""


class Executor(Protocol):
    def execute(self, step: PlanStep, prior_observations: list[str]) -> str:
        """Execute exactly one step."""


class Synthesizer(Protocol):
    def synthesize(self, goal: str, observations: list[str]) -> str:
        """Turn observations into a final result."""


class ScriptedPlanner:
    def create_plan(self, goal: str) -> list[PlanStep]:
        return [
            PlanStep(id="scope", objective=f"Clarify success criteria for: {goal}"),
            PlanStep(id="gather", objective="Collect relevant evidence and constraints"),
            PlanStep(id="synthesize", objective="Produce final recommendation"),
        ]


class ScriptedExecutor:
    def execute(self, step: PlanStep, prior_observations: list[str]) -> str:
        return f"{step.id}: completed {step.objective}"


class ScriptedSynthesizer:
    def synthesize(self, goal: str, observations: list[str]) -> str:
        return f"Final report for '{goal}' based on {len(observations)} observations."

