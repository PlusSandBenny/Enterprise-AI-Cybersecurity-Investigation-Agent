# orchestrator.py

from cybersecurity_agent.memory.investigation_memory import (
    InvestigationMemory,
)
from cybersecurity_agent.planning.mission_manager import (
    MissionManager,
)
from cybersecurity_agent.planning.planner import (
    PlanDecision,
    Planner,
)


class Orchestrator:
    def __init__(
        self,
        planner: Planner,
        mission_manager: MissionManager,
        memory: InvestigationMemory,
    ) -> None:
        self._planner = planner
        self._mission_manager = mission_manager
        self._memory = memory

    def run(
        self,
        goal: str,
        available_tools: list[str],
    ) -> PlanDecision:
        mission = self._mission_manager.get_current_mission(
            self._memory
        )

        decision = self._planner.plan(
            goal=goal,
            mission=mission,
            memory=self._memory,
            available_tools=available_tools,
        )

        self._memory.add_decision_log(
            f"Planner selected action '{decision.action}' "
            f"under mission '{decision.mission}': "
            f"{decision.reason}"
        )

        return decision