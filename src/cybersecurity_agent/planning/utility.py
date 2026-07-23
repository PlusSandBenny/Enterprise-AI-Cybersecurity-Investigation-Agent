# utility.py

from cybersecurity_agent.memory.investigation_memory import InvestigationMemory
from cybersecurity_agent.planning.information_gain import expected_gain


TOOL_COST = {
    "analyze_failed_logins": 1.0,
    "analyze_location": 1.0,
    "analyze_login_history": 2.0,
    "analyze_device_reputation": 10.0,
}


def calculate_utility(
    tool: str,
    memory: InvestigationMemory,
) -> float:
    try:
        cost = TOOL_COST[tool]
    except KeyError as error:
        raise ValueError(
            f"No cost value exists for tool: {tool}"
        ) from error

    if cost <= 0:
        raise ValueError(
            f"Tool cost must be greater than zero: {tool}"
        )

    gain = expected_gain(tool, memory)

    return gain / cost


def rank_tools(
    tools: list[str],
    memory: InvestigationMemory,
) -> list[str]:
    return sorted(
        tools,
        key=lambda tool: calculate_utility(tool, memory),
        reverse=True,
    )