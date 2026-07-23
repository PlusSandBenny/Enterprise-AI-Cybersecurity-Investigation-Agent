# test_planner.py

from cybersecurity_agent.memory.investigation_memory import InvestigationMemory
from cybersecurity_agent.planning.planner import Planner


def test_planner_selects_highest_utility_tool() -> None:
    memory = InvestigationMemory()
    planner = Planner()

    decision = planner.plan(
        goal="Determine account compromise",
        mission="INVESTIGATE",
        memory=memory,
        available_tools=[
            "analyze_device_reputation",
            "analyze_login_history",
            "analyze_location",
        ],
    )

    assert decision.action == "analyze_location"
    assert decision.mission == "INVESTIGATE"


def test_planner_does_not_prioritize_completed_evidence() -> None:
    memory = InvestigationMemory()
    planner = Planner()

    memory.add_evidence(
        "location",
        {
            "risk": "green",
            "score": 10,
            "reason": "Known location",
        },
    )

    decision = planner.plan(
        goal="Determine account compromise",
        mission="INVESTIGATE",
        memory=memory,
        available_tools=[
            "analyze_device_reputation",
            "analyze_login_history",
            "analyze_location",
        ],
    )

    assert decision.action == "analyze_login_history"


def test_planner_returns_no_action_when_no_tools_exist() -> None:
    memory = InvestigationMemory()
    planner = Planner()

    decision = planner.plan(
        goal="Determine account compromise",
        mission="INVESTIGATE",
        memory=memory,
        available_tools=[],
    )

    assert decision.action == "NO_ACTION"