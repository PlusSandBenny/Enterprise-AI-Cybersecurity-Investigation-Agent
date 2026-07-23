# planner.py

from dataclasses import dataclass

from cybersecurity_agent.memory.investigation_memory import InvestigationMemory
from cybersecurity_agent.planning.utility import rank_tools


@dataclass(frozen=True)
class PlanDecision:
    action: str
    reason: str
    mission: str


class Planner:
    def plan(
        self,
        goal: str,
        mission: str,
        memory: InvestigationMemory,
        available_tools: list[str],
    ) -> PlanDecision:
        if not available_tools:
            return PlanDecision(
                action="NO_ACTION",
                reason="No tools are currently available",
                mission=mission,
            )

        ranked_tools = rank_tools(
            tools=available_tools,
            memory=memory,
        )

        selected_tool = ranked_tools[0]

        return PlanDecision(
            action=selected_tool,
            reason=(
                f"Selected the tool with the highest utility "
                f"for goal '{goal}' under mission '{mission}'"
            ),
            mission=mission,
        )