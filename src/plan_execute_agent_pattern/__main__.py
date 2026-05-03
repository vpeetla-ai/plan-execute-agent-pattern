from .engine import PlanExecuteAgent
from .models import ScriptedExecutor, ScriptedPlanner, ScriptedSynthesizer


def main() -> None:
    agent = PlanExecuteAgent(ScriptedPlanner(), ScriptedExecutor(), ScriptedSynthesizer())
    result = agent.run("Evaluate an AI architecture migration")
    print(result.answer)
    for step in result.state.steps:
        print(f"{step.id}: {step.status}")


if __name__ == "__main__":
    main()

